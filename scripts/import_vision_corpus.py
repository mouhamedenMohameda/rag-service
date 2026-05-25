#!/usr/bin/env python3
"""
Importe les 3 JSONs vision-extracted (bac_math.json, bac_pc.json, bac_svt.json)
dans json_bac.json :
  1. Backup automatique de json_bac.json
  2. Supprime tous les exos d'annee >= 2015 (672 exos)
  3. Convertit les 416 nouveaux exos au schéma json_bac.json (split C+D)
  4. Append + sauvegarde

Usage :
  python3 scripts/import_vision_corpus.py --dry-run    # voir le diff sans toucher
  python3 scripts/import_vision_corpus.py              # appliquer
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BAC_EXPORTS = ROOT.parent / "bac_exports"
JSON_BAC = ROOT / "json_bac.json"

NEW_SOURCES = {
    "math": BAC_EXPORTS / "bac_math.json",
    "pc": BAC_EXPORTS / "bac_pc.json",
    "svt": BAC_EXPORTS / "bac_svt.json",
}

CUTOFF_YEAR = 2015  # tout exo d'annee >= cutoff sera remplacé

MATIERE_LABEL = {
    "math": "Mathématiques",
    "pc": "Sciences Physiques",
    "svt": "Sciences Naturelles",
}
SESSION_LABEL = {"normale": "Normale", "complementaire": "Complémentaire"}
SESSION_CODE = {"normale": "sn", "complementaire": "sc"}
FILIERE_LABEL = {"C": "Série C", "D": "Série D"}


def render_enonce_markdown(structure: dict[str, Any], flat_fallback: str = "") -> str:
    """Rend l'arbre {preambule, questions:[]} en texte numéroté lisible.

    Format :
      <preambule>

      1) <question 1>
        a) <sous-question a>
        b) <sous-question b>
      2) <question 2>
        ...
    """
    if not structure or not structure.get("questions"):
        # Pas de structure détectée → fallback sur l'enonce plat
        return flat_fallback.strip()

    lines: list[str] = []
    preambule = (structure.get("preambule") or "").strip()
    if preambule:
        lines.append(preambule)
        lines.append("")

    def render_node(node: dict[str, Any], depth: int = 0) -> None:
        marker_open = ["1)", "a)", "i)"][depth] if depth < 3 else f"{node['numero']})"
        # Utilise le numero réel (préserve "3" ou "b")
        marker = f"{node['numero']})"
        indent = "  " * depth
        enonce = (node.get("enonce") or "").strip()
        if enonce:
            lines.append(f"{indent}{marker} {enonce}")
        else:
            lines.append(f"{indent}{marker}")
        for sub in node.get("sous_questions") or []:
            render_node(sub, depth + 1)

    for i, q in enumerate(structure["questions"]):
        if i > 0:
            lines.append("")
        render_node(q, 0)

    return "\n".join(lines).strip()


def matiere_id_for(matiere: str) -> str:
    """Notre 'physique'/'chimie' → 'pc' (Sciences Physiques regroupe les deux)."""
    if matiere in ("physique", "chimie"):
        return "pc"
    return matiere  # math, svt


def build_id(matiere_id: str, filiere: str, annee: int, session: str, ex_num: int) -> str:
    """bac-c-2024-sn-math-ex1 (convention existante)."""
    sess = SESSION_CODE.get(session, session)
    fil = filiere.lower()
    return f"bac-{fil}-{annee}-{sess}-{matiere_id}-ex{ex_num}"


def convert_one(ex: dict[str, Any], filiere: str) -> dict[str, Any]:
    """Convertit un exo vision-extracted vers le schéma json_bac.json pour UNE filière."""
    meta = ex["metadata"]
    matiere_raw = meta.get("matiere", "")
    matiere_id = matiere_id_for(matiere_raw)
    annee = meta.get("annee")
    session = meta.get("session", "normale")
    ex_num = meta.get("numero_exercice", 0)

    enonce_complet = render_enonce_markdown(
        ex.get("enonce_structure") or {}, ex.get("enonce") or ""
    )
    correction_complet = render_enonce_markdown(
        ex.get("correction_structure") or {}, ex.get("correction") or ""
    )

    return {
        "id": build_id(matiere_id, filiere, annee, session, ex_num),
        "matiere_id": matiere_id,
        "filiere_id": filiere,
        "fichier": meta.get("source_sujet", ""),
        "exercice_numero": ex_num,
        "matiere": MATIERE_LABEL.get(matiere_id, matiere_raw),
        "annee": annee,
        "session": SESSION_LABEL.get(session, session),
        "filiere": FILIERE_LABEL.get(filiere, filiere),
        "chapitre": (meta.get("chapitres") or [""])[0],
        "chapitres": meta.get("chapitres") or [],
        "notions_traitees": meta.get("notions_traitees") or [],
        "donnees_fournies": {},
        "ennonce_complet": enonce_complet,
        "correction": correction_complet or "",
        "bareme": meta.get("bareme"),
        # Champs nouveaux : préservent la structure pour le RAG et l'UI future
        "enonce_structure": ex.get("enonce_structure"),
        "correction_structure": ex.get("correction_structure"),
        "source_extraction": "vision",  # marqueur d'origine
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "notion_ids": [],  # rempli plus tard par canonize_notions.py
        "validated_by_admin": False,
    }


FILIERE_FROM_FILENAME = re.compile(r"bac[\s_]*([cd])\b|sujet[\s_]*bac[\s_]*([cd])\b", re.I)


def filiere_from_source(source: str, fallback: list[str]) -> list[str]:
    """Dérive la filière du nom de fichier (plus fiable que le champ meta).
    'Bac C 2016 MA sn.pdf' → ['C']  ; 'Bac_C_science_2022_SC.pdf' → ['C']
    Si introuvable, fallback sur la métadata."""
    m = FILIERE_FROM_FILENAME.search(source or "")
    if m:
        f = (m.group(1) or m.group(2)).upper()
        return [f]
    return [f.upper() for f in fallback if f] or ["C"]  # défaut C


def convert_corpus(src_path: Path) -> list[dict[str, Any]]:
    """Charge un JSON vision, retourne la liste convertie.

    Filière dérivée du nom de fichier source (le champ meta['filiere'] est
    parfois sur-classifié C+D par Vision pour des exos en réalité C-only).
    """
    data = json.load(open(src_path, encoding="utf-8"))
    out: list[dict[str, Any]] = []
    for ex in data:
        source = ex["metadata"].get("source_sujet", "")
        filieres = filiere_from_source(source, ex["metadata"].get("filiere") or [])
        for fil in filieres:
            out.append(convert_one(ex, fil))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Montre le diff sans toucher")
    args = ap.parse_args()

    # Charge l'existant
    existing = json.load(open(JSON_BAC, encoding="utf-8"))
    print(f"json_bac.json actuel : {len(existing)} exos")

    # Sépare en garder vs supprimer
    keep = [e for e in existing if (e.get("annee") or 0) < CUTOFF_YEAR]
    drop = [e for e in existing if (e.get("annee") or 0) >= CUTOFF_YEAR]
    n_validated_dropped = sum(1 for e in drop if e.get("validated_by_admin"))
    print(f"  → on garde {len(keep)} exos (annee < {CUTOFF_YEAR})")
    print(f"  → on supprime {len(drop)} exos (annee >= {CUTOFF_YEAR}, dont {n_validated_dropped} validés admin)")

    # Convertit les nouveaux
    new_exos: list[dict[str, Any]] = []
    for matiere, path in NEW_SOURCES.items():
        if not path.exists():
            print(f"  ⚠ {path} introuvable, skip", file=sys.stderr)
            continue
        converted = convert_corpus(path)
        print(f"  + {matiere}: {len(converted)} entries (après split C+D)")
        new_exos.extend(converted)

    # Vérif IDs uniques
    from collections import Counter
    id_counts = Counter(e["id"] for e in new_exos)
    dups = {k: v for k, v in id_counts.items() if v > 1}
    if dups:
        print(f"\n⚠ {len(dups)} IDs dupliqués dans le nouveau corpus :")
        for k, v in list(dups.items())[:5]:
            print(f"    {k}: {v}×")
        print("  → migration AVORTÉE pour éviter la corruption.")
        return 1

    # Vérif collisions avec ceux qu'on garde
    keep_ids = {e["id"] for e in keep}
    collisions = [e for e in new_exos if e["id"] in keep_ids]
    if collisions:
        print(f"\n⚠ {len(collisions)} nouveaux IDs entrent en collision avec des exos pre-2015 conservés.")
        for e in collisions[:5]:
            print(f"    {e['id']}")
        print("  → migration AVORTÉE.")
        return 1

    final = keep + new_exos
    print(f"\nRésultat final : {len(final)} exos ({len(keep)} legacy + {len(new_exos)} vision)")

    if args.dry_run:
        print("\n[DRY-RUN] aucune écriture. Lance sans --dry-run pour appliquer.")
        return 0

    # Backup
    backup_path = JSON_BAC.with_name(
        f"json_bac.backup_pre_vision_{datetime.now():%Y%m%d_%H%M%S}.json"
    )
    shutil.copy2(JSON_BAC, backup_path)
    print(f"\n✓ Backup : {backup_path.name}")

    # Write
    with open(JSON_BAC, "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print(f"✓ json_bac.json mis à jour ({len(final)} exos)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
