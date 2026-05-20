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

from common import SUBJECTS, get_env

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
    log.info(
        "RAG ready — collection bac_corpus contient %d chunks", state.coll.count()
    )
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


# ─── Routes ─────────────────────────────────────────────────────────────────


@app.get("/health")
def health() -> dict:
    return {
        "ok": True,
        "chunks": state.coll.count() if state.coll else 0,
    }


@app.post("/search", response_model=SearchResponse, dependencies=[Depends(require_api_key)])
def search(body: SearchBody) -> SearchResponse:
    if body.subject not in SUBJECTS:
        raise HTTPException(status_code=400, detail=f"subject invalide ({body.subject})")
    if state.coll is None or state.openai is None:
        raise HTTPException(status_code=503, detail="Service non initialisé.")
    if state.coll.count() == 0:
        return SearchResponse(chunks=[], subject=body.subject, query=body.query)

    t0 = time.perf_counter()

    # Embedding de la requête
    try:
        emb_resp = state.openai.embeddings.create(model=EMBED_MODEL, input=[body.query])
    except Exception as e:
        log.error("Embedding query failed : %s", e)
        raise HTTPException(status_code=502, detail="Erreur embedding OpenAI.")
    qvec = emb_resp.data[0].embedding

    # Recherche dans Chroma, filtrée par subject
    try:
        res = state.coll.query(
            query_embeddings=[qvec],
            n_results=body.top_k,
            where={"subject": body.subject},
            include=["documents", "metadatas", "distances"],
        )
    except Exception as e:
        log.error("Chroma query failed : %s", e)
        raise HTTPException(status_code=502, detail="Erreur recherche vectorielle.")

    chunks: list[Chunk] = []
    docs = (res.get("documents") or [[]])[0]
    metas = (res.get("metadatas") or [[]])[0]
    dists = (res.get("distances") or [[]])[0]
    for doc, meta, dist in zip(docs, metas, dists):
        # Chroma cosine renvoie une distance ∈ [0, 2]. Convertit en score [0, 1]
        # similarité : 1 - dist/2.
        score = max(0.0, 1.0 - float(dist) / 2.0)
        chunks.append(
            Chunk(
                text=doc,
                source=str(meta.get("source", "?")),
                page=int(meta.get("page", 0)),
                score=round(score, 4),
            )
        )

    latency_ms = (time.perf_counter() - t0) * 1000
    trace_log.info(json.dumps({
        "evt": "search",
        "subject": body.subject,
        "query_len": len(body.query),
        "top_k": body.top_k,
        "returned": len(chunks),
        "top_score": chunks[0].score if chunks else None,
        "sources": [c.source for c in chunks],
        "latency_ms": round(latency_ms, 1),
    }, ensure_ascii=False))

    return SearchResponse(chunks=chunks, subject=body.subject, query=body.query)


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8001"))
    uvicorn.run(app, host="127.0.0.1", port=port)
