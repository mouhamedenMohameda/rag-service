#!/usr/bin/env python3
"""Cluster notions by semantic similarity to surface fusion candidates.

PHASE A — Lecture seule. Produit `scripts/cluster_candidates_<matiere>.json`
pour relecture humaine. Aucune donnée modifiée.

Pipeline :
    1. Charge notions_registry.json filtré par matière
    2. Embed les labels via OpenAI text-embedding-3-small
    3. Cosine similarity tous-vs-tous, threshold paramétrable
    4. Union-Find sur les paires → composants connexes
    5. Sortie : clusters ≥2 notions, triés par taille

Usage :
    export OPENAI_API_KEY=...
    python scripts/cluster_singletons.py --matiere math
    python scripts/cluster_singletons.py --matiere math --threshold 0.88
    python scripts/cluster_singletons.py --matiere math --singletons-only

PHASE B (à venir, autre script) : LLM judge + application aux données.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent


def embed_openai(texts: list[str], model: str = "text-embedding-3-small"):
    """Embed via OpenAI, batched. Returns list of vectors (lists of floats)."""
    try:
        from openai import OpenAI
    except ImportError:
        print("ERREUR : package 'openai' manquant. pip install openai", file=sys.stderr)
        sys.exit(2)
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERREUR : OPENAI_API_KEY manquante (mets-la dans .env).", file=sys.stderr)
        sys.exit(2)

    client = OpenAI()
    out: list[list[float]] = []
    BATCH = 100
    for i in range(0, len(texts), BATCH):
        batch = texts[i : i + BATCH]
        resp = client.embeddings.create(model=model, input=batch)
        out.extend(d.embedding for d in resp.data)
        print(f"  embedded {min(i + BATCH, len(texts))}/{len(texts)}")
    return out


def cosine_sim_matrix(vecs):
    """Returns (vecs_normalized @ vecs_normalized.T) using only stdlib + numpy."""
    import numpy as np

    arr = np.asarray(vecs, dtype="float32")
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    arr = arr / np.clip(norms, 1e-9, None)
    return arr @ arr.T


def pairs_above(sims, threshold: float):
    """Returns sorted list of (i, j, sim) for i<j and sim≥threshold."""
    import numpy as np

    n = sims.shape[0]
    iu, ju = np.triu_indices(n, k=1)
    mask = sims[iu, ju] >= threshold
    out = [(int(iu[k]), int(ju[k]), float(sims[iu[k], ju[k]])) for k in np.where(mask)[0]]
    out.sort(key=lambda t: -t[2])
    return out


class UnionFind:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--matiere", choices=["math", "pc", "svt"], default="math")
    ap.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Seuil cosine pour considérer deux notions comme fusionnables. "
        "Empiriquement : 0.90 = quasi-identique, 0.85 = très proche, "
        "0.80 = même domaine large.",
    )
    ap.add_argument(
        "--singletons-only",
        action="store_true",
        help="Ne clusteriser que les notions liées à ≤2 exos. "
        "Évite de fusionner les gros clusters déjà cohérents.",
    )
    ap.add_argument(
        "--max-cluster-size",
        type=int,
        default=15,
        help="Tronque les clusters plus grands (probablement une dérive du seuil).",
    )
    ap.add_argument("--output", default=None)
    args = ap.parse_args()

    reg = json.loads((ROOT / "notions_registry.json").read_text(encoding="utf-8"))
    mp = json.loads((ROOT / "notions_map.json").read_text(encoding="utf-8"))

    # Items = (notion_id, label, nb_exos)
    items: list[tuple[str, str, int]] = []
    for nid, data in reg.items():
        if data.get("matiere_id") != args.matiere:
            continue
        label = data.get("label") or ""
        if not label.strip():
            continue
        nb_exos = len(mp.get(nid, {}).get("exercices", []))
        if args.singletons_only and nb_exos > 2:
            continue
        items.append((nid, label, nb_exos))

    print(f"Matière : {args.matiere}")
    print(f"  filtre singletons-only : {args.singletons_only}")
    print(f"  {len(items)} notions à clusteriser")
    if len(items) < 2:
        print("Pas assez de notions, abandon.")
        return 0

    labels = [it[1] for it in items]
    print("\nEmbedding via OpenAI text-embedding-3-small...")
    vecs = embed_openai(labels)

    print(f"\nCalcul similarité cosine (threshold = {args.threshold})...")
    sims = cosine_sim_matrix(vecs)
    pairs = pairs_above(sims, args.threshold)
    print(f"  {len(pairs)} paire(s) au-dessus du seuil")

    if pairs[:5]:
        print("\n  Top 5 paires (similarité décroissante) :")
        for i, j, s in pairs[:5]:
            print(f"    {s:.3f}  '{items[i][1][:50]}' ↔ '{items[j][1][:50]}'")

    uf = UnionFind(len(items))
    for i, j, _ in pairs:
        uf.union(i, j)

    clusters: dict[int, list[int]] = {}
    for i in range(len(items)):
        clusters.setdefault(uf.find(i), []).append(i)
    multi = [idxs for idxs in clusters.values() if len(idxs) >= 2]
    multi.sort(key=len, reverse=True)
    print(f"\n  {len(multi)} cluster(s) de fusion candidat(s) (≥2 notions)")

    # Construction de la sortie
    output = []
    huge = 0
    for idxs in multi:
        if len(idxs) > args.max_cluster_size:
            huge += 1
            continue  # cluster suspect, à filtrer ou baisser threshold
        members = []
        for i in idxs:
            nid, label, nb = items[i]
            members.append({"nid": nid, "label": label, "nb_exos": nb})
        # Internal similarity stats : moyenne des paires du cluster
        cluster_pairs_sims = [
            float(sims[i, j])
            for i in idxs
            for j in idxs
            if i < j
        ]
        output.append(
            {
                "size": len(members),
                "total_exos": sum(m["nb_exos"] for m in members),
                "mean_sim": round(sum(cluster_pairs_sims) / len(cluster_pairs_sims), 3)
                if cluster_pairs_sims
                else None,
                "min_sim": round(min(cluster_pairs_sims), 3) if cluster_pairs_sims else None,
                "members": sorted(members, key=lambda m: -m["nb_exos"]),
            }
        )
    if huge:
        print(f"  ⚠️  {huge} cluster(s) ignoré(s) car >{args.max_cluster_size} notions "
              f"(probable dérive du seuil — baisse-le ou utilise --singletons-only)")
    output.sort(key=lambda c: -c["size"])

    out_path = Path(args.output) if args.output else (
        ROOT / "scripts" / f"cluster_candidates_{args.matiere}.json"
    )
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n✓ Écrit {out_path.relative_to(ROOT)} ({len(output)} clusters)")

    # Aperçu top 10
    print("\nAperçu — top 10 clusters par taille :")
    for k, c in enumerate(output[:10], 1):
        print(f"\n  [{k}] {c['size']} notions, {c['total_exos']} exos total, "
              f"mean_sim={c['mean_sim']}, min_sim={c['min_sim']}")
        for m in c["members"][:5]:
            print(f"      ({m['nb_exos']}) {m['label'][:70]}")
        if c["size"] > 5:
            print(f"      ... +{c['size']-5} autres")

    # Stats finales
    in_cluster = sum(c["size"] for c in output)
    print(f"\nStats : {in_cluster} notions dans {len(output)} clusters "
          f"(soit {100*in_cluster/len(items):.0f}% des notions analysées)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
