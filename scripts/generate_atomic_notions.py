#!/usr/bin/env python3
"""Génère des notions atomiques pour les exos avec énoncé mais sans notions.

Usage (Groq requis) :
    export GROQ_API_KEY=...
    python scripts/generate_atomic_notions.py --dry-run
    python scripts/generate_atomic_notions.py
    python scripts/generate_atomic_notions.py --resume

Puis canoniser :
    python scripts/canonize_notions.py --input scripts/notions_remaining.json \\
        --merge-registry --by-input-ids
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
OUTPUT = ROOT / "scripts" / "notions_remaining.json"
BACKUP_DIR = ROOT / "json_backups"

SYSTEM = """Tu extrais des notions atomiques pour des exercices Bac mauritanien.

Règles :
- 4 à 8 notions par exercice, en français
- Format : [Objet] + [opération/propriété] + [contrainte/contexte]
- Réutilisables entre exercices (pas de détails propres à l'énoncé sauf si compétence générale)
- Exemples : « Vitesse instantanée de formation du diiode — lecture graphique »,
  « Limite en +∞ d'une fonction avec ln|x/(x-1)| »,
  « Analyse d'un pédigrée — mode récessif vs dominant »

Réponds UNIQUEMENT en JSON :
{"notions": ["...", "..."]}"""


def needs_notions(e: dict) -> bool:
    if not (e.get("ennonce_complet") or "").strip():
        return False
    if e.get("notion_ids") or e.get("notions_traitees"):
        return False
    return True


def call_groq(ennonce: str, matiere_id: str, model: str) -> list[str] | None:
    from groq import Groq

    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    user = f"Matière : {matiere_id}\n\nÉNONCÉ :\n\"\"\"\n{ennonce[:3500]}\n\"\"\""
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.1,
        response_format={"type": "json_object"},
        max_tokens=500,
    )
    content = resp.choices[0].message.content or ""
    try:
        obj = json.loads(content)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", content, re.DOTALL)
        if not m:
            return None
        obj = json.loads(m.group(0))
    notions = obj.get("notions")
    if not isinstance(notions, list):
        return None
    out = [str(n).strip() for n in notions if str(n).strip()]
    return out[:8] if out else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--resume", action="store_true", help="Reprend les ids déjà dans OUTPUT")
    ap.add_argument("--sleep", type=float, default=0.4)
    ap.add_argument("--model", default="llama-3.3-70b-versatile")
    ap.add_argument("--output", default=str(OUTPUT))
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    targets = [e for e in data if needs_notions(e)]
    if args.limit:
        targets = targets[: args.limit]

    out_path = Path(args.output)
    existing: dict[str, list[str]] = {}
    if args.resume and out_path.exists():
        existing = json.loads(out_path.read_text(encoding="utf-8"))

    todo = [e for e in targets if e["id"] not in existing]
    print(f"→ {len(todo)} exo(s) à traiter ({len(existing)} déjà dans {out_path.name})")

    if args.dry_run:
        for e in todo[:15]:
            print(f"   {e['id']} ({e.get('matiere_id')})")
        if len(todo) > 15:
            print(f"   … +{len(todo)-15}")
        return 0

    if not os.environ.get("GROQ_API_KEY"):
        print("ERREUR : GROQ_API_KEY manquante.", file=sys.stderr)
        return 2

    result = dict(existing)
    failures: list[str] = []
    for k, e in enumerate(todo, 1):
        eid = e["id"]
        print(f"[{k}/{len(todo)}] {eid:<45} ", end="", flush=True)
        try:
            notions = call_groq(e["ennonce_complet"], e.get("matiere_id", "?"), args.model)
        except Exception as ex:
            failures.append(f"{eid}: {ex}")
            print(f"❌ {ex}")
            continue
        if not notions:
            failures.append(f"{eid}: réponse vide")
            print("❌ vide")
            continue
        result[eid] = notions
        print(f"✓ {len(notions)} notions")
        if k % 20 == 0:
            out_path.write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        if args.sleep > 0:
            time.sleep(args.sleep)

    out_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\nÉcrit {out_path} ({len(result)} exos)")
    if failures:
        print(f"Échecs : {len(failures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
