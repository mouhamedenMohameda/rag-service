"""Génère les squelettes vides pour TOUT le Bac mauritanien (2000-2024).

Combinatoire :
  6 combos (filière × matière) :
    - C × math, C × pc, C × svt
    - D × math, D × pc, D × svt
  × 25 années (2000..2024)
  × 2 sessions (Normale, Complémentaire)
  × 5 exercices par session
  = 1500 squelettes au total.

Merge intelligent : si une entrée existe déjà avec la même clé composite
(filiere_id, matiere_id, annee, session, exercice_numero), on la GARDE
intacte et on ne génère pas de squelette pour cette case. Les entrées
"extra" (ex: exo 6) sont préservées telles quelles.

Squelette généré (tous champs éditables vides) :
    {
      "id":              "bac-c-2011-sn-pc-ex3",
      "titre":           "BAC C 2011 Session normale exo 3 (Sciences Physiques)",
      "matiere_id":      "pc",  | "math" | "svt"
      "filiere_id":      "C" | "D",
      "annee":           2011,
      "session":         "Normale" | "Complémentaire",
      "exercice_numero": 3,
      "fichier":         "",
      "chapitre":        "",
      "notions_traitees":[],
      "ennonce_complet": "",
      "correction":      "",
      "donnees_fournies":{},
      "validated_by_admin": false,
      "is_skeleton":     true
    }

Backup auto + dry-run.

Usage :
    python scripts/seed_skeletons.py --dry-run
    python scripts/seed_skeletons.py
    python scripts/seed_skeletons.py --from-year 2010 --to-year 2024
    python scripts/seed_skeletons.py --only filiere=C,matiere=math
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"

# ── Paramètres métier ────────────────────────────────────────────────────────
FILIERES = ["C", "D"]
MATIERES = [
    ("math", "Mathématiques"),
    ("pc", "Sciences Physiques"),
    ("svt", "Sciences Naturelles"),
]
SESSIONS = [
    ("Normale", "sn"),
    ("Complémentaire", "sc"),
]
DEFAULT_EXOS_PER_SESSION = 5


def make_id(filiere: str, annee: int, sess_code: str, mat_id: str, ex_num: int) -> str:
    return f"bac-{filiere.lower()}-{annee}-{sess_code}-{mat_id}-ex{ex_num}"


def make_titre(filiere: str, annee: int, session: str, ex_num: int, mat_label: str) -> str:
    return f"BAC {filiere} {annee} Session {session.lower()} exo {ex_num} ({mat_label})"


def composite_key(e: dict[str, Any]) -> tuple:
    """Clé d'unicité d'un exo. Si deux entrées partagent cette clé on
    considère que c'est le même exo (et on ne génère pas de squelette en
    plus)."""
    return (
        (e.get("filiere_id") or "").upper(),
        e.get("matiere_id") or "",
        int(e.get("annee") or 0),
        (e.get("session") or "").strip().lower(),
        # On accepte exercice_numero stocké soit en int soit en string
        str(e.get("exercice_numero") or "").strip(),
    )


def build_skeleton(filiere: str, annee: int, session: str, sess_code: str,
                   mat_id: str, mat_label: str, ex_num: int) -> dict[str, Any]:
    return {
        "id": make_id(filiere, annee, sess_code, mat_id, ex_num),
        "titre": make_titre(filiere, annee, session, ex_num, mat_label),
        "matiere_id": mat_id,
        "filiere_id": filiere,
        "annee": annee,
        "session": session,
        "exercice_numero": ex_num,
        "fichier": "",
        "chapitre": "",
        "notions_traitees": [],
        "ennonce_complet": "",
        "correction": "",
        "donnees_fournies": {},
        "validated_by_admin": False,
        "is_skeleton": True,
        "matiere": mat_label,
        "filiere": f"Série {filiere}",
    }


def parse_only(s: str | None) -> dict[str, str]:
    if not s:
        return {}
    out: dict[str, str] = {}
    for token in s.split(","):
        token = token.strip()
        if not token:
            continue
        if "=" not in token:
            continue
        k, v = token.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-year", type=int, default=2000)
    ap.add_argument("--to-year", type=int, default=2024)
    ap.add_argument("--exos", type=int, default=DEFAULT_EXOS_PER_SESSION)
    ap.add_argument("--only", default=None,
                    help="Filtre. Ex: 'filiere=C,matiere=math' ou 'filiere=D'")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    only = parse_only(args.only)

    p = Path(args.json)
    data: list[dict] = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []

    existing_keys = {composite_key(e) for e in data}

    to_add: list[dict] = []
    for filiere in FILIERES:
        if only.get("filiere") and only["filiere"].upper() != filiere:
            continue
        for mat_id, mat_label in MATIERES:
            if only.get("matiere") and only["matiere"] != mat_id:
                continue
            for annee in range(args.from_year, args.to_year + 1):
                for session, sess_code in SESSIONS:
                    for ex_num in range(1, args.exos + 1):
                        key = (
                            filiere,
                            mat_id,
                            annee,
                            session.strip().lower(),
                            str(ex_num),
                        )
                        if key in existing_keys:
                            continue
                        to_add.append(build_skeleton(
                            filiere, annee, session, sess_code, mat_id, mat_label, ex_num,
                        ))
                        existing_keys.add(key)

    # ── Stats ───────────────────────────────────────────────────────────────
    print(f"\n{len(data)} entrée(s) déjà présentes — {len(to_add)} squelettes à ajouter.")
    cnt = Counter((s["filiere_id"], s["matiere_id"]) for s in to_add)
    print("\nRépartition des squelettes à ajouter :")
    for (f, m), c in sorted(cnt.items()):
        print(f"  {f}/{m:<6} : {c}")

    if not to_add:
        print("Rien à ajouter — tout est déjà couvert.")
        return 0
    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-seed-{stamp}.json"
    if p.exists():
        shutil.copy2(p, backup)
        print(f"\nBackup : {backup}")

    merged = data + to_add
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour. Total entrées : {len(merged)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
