#!/usr/bin/env python3
"""Sanitizer LaTeX/OCR — corrige les patterns toxiques laissés par Groq Vision.

Patterns ciblés (observés sur les extractions Bac C maths) :
1.  $4points$ / $0,5pt$ / $0,25pt$  → texte normal (parens artificielles transformées en $)
2.  $nonnuméroté$ / $points$        → mot français entouré inutilement de $
3.  ###Texte / ####Texte (collés)   → ### Texte (espace après les #)
4.  $$ orphelins (count impair)     → log d'alerte
5.  Texte LaTeX hors $...$ avec backslash → log d'alerte (à traiter manuellement)

Stratégie : on n'enlève les `$` autour d'un contenu que si CE contenu :
- ne contient AUCUN backslash (\\)
- ne contient AUCUN caractère math typique (^ _ { } = + < > | & ~)
- est purement alphanumérique français + ponctuation simple (espaces, virgules, points, parens, tirets)

Usage :
    .venv/bin/python scripts/sanitize_ocr_latex.py \\
        --source json_bac.json \\
        --filter annee=2014 \\
        [--dry-run] [--field ennonce_complet,correction]
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# 1. Mot français purement textuel entouré de $...$ (à dé-dollar-iser).
#    Match : $4points$, $0,5pt$, $non numéroté$, $points$, $5 pt$ …
#    Refuse si contient \, ^, _, {, }, =, etc.
TEXTY_DOLLAR_RE = re.compile(
    r"\$([A-Za-zÀ-ÖØ-öø-ÿ0-9][A-Za-zÀ-ÖØ-öø-ÿ0-9 ,.\-()']{0,40})\$"
)

# 2a. $0,5pt$ / $4 points$ — chiffre + unité de barème sans parenthèses.
PT_DOLLAR_RE = re.compile(r"\$(\d+(?:[,.]\d+)?\s*(?:points?|pts?))\$")

# 2b. $(0,5pt)$ / $(0,75 pts)$ — variante avec parenthèses incluses dans les dollars
PAREN_PT_DOLLAR_RE = re.compile(
    r"\$\(\s*(\d+(?:[,.]\d+)?)\s*(points?|pts?)\s*\)\$"
)

# 3. Markdown headings collés au texte : "####Texte" → "#### Texte"
MD_HEADER_GLUE_RE = re.compile(r"^(#{1,6})([^#\s])", re.MULTILINE)

# 4. Raccourcis ensembles hors mathbb (alerte seulement)
SET_SHORTCUT_RE = re.compile(r"(?<!\\mathbb\{)\\([NZRQC])(?![a-zA-Z])")


def is_safe_to_unwrap(content: str) -> bool:
    """True si `$content$` est *certainement* du texte français à dé-dollar-iser.

    Très conservateur — il vaut mieux laisser passer un faux positif qu'effacer
    du LaTeX légitime (noms géométriques $ABC$, points $M'$, $a-i$, etc.).

    Accepte UNIQUEMENT :
    - "4 points" / "0,5 pt" / "0,75 pts" (barème entre dollars)
    - mot français unique avec un accent (é, à, ç, ô…), longueur >= 4
    """
    if any(c in content for c in "\\^_{}|<>~=+/*"):
        return False
    s = content.strip()

    # "4 points", "0,5 pt", "0,75 pts"
    if re.fullmatch(r"\d+(?:[,.]\d+)?\s*(?:points?|pts?)", s):
        return True
    # mot français UNIQUE avec accent. Pas d'espace, pas de tiret entre mots.
    if (
        re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ]{4,30}", s)
        and re.search(r"[à-ÿ]", s)
    ):
        return True
    return False


def sanitize(text: str) -> tuple[str, dict]:
    """Renvoie (texte sanitisé, stats)."""
    stats = {"dollar_unwrapped": 0, "pt_unwrapped": 0, "md_unglued": 0, "warn_set": 0, "warn_unmatched": 0}
    out = text

    # 1. $4points$ / $non numéroté$ / etc.
    def _unwrap(m: re.Match) -> str:
        inner = m.group(1)
        if is_safe_to_unwrap(inner):
            stats["dollar_unwrapped"] += 1
            return inner
        return m.group(0)
    out = TEXTY_DOLLAR_RE.sub(_unwrap, out)

    # 2a. $0,5pt$ → 0,5pt
    def _pt(m: re.Match) -> str:
        stats["pt_unwrapped"] += 1
        return m.group(1)
    out = PT_DOLLAR_RE.sub(_pt, out)

    # 2b. $(0,5pt)$ → (0,5 pt)
    def _paren_pt(m: re.Match) -> str:
        stats["pt_unwrapped"] += 1
        return f"({m.group(1)} {m.group(2)})"
    out = PAREN_PT_DOLLAR_RE.sub(_paren_pt, out)

    # 3. ####Texte → #### Texte
    def _md(m: re.Match) -> str:
        stats["md_unglued"] += 1
        return m.group(1) + " " + m.group(2)
    out = MD_HEADER_GLUE_RE.sub(_md, out)

    # 4. Alerte : raccourcis \R, \N, \Z hors $...$ (KaTeX les voit comme erreurs)
    stats["warn_set"] = len(SET_SHORTCUT_RE.findall(out))

    # 5. Alerte : nombre de $ impairs (délimiteur orphelin)
    code_free = re.sub(r"\$\$[^$]*\$\$", "", out)
    single = code_free.count("$") - 2 * code_free.count("$$")
    if single % 2 != 0:
        stats["warn_unmatched"] = 1

    return out, stats


def parse_filter(s: str) -> tuple[str, str]:
    if "=" not in s:
        raise argparse.ArgumentTypeError(f"filtre invalide: {s!r}")
    k, v = s.split("=", 1)
    return k.strip(), v.strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", default="json_bac.json")
    ap.add_argument("--filter", type=parse_filter, action="append", default=[])
    ap.add_argument("--field", default="ennonce_complet,correction",
                    help="Champs à sanitiser (csv)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--show-samples", type=int, default=3, help="Combien d'exemples diff à afficher")
    args = ap.parse_args()

    fields = [f.strip() for f in args.field.split(",")]
    data = json.loads(Path(args.source).read_text(encoding="utf-8"))

    total = {"dollar_unwrapped": 0, "pt_unwrapped": 0, "md_unglued": 0, "warn_set": 0, "warn_unmatched": 0}
    samples: list[tuple[str, str, str]] = []  # (id, field, before/after snippet)
    touched_ids: list[str] = []
    untouched_warn: list[str] = []

    for e in data:
        if args.filter and not all(str(e.get(k)) == v for k, v in args.filter):
            continue
        changed = False
        for f in fields:
            v = e.get(f) or ""
            if not v:
                continue
            new, stats = sanitize(v)
            for k_, v_ in stats.items():
                total[k_] += v_
            if new != v:
                changed = True
                if len(samples) < args.show_samples:
                    # Trouve la 1ère différence pour snippet
                    for i, (a, b) in enumerate(zip(v, new)):
                        if a != b:
                            snip_a = v[max(0, i-30):i+50]
                            snip_b = new[max(0, i-30):i+50]
                            samples.append((e["id"], f, f"{snip_a!r}\n      → {snip_b!r}"))
                            break
                e[f] = new
            if stats["warn_set"] or stats["warn_unmatched"]:
                untouched_warn.append(f"{e['id']}::{f} (set={stats['warn_set']}, unmatched_dollar={stats['warn_unmatched']})")
        if changed:
            touched_ids.append(e["id"])

    print(f"Entrées modifiées : {len(touched_ids)}")
    print(f"  $...$ retirés autour de texte français : {total['dollar_unwrapped']}")
    print(f"  $0,5pt$ → 0,5pt                        : {total['pt_unwrapped']}")
    print(f"  ###Texte → ### Texte                   : {total['md_unglued']}")
    print(f"\nAlertes (à examiner manuellement) :")
    print(f"  Raccourcis \\R/\\N/\\Z hors mathbb       : {total['warn_set']}")
    print(f"  $ orphelins (count impair)             : {total['warn_unmatched']}")
    if untouched_warn:
        print(f"  Exemples ({min(len(untouched_warn), 5)}/{len(untouched_warn)}):")
        for w in untouched_warn[:5]:
            print(f"    - {w}")
    if samples:
        print(f"\nExemples de changements ({len(samples)}) :")
        for sid, sf, snip in samples:
            print(f"  [{sid}::{sf}]")
            print(f"      {snip}")

    if args.dry_run:
        print("\n(dry-run, rien écrit)")
        return 0

    if not touched_ids:
        print("Aucune modification, rien à écrire.")
        return 0

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = Path(args.source).with_name(f"json_bac.backup_{ts}_sanitize.json")
    shutil.copy2(args.source, backup)
    print(f"\n✓ Backup : {backup.name}")
    Path(args.source).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Écrit {args.source}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
