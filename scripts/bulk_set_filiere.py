"""Bulk update : applique une filière à un ensemble d'exercices.

Sélection :
  --only-validated  → uniquement les entrées validated_by_admin = True
  --matiere X       → uniquement matiere_id == X (filtrer en plus)
  --where-empty     → uniquement les entrées dont filiere_id == "" ou "autre"

Backup automatique avant écriture (dans json_backups/).

Usage typique :
    # Toutes les entrées que j'ai validées → Série C
    python scripts/bulk_set_filiere.py --filiere C --only-validated

    # Toutes les physiques sans filière → Série C
    python scripts/bulk_set_filiere.py --filiere C --matiere physique --where-empty

    # Dry-run pour voir ce qui changerait
    python scripts/bulk_set_filiere.py --filiere C --only-validated --dry-run
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"

FILIERE_LABEL = {
    "C": "Série C",
    "D": "Série D",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--filiere", required=True, choices=list(FILIERE_LABEL.keys()))
    ap.add_argument("--only-validated", action="store_true",
                    help="N'applique qu'aux entrées validated_by_admin=True")
    ap.add_argument("--matiere", default=None,
                    help="N'applique qu'à cette matière (math|physique|chimie|svt)")
    ap.add_argument("--where-empty", action="store_true",
                    help="N'applique qu'aux entrées avec filiere_id vide ou 'autre'")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    if not p.exists():
        print(f"ERREUR : {p} introuvable.", file=sys.stderr)
        return 2

    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("ERREUR : JSON doit être une liste.", file=sys.stderr)
        return 2

    target_label = FILIERE_LABEL[args.filiere]
    changed: list[dict] = []
    for e in data:
        # Filtres de sélection
        if args.only_validated and not e.get("validated_by_admin"):
            continue
        if args.matiere and e.get("matiere_id") != args.matiere:
            continue
        if args.where_empty:
            fid = (e.get("filiere_id") or "").strip().lower()
            if fid and fid != "autre":
                continue
        # Cible : déjà à jour ?
        if e.get("filiere_id") == args.filiere and e.get("filiere") == target_label:
            continue
        # Trace de l'ancien
        prev = (e.get("filiere_id"), e.get("filiere"))
        e["filiere_id"] = args.filiere
        e["filiere"] = target_label
        e["updated_at"] = datetime.now().isoformat(timespec="seconds")
        changed.append({"id": e.get("id"), "from": prev, "to": (args.filiere, target_label)})

    if not changed:
        print("Aucune entrée à modifier (déjà à jour ou aucune ne matche les filtres).")
        return 0

    print(f"\n{len(changed)} entrée(s) à modifier vers '{target_label}' :")
    for c in changed[:20]:
        print(f"  - {c['id']:<35} {str(c['from']):<25} → {c['to']}")
    if len(changed) > 20:
        print(f"  … et {len(changed)-20} autres")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0

    # Backup
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-bulk-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")

    # Écriture atomique
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour ({len(changed)} entrée(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
