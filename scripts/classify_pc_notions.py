"""Classifie automatiquement les exos PC remplis : assigne `chapitre` et
`notions_traitees` parmi la taxonomie figée (notions_taxonomy_pc.py).

Critères de sélection des exos à classifier :
  - matiere_id ∈ {pc, physique, chimie} (pour compat legacy)
  - filiere_id filtrable
  - année dans la plage demandée
  - ennonce_complet non vide (sinon on n'a rien à classifier)
  - SAUF si --skip-existing : ignore les exos qui ont déjà un chapitre

Pour chaque exo, on appelle Groq avec un prompt **fermé** : il doit choisir
EXACTEMENT un chapitre dans la liste fournie et 3 à 6 notions parmi celles
du chapitre choisi. La réponse JSON est validée contre la taxonomie ; si
invalide, on logue et on passe.

N'écrase que `chapitre` et `notions_traitees`. Le reste reste intact.
Backup auto + dry-run.

Usage :
    python scripts/classify_pc_notions.py --from-year 2002 --to-year 2005 --dry-run
    python scripts/classify_pc_notions.py --from-year 2002 --to-year 2005
    python scripts/classify_pc_notions.py --filiere C --from-year 2002 --to-year 2005
    python scripts/classify_pc_notions.py --skip-existing  # ne reclassifie pas
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

# Charge .env pour GROQ_API_KEY
from dotenv import load_dotenv
load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"
sys.path.insert(0, str(ROOT / "scripts"))

from notions_taxonomy_pc import ALL_PC, all_chapters, notions_for, validate  # noqa


# ─── Prompt ──────────────────────────────────────────────────────────────────


def build_taxonomy_block() -> str:
    """Sérialise la taxonomie en bloc lisible à coller dans le prompt."""
    lines = []
    for chap, notions in ALL_PC.items():
        lines.append(f"## {chap}")
        for n in notions:
            lines.append(f"  - {n}")
        lines.append("")
    return "\n".join(lines)


SYSTEM_PROMPT = """Tu es un classifieur d'exercices Bac mauritanien (Sciences \
Physiques séries C et D). Ta tâche : pour un énoncé donné, choisir UN chapitre \
et 3 à 6 notions, en respectant STRICTEMENT la taxonomie ci-dessous. Tu ne \
peux PAS inventer de chapitre ni de notion. Tu réponds uniquement en JSON.

=== TAXONOMIE AUTORISÉE ===

{taxonomy}

=== RÈGLES ===

- Le chapitre choisi doit EXACTEMENT être l'un des intitulés ci-dessus.
- Les notions doivent EXACTEMENT être prises dans la liste sous le chapitre choisi.
- 3 à 6 notions, classées des plus centrales aux plus accessoires.
- Si l'énoncé couvre plusieurs chapitres, choisis CELUI qui pèse le plus.

Réponds en JSON strict, RIEN d'autre :
{{
  "chapitre": "<nom exact>",
  "notions": ["<n1>", "<n2>", "<n3>", ...]
}}"""


def user_prompt(ennonce: str) -> str:
    return f"ÉNONCÉ À CLASSIFIER :\n\n\"\"\"\n{ennonce}\n\"\"\"\n"


# ─── Groq call ───────────────────────────────────────────────────────────────


def call_groq(ennonce: str, model: str = "llama-3.3-70b-versatile") -> dict | None:
    """Appelle Groq et retourne le dict {chapitre, notions} ou None."""
    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    taxo = build_taxonomy_block()
    sys_prompt = SYSTEM_PROMPT.format(taxonomy=taxo)

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": user_prompt(ennonce)},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
        max_tokens=400,
    )
    content = resp.choices[0].message.content or ""
    try:
        obj = json.loads(content)
    except json.JSONDecodeError:
        # Tente d'extraire le premier objet JSON dans le texte
        m = re.search(r"\{.*\}", content, re.DOTALL)
        if not m:
            return None
        try:
            obj = json.loads(m.group(0))
        except json.JSONDecodeError:
            return None
    chap = obj.get("chapitre")
    notions = obj.get("notions") or []
    if not isinstance(chap, str) or not isinstance(notions, list):
        return None
    ok, msg = validate(chap, notions)
    if not ok:
        # On tente une réparation : on garde le chapitre proposé et on
        # filtre les notions à celles qui sont autorisées.
        if chap in ALL_PC:
            allowed = set(ALL_PC[chap])
            notions = [n for n in notions if n in allowed][:6]
            if 1 <= len(notions) <= 6:
                return {"chapitre": chap, "notions": notions}
        print(f"   ⚠️ Réponse invalide : {msg}")
        return None
    return {"chapitre": chap, "notions": notions[:6]}


# ─── Main pipeline ───────────────────────────────────────────────────────────


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-year", type=int, default=2002)
    ap.add_argument("--to-year", type=int, default=2024)
    ap.add_argument("--filiere", default=None, help="C ou D (défaut: les deux)")
    ap.add_argument("--skip-existing", action="store_true",
                    help="Ne reclassifie pas les exos qui ont déjà un chapitre rempli")
    ap.add_argument("--sleep", type=float, default=0.5,
                    help="Délai entre appels Groq (rate-limit safety)")
    ap.add_argument("--model", default="llama-3.3-70b-versatile")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    ap.add_argument("--limit", type=int, default=None,
                    help="Limite le nombre d'appels (test)")
    args = ap.parse_args()

    if not os.environ.get("GROQ_API_KEY"):
        print("ERREUR : GROQ_API_KEY manquante.", file=sys.stderr)
        return 2

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))

    # Sélection des cibles
    targets: list[int] = []
    for i, e in enumerate(data):
        if e.get("matiere_id") not in ("pc", "physique", "chimie"):
            continue
        if args.filiere and e.get("filiere_id") != args.filiere:
            continue
        annee = e.get("annee")
        if not isinstance(annee, int) or not (args.from_year <= annee <= args.to_year):
            continue
        if not (e.get("ennonce_complet") or "").strip():
            continue
        if args.skip_existing and (e.get("chapitre") or "").strip():
            continue
        targets.append(i)

    if args.limit:
        targets = targets[: args.limit]

    print(f"\n→ {len(targets)} exo(s) à classifier "
          f"(années {args.from_year}-{args.to_year}, "
          f"filière {args.filiere or 'C+D'}, "
          f"skip-existing={args.skip_existing}).")
    if args.dry_run:
        for i in targets[:10]:
            e = data[i]
            print(f"   - {e.get('id')} ({e.get('chapitre', '(vide)')})")
        if len(targets) > 10:
            print(f"   … et {len(targets)-10} autres")
        print("\n(--dry-run : aucune écriture)")
        return 0

    # Backup AVANT toute écriture
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-classify-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"Backup : {backup}\n")

    success = 0
    failures: list[str] = []
    for k, i in enumerate(targets, 1):
        e = data[i]
        eid = e.get("id", "?")
        print(f"[{k}/{len(targets)}] {eid:<40} ", end="", flush=True)
        try:
            res = call_groq(e["ennonce_complet"], model=args.model)
        except Exception as ex:
            failures.append(f"{eid} : {ex}")
            print(f"❌ {ex}")
            continue
        if not res:
            failures.append(f"{eid} : réponse invalide")
            print("❌ réponse invalide")
            continue
        # Patch les champs autorisés UNIQUEMENT
        e["chapitre"] = res["chapitre"]
        e["notions_traitees"] = res["notions"]
        e["updated_at"] = datetime.now().isoformat(timespec="seconds")
        success += 1
        print(f"✓ {res['chapitre']} · {len(res['notions'])} notions")
        # Sauvegarde incrémentale tous les 10 exos pour ne rien perdre si on
        # se fait interrompre
        if k % 10 == 0:
            tmp = p.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            tmp.replace(p)
        if args.sleep > 0:
            time.sleep(args.sleep)

    # Sauvegarde finale
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)

    print(f"\n✅ Terminé : {success}/{len(targets)} classifiés.")
    if failures:
        print(f"\n❌ {len(failures)} échec(s) :")
        for f in failures:
            print(f"   - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
