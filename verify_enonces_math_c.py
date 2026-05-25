#!/usr/bin/env python3
"""
verify_enonces_math_c.py

Pour chaque exercice de math C (Bac mauritanien, 2015 → aujourd'hui) :
  1. Envoie l'énoncé à l'IA.
  2. L'IA essaie de résoudre TOUTES les questions.
  3. Si une question est insoluble (incohérence, donnée manquante, typo
     mathématique : signe inversé, exposant manquant, indice incorrect…),
     l'IA :
        - identifie la question,
        - explique l'erreur probable,
        - propose une correction minimale de l'énoncé qui rend la question
          résoluble (en restant fidèle à l'intention pédagogique).
  4. Sauvegarde un JSON structuré + checkpoints réguliers (reprise possible).

Modèle par défaut : gpt-5-mini
  → bon raisonnement mathématique, coût bas (~10× moins cher que gpt-5).
  → override : --model gpt-5  ou  --model o4-mini  ou  --model gpt-4o-mini

Usage :
  python3 verify_enonces_math_c.py                      # tout
  python3 verify_enonces_math_c.py --annee-min 2020     # 2020 → aujourd'hui
  python3 verify_enonces_math_c.py --limit 5            # test rapide
  python3 verify_enonces_math_c.py --resume             # reprend le checkpoint
  python3 verify_enonces_math_c.py --model gpt-5        # qualité max
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Any

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # facultatif : .env utile seulement si OPENAI_API_KEY n'est pas déjà exporté

from openai import OpenAI

client = OpenAI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

ROOT = Path(__file__).parent
SOURCES = [
    ROOT / "exercises_extracted" / "bac_C_math_2015_2024.json",
    ROOT / "exercises_extracted" / "bac_2025.json",
]
# Référence des énoncés déjà validés à la main par l'admin (prod).
# Si un exo y porte validated_by_admin=true, on lui fait confiance et on
# saute la vérification IA (économie de temps + d'argent).
ADMIN_REF = ROOT / "json_bac.prod.json"
OUT_PATH = ROOT / "enonces_verifies_math_C.json"
CHECKPOINT_EVERY = 1  # 1 = checkpoint après chaque exo (Ctrl+C ne perd rien)


SYSTEM_PROMPT = """Tu es un professeur agrégé de mathématiques, expert du
programme du baccalauréat mauritanien série C. Tu reçois l'énoncé d'un exercice
extrait par OCR. Ta mission :

1. RÉSOUDRE mentalement chaque question (1), 2), 3.a)… de l'exercice.
2. Détecter toute question INSOLUBLE pour cause d'erreur dans l'énoncé :
   - donnée numérique manifestement fausse (ex : Δ négatif là où on demande
     deux racines réelles distinctes),
   - signe inversé, exposant manquant, indice incorrect, parenthèse mal placée,
   - terme dupliqué (« $(1-2i)z + (1-2i)z$ » au lieu d'un seul),
   - référence à un objet jamais défini,
   - incohérence interne entre deux questions,
   - typo OCR évidente (lettre confondue, $1$ ↔ $i$, $e$ ↔ $c$, etc.).
3. Pour chaque erreur détectée, proposer une CORRECTION MINIMALE qui rend la
   question résoluble, en restant fidèle à l'intention pédagogique probable
   (cohérence avec le niveau, les autres questions, le chapitre).
4. Si l'énoncé est correct, ne rien inventer : status = "ok".

Format de sortie : JSON strict, sans markdown, sans commentaire, respectant
EXACTEMENT le schéma fourni. N'utilise PAS de backticks. Les expressions
mathématiques restent en LaTeX inline ($...$) à l'intérieur des chaînes JSON."""


SCHEMA = {
    "name": "verification_enonce",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["status", "issues", "enonce_corrige", "confiance"],
        "properties": {
            "status": {
                "type": "string",
                "enum": ["ok", "corrige", "doute"],
                "description": "ok = énoncé résoluble tel quel ; "
                               "corrige = au moins une erreur détectée et corrigée ; "
                               "doute = quelque chose semble étrange mais aucune correction sûre.",
            },
            "issues": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["question", "probleme", "correction_proposee"],
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": "Identifiant de la question (ex: '1.a)', '2)', '3.b)').",
                        },
                        "probleme": {
                            "type": "string",
                            "description": "Pourquoi la question est insoluble en l'état.",
                        },
                        "correction_proposee": {
                            "type": "string",
                            "description": "Fragment d'énoncé corrigé (court, ciblé).",
                        },
                    },
                },
            },
            "enonce_corrige": {
                "type": "string",
                "description": "L'énoncé COMPLET réécrit avec les corrections appliquées. "
                               "Vide ('') si status == 'ok'.",
            },
            "confiance": {
                "type": "string",
                "enum": ["haute", "moyenne", "basse"],
            },
        },
    },
    "strict": True,
}


def is_math_c(ex: dict) -> bool:
    md = ex.get("metadata", {})
    if md.get("matiere") != "math":
        return False
    fil = md.get("filiere") or []
    return "C" in fil


_SESSION_NORM = {
    # variantes côté prod et côté sources, mappées vers une clé canonique
    "normale": "normale",
    "sn": "normale",
    "complementaire": "complementaire",
    "complémentaire": "complementaire",
    "sc": "complementaire",
}


def _exo_key(matiere, filiere_one, annee, session, numero) -> tuple | None:
    """Clé canonique pour matcher un exo prod et un exo source."""
    if not (matiere and filiere_one and annee and session and numero):
        return None
    s = _SESSION_NORM.get((session or "").strip().lower())
    if not s:
        return None
    return (str(matiere).lower(), str(filiere_one).upper(), int(annee), s, int(numero))


def _prod_key(e: dict) -> tuple | None:
    return _exo_key(e.get("matiere_id"), e.get("filiere_id"),
                    e.get("annee"), e.get("session"), e.get("exercice_numero"))


def _src_key(e: dict) -> tuple | None:
    md = e.get("metadata") or {}
    fils = md.get("filiere") or []
    fil = fils[0] if fils else None
    return _exo_key(md.get("matiere"), fil, md.get("annee"),
                    md.get("session"), md.get("numero_exercice"))


def load_admin_validated() -> dict[tuple, dict]:
    """Index clé canonique → exo prod validé (énoncé fiable, schéma prod)."""
    if not ADMIN_REF.exists():
        log.warning("json_bac.json absent → aucune référence admin chargée.")
        return {}
    data = json.loads(ADMIN_REF.read_text(encoding="utf-8"))
    idx: dict[tuple, dict] = {}
    for e in data:
        if not e.get("validated_by_admin"):
            continue
        if e.get("matiere_id") != "math" or e.get("filiere_id") != "C":
            continue
        k = _prod_key(e)
        if k:
            idx[k] = e
    log.info("✅ %d exos Math C validés par l'admin (référence).", len(idx))
    return idx


def load_exercises(annee_min: int, annee_max: int) -> list[dict]:
    out: list[dict] = []
    seen: set[str] = set()
    for src in SOURCES:
        if not src.exists():
            log.warning("Source absente : %s", src)
            continue
        data = json.loads(src.read_text(encoding="utf-8"))
        for ex in data:
            if not is_math_c(ex):
                continue
            annee = ex.get("metadata", {}).get("annee")
            if not isinstance(annee, int):
                continue
            if annee < annee_min or annee > annee_max:
                continue
            eid = ex.get("id")
            if not eid or eid in seen:
                continue
            seen.add(eid)
            out.append(ex)
    out.sort(key=lambda e: (
        e["metadata"].get("annee", 0),
        e["metadata"].get("session", ""),
        e["metadata"].get("numero_exercice", 0),
    ))
    return out


def load_checkpoint() -> dict[str, Any]:
    if OUT_PATH.exists():
        try:
            return json.loads(OUT_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            log.warning("Checkpoint illisible, ignoré.")
    return {}


def save_checkpoint(results: dict[str, Any]) -> None:
    tmp = OUT_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(OUT_PATH)


def build_fewshot_block(source_by_key: dict[tuple, dict],
                        admin_by_key: dict[tuple, dict],
                        max_examples: int = 3) -> str:
    """Extrait jusqu'à N paires (énoncé OCR brut → énoncé validé admin)
    où les deux diffèrent vraiment. Sert d'exemples concrets pour orienter
    la détection des patterns d'erreur OCR typiques de ce corpus."""
    examples = []
    for key, admin_ex in admin_by_key.items():
        src = source_by_key.get(key)
        if not src:
            continue
        a = (src.get("enonce") or "").strip()
        b = (admin_ex.get("ennonce_complet") or "").strip()
        if not a or not b or a == b:
            continue
        if abs(len(a) - len(b)) > 400:
            continue
        label = f"Bac C {key[2]} {key[3]} ex{key[4]}"
        examples.append((label, a, b))
        if len(examples) >= max_examples:
            break
    if not examples:
        return ""
    lines = [
        "",
        "EXEMPLES réels (issus du même corpus) de corrections OCR déjà",
        "appliquées et validées par l'admin. Ils illustrent les types",
        "d'erreurs à repérer (typos numériques, exposants manquants,",
        "termes dupliqués, signes inversés…) :",
        "",
    ]
    for label, brut, corr in examples:
        lines.append(f"— {label}")
        lines.append(f"  AVANT (OCR brut) : {brut}")
        lines.append(f"  APRÈS (validé)   : {corr}")
        lines.append("")
    return "\n".join(lines)


def verify_one(ex: dict, model: str, fewshot: str = "") -> dict[str, Any]:
    md = ex["metadata"]
    user_msg = (
        f"Exercice : Bac C {md.get('annee')} session {md.get('session')} "
        f"— exercice n°{md.get('numero_exercice')}\n"
        f"Chapitres : {', '.join(md.get('chapitres') or [])}\n\n"
        f"ÉNONCÉ :\n{ex['enonce']}"
    )

    system = SYSTEM_PROMPT + (fewshot or "")
    kwargs: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_msg},
        ],
        "response_format": {"type": "json_schema", "json_schema": SCHEMA},
    }
    # Les modèles de raisonnement (o*, gpt-5*) ignorent temperature ;
    # pour les autres on fixe 0 pour la reproductibilité.
    if not (model.startswith("o") or model.startswith("gpt-5")):
        kwargs["temperature"] = 0

    # Timeout + retry exponentiel : évite les blocages indéfinis sur la connexion.
    last_err: Exception | None = None
    for attempt in range(1, 4):  # 3 tentatives max
        try:
            resp = client.with_options(timeout=180.0).chat.completions.create(**kwargs)
            break
        except Exception as e:
            last_err = e
            wait = 5 * attempt
            log.warning("  tentative %d échouée (%s) — retry dans %ds…",
                        attempt, type(e).__name__, wait)
            time.sleep(wait)
    else:
        raise last_err  # type: ignore[misc]

    content = resp.choices[0].message.content or "{}"
    parsed = json.loads(content)

    usage = resp.usage
    parsed["_meta"] = {
        "model": model,
        "tokens_in": getattr(usage, "prompt_tokens", None),
        "tokens_out": getattr(usage, "completion_tokens", None),
    }
    return parsed


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--annee-min", type=int, default=2015)
    ap.add_argument("--annee-max", type=int, default=2025)
    ap.add_argument("--model", default="gpt-5-mini",
                    help="gpt-5-mini (défaut), gpt-5, o4-mini, gpt-4o-mini…")
    ap.add_argument("--limit", type=int, default=None,
                    help="Ne traiter que les N premiers (test).")
    ap.add_argument("--resume", action="store_true",
                    help="Reprend depuis le checkpoint, saute les déjà faits.")
    ap.add_argument("--force", action="store_true",
                    help="Refait même les exos déjà traités.")
    ap.add_argument("--recheck-validated", action="store_true",
                    help="Refait la vérif IA même sur les exos validés admin "
                         "(par défaut on leur fait confiance et on les saute).")
    args = ap.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        log.error("OPENAI_API_KEY manquant (.env ou env).")
        sys.exit(1)

    admin_validated = load_admin_validated()

    exos = load_exercises(args.annee_min, args.annee_max)
    log.info("📚 %d exercices Math C entre %d et %d.",
             len(exos), args.annee_min, args.annee_max)

    source_by_key = {k: e for e in exos if (k := _src_key(e))}
    fewshot = build_fewshot_block(source_by_key, admin_validated)
    if fewshot:
        log.info("🎯 Few-shot : %d exemple(s) admin injectés dans le prompt.",
                 fewshot.count("— "))

    results: dict[str, Any] = load_checkpoint() if args.resume else {}
    if args.resume:
        log.info("⏯  Reprise : %d exos déjà dans le checkpoint.", len(results))

    if args.limit:
        exos = exos[: args.limit]

    n_done = 0
    n_corrige = 0
    n_doute = 0
    n_skipped_admin = 0
    t0 = time.time()

    for i, ex in enumerate(exos, 1):
        eid = ex["id"]
        if eid in results and not args.force:
            continue

        # Si l'admin a déjà validé cet exo en prod, on lui fait confiance.
        key = _src_key(ex)
        admin = admin_validated.get(key) if key else None
        if admin and not args.recheck_validated:
            results[eid] = {
                "id": eid,
                "prod_id": admin.get("id"),
                "annee": ex["metadata"].get("annee"),
                "session": ex["metadata"].get("session"),
                "numero_exercice": ex["metadata"].get("numero_exercice"),
                "chapitres": ex["metadata"].get("chapitres"),
                "enonce_original": ex["enonce"],
                "status": "validated_admin",
                "issues": [],
                "enonce_corrige": admin.get("ennonce_complet", ""),
                "confiance": "haute",
                "_meta": {"source": "json_bac.prod.json (validated_by_admin)"},
            }
            n_skipped_admin += 1
            log.info("[%d/%d] %s → ✅ déjà validé admin (%s), skip.",
                     i, len(exos), eid, admin.get("id"))
            continue

        try:
            log.info("[%d/%d] %s …", i, len(exos), eid)
            res = verify_one(ex, args.model, fewshot=fewshot)
        except Exception as e:
            log.error("✗ %s : %s", eid, e)
            results[eid] = {"_error": str(e), "_meta": {"model": args.model}}
            continue

        results[eid] = {
            "id": eid,
            "annee": ex["metadata"].get("annee"),
            "session": ex["metadata"].get("session"),
            "numero_exercice": ex["metadata"].get("numero_exercice"),
            "chapitres": ex["metadata"].get("chapitres"),
            "enonce_original": ex["enonce"],
            **res,
        }

        status = res.get("status")
        if status == "corrige":
            n_corrige += 1
            log.info("  ⚠️  %d issue(s) corrigée(s).", len(res.get("issues") or []))
        elif status == "doute":
            n_doute += 1
            log.info("  ❓ doute.")
        else:
            log.info("  ✓ ok.")
        n_done += 1

        if n_done % CHECKPOINT_EVERY == 0:
            save_checkpoint(results)
            log.info("💾 checkpoint (%d traités).", n_done)

    save_checkpoint(results)
    dt = time.time() - t0
    log.info("✅ Terminé. %d traités en %.1fs — corrigés: %d, doute: %d.",
             n_done, dt, n_corrige, n_doute)
    log.info("📄 Résultats : %s", OUT_PATH)


if __name__ == "__main__":
    main()
