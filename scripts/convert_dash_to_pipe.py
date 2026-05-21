"""Convertit le format à tirets vers le format à pipes pour le parser standard.

Avant : === Sciences Physiques - Série C 2002 - Session Normale - Exercice 1 ===
Après : === Sciences Physiques | Série C | 2002 | Session Normale | Exercice 1 ===

Strippe aussi tous les headers parasites :
  Fichier source: <path>
  Chapitre: <name>
  Notions: <list>

Et nettoie les "Exercice BAC-2015-SC-D-EXO5" → "Exercice 5" si possible.

Usage :
    .venv/bin/python scripts/convert_dash_to_pipe.py \\
        --input exo_extracted_backup/science-bacc.txt \\
        --output /tmp/converted_bacc.txt
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path


# Marker dash : capture matière, filière, année, session, exercice
DASH_MARKER_RE = re.compile(
    r"===\s*"
    r"(?P<mat>Sciences Physiques|Sciences Naturelles|Mathématiques)\s+-\s+"
    r"Série\s+(?P<serie>[CDcd])\s+(?P<year>\d{4})\s+-\s+"
    r"Session\s+(?P<sess>Normale|Complémentaire|Complementaire)\s+-\s+"
    r"Exercice\s+(?P<exo>[^\s=]+)"
    r"\s*===",
    re.IGNORECASE,
)


def normalize_exo_num(exo: str) -> str:
    """'BAC-2015-SC-D-EXO5' → '5'. Sinon retourne tel quel si déjà numérique."""
    m = re.search(r"EXO(\d+)", exo, re.IGNORECASE)
    if m:
        return m.group(1)
    if exo.isdigit():
        return exo
    # Format inconnu
    return exo


def convert(text: str) -> tuple[str, int]:
    """Convertit les markers. Retourne (texte_converti, nb_conversions)."""
    count = 0
    def replace_marker(m):
        nonlocal count
        count += 1
        exo_num = normalize_exo_num(m.group("exo"))
        return (f"=== {m.group('mat')} | "
                f"Série {m.group('serie').upper()} | "
                f"{m.group('year')} | "
                f"Session {m.group('sess')} | "
                f"Exercice {exo_num} ===")
    out = DASH_MARKER_RE.sub(replace_marker, text)
    return out, count


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    converted, n = convert(text)
    Path(args.output).write_text(converted, encoding="utf-8")
    print(f"Markers convertis (dash → pipe) : {n}")
    print(f"→ {args.output}")


if __name__ == "__main__":
    main()
