#!/usr/bin/env python3
"""Applique les décisions de fusion du LLM judge aux données canoniques.

PHASE C — Modifie notions_registry.json, notions_map.json, json_bac.json.
Backups automatiques avant écriture. Mode --dry-run pour preview.

Entrée :
    scripts/cluster_decisions_<matiere>.json (produit par judge_clusters.py
    puis éventuellement patché manuellement)

Pour chaque groupe à fusionner (≥2 nids) :
  1. Choisit canonical_nid = celui avec le plus d'exos liés
     (tiebreak : ordre lexicographique du nid)
  2. registry[canonical_nid].label   ← new_label
  3. registry[canonical_nid].aliases ← anciens labels + aliases des absorbés
  4. map[canonical_nid].exercices    ← union dédupliquée des 'exercices'
  5. Supprime les nids absorbés du registry et de la map
  6. Pour chaque exo dans json_bac : remplace les nids absorbés par
     canonical_nid (dédupliqué), idem pour les labels dans notions_traitees

Usage :
    python scripts/apply_merges.py --matiere math --dry-run
    python scripts/apply_merges.py --matiere math
"""
from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matiere", choices=["math", "pc", "svt"], default="math")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    decisions_path = ROOT / "scripts" / f"cluster_decisions_{args.matiere}.json"
    if not decisions_path.exists():
        print(f"ERREUR : {decisions_path} introuvable.")
        return 2

    decisions = json.loads(decisions_path.read_text(encoding="utf-8"))
    reg = json.loads((ROOT / "notions_registry.json").read_text(encoding="utf-8"))
    mp = json.loads((ROOT / "notions_map.json").read_text(encoding="utf-8"))
    data = json.loads((ROOT / "json_bac.json").read_text(encoding="utf-8"))

    # Construit la liste des groupes à fusionner : [(canonical_nid, new_label, absorbed_nids)]
    merges: list[tuple[str, str, list[str], list[str]]] = []
    # tuple = (canonical_nid, new_label, absorbed_nids, all_member_nids)
    for d in decisions:
        if d.get("decision") not in ("merge_all", "split"):
            continue
        for g in d.get("groups") or []:
            nids = g.get("nids") or []
            new_label = g.get("new_label") or ""
            if len(nids) < 2:
                continue  # singleton group → rien à faire
            if not new_label.strip():
                print(f"⚠️  groupe sans new_label : {nids}, skipped")
                continue
            # Tiebreak : nid avec le plus d'exos, puis ordre alpha
            by_nb = sorted(
                nids,
                key=lambda n: (-len(mp.get(n, {}).get("exercices", [])), n),
            )
            canonical = by_nb[0]
            absorbed = by_nb[1:]
            merges.append((canonical, new_label, absorbed, nids))

    print(f"Plan : {len(merges)} fusion(s) à appliquer (matière {args.matiere})")

    # Aperçu
    for k, (canon, new_lbl, absorbed, _) in enumerate(merges[:10], 1):
        n_can = len(mp.get(canon, {}).get("exercices", []))
        n_abs = sum(len(mp.get(a, {}).get("exercices", [])) for a in absorbed)
        print(f"  [{k}] {canon} ({n_can} exos) ← {len(absorbed)} absorbé(s) ({n_abs} exos) "
              f"→ '{new_lbl[:50]}'")
    if len(merges) > 10:
        print(f"  ... +{len(merges)-10} autres")

    if args.dry_run:
        print("\n--dry-run : aucune modification.")
        return 0

    # Backup
    BK = ROOT / "json_backups"
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    for fname in ["notions_registry.json", "notions_map.json", "json_bac.json"]:
        shutil.copy2(ROOT / fname, BK / f"{Path(fname).stem}-pre-apply-merges-{args.matiere}-{ts}{Path(fname).suffix}")
    print(f"\nbackups → timestamp {ts}")

    # Construit absorbed_to_canonical et label_remap (old_label → new_label)
    absorbed_to_canonical: dict[str, str] = {}
    label_remap: dict[str, str] = {}  # label sourd → new_label canonique
    for canon, new_lbl, absorbed, all_nids in merges:
        # On remap aussi le canonical si son ancien label diffère du new_label
        canon_old_label = reg.get(canon, {}).get("label")
        if canon_old_label and canon_old_label != new_lbl:
            label_remap[canon_old_label] = new_lbl
        for a in absorbed:
            absorbed_to_canonical[a] = canon
            old_lbl = reg.get(a, {}).get("label")
            if old_lbl:
                label_remap[old_lbl] = new_lbl
            # Aliases existants des absorbés → tous remap vers new_label
            for al in (reg.get(a, {}).get("aliases") or []):
                label_remap[al] = new_lbl

    # 1) Mise à jour du registry : label, aliases, suppression des absorbés
    for canon, new_lbl, absorbed, all_nids in merges:
        canon_entry = reg.setdefault(canon, {})
        old_label = canon_entry.get("label")
        new_aliases = set(canon_entry.get("aliases") or [])
        if old_label and old_label != new_lbl:
            new_aliases.add(old_label)
        for a in absorbed:
            absorbed_entry = reg.get(a, {})
            old_a = absorbed_entry.get("label")
            if old_a:
                new_aliases.add(old_a)
            for al in (absorbed_entry.get("aliases") or []):
                new_aliases.add(al)
        canon_entry["label"] = new_lbl
        canon_entry["aliases"] = sorted(new_aliases)
    for a in absorbed_to_canonical:
        if a in reg:
            del reg[a]

    # 2) Mise à jour de la map : fusion des exercices, suppression des absorbés
    for canon, new_lbl, absorbed, all_nids in merges:
        canon_map = mp.setdefault(canon, {"label": new_lbl, "exercices": []})
        canon_map["label"] = new_lbl
        seen_ids = {ex["id"] for ex in canon_map.get("exercices") or []}
        for a in absorbed:
            for ex in (mp.get(a, {}).get("exercices") or []):
                if ex["id"] not in seen_ids:
                    canon_map.setdefault("exercices", []).append(ex)
                    seen_ids.add(ex["id"])
    for a in absorbed_to_canonical:
        if a in mp:
            del mp[a]

    # 3) Mise à jour de json_bac.json : remap des notion_ids et notions_traitees
    changed_exos = 0
    for e in data:
        nids = e.get("notion_ids") or []
        nts = e.get("notions_traitees") or []
        # Remap nids : absorbé → canonical, dédupliqué en préservant l'ordre
        new_nids: list[str] = []
        seen_n = set()
        for n in nids:
            mapped = absorbed_to_canonical.get(n, n)
            if mapped not in seen_n:
                new_nids.append(mapped)
                seen_n.add(mapped)
        # Remap labels en parallèle (par position, fallback par label_remap)
        new_nts: list[str] = []
        seen_l = set()
        for lbl in nts:
            remapped = label_remap.get(lbl, lbl)
            if remapped not in seen_l:
                new_nts.append(remapped)
                seen_l.add(remapped)
        if new_nids != nids or new_nts != nts:
            e["notion_ids"] = new_nids
            e["notions_traitees"] = new_nts
            changed_exos += 1

    # Écrire
    (ROOT / "notions_registry.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "notions_map.json").write_text(
        json.dumps(mp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "json_bac.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Stats finales
    print(f"\n✓ {changed_exos} exo(s) mis à jour dans json_bac.json")
    print(f"✓ {len(absorbed_to_canonical)} notion(s) absorbée(s) supprimée(s)")
    print(f"✓ Registry : {len(reg)} notions (avant : {len(reg) + len(absorbed_to_canonical)})")
    print(f"✓ Map      : {len(mp)} entries")

    # Diff singletons
    new_singletons = sum(1 for v in mp.values() if len(v.get('exercices', [])) == 1)
    new_ge2 = sum(1 for v in mp.values() if len(v.get('exercices', [])) >= 2)
    new_ge3 = sum(1 for v in mp.values() if len(v.get('exercices', [])) >= 3)
    print(f"  singletons : {new_singletons}")
    print(f"  ≥2 exos    : {new_ge2}")
    print(f"  ≥3 exos    : {new_ge3}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
