"""Correcteur de syntaxe « léger » pour les énoncés collés à la main.

PRINCIPE : ne JAMAIS reformuler. On corrige uniquement les artefacts de
copier-coller :
  - chiffres collés au mauvais endroit (« 5g/mol » au lieu de « 5 g/mol »)
  - lettres parasites (« I-l » au lieu de « I- »)
  - unités qui sautent (« H_2O_2 » écrit « H2O_2 » par moitié)
  - accents perdus, doubles espaces, ponctuation mal placée
  - LaTeX cassé sans reformuler (`$frac` → `\\frac`)

Le LLM reçoit un prompt très strict : "tu modifies UNIQUEMENT les
caractères clairement parasites, tu PRÉSERVES la structure, la
numérotation, les phrases, l'ordre des questions, les valeurs numériques
attendues d'après le contexte."

Garde-fou côté Python : si la version corrigée diffère de plus de N% de
caractères, on rejette (probable réécriture par le LLM). Configurable
via --max-diff-pct.

Auto-save désactivé pour ce script : tu choisis pour chaque exo
d'accepter ou rejeter la suggestion (mode interactif), ou en bulk avec
--apply-all (à tes risques, mais backup auto fait avant chaque écriture).

Usage :
    # Mode interactif (recommandé pour débuter)
    python scripts/fix_syntax_ennonce.py --from-year 2002 --to-year 2005

    # Bulk auto (uniquement si tu as confiance)
    python scripts/fix_syntax_ennonce.py --apply-all --max-diff-pct 5
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"


SYSTEM_PROMPT = """Tu es un correcteur de syntaxe pour des énoncés de Bac \
mauritanien (Sciences Physiques) qui ont été extraits puis collés à la main, \
ce qui a introduit des artefacts (chiffres collés à un mauvais endroit, \
caractères parasites, espaces manquants, accents perdus, LaTeX cassé, \
indices oubliés type "S2O8 2-" au lieu de "S₂O₈²⁻" ou "S_2O_8^{2-}").

RÈGLES ABSOLUES :
1. Tu NE REFORMULES JAMAIS. Tu gardes EXACTEMENT les mêmes phrases, le même \
   ordre, la même numérotation des questions (1.1, 2.3, etc.).
2. Tu NE CHANGES PAS les valeurs numériques de l'énoncé. Si tu vois "0,55V" \
   ou "0.55 V", tu décides un seul format en restant fidèle aux chiffres.
3. Tu NE COMPLÈTES PAS l'exercice avec des informations absentes. Si le \
   collage a perdu une formule ou une donnée, tu laisses tel quel (avec un \
   marqueur "[…?]" si vraiment illisible).
4. Tu corriges UNIQUEMENT :
   - espaces manquants entre nombre et unité (« 20mL » → « 20 mL »)
   - caractères parasites flagrants (« I-l » seul → « I- »)
   - LaTeX visiblement cassé sans le réinventer (« $frac{a}{b}$ » → « $\\\\frac{a}{b}$ »)
   - indices/exposants chimiques avec _N et ^N corrects (« S2O82- » → « S_2O_8^{2-} ») \
     mais SEULEMENT si tu es 100% sûr du sens
   - accents perdus (« deduire » → « déduire »)
   - ponctuation mal placée (« .Calculer » → « . Calculer »)

5. Si tu n'es PAS SÛR d'une correction, tu LAISSES tel quel.

Réponds en JSON strict :
{
  "corrected": "<texte corrigé>",
  "changes_summary": "<1-2 phrases décrivant les types de corrections appliquées>"
}"""


def call_groq(ennonce: str, model: str = "llama-3.3-70b-versatile") -> dict | None:
    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"ÉNONCÉ À CORRIGER :\n\n\"\"\"\n{ennonce}\n\"\"\""},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
        max_tokens=3000,
    )
    try:
        return json.loads(resp.choices[0].message.content or "{}")
    except json.JSONDecodeError:
        return None


def diff_pct(a: str, b: str) -> float:
    """% de caractères différents entre a et b (0 = identique)."""
    if not a:
        return 100.0 if b else 0.0
    sm = difflib.SequenceMatcher(None, a, b)
    return (1 - sm.ratio()) * 100


def show_diff(a: str, b: str, label_a: str = "AVANT", label_b: str = "APRÈS") -> None:
    """Affiche un diff lisible des deux versions."""
    print(f"\n--- {label_a} ".ljust(78, "-"))
    print(a[:1000] + ("…" if len(a) > 1000 else ""))
    print(f"\n+++ {label_b} ".ljust(78, "+"))
    print(b[:1000] + ("…" if len(b) > 1000 else ""))
    print(f"\nDiff: {diff_pct(a, b):.1f}% de caractères changés.")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-year", type=int, default=2002)
    ap.add_argument("--to-year", type=int, default=2024)
    ap.add_argument("--filiere", default=None)
    ap.add_argument("--apply-all", action="store_true",
                    help="Applique TOUS les diff <= max-diff-pct sans demander")
    ap.add_argument("--max-diff-pct", type=float, default=15.0,
                    help="Rejet automatique si plus de N%% de caractères changés")
    ap.add_argument("--sleep", type=float, default=0.5)
    ap.add_argument("--model", default="llama-3.3-70b-versatile")
    ap.add_argument("--json", default=str(JSON_PATH))
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    if not os.environ.get("GROQ_API_KEY"):
        print("ERREUR : GROQ_API_KEY manquante.", file=sys.stderr)
        return 2

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))

    targets = []
    for i, e in enumerate(data):
        if e.get("matiere_id") not in ("pc", "physique", "chimie"):
            continue
        if args.filiere and e.get("filiere_id") != args.filiere:
            continue
        a = e.get("annee")
        if not isinstance(a, int) or not (args.from_year <= a <= args.to_year):
            continue
        if not (e.get("ennonce_complet") or "").strip():
            continue
        targets.append(i)
    if args.limit:
        targets = targets[: args.limit]

    print(f"\n→ {len(targets)} énoncé(s) à examiner.\n")

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(p, BACKUP_DIR / f"json_bac-pre-syntax-{stamp}.json")

    accepted = 0
    skipped = 0
    rejected_too_big = 0
    for k, i in enumerate(targets, 1):
        e = data[i]
        eid = e.get("id", "?")
        old = e["ennonce_complet"]
        print(f"\n[{k}/{len(targets)}] {eid}")
        try:
            res = call_groq(old, model=args.model)
        except Exception as ex:
            print(f"   ❌ erreur Groq : {ex}")
            continue
        if not res or "corrected" not in res:
            print("   ❌ réponse invalide")
            continue
        new = res["corrected"]
        d = diff_pct(old, new)
        if d == 0:
            print("   ✓ rien à corriger")
            skipped += 1
            continue
        if d > args.max_diff_pct:
            print(f"   ⚠️ rejet auto : diff {d:.1f}% > seuil {args.max_diff_pct}%")
            rejected_too_big += 1
            continue
        if args.apply_all:
            e["ennonce_complet"] = new
            e["updated_at"] = datetime.now().isoformat(timespec="seconds")
            accepted += 1
            print(f"   ✓ appliqué ({d:.1f}% changé) : {res.get('changes_summary', '')[:80]}")
        else:
            show_diff(old, new)
            print(f"\nRésumé : {res.get('changes_summary', '')}")
            choice = input("[A]ccepter / [R]efuser / [Q]uitter ? ").strip().lower()
            if choice == "q":
                break
            if choice == "a":
                e["ennonce_complet"] = new
                e["updated_at"] = datetime.now().isoformat(timespec="seconds")
                accepted += 1
                print("   ✓ accepté")
            else:
                print("   ↷ refusé")
        # Sauvegarde tous les 5 changements
        if accepted and accepted % 5 == 0:
            tmp = p.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            tmp.replace(p)
        if args.sleep > 0:
            time.sleep(args.sleep)

    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)

    print(f"\n✅ Terminé : {accepted} accepté(s), {skipped} skipped, {rejected_too_big} rejetés (diff trop gros).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
