"""Module retrieval — Phase 2.

Pipeline complet : embedding sémantique (Chroma) + BM25 lexical, fusionnés via
Reciprocal Rank Fusion (RRF). Conçu pour rester modulable : on peut activer/
désactiver BM25 via env var RAG_USE_BM25.
"""

from .bm25 import BM25Index
from .hybrid import rrf_fuse

__all__ = ["BM25Index", "rrf_fuse"]
