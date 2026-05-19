"""Outils partagés entre ingest.py et server.py."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterator, Optional

# Sujets correspondent aux IDs côté Débloque-moi (src/lib/subjects.ts).
SUBJECTS = ("math", "physique", "chimie", "svt")

# Mots-clés (en minuscules, fautes de frappe et variantes courantes inclus)
# associés à chaque matière. La classification matche n'importe lequel.
SUBJECT_KEYWORDS = {
    "math": ["math", "algebre", "algébre", "analyse", "arithmétique", "geometrie", "géométrie"],
    "physique": ["physique", "phisique", "physics", "mécanique", "electromagnetisme"],
    "chimie": ["chimie", "chemistry"],
    "svt": [
        "sciences naturelles",
        "science naturelle",
        "sciences naturelle",  # variantes orthographiques
        "science naturelles",
        "svt",
        "biologie",
        "bac d sn",
        " sn ",  # « Bac C ... SN corr.pdf »
        "/sn/",
    ],
}


def classify_pdf(path: Path) -> list[str]:
    """Retourne la liste des subject_id ('math', 'physique', 'chimie', 'svt')
    auxquels ce PDF s'applique.

    - Retourne une liste vide si le PDF n'est pas pertinent.
    - Retourne plusieurs sujets pour un PDF qui en couvre plusieurs (ex :
      « Bac C PC corrigé.pdf » → ['physique', 'chimie']).
    - Tolère les fautes de frappe (« phisique ») et les variantes
      orthographiques (« Science naturelle »).
    """
    s = str(path).lower()
    matched: list[str] = []
    for subject, keywords in SUBJECT_KEYWORDS.items():
        if any(kw in s for kw in keywords):
            matched.append(subject)
    # Heuristique : si "pc" apparaît dans le nom de fichier comme abréviation
    # de « Physique & Chimie » → ajouter les deux.
    name = path.name.lower()
    if " pc " in f" {name} " or name.startswith("pc "):
        for s_id in ("physique", "chimie"):
            if s_id not in matched:
                matched.append(s_id)
    return matched


# Séparateurs utilisés en cascade par le chunker (le plus structurant d'abord).
SPLIT_SEPARATORS = ["\n\n\n", "\n\n", "\n", ". ", " "]


def split_text(
    text: str,
    target_chars: int = 2400,
    overlap_chars: int = 200,
) -> list[str]:
    """Découpe ``text`` en morceaux d'environ ``target_chars`` caractères avec
    ``overlap_chars`` de chevauchement entre morceaux successifs.

    ~2400 caractères ≈ 600 tokens ≈ une page d'un manuel, ce qui correspond bien
    à une unité de contenu cohérent (un théorème + sa preuve, ou un exercice +
    une étape de correction).
    """
    text = text.strip()
    if not text:
        return []
    if len(text) <= target_chars:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + target_chars)
        if end < len(text):
            # On essaie de couper sur un séparateur naturel proche de end.
            window_start = max(start + target_chars // 2, start)
            window = text[window_start:end]
            cut_at = -1
            for sep in SPLIT_SEPARATORS:
                idx = window.rfind(sep)
                if idx != -1:
                    cut_at = window_start + idx + len(sep)
                    break
            if cut_at != -1 and cut_at > start:
                end = cut_at
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= len(text):
            break
        start = max(end - overlap_chars, start + 1)
    return chunks


_WHITESPACE_RE = re.compile(r"[ \t]+")
_MULTIPLE_NEWLINES_RE = re.compile(r"\n{3,}")


def normalize_text(text: str) -> str:
    """Aplatit les espaces multiples et retours à la ligne en excès."""
    text = _WHITESPACE_RE.sub(" ", text)
    text = _MULTIPLE_NEWLINES_RE.sub("\n\n", text)
    return text.strip()


def iter_pdfs(root: Path) -> Iterator[Path]:
    """Itère récursivement sur les fichiers .pdf sous ``root``."""
    if not root.exists():
        return
    for p in sorted(root.rglob("*.pdf")):
        if p.is_file():
            yield p


def get_env(name: str, default: Optional[str] = None) -> str:
    val = os.environ.get(name, default)
    if val is None or val == "":
        raise RuntimeError(f"Variable d'environnement requise : {name}")
    return val
