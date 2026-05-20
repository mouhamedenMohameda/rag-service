"""Migration : collapse les filières M / TM / C / autres → C, garde D.

Logique métier Bac mauritanien actuelle (mai 2026) :
- Filières scientifiques effectives = 2 seulement :
    C  (anciennement Math, Math-Tech, "C")
    D  (Sciences Naturelles / SVT)
- Les anciens libellés M, TM, MA, etc. sont des variantes historiques de C.

Ce script normalise tout le JSON existant pour ne plus avoir que C ou D.

Backup auto + dry-run dispo.

Usage :
    python scripts/migrate_filiere_to_cd.py --dry-run
    python scripts/migrate_filiere_to_cd.py
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


def new_filiere(old: str | None) -> str:
    """Mapping unique : tout sauf D devient C."""
    if not old:
        return "C"
    v = old.strip().upper()
    if v == "D":
        return "D"
    return "C"


LABEL = {"C": "Série C", "D": "Série D"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))

    changes: list[tuple[str, str, str]] = []
    for e in data:
        old = e.get("filiere_id") or ""
        new = new_filiere(old)
        if old != new:
            changes.append((e.get("id", "?"), old or "(vide)", new))
            e["filiere_id"] = new
            e["filiere"] = LABEL[new]
            e["updated_at"] = datetime.now().isoformat(timespec="seconds")

    print(f"\n{len(changes)} entrée(s) à migrer (sur {len(data)}) :")
    summary: dict[tuple[str, str], int] = {}
    for _, o, n in changes:
        summary[(o, n)] = summary.get((o, n), 0) + 1
    for (o, n), c in sorted(summary.items()):
        print(f"  {o:<10} → {n:<3}  : {c} entrées")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0

    if not changes:
        print("Rien à faire.")
        return 0

    # Backup
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-migrate-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")

    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
