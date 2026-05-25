#!/usr/bin/env python3
"""
Génère un fichier .tex compilable depuis le JSON d'exercices extrait.
Usage: python3 json_to_latex.py --input exercises_extracted/bac_2025_vision.json --output bac_2025.tex
"""
import json
import argparse
import re

LATEX_HEADER = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\usepackage{enumitem}
\geometry{margin=2cm}

\title{Exercices Bac Mauritanie}
\date{}
\begin{document}
\maketitle
"""

LATEX_FOOTER = r"\end{document}"


def enonce_to_latex(enonce: str) -> str:
    """Convertit la chaîne enonce (avec \n et LaTeX inline) en blocs LaTeX propres."""
    # Remplacer les \n par de vrais sauts de paragraphe LaTeX
    text = enonce.replace('\n\n', '\n\n\\medskip\n\n')
    text = text.replace('\n', '\n\n')
    return text


def exercise_to_latex(ex: dict) -> str:
    meta = ex['metadata']
    matiere = meta.get('matiere', '').upper()
    annee = meta.get('annee', '')
    session = meta.get('session', '')
    numero = meta.get('numero_exercice', '')
    bareme = meta.get('bareme', '')
    chapitres = ', '.join(meta.get('chapitres') or [])
    source = meta.get('source_sujet', '')

    titre = f"{matiere} — Exercice {numero} ({bareme} pts) — {annee} session {session}"
    if chapitres:
        titre += f"\n\\newline\\textit{{{chapitres}}}"

    enonce = ex.get('enonce') or ''
    correction = ex.get('correction') or ''

    lines = []
    lines.append(f"\\section*{{{titre}}}")
    lines.append(f"\\noindent\\textbf{{Source :}} \\texttt{{{source}}}")
    lines.append('')
    lines.append(enonce_to_latex(enonce))

    if correction:
        lines.append('')
        lines.append(r'\bigskip')
        lines.append(r'\noindent\textbf{Correction :}')
        lines.append('')
        lines.append(enonce_to_latex(correction))

    lines.append(r'\bigskip\hrule\bigskip')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='JSON source')
    parser.add_argument('--output', required=True, help='Fichier .tex de sortie')
    parser.add_argument('--matiere', help='Filtrer par matière (math ou svt)')
    parser.add_argument('--annee', type=int, help='Filtrer par année')
    parser.add_argument('--session', help='Filtrer par session (normale, complementaire)')
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Filtres optionnels
    exercises = data
    if args.matiere:
        exercises = [e for e in exercises if e['metadata'].get('matiere') == args.matiere]
    if args.annee:
        exercises = [e for e in exercises if e['metadata'].get('annee') == args.annee]
    if args.session:
        exercises = [e for e in exercises if e['metadata'].get('session') == args.session]

    print(f"{len(exercises)} exercice(s) à exporter")

    body_parts = [exercise_to_latex(ex) for ex in exercises]
    body = '\n\n'.join(body_parts)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(LATEX_HEADER)
        f.write('\n')
        f.write(body)
        f.write('\n')
        f.write(LATEX_FOOTER)

    print(f"✓ Écrit dans {args.output}")


if __name__ == '__main__':
    main()
