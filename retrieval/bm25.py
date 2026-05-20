"""Index BM25 lexical — Phase 2.

Pourquoi BM25 en plus des embeddings ?
- Les embeddings sont forts pour la similarité **conceptuelle** ("dérivée" ≈
  "fonction dérivable"), mais peuvent rater des **termes exacts** rares ou
  techniques ("peroxodisulfate", "GnRH", "barycentre", "S_2O_8^{2-}").
- BM25 score par fréquence pondérée des termes exacts → complémentaire.
- Combinés via Reciprocal Rank Fusion, on récupère le meilleur des deux.

Architecture :
- Pas de service externe : l'index BM25 est construit en mémoire au boot du
  serveur depuis le contenu de Chroma. Pour 2625 chunks ≈ 50 MB, < 2 s.
- Pas de persistance disque pour l'instant (pickle fragile). Si l'index devient
  lourd on ajoutera un cache pickle.

Filtrage par subject : on garde un mapping subject → liste d'IDs internes pour
ne BM25-rank que les chunks de la matière demandée (sinon le top serait
contaminé par des matières non pertinentes).
"""

from __future__ import annotations

import logging
import re
import time
import unicodedata
from typing import Iterable

from rank_bm25 import BM25Okapi

log = logging.getLogger("rag-server")


# ─── Tokenization ────────────────────────────────────────────────────────────

# On retire les commandes LaTeX (\boxed, \frac, …) pour qu'elles ne pollue pas
# la statistique BM25, mais on garde les noms de variables et formules courtes.
_LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]+")
# Caractères de ponctuation à remplacer par espace (on garde tirets et chiffres)
_PUNCT_RE = re.compile(r"[^\w\-]+", flags=re.UNICODE)
_MULTI_SPACE_RE = re.compile(r"\s+")

# Stopwords français les plus fréquents (liste courte volontairement —
# pour BM25 elles ne posent pas vraiment de problème grâce à l'IDF, mais on
# évite que "le", "la", "de" gonflent les vecteurs).
_STOPWORDS_FR = frozenset({
    "le", "la", "les", "un", "une", "des", "du", "de", "d",
    "et", "ou", "que", "qui", "qu", "ce", "ces", "cet", "cette",
    "il", "elle", "ils", "elles", "on", "nous", "vous",
    "est", "sont", "etre", "être", "fait", "faire",
    "pour", "par", "dans", "sur", "sous", "avec", "sans", "vers",
    "en", "au", "aux", "à", "a",
    "si", "donc", "alors", "puis",
    "se", "sa", "son", "ses", "ma", "mon", "mes", "ta", "ton", "tes",
    "y",
})


def tokenize(text: str) -> list[str]:
    """Tokenize bas-niveau pour BM25 : minuscule + NFC + suppression commandes
    LaTeX + split sur ponctuation + retrait stopwords FR courts."""
    if not text:
        return []
    t = unicodedata.normalize("NFC", text).lower()
    t = _LATEX_CMD_RE.sub(" ", t)
    t = _PUNCT_RE.sub(" ", t)
    t = _MULTI_SPACE_RE.sub(" ", t).strip()
    if not t:
        return []
    return [w for w in t.split(" ") if len(w) >= 2 and w not in _STOPWORDS_FR]


# ─── Index ───────────────────────────────────────────────────────────────────


class BM25Index:
    """Index BM25 partitionné par matière.

    Pour chaque matière (math/physique/chimie/svt), on maintient :
    - une liste d'IDs Chroma (ordre stable),
    - une instance BM25Okapi entraînée sur les tokens de ces chunks.

    L'API ``search`` retourne un ranking trié par score BM25 décroissant.
    """

    def __init__(self) -> None:
        self._indexes: dict[str, BM25Okapi] = {}
        self._ids: dict[str, list[str]] = {}
        self._docs: dict[str, list[str]] = {}
        self.built_at: float | None = None

    @property
    def subjects(self) -> list[str]:
        return list(self._indexes.keys())

    def total_chunks(self) -> int:
        return sum(len(ids) for ids in self._ids.values())

    def build_from_chroma(self, items: Iterable[tuple[str, str, dict]]) -> None:
        """Construit l'index depuis ``items`` = iterable de (id, document, metadata).

        ``metadata`` doit contenir ``subject``. Partitionne par subject puis
        entraîne un BM25Okapi par matière.
        """
        t0 = time.perf_counter()
        # Collecte par matière
        by_subject: dict[str, list[tuple[str, str]]] = {}
        for cid, doc, meta in items:
            subject = (meta or {}).get("subject")
            if not subject or not doc:
                continue
            by_subject.setdefault(subject, []).append((cid, doc))

        # Construit un index par matière
        self._indexes.clear()
        self._ids.clear()
        self._docs.clear()
        for subject, pairs in by_subject.items():
            ids = [p[0] for p in pairs]
            docs = [p[1] for p in pairs]
            tokens = [tokenize(d) for d in docs]
            # Skip subjects sans aucun token (corpus vide ou tout en LaTeX) :
            # rank-bm25 plante sur des corpus vides.
            if not any(tokens):
                log.warning("BM25 : subject=%s skippé (aucun token utilisable)", subject)
                continue
            self._indexes[subject] = BM25Okapi(tokens)
            self._ids[subject] = ids
            self._docs[subject] = docs

        self.built_at = time.time()
        log.info(
            "BM25 index built : %d chunks, %d matières, en %.2fs",
            self.total_chunks(),
            len(self._indexes),
            time.perf_counter() - t0,
        )

    def search(self, subject: str, query: str, top_k: int = 20) -> list[tuple[str, float]]:
        """Retourne les top_k (chunk_id, score_bm25) pour la matière donnée.

        Score brut BM25 (non normalisé) — la normalisation se fait au moment
        de la fusion RRF, où seuls les rangs comptent.
        """
        idx = self._indexes.get(subject)
        if idx is None:
            return []
        q_tokens = tokenize(query)
        if not q_tokens:
            return []
        # rank-bm25 renvoie un score pour CHAQUE document de la matière. On
        # trie ensuite et tronque à top_k. Pour 2625 chunks par matière max,
        # c'est instantané (~1 ms).
        scores = idx.get_scores(q_tokens)
        ids = self._ids[subject]
        # Index trié par score décroissant
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        out: list[tuple[str, float]] = []
        for rank_idx in ranked[:top_k]:
            score = float(scores[rank_idx])
            if score <= 0:  # BM25 ≤ 0 = document totalement non pertinent
                break
            out.append((ids[rank_idx], score))
        return out
