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
from vision_ocr import get_groq_client, ocr_page_via_vision

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


def extract_pages(path: Path, use_vision: bool = True) -> list[tuple[int, str]]:
    """Retourne [(page_num, text), ...].

    Pour chaque page : (1) tente le texte natif via PyMuPDF, (2) si la page
    semble scannée (< 80 caractères extraits), tente Groq Vision OCR si
    disponible (clé GROQ_API_KEY présente).

    Une page sans texte natif ET sans OCR (clé absente ou OCR échoué) est
    skippée silencieusement.
    """
    out: list[tuple[int, str]] = []
    try:
        doc = fitz.open(path)
    except Exception as e:
        log.warning("Impossible d'ouvrir %s : %s", path.name, e)
        return out
    n_vision = 0
    try:
        for i, page in enumerate(doc, start=1):
            try:
                txt = page.get_text("text") or ""
            except Exception:
                continue
            txt = normalize_text(txt)
            if len(txt) >= 80:
                out.append((i, txt))
                continue
            if not use_vision:
                continue
            # Page scannée → tentative OCR Vision
            ocr_text = ocr_page_via_vision(page)
            if ocr_text:
                out.append((i, normalize_text(ocr_text)))
                n_vision += 1
    finally:
        doc.close()
    if n_vision > 0:
        log.info("  ↳ %d page(s) extraites via Vision OCR", n_vision)
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
    parser.add_argument(
        "--no-vision",
        action="store_true",
        help="Désactive l'OCR Vision sur les PDFs scannés (skip silencieux)",
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
        subjects_matched = classify_pdf(pdf_path)
        if not subjects_matched:
            continue
        if args.subject:
            if args.subject not in subjects_matched:
                continue
            subjects_matched = [args.subject]
        total_pdfs += 1

        fp = pdf_fingerprint(pdf_path)
        # Une "fingerprint" unique englobe tous les sujets : si le PDF a été
        # indexé pour tous, on saute. Sinon on (ré)indexe.
        pdf_key = f"{'+'.join(sorted(subjects_matched))}|{pdf_path.name}|{fp}"
        if pdf_key in existing_fingerprints:
            log.info("[skip] %s (déjà indexé)", pdf_path.name)
            continue

        # En dry-run, on ne déclenche pas l'OCR Vision (gratuit garanti).
        use_vision = (not args.no_vision) and (not args.dry_run)
        pages = extract_pages(pdf_path, use_vision=use_vision)
        if not pages:
            log.info("[skip] %s (aucun texte natif — scanné ?)", pdf_path.name)
            continue

        # Calcule les chunks une seule fois, puis upsert pour chaque sujet.
        chunks_per_page: list[tuple[int, list[str]]] = []
        for page_num, page_text in pages:
            chunks_per_page.append((page_num, split_text(page_text)))

        total_chunks_this_pdf = sum(len(c) for _, c in chunks_per_page)
        if total_chunks_this_pdf == 0:
            continue

        if args.dry_run:
            log.info(
                "[dry-run] %s → %d chunks × %d sujet(s) (%s)",
                pdf_path.name,
                total_chunks_this_pdf,
                len(subjects_matched),
                ",".join(subjects_matched),
            )
            for s in subjects_matched:
                by_subject[s] += total_chunks_this_pdf
            total_chunks_added += total_chunks_this_pdf * len(subjects_matched)
            continue

        log.info(
            "Indexing %s → %d chunks × %s",
            pdf_path.name,
            total_chunks_this_pdf,
            ",".join(subjects_matched),
        )

        # Embedding une seule fois (les chunks ne dépendent pas du sujet),
        # puis upsert avec un ID + metadata différents par sujet.
        flat_docs: list[str] = []
        flat_meta_keys: list[tuple[int, int]] = []  # (page_num, chunk_idx)
        for page_num, page_chunks in chunks_per_page:
            for j, chunk in enumerate(page_chunks):
                flat_docs.append(chunk)
                flat_meta_keys.append((page_num, j))

        all_embeddings: list[list[float]] = []
        for k in range(0, len(flat_docs), EMBED_BATCH):
            sub = flat_docs[k : k + EMBED_BATCH]
            all_embeddings.extend(embed_batch(client, sub))

        for subject in subjects_matched:
            batch_ids: list[str] = []
            batch_metas: list[dict] = []
            for (page_num, j) in flat_meta_keys:
                batch_ids.append(chunk_id(subject, pdf_path, page_num, j))
                batch_metas.append(
                    {
                        "subject": subject,
                        "source": pdf_path.name,
                        "page": page_num,
                        "fingerprint": pdf_key,
                    }
                )
            coll.upsert(
                ids=batch_ids,
                documents=flat_docs,
                metadatas=batch_metas,
                embeddings=all_embeddings,
            )
            by_subject[subject] += total_chunks_this_pdf
            total_chunks_added += total_chunks_this_pdf

    log.info("─" * 60)
    log.info("PDFs scannés        : %d", total_pdfs)
    log.info("Chunks ajoutés      : %d", total_chunks_added)
    log.info("Chunks skip (cache) : %d", total_chunks_skipped)
    for s, n in by_subject.items():
        if n > 0:
            log.info("  %-10s : %d chunks", s, n)
    if args.dry_run:
        log.info("Total dans la collection : (dry-run, pas écrit)")
    else:
        log.info("Total dans la collection : %d", coll.count())
    return 0


if __name__ == "__main__":
    sys.exit(main())
