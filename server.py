"""Serveur RAG : expose POST /search pour récupérer les chunks les plus
proches d'une question, filtrés par matière.

Authentification : header ``X-Api-Key: <RAG_S2S_KEY>``. Le service n'est pas
public — il est appelé depuis le backend Débloque-moi (ou autre app interne).
"""

from __future__ import annotations

import json
import logging
import os
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Optional

import chromadb
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field

from admin_api import AdminStore, build_admin_router
from admin_courses import CoursesStore, build_courses_router
from common import SUBJECTS, get_env
from retrieval import BM25Index, rrf_fuse

# ─── Configuration ──────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("rag-server")

# Logger dédié aux traces de recherche : une ligne JSON par requête /search,
# pour pouvoir auditer en prod ce que le RAG ramène (préparation Phase 4).
trace_log = logging.getLogger("rag-trace")
trace_log.propagate = False
if not trace_log.handlers:
    _h = logging.StreamHandler()
    _h.setFormatter(logging.Formatter("%(message)s"))
    trace_log.addHandler(_h)
    trace_log.setLevel(logging.INFO)

EMBED_MODEL = "text-embedding-3-small"


# ─── État global (initialisé au boot) ───────────────────────────────────────


class State:
    openai: Optional[OpenAI] = None
    chroma: Optional[chromadb.PersistentClient] = None
    coll = None
    api_key: str = ""
    min_score: float = 0.55
    # Phase 2 — hybride
    bm25: Optional[BM25Index] = None
    use_bm25: bool = True
    hybrid_pool: int = 20


state = State()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    load_dotenv()
    state.api_key = get_env("RAG_S2S_KEY")
    state.openai = OpenAI(api_key=get_env("OPENAI_API_KEY"))
    chroma_dir = Path(get_env("RAG_CHROMA_DIR")).resolve()
    chroma_dir.mkdir(parents=True, exist_ok=True)
    state.chroma = chromadb.PersistentClient(path=str(chroma_dir))
    state.coll = state.chroma.get_or_create_collection(
        name="bac_corpus",
        metadata={"hnsw:space": "cosine"},
    )
    # Seuil de confiance configurable (Phase 1). En dessous, la réponse est
    # marquée low_confidence=true. Défaut prudent : 0.55 (cosine similarity).
    state.min_score = float(os.environ.get("RAG_MIN_SCORE", "0.55"))

    # Phase 2 — hybride. RAG_USE_BM25=false pour A/B test / fallback rapide.
    state.use_bm25 = os.environ.get("RAG_USE_BM25", "true").lower() in ("1", "true", "yes")
    state.hybrid_pool = int(os.environ.get("RAG_HYBRID_POOL", "20"))

    n = state.coll.count()
    log.info("RAG ready — collection bac_corpus contient %d chunks", n)

    if state.use_bm25 and n > 0:
        try:
            log.info("BM25 : construction de l'index lexical depuis Chroma…")
            existing = state.coll.get(include=["documents", "metadatas"])
            items = list(zip(
                existing.get("ids") or [],
                existing.get("documents") or [],
                existing.get("metadatas") or [],
            ))
            bm25 = BM25Index()
            bm25.build_from_chroma(items)
            state.bm25 = bm25
        except Exception as e:
            # On dégrade gracieusement vers embeddings-only plutôt que de
            # bloquer le service entier.
            log.error("BM25 indexation échouée, fallback embeddings-only : %s", e)
            state.bm25 = None
    else:
        log.info("BM25 désactivé (RAG_USE_BM25=false ou corpus vide)")

    # Admin API — édition manuelle du JSON Bac
    json_path = Path(os.environ.get("RAG_JSON_BAC", "json_bac.json")).resolve()
    backup_dir = json_path.parent / "json_backups"
    store = AdminStore(json_path=json_path, backup_dir=backup_dir)
    admin_router = build_admin_router(store, api_key=state.api_key)
    _app.include_router(admin_router)
    log.info("Admin API mountée sur /admin (JSON: %s)", json_path)

    # Admin Courses API — génération et édition de cours par notion
    cours_path = json_path.parent / "cours.json"
    courses_store = CoursesStore(path=cours_path, backup_dir=backup_dir)
    courses_router = build_courses_router(
        json_bac_store=store,
        courses_store=courses_store,
        root=json_path.parent,
        api_key=state.api_key,
    )
    _app.include_router(courses_router)
    log.info("Admin Courses API mountée sur /admin/courses (cours: %s)", cours_path)
    yield


app = FastAPI(title="rag-service", lifespan=lifespan)


# ─── Auth S2S ───────────────────────────────────────────────────────────────


def require_api_key(x_api_key: Optional[str] = Header(default=None)) -> None:
    if not x_api_key or x_api_key != state.api_key:
        raise HTTPException(status_code=401, detail="Clé S2S invalide.")


# ─── Schémas ────────────────────────────────────────────────────────────────


class SearchBody(BaseModel):
    subject: str = Field(..., description="math | physique | chimie | svt")
    query: str = Field(..., min_length=3, max_length=4000)
    top_k: int = Field(default=5, ge=1, le=20)


class Chunk(BaseModel):
    text: str
    source: str
    page: int
    score: float


class SearchResponse(BaseModel):
    chunks: list[Chunk]
    subject: str
    query: str
    # Phase 1 — anti-hallucination : true si aucun chunk n'a un score >=
    # RAG_MIN_SCORE. Le client peut afficher un avertissement à l'élève et/ou
    # adapter le prompt (« raisonne sans corrigé proche »).
    low_confidence: bool
    min_score_threshold: float


# ─── Routes ─────────────────────────────────────────────────────────────────


@app.get("/health")
def health() -> dict:
    return {
        "ok": True,
        "chunks": state.coll.count() if state.coll else 0,
        # Phase 2 — visibilité opérationnelle
        "mode": "hybrid" if (state.use_bm25 and state.bm25) else "embeddings",
        "bm25_chunks": state.bm25.total_chunks() if state.bm25 else 0,
        "bm25_subjects": state.bm25.subjects if state.bm25 else [],
        "min_score_threshold": state.min_score,
        "hybrid_pool": state.hybrid_pool,
    }


@app.post("/search", response_model=SearchResponse, dependencies=[Depends(require_api_key)])
def search(body: SearchBody) -> SearchResponse:
    if body.subject not in SUBJECTS:
        raise HTTPException(status_code=400, detail=f"subject invalide ({body.subject})")
    if state.coll is None or state.openai is None:
        raise HTTPException(status_code=503, detail="Service non initialisé.")
    if state.coll.count() == 0:
        return SearchResponse(
            chunks=[],
            subject=body.subject,
            query=body.query,
            low_confidence=True,
            min_score_threshold=state.min_score,
        )

    t0 = time.perf_counter()

    # Taille du pool à récupérer côté Chroma. En mode hybride, on en prend plus
    # que ``top_k`` pour donner à RRF un vrai espace de fusion. En mode pur
    # embeddings, on prend juste ``top_k``.
    bm25_active = state.use_bm25 and state.bm25 is not None
    chroma_pool = state.hybrid_pool if bm25_active else body.top_k

    # ─── 1. Embedding de la requête ────────────────────────────────────────
    try:
        emb_resp = state.openai.embeddings.create(model=EMBED_MODEL, input=[body.query])
    except Exception as e:
        log.error("Embedding query failed : %s", e)
        raise HTTPException(status_code=502, detail="Erreur embedding OpenAI.")
    qvec = emb_resp.data[0].embedding

    # ─── 2. Recherche vectorielle (embeddings) ─────────────────────────────
    try:
        res = state.coll.query(
            query_embeddings=[qvec],
            n_results=chroma_pool,
            where={"subject": body.subject},
            include=["documents", "metadatas", "distances"],
        )
    except Exception as e:
        log.error("Chroma query failed : %s", e)
        raise HTTPException(status_code=502, detail="Erreur recherche vectorielle.")

    emb_ids: list[str] = (res.get("ids") or [[]])[0]
    emb_docs: list[str] = (res.get("documents") or [[]])[0]
    emb_metas: list[dict] = (res.get("metadatas") or [[]])[0]
    emb_dists: list[float] = (res.get("distances") or [[]])[0]

    # Lookup id → (doc, meta, cosine_score) pour pouvoir reconstruire les
    # chunks après fusion RRF dans n'importe quel ordre.
    pool: dict[str, dict] = {}
    for cid, doc, meta, dist in zip(emb_ids, emb_docs, emb_metas, emb_dists):
        cosine = max(0.0, 1.0 - float(dist) / 2.0)
        pool[cid] = {"doc": doc, "meta": meta, "score": cosine}

    # ─── 3. Recherche lexicale (BM25) si activée ───────────────────────────
    bm25_ids: list[str] = []
    bm25_scores: dict[str, float] = {}
    if bm25_active:
        bm25_hits = state.bm25.search(body.subject, body.query, top_k=state.hybrid_pool)
        bm25_ids = [cid for cid, _ in bm25_hits]
        bm25_scores = dict(bm25_hits)

        # Pour les hits BM25 absents du pool embeddings, on récupère leur
        # texte/meta depuis Chroma (par batch, 1 seul appel).
        missing = [cid for cid in bm25_ids if cid not in pool]
        if missing:
            try:
                got = state.coll.get(ids=missing, include=["documents", "metadatas"])
                for cid, doc, meta in zip(
                    got.get("ids") or [],
                    got.get("documents") or [],
                    got.get("metadatas") or [],
                ):
                    # Score cosine inconnu pour ces hits (Chroma ne les a pas
                    # ressortis dans son top). On met 0 — ils ne compteront
                    # pas dans low_confidence sauf si reranke en tête.
                    pool[cid] = {"doc": doc, "meta": meta, "score": 0.0}
            except Exception as e:
                log.warning("BM25 hits missing fetch a échoué : %s", e)

    # ─── 4. Fusion RRF ──────────────────────────────────────────────────────
    if bm25_active and bm25_ids:
        fused = rrf_fuse([emb_ids, bm25_ids])
        ranked_ids = [cid for cid, _ in fused if cid in pool][: body.top_k]
    else:
        ranked_ids = emb_ids[: body.top_k]

    chunks: list[Chunk] = []
    for cid in ranked_ids:
        entry = pool.get(cid)
        if not entry:
            continue
        meta = entry["meta"] or {}
        chunks.append(
            Chunk(
                text=entry["doc"],
                source=str(meta.get("source", "?")),
                page=int(meta.get("page", 0)),
                score=round(float(entry["score"]), 4),
            )
        )

    latency_ms = (time.perf_counter() - t0) * 1000

    # low_confidence : on regarde le meilleur cosine parmi les chunks renvoyés
    # (le top peut être un hit BM25-only avec cosine=0, donc max plutôt que [0]).
    cosines = [c.score for c in chunks if c.score > 0]
    best_cosine = max(cosines) if cosines else None
    low_confidence = best_cosine is None or best_cosine < state.min_score

    trace_log.info(json.dumps({
        "evt": "search",
        "mode": "hybrid" if bm25_active else "embeddings",
        "subject": body.subject,
        "query_len": len(body.query),
        "top_k": body.top_k,
        "pool": chroma_pool,
        "returned": len(chunks),
        "top_score": chunks[0].score if chunks else None,
        "best_cosine": best_cosine,
        "min_score": state.min_score,
        "low_confidence": low_confidence,
        "sources": [c.source for c in chunks],
        "bm25_overlap": (
            len(set(bm25_ids) & set(emb_ids)) if bm25_active and bm25_ids else None
        ),
        "latency_ms": round(latency_ms, 1),
    }, ensure_ascii=False))

    return SearchResponse(
        chunks=chunks,
        subject=body.subject,
        query=body.query,
        low_confidence=low_confidence,
        min_score_threshold=state.min_score,
    )


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8001"))
    uvicorn.run(app, host="127.0.0.1", port=port)
