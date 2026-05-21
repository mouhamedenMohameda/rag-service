"""Import depuis les fichiers backup convertis, en routant chaque exo selon
la matière indiquée dans son MARKER (et non selon le nom du fichier).

Le backup peut contenir un mix de matières (Sciences Physiques + Sciences
Naturelles + Mathématiques) dans le même fichier — c'est ce qui se passe
dans `science-bacc.txt` du backup qui contient à la fois des PC et des SVT.

Format de marker attendu (après conversion dash → pipe) :
    === Sciences Physiques | Série C | 2002 | Session Normale | Exercice 1 ===

Mapping matière du marker → matiere_id du JSON :
    Sciences Physiques  → pc
    Sciences Naturelles → svt
    Mathématiques       → math

Usage :
    .venv/bin/python scripts/import_by_marker.py --input /tmp/converted_bacc.txt --dry-run
    .venv/bin/python scripts/import_by_marker.py --input /tmp/converted_bacc.txt --force
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from import_exos_from_text import find_entry, validate_ennonce  # noqa: E402


MATIERE_MAP = {
    "sciences physiques": "pc",
    "sciences naturelles": "svt",
    "mathématiques": "math",
}

_RE_BLOCK_HEADER = re.compile(
    r"^=== \s*"
    r"(?P<matiere>.+?)\s*\|\s*"
    r"Série\s+(?P<serie>[CD])\s*\|\s*"
    r"(?P<annee>\d{4})\s*\|\s*"
    r"Session\s+(?P<session>Normale|Complémentaire|Complementaire)\s*\|\s*"
    r"Exercice\s*(?P<ex_num>\S+?)\s*===\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def normalize_exo_num(exo: str) -> int | None:
    """Convertit 'BAC-2015-SC-D-EXO5' ou '5' → 5. None si impossible."""
    if exo.isdigit():
        return int(exo)
    m = re.search(r"EXO(\d+)", exo, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def clean_body(body: str) -> str:
    """Strip les headers parasites du début du bloc."""
    # Strip lines "Fichier source: ...", "Chapitre: ...", "Notions: ..."
    lines = body.split("\n")
    out_lines = []
    skipped_header = False
    in_skip_zone = True
    for line in lines:
        s = line.strip()
        if in_skip_zone and re.match(r"^(Fichier source|Chapitre|Notions)\s*:", s, re.IGNORECASE):
            skipped_header = True
            continue
        if in_skip_zone and skipped_header and not s:
            # ligne vide après le header → on a fini la zone de skip
            in_skip_zone = False
            continue
        in_skip_zone = False
        out_lines.append(line)
    return "\n".join(out_lines).strip()


def parse_file(text: str):
    """Yield (matiere, filiere, annee, session, ex_num, body)."""
    matches = list(_RE_BLOCK_HEADER.finditer(text))
    for i, m in enumerate(matches):
        mat_name = m.group("matiere").strip().lower()
        if mat_name not in MATIERE_MAP:
            yield {"error": f"matière inconnue: {mat_name}", "raw": m.group(0)}
            continue
        matiere = MATIERE_MAP[mat_name]
        filiere = m.group("serie").upper()
        annee = int(m.group("annee"))
        session = m.group("session").capitalize().replace("Complementaire", "Complémentaire")
        ex_num = normalize_exo_num(m.group("ex_num"))
        if ex_num is None:
            yield {"error": f"ex_num non parsable: {m.group('ex_num')}", "raw": m.group(0)}
            continue
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = clean_body(text[start:end])
        yield {
            "matiere": matiere,
            "filiere": filiere,
            "annee": annee,
            "session": session,
            "ex_num": ex_num,
            "body": body,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="Fichier converti (pipe format)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="Écrase les énoncés déjà remplis")
    ap.add_argument("--min-body-size", type=int, default=80,
                    help="Taille minimum du body pour considérer l'exo valide")
    args = ap.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    now = datetime.now().isoformat(timespec="seconds")

    stats = Counter()
    updated = []
    skipped_filled = []
    skipped_missing = []
    skipped_short = []
    errors = []

    for r in parse_file(text):
        if "error" in r:
            errors.append(r)
            stats["errors"] += 1
            continue

        label = f"{r['filiere']}/{r['matiere']}/{r['annee']}/{r['session'][:2].lower()}/ex{r['ex_num']}"
        body = r["body"]

        if len(body) < args.min_body_size:
            skipped_short.append((label, len(body)))
            stats["short"] += 1
            continue

        sess_code = "sn" if r["session"].lower().startswith("n") else "sc"
        e = find_entry(data, r["filiere"], r["matiere"], r["annee"], sess_code, r["ex_num"])
        if e is None:
            skipped_missing.append(label)
            stats["missing"] += 1
            continue

        old = (e.get("ennonce_complet") or "").strip()
        if old and len(old) > 100 and not args.force:
            skipped_filled.append((label, len(old), len(body)))
            stats["already_filled"] += 1
            continue

        if not args.dry_run:
            e["ennonce_complet"] = body.strip()
            e["is_skeleton"] = False
            e["updated_at"] = now
        updated.append((label, len(old), len(body)))
        stats["updated"] += 1

    print(f"Markers parsés : {sum(stats.values())}")
    print(f"  ✅ Mis à jour     : {stats['updated']}")
    print(f"  ⏭️  Déjà remplis  : {stats['already_filled']} (--force pour écraser)")
    print(f"  ❌ Slot inexistant: {stats['missing']}")
    print(f"  ⚠️  Body trop court: {stats['short']}")
    print(f"  ⚠️  Erreurs       : {stats['errors']}")

    if stats["missing"] and len(skipped_missing) <= 30:
        print("\nSlots inexistants (à seed potentiellement) :")
        for s in skipped_missing:
            print(f"  - {s}")

    if errors and len(errors) <= 5:
        print("\nErreurs de parsing :")
        for e in errors:
            print(f"  - {e['error']} | {e['raw'][:80]}")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return

    if stats["updated"] == 0:
        return

    BACKUP_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-import-marker-{ts}.json"
    shutil.copy(JSON_PATH, backup)
    print(f"\nBackup : {backup}")

    JSON_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"→ {JSON_PATH} mis à jour ({stats['updated']} entrées).")


if __name__ == "__main__":
    main()
