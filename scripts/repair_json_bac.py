"""Répare et normalise json_bac.json.

Ton JSON contient 3 schémas mélangés (à cause de génération par différents
outils LLM) et des erreurs de syntaxe :

  Schéma A : flat, `chapitre` (singulier)
  Schéma B : flat, `chapitres` (pluriel = liste)
  Schéma C : nested  {id, metadata: {fichier_source, ...}, contenu: {...}}

Erreurs de syntaxe rencontrées :
  - `\%` non valide en JSON → remplacé par `%`
  - tableaux imbriqués sauvages

Ce script :
  1. Lit le fichier brut, applique des corrections regex (escape sequences).
  2. Sauve une version 'parseable' (json_bac_parseable.json).
  3. Aplatit récursivement (descend dans les listes imbriquées).
  4. Normalise vers UN schéma cible commun.
  5. Sauve `json_bac_clean.json` propre.

Schéma cible :
  {
    id, matiere_id, filiere_id,         ← ajoutés
    fichier, exercice_numero, matiere,
    annee, session, filiere,
    chapitre, chapitres, notions_traitees,
    ennonce_complet,
    donnees_fournies (optionnel)
  }
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "json_bac.json"
DEFAULT_OUTPUT = ROOT / "json_bac_clean.json"
PARSEABLE_DUMP = ROOT / "json_bac_parseable.json"


# ─── 1. Réparation syntaxe ──────────────────────────────────────────────────


def repair_json_text(raw: str) -> str:
    """Corrige les erreurs de syntaxe JSON courantes générées par LLMs."""
    # \% n'est pas un escape JSON valide. On remplace par %.
    # Idem pour les autres \X où X n'est pas un escape standard.
    valid_escapes = set('"\\/bfnrtu')

    def fix_escape(m: re.Match) -> str:
        c = m.group(1)
        if c in valid_escapes:
            return m.group(0)  # garde \" \\ etc.
        return c  # supprime le backslash

    raw = re.sub(r"\\(.)", fix_escape, raw)
    return raw


# ─── 2. Parsing tolérant ────────────────────────────────────────────────────


def safe_load(path: Path) -> list:
    """Charge le JSON de façon tolérante.

    Stratégie :
      1. Tente un parse direct (après réparation des escapes).
      2. Si ça échoue, on extrait tous les objets de premier niveau via
         json.JSONDecoder.raw_decode — peu importe la structure englobante
         (listes mal fermées, imbrications sauvages, etc.).
    """
    raw = path.read_text(encoding="utf-8")
    repaired = repair_json_text(raw)
    PARSEABLE_DUMP.write_text(repaired, encoding="utf-8")
    try:
        return json.loads(repaired)
    except json.JSONDecodeError as e:
        print(f"\n⚠️ Parse direct échoué (ligne {e.lineno}): {e.msg}", file=sys.stderr)
        print("   → fallback : extraction objet-par-objet tolérante", file=sys.stderr)

    # Fallback : extraction tolérante. On scanne le texte et on récupère tous
    # les objets JSON (dict) qu'on trouve, en sautant les caractères entre.
    decoder = json.JSONDecoder()
    objects: list = []
    i = 0
    n = len(repaired)
    while i < n:
        # On saute jusqu'au prochain '{' qui démarre un objet
        while i < n and repaired[i] != "{":
            i += 1
        if i >= n:
            break
        try:
            obj, end = decoder.raw_decode(repaired, i)
            objects.append(obj)
            i = end
        except json.JSONDecodeError:
            # Cet emplacement n'est pas un objet valide, on avance d'un cran
            i += 1
    print(f"   → {len(objects)} objets récupérés via le fallback", file=sys.stderr)
    return objects


# ─── 3. Aplatissement récursif ──────────────────────────────────────────────


def flatten(data) -> list[dict]:
    """Aplatit récursivement n'importe quelle structure imbriquée [list of
    list of dict] en une seule liste de dicts."""
    out: list[dict] = []
    if isinstance(data, dict):
        out.append(data)
    elif isinstance(data, list):
        for item in data:
            out.extend(flatten(item))
    return out


# ─── 4. Normalisation vers schéma commun ────────────────────────────────────


def normalize_entry(entry: dict) -> dict | None:
    """Convertit n'importe lequel des 3 schémas en un schéma flat commun.
    Retourne None si l'entrée est inutilisable."""
    if not isinstance(entry, dict):
        return None

    # Schéma C : nested → on remonte metadata et contenu d'un niveau
    if "metadata" in entry or "contenu" in entry:
        meta = entry.get("metadata") or {}
        cont = entry.get("contenu") or {}
        merged = {**meta, **cont}
        # Garde l'id éventuel et le exercice_numero
        if "id" in entry and "id" not in merged:
            merged["id_source"] = entry["id"]
        # Renomme fichier_source → fichier pour cohérence
        if "fichier_source" in merged and "fichier" not in merged:
            merged["fichier"] = merged.pop("fichier_source")
        # Renomme notions_cles → notions_traitees
        if "notions_cles" in merged and "notions_traitees" not in merged:
            merged["notions_traitees"] = merged.pop("notions_cles")
        entry = merged

    # `chapitre` (singulier) vs `chapitres` (liste)
    chapitre = entry.get("chapitre")
    chapitres = entry.get("chapitres")
    if not chapitre and chapitres:
        # On garde le premier comme chapitre principal, on conserve la liste
        if isinstance(chapitres, list) and chapitres:
            chapitre = chapitres[0]
    if not chapitres and chapitre:
        chapitres = [chapitre]
    if not isinstance(chapitres, list):
        chapitres = []

    # Champs minimums requis
    fichier = entry.get("fichier", "")
    matiere = entry.get("matiere", "")
    annee = entry.get("annee")
    if not fichier or not matiere or annee is None:
        return None

    return {
        "fichier": fichier,
        "exercice_numero": entry.get("exercice_numero", entry.get("id_source", "?")),
        "matiere": matiere,
        "annee": annee,
        "session": entry.get("session", "Normale"),
        "filiere": entry.get("filiere", ""),
        "chapitre": chapitre or "",
        "chapitres": chapitres,
        "notions_traitees": entry.get("notions_traitees", []),
        "ennonce_complet": entry.get("ennonce_complet", ""),
        "donnees_fournies": entry.get("donnees_fournies", {}),
    }


# ─── 5. Enrichissement (matiere_id, filiere_id, id) ─────────────────────────


_CITE_RE = re.compile(r"\s*\[cite:\s*[^\]]+\]")


def clean_ennonce(text: str) -> str:
    if not text:
        return ""
    t = _CITE_RE.sub("", text)
    t = re.sub(r"[ \t]+", " ", t).strip()
    return t


def detect_matiere(matiere: str) -> str:
    if not matiere:
        return "autre"
    s = unicodedata.normalize("NFC", matiere).lower()
    if "(chimie)" in s or s.strip() == "chimie":
        return "chimie"
    if "(physique)" in s or "physique" in s and "chimie" not in s:
        return "physique"
    if "(svt)" in s or "naturelle" in s or s.strip() == "svt":
        return "svt"
    if "math" in s:
        return "math"
    return "autre"


def detect_filiere(filiere: str) -> str:
    if not filiere:
        return "autre"
    s = unicodedata.normalize("NFC", filiere).upper()
    if re.search(r"\bT\.?M\.?G\.?M\.?\b", s) or re.search(r"\bT\.?M\.?\b", s):
        return "TM"
    if re.search(r"\bS[EÉ]RIE\s+C\b", s) or "BAC C" in s:
        return "C"
    if re.search(r"\bS[EÉ]RIE\s+D\b", s) or "BAC D" in s:
        return "D"
    if re.search(r"\bS[EÉ]RIE\s+M\b", s):
        return "M"
    if "MATH" in s:
        return "M"  # défaut prudent
    return "autre"


def make_id(mat: str, annee, session: str, ex_num) -> str:
    s = (session or "").lower()
    sess_code = "sn" if "normal" in s else ("sc" if "compl" in s else "x")
    return f"{mat}-{annee}-{sess_code}-ex{ex_num}"


def enrich(entry: dict) -> dict:
    mat_id = detect_matiere(entry.get("matiere", ""))
    fil_id = detect_filiere(entry.get("filiere", ""))
    return {
        "id": make_id(mat_id, entry["annee"], entry.get("session", ""), entry.get("exercice_numero")),
        "matiere_id": mat_id,
        "filiere_id": fil_id,
        **{k: v for k, v in entry.items() if k != "ennonce_complet"},
        "ennonce_complet": clean_ennonce(entry.get("ennonce_complet", "")),
    }


# ─── 6. Pipeline ────────────────────────────────────────────────────────────


def main() -> int:
    print(f"→ Lecture {DEFAULT_INPUT}")
    raw = safe_load(DEFAULT_INPUT)
    print(f"   parsé OK ({type(raw).__name__})")

    flat = flatten(raw)
    print(f"→ Aplatissement : {len(flat)} dicts trouvés (toutes structures confondues)")

    normalized = [n for n in (normalize_entry(e) for e in flat) if n]
    print(f"→ Normalisation : {len(normalized)} entrées valides "
          f"({len(flat) - len(normalized)} rejetées car incomplètes)")

    enriched = [enrich(e) for e in normalized]
    DEFAULT_OUTPUT.write_text(
        json.dumps(enriched, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"→ Écriture {DEFAULT_OUTPUT} ({len(enriched)} entrées)")

    # ─── Stats ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print(f"TOTAL : {len(enriched)} exercices après nettoyage")
    print("=" * 70)

    by_mat: dict[str, list] = defaultdict(list)
    for e in enriched:
        by_mat[e["matiere_id"]].append(e)

    print(f"\n{'Matière':<12} {'Exos':<6} {'Années couvertes':<35} {'Chapitres':<10}")
    print("-" * 70)
    for mat in ["math", "physique", "chimie", "svt", "autre"]:
        entries = by_mat.get(mat, [])
        if mat == "autre" and not entries:
            continue
        n = len(entries)
        years = sorted({e["annee"] for e in entries})
        chap = sorted({e.get("chapitre") for e in entries if e.get("chapitre")})
        years_str = ", ".join(str(y) for y in years) if years else "—"
        if len(years_str) > 32:
            years_str = f"{min(years)}–{max(years)} ({len(years)} ans)"
        print(f"{mat:<12} {n:<6} {years_str:<35} {len(chap):<10}")

    # Détail par matière
    print("\n## Détail par matière (exos par année)\n")
    for mat in ["math", "physique", "chimie", "svt", "autre"]:
        entries = by_mat.get(mat, [])
        if not entries:
            continue
        print(f"### {mat} : {len(entries)} exo(s)")
        by_year: dict = defaultdict(list)
        for e in entries:
            by_year[e["annee"]].append(e)
        for year in sorted(by_year):
            exs = by_year[year]
            print(f"  {year} : {len(exs)} exo(s)")
        print()

    # Matrice matière × année
    print("## Matrice matière × année\n")
    all_years = sorted({e["annee"] for e in enriched})
    if all_years:
        header = "         | " + " | ".join(str(y) for y in all_years) + " |"
        print(header)
        print("         |" + "------|" * len(all_years))
        for mat in ["math", "physique", "chimie", "svt"]:
            entries = by_mat.get(mat, [])
            row = []
            for y in all_years:
                n = sum(1 for e in entries if e["annee"] == y)
                row.append(f"{n:^4}" if n else "  —  ")
            print(f"{mat:<8} | " + " | ".join(row) + " |")

    # Top chapitres
    print("\n## Top chapitres\n")
    chap_counter = Counter(e.get("chapitre", "?") for e in enriched if e.get("chapitre"))
    for chap, n in chap_counter.most_common(15):
        print(f"  {n:3}  {chap}")

    # Couverture vs corpus
    files_in_json = {e["fichier"] for e in enriched if e.get("fichier")}
    corpus = set()
    drive = ROOT.parent / "drive_archive"
    if drive.exists():
        for p in drive.rglob("*.pdf"):
            corpus.add(p.name)
        corrige = {f for f in corpus if "corr" in f.lower()}
        cov = files_in_json & corpus
        cov_corr = files_in_json & corrige
        print("\n## Couverture vs drive_archive/")
        print(f"  PDFs uniques dans le JSON  : {len(files_in_json)}")
        print(f"  PDFs dans drive_archive    : {len(corpus)}")
        print(f"  Corrigés dans drive_archive: {len(corrige)}")
        print(f"  → JSON ∩ corpus            : {len(cov)} ({len(cov)/max(1,len(corpus)):.1%})")
        print(f"  → JSON ∩ corrigés          : {len(cov_corr)} ({len(cov_corr)/max(1,len(corrige)):.1%})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
