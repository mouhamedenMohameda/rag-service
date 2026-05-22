#!/usr/bin/env python3
"""Ré-extraction Groq ciblée pour une liste d'exos précise.

Sert à corriger les exos contaminés par un libellé halluciné par le LLM
(few-shot leakage). Réutilise le SYSTEM prompt corrigé de
``generate_atomic_notions.py`` et ajoute (sans écraser) les nouvelles notions
aux notions_traitees déjà présentes pour ces exos.

Pipeline :
    1. Lit scripts/_reextract_targets.json (liste d'ids)
    2. Pour chaque exo, appelle Groq → 4-8 nouvelles notions
    3. Écrit scripts/notions_reextract.json {id: [labels]}
    4. Tu peux ensuite canoniser :
         python scripts/canonize_notions.py \
             --input scripts/notions_reextract.json \
             --merge-registry --by-input-ids

Usage :
    export GROQ_API_KEY=...
    python scripts/reextract_targeted.py --dry-run
    python scripts/reextract_targeted.py
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

# Réutilise le prompt corrigé + l'appel Groq du script principal
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_atomic_notions import SYSTEM, call_groq  # noqa: E402

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
TARGETS = ROOT / "scripts" / "_reextract_targets.json"
OUTPUT = ROOT / "scripts" / "notions_reextract.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.4)
    ap.add_argument("--model", default="llama-3.3-70b-versatile")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    if not TARGETS.exists():
        print(f"ERREUR : {TARGETS} introuvable.", file=sys.stderr)
        return 2

    target_ids = json.loads(TARGETS.read_text(encoding="utf-8"))
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in data}

    targets = [by_id[i] for i in target_ids if i in by_id]
    if args.limit:
        targets = targets[: args.limit]

    existing: dict[str, list[str]] = {}
    if args.resume and OUTPUT.exists():
        existing = json.loads(OUTPUT.read_text(encoding="utf-8"))

    todo = [e for e in targets if e["id"] not in existing]
    print(f"→ {len(todo)} exo(s) à ré-extraire ({len(existing)} déjà faits)")

    if args.dry_run:
        for e in todo[:10]:
            print(f"   {e['id']} ({e.get('matiere_id')}) — "
                  f"{(e.get('ennonce_complet') or '')[:60]}…")
        return 0

    if not os.environ.get("GROQ_API_KEY"):
        print("ERREUR : GROQ_API_KEY manquante.", file=sys.stderr)
        return 2

    # Sanity check : si le SYSTEM contient encore l'exemple fuité, on refuse
    if "ln|x/(x-1)|" in SYSTEM:
        print("ERREUR : le prompt SYSTEM contient encore l'exemple « ln|x/(x-1)| ». "
              "Le few-shot leakage va se reproduire. Corrige generate_atomic_notions.py.",
              file=sys.stderr)
        return 3

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
            failures.append(f"{eid}: vide")
            print("❌ vide")
            continue
        # Détection précoce : si le libellé fuité réapparaît, on alerte
        if any("ln|x/(x-1)|" in n for n in notions):
            print(f"⚠️  RÉ-APPARITION du libellé fuité — vérifier le prompt")
        result[eid] = notions
        print(f"✓ {len(notions)} notions")
        if k % 10 == 0:
            OUTPUT.write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        if args.sleep > 0:
            time.sleep(args.sleep)

    OUTPUT.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"\nÉcrit {OUTPUT} ({len(result)} exos)")
    if failures:
        print(f"Échecs : {len(failures)}")

    # Vérif globale post-extraction
    from collections import Counter
    cnt = Counter()
    for labels in result.values():
        for l in labels:
            cnt[l] += 1
    repeated = [(l, n) for l, n in cnt.most_common(10) if n >= 5]
    if repeated:
        print("\n⚠️  Libellés répétés ≥5 fois (à surveiller) :")
        for l, n in repeated:
            print(f"  {n:3d}× {l}")
    else:
        print("\n✓ Aucun libellé répété ≥5 fois — pas de leakage évident.")

    print(f"\nProchain pas :")
    print(f"  python scripts/canonize_notions.py \\")
    print(f"      --input {OUTPUT.relative_to(ROOT)} \\")
    print(f"      --merge-registry --by-input-ids")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
