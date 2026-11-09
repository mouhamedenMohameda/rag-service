"""Range des exercices dans un chapitre (champ ``chapitre``) à partir d'un module
de content/ qui définit ``CHAPITRES = {exercice_id: "Nom du chapitre"}``.

    python scripts/set_chapters.py chapitres_d_2010            # simulation
    python scripts/set_chapters.py chapitres_d_2010 --apply    # écriture

Règles :
  - un exercice validé par l'admin n'est jamais modifié ;
  - un exercice qui a déjà un chapitre n'est pas modifié (sauf --force) ;
  - le nom du chapitre doit déjà exister pour la même matière (pas de faute de
    frappe qui créerait un chapitre fantôme) ;
  - sauvegarde automatique dans json_backups/ avant écriture.
"""
from __future__ import annotations

import argparse
import importlib
import os
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "content"))

from admin_api import AdminStore  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("content", help="module de content/ avec CHAPITRES = {id: chapitre}")
    ap.add_argument("--apply", action="store_true", help="écrire (sinon simulation)")
    ap.add_argument("--force", action="store_true", help="remplacer un chapitre déjà posé (exercice non validé)")
    args = ap.parse_args()

    mapping: dict[str, str] = importlib.import_module(args.content).CHAPITRES
    json_path = Path(os.environ.get("RAG_JSON_BAC", ROOT / "json_bac.json")).resolve()
    store = AdminStore(json_path=json_path, backup_dir=json_path.parent / "json_backups")
    data = store.load()
    by_id = {e["id"]: e for e in data}

    known = {}
    for e in data:
        if e.get("chapitre"):
            known.setdefault(e.get("matiere_id"), set()).add(e["chapitre"])

    print(f"== {args.content} — {len(mapping)} exercice(s) — "
          f"{'ÉCRITURE' if args.apply else 'SIMULATION (ajoute --apply pour écrire)'}\n")
    changes = errors = 0
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    for eid, chap in mapping.items():
        e = by_id.get(eid)
        if e is None:
            print(f"  ✗ {eid} : exercice introuvable"); errors += 1; continue
        if chap not in known.get(e.get("matiere_id"), set()):
            print(f"  ✗ {eid} : chapitre inconnu « {chap} »"); errors += 1; continue
        cur = e.get("chapitre") or ""
        if cur == chap:
            print(f"  = {eid} : déjà dans « {chap} »"); continue
        if e.get("validated_by_admin"):
            print(f"  · {eid} : validé par l'admin, non modifié"); continue
        if cur and not args.force:
            print(f"  · {eid} : déjà dans « {cur} » (--force pour remplacer)"); continue
        print(f"  + {eid} : « {cur or '∅'} » → « {chap} »")
        e["chapitre"] = chap
        e["updated_at"] = now
        changes += 1

    if errors:
        print(f"\n{errors} erreur(s) : rien n'a été écrit.")
        return 1
    if not args.apply:
        print(f"\nSimulation : {changes} changement(s), rien n'a été écrit.")
        return 0
    if changes:
        store.save(data)
    print(f"\nÉcrit : {changes} exercice(s) rangé(s). Sauvegarde dans json_backups/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
