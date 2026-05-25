#!/usr/bin/env python3
"""Patch post-extraction des 2 anomalies connues sur math_c_2007sc_2012sc.json.

Anomalies (cf. analyse manuelle vs scans) :
- 2011 SN ex5 : faux exo. C'est la continuation des sous-questions de ex4
  (3.d, 4, 5...). Le sujet original n'a que 4 exos.
- 2007 SC ex3 + ex4 : Partie A et Partie B d'un même "Problème (10 pts)".
  Le sujet réel : Ex1, Ex2, Problème.

Le patch :
1. Fusionne 2011 SN ex5 dans ex4 (ennonce + corrige), supprime ex5.
2. Fusionne 2007 SC ex4 dans ex3 (Partie B → suite de Partie A), supprime ex4.
   ex3 garde exercice_numero=3 mais ennonce démarre par "Problème (10 points)".

Idempotent : si les fusions ont déjà été appliquées (entrée cible absente),
le patch n'écrit rien.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PATH = Path("exo_extracted/math_c_2007sc_2012sc.json")


def find(data, **kw):
    for i, e in enumerate(data):
        if all(e.get(k) == v for k, v in kw.items()):
            return i, e
    return -1, None


def _strip_trailing_page_marker(text: str) -> str:
    # Retire un éventuel "<!-- page N -->" en fin de bloc
    import re
    return re.sub(r"\n*<!--\s*page\s+\d+\s*-->\s*$", "", text).rstrip()


def merge(target: dict, src: dict, field: str) -> None:
    a = _strip_trailing_page_marker(target.get(field, "") or "")
    b = (src.get(field, "") or "").strip()
    if not b:
        return
    target[field] = f"{a}\n\n{b}".strip()


def main() -> int:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    changed = False

    # --- 1) 2011 SN : ex5 → ex4 -------------------------------------------
    i5, ex5 = find(data, id="bac-c-2011-sn-math-ex5")
    i4, ex4 = find(data, id="bac-c-2011-sn-math-ex4")
    if ex5 and ex4:
        merge(ex4, ex5, "ennonce_complet")
        merge(ex4, ex5, "correction")
        data.pop(i5)
        changed = True
        print("✓ 2011 SN : ex5 fusionné dans ex4")

    # --- 2) 2007 SC : ex4 → ex3 (Problème) --------------------------------
    i4, ex4 = find(data, id="bac-c-2007-sc-math-ex4")
    i3, ex3 = find(data, id="bac-c-2007-sc-math-ex3")
    if ex4 and ex3:
        # En-tête de ex3 : ajoute "Problème (10 points)" si absent
        if "Problème" not in ex3["ennonce_complet"][:200]:
            ex3["ennonce_complet"] = (
                "Problème (10 points)\n\n" + ex3["ennonce_complet"].lstrip()
            )
        merge(ex3, ex4, "ennonce_complet")
        merge(ex3, ex4, "correction")
        # Track que cet exo est en fait un Problème (utile pour le RAG)
        ex3["is_probleme"] = True
        data.pop(i4)
        changed = True
        print("✓ 2007 SC : ex4 (Partie B) fusionné dans ex3, marqué is_probleme")

    if not changed:
        print("Rien à patcher (déjà appliqué ou anomalies absentes).")
        return 0

    PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"→ {len(data)} exos après patch ({PATH})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
