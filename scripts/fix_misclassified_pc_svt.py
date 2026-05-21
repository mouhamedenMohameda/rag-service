"""Corrige les mismatches PC ↔ SVT.

Détecte par mots-clés les entrées mal classées entre PC (physique-chimie) et
SVT (biologie/sciences naturelles), puis migre vers le bon slot.

Heuristique :
  - Détecté SVT : ≥3 hits SVT et hits_svt > hits_pc → matière réelle = svt
  - Détecté PC  : ≥3 hits PC  et hits_pc  > hits_svt et hits_svt ≤ 1 → matière réelle = pc

Trop conservateur ? On affiche dans le dry-run, l'utilisateur décide.

Pour chaque cas confirmé :
  1. Trouve le slot cible (même filière/année/session/exercice_numero, matière correcte)
  2. Si slot cible existe ET est vide (is_skeleton OU énoncé vide) → copie l'énoncé
  3. Si slot cible déjà rempli → SKIP avec warning (l'utilisateur tranche à la main)
  4. Vide le slot source (is_skeleton=True, ennonce/chapitre/notions vidés)

Backup automatique avant écriture.

Usage :
    .venv/bin/python scripts/fix_misclassified_pc_svt.py --dry-run
    .venv/bin/python scripts/fix_misclassified_pc_svt.py
    .venv/bin/python scripts/fix_misclassified_pc_svt.py --only-direction pc-to-svt
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"


_PC_KW = re.compile(
    r"\b(acide|base|pH(?!o)|pKa|m[ée]canique|champ\s+(?:magn[ée]tique|[ée]lectrique)|"
    r"oscillateur|condensateur|bobine|ester|alcool|c[ée]tone|ald[ée]hyde|"
    r"r[ée]actif|cin[ée]tique|alc[èe]ne|alcane|est[ée]rification|"
    r"thiosulfate|peroxodisulfate|m[ée]thano(?:ïque|ique)|propano(?:ate|ïque|ique)|"
    r"sol[ée]no[ïi]de|flux\s+magn[ée]tique|f\.e\.m|"
    r"noyau|radioactif|d[ée]sint[ée]gration|demi-vie|alpha|b[ée]ta|gamma|photon|"
    r"longueur\s+d['’]onde|fr[ée]quence(?!\s+all[ée]lique)|p[ée]riode\s+radioactive|"
    r"acc[ée]l[ée]ration|chute\s+libre|projectile|"
    r"combustion|saponification|hydrolyse|oxydation|"
    r"benz[èe]ne|chlorure|sulfate|nitrate|hydroxyde)\b",
    re.IGNORECASE,
)
_SVT_KW = re.compile(
    r"\b(ADN|ARN|chromosome|m[ée]iose|mitose|hormone|g[ée]n[ée]tique|"
    r"all[èe]le|p[ée]digr[ée]e|enzyme|prot[ée]ine|nerveuse|ovaire|spermat|"
    r"g[ée]notype|ph[ée]notype|caryotype|biopsie|fibre\s+nerveuse|neurone|"
    r"synaptique|placenta|moustique|paludisme|h[ée]r[ée]ditaire|fœtus|foetus|"
    r"endom[èe]tre|myom[èe]tre|cycle\s+sexuel|fuseau\s+neuromusculaire|"
    r"immunit|antig[èe]ne|anticorps|lymphocyte|VIH|SIDA|vaccin|"
    r"glyc[ée]mie|insuline|glucagon|diab[èe]te|pancr[ée]as|"
    r"r[ée]flexe|moelle\s+[ée]pini[èe]re|cerveau|nerf|axone|dendrite|"
    r"hypophyse|hypothalamus|thyro[ïi]de|testost[ée]rone|œstrog[èe]ne|oestrog[èe]ne|"
    r"progest[ée]rone|f[ée]condation|nidation|grossesse|ovulation|"
    r"mendel|monohybridisme|dihybridisme|gam[èe]te|zygote|brassage|drosophile|"
    r"plasmide|bact[ée]rie|virus|infection|s[ée]rum|antibiotique|"
    r"photosynth[èe]se|chlorophylle|stomate|s[èe]ve|racine|tige\s+(?!en\s+cuivre)|"
    r"respiration\s+cellulaire|mitochondrie|ATP|krebs|glycolyse|amniocentèse|"
    r"villosit[ée]s|colchicine|effectrice|globules?|h[ée]matie|leucocyte|"
    r"plasmocyte|macrophage|sarcom[èe]re|muscle|contraction\s+musculaire)\b",
    re.IGNORECASE,
)


def hits(text):
    return {
        "pc": len(_PC_KW.findall(text)),
        "svt": len(_SVT_KW.findall(text)),
    }


def slot_id(e):
    return f"{e['filiere_id']}/{e['matiere_id']}/{e.get('annee')}/{str(e.get('session',''))[:2].lower()}/ex{e.get('exercice_numero')}"


def find_target_slot(data, filiere, target_mat, annee, session, ex_num):
    for e in data:
        if e.get("filiere_id") != filiere: continue
        if e.get("matiere_id") != target_mat: continue
        if e.get("annee") != annee: continue
        if str(e.get("session","")).lower()[:2] != str(session).lower()[:2]: continue
        try:
            if int(e.get("exercice_numero")) == int(ex_num):
                return e
        except (TypeError, ValueError):
            continue
    return None


def is_empty_slot(e):
    return e.get("is_skeleton") is True or not (e.get("ennonce_complet") or "").strip()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--only-direction", choices=["pc-to-svt", "svt-to-pc"])
    args = p.parse_args()

    data = json.load(open(JSON_PATH))
    filled = [e for e in data if (e.get("ennonce_complet") or "").strip()]

    candidates = []  # (entry, current, target, hits)

    for e in filled:
        cur = e["matiere_id"]
        if cur not in ("pc", "svt"):
            continue
        h = hits(e["ennonce_complet"])
        if cur == "pc":
            # Vraiment SVT si SVT >= 3 ET SVT > PC
            if h["svt"] >= 3 and h["svt"] > h["pc"]:
                candidates.append((e, "pc", "svt", h))
        elif cur == "svt":
            # Vraiment PC si PC >= 3 ET PC > SVT (et SVT <= 1 pour éviter ambigu)
            if h["pc"] >= 3 and h["pc"] > h["svt"] and h["svt"] <= 1:
                candidates.append((e, "svt", "pc", h))

    if args.only_direction:
        wanted = tuple(args.only_direction.split("-to-"))
        candidates = [c for c in candidates if (c[1], c[2]) == wanted]

    print(f"Candidats détectés : {len(candidates)}")
    print()

    migrated = []
    skipped = []
    no_target = []

    for e, cur, tgt, h in candidates:
        target = find_target_slot(
            data, e["filiere_id"], tgt,
            e.get("annee"), e.get("session"), e.get("exercice_numero")
        )
        sid_src = slot_id(e)
        if target is None:
            no_target.append((e, cur, tgt, h))
            print(f"  ❌ {sid_src}  → {tgt}  pas de slot cible  (hits {h})")
            continue
        sid_tgt = slot_id(target)
        if not is_empty_slot(target):
            skipped.append((e, target, h))
            print(f"  ⚠️  {sid_src}  → {sid_tgt}  cible DÉJÀ remplie (collision)  (hits {h})")
            continue
        # OK on peut migrer
        migrated.append((e, target, h))
        print(f"  ✅ {sid_src}  → {sid_tgt}  (hits {h})")

    print()
    print(f"Migrations possibles : {len(migrated)}")
    print(f"Collisions (cible remplie) : {len(skipped)}")
    print(f"Pas de slot cible : {len(no_target)}")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return

    if not migrated:
        return

    # Backup
    BACKUP_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-fix-pc-svt-{ts}.json"
    shutil.copy(JSON_PATH, backup)
    print(f"\nBackup : {backup}")

    # Appliquer
    fields_to_copy = ["ennonce_complet", "correction", "chapitre", "notions_traitees",
                      "validated_by_admin"]
    for src, tgt, _ in migrated:
        for f in fields_to_copy:
            if f in src:
                tgt[f] = src[f]
        tgt["is_skeleton"] = False
        # Vider la source
        src["ennonce_complet"] = ""
        src["correction"] = ""
        src["chapitre"] = ""
        src["notions_traitees"] = []
        src["validated_by_admin"] = False
        src["is_skeleton"] = True

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"→ {JSON_PATH} mis à jour ({len(migrated)} migrations).")


if __name__ == "__main__":
    main()
