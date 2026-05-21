#!/usr/bin/env python3
"""Canonise les notions d'un lot d'exercices : registre stable + carte inversée.

Lit ``notions_first_100.json`` (ou --input), regroupe les libellés proches
(même matière), assigne des ``notion_id`` stables, met à jour json_bac.json.

Produit :
  - notions_registry.json   { notion_id: { label, matiere_id, aliases, ... } }
  - notions_map.json        { notion_id: { label, exercices: [...] } }
  - notions_first_100.json  (libellés canoniques)
  - json_bac.json           (notion_ids + notions_traitees canoniques)

Usage :
    python scripts/canonize_notions.py
    python scripts/canonize_notions.py --threshold 0.68 --dry-run
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from collections import defaultdict
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "scripts" / "notions_first_100.json"
JSON_PATH = ROOT / "json_bac.json"
REGISTRY_PATH = ROOT / "notions_registry.json"
MAP_PATH = ROOT / "notions_map.json"
BACKUP_DIR = ROOT / "json_backups"

# Regroupements manuels (libellé canonique) pour éviter les éclatements évidents
MANUAL_CANON: dict[str, list[str]] = {
    "pc.cinetique.bilan-redox-i-peroxo": [
        r"i.?/s2o8",
        r"peroxodisulfate",
        r"oxydation des ions iodure",
        r"oxydation i",
    ],
    "pc.cinetique.vitesse-formation-i2": [
        r"vitesse.*formation.*(iode|i2|i₂)",
        r"formation du diiode",
        r"formation de l.iode",
    ],
    "pc.cinetique.vitesse-disparition": [
        r"vitesse.*disparition",
    ],
    "pc.cinetique.vitesse-graphique": [
        r"vitesse.*(instantanée|instantanee).*(calcul|lecture|graphique|courbe)",
        r"calcul de la vitesse instantanée",
        r"vitesse volumique",
    ],
    "pc.cinetique.facteurs-cinetiques": [
        r"facteur cinétique",
        r"facteurs cinétiques",
        r"température comme facteur",
        r"effet de la concentration sur la vitesse",
        r"effet de la température",
    ],
    "pc.cinetique.trempe": [
        r"trempe",
        r"refroidissement avant",
        r"arrêt de la réaction",
        r"eau glacée",
    ],
    "pc.cinetique.reactif-limitant": [
        r"réactif limitant",
        r"reactif limitant",
    ],
    "pc.cinetique.composition-t": [
        r"composition du mélange",
    ],
    "pc.cinetique.dosage-i2": [
        r"dosage.*(iode|i2|i₂)",
        r"iodométrique",
        r"thiosulfate",
        r"n\(i2\)",
    ],
    "pc.cinetique.diminution-vitesse": [
        r"diminution de la vitesse",
    ],
    "pc.acide-base.pka-demi-equiv": [
        r"pka.*demi",
        r"demi-équivalence",
        r"demi équivalence",
    ],
    "pc.acide-base.dosage-acide-faible": [
        r"dosage.*acide",
        r"dosage d.un acide faible",
    ],
    "pc.acide-base.equation-eau": [
        r"réaction.*(acide|amine).*eau",
        r"équation.*eau",
        r"acide faible monoprotique avec l.eau",
        r"acide méthanoïque / eau",
        r"acide propanoïque / eau",
        r"acide acétique / eau",
        r"acide éthanoïque / eau",
    ],
    "pc.acide-base.especes-ph": [
        r"espèces en solution",
        r"concentrations des espèces",
        r"calcul du ph",
        r"coefficient d.ionisation",
    ],
    "pc.acide-base.tampon": [
        r"solution tampon",
        r"propriétés d.une solution tampon",
        r"préparation.*tampon",
    ],
    "pc.acide-base.acide-fort-faible": [
        r"acide fort.*faible",
        r"distinction acide fort",
        r"comparaison.*hcl",
    ],
    "pc.acide-base.equiv-basique": [
        r"caractère basique.*équivalence",
        r"ph basique à l.équivalence",
        r"basique du mélange",
    ],
    "pc.orga.esterification": [
        r"estérification",
        r"esterification",
        r"équation d.estérification",
        r"limite d.estérification",
    ],
    "pc.orga.ester-hydrolyse-equilibre": [
        r"hydrolyse d.un ester",
        r"rendement.*estér",
        r"constante d.équilibre.*estér",
        r"composition.*équilibre",
    ],
    "pc.orga.anhydride-amine": [
        r"anhydride.*amine",
        r"acylation",
        r"avantages de l.anhydride",
    ],
    "pc.orga.amine-formule-isomeres": [
        r"formule brute.*amine",
        r"isomères.*amine",
        r"%.*azote",
    ],
    "pc.orga.alcool-isomeres-oxydation": [
        r"isomères.*alcool",
        r"oxydation ménagée",
        r"dnph",
        r"fehling",
        r"schiff",
    ],
    "pc.electroaimantisme.solenoide-flux": [
        r"solénoïde",
        r"flux magnétique.*bobine",
    ],
    "pc.electroaimantisme.circuit-rl": [
        r"circuit rl",
        r"équation différentielle.*intensité",
        r"constante de temps",
        r"énergie magnétique",
    ],
    "pc.meca.ressort-harmonique": [
        r"équation différentielle du mouvement harmonique",
        r"équation horaire",
        r"oscillations harmoniques",
        r"mouvement harmonique",
        r"ressort.*raideur",
    ],
    "pc.meca.projectile": [
        r"portée du tir",
        r"flèche",
        r"projectile",
        r"équation cartésienne de la trajectoire",
        r"chute libre après détachement",
    ],
    "pc.meca.rayon-trajetoire-b": [
        r"rayon de trajectoire",
        r"rayon r=mv",
        r"séparation d.isotopes",
        r"spectrographie",
    ],
    "pc.meca.champ-b-mcu": [
        r"mouvement circulaire uniforme.*charge",
        r"force magnétique",
        r"cyclotron",
        r"déviation circulaire",
    ],
    "pc.optique.young": [
        r"young",
        r"interfrange",
        r"franges d.interférence",
    ],
    "pc.ondes.progressive": [
        r"longueur d.onde",
        r"équation d.onde",
        r"onde progressive",
    ],
    "pc.radioactivite.desintegration": [
        r"désintégration",
        r"desintegration",
        r"demi-vie",
        r"constante radioactive",
        r"activité initiale",
        r"activité après",
    ],
    "pc.radioactivite.noyaux": [
        r"nombre de noyaux",
    ],
    "pc.gravitation.satellite": [
        r"satellite",
        r"kepler",
        r"gravitation",
        r"masse de la terre",
    ],
    "pc.spectro.acceleration-ions": [
        r"accélération d.ion",
        r"vitesse.*ion.*potentiel",
        r"spectrographie",
    ],
    "math.complexe.similitude": [
        r"similitude directe",
        r"affixe",
        r"plan complexe",
    ],
    "math.geo.transformations": [
        r"rotation",
        r"réflexion",
        r"composition.*réflexion",
    ],
    "math.analyse.edo-second-ordre": [
        r"équation différentielle.*second ordre",
        r"y''",
    ],
    "math.analyse.integrales-un": [
        r"intégrale u_n",
        r"intégration par parties",
    ],
    "math.analyse.fonction-ln-quotient": [
        r"ln\|",
        r"1/ln",
        r"homothétie",
        r"ln x",
        r"ln\(1/x\)",
        r"ln\|x/\(x-1\)\|",
    ],
    "math.complexe.equation-second-degre-param": [
        r"équation.*z",
        r"résoudre.*e\)",
        r"affixes z_1",
        r"affixe z",
    ],
    "math.complexe.lieu-ellipse-affixes": [
        r"ellipse",
        r"lieu.*gamma",
        r"excentricité",
        r"sommets",
    ],
    "math.complexe.application-affine-affixe": [
        r"z'=",
        r"affixe.*barre",
        r"image de.*gamma",
        r"3z-",
    ],
    "math.geo.similitude-directe": [
        r"similitude directe",
        r"rapport et angle",
        r"centre de s",
    ],
    "math.geo.rotation": [
        r"rotation.*centre",
        r"angle de r",
        r"unique rotation",
    ],
    "math.analyse.integrale-fonction-ln": [
        r"intégrale.*ln",
        r"g_n.*intégrale",
        r"f\(x\)=1/ln",
        r"1/ln x",
    ],
    "math.analyse.suite-integrales-encadrement": [
        r"u_n=.*intégrale",
        r"encadrement.*u_n",
        r"limite.*u_n",
    ],
    "math.analyse.sommes-riemann": [
        r"somme.*f\(k/n\)",
        r"encadrement.*s_n",
        r"riemann",
    ],
    "math.analyse.developpement-ln": [
        r"ln\(1\+x\)",
        r"développement.*ln",
        r"s_n\(x\)",
    ],
    "math.analyse.suite-harmonique-euler": [
        r"constante d'euler",
        r"s_n=.*somme",
        r"u_n.*ln n",
    ],
    "math.geo.orthocentre-cercles": [
        r"orthocentre",
        r"cercles.*diamètre",
    ],
    "math.geo.lieux-ensembles-points": [
        r"lieu.*points m",
        r"ensemble.*gamma",
        r"gamma_k",
        r"lieu géométrique",
    ],
    "math.geo.geometrie-espace": [
        r"tétraèdre",
        r"équation du plan",
        r"produit scalaire.*espace",
        r"volume du tétraèdre",
    ],
    "svt.genetique.pedigree": [
        r"pédigrée",
        r"pedigree",
        r"récessive vs dominante",
    ],
    "svt.genetique.caryotype-meiose": [
        r"caryotype",
        r"méiose",
        r"génotype",
    ],
}


def slugify(text: str, max_len: int = 48) -> str:
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t[:max_len] or "notion"


def normalize(text: str) -> str:
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def tokens(text: str) -> set[str]:
    stop = {
        "de", "du", "des", "la", "le", "les", "un", "une", "et", "en", "par",
        "pour", "sur", "dans", "a", "au", "aux", "ou", "son", "sa", "ses",
        "donne", "donner", "calculer", "montrer", "etablir", "preciser",
    }
    return {w for w in normalize(text).split() if len(w) > 2 and w not in stop}


def similarity(a: str, b: str) -> float:
    na, nb = normalize(a), normalize(b)
    if na == nb:
        return 1.0
    seq = SequenceMatcher(None, na, nb).ratio()
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return seq
    jacc = len(ta & tb) / len(ta | tb)
    return 0.45 * seq + 0.55 * jacc


def manual_cluster_id(label: str) -> str | None:
    n = normalize(label)
    for nid, patterns in MANUAL_CANON.items():
        for pat in patterns:
            if re.search(pat, n):
                return nid
    return None


def matiere_from_ex_id(ex_id: str, ex_meta: dict | None) -> str:
    if ex_meta:
        return ex_meta.get("matiere_id") or "pc"
    if ex_id.startswith("bac-") or "math" in ex_id:
        return "math"
    if ex_id.startswith("svt-"):
        return "svt"
    if ex_id.startswith("physique-"):
        return "pc"
    return "pc"


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
            self.p[rb] = ra


def pick_canonical_label(labels: list[str], notion_id: str = "") -> str:
    """Libellé représentatif : préfère les formulations générales (sans formule longue)."""
    counts: dict[str, int] = defaultdict(int)
    for lb in labels:
        counts[lb] += 1
    best_freq = max(counts.values())
    candidates = [lb for lb, c in counts.items() if c == best_freq]

    def score(lb: str) -> tuple:
        n = normalize(lb)
        # pénalise formules, rendements spécifiques, noms propres d'espèces
        penalty = 0
        if re.search(r"[=+\-*/^]|v\(t\)|n\(|%", lb):
            penalty += 3
        if re.search(r"rendement|méthanoïque|propanoïque|acétique|benzoïque", n):
            penalty += 2
        if "test " in n and " — " in lb:
            penalty += 1
        return (penalty, len(lb))

    return min(candidates, key=score)


def cluster_labels(
    items: list[tuple[str, str, str]],
    threshold: float,
) -> dict[str, str]:
    """items: (label, ex_id, matiere_id) -> label -> notion_id"""
    # Pré-assignation manuelle
    label_to_nid: dict[str, str] = {}
    for label, _ex, mat in items:
        mid = manual_cluster_id(label)
        if mid:
            label_to_nid[label] = mid

    # Index des labels restants par matière
    by_mat: dict[str, list[int]] = defaultdict(list)
    all_labels = [it[0] for it in items]
    for i, (_, _, mat) in enumerate(items):
        if all_labels[i] not in label_to_nid:
            by_mat[mat].append(i)

    for mat, indices in by_mat.items():
        uf = UnionFind(len(indices))
        for a in range(len(indices)):
            for b in range(a + 1, len(indices)):
                i, j = indices[a], indices[b]
                la, lb = items[i][0], items[j][0]
                if la in label_to_nid or lb in label_to_nid:
                    # fusion si même manual id déjà assigné à l'un
                    ida = label_to_nid.get(la) or manual_cluster_id(la)
                    idb = label_to_nid.get(lb) or manual_cluster_id(lb)
                    if ida and idb and ida == idb:
                        uf.union(a, b)
                    continue
                if similarity(la, lb) >= threshold:
                    uf.union(a, b)

        groups: dict[int, list[int]] = defaultdict(list)
        for local_i, global_i in enumerate(indices):
            root = uf.find(local_i)
            groups[root].append(global_i)

        used_slugs: set[str] = set()
        for _root, group_idxs in groups.items():
            group_labels = [items[i][0] for i in group_idxs]
            # Si déjà des manual ids dans le groupe, fusionner sous le premier
            manual_ids = {label_to_nid.get(lb) or manual_cluster_id(lb)
                          for lb in group_labels}
            manual_ids.discard(None)
            if manual_ids:
                nid = sorted(manual_ids)[0]
            else:
                canon = pick_canonical_label(group_labels)
                base = f"{mat}.{slugify(canon)}"
                nid = base
                n = 2
                while nid in used_slugs:
                    nid = f"{base}-{n}"
                    n += 1
            used_slugs.add(nid)
            for i in group_idxs:
                label_to_nid[items[i][0]] = nid

    return label_to_nid


FIXED_LABELS: dict[str, str] = {
    "pc.orga.esterification": "Estérification — équation, suivi et équilibre",
    "pc.cinetique.bilan-redox-i-peroxo": "Bilan redox I⁻ / S₂O₈²⁻ (peroxodisulfate)",
    "pc.cinetique.vitesse-formation-i2": "Vitesse instantanée de formation du diiode",
    "pc.meca.projectile": "Mouvement de projectile — trajectoire, portée et flèche",
    "pc.meca.rayon-trajetoire-b": "Rayon de trajectoire d'un ion dans un champ B",
    "pc.orga.anhydride-amine": "Réaction anhydride d'acide + amine (amide)",
    "pc.acide-base.pka-demi-equiv": "pKa à la demi-équivalence",
    "pc.acide-base.tampon": "Solution tampon — propriétés et préparation",
    "math.complexe.similitude": "Similitude directe dans le plan complexe — rapport et centre",
    "math.analyse.integrales-un": "Suite d'intégrales U_n — intégration par parties",
    "math.analyse.fonction-ln-quotient": "Fonction ln|x/(x-1)| et familles de courbes",
    "math.complexe.lieu-ellipse-affixes": "Lieu géométrique — ellipse à partir d'affixes",
    "math.geo.similitude-directe": "Similitude directe — angle, rapport et centre",
    "math.geo.rotation": "Rotation — centre et angle",
}


def build_label_index(registry: dict[str, dict]) -> dict[str, str]:
    """label ou alias → notion_id."""
    idx: dict[str, str] = {}
    for nid, reg in registry.items():
        idx[reg["label"]] = nid
        for a in reg.get("aliases") or []:
            idx[a] = nid
    return idx


def match_existing(
    label: str,
    mat: str,
    index: dict[str, str],
    registry: dict[str, dict],
    threshold: float,
) -> str | None:
    if label in index:
        return index[label]
    manual = manual_cluster_id(label)
    if manual and manual in registry:
        return manual
    best_nid, best_sc = None, threshold
    for nid, reg in registry.items():
        if reg.get("matiere_id") != mat:
            continue
        sc = similarity(label, reg["label"])
        for a in reg.get("aliases") or []:
            sc = max(sc, similarity(label, a))
        if sc >= best_sc:
            best_sc, best_nid = sc, nid
    return best_nid


def cluster_labels_merge(
    items: list[tuple[str, str, str]],
    threshold: float,
    registry: dict[str, dict],
) -> dict[str, str]:
    """Associe chaque libellé à un notion_id (existant ou nouveau)."""
    index = build_label_index(registry)
    label_to_nid: dict[str, str] = {}
    pending: list[tuple[str, str, str]] = []

    for label, ex_id, mat in items:
        nid = match_existing(label, mat, index, registry, threshold)
        if nid:
            label_to_nid[label] = nid
            if label not in index:
                registry[nid].setdefault("aliases", [])
                if label != registry[nid]["label"] and label not in registry[nid]["aliases"]:
                    registry[nid]["aliases"].append(label)
                index[label] = nid
        else:
            pending.append((label, ex_id, mat))

    if pending:
        new_map = cluster_labels(pending, threshold)
        for label, nid in new_map.items():
            label_to_nid[label] = nid
            if nid not in registry:
                labels_grp = [lb for lb, _, _ in pending if new_map.get(lb) == nid]
                canon = pick_canonical_label(labels_grp, nid)
                if nid in FIXED_LABELS:
                    canon = FIXED_LABELS[nid]
                mat = nid.split(".")[0] if "." in nid else pending[0][2]
                registry[nid] = {
                    "label": canon,
                    "matiere_id": mat if mat in ("math", "svt", "pc") else "pc",
                    "aliases": sorted(set(labels_grp) - {canon}),
                }
                index[canon] = nid
                for a in registry[nid]["aliases"]:
                    index[a] = nid
            else:
                if label != registry[nid]["label"] and label not in registry[nid]["aliases"]:
                    registry[nid]["aliases"].append(label)
                index[label] = nid
    return label_to_nid


def ex_entry(meta: dict) -> dict:
    return {
        "id": meta.get("id"),
        "annee": meta.get("annee"),
        "filiere_id": meta.get("filiere_id"),
        "session": meta.get("session"),
        "matiere_id": meta.get("matiere_id"),
        "exercice_numero": meta.get("exercice_numero"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default=str(DEFAULT_INPUT))
    ap.add_argument("--threshold", type=float, default=0.62)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--merge-registry", action="store_true",
                    help="Fusionne avec notions_registry.json existant")
    ap.add_argument("--by-input-ids", action="store_true",
                    help="Met à jour tous les exos dont l'id est dans --input (ignore offset/limit)")
    args = ap.parse_args()

    notions_by_ex: dict[str, list[str]] = json.loads(
        Path(args.input).read_text(encoding="utf-8")
    )
    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    if args.by_input_ids:
        id_set = set(notions_by_ex.keys())
        slice_data = [e for e in data if e.get("id") in id_set]
    else:
        slice_data = data[args.offset: args.offset + args.limit]
    ex_by_id = {e["id"]: e for e in data}

    items: list[tuple[str, str, str]] = []
    for ex_id, labels in notions_by_ex.items():
        meta = ex_by_id.get(ex_id, {})
        mat = matiere_from_ex_id(ex_id, meta)
        for lb in labels:
            items.append((lb, ex_id, mat))

    if args.merge_registry and REGISTRY_PATH.exists():
        registry: dict[str, dict] = json.loads(
            REGISTRY_PATH.read_text(encoding="utf-8")
        )
        label_to_nid = cluster_labels_merge(items, args.threshold, registry)
    else:
        registry = {}
        label_to_nid = cluster_labels(items, args.threshold)
        aliases_map: dict[str, set[str]] = defaultdict(set)
        for label, nid in label_to_nid.items():
            aliases_map[nid].add(label)
        for nid, aliases in aliases_map.items():
            labels = sorted(aliases, key=len)
            canon = pick_canonical_label(labels, nid)
            if nid in FIXED_LABELS:
                canon = FIXED_LABELS[nid]
            mat = nid.split(".")[0] if "." in nid else "pc"
            registry[nid] = {
                "label": canon,
                "matiere_id": mat if mat in ("math", "svt", "pc") else "pc",
                "aliases": sorted(set(labels) - {canon}),
            }

    if args.merge_registry and MAP_PATH.exists():
        notions_map: dict[str, dict] = json.loads(
            MAP_PATH.read_text(encoding="utf-8")
        )
    else:
        notions_map = {}
    for nid, reg in registry.items():
        notions_map.setdefault(nid, {
            "label": reg["label"],
            "matiere_id": reg["matiere_id"],
            "exercices": [],
        })

    updated_ex: dict[str, list[str]] = {}
    batch_ex_ids = set()
    for ex_id, labels in notions_by_ex.items():
        canon_labels: list[str] = []
        seen: set[str] = set()
        for lb in labels:
            nid = label_to_nid.get(lb)
            if not nid or nid in seen:
                continue
            seen.add(nid)
            canon_labels.append(registry[nid]["label"])
            meta = ex_by_id.get(ex_id)
            if meta:
                batch_ex_ids.add(ex_id)
                entry = ex_entry(meta)
                existing = notions_map[nid]["exercices"]
                if not any(x.get("id") == ex_id for x in existing):
                    existing.append(entry)
        updated_ex[ex_id] = canon_labels

    total_aliases = sum(len(r.get("aliases") or []) for r in registry.values())
    reused = sum(1 for nid in notions_map if len(notions_map[nid]["exercices"]) > 1)
    new_in_registry = sum(1 for nid in registry if nid.startswith("math."))
    print(f"Lot offset={args.offset} limit={args.limit} · exos avec notions: {len(updated_ex)}")
    print(f"Libellés sources : {len(label_to_nid)}")
    print(f"Notions dans le registre : {len(registry)}")
    print(f"Aliases fusionnés : {total_aliases}")
    print(f"Notions utilisées par ≥2 exos (map) : {reused}")

    if args.dry_run:
        print("\n(--dry-run)")
        top = sorted(notions_map.items(),
                     key=lambda x: -len(x[1]["exercices"]))[:12]
        for nid, m in top:
            print(f"  [{len(m['exercices'])}] {nid}: {m['label'][:60]}")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(JSON_PATH, BACKUP_DIR / f"json_bac-pre-canon-{stamp}.json")

    REGISTRY_PATH.write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    MAP_PATH.write_text(
        json.dumps(notions_map, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    Path(args.input).write_text(
        json.dumps(updated_ex, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for e in slice_data:
        eid = e["id"]
        if eid in updated_ex:
            seen_ids: set[str] = set()
            unique_ids: list[str] = []
            for lb in notions_by_ex.get(eid, []):
                nid = label_to_nid.get(lb)
                if nid and nid not in seen_ids:
                    seen_ids.add(nid)
                    unique_ids.append(nid)
            e["notion_ids"] = unique_ids
            e["notions_traitees"] = updated_ex[eid]
            e["updated_at"] = datetime.now().isoformat(timespec="seconds")

    JSON_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"\nÉcrit : {REGISTRY_PATH}")
    print(f"Écrit : {MAP_PATH}")
    if args.by_input_ids:
        print(f"Mis à jour : {JSON_PATH} [{len(slice_data)} exos par id]")
    else:
        print(f"Mis à jour : {JSON_PATH} [exos {args.offset+1}–{args.offset+args.limit}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
