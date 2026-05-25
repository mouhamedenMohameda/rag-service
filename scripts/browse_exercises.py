#!/usr/bin/env python3
"""
browse_exercises.py — Parcourt tous les exercices du json_bac LOCAL.

Pour chaque exercice avec un énoncé :
  - Affiche le titre, la matière, le chapitre
  - Pour les exercices de math : appelle Newton API pour valider les expressions

Usage :
  python scripts/browse_exercises.py                      # tous
  python scripts/browse_exercises.py --matiere math       # math seulement
  python scripts/browse_exercises.py --matiere pc         # physique-chimie
  python scripts/browse_exercises.py --matiere svt        # svt
  python scripts/browse_exercises.py --filiere C          # série C seulement
  python scripts/browse_exercises.py --annee 2023         # année précise
  python scripts/browse_exercises.py --skip-skeletons     # exclure squelettes vides
  python scripts/browse_exercises.py --newton             # activer Newton (math seulement)
  python scripts/browse_exercises.py --output rapport.json  # exporter rapport JSON
  python scripts/browse_exercises.py --matiere math --newton --output rapport.json

Lancé depuis le dossier rag-service :
  cd /Users/mohameda/Documents/Bac/rag-service
  python scripts/browse_exercises.py --matiere math --skip-skeletons --newton
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

# ─── Chemins ──────────────────────────────────────────────────────────────────

ROOT = Path(__file__).resolve().parent.parent   # dossier rag-service/
DEFAULT_JSON = ROOT / "json_bac.json"

# ─── Newton API ───────────────────────────────────────────────────────────────

NEWTON_BASE = "https://newton.vercel.app/api/v2"


def newton_compute(operation: str, expression: str, timeout: float = 4.0) -> str | None:
    """Appelle Newton API et retourne le résultat, ou None si échec/erreur."""
    try:
        encoded = urllib.parse.quote(expression.strip(), safe="")
        url = f"{NEWTON_BASE}/{operation}/{encoded}"
        req = urllib.request.Request(url, headers={"User-Agent": "bac-browse/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
            result = data.get("result", "")
            # Newton signale les erreurs avec "Stop:" ou résultat vide
            if not result or result == "undefined" or "Stop:" in result:
                return None
            return result
    except Exception:
        return None


# ─── Extraction d'expressions LaTeX ───────────────────────────────────────────

_INLINE_RE  = re.compile(r"\$([^$]{2,60})\$")
_BLOCK_RE   = re.compile(r"\$\$([^$]{2,200})\$\$")
# Commandes LaTeX incompatibles avec Newton (géométrie, vecteurs, logique...)
_SKIP_RE = re.compile(
    r"\\(?:begin|end|frac|vec|sum|int|lim|partial|cdot|over|theta|alpha|beta|"
    r"gamma|delta|Gamma|Delta|pi|phi|psi|omega|Omega|lambda|mu|nu|xi|rho|"
    r"sigma|tau|epsilon|eta|kappa|zeta|chi|in|subset|cup|cap|forall|exists|"
    r"mathbb|mathcal|mathrm|text|left|right|quad|qquad|implies|iff|"
    r"overline|underline|hat|tilde|bar|dot|ddot|sqrt|cos|sin|tan)"
)
# Expression Newton-compatible : que des chars algébriques simples
_NEWTON_OK_RE = re.compile(r"^[a-zA-Z0-9\s+\-*/^().,_=<>]+$")


def extract_expressions(ennonce: str) -> list[str]:
    """Extrait les expressions LaTeX simples pouvant être soumises à Newton."""
    inline = _INLINE_RE.findall(ennonce)
    block  = _BLOCK_RE.findall(ennonce)
    candidates = []
    for expr in inline + block:
        cleaned = expr.strip()
        # Doit contenir une variable mais pas de commandes LaTeX complexes
        if (
            re.search(r"[a-zA-Z]", cleaned)
            and not _SKIP_RE.search(cleaned)
            and _NEWTON_OK_RE.match(cleaned)
            and len(cleaned) >= 3
            and len(cleaned) < 60
        ):
            candidates.append(cleaned)
    # Déduplique tout en préservant l'ordre
    seen: set[str] = set()
    result = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return result[:5]  # max 5 par exercice


def newton_validate(ennonce: str) -> dict[str, Any]:
    """Tente de valider des expressions de l'énoncé via Newton.
    Retourne {'valid': bool, 'results': [{'expr': ..., 'result': ...}]}
    """
    exprs = extract_expressions(ennonce)
    if not exprs:
        return {"valid": False, "results": [], "reason": "aucune expression extraite"}

    results = []
    for expr in exprs:
        r = newton_compute("simplify", expr)
        if r:
            results.append({"expr": expr, "result": r})
        time.sleep(0.1)  # politesse envers l'API publique

    return {
        "valid": len(results) > 0,
        "results": results,
        "reason": "" if results else "Newton n'a pas pu simplifier ces expressions",
    }


# ─── Chargement et filtrage ───────────────────────────────────────────────────

def load_exercises(
    json_path: Path,
    matiere: str | None,
    filiere: str | None,
    annee: int | None,
    skip_skeletons: bool,
) -> list[dict]:
    with open(json_path, encoding="utf-8") as f:
        data: list[dict] = json.load(f)

    if matiere:
        # "pc" regroupe aussi les anciens ids "physique" et "chimie"
        if matiere == "pc":
            data = [e for e in data if e.get("matiere_id") in ("pc", "physique", "chimie")]
        else:
            data = [e for e in data if e.get("matiere_id") == matiere]
    if filiere:
        data = [e for e in data if e.get("filiere_id") == filiere]
    if annee:
        data = [e for e in data if e.get("annee") == annee]
    if skip_skeletons:
        data = [e for e in data if not e.get("is_skeleton")]

    # Tri chronologique : année ASC, session normale avant complémentaire, exercice ASC
    _sess = {"normale": 0, "complémentaire": 1, "complementaire": 1}
    data.sort(key=lambda e: (
        e.get("annee") or 0,
        _sess.get((e.get("session") or "").lower(), 9),
        e.get("exercice_numero") or 0,
    ))
    return data


# ─── Affichage ────────────────────────────────────────────────────────────────

COLORS = {
    "reset":  "\033[0m",
    "bold":   "\033[1m",
    "dim":    "\033[2m",
    "green":  "\033[32m",
    "yellow": "\033[33m",
    "red":    "\033[31m",
    "cyan":   "\033[36m",
    "blue":   "\033[34m",
}

def c(color: str, text: str, no_color: bool = False) -> str:
    if no_color:
        return text
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


def display_exercise(
    ex: dict,
    idx: int,
    total: int,
    newton: bool,
    no_color: bool,
) -> dict:
    """Affiche un exercice et retourne son entrée rapport."""
    ennonce = (ex.get("ennonce_complet") or "").strip()
    is_skel = ex.get("is_skeleton", False)
    matiere_id = ex.get("matiere_id", "?")

    # ── En-tête ──────────────────────────────────────────────────────────────
    prefix = c("dim", f"[{idx}/{total}]", no_color)
    titre  = c("bold", ex.get("titre") or ex.get("id", "?"), no_color)
    print(f"\n{prefix} {titre}")

    # ── Métadonnées ──────────────────────────────────────────────────────────
    tags = []
    if matiere_id:
        color = {"math": "blue", "pc": "cyan", "svt": "green"}.get(matiere_id, "dim")
        tags.append(c(color, matiere_id.upper(), no_color))
    if ex.get("filiere_id"):
        tags.append(c("dim", f"Série {ex['filiere_id']}", no_color))
    if ex.get("annee"):
        tags.append(c("dim", str(ex["annee"]), no_color))
    if ex.get("session"):
        tags.append(c("dim", ex["session"], no_color))
    if tags:
        print("  " + " · ".join(tags))

    chapitres = ex.get("chapitres") or ([ex.get("chapitre")] if ex.get("chapitre") else [])
    if chapitres:
        print("  " + c("dim", "Chapitres: ", no_color) + ", ".join(chapitres))

    notions = ex.get("notions_traitees") or []
    if notions:
        preview = notions[:3]
        suffix = f" +{len(notions)-3}" if len(notions) > 3 else ""
        print("  " + c("dim", "Notions: ", no_color) + c("dim", ", ".join(preview) + suffix, no_color))

    # ── Statut énoncé + correction ──────────────────────────────────────────
    correction = (ex.get("correction") or "").strip()
    has_correction = bool(correction)

    if is_skel:
        print("  " + c("yellow", "⚠ Squelette vide (pas d'énoncé)", no_color))
    else:
        preview = ennonce[:200].replace("\n", " ")
        print("  " + c("dim", f"Énoncé ({len(ennonce)} chars): ", no_color) + preview + ("…" if len(ennonce) > 200 else ""))

    ennonce_icon = c("green", "✓ énoncé", no_color) if not is_skel else c("red", "✗ énoncé", no_color)
    correction_icon = c("green", "✓ correction", no_color) if has_correction else c("red", "✗ correction manquante", no_color)
    print("  " + ennonce_icon + "   " + correction_icon)

    validated = ex.get("validated_by_admin", False)
    if validated:
        print("  " + c("green", "✓ validé admin", no_color))

    # ── Newton (math seulement, si activé) ───────────────────────────────────
    newton_report: dict = {}
    if newton and matiere_id == "math" and ennonce:
        print("  " + c("dim", "Newton: validation...", no_color), end="\r")
        newton_report = newton_validate(ennonce)
        if newton_report["valid"]:
            for r in newton_report["results"]:
                print("  " + c("green", f"✓ Newton: {r['expr']} = {r['result']}", no_color))
        else:
            print("  " + c("dim", f"Newton: {newton_report.get('reason', 'non applicable')}", no_color))

    return {
        "id": ex.get("id"),
        "matiere_id": matiere_id,
        "filiere_id": ex.get("filiere_id"),
        "annee": ex.get("annee"),
        "session": ex.get("session"),
        "exercice_numero": ex.get("exercice_numero"),
        "is_skeleton": is_skel,
        "has_ennonce": bool(ennonce),
        "has_correction": has_correction,
        "ennonce_len": len(ennonce),
        "correction_len": len(correction),
        "validated_by_admin": validated,
        "chapitres": chapitres,
        "notions_count": len(notions),
        "newton": newton_report if newton and matiere_id == "math" else None,
    }


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parcourt les exercices du json_bac local.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--json",    default=str(DEFAULT_JSON), help="Chemin vers json_bac.json")
    parser.add_argument("--matiere", choices=["math", "pc", "svt"], help="Filtrer par matière")
    parser.add_argument("--filiere", choices=["C", "D"],            help="Filtrer par filière")
    parser.add_argument("--annee",   type=int,                      help="Filtrer par année")
    parser.add_argument("--skip-skeletons",      action="store_true", help="Exclure les squelettes vides")
    parser.add_argument("--only-missing-correction", action="store_true", help="Afficher uniquement les exercices sans correction")
    parser.add_argument("--newton",               action="store_true", help="Valider via Newton API (math uniquement)")
    parser.add_argument("--output",                                  help="Exporter le rapport en JSON")
    parser.add_argument("--no-color",       action="store_true",    help="Désactiver les couleurs ANSI")
    parser.add_argument("--limit",   type=int, default=0,           help="Limiter le nombre d'exercices affichés (0 = tous)")
    args = parser.parse_args()

    json_path = Path(args.json)
    if not json_path.exists():
        print(f"Erreur : fichier introuvable : {json_path}", file=sys.stderr)
        sys.exit(1)

    no_color = args.no_color

    # ── Chargement ───────────────────────────────────────────────────────────
    exercises = load_exercises(
        json_path,
        matiere=args.matiere,
        filiere=args.filiere,
        annee=args.annee,
        skip_skeletons=args.skip_skeletons,
    )

    if args.only_missing_correction:
        exercises = [e for e in exercises if not (e.get("correction") or "").strip()]

    total = len(exercises)
    if args.limit > 0:
        exercises = exercises[:args.limit]
        displayed = len(exercises)
    else:
        displayed = total

    # ── Résumé initial ────────────────────────────────────────────────────────
    print(c("bold", f"\n{'='*60}", no_color))
    print(c("bold", f"  json_bac — {json_path.name}", no_color))
    filtres = []
    if args.matiere:   filtres.append(f"matière={args.matiere}")
    if args.filiere:   filtres.append(f"filière={args.filiere}")
    if args.annee:     filtres.append(f"année={args.annee}")
    if args.skip_skeletons: filtres.append("sans squelettes")
    if filtres:
        print(c("dim", f"  Filtres : {', '.join(filtres)}", no_color))
    print(c("dim", f"  {total} exercices trouvés — affichage de {displayed}", no_color))
    if args.newton:
        print(c("yellow", "  Newton API activé (math uniquement)", no_color))
    print(c("bold", f"{'='*60}\n", no_color))

    # ── Parcours ──────────────────────────────────────────────────────────────
    rapport: list[dict] = []
    for i, ex in enumerate(exercises, start=1):
        entry = display_exercise(ex, i, displayed, newton=args.newton, no_color=no_color)
        rapport.append(entry)

    # ── Statistiques finales ──────────────────────────────────────────────────
    print(c("bold", f"\n{'='*60}", no_color))
    print(c("bold", "  Statistiques", no_color))
    skeletons      = sum(1 for r in rapport if r["is_skeleton"])
    with_ennonce   = sum(1 for r in rapport if r["has_ennonce"])
    with_correction = sum(1 for r in rapport if r["has_correction"])
    without_correction = with_ennonce - with_correction
    validated      = sum(1 for r in rapport if r["validated_by_admin"])
    print(f"  Exercices affichés    : {displayed}")
    print(f"  Avec énoncé           : {c('green', str(with_ennonce), no_color)}")
    print(f"  Sans énoncé (squelettes): {c('yellow', str(skeletons), no_color)}")
    print(f"  Avec correction       : {c('green', str(with_correction), no_color)}")
    print(f"  Sans correction       : {c('red', str(without_correction), no_color)}")
    print(f"  Validés admin         : {c('green', str(validated), no_color)}")

    if args.newton:
        math_entries = [r for r in rapport if r["matiere_id"] == "math" and r.get("newton")]
        newton_valid = sum(1 for r in math_entries if r["newton"] and r["newton"].get("valid"))
        print(f"  Newton valides    : {c('green', str(newton_valid), no_color)} / {len(math_entries)} math avec énoncé")

    by_matiere: dict[str, int] = {}
    for r in rapport:
        m = r["matiere_id"] or "?"
        by_matiere[m] = by_matiere.get(m, 0) + 1
    if by_matiere:
        print("  Par matière       : " + " | ".join(f"{m}={n}" for m, n in sorted(by_matiere.items())))

    print(c("bold", f"{'='*60}\n", no_color))

    # ── Export JSON ───────────────────────────────────────────────────────────
    if args.output:
        out_path = Path(args.output)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({
                "source": str(json_path),
                "filtres": {
                    "matiere": args.matiere,
                    "filiere": args.filiere,
                    "annee": args.annee,
                    "skip_skeletons": args.skip_skeletons,
                    "newton": args.newton,
                },
                "total_apres_filtre": total,
                "exercices": rapport,
            }, f, ensure_ascii=False, indent=2)
        print(c("green", f"  ✓ Rapport exporté → {out_path}", no_color))


if __name__ == "__main__":
    main()
