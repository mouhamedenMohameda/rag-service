"""Parse les fichiers backup au format PDF brut et les convertit au format structuré.

Le backup `exo_extracted_backup/science-bacc.txt` (et potentiellement d'autres)
est un dump brut concaténant plusieurs PDFs sources, sans format unifié :

    Bac C 2023 SN sc.pdf

    I- Maitrise des connaissances
    QCM (3 points)
    1- ...

    II-Compétences méthodologiques :
    Exercice 1 (5 points)
    ...

    Bac C 2010 SN sn.pdf
    Divisions cellulaires: (12pts)
    ...

Ce script :
  1. Identifie les sections PDF (filename → année, session, filière).
  2. Découpe chaque section en blocs d'exercices via plusieurs heuristiques :
     - `Exercice N (Xpts/X points)` (numéroté)
     - `QCM (Xpts)` (= ex1 traditionnellement)
     - `QROC (Xpts)` (= ex0 ou ex1)
     - `<Titre>: (Xpts)` (ex: "Reproduction: (7pts)")
  3. Numérote les exos dans l'ordre d'apparition.
  4. Écrit un fichier au format `=== Sciences Naturelles | Série C | YYYY | Session X | Exercice N ===`
     consommable par `import_extracted_folder.py`.

Usage :
    .venv/bin/python scripts/parse_raw_backup.py \\
        --input exo_extracted_backup/science-bacc.txt \\
        --filiere C --matiere svt \\
        --output /tmp/parsed_bacc_svt.txt
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


# Pattern PDF : "Bac C 2023 SN sc.pdf", "Bac d SN 2014 sn.pdf", "Bac D PC 2015 sn corrigé.pdf"
PDF_RE = re.compile(
    r"Bac\s+(?P<serie>[CcDd])\s+"
    r"(?:(?P<subj1>SN|PC|sn|pc)\s+)?"
    r"(?P<year>\d{4})\s+"
    r"(?P<subj2>SN|PC|sn|pc)?\s*"
    r"(?P<sess>sn|sc)"
    r"(?:[\s\w]*)\.pdf",
    re.IGNORECASE,
)


def detect_matiere_from_pdf(pdf_filename: str, default: str) -> str:
    """Détecte matière (svt/pc/math) depuis le nom de PDF.
    'Bac C 2023 SN sc.pdf' → svt (SN = Sciences Naturelles)
    'Bac D PC 2015 sn.pdf' → pc
    """
    s = pdf_filename.upper()
    if " PC " in s or " PC." in s:
        return "pc"
    if " SN " in s or " SN." in s:
        return "svt"
    # Pas explicite → fallback
    return default


# Patterns d'exos, par ordre de priorité
EXO_PATTERNS = [
    # `Exercice N (Xpts)` ou `Exercice N (X points)`
    re.compile(r"(?P<full>Exercice\s+(?P<num>\d+)\s*\([^)]+\))", re.IGNORECASE),
    # `QCM (Xpts)` — numéro à attribuer
    re.compile(r"(?P<full>QCM\s*\([^)]+\))", re.IGNORECASE),
    # `QROC (Xpts)`
    re.compile(r"(?P<full>QROC\s*\([^)]+\))", re.IGNORECASE),
    # `Exercice (Xpts)` sans numéro
    re.compile(r"(?P<full>Exercice\s*\([^)]+\))", re.IGNORECASE),
    # `<Titre>: (Xpts)` — titre court suivi de deux-points + parenthèses
    # ex "Reproduction: (7pts)", "Physiologie nerveuse: (6pts)"
    re.compile(r"(?P<full>(?<=\n)[A-ZÉÈ][A-Za-zÉÈéèàâêîôûç\s']{3,40}\s*:\s*\([^)]+\))"),
]


def parse_pdf_filename(match) -> tuple[str, int, str]:
    """Extrait (filière, année, session) du nom de PDF."""
    serie = match.group("serie").upper()  # C ou D
    year = int(match.group("year"))
    sess = match.group("sess").lower()
    session = "Normale" if sess == "sn" else "Complémentaire"
    return serie, year, session


def find_exo_starts(text: str) -> list[tuple[int, str]]:
    """Trouve les positions de début d'exercices dans le texte.

    Retourne liste de (position, header_match) triée par position.
    """
    found = []
    for pat in EXO_PATTERNS:
        for m in pat.finditer(text):
            found.append((m.start(), m.group("full")))
    # Dédupliquer par position (un même point peut matcher 2 patterns)
    found.sort()
    deduped = []
    last_pos = -100
    for pos, h in found:
        if pos - last_pos < 5:
            continue  # même endroit, garde le premier
        deduped.append((pos, h))
        last_pos = pos
    return deduped


def split_exos(section_text: str) -> list[tuple[str, str]]:
    """Découpe une section PDF en blocs (header, contenu)."""
    starts = find_exo_starts(section_text)
    if not starts:
        return []
    blocks = []
    for i, (pos, header) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(section_text)
        # Le contenu inclut le header (utile pour le LLM/lecteur)
        block = section_text[pos:end].strip()
        blocks.append((header, block))
    return blocks


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Fichier backup brut")
    p.add_argument("--filiere", required=True, choices=["C", "D"])
    p.add_argument("--matiere", required=True, choices=["math", "pc", "svt"],
                   help="Matière par défaut si non-détectable depuis nom PDF")
    p.add_argument("--output", required=True, help="Fichier structuré à produire")
    p.add_argument("--min-block-size", type=int, default=150,
                   help="Taille minimum d'un bloc pour être conservé (chars)")
    args = p.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")

    # Trouver toutes les sections PDF
    pdf_matches = list(PDF_RE.finditer(text))
    print(f"Sections PDF trouvées : {len(pdf_matches)}")

    label_map = {"svt": "Sciences Naturelles", "pc": "Sciences Physiques", "math": "Mathématiques"}

    output_blocks = []
    failed_sections = []

    for i, m in enumerate(pdf_matches):
        serie, year, session = parse_pdf_filename(m)
        if serie != args.filiere:
            print(f"  ⚠️  skip {m.group(0)} (filière {serie} ≠ {args.filiere})")
            continue

        # Détecter la matière de cette section depuis le nom du PDF
        section_matiere = detect_matiere_from_pdf(m.group(0), args.matiere)
        matiere_label = label_map[section_matiere]

        # Contenu = de la fin du match au début du suivant
        start = m.end()
        end = pdf_matches[i + 1].start() if i + 1 < len(pdf_matches) else len(text)
        section = text[start:end]

        blocks = split_exos(section)
        if not blocks:
            failed_sections.append((m.group(0), len(section)))
            print(f"  ❌ {m.group(0)} ({len(section)} chars) → aucun exo détecté")
            continue

        # Filtrer les blocs trop petits (probablement faux positifs)
        blocks = [(h, b) for h, b in blocks if len(b) >= args.min_block_size]
        if not blocks:
            failed_sections.append((m.group(0), len(section)))
            print(f"  ❌ {m.group(0)} → tous les blocs < {args.min_block_size} chars")
            continue

        print(f"  ✅ {m.group(0)} → {len(blocks)} exos détectés")
        for ex_num, (header, body) in enumerate(blocks, start=1):
            output_blocks.append({
                "matiere": matiere_label,
                "filiere": serie,
                "year": year,
                "session": session,
                "ex_num": ex_num,
                "header_original": header,
                "body": body,
            })

    # Écriture du fichier de sortie
    out_lines = []
    for b in output_blocks:
        marker = (f"=== {b['matiere']} | Série {b['filiere']} | {b['year']} | "
                  f"Session {b['session']} | Exercice {b['ex_num']} ===")
        out_lines.append(marker)
        out_lines.append("")
        out_lines.append(b["body"])
        out_lines.append("")
        out_lines.append("")

    Path(args.output).write_text("\n".join(out_lines), encoding="utf-8")
    print()
    print("=" * 70)
    print(f"Total exos extraits : {len(output_blocks)}")
    print(f"Sections en échec   : {len(failed_sections)}")
    if failed_sections:
        print("  Échecs :")
        for name, size in failed_sections:
            print(f"    - {name} ({size} chars)")
    print(f"→ {args.output} écrit")


if __name__ == "__main__":
    main()
