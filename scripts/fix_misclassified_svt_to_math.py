"""Corrige les entrées D/svt qui sont en réalité des exos de math.

Contexte : "Série Sciences de la Nature" est le nom de la filière D (au sens
du système éducatif mauritanien). J'ai confondu ce nom avec la matière SVT
(biologie) lors de l'import. Du coup beaucoup d'exos de math ont été classés
sous matiere_id='svt' par erreur.

Ce script :
  1. Identifie les entrées (filiere_id='D', matiere_id='svt') dont le contenu
     est manifestement de math (fonctions, complexes, suites, intégrales...)
  2. Pour chacune, trouve le slot D/math correspondant (même année, session,
     ex_num) et y copie l'ennonce_complet + autres champs.
  3. Vide l'entrée D/svt source (ennonce vide, is_skeleton=True,
     validated_by_admin=False).
  4. Backup automatique avant écriture.

Heuristique de détection :
  - MATH si présence de mots-clés math (complexe, dérivée, fonction, etc.)
    ET absence de mots-clés SVT (ADN, méiose, hormone, etc.)
  - SVT confirmé si présence de mots-clés biologie
  - Ambigu sinon : laissé tel quel + reporté

Usage :
    .venv/bin/python scripts/fix_misclassified_svt_to_math.py --dry-run
    .venv/bin/python scripts/fix_misclassified_svt_to_math.py
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"


_MATH_KW = re.compile(
    r"\b(complexe|polyn[oô]me|d[ée]riv[ée]|int[ée]grale|suite|barycentre|"
    r"asymptote|bijection|primitive|tangente|inflexion|r[ée]ciproque|"
    r"exponentielle|logarithme|argument|affixe|module(?!\s+de\s+(?:young|silver))|"
    r"intersection|cocyclique|sim(?:ilitude|étrie)|rotation|homoth[ée]tie|"
    r"trigonom[ée]trique|isobarycentre|trinôme|"
    r"probabilit[ée]|[ée]v[èé]nement|al[ée]atoire|esp[ée]rance|loi\s+uniforme|"
    r"loi\s+(?:binomiale|exponentielle|géométrique)|variance|"
    r"QCM|tirage|d[ée]nombrement)\b|"
    r"\$f\(x\)|\$f'\(|\\ln|\\exp|\\frac|p\(A|p_[A-Z]|P\([A-Z]|"
    r"\$u_n|\$v_n|\$w_n|\$x_n|u_\{n",
    re.IGNORECASE,
)
_PC_KW = re.compile(
    r"\b(acide|base|pH(?!o)|pKa|m[ée]canique|champ\s+(?:magn[ée]tique|[ée]lectrique)|"
    r"oscillateur|condensateur|bobine|ester|alcool|c[ée]tone|ald[ée]hyde|"
    r"r[ée]actif|cin[ée]tique|alc[èe]ne|alcane|est[ée]rification|"
    r"thiosulfate|peroxodisulfate|m[ée]thanoïque|propano(?:ate|ïque))\b",
    re.IGNORECASE,
)
_SVT_KW = re.compile(
    r"\b(ADN|chromosome|m[ée]iose|mitose|cellule|hormone|g[ée]n[ée]tique|"
    r"all[èe]le|p[ée]digr[ée]e|enzyme|prot[ée]ine|nerveuse|ovaire|spermat|"
    r"g[ée]notype|ph[ée]notype|caryotype|biopsie|fibre\s+nerveuse|neurone|"
    r"synaptique|placenta|moustique|paludisme|h[ée]r[ée]ditaire|fœtus|"
    r"endomètre|myomètre|cycle\s+sexuel|fuseau\s+neuromusculaire)\b",
    re.IGNORECASE,
)


def classify(text: str) -> str:
    """Retourne 'math', 'pc', 'svt' ou 'ambigu' selon le contenu."""
    is_math = bool(_MATH_KW.search(text))
    is_pc = bool(_PC_KW.search(text))
    is_svt = bool(_SVT_KW.search(text))
    if is_svt and not is_math:
        return "svt"
    if is_math and not is_svt:
        return "math"
    if is_pc and not is_svt and not is_math:
        return "pc"
    return "ambigu"


def find_math_slot(data: list[dict], annee, session, exercice_numero):
    """Trouve le slot D/math correspondant. Retourne None si introuvable."""
    sess_l = str(session or "").lower()
    for e in data:
        if e.get("filiere_id") != "D":
            continue
        if e.get("matiere_id") != "math":
            continue
        if e.get("annee") != annee:
            continue
        if not sess_l or sess_l[:5] not in str(e.get("session", "")).lower()[:5]:
            continue
        try:
            if int(e.get("exercice_numero")) == int(exercice_numero):
                return e
        except (TypeError, ValueError):
            continue
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))
    now = datetime.now().isoformat(timespec="seconds")

    # Toutes les D/svt avec contenu
    candidates = [e for e in data if e.get("filiere_id") == "D"
                  and e.get("matiere_id") == "svt"
                  and (e.get("ennonce_complet") or "").strip()]

    moved = []
    ambigus = []
    missing_slot = []
    real_svt = []

    for e in candidates:
        txt = e.get("ennonce_complet", "")
        cat = classify(txt)
        if cat == "svt":
            real_svt.append(e.get("id"))
            continue
        if cat == "ambigu":
            ambigus.append((e.get("id"), txt[:120]))
            continue
        # math ou pc → trouver le slot cible
        target_mat = cat
        target = None
        if cat == "math":
            target = find_math_slot(data, e.get("annee"), e.get("session"), e.get("exercice_numero"))
        # Pour pc on fait pas ici (peu d'occurrences) mais on reporte
        if target is None:
            missing_slot.append((e.get("id"), cat, e.get("annee"), e.get("session"), e.get("exercice_numero")))
            continue
        # Copie ennonce + autres champs éditables
        moved.append((e.get("id"), target.get("id"), len(txt)))
        target["ennonce_complet"] = txt
        target["correction"] = e.get("correction", "")
        target["chapitre"] = e.get("chapitre", "")
        target["notions_traitees"] = e.get("notions_traitees", [])
        target["is_skeleton"] = False
        target["updated_at"] = now
        if e.get("validated_by_admin"):
            target["validated_by_admin"] = True
        # Vide la source
        e["ennonce_complet"] = ""
        e["correction"] = ""
        e["chapitre"] = ""
        e["notions_traitees"] = []
        e["is_skeleton"] = True
        e["validated_by_admin"] = False
        e["updated_at"] = now

    # ─── Rapport ────────────────────────────────────────────────────────
    print(f"D/svt avec contenu : {len(candidates)}")
    print(f"  → Vraie SVT (gardés)     : {len(real_svt)}")
    print(f"  → Migrés vers D/math     : {len(moved)}")
    print(f"  → Ambigus (laissés)      : {len(ambigus)}")
    print(f"  → Slot D/math introuvable: {len(missing_slot)}")

    if moved:
        print("\nMigration D/svt → D/math (premiers 20) :")
        for src, tgt, ln in moved[:20]:
            print(f"  {src:45} → {tgt:45} ({ln} chars)")
        if len(moved) > 20:
            print(f"  ... + {len(moved) - 20} autres")
    if ambigus:
        print("\nAmbigus (à revoir manuellement) :")
        for eid, sample in ambigus:
            print(f"  {eid:45}  {sample}")
    if missing_slot:
        print("\nSlot D/math introuvable :")
        for eid, cat, annee, sess, ex_num in missing_slot:
            print(f"  {eid:45}  cat={cat} {annee}/{sess[:5]}/ex{ex_num}")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not moved:
        print("\nRien à migrer.")
        return 0

    # Backup défensif puis écriture
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-svt-fix-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")

    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour ({len(moved)} entrées migrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
