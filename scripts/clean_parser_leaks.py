"""Nettoie les résidus du parser dans ennonce_complet.

Deux types de pollution détectés :
  1. Marker '===' suivi du header d'un AUTRE exercice (parser a leaké du contexte).
     → Tronquer à partir du '===' (et nettoyer les espaces de fin).
  2. Header de métadonnée en TÊTE d'énoncé :
        Fichier source: ...
        Chapitre: ...
        Notions: ...
        <ligne vide>
        <vrai énoncé>
     → Strip le header, garder le vrai énoncé. Si Chapitre/Notions vides côté JSON,
       les remplir depuis ce header avant de strip.

Backup automatique avant écriture.

Usage :
    .venv/bin/python scripts/clean_parser_leaks.py --dry-run
    .venv/bin/python scripts/clean_parser_leaks.py
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"


def slot_id(e):
    return f"{e['filiere_id']}/{e['matiere_id']}/{e.get('annee')}/{str(e.get('session',''))[:2].lower()}/ex{e.get('exercice_numero')}"


_HEADER_RE = re.compile(
    r"^(?:Fichier source:\s*(?P<source>.+?)\n)?"
    r"(?:Chapitre:\s*(?P<chap>.+?)\n)?"
    r"(?:Notions:\s*(?P<notions>.+?)\n)?"
    r"\s*\n",
    re.IGNORECASE,
)


def clean_entry(e: dict) -> tuple[bool, list[str]]:
    """Modifie e in-place. Retourne (modified, log_messages)."""
    changes = []
    text = e.get("ennonce_complet", "")
    if not text:
        return False, changes

    modified = False

    # --- 1. Truncate à partir de '===' ---
    if "===" in text:
        idx = text.find("===")
        truncated = text[idx:]
        text = text[:idx].rstrip()
        changes.append(f"truncate-=== ({len(truncated)} chars supprimés)")
        modified = True

    # --- 2. Strip header métadonnée en tête ---
    m = _HEADER_RE.match(text)
    if m and (m.group("chap") or m.group("notions") or m.group("source")):
        # Remplit chapitre/notions si vides côté JSON
        chap = (m.group("chap") or "").strip()
        notions_str = (m.group("notions") or "").strip()
        if chap and not (e.get("chapitre") or "").strip():
            e["chapitre"] = chap
            changes.append(f"chapitre={chap!r}")
        if notions_str:
            notions_list = [n.strip() for n in re.split(r"[,;]", notions_str) if n.strip()]
            if notions_list and not e.get("notions_traitees"):
                e["notions_traitees"] = notions_list
                changes.append(f"notions={notions_list}")
        # Strip le header
        text = text[m.end():]
        changes.append("strip-header")
        modified = True

    # --- 3. Cleanup espaces ---
    text = text.strip()
    if modified:
        e["ennonce_complet"] = text

    return modified, changes


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    data = json.load(open(JSON_PATH))
    print(f"Total entrées : {len(data)}")

    modified_entries = []
    for e in data:
        modified, changes = clean_entry(e)
        if modified:
            modified_entries.append((e, changes))

    print(f"\nEntrées modifiées : {len(modified_entries)}")
    for e, changes in modified_entries:
        print(f"  {slot_id(e):30s}  {' | '.join(changes)}")

    if not modified_entries:
        print("Rien à nettoyer.")
        return

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return

    # Backup
    BACKUP_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-clean-parser-{ts}.json"
    shutil.copy(JSON_PATH, backup)
    print(f"\nBackup : {backup}")

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"→ {JSON_PATH} mis à jour.")


if __name__ == "__main__":
    main()
