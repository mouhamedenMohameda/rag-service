#!/usr/bin/env python3
"""
apply_corrections_to_prod.py

Applique les corrections produites par verify_enonces_math_c.py
(enonces_verifies_math_C.json) dans une copie du json_bac de prod.

Sécurité :
  - écrit dans un NOUVEAU fichier (json_bac.prod.corrected.json) ;
    le fichier prod téléchargé n'est jamais modifié, sauf avec --in-place.
  - crée une sauvegarde horodatée avant toute écriture in-place.
  - ne met PAS validated_by_admin=True : tu valides toi-même dans l'UI admin.
    (option --auto-validate pour valider auto un niveau de confiance donné.)
  - écrit un rapport lisible (injection_report.md).

Champs ajoutés à chaque exo corrigé :
  ennonce_complet      → remplacé par l'énoncé corrigé
  ennonce_complet_ocr  → ancien énoncé conservé (traçabilité / rollback)
  ai_ocr_corrected     → True
  ai_ocr_confidence    → "haute" | "moyenne" | "basse"
  ai_ocr_issues        → liste {question, probleme, correction_proposee}

Usage :
  python3 apply_corrections_to_prod.py                      # toutes confiances → nouveau fichier
  python3 apply_corrections_to_prod.py --only haute         # seulement conf=haute
  python3 apply_corrections_to_prod.py --auto-validate haute # valide auto les haute
  python3 apply_corrections_to_prod.py --in-place           # écrase json_bac.prod.json (backup auto)
"""

from __future__ import annotations

import argparse
import json
import shutil
import unicodedata
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
VERIFIED = ROOT / "enonces_verifies_math_C.json"
PROD = ROOT / "json_bac.prod.json"
OUT = ROOT / "json_bac.prod.corrected.json"
REPORT = ROOT / "injection_report.md"

CONF_RANK = {"haute": 3, "moyenne": 2, "basse": 1}


def norm_sess(s: str | None) -> str | None:
    s = unicodedata.normalize("NFD", (s or "")).encode("ascii", "ignore").decode().lower().strip()
    return {
        "normale": "normale", "sn": "normale",
        "complementaire": "complementaire", "sc": "complementaire",
    }.get(s)


def prod_key(e: dict) -> tuple | None:
    try:
        return ("C", int(e["annee"]), norm_sess(e.get("session")), int(e["exercice_numero"]))
    except (KeyError, TypeError, ValueError):
        return None


def verif_key(v: dict) -> tuple | None:
    try:
        return ("C", int(v["annee"]), norm_sess(v.get("session")), int(v["numero_exercice"]))
    except (KeyError, TypeError, ValueError):
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["haute", "moyenne", "basse"], default=None,
                    help="N'appliquer que ce niveau de confiance minimum (ex: haute).")
    ap.add_argument("--auto-validate", choices=["haute", "moyenne", "basse"], default=None,
                    help="Mettre validated_by_admin=True pour ce niveau de confiance minimum.")
    ap.add_argument("--in-place", action="store_true",
                    help="Écrase json_bac.prod.json (backup horodaté auto).")
    args = ap.parse_args()

    verified = json.loads(VERIFIED.read_text(encoding="utf-8"))
    prod = json.loads(PROD.read_text(encoding="utf-8"))

    # index prod math C
    prod_idx: dict[tuple, dict] = {}
    for e in prod:
        if e.get("matiere_id") == "math" and e.get("filiere_id") == "C":
            k = prod_key(e)
            if k:
                prod_idx[k] = e

    min_rank = CONF_RANK.get(args.only, 0)
    val_rank = CONF_RANK.get(args.auto_validate, 99) if args.auto_validate else 99

    applied, skipped_conf, no_match, validated = [], [], [], []

    for vid, v in verified.items():
        if v.get("status") != "corrige":
            continue
        conf = v.get("confiance", "basse")
        if CONF_RANK.get(conf, 0) < min_rank:
            skipped_conf.append((vid, conf))
            continue
        k = verif_key(v)
        pe = prod_idx.get(k) if k else None
        if not pe:
            no_match.append(vid)
            continue

        corrected = (v.get("enonce_corrige") or "").strip()
        if not corrected:
            no_match.append(vid)
            continue

        # garde l'ancien énoncé une seule fois (pas d'écrasement si re-run)
        if "ennonce_complet_ocr" not in pe:
            pe["ennonce_complet_ocr"] = pe.get("ennonce_complet", "")
        pe["ennonce_complet"] = corrected
        pe["ai_ocr_corrected"] = True
        pe["ai_ocr_confidence"] = conf
        pe["ai_ocr_issues"] = v.get("issues") or []
        pe["updated_at"] = datetime.now().isoformat(timespec="seconds")

        if args.auto_validate and CONF_RANK.get(conf, 0) >= val_rank:
            pe["validated_by_admin"] = True
            validated.append(vid)

        applied.append((vid, pe.get("id"), conf, len(v.get("issues") or [])))

    # ── écriture ────────────────────────────────────────────────────────────
    target = PROD if args.in_place else OUT
    if args.in_place:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = PROD.with_name(f"json_bac.prod.backup_{stamp}.json")
        shutil.copy2(PROD, backup)
        print(f"🛟  Backup : {backup.name}")
    target.write_text(json.dumps(prod, ensure_ascii=False, indent=2), encoding="utf-8")

    # ── rapport ─────────────────────────────────────────────────────────────
    lines = [
        "# Rapport d'injection des corrections OCR — Math C",
        "",
        f"- Date : {datetime.now().isoformat(timespec='seconds')}",
        f"- Filtre confiance : {args.only or 'aucun (toutes)'}",
        f"- Auto-validation : {args.auto_validate or 'non'}",
        f"- Fichier écrit : `{target.name}`",
        "",
        f"## Résumé",
        f"- ✅ Corrections appliquées : **{len(applied)}**",
        f"- ⏭️  Ignorées (confiance < seuil) : {len(skipped_conf)}",
        f"- ❓ Sans correspondance prod : {len(no_match)}",
        f"- 🔒 Auto-validées : {len(validated)}",
        "",
        "## Détail des corrections appliquées",
        "",
        "| exo source | id prod | confiance | #issues |",
        "|---|---|---|---|",
    ]
    for vid, pid, conf, n in sorted(applied, key=lambda x: x[0]):
        lines.append(f"| {vid} | {pid} | {conf} | {n} |")
    if skipped_conf:
        lines += ["", "## Ignorées (confiance insuffisante)", ""]
        for vid, conf in skipped_conf:
            lines.append(f"- {vid} ({conf})")
    if no_match:
        lines += ["", "## ⚠️ Sans correspondance prod", ""]
        for vid in no_match:
            lines.append(f"- {vid}")
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(f"✅ {len(applied)} corrections appliquées → {target.name}")
    print(f"⏭️  {len(skipped_conf)} ignorées (confiance), ❓ {len(no_match)} sans match prod")
    if validated:
        print(f"🔒 {len(validated)} auto-validées (validated_by_admin=True)")
    print(f"📄 Rapport : {REPORT.name}")
    if not args.in_place:
        print()
        print("ℹ️  Fichier prod d'origine NON modifié.")
        print(f"   Pour pousser en prod : scp {target.name} root@5.189.153.144:/opt/rag-service/json_bac.json")


if __name__ == "__main__":
    main()
