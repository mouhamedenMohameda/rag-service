"""Audit de classification : détecte les énoncés rangés dans la mauvaise matière.

Réutilise les heuristiques mots-clés de fix_misclassified_svt_to_math.py
et les applique à TOUS les énoncés remplis (pas seulement D/svt).

Aucune écriture — diagnostic uniquement.

Usage :
    .venv/bin/python scripts/audit_classification.py
    .venv/bin/python scripts/audit_classification.py --show-ambigus
    .venv/bin/python scripts/audit_classification.py --matiere svt
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"

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
    r"thiosulfate|peroxodisulfate|m[ée]thano(?:ïque|ique)|propano(?:ate|ïque|ique)|"
    r"r[ée]sistance|tension|intensit[ée]|condensat|noyau|radioactif|"
    r"d[ée]sint[ée]gration|demi-vie|alpha|b[ée]ta|gamma|photon|onde|"
    r"longueur\s+d['’]onde|fr[ée]quence|p[ée]riode|spectre|"
    r"v[ée]locit[ée]|acc[ée]l[ée]ration|cinem|chute\s+libre|projectile|"
    r"masse\s+volumique|densit[ée]|pression|temperature|chaleur|"
    r"combustion|saponification|hydrolyse|oxydation|r[ée]duction|"
    r"[ée]lectrolyse|pile|[ée]lectrode|cathode|anode|"
    r"benz[èe]ne|m[ée]thane|[ée]thane|propane|butane|"
    r"chlorure|sulfate|nitrate|carbonate|hydroxyde)\b",
    re.IGNORECASE,
)
_SVT_KW = re.compile(
    r"\b(ADN|ARN|chromosome|m[ée]iose|mitose|cellule|hormone|g[ée]n[ée]tique|"
    r"all[èe]le|p[ée]digr[ée]e|enzyme|prot[ée]ine|nerveuse|ovaire|spermat|"
    r"g[ée]notype|ph[ée]notype|caryotype|biopsie|fibre\s+nerveuse|neurone|"
    r"synaptique|placenta|moustique|paludisme|h[ée]r[ée]ditaire|fœtus|"
    r"endom[èe]tre|myom[èe]tre|cycle\s+sexuel|fuseau\s+neuromusculaire|"
    r"immunit|antig[èe]ne|anticorps|lymphocyte|VIH|SIDA|vaccin|"
    r"glyc[ée]mie|insuline|glucagon|diab[èe]te|pancr[ée]as|"
    r"r[ée]flexe|moelle\s+[ée]pini[èe]re|cerveau|nerf|axone|dendrite|"
    r"hypophyse|hypothalamus|thyro[ïi]de|testost[ée]rone|œstrog[èe]ne|"
    r"progest[ée]rone|f[ée]condation|nidation|grossesse|ovulation|"
    r"mendel|monohybridisme|dihybridisme|gam[èe]te|zygote|"
    r"plasmide|bact[ée]rie|virus|infection|s[ée]rum|antibiotique|"
    r"photosynth[èe]se|chlorophylle|stomate|s[èe]ve|racine|tige|feuille|"
    r"respiration\s+cellulaire|mitochondrie|ATP|krebs|glycolyse)\b",
    re.IGNORECASE,
)


def classify(text: str) -> tuple[str, dict]:
    """Retourne (label, hits) où label ∈ {math, pc, svt, ambigu, vide}."""
    if not text or not text.strip():
        return "vide", {}
    math_hits = _MATH_KW.findall(text)
    pc_hits = _PC_KW.findall(text)
    svt_hits = _SVT_KW.findall(text)
    hits = {"math": len(math_hits), "pc": len(pc_hits), "svt": len(svt_hits)}

    # Règles de décision : la matière dominante l'emporte, sauf signaux croisés forts.
    is_math = hits["math"] > 0
    is_pc = hits["pc"] > 0
    is_svt = hits["svt"] > 0

    # SVT prioritaire si présent ET autres absents ou faibles
    if is_svt and hits["svt"] >= max(hits["math"], hits["pc"]):
        # Vérif : si on a 5+ termes math, c'est suspect
        if hits["math"] >= 5 and hits["svt"] < hits["math"]:
            return "ambigu", hits
        return "svt", hits
    if is_math and hits["math"] > max(hits["pc"], hits["svt"]):
        return "math", hits
    if is_pc and hits["pc"] > max(hits["math"], hits["svt"]):
        return "pc", hits
    if is_math or is_pc or is_svt:
        return "ambigu", hits
    return "ambigu", hits


def slot_id(e):
    return f"{e['filiere_id']}/{e['matiere_id']}/{e.get('annee')}/{str(e.get('session','')).lower()[:2]}/ex{e.get('exercice_numero')}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--matiere", help="Filtre sur une matière (math/pc/svt)")
    p.add_argument("--show-ambigus", action="store_true", help="Liste les ambigus aussi")
    p.add_argument("--show-snippets", action="store_true", help="Affiche un extrait pour chaque mismatch")
    args = p.parse_args()

    data = json.load(open(JSON_PATH))
    filled = [e for e in data if (e.get("ennonce_complet") or "").strip()]
    print(f"Total énoncés remplis : {len(filled)}\n")

    mismatches = defaultdict(list)  # (stored, detected) -> list of entries
    ambigus = []
    matches = Counter()

    for e in filled:
        if args.matiere and e["matiere_id"] != args.matiere:
            continue
        text = e["ennonce_complet"]
        detected, hits = classify(text)
        stored = e["matiere_id"]
        if detected == "vide":
            continue
        if detected == "ambigu":
            ambigus.append((e, hits))
            continue
        if detected == stored:
            matches[stored] += 1
        else:
            mismatches[(stored, detected)].append((e, hits))

    print("=" * 70)
    print("CORRECTEMENT CLASSÉS (matière stockée == détectée)")
    print("=" * 70)
    for k, v in sorted(matches.items()):
        print(f"  {k}: {v}")

    print(f"\n{'='*70}")
    print(f"MISMATCHES — {sum(len(v) for v in mismatches.values())} cas")
    print("=" * 70)
    for (stored, detected), items in sorted(mismatches.items()):
        print(f"\n⚠️  Stocké comme [{stored}] mais détecté [{detected}] — {len(items)} cas")
        for e, hits in items[:20]:
            print(f"    {slot_id(e)}   hits={hits}")
            if args.show_snippets:
                snippet = e["ennonce_complet"][:200].replace("\n", " ")
                print(f"      → {snippet}...")
        if len(items) > 20:
            print(f"    ... ({len(items)-20} de plus)")

    print(f"\n{'='*70}")
    print(f"AMBIGUS — {len(ambigus)} cas")
    print("=" * 70)
    if args.show_ambigus:
        for e, hits in ambigus[:30]:
            print(f"  {slot_id(e)}   hits={hits}")
            if args.show_snippets:
                snippet = e["ennonce_complet"][:200].replace("\n", " ")
                print(f"    → {snippet}...")
        if len(ambigus) > 30:
            print(f"  ... ({len(ambigus)-30} de plus, --show-ambigus pour la suite)")
    else:
        print("(--show-ambigus pour les détails)")

    print(f"\n{'='*70}")
    print("RÉSUMÉ")
    print("=" * 70)
    total = sum(matches.values()) + sum(len(v) for v in mismatches.values()) + len(ambigus)
    print(f"  Match           : {sum(matches.values())} ({100*sum(matches.values())/max(total,1):.1f}%)")
    print(f"  Mismatch        : {sum(len(v) for v in mismatches.values())} ({100*sum(len(v) for v in mismatches.values())/max(total,1):.1f}%)")
    print(f"  Ambigu          : {len(ambigus)} ({100*len(ambigus)/max(total,1):.1f}%)")


if __name__ == "__main__":
    main()
