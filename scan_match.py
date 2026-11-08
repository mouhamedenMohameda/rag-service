"""Reconnaissance d'un exercice photographié — sans appel IA (gratuit, instantané).

Entrée : le texte lu sur la photo (OCR) + la série de l'élève.
Sortie :
  - ``match``     : l'exercice de bac correspondant, si la similarité est nette ;
  - ``chapters``  : les chapitres candidats, classés (vote des exercices voisins) ;
  - ``neighbors`` : les exercices les plus proches.

Méthode : TF-IDF (mots + nombres + paires de nombres consécutifs, qui capturent
les coefficients d'un polynôme) et similarité cosinus. L'index est reconstruit
seulement quand json_bac.json change.
"""
from __future__ import annotations

import math
import re
import threading
import unicodedata
from collections import Counter, defaultdict
from typing import Iterable, Optional

_STOP = set("""
les des une un le la et en du de dans pour par que qui sur au aux est sont on
tout tous toute toutes son ses sa leur leurs avec cette ces ce cet il elle ils
pas plus ou nombre nombres point points donner calculer determiner montrer
justifier verifier deduire ecrire placer construire ensemble tel telle tels
telles soit soient alors puis forme repere plan complexe complexes orthonorme
direct affixe affixes respectives respectivement suivant suivante suivantes
""".split())

_CMD = re.compile(r"\\(?:dfrac|frac|tfrac|left|right|mathbb|mathrm|operatorname|text|vec|overrightarrow|overline|bar|quad|qquad|displaystyle|cdot|times|sqrt|in|forall|iff|equiv|pi|alpha|theta|arg|ln|lim|infty|leq|geq|neq|ne|le|ge)\b")


def _norm(text: str) -> str:
    t = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()
    t = t.replace("²", "^2").replace("³", "^3")
    t = _CMD.sub(" ", t)
    t = re.sub(r"[{}$\\]", " ", t)
    return t


def tokens(text: str) -> list[str]:
    t = _norm(text)
    words = [w for w in re.findall(r"[a-z]{3,}", t) if w not in _STOP]
    nums = re.findall(r"\d+(?:[.,]\d+)?", t)
    feats = words + [f"#{n}" for n in nums]
    feats += [f"#{a}_{b}" for a, b in zip(nums, nums[1:])]
    return feats


class ExerciseIndex:
    def __init__(self, exercises: Iterable[dict]):
        self.items: list[dict] = []
        docs: list[Counter] = []
        df: Counter = Counter()
        for e in exercises:
            text = e.get("ennonce_complet") or ""
            if len(text.strip()) < 40 or e.get("is_skeleton"):
                continue
            c = Counter(tokens(text))
            if not c:
                continue
            self.items.append(e)
            docs.append(c)
            df.update(c.keys())
        n = max(1, len(docs))
        self.idf = {f: math.log((1 + n) / (1 + k)) + 1.0 for f, k in df.items()}
        self.vecs = [self._weigh(c) for c in docs]

    def _weigh(self, c: Counter) -> dict[str, float]:
        v = {f: (1 + math.log(k)) * self.idf.get(f, 1.0) for f, k in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {f: x / norm for f, x in v.items()}

    def search(self, text: str, filiere: Optional[str] = None, k: int = 8) -> list[tuple[float, dict]]:
        q = self._weigh(Counter(tokens(text)))
        if not q:
            return []
        out = []
        for e, v in zip(self.items, self.vecs):
            if filiere and e.get("filiere_id") != filiere:
                continue
            s = sum(w * v.get(f, 0.0) for f, w in q.items())
            if s > 0:
                out.append((s, e))
        out.sort(key=lambda x: -x[0])
        return out[:k]


_cache_lock = threading.Lock()
_cache: dict = {"key": None, "index": None}


def get_index(store) -> ExerciseIndex:
    """Index mis en cache tant que json_bac.json n'a pas changé."""
    path = store.json_path
    key = path.stat().st_mtime_ns if path.exists() else 0
    with _cache_lock:
        if _cache["key"] != key or _cache["index"] is None:
            _cache["index"] = ExerciseIndex(store.load())
            _cache["key"] = key
        return _cache["index"]


# Seuils (réglés sur les énoncés OCR bruts vs énoncés vérifiés, série D)
MATCH_MIN = 0.45      # similarité minimale pour « c'est cet exercice du bac »
MATCH_MARGIN = 0.08   # écart minimal avec le 2e candidat
CHAPTER_MIN = 0.12    # similarité minimale d'un voisin pour voter


def rank_chapters(neighbors: list[tuple[float, dict]], chapters_of) -> list[tuple[str, str, float]]:
    """Vote pondéré des voisins : [(matiere, chapitre, part du vote)]."""
    votes: dict[tuple[str, str], float] = defaultdict(float)
    total = 0.0
    for s, e in neighbors:
        if s < CHAPTER_MIN:
            continue
        chs = chapters_of(e)
        if not chs:
            continue
        m = e.get("matiere_id") or ""
        for c in chs:
            votes[(m, c)] += s / len(chs)
        total += s
    if not total:
        return []
    return sorted(((m, c, v / total) for (m, c), v in votes.items()), key=lambda x: -x[2])


def pick_match(neighbors: list[tuple[float, dict]]) -> Optional[tuple[float, dict]]:
    if not neighbors:
        return None
    s1, e1 = neighbors[0]
    s2 = neighbors[1][0] if len(neighbors) > 1 else 0.0
    if s1 >= MATCH_MIN and (s1 - s2) >= MATCH_MARGIN:
        return s1, e1
    return None


def score_notions(
    text: str,
    neighbors: list[tuple[float, dict]],
    allowed: list[str],
    keywords: dict[str, list[str]],
) -> list[tuple[str, float]]:
    """Notions détectées parmi ``allowed`` : vote des voisins + mots-clés."""
    t = (text or "").lower()
    allowed_set = set(allowed)
    vote: dict[str, float] = defaultdict(float)
    total = 0.0
    for s, e in neighbors:
        ids = [i for i in (e.get("notion_ids") or []) if i in allowed_set]
        if s < CHAPTER_MIN or not ids:
            continue
        total += s
        for i in ids:
            vote[i] += s
    out = []
    for nid in allowed:
        v = vote[nid] / total if total else 0.0
        kw = any(k.lower() in t for k in keywords.get(nid, []))
        score = 0.6 * v + (0.5 if kw else 0.0)
        if score >= 0.35:
            out.append((nid, round(score, 3)))
    out.sort(key=lambda x: -x[1])
    return out[:5]
