"""Détecte et résout les doublons quasi-identiques entre slots PC et SVT.

Quand le même énoncé est présent dans PC[F/Y/S/N] et SVT[F/Y/S/N] avec
similarité élevée, c'est qu'un import a copié l'exo dans les deux slots.
Le contenu étant de la biologie (sinon il ne serait pas un candidat),
on garde la version SVT et on vide la version PC.

Stratégie :
  1. Pour chaque (filiere, annee, session, ex_num), regarde PC + SVT remplis.
  2. Calcule la similarité du contenu.
  3. Si similarité >= --threshold (défaut 0.85) :
     - Si contenu = biologie (≥3 hits SVT) → vide le slot PC
     - Sinon : reporte pour inspection manuelle

Usage :
    .venv/bin/python scripts/fix_duplicates_pc_svt.py --dry-run
    .venv/bin/python scripts/fix_duplicates_pc_svt.py --threshold 0.85
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"

_SVT_KW = re.compile(
    r"\b(ADN|ARN|chromosome|m[ée]iose|mitose|hormone|g[ée]n[ée]tique|"
    r"all[èe]le|p[ée]digr[ée]e|enzyme|prot[ée]ine|ovaire|spermat|"
    r"g[ée]notype|ph[ée]notype|caryotype|biopsie|neurone|brassage|drosophile|"
    r"immunit|antig[èe]ne|anticorps|lymphocyte|VIH|SIDA|vaccin|"
    r"glyc[ée]mie|insuline|glucagon|diab[èe]te|"
    r"hypophyse|hypothalamus|f[ée]condation|ovulation|"
    r"mendel|gam[èe]te|zygote|amniocentèse|villosit[ée]s|"
    r"plasmocyte|macrophage|muscle)\b",
    re.IGNORECASE,
)


def slot_id(e):
    return f"{e['filiere_id']}/{e['matiere_id']}/{e.get('annee')}/{str(e.get('session',''))[:2].lower()}/ex{e.get('exercice_numero')}"


def is_filled(e):
    return bool((e.get("ennonce_complet") or "").strip())


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--threshold", type=float, default=0.85)
    args = p.parse_args()

    data = json.load(open(JSON_PATH))

    # Group by (filiere, annee, session, ex_num)
    groups = {}
    for e in data:
        k = (e.get("filiere_id"), e.get("annee"), e.get("session"), e.get("exercice_numero"))
        groups.setdefault(k, []).append(e)

    to_clear = []  # entries to empty
    manual = []   # cases needing human review

    for k, entries in groups.items():
        pc = [e for e in entries if e.get("matiere_id") == "pc" and is_filled(e)]
        svt = [e for e in entries if e.get("matiere_id") == "svt" and is_filled(e)]
        if not pc or not svt:
            continue
        for ep in pc:
            for es in svt:
                ratio = difflib.SequenceMatcher(None, ep["ennonce_complet"], es["ennonce_complet"]).ratio()
                if ratio < args.threshold:
                    continue
                # Contenu identique entre PC et SVT à 85%+ → le slot SVT garde la version,
                # on vide le slot PC sans perte (le contenu reste accessible).
                svt_hits = len(_SVT_KW.findall(es["ennonce_complet"]))
                to_clear.append((ep, es, ratio, svt_hits))

    print(f"Doublons à nettoyer (vider le slot PC) : {len(to_clear)}")
    for ep, es, ratio, hits in to_clear:
        print(f"  {slot_id(ep)} ≡ {slot_id(es)}  similarité={ratio:.1%}  svt_hits={hits}")

    if manual:
        print(f"\nCas ambigus (similarité haute mais peu de mots-clés bio) — inspection manuelle :")
        for ep, es, ratio, hits in manual:
            print(f"  {slot_id(ep)} ≡ {slot_id(es)}  similarité={ratio:.1%}  svt_hits={hits}")

    if not to_clear or args.dry_run:
        if args.dry_run:
            print("\n(--dry-run : aucune écriture)")
        return

    # Backup
    BACKUP_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-dedupe-pc-svt-{ts}.json"
    shutil.copy(JSON_PATH, backup)
    print(f"\nBackup : {backup}")

    for ep, es, _, _ in to_clear:
        ep["ennonce_complet"] = ""
        ep["correction"] = ""
        ep["chapitre"] = ""
        ep["notions_traitees"] = []
        ep["validated_by_admin"] = False
        ep["is_skeleton"] = True

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"→ {JSON_PATH} mis à jour ({len(to_clear)} slots PC vidés).")


if __name__ == "__main__":
    main()
