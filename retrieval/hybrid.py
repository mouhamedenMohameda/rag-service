"""Fusion RRF entre embeddings et BM25 — Phase 2.

Reciprocal Rank Fusion (RRF) — la méthode standard pour combiner plusieurs
classements sans devoir normaliser leurs scores absolus :

    score_RRF(d) = Σ_l  1 / (k + rank_l(d))

où ``l`` parcourt les listes de classement (ici : embeddings et BM25), et
``k`` est une constante de lissage (60 par défaut, valeur de référence du
papier original Cormack et al. 2009).

Avantages :
- Pas besoin de calibrer les échelles de scores (cosine ∈ [0,1] vs BM25 ≥ 0)
- Robuste aux distributions très différentes
- Implémentation tenant en 10 lignes
- Le top RRF favorise les documents bien classés dans **les deux** listes,
  ce qui correspond à notre objectif : documents pertinents à la fois
  conceptuellement (embeddings) et lexicalement (BM25).
"""

from __future__ import annotations

from typing import Iterable


def rrf_fuse(
    rankings: Iterable[list[str]],
    k: int = 60,
    weights: Iterable[float] | None = None,
) -> list[tuple[str, float]]:
    """Fusionne plusieurs classements via Reciprocal Rank Fusion.

    Args:
        rankings: itérable de listes ordonnées d'IDs (du meilleur au pire).
        k: constante de lissage (60 dans le papier original).
        weights: poids optionnel par liste (ex. [1.0, 0.7] pour donner plus
            d'importance aux embeddings). Défaut : poids égaux à 1.

    Returns:
        Liste (id, score_RRF) triée par score décroissant. Inclut tous les
        IDs apparaissant dans au moins une des listes.
    """
    rankings = list(rankings)
    if not rankings:
        return []
    w_list = list(weights) if weights is not None else [1.0] * len(rankings)
    if len(w_list) != len(rankings):
        raise ValueError("weights doit avoir la même longueur que rankings")

    scores: dict[str, float] = {}
    for ranking, w in zip(rankings, w_list):
        for rank, cid in enumerate(ranking, start=1):
            scores[cid] = scores.get(cid, 0.0) + w * (1.0 / (k + rank))

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
