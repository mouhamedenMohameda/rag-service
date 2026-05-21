"""Import en masse d'énoncés Bac depuis un texte (extraction Gemini).

Usage :
    # Sauve ton texte Gemini dans un fichier
    cat > /tmp/gemini.txt <<'EOF'
    Baccalauréat 2015 - Session Normale
    Exercice 1 (5pt)
    <énoncé exo 1>
    Exercice 2 (4pt)
    <énoncé exo 2>
    ...
    Baccalauréat 2015 - Session Complémentaire
    Exercice 1 (3pt)
    ...
    EOF

    # Dry-run pour vérifier le parsing avant écriture
    .venv/bin/python scripts/import_exos_from_text.py \
        --filiere C --matiere math --file /tmp/gemini.txt --dry-run

    # Application
    .venv/bin/python scripts/import_exos_from_text.py \
        --filiere C --matiere math --file /tmp/gemini.txt

    # Forcer l'écrasement des entrées déjà remplies
    .venv/bin/python scripts/import_exos_from_text.py \
        --filiere C --matiere math --file /tmp/gemini.txt --force

Pattern attendu dans le texte source :
  - Header de session : "Baccalauréat YYYY - Session [Normale|Complémentaire]"
    (insensible à la casse, accepte aussi "BAC", "Bac.", etc.)
  - Header d'exercice : "Exercice N" ou "EXERCICE N" ou "QCM"
    (les éventuels " (X points)" sont absorbés)
  - Le contenu de chaque exercice court jusqu'au prochain header.

Mapping vers les slots :
  - Si un QCM est présent dans une session : QCM → ex1, Exercice 1 → ex2, etc.
  - Sinon : Exercice N → exN.
  - Cible : entrée existante avec (filiere, matiere, année, session, exercice_numero).
    Pour matiere="pc", accepte aussi matiere_id legacy chimie/physique.

Validation et rapport :
  - Détecte les sessions sans header reconnu (silencieusement skip).
  - Détecte les exercices avec énoncé trop court (<50 chars) → warning.
  - Détecte les slots introuvables dans json_bac.json → liste.
  - Détecte les entrées déjà remplies (>100 chars) sans --force → liste.
  - Détecte les caractères suspects (artefacts OCR fréquents) → liste.

NE TOUCHE PAS validated_by_admin. Backup automatique avant écriture.
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


# ─── Parsing ────────────────────────────────────────────────────────────────

# "Baccalauréat 2015 - Session Complémentaire" + variantes (BAC, accents, " - Séries C & TMGM" en suffixe)
_RE_SESSION_HEADER = re.compile(
    r"Bac(?:c?al(?:\.|[éae]?aur[ée]?at)?)?\.?\s*"
    r"(\d{4})\s*[-–—]\s*Session\s*"
    r"(Normale?|Compl[ée]mentaire|complementaire)"
    r"(?:\s*[-–—].*?)?(?=\s*(?:Exercice|EXERCICE|QCM|Q\.C\.M|Q\.\s*C\.\s*M))",
    re.IGNORECASE | re.DOTALL,
)

# "Exercice 1 (4 pts)" ou "EXERCICE 1" ou "QCM (4 pts)"
_RE_EX_HEADER = re.compile(
    r"(?P<full>(?:Exercice|EXERCICE)\s*N?[°ºo]?\s*(?P<num>\d+)"
    r"(?:\s*(?:\([^)]*\)|bis|Bis|BIS))*"
    r"|(?:Q\.?\s*C\.?\s*M\.?)(?:\s*\([^)]*\))?)",
    re.IGNORECASE,
)

_SESSION_TO_CODE = {"normale": "sn", "normal": "sn",
                    "complémentaire": "sc", "complementaire": "sc"}


def normalize_session(s: str) -> str:
    return _SESSION_TO_CODE.get(s.strip().lower().rstrip("e") + "e", "")


def parse_text(text: str) -> list[tuple[int, str, int, str]]:
    """Retourne [(annee, sess_code, ex_num_canonique, ennonce), ...].

    ex_num_canonique : QCM → 1, Exercice N → N (ou N+1 s'il y a un QCM en tête
    de session — mais on garde N par défaut, le mapping QCM→ex1 est appliqué
    plus loin si nécessaire).
    """
    # Trouve toutes les sessions
    session_matches = list(_RE_SESSION_HEADER.finditer(text))
    if not session_matches:
        return []

    results: list[tuple[int, str, int, str]] = []
    for i, sm in enumerate(session_matches):
        annee = int(sm.group(1))
        sess_word = sm.group(2).lower()
        sess_code = "sn" if "normal" in sess_word else "sc"

        # Bornes de la section
        section_start = sm.end()
        section_end = session_matches[i + 1].start() if i + 1 < len(session_matches) else len(text)
        section = text[section_start:section_end]

        # Trouve tous les headers d'exercices dans la section
        ex_matches = list(_RE_EX_HEADER.finditer(section))
        if not ex_matches:
            continue

        # Détermine si la session commence par un QCM
        has_qcm = any("QCM" in m.group("full").upper() or "Q.C.M" in m.group("full").upper()
                      for m in ex_matches[:1])

        # Pour chaque exercice, extraire le contenu jusqu'au prochain header
        for j, em in enumerate(ex_matches):
            full_label = em.group("full").strip()
            is_qcm = "QCM" in full_label.upper() or "Q.C.M" in full_label.upper().replace(" ", "")

            if is_qcm:
                ex_num = 1  # QCM toujours en ex1
            else:
                num = int(em.group("num"))
                # Si la session commence par un QCM, décale les Exercice N → N+1
                ex_num = num + 1 if has_qcm else num

            content_start = em.end()
            content_end = ex_matches[j + 1].start() if j + 1 < len(ex_matches) else len(section)
            ennonce = section[content_start:content_end].strip()

            # Reconstruit l'en-tête original pour le préserver dans l'énoncé
            ennonce_with_header = f"{full_label}\n{ennonce}" if ennonce else full_label

            results.append((annee, sess_code, ex_num, ennonce_with_header))

    return results


# ─── Mapping vers entrées JSON ─────────────────────────────────────────────

_SESSION_MATCH = {"sn": "normal", "sc": "compl"}


def find_entry(data, filiere, matiere, annee, sess_code, ex_num):
    sess_substr = _SESSION_MATCH[sess_code]
    mat_accept = {"pc", "physique", "chimie"} if matiere == "pc" else {matiere}
    candidates = []
    for e in data:
        if e.get("filiere_id") != filiere:
            continue
        if e.get("matiere_id") not in mat_accept:
            continue
        if e.get("annee") != annee:
            continue
        if sess_substr not in str(e.get("session", "")).lower():
            continue
        try:
            num = int(e.get("exercice_numero"))
        except (TypeError, ValueError):
            continue
        if num != ex_num:
            continue
        candidates.append(e)
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    # Préfère l'entrée déjà remplie (legacy) si plusieurs candidats
    for c in candidates:
        if not c.get("is_skeleton") and (c.get("ennonce_complet") or "").strip():
            return c
    return candidates[0]


# ─── Validation ────────────────────────────────────────────────────────────

# Artefacts OCR typiques de Gemini : caractères mal décodés, espaces oubliés
_SUSPICIOUS_PATTERNS = [
    (re.compile(r"\$\$"), "double $$"),
    (re.compile(r"[Ss]érîe|sêrie|sárie"), "accent corrompu dans 'série'"),
    (re.compile(r"^\s*\)", re.MULTILINE), "parenthèse fermante isolée"),
    (re.compile(r"\\(?![a-zA-Z\\{}_^$%&#])"), "backslash isolé"),
    (re.compile(r"[^\x00-\x7FÀ-ſ̀-ͯ$\\{}^_<>≤≥±×÷∞∫∑∏√∂∆∇αβγδεζηθικλμνξοπρστυφχψωΓΔΘΛΞΠΣΦΨΩ°²³µπ–—…«»œœ€]"),
     "caractère non-latin/math suspect"),
]


def validate_ennonce(ennonce: str) -> list[str]:
    """Retourne la liste des warnings pour cet énoncé."""
    warnings = []
    if len(ennonce.strip()) < 50:
        warnings.append(f"énoncé court ({len(ennonce)} chars)")
    for pat, desc in _SUSPICIOUS_PATTERNS:
        m = pat.search(ennonce)
        if m:
            ctx = ennonce[max(0, m.start() - 15):min(len(ennonce), m.end() + 15)]
            warnings.append(f"{desc} : '...{ctx}...'")
    return warnings


# ─── Main ──────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--filiere", required=True, choices=["C", "D"])
    ap.add_argument("--matiere", required=True, choices=["math", "pc", "svt"])
    ap.add_argument("--file", required=True, help="Chemin du fichier texte Gemini")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="Écrase même les entrées déjà remplies (>100 chars).")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    parsed = parse_text(text)

    if not parsed:
        print("⚠️  Aucune session/exercice détecté(e) dans le fichier.",
              file=sys.stderr)
        print("    Vérifie que le texte contient bien des headers du type :",
              file=sys.stderr)
        print("    'Baccalauréat YYYY - Session [Normale|Complémentaire]'",
              file=sys.stderr)
        print("    'Exercice N (...)'", file=sys.stderr)
        return 2

    print(f"📋 Parsing du fichier : {len(parsed)} énoncé(s) détecté(s).\n")

    # Charge JSON
    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))
    now = datetime.now().isoformat(timespec="seconds")

    updated, skipped_missing, skipped_filled, warnings_global = [], [], [], []

    for annee, sess, ex_num, ennonce in parsed:
        label = f"{args.filiere}/{args.matiere}/{annee}/{sess}/ex{ex_num}"

        # Validation
        warns = validate_ennonce(ennonce)
        if warns:
            warnings_global.append((label, warns))

        e = find_entry(data, args.filiere, args.matiere, annee, sess, ex_num)
        if e is None:
            skipped_missing.append(label)
            continue
        eid = e.get("id", "?")
        old = (e.get("ennonce_complet") or "").strip()
        if old and len(old) > 100 and not args.force:
            skipped_filled.append((label, eid, len(old)))
            continue

        e["ennonce_complet"] = ennonce.strip()
        e["is_skeleton"] = False
        e["updated_at"] = now
        updated.append((label, eid, len(old), len(ennonce.strip())))

    # ─── Rapport ────────────────────────────────────────────────────────
    print(f"Mapping vers slots json_bac.json :")
    print(f"  → mis à jour    : {len(updated)}")
    print(f"  → introuvables  : {len(skipped_missing)}")
    print(f"  → déjà remplis  : {len(skipped_filled)} (utiliser --force pour écraser)")
    print(f"  → warnings      : {len(warnings_global)}")

    if updated:
        print(f"\n✅ Mises à jour (premiers 20) :")
        for label, eid, ol, nl in updated[:20]:
            print(f"  {label:30}  → {eid:45}  {ol} → {nl} chars")
        if len(updated) > 20:
            print(f"  ... + {len(updated) - 20} autres")

    if skipped_missing:
        print(f"\n❌ Introuvables ({len(skipped_missing)} — slot inexistant dans json_bac.json) :")
        for label in skipped_missing[:30]:
            print(f"  {label}")
        if len(skipped_missing) > 30:
            print(f"  ... + {len(skipped_missing) - 30} autres")

    if skipped_filled:
        print(f"\n⏭️  Déjà remplis (>100 chars), --force pour écraser :")
        for label, eid, ln in skipped_filled[:30]:
            print(f"  {label:30}  → {eid:45}  ({ln} chars)")
        if len(skipped_filled) > 30:
            print(f"  ... + {len(skipped_filled) - 30} autres")

    if warnings_global:
        print(f"\n⚠️  Warnings de validation ({len(warnings_global)} énoncés concernés) :")
        for label, warns in warnings_global[:20]:
            for w in warns:
                print(f"  {label:30}  {w}")
        if len(warnings_global) > 20:
            print(f"  ... + {len(warnings_global) - 20} autres énoncés avec warnings")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not updated:
        print("\nRien à écrire.")
        return 0

    # Écriture
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-import-{args.filiere}-{args.matiere}-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")

    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour ({len(updated)} entrées).")
    print("Pas besoin de restart rag-service.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
