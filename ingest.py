"""Indexe les PDFs de drive_archive dans le vector store Chroma.

Utilisation :
    python ingest.py                    # indexe TOUTES les matières
    python ingest.py --subject svt      # indexe uniquement SVT
    python ingest.py --reset            # vide d'abord la collection

Le script est ré-entrant : un PDF déjà indexé (même mtime + même taille) n'est
pas recalculé. Pour forcer la ré-indexation : --reset.
"""

from __future__ import annotations

import argparse
import hashlib
import logging
import sys
import time
from pathlib import Path
from typing import Optional

import chromadb
import fitz  # PyMuPDF
from dotenv import load_dotenv
from openai import OpenAI

from common import (
    SUBJECTS,
    classify_pdf,
    get_env,
    iter_pdfs,
    normalize_text,
    split_text,
)

# ─── Configuration ──────────────────────────────────────────────────────────

EMBED_MODEL = "text-embedding-3-small"
EMBED_DIM = 1536  # dimension de text-embedding-3-small
EMBED_BATCH = 100  # OpenAI accepte jusqu'à 2048, 100 est un bon compromis

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("ingest")


# ─── Helpers ────────────────────────────────────────────────────────────────


def pdf_fingerprint(path: Path) -> str:
    """Empreinte stable d'un PDF : taille + mtime. Évite de relire des Mo
    pour décider si on doit ré-indexer."""
    st = path.stat()
    return f"{st.st_size}-{int(st.st_mtime)}"


def extract_pages(path: Path) -> list[tuple[int, str]]:
    """Retourne [(page_num, text), ...] pour les pages contenant du texte
    natif. Skip silencieusement les pages 100 % scannées (où get_text renvoie
    une chaîne vide ou quasi vide) — la prise en charge OCR scannée sera
    ajoutée plus tard si besoin.
    """
    out: list[tuple[int, str]] = []
    try:
        doc = fitz.open(path)
    except Exception as e:
        log.warning("Impossible d'ouvrir %s : %s", path.name, e)
        return out
    try:
        for i, page in enumerate(doc, start=1):
            try:
                txt = page.get_text("text") or ""
            except Exception:
                continue
            txt = normalize_text(txt)
            if len(txt) >= 80:  # seuil minimal pour éviter les pages bruit
                out.append((i, txt))
    finally:
        doc.close()
    return out


def chunk_id(subject: str, pdf_path: Path, page: int, idx: int) -> str:
    """ID unique et stable pour un chunk (permet upsert idempotent)."""
    rel = pdf_path.name
    raw = f"{subject}|{rel}|{page}|{idx}"
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:24]


def embed_batch(client: OpenAI, texts: list[str]) -> list[list[float]]:
    """Calcule les embeddings d'un batch avec retry simple."""
    last_err: Optional[Exception] = None
    for attempt in range(3):
        try:
            resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
            return [d.embedding for d in resp.data]
        except Exception as e:  # pragma: no cover (réseau)
            last_err = e
            wait = 2 ** attempt
            log.warning("Embedding batch failed (attempt %d) : %s — retry in %ds", attempt + 1, e, wait)
            time.sleep(wait)
    raise RuntimeError(f"Échec embeddings après 3 tentatives : {last_err}")


# ─── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--subject",
        choices=SUBJECTS,
        help="Limiter l'indexation à une matière",
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Vide la collection avant de réindexer",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Liste les PDFs et chunks qui SERAIENT indexés, sans appel API",
    )
    args = parser.parse_args()

    load_dotenv()
    pdf_root = Path(get_env("RAG_PDF_ROOT")).resolve()
    chroma_dir = Path(get_env("RAG_CHROMA_DIR")).resolve()
    chroma_dir.mkdir(parents=True, exist_ok=True)

    log.info("PDF root : %s", pdf_root)
    log.info("Chroma   : %s", chroma_dir)

    client = OpenAI(api_key=get_env("OPENAI_API_KEY")) if not args.dry_run else None

    chroma = chromadb.PersistentClient(path=str(chroma_dir))
    coll = chroma.get_or_create_collection(
        name="bac_corpus",
        metadata={"hnsw:space": "cosine"},
    )

    if args.reset:
        log.warning("Reset : suppression de la collection bac_corpus")
        chroma.delete_collection("bac_corpus")
        coll = chroma.get_or_create_collection(
            name="bac_corpus",
            metadata={"hnsw:space": "cosine"},
        )

    # Index : fingerprints des PDFs déjà ingérés (pour ré-entrance)
    existing_fingerprints: set[str] = set()
    try:
        existing = coll.get(include=["metadatas"], limit=100_000)
        for md in existing.get("metadatas") or []:
            fp = md.get("fingerprint") if md else None
            if fp:
                existing_fingerprints.add(fp)
    except Exception:
        pass

    total_pdfs = 0
    total_chunks_added = 0
    total_chunks_skipped = 0
    by_subject: dict[str, int] = {s: 0 for s in SUBJECTS}

    for pdf_path in iter_pdfs(pdf_root):
        subject = classify_pdf(pdf_path)
        if subject is None:
            continue
        if args.subject and subject != args.subject:
            continue
        total_pdfs += 1

        fp = pdf_fingerprint(pdf_path)
        pdf_key = f"{subject}|{pdf_path.name}|{fp}"
        if pdf_key in existing_fingerprints:
            log.info("[skip] %s (déjà indexé)", pdf_path.name)
            continue

        pages = extract_pages(pdf_path)
        if not pages:
            log.info("[skip] %s (aucun texte natif — scanné ?)", pdf_path.name)
            continue

        # Pour chaque page → chunks → batch embeddings → upsert
        batch_ids: list[str] = []
        batch_docs: list[str] = []
        batch_metas: list[dict] = []

        chunk_count_this_pdf = 0
        for page_num, page_text in pages:
            chunks = split_text(page_text)
            for j, chunk in enumerate(chunks):
                cid = chunk_id(subject, pdf_path, page_num, j)
                batch_ids.append(cid)
                batch_docs.append(chunk)
                batch_metas.append(
                    {
                        "subject": subject,
                        "source": pdf_path.name,
                        "page": page_num,
                        "fingerprint": pdf_key,
                    }
                )
                chunk_count_this_pdf += 1

        if not batch_docs:
            continue

        if args.dry_run:
            log.info("[dry-run] %s → %d chunks (%s)", pdf_path.name, len(batch_docs), subject)
            total_chunks_added += len(batch_docs)
            by_subject[subject] += len(batch_docs)
            continue

        log.info(
            "Indexing %s → %d chunks (%s)", pdf_path.name, len(batch_docs), subject
        )
        # Embeddings par mini-batchs
        all_embeddings: list[list[float]] = []
        for k in range(0, len(batch_docs), EMBED_BATCH):
            sub = batch_docs[k : k + EMBED_BATCH]
            all_embeddings.extend(embed_batch(client, sub))

        # Upsert atomique pour ce PDF
        coll.upsert(
            ids=batch_ids,
            documents=batch_docs,
            metadatas=batch_metas,
            embeddings=all_embeddings,
        )
        total_chunks_added += chunk_count_this_pdf
        by_subject[subject] += chunk_count_this_pdf

    log.info("─" * 60)
    log.info("PDFs scannés        : %d", total_pdfs)
    log.info("Chunks ajoutés      : %d", total_chunks_added)
    log.info("Chunks skip (cache) : %d", total_chunks_skipped)
    for s, n in by_subject.items():
        if n > 0:
            log.info("  %-10s : %d chunks", s, n)
    log.info(
        "Total dans la collection : %d", coll.count() if not args.dry_run else "n/a"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
