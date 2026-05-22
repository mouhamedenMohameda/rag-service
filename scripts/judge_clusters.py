#!/usr/bin/env python3
"""LLM judge — pour chaque cluster candidat, décide quoi fusionner.

PHASE B — Lecture seule. Produit ``cluster_decisions_<matiere>.json`` avec
le plan de fusion. Aucune donnée modifiée. Phase C (apply_merges.py)
appliquera ce plan après revue.

Pour chaque cluster :
  - Envoie les labels + 1 énoncé exemple par notion
  - Le LLM décide :
      - "merge_all" → fusionner toutes en 1 ; donne new_label
      - "split"     → grouper en sous-clusters ; donne groups[][new_label]
      - "no_merge"  → ne pas fusionner (faux positif du clustering)

Usage :
    export GROQ_API_KEY=...
    python scripts/judge_clusters.py --matiere math
    python scripts/judge_clusters.py --matiere math --dry-run-llm   # vérifie sans appeler
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent


SYSTEM = """Tu es un correcteur expert en mathématiques/physique/SVT du Bac mauritanien.
On te donne un groupe de notions atomiques sémantiquement proches, repérées
automatiquement par embedding. Tu dois décider si elles décrivent
**la même compétence atomique** ou non, en t'appuyant sur les énoncés exemples.

Trois décisions possibles :

1. "merge_all" : TOUTES les notions désignent la même compétence atomique.
   Tu fournis un libellé canonique unique, atomique, réutilisable.
   Format du libellé : [opération / objet] — [contrainte / méthode]
   Exemple : "Décomposition d'une fraction rationnelle en éléments simples"

2. "split" : il y a 2+ compétences distinctes regroupées par erreur.
   Tu fournis 2+ sous-groupes en listant les ``nid`` qui vont ensemble,
   chacun avec son libellé canonique. Les nids qui restent seuls forment
   des sous-groupes de taille 1 (à laisser inchangés).
   Exemple : suite et série, ou IPP et substitution.

3. "no_merge" : tu n'es pas confiant, ou les notions sont vraiment distinctes.
   Laisser tel quel.

Règles strictes :
- Ne fusionne JAMAIS deux notions qui désignent des objets mathématiques
  différents (suite ≠ série, IPP ≠ substitution, fonction ≠ équation
  différentielle, etc.).
- Si deux notions diffèrent uniquement par l'exemple cité (e.g. "y''-4y'+5y=0"
  vs "y''-4y'+4y=0"), c'est la même compétence → merge.
- Le libellé canonique doit décrire la COMPÉTENCE, pas l'exemple particulier.
  Pas de nom de variable concret (f, uₙ, A, B…). Pas de coefficients numériques.

Réponds UNIQUEMENT en JSON, exactement ce schéma :

{
  "decision": "merge_all" | "split" | "no_merge",
  "reason": "courte justification (< 30 mots)",
  "groups": [
    {"nids": ["math.xxx", "math.yyy"], "new_label": "Libellé canonique"}
  ]
}

- Si "merge_all" : groups contient 1 seul élément avec tous les nids.
- Si "split"     : groups contient 2+ éléments. Les nids isolés peuvent être
                   omis (= rester tels quels).
- Si "no_merge"  : groups = [].
"""


def call_groq_judge(client, cluster: dict, model: str, examples_by_nid: dict[str, str]):
    """Appel Groq judge sur un cluster. Renvoie le dict décision ou None."""
    lines = ["NOTIONS DU CLUSTER :"]
    for m in cluster["members"]:
        nid = m["nid"]
        ex = examples_by_nid.get(nid, "")
        ex_short = (ex[:280] + "…") if len(ex) > 280 else ex
        lines.append(f"\n  • nid: {nid}")
        lines.append(f"    label: {m['label']}")
        lines.append(f"    nb_exos: {m['nb_exos']}")
        if ex_short:
            lines.append(f"    énoncé exemple: {ex_short}")
    user = "\n".join(lines)

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        temperature=0.2,  # un peu de variabilité, mais on reste précis
        response_format={"type": "json_object"},
        max_tokens=600,
    )
    content = resp.choices[0].message.content or ""
    try:
        obj = json.loads(content)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", content, re.DOTALL)
        if not m:
            return None
        obj = json.loads(m.group(0))

    if obj.get("decision") not in ("merge_all", "split", "no_merge"):
        return None
    # Sanity : si merge_all, normaliser groups à [{nids: all, new_label: ...}]
    decision = obj["decision"]
    groups = obj.get("groups") or []
    if decision == "merge_all":
        if not groups or "new_label" not in groups[0]:
            return None
        # Forcer tous les nids dans le seul groupe
        groups = [{"nids": [m["nid"] for m in cluster["members"]],
                   "new_label": groups[0]["new_label"]}]
    elif decision == "no_merge":
        groups = []
    obj["groups"] = groups
    return obj


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matiere", choices=["math", "pc", "svt"], default="math")
    ap.add_argument("--model", default="llama-3.3-70b-versatile")
    ap.add_argument("--sleep", type=float, default=0.4)
    ap.add_argument("--dry-run-llm", action="store_true",
                    help="Affiche les prompts sans appeler le LLM")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    candidates_path = ROOT / "scripts" / f"cluster_candidates_{args.matiere}.json"
    if not candidates_path.exists():
        print(f"ERREUR : {candidates_path} introuvable. Lance d'abord "
              f"cluster_singletons.py --matiere {args.matiere}", file=sys.stderr)
        return 2

    clusters = json.loads(candidates_path.read_text(encoding="utf-8"))
    if args.limit:
        clusters = clusters[: args.limit]
    print(f"→ {len(clusters)} cluster(s) à juger pour {args.matiere}")

    # Charger json_bac pour récupérer un énoncé exemple par notion
    data = json.loads((ROOT / "json_bac.json").read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in data}
    mp = json.loads((ROOT / "notions_map.json").read_text(encoding="utf-8"))

    examples_by_nid: dict[str, str] = {}
    random.seed(0)
    for c in clusters:
        for m in c["members"]:
            nid = m["nid"]
            if nid in examples_by_nid:
                continue
            exos = mp.get(nid, {}).get("exercices", [])
            if not exos:
                continue
            # Prendre l'énoncé d'1 exo au hasard (stable via seed)
            ex_id = random.choice(exos)["id"]
            ex = by_id.get(ex_id, {})
            examples_by_nid[nid] = (ex.get("ennonce_complet") or "").strip()

    if args.dry_run_llm:
        print("\n=== Dry-run prompts pour les 3 premiers clusters ===")
        for c in clusters[:3]:
            lines = []
            for m in c["members"]:
                ex = examples_by_nid.get(m["nid"], "")
                lines.append(f"• {m['label']} (nb={m['nb_exos']}) → ex: {ex[:120]}…")
            print(f"\nCluster {c['size']} notions, sim={c['mean_sim']}:")
            print("\n".join(lines))
        return 0

    if not os.environ.get("GROQ_API_KEY"):
        print("ERREUR : GROQ_API_KEY manquante.", file=sys.stderr)
        return 2

    from groq import Groq
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    decisions = []
    for k, c in enumerate(clusters, 1):
        print(f"[{k}/{len(clusters)}] cluster de {c['size']} notions "
              f"(sim={c['mean_sim']}) ", end="", flush=True)
        try:
            d = call_groq_judge(client, c, args.model, examples_by_nid)
        except Exception as ex:
            print(f"❌ {ex}")
            decisions.append({"cluster": c, "decision": None, "error": str(ex)})
            continue
        if not d:
            print("❌ parsing impossible")
            decisions.append({"cluster": c, "decision": None, "error": "parse"})
            continue
        decisions.append({"cluster": c, **d})
        if d["decision"] == "merge_all":
            new_lbl = d["groups"][0]["new_label"]
            print(f"✓ MERGE_ALL → '{new_lbl[:50]}'")
        elif d["decision"] == "split":
            print(f"✓ SPLIT en {len(d['groups'])} sous-groupes")
        else:
            print(f"✓ NO_MERGE — {d.get('reason','')[:50]}")
        if args.sleep > 0:
            time.sleep(args.sleep)

    out = ROOT / "scripts" / f"cluster_decisions_{args.matiere}.json"
    out.write_text(json.dumps(decisions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n✓ Écrit {out.relative_to(ROOT)}")

    # Stats
    from collections import Counter
    cnt = Counter(d.get("decision") for d in decisions)
    print(f"\nDécisions : merge_all={cnt.get('merge_all',0)}  "
          f"split={cnt.get('split',0)}  "
          f"no_merge={cnt.get('no_merge',0)}  "
          f"erreurs={cnt.get(None,0)}")
    nb_notions_fused = sum(
        len(g["nids"])
        for d in decisions if d.get("decision") in ("merge_all", "split")
        for g in d.get("groups", [])
        if len(g.get("nids", [])) >= 2
    )
    print(f"Notions à fusionner (au total) : {nb_notions_fused}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
