#!/usr/bin/env python3
"""
generate_corrections.py

Extrait les corrections des PDF corrigés du bac mauritanien et les associe
aux exercices déjà extraits par extract_vision.py.

Stratégie :
  1. Charge les exercices JSON (avec correction=null)
  2. Pour chaque exercice, trouve le meilleur PDF corrigé correspondant
     (année + filière + session)
  3. Transcrit le PDF avec vision GPT-4o-mini (cache → payé une seule fois)
  4. Extrait uniquement la correction de cet exercice depuis la transcription
  5. Sauvegarde incrémentalement (checkpoint toutes les 10 corrections)

Usage :
  python3 generate_corrections.py --matiere math
  python3 generate_corrections.py --matiere pc
  python3 generate_corrections.py --matiere svt
  python3 generate_corrections.py --matiere math --dry-run   # test matching sans appel API
"""

import json
import os
import re
import sys
import time
import argparse
import logging
import base64
from pathlib import Path

import fitz  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ── Modèles ──────────────────────────────────────────────────────────────────
# gpt-4o    : vision (transcription PDF) — obligatoire, gpt-4o-mini refuse les docs d'examen
# gpt-4o-mini : extraction texte → correction — pas d'image, ~33x moins cher
VISION_MODEL = "gpt-4o"        # lecture OCR des pages PDF (corrigés scannés)
STRUCT_MODEL  = "gpt-4o-mini"  # extraction de la correction depuis le texte transcrit
RENDER_ZOOM   = 2.0
JPEG_QUALITY  = 85

# ── Dossiers de corrections par matière et filière ──────────────────────────
BASE = "/Users/mohameda/Documents/Bac/drive_archive/annals"
CORR_DIRS = {
    "math": {
        "C": [{"path": f"{BASE}/Sujets corrigés math/bac c/les corrigee", "dedicated": True}],
        "D": [{"path": f"{BASE}/Sujets corrigés math/bac d/les corrigee", "dedicated": True}],
    },
    "pc": {
        # bac c : dossier mixte (sujets + corrigés sans "corr" dans le nom)
        # → on inclut tous les PDFs, le matching filtre par année/session
        # Les sujets déjà extraits seront ignorés car ils ne contiennent pas la correction
        "C": [{"path": f"{BASE}/phisique et chimie/bac c", "dedicated": False}],
        "D": [{"path": f"{BASE}/phisique et chimie/bac d/les corrigee", "dedicated": True}],
    },
    "svt": {
        "C": [{"path": f"{BASE}/Science naturelle/bac c/les corrigee", "dedicated": True}],
        "D": [{"path": f"{BASE}/Science naturelle/bac d/les corrigee", "dedicated": True}],
    },
}

# ── JSONs d'exercices source par matière ────────────────────────────────────
EXERCISE_JSONS = {
    "math": [
        "exercises_extracted/bac_C_math_2015_2024.json",
        "exercises_extracted/bac_D_math_2015_2024.json",
        "exercises_extracted/bac_2025_vision.json",
    ],
    "pc": [
        "exercises_extracted/bac_CD_pc_2015_2025.json",
    ],
    "svt": [
        "exercises_extracted/bac_CD_svt_2015_2025.json",
    ],
}

# Normalisation matière
MATIERE_MAP = {
    "physique": "pc", "chimie": "pc", "physique-chimie": "pc",
    "math": "math", "mathematiques": "math",
    "svt": "svt", "science naturelle": "svt", "sciences naturelles": "svt",
}


# ────────────────────────────────────────────────────────────────────────────
# 1. Parser les informations d'un PDF de correction depuis son nom de fichier
# ────────────────────────────────────────────────────────────────────────────

def parse_pdf_info(pdf_path: Path) -> dict:
    """Extrait année, filière, session depuis le nom d'un PDF de correction."""
    name = pdf_path.name.lower()
    path_str = str(pdf_path).lower()

    # Est-ce un corrigé ? (pour les dossiers mixtes comme bac c PC)
    is_corr = any(x in name for x in ["corr", "corrigé", "corrige", "correction", "solution"])

    # Filière depuis le chemin
    filieres = set()
    if "/bac c/" in path_str:
        filieres.add("C")
    if "/bac d/" in path_str:
        filieres.add("D")
    # Filière depuis le nom de fichier
    if re.search(r"\bbac\s*c\b", name) or re.search(r"\bbacc\b", name):
        filieres.add("C")
    if re.search(r"\bbac\s*d\b", name) or re.search(r"\bbacd\b", name):
        filieres.add("D")

    # Session
    has_sn = bool(re.search(r"[\s_\-\.]sn[\s_\-\.]|[\s_\-\.]sn$", name))
    has_sc = bool(re.search(r"[\s_\-\.]sc[\s_\-\.]|[\s_\-\.]sc$|sc\s*\(", name))
    # More permissive
    if not has_sn:
        has_sn = bool(re.search(r"\bsn\b", name))
    if not has_sc:
        has_sc = bool(re.search(r"\bsc\b", name))

    if has_sn and has_sc:
        sessions = {"sn", "sc"}
    elif has_sn:
        sessions = {"sn"}
    elif has_sc:
        sessions = {"sc"}
    else:
        sessions = {"sn", "sc"}   # couvre les deux par défaut

    # Plage d'années : "2002 a 2012", "2005 - 2014", ou année unique
    range1 = re.search(r"(\d{4})\s+[aà]\s+(\d{4})", name)
    range2 = re.search(r"(\d{4})\s*[-–]\s*(\d{4})", name)
    years_found = re.findall(r"(?<!\d)(20\d{2})(?!\d)", name)

    if range1:
        y1, y2 = int(range1.group(1)), int(range1.group(2))
    elif range2:
        y1, y2 = int(range2.group(1)), int(range2.group(2))
    elif years_found:
        y1 = y2 = int(years_found[0])
    else:
        y1 = y2 = None

    return {
        "path": pdf_path,
        "year_start": y1,
        "year_end": y2,
        "filieres": filieres,
        "sessions": sessions,
        "is_correction": is_corr,
    }


def scan_corr_pdfs(matiere: str) -> list:
    """Liste tous les PDFs de corrections disponibles pour une matière."""
    results = []
    dirs_by_filiere = CORR_DIRS.get(matiere, {})

    for filiere, dir_list in dirs_by_filiere.items():
        for dir_cfg in dir_list:
            d = dir_cfg["path"]
            dedicated = dir_cfg["dedicated"]  # True = dossier 100% corrigés
            p = Path(d)
            if not p.exists():
                log.warning(f"Dossier introuvable : {d}")
                continue
            for f in sorted(p.glob("*.pdf")):
                info = parse_pdf_info(f)
                # Dans un dossier dédié corrigés → tout est corrigé
                if dedicated:
                    info["is_correction"] = True
                # Dans un dossier mixte → inclure si corrigé nommé OU si a une année+session
                elif not info["is_correction"]:
                    # Inclure si le fichier a une année et une session explicite (probable corrigé)
                    if info["year_start"] and (
                        re.search(r"\bsn\b", f.name.lower()) or
                        re.search(r"\bsc\b", f.name.lower())
                    ):
                        info["is_correction"] = True  # probable corrigé
                # Inférer filière depuis le dossier si non détectée
                if not info["filieres"]:
                    info["filieres"].add(filiere)
                if info["is_correction"]:
                    results.append(info)

    log.info(f"  → {len(results)} PDFs de corrigés trouvés pour {matiere}")
    return results


# ────────────────────────────────────────────────────────────────────────────
# 2. Matching exercice → PDF corrigé
# ────────────────────────────────────────────────────────────────────────────

def find_correction_pdf(year: int, filiere: str, session_code: str,
                        corr_pdfs: list) -> dict:
    """
    Trouve le meilleur PDF corrigé pour (année, filière, session).
    Préfère : année exacte > plage d'années, session exacte > toutes sessions.
    """
    candidates = []
    for info in corr_pdfs:
        y1, y2 = info["year_start"], info["year_end"]
        if y1 is None:
            continue
        # Filtre année
        if not (y1 <= year <= y2):
            continue
        # Filtre filière (si spécifié dans le PDF)
        if info["filieres"] and filiere not in info["filieres"]:
            continue

        # Score : plus c'est précis, mieux c'est
        score = 0
        if y1 == y2 == year:
            score += 10                  # année exacte
        else:
            score += max(0, 5 - (y2 - y1) // 2)  # pénalité pour grande plage

        if session_code in info["sessions"]:
            score += 5
        if len(info["sessions"]) == 1:
            score += 2                  # session exacte (pas générique)

        candidates.append((score, info))

    if not candidates:
        return None
    candidates.sort(key=lambda x: -x[0])
    return candidates[0][1]


# ────────────────────────────────────────────────────────────────────────────
# 3. Transcription PDF → texte (avec cache)
# ────────────────────────────────────────────────────────────────────────────

def render_pdf_pages(pdf_path: Path, max_pages: int = 30) -> list:
    """Convertit les pages PDF en JPEG bytes."""
    doc = fitz.open(str(pdf_path))
    pages = []
    mat = fitz.Matrix(RENDER_ZOOM, RENDER_ZOOM)
    for i, page in enumerate(doc):
        if i >= max_pages:
            log.warning(f"  Limite {max_pages} pages atteinte pour {pdf_path.name}")
            break
        pix = page.get_pixmap(matrix=mat)
        pages.append(pix.tobytes("jpeg", jpg_quality=JPEG_QUALITY))
    doc.close()
    return pages


def transcribe_pdf(pdf_path: Path, cache_dir: Path) -> str:  # noqa
    """Transcrit un PDF corrigé avec vision GPT-4o-mini. Résultat mis en cache."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / (pdf_path.stem + ".txt")

    if cache_file.exists():
        log.info(f"  [CACHE] {pdf_path.name}")
        return cache_file.read_text(encoding="utf-8")

    log.info(f"  Transcription vision : {pdf_path.name}")
    pages_bytes = render_pdf_pages(pdf_path)
    parts = []

    for i, page_bytes in enumerate(pages_bytes):
        b64 = base64.b64encode(page_bytes).decode()
        kb = len(page_bytes) / 1024
        log.info(f"    Page {i+1}/{len(pages_bytes)} ({kb:.1f} KB) → {VISION_MODEL}")
        if i > 0:
            time.sleep(3.0)  # évite le rate limit TPM (200K/min pour gpt-4o-mini)
        resp = _api_call(client.chat.completions.create,
            model=VISION_MODEL,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Tu lis un corrigé d'examen du baccalauréat mauritanien. "
                            "Transcris TOUT le texte visible sur cette page. "
                            "Conserve la structure : Exercice N, parties (1), (2), (a), (b)... "
                            "Utilise LaTeX pour les formules mathématiques ($...$). "
                            "Transcris les figures ou schémas brièvement entre [FIGURE: ...]. "
                            "Ne saute aucun contenu."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{b64}",
                            "detail": "high",
                        },
                    },
                ],
            }],
            max_tokens=4096,
        )
        parts.append(f"=== PAGE {i+1} ===\n{resp.choices[0].message.content}")

    full_text = "\n\n".join(parts)
    cache_file.write_text(full_text, encoding="utf-8")
    log.info(f"  ✓ Transcription sauvegardée ({len(full_text)} chars) → cache")
    return full_text


# ────────────────────────────────────────────────────────────────────────────
# 4. Extraction de la correction d'un exercice depuis la transcription
# ────────────────────────────────────────────────────────────────────────────

def _api_call(func, *args, max_retries=5, **kwargs):
    """Appel API avec retry exponentiel sur rate limit (429)."""
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "429" in str(e) or "rate_limit" in str(e).lower():
                wait = 65 * (attempt + 1)  # 65s, 130s, ...
                log.warning(f"Rate limit 429 — attente {wait}s (tentative {attempt+1}/{max_retries})")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("Rate limit persistant après plusieurs tentatives")


def get_relevant_excerpt(transcript: str, year: int, session_code: str,
                         max_len: int = 14000) -> str:
    """
    Pour les PDFs multi-années (grande transcription), extrait la portion
    pertinente autour de l'année cible pour réduire les tokens.
    """
    if len(transcript) <= max_len:
        return transcript

    year_str = str(year)
    # Cherche la position de l'année dans le transcript
    idx = -1
    for pat in [year_str + r".*" + session_code, session_code + r".*" + year_str, year_str]:
        m = re.search(pat, transcript, re.IGNORECASE)
        if m:
            idx = m.start()
            break

    if idx == -1:
        return transcript[:max_len]  # fallback : début du document

    start = max(0, idx - 500)
    end = min(len(transcript), start + max_len)
    return transcript[start:end]


def extract_correction(transcript: str, exercise: dict):
    """Extrait la correction d'un exercice depuis la transcription du corrigé."""
    meta = exercise.get("metadata", {})
    year = meta.get("annee", "?")
    filiere_raw = meta.get("filiere", ["C"])
    filiere = filiere_raw[0] if isinstance(filiere_raw, list) else filiere_raw
    session_str = meta.get("session", "normale")
    session_code = "sn" if session_str == "normale" else "sc"
    session_label = "Normale (SN)" if session_str == "normale" else "Complémentaire (SC)"
    num = meta.get("numero_exercice", 1)
    titre = meta.get("titre") or ""
    enonce = exercise.get("enonce", "")[:1000]

    excerpt = get_relevant_excerpt(transcript, year, session_code)

    prompt = f"""Tu as la transcription d'un corrigé du Baccalauréat {filiere} — Année {year} — Session {session_label}.

TRANSCRIPTION DU CORRIGÉ :
{excerpt}

---
Extrais UNIQUEMENT la correction complète de l'**Exercice {num}**{f' — {titre}' if titre else ''}.

L'énoncé de cet exercice est :
{enonce}

Instructions strictes :
- Restitue TOUTE la correction de cet exercice (calculs détaillés, démonstrations étape par étape, résultats finals).
- Conserve la structure originale : parties (1), (2)... (a), (b)... telles qu'elles apparaissent.
- Utilise la syntaxe LaTeX pour les formules mathématiques ($...$ ou $$...$$).
- Si l'exercice a des parties numérotées dans l'énoncé, assure-toi de couvrir chacune.
- NE génère PAS de correction de ta propre initiative : extrait UNIQUEMENT ce qui est présent dans le document transcrit.
- Si cet exercice n'est PAS présent dans la transcription, réponds uniquement : NON_DISPONIBLE"""

    resp = _api_call(client.chat.completions.create,
        model=STRUCT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Tu es un assistant spécialisé dans l'extraction fidèle de corrections d'examens. "
                    "Tu copies et formates ce qui existe dans le document, sans jamais inventer."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=3000,
        temperature=0,
    )

    result = resp.choices[0].message.content.strip()
    if result.upper().startswith("NON_DISPONIBLE") or "non_disponible" in result[:40].lower():
        return None
    return result


# ────────────────────────────────────────────────────────────────────────────
# 5. Chargement des exercices
# ────────────────────────────────────────────────────────────────────────────

def load_exercises(matiere: str) -> list:
    """Charge tous les exercices d'une matière depuis les JSONs sources."""
    exercises = []
    seen_ids = set()

    for json_path_str in EXERCISE_JSONS.get(matiere, []):
        p = Path(json_path_str)
        if not p.exists():
            log.warning(f"JSON introuvable : {json_path_str}")
            continue

        data = json.loads(p.read_text(encoding="utf-8"))
        exs = data if isinstance(data, list) else data.get("exercises", [])

        for ex in exs:
            eid = ex.get("id", "")
            # Filtrer par matière
            ex_mat = ex.get("matiere") or ex.get("metadata", {}).get("matiere", "")
            normalized = MATIERE_MAP.get(ex_mat.lower() if ex_mat else "", ex_mat)
            if normalized != matiere:
                continue
            if eid in seen_ids:
                continue
            seen_ids.add(eid)
            exercises.append(ex)

    log.info(f"{len(exercises)} exercices chargés pour matière={matiere}")
    return exercises


# ────────────────────────────────────────────────────────────────────────────
# 6. Main
# ────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Extrait les corrections des corrigés PDF et les lie aux exercices"
    )
    parser.add_argument("--matiere", required=True, choices=["math", "pc", "svt"],
                        help="Matière à traiter")
    parser.add_argument("--output", default=None,
                        help="Fichier JSON de sortie (défaut: corrections/corrections_{matiere}.json)")
    parser.add_argument("--cache-dir", default=None,
                        help="Dossier cache des transcriptions (défaut: .correction_cache/{matiere})")
    parser.add_argument("--dry-run", action="store_true",
                        help="Teste le matching PDF sans appeler l'API (pas de coût)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limite le nombre d'exercices à traiter (pour test)")
    args = parser.parse_args()

    output_path = Path(args.output or f"corrections/corrections_{args.matiere}.json")
    cache_dir   = Path(args.cache_dir or f".correction_cache/{args.matiere}")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Charger les résultats existants (reprise si interruption)
    if output_path.exists():
        existing = json.loads(output_path.read_text(encoding="utf-8"))
        results = {r["id"]: r for r in existing}
        log.info(f"Reprise : {len(results)} exercices déjà traités")
    else:
        results = {}
    # Charger exercices
    exercises = load_exercises(args.matiere)
    if args.limit:
        exercises = exercises[: args.limit]

    # Scanner les PDFs de corrections
    corr_pdfs = scan_corr_pdfs(args.matiere)

    if args.dry_run:
        log.info("=== MODE DRY RUN — matching seulement, pas d'appels API ===")
        found = 0
        for ex in exercises:
            meta = ex.get("metadata", {})
            year = meta.get("annee")
            filiere = meta.get("filiere", ["C"])
            if isinstance(filiere, list):
                filiere = filiere[0] if filiere else "C"
            session_str = meta.get("session", "normale")
            session_code = "sn" if session_str == "normale" else "sc"
            num = meta.get("numero_exercice", 1)

            match = find_correction_pdf(year, filiere, session_code, corr_pdfs)
            status = f"✓ {match['path'].name}" if match else "✗ pas de corrigé"
            log.info(f"  {ex.get('id', '?')} → {status}")
            if match:
                found += 1
        log.info(f"\nDry run : {found}/{len(exercises)} exercices ont un corrigé")
        return

    # Cache de transcriptions (évite de re-transcrire le même PDF)
    transcription_cache = {}

    stats = {"new": 0, "skipped": 0, "not_found": 0, "unavailable": 0}

    for i, ex in enumerate(exercises):
        eid = ex.get("id", f"ex_{i}")

        # Skip si déjà traité et non-nul
        if eid in results and results[eid].get("correction") is not None:
            stats["skipped"] += 1
            continue

        meta = ex.get("metadata", {})
        year = meta.get("annee")
        filiere = meta.get("filiere", ["C"])
        if isinstance(filiere, list):
            filiere = filiere[0] if filiere else "C"
        session_str = meta.get("session", "normale")
        session_code = "sn" if session_str == "normale" else "sc"
        num = meta.get("numero_exercice", 1)

        log.info(f"[{i+1}/{len(exercises)}] {eid}")

        # Trouver le PDF corrigé correspondant
        pdf_info = find_correction_pdf(year, filiere, session_code, corr_pdfs)
        if pdf_info is None:
            log.info(f"  ⚠ Pas de corrigé disponible pour {year} {filiere} {session_code}")
            results[eid] = {**ex, "correction": None, "correction_source": None}
            stats["not_found"] += 1
            continue

        pdf_path = pdf_info["path"]
        log.info(f"  → Corrigé : {pdf_path.name}")

        # Transcrire le PDF (utilise le cache si disponible)
        pdf_key = str(pdf_path)
        if pdf_key not in transcription_cache:
            transcription_cache[pdf_key] = transcribe_pdf(pdf_path, cache_dir)
        transcript = transcription_cache[pdf_key]

        # Extraire la correction de cet exercice
        correction = extract_correction(transcript, ex)

        if correction:
            log.info(f"  ✓ Correction extraite ({len(correction)} chars)")
            stats["new"] += 1
        else:
            log.info(f"  ✗ Exercice {num} non trouvé dans le corrigé")
            stats["unavailable"] += 1

        results[eid] = {
            **ex,
            "correction": correction,
            "correction_source": pdf_path.name if correction else None,
        }

        # Checkpoint toutes les 10 corrections
        if (i + 1) % 10 == 0:
            _save(output_path, results)
            log.info(f"  [Checkpoint] {len(results)} sauvegardés")

    # Sauvegarde finale
    _save(output_path, results)
    log.info(
        f"\n{'='*60}\n"
        f"Terminé pour matière={args.matiere}\n"
        f"  ✓ {stats['new']} corrections extraites\n"
        f"  ↩ {stats['skipped']} déjà traitées (reprise)\n"
        f"  ⚠ {stats['not_found']} sans corrigé PDF\n"
        f"  ✗ {stats['unavailable']} exercice introuvable dans le corrigé\n"
        f"  Sortie : {output_path}\n"
        f"{'='*60}"
    )


def _save(path: Path, results: dict):
    data = list(results.values())
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
