"""Remplit des exercices « cases vides » (sans énoncé) à partir d'un module de
content/ qui définit ``ENONCES = {id: {chapitre, chapitres, enonce, note}}``.

    python scripts/load_enonces.py enonces_d_2010_2014            # simulation
    python scripts/load_enonces.py enonces_d_2010_2014 --apply    # écriture

Règles :
  - l'exercice doit déjà exister en base (id du squelette) ;
  - un exercice validé par l'admin n'est jamais modifié ;
  - un énoncé déjà présent n'est pas remplacé (sauf --force), sauf si l'exercice
    est encore marqué « squelette » ou que l'entrée porte ``replace_ocr: True``
    (texte OCR jamais vérifié) ; l'ancien texte est gardé dans ``ennonce_ocr`` ;
  - tout reste en brouillon (validated_by_admin = False) ;
  - le chapitre doit déjà exister pour la même matière ;
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
    ap.add_argument("content", help="module de content/ avec ENONCES = {id: {...}}")
    ap.add_argument("--apply", action="store_true", help="écrire (sinon simulation)")
    ap.add_argument("--force", action="store_true", help="remplacer un énoncé déjà présent (exercice non validé)")
    args = ap.parse_args()

    enonces: dict[str, dict] = importlib.import_module(args.content).ENONCES
    json_path = Path(os.environ.get("RAG_JSON_BAC", ROOT / "json_bac.json")).resolve()
    store = AdminStore(json_path=json_path, backup_dir=json_path.parent / "json_backups")
    data = store.load()
    by_id = {e["id"]: e for e in data}
    known: dict[str, set] = {}
    for e in data:
        if e.get("chapitre"):
            known.setdefault(e.get("matiere_id"), set()).add(e["chapitre"])

    print(f"== {args.content} — {len(enonces)} énoncé(s) — "
          f"{'ÉCRITURE' if args.apply else 'SIMULATION (ajoute --apply pour écrire)'}\n")
    changes = errors = 0
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    for eid, item in enonces.items():
        e = by_id.get(eid)
        if e is None:
            print(f"  ✗ {eid} : exercice introuvable"); errors += 1; continue
        mat = e.get("matiere_id")
        bad = [c for c in [item["chapitre"], *item.get("chapitres", [])] if c not in known.get(mat, set())]
        if bad:
            print(f"  ✗ {eid} : chapitre inconnu {bad}"); errors += 1; continue
        if e.get("validated_by_admin"):
            print(f"  · {eid} : validé par l'admin, non modifié"); continue
        cur = (e.get("ennonce_complet") or "").strip()
        if cur == item["enonce"].strip() and e.get("chapitre") == item["chapitre"]:
            print(f"  = {eid} : déjà à jour"); continue
        has_text = len(cur) >= 40
        # replace_ocr : une seule fois (tant que le texte OCR n'a pas été mis de côté),
        # pour ne jamais écraser une correction faite ensuite par l'admin.
        ocr_once = item.get("replace_ocr") and not e.get("ennonce_ocr")
        if has_text and not e.get("is_skeleton") and not (args.force or ocr_once):
            print(f"  · {eid} : énoncé déjà présent (--force pour remplacer)"); continue
        if has_text and not e.get("ennonce_ocr"):
            e["ennonce_ocr"] = e["ennonce_complet"]
        e["ennonce_complet"] = item["enonce"].strip() + "\n"
        e["chapitre"] = item["chapitre"]
        e["chapitres"] = item.get("chapitres") or None
        e["is_skeleton"] = False
        e["validated_by_admin"] = False
        if item.get("note"):
            e["note_admin"] = item["note"]
        e["updated_at"] = now
        changes += 1
        extra = f" (+ {', '.join(item['chapitres'])})" if item.get("chapitres") else ""
        print(f"  + {eid} : {item['chapitre']}{extra}" + (" ⚠ note" if item.get("note") else ""))

    if errors:
        print(f"\n{errors} erreur(s) : rien n'a été écrit.")
        return 1
    if not args.apply:
        print(f"\nSimulation : {changes} exercice(s) à remplir, rien n'a été écrit.")
        return 0
    if changes:
        store.save(data)
    print(f"\nÉcrit : {changes} énoncé(s) en brouillon. Sauvegarde dans json_backups/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
