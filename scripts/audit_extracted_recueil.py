#!/usr/bin/env python3
"""Audit rapide d'un JSON produit par extract_recueil_exos.py.

Affiche : nombre d'exos par session, énoncés courts (<200c), corrigés vides,
balises résiduelles [[…]] non consommées.

Usage :
    .venv/bin/python scripts/audit_extracted_recueil.py exo_extracted/<file>.json
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

RESIDUAL_MARKER_RE = re.compile(r"\[\[(?:EXO|PROBLEME|CORRIGE)[^\]]*\]\]")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: audit_extracted_recueil.py <file.json>", file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))

    print(f"Total exos : {len(data)}\n")
    by_session: dict[tuple[int, str], list[int]] = defaultdict(list)
    short_e, empty_c, leaks = [], [], []
    for e in data:
        by_session[(e["annee"], e["session"])].append(e["exercice_numero"])
        if len(e.get("ennonce_complet", "")) < 200:
            short_e.append((e["id"], len(e["ennonce_complet"])))
        if not e.get("correction"):
            empty_c.append(e["id"])
        for field in ("ennonce_complet", "correction"):
            if RESIDUAL_MARKER_RE.search(e.get(field, "") or ""):
                leaks.append(f"{e['id']}::{field}")

    for k in sorted(by_session, reverse=True):
        print(f"  {k[0]} {k[1]:<14} {len(by_session[k])} exos : {by_session[k]}")
    print()
    print(f"Énoncé < 200c   : {len(short_e)}  {short_e[:5]}")
    print(f"Corrigé vide    : {len(empty_c)}  {empty_c[:5]}")
    print(f"Balises résid.  : {len(leaks)}    {leaks[:5]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
