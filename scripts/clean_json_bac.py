"""Nettoie et enrichit json_bac.json.

Fait 4 choses :
1. Supprime les balises [cite: ...] résiduelles de l'extraction LLM.
2. Ajoute `matiere_id`  ∈ {math, physique, chimie, svt}.
3. Ajoute `filiere_id`  ∈ {C, D, TM, M, autre}.
4. Ajoute `id` unique stable (matiere_id-annee-session-exN).

Calcule aussi le taux de couverture : combien de PDFs du corpus indexé sont
référencés par au moins une entrée du JSON.

Idempotent : on peut le relancer, il met juste à jour les champs.

Usage:
    python scripts/clean_json_bac.py                      # crée json_bac_clean.json
    python scripts/clean_json_bac.py --in-place           # écrase json_bac.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "json_bac.json"
DEFAULT_OUTPUT = ROOT / "json_bac_clean.json"

# ─── Normalisation ──────────────────────────────────────────────────────────

# Balises issues de l'extraction LLM (NotebookLM / Claude / GPT) : [cite: 6, 7, 8]
_CITE_RE = re.compile(r"\s*\[cite:\s*[^\]]+\]")
# Multiples espaces / sauts de ligne → un seul espace
_WHITESPACE_RE = re.compile(r"[ \t]+")
_MULTI_NEWLINE_RE = re.compile(r"\n{3,}")


def clean_ennonce(text: str) -> str:
    """Nettoie l'énoncé : retire balises [cite], collapse les espaces."""
    if not text:
        return ""
    t = _CITE_RE.sub("", text)
    t = _WHITESPACE_RE.sub(" ", t)
    t = _MULTI_NEWLINE_RE.sub("\n\n", t)
    return t.strip()


# Mapping matière verbose → matiere_id
_MATIERE_PATTERNS = [
    (r"chimie", "chimie"),
    (r"physiques?\b(?!\s*\(chimie\))", "physique"),  # "Sciences Physiques" sans (Chimie)
    (r"math[eé]matiques?", "math"),
    (r"sciences? naturelles?", "svt"),
    (r"\bsvt\b", "svt"),
    (r"biologie", "svt"),
]


def detect_matiere(matiere: str) -> str:
    """Renvoie math|physique|chimie|svt depuis la chaîne verbose."""
    if not matiere:
        return "autre"
    s = unicodedata.normalize("NFC", matiere).lower()
    # Cas spécial : "Sciences Physiques (Chimie)" → chimie (parenthèse domine)
    if "(chimie)" in s:
        return "chimie"
    if "(physique)" in s:
        return "physique"
    if "(svt)" in s or "(sciences naturelles)" in s:
        return "svt"
    for pat, sid in _MATIERE_PATTERNS:
        if re.search(pat, s):
            return sid
    return "autre"


# Mapping filière verbose → filiere_id
def detect_filiere(filiere: str) -> str:
    """Mauritanie 2026 — 2 filières scientifiques effectives.

    - C : toutes les variantes math/scientifiques (C, M, TM, TMGM, MA)
    - D : SVT
    """
    if not filiere:
        return "C"
    s = unicodedata.normalize("NFC", filiere).upper()
    if re.search(r"\bS[EÉ]RIE\s+D\b", s) or re.search(r"\bBAC\s*D\b", s):
        return "D"
    return "C"


def make_id(matiere_id: str, annee, session: str, ex_num) -> str:
    sess = (session or "").lower()
    sess_code = "sn" if "normal" in sess else ("sc" if "compl" in sess else "x")
    return f"{matiere_id}-{annee}-{sess_code}-ex{ex_num}"


# ─── Pipeline ───────────────────────────────────────────────────────────────


def enrich(entry: dict) -> dict:
    matiere_id = detect_matiere(entry.get("matiere", ""))
    filiere_id = detect_filiere(entry.get("filiere", ""))
    eid = make_id(matiere_id, entry.get("annee"), entry.get("session", ""), entry.get("exercice_numero"))
    return {
        "id": eid,
        "matiere_id": matiere_id,
        "filiere_id": filiere_id,
        # On garde les champs originaux pour traçabilité
        **{k: v for k, v in entry.items() if k != "ennonce_complet"},
        "ennonce_complet": clean_ennonce(entry.get("ennonce_complet", "")),
    }


def compute_coverage(entries: list[dict], chroma_dir: Path) -> dict:
    """Calcule le taux de couverture vs Chroma : combien de PDFs du corpus
    indexé apparaissent dans le JSON."""
    files_in_json = {e.get("fichier") for e in entries if e.get("fichier")}
    out = {
        "entries": len(entries),
        "unique_files_in_json": len(files_in_json),
        "chroma_available": False,
    }
    try:
        import chromadb
        if not chroma_dir.exists():
            return out
        client = chromadb.PersistentClient(path=str(chroma_dir))
        coll = client.get_or_create_collection(name="bac_corpus")
        all_meta = coll.get(include=["metadatas"]).get("metadatas") or []
        sources_in_chroma = {(m or {}).get("source") for m in all_meta}
        sources_in_chroma.discard(None)
        covered = files_in_json & sources_in_chroma
        out.update({
            "chroma_available": True,
            "chroma_total_pdfs": len(sources_in_chroma),
            "chroma_total_chunks": len(all_meta),
            "files_covered_by_json": len(covered),
            "coverage_rate_pdfs": round(len(covered) / max(1, len(sources_in_chroma)), 4),
            "files_in_json_not_in_chroma": sorted(files_in_json - sources_in_chroma),
        })
    except Exception as e:
        out["chroma_error"] = str(e)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--in-place", action="store_true", help="écrase --input")
    parser.add_argument("--chroma-dir", default=str(ROOT / "data" / "chroma"))
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"ERREUR : {in_path} introuvable.", file=sys.stderr)
        return 2

    data = json.loads(in_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("ERREUR : json_bac.json doit être une liste.", file=sys.stderr)
        return 2

    enriched = [enrich(e) for e in data]

    out_path = in_path if args.in_place else Path(args.output)
    out_path.write_text(
        json.dumps(enriched, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # ─── Stats ──────────────────────────────────────────────────────────────
    mat = Counter(e["matiere_id"] for e in enriched)
    fil = Counter(e["filiere_id"] for e in enriched)
    chap = Counter(e.get("chapitre", "?") for e in enriched)
    cov = compute_coverage(enriched, Path(args.chroma_dir))

    if not args.quiet:
        print(f"\n→ {len(enriched)} entrées écrites dans {out_path}")
        print("\n## Répartition")
        print(f"  matières  : {dict(mat)}")
        print(f"  filières  : {dict(fil)}")
        print(f"  chapitres : {len(chap)} distincts → {dict(chap)}")
        print("\n## Couverture vs corpus Chroma indexé")
        if not cov["chroma_available"]:
            print(f"  ⚠️  Chroma DB non lisible ici ({cov.get('chroma_error', 'pas de DB locale')})")
            print(f"  PDFs uniques dans le JSON : {cov['unique_files_in_json']}")
        else:
            print(f"  Chroma : {cov['chroma_total_pdfs']} PDFs uniques ({cov['chroma_total_chunks']} chunks)")
            print(f"  JSON   : {cov['unique_files_in_json']} PDFs uniques")
            print(f"  Couverts : {cov['files_covered_by_json']} → "
                  f"**{cov['coverage_rate_pdfs']:.1%}** des PDFs du corpus indexé")
            if cov["files_in_json_not_in_chroma"]:
                print("  ⚠️  PDFs dans le JSON absents de Chroma :")
                for f in cov["files_in_json_not_in_chroma"]:
                    print(f"     - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
