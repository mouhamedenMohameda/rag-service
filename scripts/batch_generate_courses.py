"""Script batch : génère N cours de maths via Groq avec tracking de coût.

Utilisation :
    # Test prod sur 50 notions math (sélection auto : top par nb d'exos bac)
    python scripts/batch_generate_courses.py --matiere math --limit 50

    # Reprendre après crash (skip ce qui est déjà dans cours.json)
    python scripts/batch_generate_courses.py --matiere math --limit 50 --resume

    # Forcer la régénération même si déjà présent
    python scripts/batch_generate_courses.py --matiere math --limit 50 --force

    # Dry-run : afficher les notions sélectionnées sans appeler Groq
    python scripts/batch_generate_courses.py --matiere math --limit 50 --dry-run

    # Tester sur une seule notion précise
    python scripts/batch_generate_courses.py --notion math.complexe.similitude

Variables d'environnement requises :
    GROQ_API_KEY    Clé API Groq

Le script écrit dans ``cours.json`` (à la racine du rag-service) après chaque
notion (donc resume gratuit en cas d'interruption).
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

# Permet d'importer course_generator / katex_validator depuis le dossier parent
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from course_generator import (  # noqa: E402
    MODEL_DEEP,
    MODEL_FAST,
    generate_course,
    pick_model,
)
from katex_validator import validate  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("batch")


# ─── Chargement des données ──────────────────────────────────────────────────

def load_json(path: Path) -> dict | list:
    if not path.exists():
        raise FileNotFoundError(f"{path} introuvable")
    return json.loads(path.read_text(encoding="utf-8"))


# ─── Sélection des notions à traiter ────────────────────────────────────────

def select_notions(
    registry: dict,
    notions_map: dict,
    json_bac: list,
    matiere: str,
    limit: int,
    min_exos: int = 3,
) -> list[dict]:
    """Sélectionne les notions à traiter.

    Critères :
      - matiere_id correspondant
      - au moins ``min_exos`` exos de bac avec énoncé exploitable (>200 chars)
      - tri par nb d'exos bac décroissant (meilleur contexte ANNALES_BAC)
      - top ``limit``
    """
    by_id = {e["id"]: e for e in json_bac}

    candidates = []
    for nid, entry in registry.items():
        if entry.get("matiere_id") != matiere:
            continue
        refs = notions_map.get(nid, {}).get("exercices") or []
        usable = [
            by_id[r["id"]]
            for r in refs
            if r["id"] in by_id
            and len((by_id[r["id"]].get("ennonce_complet") or "").strip()) >= 200
        ]
        if len(usable) < min_exos:
            continue
        candidates.append({
            "notion_id": nid,
            "label": entry.get("label", nid),
            "chapitre": entry.get("chapitre", ""),
            "matiere_id": matiere,
            "annales_bac": usable,
            "nb_exos": len(usable),
        })

    candidates.sort(key=lambda c: (-c["nb_exos"], c["notion_id"]))
    return candidates[:limit]


# ─── Sauvegarde atomique de cours.json ───────────────────────────────────────

def load_courses(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_courses(path: Path, data: dict, backup_dir: Optional[Path] = None) -> None:
    if backup_dir and path.exists():
        backup_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(path, backup_dir / f"cours-{stamp}.json")
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    tmp.replace(path)


# ─── Boucle principale ───────────────────────────────────────────────────────

def run(args: argparse.Namespace) -> int:
    root = ROOT
    registry = load_json(root / "notions_registry.json")
    notions_map = load_json(root / "notions_map.json")
    json_bac = load_json(root / "json_bac.json")
    courses_path = root / "cours.json"
    backup_dir = root / "json_backups" / "cours"

    # Sélection
    if args.notion:
        # Single notion
        nid = args.notion
        if nid not in registry:
            log.error("Notion '%s' introuvable dans le registry", nid)
            return 1
        entry = registry[nid]
        refs = notions_map.get(nid, {}).get("exercices") or []
        by_id = {e["id"]: e for e in json_bac}
        usable = [
            by_id[r["id"]]
            for r in refs
            if r["id"] in by_id
            and len((by_id[r["id"]].get("ennonce_complet") or "").strip()) >= 200
        ]
        selected = [{
            "notion_id": nid,
            "label": entry.get("label", nid),
            "chapitre": entry.get("chapitre", ""),
            "matiere_id": entry.get("matiere_id", ""),
            "annales_bac": usable,
            "nb_exos": len(usable),
        }]
    else:
        selected = select_notions(
            registry=registry,
            notions_map=notions_map,
            json_bac=json_bac,
            matiere=args.matiere,
            limit=args.limit,
            min_exos=args.min_exos,
        )

    log.info("Notions sélectionnées : %d", len(selected))
    for i, c in enumerate(selected[:10], 1):
        log.info("  [%2d] %s (%d exos)", i, c["notion_id"], c["nb_exos"])
    if len(selected) > 10:
        log.info("  ... et %d autres", len(selected) - 10)

    if args.dry_run:
        log.info("[DRY-RUN] Arrêt avant les appels Groq.")
        # Affiche aussi le routing prévu
        n_fast = sum(1 for c in selected if pick_model(c["notion_id"], c["label"]) == MODEL_FAST)
        n_deep = len(selected) - n_fast
        log.info("Routing prévu : %d notions → %s, %d notions → %s",
                 n_fast, MODEL_FAST, n_deep, MODEL_DEEP)
        return 0

    if not os.environ.get("GROQ_API_KEY"):
        log.error("GROQ_API_KEY absente. export GROQ_API_KEY=...")
        return 2

    # Chargement courses existants
    courses = load_courses(courses_path)
    log.info("Cours existants : %d", len(courses))

    # Métriques
    total_cost = 0.0
    total_in_tokens = 0
    total_out_tokens = 0
    n_ok = 0
    n_invalid = 0
    n_skipped = 0
    n_error = 0
    start = time.time()

    for i, c in enumerate(selected, 1):
        nid = c["notion_id"]
        label = c["label"]

        if nid in courses and not args.force and args.resume:
            log.info("[%2d/%d] SKIP (déjà présent) %s", i, len(selected), nid)
            n_skipped += 1
            continue
        if nid in courses and not args.force:
            log.info("[%2d/%d] SKIP (déjà présent, --force pour écraser) %s",
                     i, len(selected), nid)
            n_skipped += 1
            continue

        model = args.model or pick_model(nid, label)
        log.info("[%2d/%d] %s | %s | model=%s | %d annales",
                 i, len(selected), nid, label[:50], model.split("-")[0], c["nb_exos"])

        try:
            t0 = time.time()
            result = generate_course(
                label=label,
                notion_id=nid,
                chapitre=c.get("chapitre", ""),
                annales_bac=c["annales_bac"],
                serie_hint=None,  # cours générique séries C+D
                model=model,
            )
            elapsed = time.time() - t0
        except Exception as e:
            log.error("    ❌ Erreur Groq : %s", e)
            n_error += 1
            if args.stop_on_error:
                return 3
            continue

        # Validation KaTeX
        report = validate(result.content)
        status = "✅ OK" if report.ok else "⚠️ INVALID"
        if not report.ok:
            n_invalid += 1
            log.warning("    %s", report.summary().replace("\n", "\n    "))
        else:
            n_ok += 1

        total_cost += result.cost_usd
        total_in_tokens += result.prompt_tokens
        total_out_tokens += result.completion_tokens

        log.info("    %s | %d in + %d out tokens | $%.4f | %.1fs",
                 status, result.prompt_tokens, result.completion_tokens,
                 result.cost_usd, elapsed)

        # Sauvegarde immédiate (resume gratuit)
        courses[nid] = {
            "content": result.content,
            "model": result.model,
            "generated_at": datetime.utcnow().isoformat(timespec="seconds"),
            "edited_at": None,
            "validated_by_admin": False,
            "notion_label": label,
            "context_exo_ids": [e["id"] for e in c["annales_bac"]],
            "validation": {
                "ok": report.ok,
                "errors": report.errors,
                "warnings": report.warnings,
            },
            "metrics": {
                "prompt_tokens": result.prompt_tokens,
                "completion_tokens": result.completion_tokens,
                "cost_usd": result.cost_usd,
                "duration_s": round(elapsed, 2),
            },
        }
        save_courses(courses_path, courses, backup_dir=backup_dir if i == 1 else None)

        # Petit délai pour respecter le rate-limit Groq (gentle)
        if i < len(selected):
            time.sleep(args.delay)

    elapsed_total = time.time() - start

    log.info("=" * 60)
    log.info("BATCH TERMINÉ")
    log.info("  Notions traitées  : %d", len(selected))
    log.info("  ✅ Valides         : %d", n_ok)
    log.info("  ⚠️  Invalides       : %d", n_invalid)
    log.info("  ⏭️  Skippées        : %d", n_skipped)
    log.info("  ❌ Erreurs         : %d", n_error)
    log.info("  Tokens in/out     : %d / %d", total_in_tokens, total_out_tokens)
    log.info("  💰 Coût total     : $%.4f", total_cost)
    log.info("  ⏱️  Durée totale   : %.1fs (%.1fs/notion)",
             elapsed_total, elapsed_total / max(1, len(selected) - n_skipped))
    log.info("=" * 60)

    if n_invalid > 0:
        log.warning("Pour examiner les invalides : "
                    "jq '.[].validation | select(.ok==false)' cours.json")

    return 0


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--matiere", default="math", help="math|pc|svt (défaut: math)")
    p.add_argument("--limit", type=int, default=50, help="Nombre max de notions")
    p.add_argument("--min-exos", type=int, default=3,
                   help="Minimum d'exos bac requis par notion")
    p.add_argument("--notion", default=None,
                   help="Traiter UNE notion spécifique (ignore matiere/limit)")
    p.add_argument("--force", action="store_true",
                   help="Régénérer même si déjà présent")
    p.add_argument("--resume", action="store_true",
                   help="Reprendre : skip notions déjà présentes")
    p.add_argument("--dry-run", action="store_true",
                   help="Affiche la sélection sans appeler Groq")
    p.add_argument("--delay", type=float, default=1.0,
                   help="Délai entre 2 notions (s) — protège du rate-limit")
    p.add_argument("--stop-on-error", action="store_true",
                   help="Arrête le batch à la première erreur Groq")
    p.add_argument("--model", default=None,
                   help="Force un modèle spécifique (override le routing 2-étages)")
    return p.parse_args()


if __name__ == "__main__":
    sys.exit(run(parse_args()))
