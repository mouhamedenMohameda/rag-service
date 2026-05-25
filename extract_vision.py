#!/usr/bin/env python3
"""
Extraction d'exercices du Bac mauritanien — pipeline Vision-First.

Stratégie pour < 2% d'erreur :
  1. Chaque page PDF est rendue en image haute résolution (pas d'OCR PyMuPDF).
  2. GPT-4o Vision transcrit chaque page en LaTeX propre.
  3. GPT-4o structure la transcription complète en exercices JSON.

Pourquoi ce pipeline > l'ancienne approche :
  - Les PDFs ont une couche OCR embarquée corrompue (formules perdues).
  - PyMuPDF lisait cette couche, le LLM "devinait" les formules → hallucinations.
  - GPT-4o Vision lit directement le rendu visuel de la page → fidélité réelle.

Usage :
  python3 extract_vision.py --pdf-dir /chemin/vers/annals --output exercises_extracted/bac_2025.json --years 2025
  python3 extract_vision.py --pdf-dir /chemin/vers/annals --output exercises_extracted/bac_2024.json --years 2024
  python3 extract_vision.py --pdf-dir /chemin/vers/annals --output exercises_extracted/bac_all.json
"""

from __future__ import annotations

import argparse
import base64
import json
import logging
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

import fitz  # PyMuPDF — utilisé uniquement pour le rendu image
from dotenv import load_dotenv
from openai import OpenAI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("extract_vision")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Zoom de rendu : 2.0 = 150 DPI (A4 standard ~72 DPI × 2 = 144 DPI réel)
# Suffisant pour GPT-4o, limite la taille JPEG.
RENDER_ZOOM = 2.0
JPEG_QUALITY = 85
# Limite ~20 MB pour l'API OpenAI, on reste bien en dessous avec JPEG 85
MAX_IMAGE_BYTES = 18_000_000

# Modèle pour transcription + structuration
VISION_MODEL = "gpt-4o"
STRUCT_MODEL = "gpt-4o"

# Référentiel des chapitres officiels mauritaniens
CHAPITRES_REFERENTIEL = {
    "math": [
        "Nombres complexes",
        "Suites numériques",
        "Fonctions numériques (Limites et Continuité)",
        "Fonctions Logarithmes et Exponentielles",
        "Intégration et Primitives",
        "Équations différentielles",
        "Arithmétique",
        "Similitudes planes directes",
        "Coniques",
        "Probabilités",
        "Statistiques double",
    ],
    "physique": [
        "Ondes mécaniques",
        "Cinématique et lois de Newton",
        "Mouvements dans des champs uniformes",
        "Force de Lorentz et effet Hall",
        "Induction et auto-induction électromagnétique",
        "Circuits RLC (Régime transitoire et sinusoïdal)",
        "Radioactivité et réactions nucléaires",
        "Effet photoélectrique (Dualité onde-corpuscule)",
    ],
    "chimie": [
        "Cinétique chimique",
        "Équilibres chimiques et pH des solutions aqueuses",
        "Réactions d'estérification et d'hydrolyse",
        "Chimie Organique",
    ],
    "svt": [
        "Génétique classique et humaine",
        "Immunologie",
        "Neurophysiologie",
        "Géologie",
        "Reproduction humaine et endocrinologie",
    ],
}

EXAMEN_JSON_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "exercices": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "numero": {"type": "integer"},
                    "titre": {"type": ["string", "null"]},
                    "matiere": {
                        "type": "string",
                        "enum": ["math", "physique", "chimie", "svt"],
                    },
                    "filiere": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "enonce": {"type": "string"},
                    "correction": {"type": ["string", "null"]},
                    "chapitres": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "notions_traitees": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "bareme": {"type": ["number", "null"]},
                },
                "required": [
                    "numero",
                    "titre",
                    "matiere",
                    "filiere",
                    "enonce",
                    "correction",
                    "chapitres",
                    "notions_traitees",
                    "bareme",
                ],
            },
        }
    },
    "required": ["exercices"],
}


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------


def extraire_metadonnees_chemin(path: Path) -> Dict[str, Any]:
    """Extrait matière, série, année, session et type depuis le chemin du fichier."""
    nom = path.name.lower()
    chemin = unicodedata.normalize("NFC", str(path)).lower()

    # Matière
    matiere = None
    if "math" in chemin:
        matiere = "math"
    elif "physique" in chemin or "chimie" in chemin or "pc" in chemin:
        matiere = "physique-chimie"
    elif "science" in chemin or "svt" in chemin or "sn" in chemin.split("/")[-2]:
        matiere = "svt"

    # Série
    filiere = "C"
    nom_no_space = nom.replace(" ", "")
    if "bacd" in nom_no_space or "/bac d/" in chemin:
        filiere = "D"
    elif "bacc" in nom_no_space or "/bac c/" in chemin:
        filiere = "C"

    # Année
    m = re.search(r"(20[0-2]\d)", nom)
    annee = int(m.group(1)) if m else None

    # Session
    session = "normale"
    # "sc" dans le nom = session complémentaire
    # Attention : "sc" peut aussi apparaître dans "science" — on regarde le nom de fichier
    nom_stem = path.stem.lower()
    if re.search(r"\bsc\b", nom_stem) or "complementaire" in nom_stem:
        session = "complementaire"
    elif re.search(r"\bsn\b", nom_stem) or "normale" in nom_stem:
        session = "normale"

    # Type de document
    type_doc = "sujet"
    if any(x in nom for x in ["corr", "corrig", "solution"]):
        type_doc = "corrige"

    return {
        "nom_fichier": path.name,
        "matiere_dossier": matiere,
        "filiere_defaut": filiere,
        "annee": annee,
        "session": session,
        "type_document": type_doc,
    }


def render_page_jpeg(page: "fitz.Page", zoom: float = RENDER_ZOOM) -> Tuple[str, int]:
    """Rend une page PDF en JPEG base64. Retourne (data_url, taille_bytes)."""
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat)
    if pix.alpha:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    img_bytes = pix.tobytes("jpeg", jpg_quality=JPEG_QUALITY)
    if len(img_bytes) > MAX_IMAGE_BYTES:
        # Réduire qualité si trop grand
        img_bytes = pix.tobytes("jpeg", jpg_quality=70)
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return f"data:image/jpeg;base64,{b64}", len(img_bytes)


# ---------------------------------------------------------------------------
# Étape 1 : Transcription vision par page
# ---------------------------------------------------------------------------

TRANSCRIPTION_SYSTEM = """Tu es un transcripteur expert d'annales du Baccalauréat mauritanien.
Ta tâche est de TRANSCRIRE FIDÈLEMENT le contenu de la page fournie.

Règles absolues :
- Transcris TOUT le texte visible : énoncés, questions, sous-questions, formules.
- Formules mathématiques : utilise OBLIGATOIREMENT LaTeX entre $...$ pour inline et $$...$$ pour les formules display sur leur propre ligne.
  Exemples : $\\int_0^1 f(x)\\,dx$, $z_1 = 2 + 2e^{i\\alpha}$, $P(z) = z^3 - (6+4i\\sin\\alpha)z^2$
- Équations chimiques : $H_2SO_4$, $CH_3COOH$, etc.
- Conserve la numérotation exacte des exercices et questions (Exercice 1, 2.a, 3.b.i, etc.).
- Barèmes : note-les sur leur propre ligne entre crochets, ex: [1 pt] ou [0,5 pt], JAMAIS avec \\hfill.
- N'utilise JAMAIS de commandes de mise en page LaTeX : pas de \\hfill, \\vspace, \\newpage, \\textbf, etc.
- Si la page contient un schéma, figure, graphe, courbe, micrographie, coupe anatomique, ou tout autre élément visuel :
  * Pour les SVT : décris-le de façon EXHAUSTIVE et DÉTAILLÉE entre [FIGURE: ...]. Inclus : forme générale, toutes les structures visibles et leurs noms/labels, couleurs distinctives, flèches et leur direction, légendes, relations entre les parties, échelle si présente, tout chiffre ou lettre visible dans la figure. Ne laisse aucun détail.
  * Pour les autres matières : décris-le en français entre [SCHEMA: ...] ou [TABLEAU: ...] ou [GRAPHE: ...] ou [COURBE: ...].
- Si la page est le recto d'un corrigé : transcris la correction complète avec tous les calculs.
- NE résous PAS les exercices, transcris seulement ce qui est écrit.
- NE résume PAS, NE saute PAS de contenu.
- N'enveloppe JAMAIS ta réponse dans des blocs de code markdown (``` ou ```markdown). Réponds en texte brut.
Si la page est vide ou hors-sujet, réponds uniquement : PAGE_VIDE"""


def transcrire_page(client: OpenAI, data_url: str, page_num: int, total: int) -> str:
    """Envoie une page à GPT-4o Vision pour transcription LaTeX fidèle."""
    try:
        response = client.chat.completions.create(
            model=VISION_MODEL,
            messages=[
                {"role": "system", "content": TRANSCRIPTION_SYSTEM},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Transcris fidèlement le contenu de cette page ({page_num}/{total}) :",
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": data_url, "detail": "high"},
                        },
                    ],
                },
            ],
            temperature=0.0,
            max_tokens=4096,
            timeout=120.0,
        )
        return response.choices[0].message.content or ""
    except Exception as e:
        log.error("Erreur transcription page %d : %s", page_num, e)
        return ""


def transcrire_pdf(client: OpenAI, pdf_path: Path, cache_dir: Optional[Path] = None) -> str:
    """Transcrit toutes les pages d'un PDF via vision. Utilise le cache si disponible."""
    cache_file = None
    if cache_dir:
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file = cache_dir / (pdf_path.stem + ".txt")
        if cache_file.exists():
            log.info("  ↳ [CACHE] Transcription récupérée depuis %s", cache_file.name)
            return cache_file.read_text(encoding="utf-8")

    doc = fitz.open(pdf_path)
    n_pages = len(doc)
    log.info("  ↳ Transcription vision de %d page(s)...", n_pages)

    pages_text: List[str] = []
    for i, page in enumerate(doc, start=1):
        data_url, size_bytes = render_page_jpeg(page)
        log.info("    Page %d/%d (%.1f KB) → GPT-4o Vision...", i, n_pages, size_bytes / 1024)
        text = transcrire_page(client, data_url, i, n_pages)
        if text == "PAGE_VIDE":
            log.info("    Page %d : vide, ignorée.", i)
        else:
            pages_text.append(f"=== PAGE {i}/{n_pages} ===\n{text}")
    doc.close()

    full_text = "\n\n".join(pages_text)

    if cache_file:
        cache_file.write_text(full_text, encoding="utf-8")
        log.info("  ↳ Transcription sauvegardée dans le cache : %s", cache_file.name)

    return full_text


# ---------------------------------------------------------------------------
# Étape 2 : Structuration en exercices JSON
# ---------------------------------------------------------------------------


def structurer_en_exercices(
    client: OpenAI, transcription: str, meta: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Envoie la transcription à GPT-4o pour extraction structurée des exercices."""
    ref_str = "\n".join(
        [f"  - {m.upper()} : {', '.join(chaps)}" for m, chaps in CHAPITRES_REFERENTIEL.items()]
    )

    system_prompt = f"""Tu es un expert en structuration d'annales du Baccalauréat mauritanien.
Tu reçois la transcription LaTeX fidèle d'une épreuve. Ton rôle est de l'organiser en exercices structurés.

Contexte du document :
  - Matière (dossier) : {meta['matiere_dossier']}
  - Filière par défaut : {meta['filiere_defaut']}
  - Année : {meta['annee']}
  - Session : {meta['session']}
  - Type : {meta['type_document']} (sujet = énoncé, corrige = correction)

Référentiel des chapitres officiels mauritaniens (utilise UNIQUEMENT ces chapitres) :
{ref_str}

Règles :
1. Extrais chaque exercice séparément avec son numéro, toutes ses questions et sous-questions.
2. Copie l'énoncé INTÉGRALEMENT dans le champ "enonce" — sans résumer, sans couper.
   - SUPPRIME toutes les annotations de barème inline ("1 pt", "0,5 pt", "[1 pt]", "\\hfill 0,5 pt", etc.) de l'enonce.
   - N'inclus JAMAIS de commandes LaTeX de mise en page (\\hfill, \\vspace, \\newline, \\textbf, etc.).
   - Formules : garde le LaTeX pur entre $...$ ou $$...$$, sans commandes de document.
3. Si type_document = "sujet" : "correction" = null.
4. Si type_document = "corrige" : "correction" = texte complet de la correction, sans annotations de barème.
5. Pour physique-chimie : détermine précisément "physique" ou "chimie" par exercice.
6. Le champ "filiere" est une liste : ["C"], ["D"] ou ["C", "D"].
7. "bareme" = total de points de l'exercice entier (nombre décimal, ex: 4.0).
8. Les notions_traitees sont précises (ex: "Équations diophantiennes", "Petit théorème de Fermat", pas juste "Arithmétique").
"""

    user_content = f"""Transcription de l'épreuve à structurer :

{transcription}

Réponds UNIQUEMENT avec le JSON structuré des exercices."""

    try:
        response = client.chat.completions.create(
            model=STRUCT_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            temperature=0.0,
            timeout=180.0,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "examen_schema",
                    "schema": EXAMEN_JSON_SCHEMA,
                    "strict": True,
                },
            },
        )
        content = response.choices[0].message.content
        result = json.loads(content)
        return result.get("exercices", [])
    except Exception as e:
        log.error("Erreur structuration : %s", e)
        return []


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Extraction vision-first des exercices du Bac mauritanien (< 2% d'erreur)"
    )
    parser.add_argument(
        "--pdf-dir",
        default="/Users/mohameda/Documents/Bac/drive_archive/annals",
        help="Dossier racine contenant les PDFs",
    )
    parser.add_argument(
        "--output",
        default="exercises_extracted/bac_exercises.json",
        help="Fichier JSON de sortie",
    )
    parser.add_argument(
        "--years",
        help="Années à traiter, séparées par virgule (ex: 2024,2025)",
    )
    parser.add_argument(
        "--subjects",
        help="Matières à filtrer : math, pc, svt (ex: math,svt)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limiter le nombre de PDFs traités",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Désactive le cache des transcriptions",
    )
    parser.add_argument(
        "--transcription-only",
        action="store_true",
        help="Arrête après la transcription (sans structuration JSON)",
    )
    parser.add_argument(
        "--sujet-only",
        action="store_true",
        default=True,
        help="Ignore les corrigés, traite uniquement les sujets (défaut: True)",
    )
    parser.add_argument(
        "--include-corrections",
        action="store_true",
        help="Inclure aussi les corrigés (désactive --sujet-only)",
    )
    args = parser.parse_args()
    if args.include_corrections:
        args.sujet_only = False

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        log.error("OPENAI_API_KEY non défini dans l'environnement ou .env")
        return 1

    client = OpenAI(api_key=api_key)

    pdf_dir = Path(args.pdf_dir).resolve()
    if not pdf_dir.exists():
        log.error("Dossier PDF introuvable : %s", pdf_dir)
        return 1

    output_file = Path(args.output).resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Cache des transcriptions vision (évite de repayer le même PDF)
    cache_dir = None if args.no_cache else output_file.parent / ".transcription_cache"

    # Chargement de l'existant (checkpoint)
    reconciled: Dict[str, Any] = {}
    processed_files: set = set()
    if output_file.exists():
        try:
            with open(output_file, encoding="utf-8") as f:
                for ex in json.load(f):
                    reconciled[ex["id"]] = ex
                    md = ex.get("metadata", {})
                    for k in ("source_sujet", "source_corrige"):
                        if md.get(k):
                            processed_files.add(md[k])
            log.info(
                "Chargé %d exercices existants (%d fichiers déjà traités).",
                len(reconciled),
                len(processed_files),
            )
        except Exception as e:
            log.warning("Impossible de lire le fichier existant : %s", e)

    # Parcours des PDFs
    pdf_files = sorted(pdf_dir.rglob("*.pdf"))
    log.info("Trouvé %d PDFs sous %s", len(pdf_files), pdf_dir)

    # Filtres
    if args.years:
        target_years = {int(y.strip()) for y in args.years.split(",") if y.strip().isdigit()}
    else:
        target_years = None

    if args.subjects:
        target_subjects = {s.strip().lower() for s in args.subjects.split(",") if s.strip()}
    else:
        target_subjects = None

    if args.limit:
        pdf_files = pdf_files[: args.limit]

    processed_count = 0
    for idx, pdf_path in enumerate(pdf_files, start=1):
        meta = extraire_metadonnees_chemin(pdf_path)

        if not meta["annee"]:
            log.debug("[%d/%d] skip (année non détectée) : %s", idx, len(pdf_files), pdf_path.name)
            continue

        if target_years and meta["annee"] not in target_years:
            continue

        if target_subjects:
            mat = meta["matiere_dossier"] or ""
            mat_key = "pc" if mat == "physique-chimie" else mat
            if mat_key not in target_subjects:
                continue

        if args.sujet_only and meta["type_document"] == "corrige":
            log.debug("[%d/%d] skip (corrigé, --sujet-only actif) : %s", idx, len(pdf_files), pdf_path.name)
            continue

        if pdf_path.name in processed_files:
            log.info("[%d/%d] [SKIP] %s (déjà traité)", idx, len(pdf_files), pdf_path.name)
            continue

        log.info(
            "[%d/%d] Traitement : %s | matière=%s | %s | %s | %s",
            idx,
            len(pdf_files),
            pdf_path.name,
            meta["matiere_dossier"],
            meta["annee"],
            meta["session"],
            meta["type_document"],
        )

        # --- Étape 1 : Transcription vision ---
        transcription = transcrire_pdf(client, pdf_path, cache_dir=cache_dir)
        if not transcription.strip():
            log.warning("  ↳ Transcription vide, PDF ignoré.")
            continue

        if args.transcription_only:
            print(f"\n{'='*60}\n{pdf_path.name}\n{'='*60}\n{transcription}\n")
            continue

        # --- Étape 2 : Structuration ---
        log.info("  ↳ Structuration en exercices...")
        exercices = structurer_en_exercices(client, transcription, meta)
        if not exercices:
            log.warning("  ↳ Aucun exercice extrait.")
            continue

        log.info("  ↳ %d exercices extraits.", len(exercices))
        processed_count += 1
        new_count = 0

        for ex in exercices:
            annee = ex.get("annee") or meta["annee"]
            session = ex.get("session") or meta["session"]
            filiere_list = ex.get("filiere") or [meta["filiere_defaut"]]
            filiere_str = "+".join(sorted(str(f) for f in filiere_list))
            matiere = ex.get("matiere", meta["matiere_dossier"] or "unknown")
            numero = ex.get("numero", 0)

            key = f"{matiere}_{annee}_{session}_{filiere_str}_ex{numero}"

            enonce = (ex.get("enonce") or "").strip()
            correction = (ex.get("correction") or "").strip() or None

            if key not in reconciled:
                reconciled[key] = {
                    "id": key,
                    "metadata": {
                        "matiere": matiere,
                        "filiere": filiere_list,
                        "annee": annee,
                        "session": session,
                        "numero_exercice": numero,
                        "titre": ex.get("titre"),
                        "chapitres": ex.get("chapitres", []),
                        "notions_traitees": ex.get("notions_traitees", []),
                        "bareme": ex.get("bareme"),
                    },
                    "enonce": enonce,
                    "correction": correction,
                }
                new_count += 1
            else:
                existing = reconciled[key]
                if enonce and len(enonce) > len(existing.get("enonce") or ""):
                    existing["enonce"] = enonce
                if correction and len(correction) > len(existing.get("correction") or ""):
                    existing["correction"] = correction
                existing_notions = set(existing["metadata"].get("notions_traitees", []))
                existing_notions.update(ex.get("notions_traitees", []))
                existing["metadata"]["notions_traitees"] = list(existing_notions)

            # Source
            src_key = "source_sujet" if meta["type_document"] == "sujet" else "source_corrige"
            reconciled[key]["metadata"][src_key] = meta["nom_fichier"]

        # Sauvegarde après chaque fichier (checkpoint)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(list(reconciled.values()), f, ensure_ascii=False, indent=2)
        log.info(
            "  ↳ Sauvegardé : %d exercices au total (%d nouveaux ce fichier)",
            len(reconciled),
            new_count,
        )

    if not args.transcription_only:
        log.info(
            "Terminé. %d PDFs traités → %d exercices uniques dans %s",
            processed_count,
            len(reconciled),
            output_file,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
