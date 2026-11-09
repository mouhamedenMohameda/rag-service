"""Contrôle qualité d'un ou plusieurs modules de content/ (voir content_check.py).

    python scripts/check_content.py enonces_logexp_d fonctions_log_exp
    python scripts/check_content.py --all          # tous les modules de content/

Code de sortie 1 s'il reste au moins une ERREUR.
"""
from __future__ import annotations

import argparse
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "content"))

from content_check import check_module  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("modules", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--no-katex", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="n'afficher que les erreurs")
    args = ap.parse_args()
    mods = args.modules or []
    if args.all:
        mods = sorted(p.stem for p in (ROOT / "content").glob("*.py") if not p.stem.startswith("_"))
    if not mods:
        ap.error("donner un module ou --all")
    total_err = 0
    for name in mods:
        mod = importlib.import_module(name)
        rep, st = check_module(mod, katex=not args.no_katex)
        total_err += len(rep.errors)
        print(f"== {name} : {st['textes']} textes, {st['formules']} formules, "
              f"{st['calculs']} calculs revérifiés, {st.get('racines', 0)} racines retrouvées, {st['controles_math']} contrôles math OK, {st.get('acceptes', 0)} avertissement(s) déjà relus — {len(rep.errors)} erreur(s), "
              f"{len(rep.warnings)} avertissement(s)")
        for e in rep.errors:
            print("  ✗ ERREUR   ", e)
        if not args.quiet:
            for w in rep.warnings:
                print("  ⚠ attention", w)
    return 1 if total_err else 0


if __name__ == "__main__":
    raise SystemExit(main())
