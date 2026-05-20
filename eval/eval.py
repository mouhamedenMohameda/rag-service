"""Évalue le rag-service contre le gold set (eval/gold.jsonl).

Phase 0 : mesure le retrieval (Recall@5, MRR) et la latence.
Phase 1+ : ajoutera citation_accuracy et style_score quand on aura la
génération de réponses branchée.

Usage :
    python eval/eval.py
    python eval/eval.py --rag-url http://127.0.0.1:8001 --top-k 5
    python eval/eval.py --gold eval/gold.jsonl --out eval/runs

Exit code : 0 si recall@5 ≥ seuil (--min-recall, défaut 0.6), 1 sinon.
Utile pour intégrer dans une CI ou un script de deploy.
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv


# ─── Chargement gold ────────────────────────────────────────────────────────


def load_gold(path: Path) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            try:
                cases.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise SystemExit(f"gold.jsonl ligne {i} invalide : {e}")
    return cases


# ─── Matching attendu ↔ retourné ────────────────────────────────────────────


def source_matches(expected: list[str], actual_source: str) -> bool:
    """Substring match case-insensitive. Tolère les variantes de nom de fichier
    (ex. "Bac C 2002" matche "Bac C 2002 a 2012 sn et sc corrigé.pdf")."""
    s = actual_source.lower()
    return any(needle.lower() in s for needle in expected)


def first_match_rank(expected: list[str], chunks: list[dict[str, Any]]) -> int:
    """Renvoie le rang 1-indexé du premier chunk dont la source matche.
    0 si aucun match dans la liste."""
    for i, c in enumerate(chunks, 1):
        if source_matches(expected, str(c.get("source", ""))):
            return i
    return 0


# ─── Appel rag-service ──────────────────────────────────────────────────────


def call_search(
    base_url: str, api_key: str, subject: str, query: str, top_k: int, timeout: float
) -> tuple[dict[str, Any], float]:
    """Appelle POST /search. Retourne (data, latency_ms) où data contient
    chunks, low_confidence, min_score_threshold. Lève RuntimeError sur HTTP."""
    t0 = time.perf_counter()
    r = httpx.post(
        f"{base_url.rstrip('/')}/search",
        headers={"X-Api-Key": api_key, "Content-Type": "application/json"},
        json={"subject": subject, "query": query, "top_k": top_k},
        timeout=timeout,
    )
    latency_ms = (time.perf_counter() - t0) * 1000
    if r.status_code >= 400:
        raise RuntimeError(f"/search HTTP {r.status_code}: {r.text[:300]}")
    return r.json(), latency_ms


# ─── Rapport ────────────────────────────────────────────────────────────────


def percentile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * p
    f = int(k)
    c = min(f + 1, len(s) - 1)
    if f == c:
        return s[f]
    return s[f] + (s[c] - s[f]) * (k - f)


def render_report(results: list[dict[str, Any]], top_k: int) -> str:
    n = len(results)
    if n == 0:
        return "# Eval RAG\n\n_Aucun cas évalué._\n"

    hits = sum(1 for r in results if r["rank"] > 0)
    recall = hits / n
    mrr = sum((1.0 / r["rank"]) if r["rank"] > 0 else 0.0 for r in results) / n
    lats = [r["latency_ms"] for r in results if r["latency_ms"] is not None]
    p50 = percentile(lats, 0.5)
    p95 = percentile(lats, 0.95)
    mean_lat = statistics.mean(lats) if lats else 0.0

    # Phase 1 — confiance retrieval
    scores = [r["top_score"] for r in results if r.get("top_score") is not None]
    mean_top_score = statistics.mean(scores) if scores else 0.0
    low_conf = sum(1 for r in results if r.get("low_confidence"))
    low_conf_rate = low_conf / n if n else 0.0
    threshold = next((r["min_score"] for r in results if r.get("min_score") is not None), None)

    lines = [
        f"# Eval RAG — {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"- Cas évalués : **{n}**",
        f"- Recall@{top_k} : **{recall:.0%}** ({hits}/{n})",
        f"- MRR : **{mrr:.3f}**",
        f"- Top score moyen : **{mean_top_score:.3f}**"
        + (f" (seuil low_confidence = {threshold:.2f})" if threshold is not None else ""),
        f"- Taux low_confidence : **{low_conf_rate:.0%}** ({low_conf}/{n})",
        f"- Latence : moyenne {mean_lat:.0f} ms · p50 {p50:.0f} ms · p95 {p95:.0f} ms",
        "",
        "## Détail par cas",
        "",
        "| ID | Subject | Rank | Top score | Low conf. | Latence (ms) | Top source |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in results:
        rank_str = str(r["rank"]) if r["rank"] > 0 else "—"
        top_src = r["top_source"] or "(rien)"
        lat = f"{r['latency_ms']:.0f}" if r["latency_ms"] is not None else "ERR"
        ts = f"{r['top_score']:.3f}" if r.get("top_score") is not None else "—"
        lc = "⚠️" if r.get("low_confidence") else "ok"
        lines.append(
            f"| {r['id']} | {r['subject']} | {rank_str} | {ts} | {lc} | {lat} | {top_src} |"
        )

    errs = [r for r in results if r.get("error")]
    if errs:
        lines += ["", "## Erreurs", ""]
        for r in errs:
            lines.append(f"- **{r['id']}** : {r['error']}")

    lines.append("")
    return "\n".join(lines)


# ─── Main ───────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description="Eval RAG retrieval")
    parser.add_argument("--gold", default="eval/gold.jsonl")
    parser.add_argument("--rag-url", default=os.environ.get("RAG_URL", "http://127.0.0.1:8001"))
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--out", default="eval/runs")
    parser.add_argument("--min-recall", type=float, default=0.6,
                        help="Recall@K minimum pour exit 0 (CI gate)")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("RAG_S2S_KEY")
    if not api_key:
        print("ERREUR : RAG_S2S_KEY manquant (.env ou env var).", file=sys.stderr)
        return 2

    gold_path = Path(args.gold)
    if not gold_path.exists():
        print(f"ERREUR : gold introuvable : {gold_path}", file=sys.stderr)
        return 2

    cases = load_gold(gold_path)
    if not cases:
        print("ERREUR : aucun cas dans le gold.", file=sys.stderr)
        return 2

    results: list[dict[str, Any]] = []
    for case in cases:
        cid = case.get("id", "?")
        subject = case.get("subject", "")
        query = case.get("query", "")
        expected = case.get("expected_sources") or []
        if not subject or not query or not expected:
            results.append({
                "id": cid, "subject": subject, "rank": 0, "latency_ms": None,
                "top_source": None, "error": "cas mal formé (subject/query/expected_sources requis)",
            })
            continue
        try:
            data, lat = call_search(
                args.rag_url, api_key, subject, query, args.top_k, args.timeout
            )
            chunks = data.get("chunks", [])
            rank = first_match_rank(expected, chunks)
            top_src = str(chunks[0].get("source")) if chunks else None
            top_score = float(chunks[0].get("score")) if chunks else None
            results.append({
                "id": cid, "subject": subject, "rank": rank,
                "latency_ms": lat, "top_source": top_src,
                "top_score": top_score,
                "low_confidence": bool(data.get("low_confidence", False)),
                "min_score": data.get("min_score_threshold"),
                "error": None,
            })
        except Exception as e:
            results.append({
                "id": cid, "subject": subject, "rank": 0, "latency_ms": None,
                "top_source": None, "top_score": None,
                "low_confidence": True, "min_score": None,
                "error": str(e),
            })

    report = render_report(results, args.top_k)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_file = out_dir / f"{stamp}.md"
    out_file.write_text(report, encoding="utf-8")

    if not args.quiet:
        print(report)
        print(f"\n→ Rapport écrit : {out_file}")

    n = len(results)
    hits = sum(1 for r in results if r["rank"] > 0)
    recall = hits / n if n else 0.0
    return 0 if recall >= args.min_recall else 1


if __name__ == "__main__":
    sys.exit(main())
