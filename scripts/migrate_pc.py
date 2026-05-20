"""Migration : collapse matiere_id physique/chimie → pc.

Logique métier : l'épreuve "Sciences Physiques" du Bac mauritanien donne
des exercices à la fois de physique et de chimie dans le MÊME papier
(même PDF). Côté admin/JSON on les regroupe en une seule matière `pc`.

Conséquences :
- Tous les exos ayant matiere_id ∈ {physique, chimie} deviennent `pc`.
- Le champ verbose `matiere` est normalisé en "Sciences Physiques".
- L'id technique est conservé pour ne pas casser les références
  existantes (ex: `chimie-2020-sn-ex1` reste tel quel, on ne renomme pas).

Backup auto + dry-run.

Usage :
    python scripts/migrate_pc.py --dry-run
    python scripts/migrate_pc.py
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))

    changed: list[tuple[str, str]] = []
    for e in data:
        m = e.get("matiere_id")
        if m in ("physique", "chimie"):
            changed.append((e.get("id", "?"), m))
            e["matiere_id"] = "pc"
            e["matiere"] = "Sciences Physiques"
            e["updated_at"] = datetime.now().isoformat(timespec="seconds")

    print(f"\n{len(changed)} entrée(s) à migrer vers matiere_id='pc' (sur {len(data)}) :")
    from collections import Counter
    src = Counter(o for _, o in changed)
    for s, c in sorted(src.items()):
        print(f"  {s:<10} → pc  : {c} entrées")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not changed:
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-pc-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")

    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
