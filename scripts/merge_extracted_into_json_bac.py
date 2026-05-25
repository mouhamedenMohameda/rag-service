#!/usr/bin/env python3
"""Merge un JSON produit par extract_recueil_exos.py dans json_bac.json.

Pour chaque exo extrait :
- Si un exo existe dans json_bac.json avec le même `id` → on UPDATE en place
  les champs : ennonce_complet (remplacé par version OCR fidèle), correction
  (ajouté), fichier (renseigné), updated_at, et flags (is_probleme si présent).
  Les autres champs (notions_traitees, notion_ids, chapitre, chapitres,
  donnees_fournies, matiere/filiere, etc.) sont PRÉSERVÉS.
- Si aucun match (id absent dans json_bac.json) → INSERT à la fin avec un
  squelette de champs vides pour les notions (à remplir plus tard).

Backup horodaté de json_bac.json avant écriture, format aligné sur les backups
existants : `json_bac.backup_<YYYYMMDD>_<HHMMSS>.json`.

Usage :
    .venv/bin/python scripts/merge_extracted_into_json_bac.py \\
        --extracted exo_extracted/math_c_2007sc_2012sc.json \\
        [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

JSON_BAC = Path("json_bac.json")

# Champs sources autorisés à écraser/ajouter sur l'exo existant.
UPDATE_FIELDS = (
    "ennonce_complet",
    "correction",
    "fichier",
    "is_probleme",
    "_source_pages_enonce",
    "_source_pages_corrige",
)

# Champs requis pour une NOUVELLE entrée (squelette compatible json_bac.json).
NEW_SKELETON = {
    "chapitre": "",
    "chapitres": [],
    "notions_traitees": [],
    "donnees_fournies": {},
    "notion_ids": [],
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--extracted", required=True, help="JSON produit par extract_recueil_exos.py")
    ap.add_argument("--dry-run", action="store_true", help="Affiche le diff sans écrire")
    args = ap.parse_args()

    extracted = json.loads(Path(args.extracted).read_text(encoding="utf-8"))
    bac = json.loads(JSON_BAC.read_text(encoding="utf-8"))
    by_id = {e["id"]: i for i, e in enumerate(bac)}

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    updates: list[str] = []
    inserts: list[str] = []
    diffs: list[tuple[str, int, int]] = []  # (id, old_len, new_len) pour ennonce

    for src in extracted:
        eid = src["id"]
        if eid in by_id:
            tgt = bac[by_id[eid]]
            old_len = len(tgt.get("ennonce_complet") or "")
            new_len = len(src.get("ennonce_complet") or "")
            for f in UPDATE_FIELDS:
                if f in src and src[f] not in (None, ""):
                    tgt[f] = src[f]
            tgt["updated_at"] = now
            updates.append(eid)
            diffs.append((eid, old_len, new_len))
        else:
            # Nouvelle entrée : merge squelette + champs extraits, garde metadata
            new_entry = dict(NEW_SKELETON)
            new_entry.update({
                "id": src["id"],
                "matiere_id": src["matiere_id"],
                "matiere": src.get("matiere", ""),
                "filiere_id": src["filiere_id"],
                "filiere": src.get("filiere", ""),
                "annee": src["annee"],
                "session": src["session"],
                "fichier": src.get("fichier", ""),
                "exercice_numero": src["exercice_numero"],
                "ennonce_complet": src["ennonce_complet"],
                "correction": src.get("correction", src.get("correction", "")),
                "updated_at": now,
            })
            for opt in ("is_probleme", "_source_pages_enonce", "_source_pages_corrige"):
                if opt in src:
                    new_entry[opt] = src[opt]
            bac.append(new_entry)
            inserts.append(eid)

    print(f"Updates : {len(updates)}")
    print(f"Inserts : {len(inserts)}")
    if inserts:
        print("  ↳ nouveaux IDs :", inserts[:10], ("…" if len(inserts) > 10 else ""))

    # Aperçu des plus gros changements d'énoncé (gain de fidélité)
    diffs.sort(key=lambda x: x[2] - x[1], reverse=True)
    print("\nTop 5 gains d'énoncé (chars) :")
    for eid, old, new in diffs[:5]:
        print(f"  {eid:<35} {old:>5} → {new:>5}  (+{new-old})")

    if args.dry_run:
        print("\n(dry-run, rien écrit)")
        return 0

    # Backup horodaté avant écriture
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = JSON_BAC.with_name(f"json_bac.backup_{ts}.json")
    shutil.copy2(JSON_BAC, backup)
    print(f"\n✓ Backup : {backup.name}")

    JSON_BAC.write_text(json.dumps(bac, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Écrit {JSON_BAC} ({len(bac)} entrées)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
