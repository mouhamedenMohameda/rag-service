#!/usr/bin/env python3
"""
Fusionne plusieurs JSONs d'exercices et génère un .tex compilable.
Usage:
  python3 merge_and_export.py
  python3 merge_and_export.py --tex-out bac_math_complet.tex
"""
import json
import argparse
from pathlib import Path


LATEX_HEADER = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{geometry}
\usepackage{parskip}
\geometry{margin=2cm}

\newcommand{\exosection}[4]{%
  \bigskip
  \noindent\rule{\linewidth}{0.4pt}\\[2pt]
  \noindent{\large\bfseries #1 — Exercice #2 (#3 pts)}\\
  \noindent\small\textit{#4}
  \medskip
}

\begin{document}
"""

LATEX_FOOTER = r"\end{document}"

SESSION_LABELS = {"normale": "Normale", "complementaire": "Complémentaire"}
FILIERE_LABELS = {"C": "Bac C", "D": "Bac D"}


def enonce_to_latex(enonce: str) -> str:
    """Convertit la chaîne enonce JSON en blocs LaTeX propres."""
    text = enonce.replace('\r\n', '\n').replace('\r', '\n')
    # Double newline → paragraph break
    text = text.replace('\n\n', '\n\n\\medskip\n\n')
    # Single newline → LaTeX paragraph
    text = text.replace('\n', '\n\n')
    return text


def exercise_to_latex(ex: dict) -> str:
    meta = ex['metadata']
    matiere = meta.get('matiere', '').upper()
    annee = meta.get('annee', '?')
    session = SESSION_LABELS.get(meta.get('session', ''), meta.get('session', ''))
    filiere_list = meta.get('filiere') or ['?']
    filiere = ' / '.join(FILIERE_LABELS.get(f, f) for f in filiere_list)
    numero = meta.get('numero_exercice', '?')
    bareme = meta.get('bareme', '?')
    chapitres = ', '.join(meta.get('chapitres') or [])
    source = meta.get('source_sujet', '')

    titre = f"{filiere} — {matiere} {annee} (session {session})"
    sous_titre = chapitres or source

    enonce = ex.get('enonce') or ''
    correction = ex.get('correction') or ''

    lines = []
    lines.append(f"\\exosection{{{titre}}}{{{numero}}}{{{bareme}}}{{{sous_titre}}}")
    lines.append('')
    lines.append(enonce_to_latex(enonce))

    if correction:
        lines.append('')
        lines.append(r'\bigskip')
        lines.append(r'\noindent\textbf{\underline{Correction :}}')
        lines.append('')
        lines.append(enonce_to_latex(correction))

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json-dir', default='exercises_extracted',
                        help='Dossier contenant les JSONs')
    parser.add_argument('--tex-out', default='bac_math_complet.tex',
                        help='Fichier .tex de sortie')
    parser.add_argument('--matiere', default='math',
                        help='Filtrer par matière (math, svt, etc.)')
    parser.add_argument('--filiere', help='Filtrer par filière (C ou D)')
    args = parser.parse_args()

    json_dir = Path(args.json_dir)
    all_exercises = {}

    # Charger tous les JSONs du dossier
    json_files = sorted(json_dir.glob('*.json'))
    print(f"Chargement de {len(json_files)} fichier(s) JSON depuis {json_dir}/")
    for jf in json_files:
        try:
            with open(jf, encoding='utf-8') as f:
                data = json.load(f)
            for ex in data:
                eid = ex.get('id', '')
                if eid:
                    all_exercises[eid] = ex
            print(f"  ✓ {jf.name} → {len(data)} exercice(s)")
        except Exception as e:
            print(f"  ✗ {jf.name} : {e}")

    print(f"\n{len(all_exercises)} exercices au total (dédupliqués par id)")

    def get_matiere(e):
        """Déduit et normalise la matière (physique/chimie → pc)."""
        m = e.get('metadata', {}).get('matiere') or e.get('matiere')
        if not m:
            eid = e.get('id', '').lower()
            if eid.startswith('math'):
                m = 'math'
            elif eid.startswith('physique') or eid.startswith('chimie'):
                m = 'physique'
            elif eid.startswith('svt'):
                m = 'svt'
        if m in ('physique', 'chimie', 'physique-chimie'):
            return 'pc'
        return m

    # Filtres
    exercises = list(all_exercises.values())
    if args.matiere:
        matiere_filter = args.matiere
        exercises = [e for e in exercises if get_matiere(e) == matiere_filter]
    if args.filiere:
        exercises = [e for e in exercises if args.filiere in (e.get('metadata', {}).get('filiere') or [])]

    print(f"{len(exercises)} exercices après filtres (matière={args.matiere}, filière={args.filiere or 'toutes'})")

    # Trier : par année DESC, session (normale avant complémentaire), numéro
    session_order = {'normale': 0, 'complementaire': 1}
    exercises.sort(key=lambda e: (
        -(e.get('metadata', {}).get('annee') or 0),
        session_order.get(e.get('metadata', {}).get('session', ''), 2),
        e.get('metadata', {}).get('numero_exercice') or 0
    ))

    # Regrouper par année + session pour les titres de section
    sections = {}
    for ex in exercises:
        meta = ex.get('metadata', {})
        annee = meta.get('annee', 0)
        session = meta.get('session', 'normale')
        filiere_list = meta.get('filiere') or ['C']
        filiere = '/'.join(filiere_list)
        key = (annee, session, filiere)
        sections.setdefault(key, []).append(ex)

    # Générer le .tex
    tex_out = Path(args.tex_out)
    with open(tex_out, 'w', encoding='utf-8') as f:
        f.write(LATEX_HEADER)
        current_year = None
        for (annee, session, filiere), exs in sorted(
            sections.items(),
            key=lambda kv: (-kv[0][0], session_order.get(kv[0][1], 2))
        ):
            if annee != current_year:
                current_year = annee
                f.write(f"\n\\section*{{\\centering Année {annee}}}\n\\hrule\n\n")

            session_label = SESSION_LABELS.get(session, session)
            filiere_label = ' / '.join(FILIERE_LABELS.get(fi, fi) for fi in filiere.split('/'))
            f.write(f"\n\\subsection*{{{filiere_label} — Session {session_label}}}\n\n")

            for ex in exs:
                f.write(exercise_to_latex(ex))
                f.write('\n\n')

        f.write('\n' + LATEX_FOOTER + '\n')

    print(f"\n✓ Fichier généré : {tex_out}")
    print(f"  → {len(exercises)} exercices, {len(sections)} section(s)")


if __name__ == '__main__':
    main()
