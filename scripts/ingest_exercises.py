#!/usr/bin/env python3
"""Indexe les exercices structurés (json_bac.json source_extraction=vision) dans Chroma.

Stratégie de chunking :
  - 1 chunk = 1 sous-question FEUILLE (la plus profonde dans l'arbre)
  - Le texte du chunk inclut le préambule de l'exo + l'énoncé de la question parente
    + l'énoncé de la sous-question, pour donner du contexte au retrieval.
  - Pour les exos sans structure (QCMs notamment), 1 chunk = l'énoncé complet.

Métadonnées par chunk (riche pour filtrage) :
  source_type:    "exercise_v2"  (vs "pdf_page" pour l'ancien ingest.py)
  ex_id:          "bac-c-2024-sn-math-ex1"
  matiere_id:     math | pc | svt
  filiere_id:     C | D
  annee:          2024
  session:        Normale | Complémentaire
  chapitre:       "Cinétique chimique"
  notion_ids:     "pc.cinetique.trempe,pc.cinetique.dosage-i2"  (CSV — Chroma n'aime pas les listes)
  question_path:  "1.2.3"  (chemin numérique vers la feuille)
  has_correction: bool

Usage :
  python scripts/ingest_exercises.py --dry-run                  # voir ce qui serait fait
  python scripts/ingest_exercises.py --matiere math             # une seule matière
  python scripts/ingest_exercises.py                            # tout indexer
  python scripts/ingest_exercises.py --reset-source-type        # supprimer les chunks
                                                                # exercise_v2 avant
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any, Iterable

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from common import get_env  # noqa: E402

EMBED_MODEL = "text-embedding-3-small"
EMBED_BATCH = 100
COLLECTION = "bac_corpus"
SOURCE_TYPE = "exercise_v2"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("ingest_exercises")


# ─── Chunking ───────────────────────────────────────────────────────────────


def iter_leaves(
    node: dict[str, Any],
    path: list[str],
    ancestors: list[tuple[str, str]],
) -> Iterable[tuple[str, list[tuple[str, str]]]]:
    """Yield (path_str, ancestors[]) pour chaque feuille de l'arbre.

    ancestors = liste de (numero, enonce) des ancêtres (préambule exclus).
    """
    sub = node.get("sous_questions") or []
    cur_path = path + [str(node.get("numero", "?"))]
    cur_ancestors = ancestors + [(str(node.get("numero", "?")), (node.get("enonce") or "").strip())]
    if not sub:
        yield ".".join(cur_path), cur_ancestors
    else:
        for child in sub:
            yield from iter_leaves(child, cur_path, cur_ancestors)


def build_chunks(ex: dict[str, Any]) -> list[dict[str, Any]]:
    """Retourne une liste de {text, question_path} pour un exo."""
    structure = ex.get("enonce_structure") or {}
    questions = structure.get("questions") or []
    preambule = (structure.get("preambule") or "").strip()
    flat_enonce = (ex.get("ennonce_complet") or "").strip()

    # Fallback : pas de structure → 1 chunk = enonce plat
    if not questions:
        if not flat_enonce:
            return []
        return [{"text": flat_enonce, "question_path": ""}]

    chunks: list[dict[str, Any]] = []
    for q in questions:
        for path_str, ancestors in iter_leaves(q, [], []):
            parts: list[str] = []
            if preambule:
                parts.append(f"Préambule : {preambule}")
            # Ancêtres : la question principale (Q1) puis intermédiaires
            for i, (num, enonce) in enumerate(ancestors[:-1]):
                if enonce:
                    parts.append(f"Q{num} : {enonce}")
            # La feuille
            num, enonce = ancestors[-1]
            if enonce:
                parts.append(f"Q{path_str} : {enonce}")
            text = "\n".join(p for p in parts if p)
            if text.strip():
                chunks.append({"text": text, "question_path": path_str})
    return chunks


def chunk_id(ex_id: str, question_path: str) -> str:
    raw = f"{ex_id}|{question_path}"
    return "ex_" + hashlib.sha1(raw.encode("utf-8")).hexdigest()[:20]


def chunk_metadata(ex: dict[str, Any], question_path: str) -> dict[str, Any]:
    # Chroma n'accepte pas les listes dans metadata, on sérialise notion_ids
    notion_ids = ex.get("notion_ids") or []
    return {
        "source_type": SOURCE_TYPE,
        "ex_id": ex["id"],
        "matiere_id": ex.get("matiere_id", ""),
        "filiere_id": ex.get("filiere_id", ""),
        "annee": int(ex.get("annee") or 0),
        "session": ex.get("session", ""),
        "chapitre": ex.get("chapitre", "") or "",
        "notion_ids": ",".join(notion_ids),
        "question_path": question_path,
        "has_correction": bool((ex.get("correction") or "").strip()),
        "source_file": ex.get("fichier", ""),
    }


# ─── Embeddings ─────────────────────────────────────────────────────────────


def embed_batch(client: OpenAI, texts: list[str]) -> list[list[float]]:
    last_err = None
    for attempt in range(3):
        try:
            resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
            return [d.embedding for d in resp.data]
        except Exception as e:
            last_err = e
            wait = 2 ** attempt
            log.warning("Embed batch failed (try %d): %s — retry in %ds", attempt + 1, e, wait)
            time.sleep(wait)
    raise RuntimeError(f"Embed failed: {last_err}")


# ─── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=str(ROOT / "json_bac.json"))
    ap.add_argument("--matiere", choices=["math", "pc", "svt"])
    ap.add_argument("--filiere", choices=["C", "D"])
    ap.add_argument(
        "--all-vision",
        action="store_true",
        default=True,
        help="N'indexer que les exos source_extraction=vision (défaut)",
    )
    ap.add_argument(
        "--include-legacy",
        action="store_true",
        help="Indexer aussi les exos legacy (sans enonce_structure)",
    )
    ap.add_argument("--reset-source-type", action="store_true",
                    help="Supprime tous les chunks exercise_v2 existants avant ingestion")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, help="Limiter à N exercices (test)")
    args = ap.parse_args()

    if args.include_legacy:
        args.all_vision = False

    data = json.loads(Path(args.json).read_text(encoding="utf-8"))
    log.info("Chargé %d exos depuis %s", len(data), args.json)

    # Filtres
    if args.all_vision:
        data = [e for e in data if e.get("source_extraction") == "vision"]
    if args.matiere:
        data = [e for e in data if e.get("matiere_id") == args.matiere]
    if args.filiere:
        data = [e for e in data if e.get("filiere_id") == args.filiere]
    if args.limit:
        data = data[: args.limit]

    log.info("Après filtres : %d exos à indexer", len(data))

    # Build chunks
    all_chunks: list[tuple[dict, dict[str, Any]]] = []  # (ex, chunk_dict)
    n_no_chunks = 0
    for ex in data:
        chunks = build_chunks(ex)
        if not chunks:
            n_no_chunks += 1
            continue
        for c in chunks:
            all_chunks.append((ex, c))

    log.info("Chunks générés : %d (exos sans chunk : %d)", len(all_chunks), n_no_chunks)

    # Dédup par chunk_id (cas : deux sous-questions de même numero sous le même
    # parent → même question_path → même chunk_id). On garde le texte le plus
    # long (plus de contexte) parmi les doublons.
    dedup: dict[str, tuple[dict, dict[str, Any]]] = {}
    n_dropped = 0
    for ex, c in all_chunks:
        cid = chunk_id(ex["id"], c["question_path"])
        prev = dedup.get(cid)
        if prev is None or len(c["text"]) > len(prev[1]["text"]):
            if prev is not None:
                n_dropped += 1
            dedup[cid] = (ex, c)
        else:
            n_dropped += 1
    if n_dropped:
        log.warning("Dédup : %d chunks doublons écartés (collision de question_path)", n_dropped)
    all_chunks = list(dedup.values())
    log.info("Chunks uniques après dédup : %d", len(all_chunks))

    if args.dry_run:
        from collections import Counter
        by_matiere = Counter(ex.get("matiere_id") for ex, _ in all_chunks)
        log.info("Par matière :")
        for m, n in sorted(by_matiere.items()):
            log.info("  %s : %d chunks", m, n)
        # Échantillon
        if all_chunks:
            ex, c = all_chunks[0]
            log.info("\n=== Échantillon (1er chunk) ===")
            log.info("ID    : %s", chunk_id(ex["id"], c["question_path"]))
            log.info("Meta  : %s", chunk_metadata(ex, c["question_path"]))
            log.info("Texte :\n%s", c["text"][:500] + ("..." if len(c["text"]) > 500 else ""))
        log.info("\n[DRY-RUN] aucun embedding calculé.")
        return 0

    # Connect to Chroma
    chroma_dir = Path(get_env("RAG_CHROMA_DIR")).resolve()
    chroma_dir.mkdir(parents=True, exist_ok=True)
    chroma = chromadb.PersistentClient(path=str(chroma_dir))
    coll = chroma.get_or_create_collection(
        name=COLLECTION,
        metadata={"hnsw:space": "cosine"},
    )

    if args.reset_source_type:
        log.warning("Suppression des chunks existants avec source_type=%s", SOURCE_TYPE)
        try:
            coll.delete(where={"source_type": SOURCE_TYPE})
            log.info("  → suppression OK")
        except Exception as e:
            log.warning("  → suppression échouée (%s), on continue", e)

    client = OpenAI(api_key=get_env("OPENAI_API_KEY"))

    # Batch embed + upsert
    BATCH = EMBED_BATCH
    total_added = 0
    for start in range(0, len(all_chunks), BATCH):
        batch = all_chunks[start : start + BATCH]
        texts = [c["text"] for _, c in batch]
        ids = [chunk_id(ex["id"], c["question_path"]) for ex, c in batch]
        metas = [chunk_metadata(ex, c["question_path"]) for ex, c in batch]

        embeddings = embed_batch(client, texts)
        coll.upsert(ids=ids, documents=texts, metadatas=metas, embeddings=embeddings)
        total_added += len(batch)
        log.info("Upsert batch %d-%d (total %d/%d)",
                 start, start + len(batch), total_added, len(all_chunks))

    log.info("─" * 50)
    log.info("Terminé : %d chunks indexés dans collection '%s' (source_type=%s)",
             total_added, COLLECTION, SOURCE_TYPE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
