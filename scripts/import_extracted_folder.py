"""Import les exos depuis le format custom `=== ... ===` (folder exo_extracted/).

Format attendu :
    === Matière | Série X | YYYY | Session Normale|Complémentaire | Exercice N ===
    <contenu de l'exo>
    === ... ===
    ...

Mapping nom de fichier → (filiere, matiere) :
    math-bacC.txt        → C / math
    math-bacD.txt        → D / math
    science-bacc.txt     → C / svt
    science-bacD.txt     → D / svt

Cas spéciaux :
  Si le contenu d'un bloc contient ≥2 occurrences de "Baccalauréat YYYY session ..."
  (bloc malformé contenant plusieurs exos d'années différentes), on normalise
  ces headers embedded et on les utilise au lieu du header `===` du bloc.

Le script convertit chaque fichier en format "Baccalauréat YYYY - Session XXX"
puis appelle la même logique que import_exos_from_text.py.

Usage :
    .venv/bin/python scripts/import_extracted_folder.py --dir exo_extracted --dry-run
    .venv/bin/python scripts/import_extracted_folder.py --dir exo_extracted
    .venv/bin/python scripts/import_extracted_folder.py --dir exo_extracted --force
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"

# Import de la logique de parsing depuis le script existant
sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_exos_from_text import parse_text, find_entry, validate_ennonce  # noqa: E402


FILE_TO_FIL_MAT = {
    "math-bacC.txt": ("C", "math"),
    "math-bacD.txt": ("D", "math"),
    "science-bacC.txt": ("C", "svt"),
    "science-bacc.txt": ("C", "svt"),
    "science-bacD.txt": ("D", "svt"),
}

_RE_BLOCK_HEADER = re.compile(
    r"^=== \s*"
    r"(?P<matiere>.+?)\s*\|\s*"
    r"Série\s+(?P<serie>[CD])\s*\|\s*"
    r"(?P<annee>\d{4})\s*\|\s*"
    r"Session\s+(?P<session>Normale|Complémentaire|complementaire)\s*\|\s*"
    r"Exercice\s*(?P<ex_num>\d+)\s*===\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def convert_extracted_file(path: Path) -> str:
    """Convertit le format `=== ... ===` en "Baccalauréat YYYY - Session XXX"."""
    text = path.read_text(encoding="utf-8")
    matches = list(_RE_BLOCK_HEADER.finditer(text))
    if not matches:
        return ""

    out_parts: list[str] = []
    for i, m in enumerate(matches):
        annee = m.group("annee")
        session = m.group("session").capitalize()
        ex_num = m.group("ex_num")
        content_start = m.end()
        content_end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        content = text[content_start:content_end].strip()

        # Cas malformé : si le contenu a plusieurs "Baccalauréat YYYY session ..."
        # embedded (header de session collé au texte), on les normalise en
        # "Baccalauréat YYYY - Session XXX" et on ignore le header === du bloc.
        # Le parser principal détectera ensuite chaque session avec ses exos.
        normalized = re.sub(
            r"Baccalauréat\s+(\d{4})\s+session\s+(Normale|Complémentaire)",
            r"\n\nBaccalauréat \1 - Session \2\n",
            content,
            flags=re.IGNORECASE,
        )
        embedded_count = len(re.findall(r"Baccalauréat \d{4} - Session", normalized))
        if embedded_count >= 2:
            # Bloc malformé : on garde les headers embedded
            out_parts.append("\n\n" + normalized)
        else:
            # Bloc propre : on génère le header à partir du ===
            out_parts.append(f"\n\nBaccalauréat {annee} - Session {session}\nExercice {ex_num}\n{content}")

    return "".join(out_parts)


def apply_to_json(parsed, filiere, matiere, data, now, force=False):
    updated = []
    skipped_filled = []
    skipped_missing = []
    warnings_global = []
    for annee, sess, ex_num, ennonce in parsed:
        label = f"{filiere}/{matiere}/{annee}/{sess}/ex{ex_num}"
        warns = validate_ennonce(ennonce)
        if warns:
            warnings_global.append((label, warns))
        e = find_entry(data, filiere, matiere, annee, sess, ex_num)
        if e is None:
            skipped_missing.append(label)
            continue
        eid = e.get("id", "?")
        old = (e.get("ennonce_complet") or "").strip()
        if old and len(old) > 100 and not force:
            skipped_filled.append((label, eid, len(old)))
            continue
        e["ennonce_complet"] = ennonce.strip()
        e["is_skeleton"] = False
        e["updated_at"] = now
        updated.append((label, eid, len(old), len(ennonce.strip())))
    return updated, skipped_missing, skipped_filled, warnings_global


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="exo_extracted", help="Dossier contenant les .txt")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    folder = Path(args.dir)
    if not folder.is_dir():
        print(f"❌ Dossier introuvable : {folder}", file=sys.stderr)
        return 2

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))
    now = datetime.now().isoformat(timespec="seconds")

    total_updated = 0
    total_skipped_missing = 0
    total_skipped_filled = 0
    total_warnings = 0
    per_file_reports = []

    for filename, (filiere, matiere) in FILE_TO_FIL_MAT.items():
        path = folder / filename
        if not path.exists():
            print(f"⚠️  {filename} : fichier absent — skip")
            continue
        converted = convert_extracted_file(path)
        if not converted.strip():
            print(f"⚠️  {filename} : aucun bloc détecté")
            continue
        parsed = parse_text(converted)
        if not parsed:
            print(f"⚠️  {filename} : 0 énoncé extrait")
            continue

        updated, skipped_missing, skipped_filled, warns = apply_to_json(
            parsed, filiere, matiere, data, now, force=args.force,
        )
        per_file_reports.append({
            "filename": filename,
            "filiere": filiere,
            "matiere": matiere,
            "parsed": len(parsed),
            "updated": updated,
            "skipped_missing": skipped_missing,
            "skipped_filled": skipped_filled,
            "warnings": warns,
        })
        total_updated += len(updated)
        total_skipped_missing += len(skipped_missing)
        total_skipped_filled += len(skipped_filled)
        total_warnings += len(warns)

    # ─── Rapport ─────────────────────────────────────────────────────────────
    print("═" * 72)
    print(f"RAPPORT GLOBAL")
    print("═" * 72)
    for r in per_file_reports:
        print(f"\n📄 {r['filename']} ({r['filiere']}/{r['matiere']})")
        print(f"  Parsés       : {r['parsed']}")
        print(f"  Mis à jour   : {len(r['updated'])}")
        print(f"  Introuvables : {len(r['skipped_missing'])}")
        print(f"  Déjà remplis : {len(r['skipped_filled'])} (--force pour écraser)")
        print(f"  Warnings     : {len(r['warnings'])}")
        if r["skipped_missing"]:
            print(f"  Exemples introuvables :")
            for lbl in r["skipped_missing"][:5]:
                print(f"    - {lbl}")
            if len(r["skipped_missing"]) > 5:
                print(f"    ... + {len(r['skipped_missing']) - 5} autres")

    print()
    print("═" * 72)
    print(f"TOTAL : {total_updated} mis à jour | {total_skipped_missing} introuvables | "
          f"{total_skipped_filled} déjà remplis | {total_warnings} warnings")
    print("═" * 72)

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not total_updated:
        print("\nRien à écrire.")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-import-extracted-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour ({total_updated} entrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
