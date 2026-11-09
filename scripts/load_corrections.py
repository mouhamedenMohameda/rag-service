"""Charge les corrections d'un module de content/ qui définit
``CORRECTIONS = {id: {enonce, correction, note}}`` (énoncé vérifié + correction).

    python scripts/load_corrections.py corrections_d_2010_2014            # simulation
    python scripts/load_corrections.py corrections_d_2010_2014 --apply    # écriture

Règles :
  - le contrôle qualité (content_check.py) tourne d'abord ; --apply est refusé
    s'il trouve une erreur ;
  - la correction n'est écrite que si l'énoncé en base est EXACTEMENT l'énoncé
    vérifié du module (sinon la correction pourrait ne pas lui correspondre) :
    charger d'abord les énoncés (scripts/load_enonces.py) ;
  - un exercice validé par l'admin n'est jamais modifié ;
  - une correction déjà présente est gardée, sauf --force-corrections ;
  - tout reste en brouillon ; sauvegarde automatique avant écriture.
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
from content_check import check_module  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("content", help="module de content/ avec CORRECTIONS = {id: {...}}")
    ap.add_argument("--apply", action="store_true", help="écrire (sinon simulation)")
    ap.add_argument("--force-corrections", action="store_true",
                    help="remplacer une correction déjà présente (exercice non validé)")
    ap.add_argument("--skip-check", action="store_true", help="ne pas bloquer sur le contrôle (déconseillé)")
    args = ap.parse_args()

    module = importlib.import_module(args.content)
    corrections: dict[str, dict] = module.CORRECTIONS

    qrep, st = check_module(module)
    print(f"Contrôle qualité : {st['textes']} textes, {st['formules']} formules, {st['calculs']} calculs, "
          f"{st['controles_math']} contrôles math — {len(qrep.errors)} erreur(s), {len(qrep.warnings)} avertissement(s)")
    for e in qrep.errors[:20]:
        print(f"  ✗ {e}")
    for w in qrep.warnings[:10]:
        print(f"  ⚠ {w}")
    if qrep.errors and args.apply and not args.skip_check:
        print("Arrêt : corrige les erreurs ci-dessus avant --apply (détail : python scripts/check_content.py).")
        return 1

    json_path = Path(os.environ.get("RAG_JSON_BAC", ROOT / "json_bac.json")).resolve()
    store = AdminStore(json_path=json_path, backup_dir=json_path.parent / "json_backups")
    data = store.load()
    by_id = {e["id"]: e for e in data}

    print(f"\n== {args.content} — {len(corrections)} correction(s) — "
          f"{'ÉCRITURE' if args.apply else 'SIMULATION (ajoute --apply pour écrire)'}\n")
    changes = problems = 0
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    for eid, item in corrections.items():
        e = by_id.get(eid)
        if e is None:
            print(f"  ✗ {eid} : exercice introuvable"); problems += 1; continue
        if e.get("validated_by_admin"):
            print(f"  · {eid} : validé par l'admin, non modifié"); continue
        if (e.get("ennonce_complet") or "").strip() != item["enonce"].strip():
            print(f"  ✗ {eid} : l'énoncé en base n'est pas l'énoncé vérifié — charge d'abord les énoncés")
            problems += 1
            continue
        new_corr = item["correction"].strip()
        cur = (e.get("correction") or "").strip()
        if cur == new_corr:
            print(f"  = {eid} : déjà à jour"); continue
        if cur and not args.force_corrections:
            print(f"  · {eid} : correction déjà présente (--force-corrections pour la remplacer)"); continue
        e["correction"] = new_corr + "\n"
        if item.get("note"):
            old = (e.get("note_admin") or "").strip()
            e["note_admin"] = (old + " | Correction : " + item["note"]).strip(" |") if old else "Correction : " + item["note"]
        e["validated_by_admin"] = False
        e["updated_at"] = now
        changes += 1
        print(f"  + {eid} : correction" + (" ⚠ note" if item.get("note") else ""))

    if not args.apply:
        print(f"\nSimulation : {changes} correction(s) à écrire, {problems} problème(s). Rien n'a été écrit.")
        return 0
    if changes:
        store.save(data)
    print(f"\nÉcrit : {changes} correction(s) en brouillon ({problems} problème(s)). Sauvegarde dans json_backups/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
