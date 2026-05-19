"""Outils partagés entre ingest.py et server.py."""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Iterator, Optional

# Sujets correspondent aux IDs côté Débloque-moi (src/lib/subjects.ts).
SUBJECTS = ("math", "physique", "chimie", "svt")

# Mappings dossier parent → liste de matières.
# Classification basée EXCLUSIVEMENT sur le chemin (dossier parent), pas sur
# le nom de fichier — car « sn » dans un filename signifie souvent
# « session normale » (date d'examen) et non « Sciences Naturelles ».
FOLDER_PATTERNS = [
    # (substring à chercher dans le path en minuscules, liste de matières)
    ("sujets corrigés math", ["math"]),
    ("sujets corriges math", ["math"]),
    ("/math/", ["math"]),
    ("phisique et chimie", ["physique", "chimie"]),
    ("physique et chimie", ["physique", "chimie"]),
    ("physique & chimie", ["physique", "chimie"]),
    ("/physique/", ["physique"]),
    ("/chimie/", ["chimie"]),
    ("science naturelle", ["svt"]),
    ("sciences naturelles", ["svt"]),
    ("sciences naturelle", ["svt"]),
    ("science naturelles", ["svt"]),
    ("/svt/", ["svt"]),
]


def classify_pdf(path: Path) -> list[str]:
    """Retourne la liste des subject_id auxquels ce PDF s'applique, déduite
    EXCLUSIVEMENT du dossier parent. Pas de fallback filename pour éviter
    les ambigüités du type « sn » qui peut être « session normale » plutôt
    que « Sciences Naturelles ».

    Retourne [] si le PDF est dans un dossier non reconnu.
    """
    s = str(path).lower()
    for pattern, subjects in FOLDER_PATTERNS:
        if pattern in s:
            return list(subjects)
    return []


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
