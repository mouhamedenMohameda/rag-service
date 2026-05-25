#!/usr/bin/env python3
"""Extracteur d'exercices depuis un recueil scanné (1 JPEG par page) → JSON.

Pipeline : pour chaque session déclarée dans la config, OCR via Groq Vision les
pages d'énoncé et de corrigé, puis split par "Exercice N". Le résultat est un
JSON liste compatible avec le schéma de `json_bac.json`.

Réutilisable : on lui passe une config JSON décrivant le recueil + la table
des matières (mapping session → pages). Cf. configs/recueil_math_c_2007sc_2012sc.json.

Usage :
    cd rag-service
    GROQ_API_KEY=... .venv/bin/python scripts/extract_recueil_exos.py \\
        --config configs/recueil_math_c_2007sc_2012sc.json \\
        --output exo_extracted/math_c_2007sc_2012sc.json

Options utiles :
    --only-session "2012:Normale"   Limiter à une session (debug)
    --skip-corrige                  N'extrait que les énoncés (rapide)
    --dry-run                       Liste les pages qu'on ouvrirait, sans appel API
"""

from __future__ import annotations

import argparse
import base64
import io
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from PIL import Image

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("extract-recueil")

VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
MAX_TOKENS = 2048
MAX_IMAGE_BYTES = 3_500_000
JPEG_QUALITY = 80
RESIZE_STEPS = [1.0, 0.85, 0.70, 0.55]  # facteurs si l'image source dépasse la limite

SESSION_CODES = {"Normale": "sn", "Complémentaire": "sc"}

OCR_PROMPT = """MODE STRICT — TRANSCRIPTION LITTÉRALE D'UNE IMAGE.

Tu es un OCR pour les annales du Baccalauréat C mauritanien (Mathématiques,
Sciences naturelles). Règle absolue : tu transcris UNIQUEMENT ce qui est
physiquement écrit sur l'image. Tu ne résouds RIEN. Tu ne calcules RIEN.
Tu ne complètes RIEN. Tu ne devines RIEN.

Si la page montre "Calculer P(2i)" sans le résultat → tu écris exactement
"Calculer P(2i)", sans rajouter le calcul. Si la question demande un
développement absent de l'image, tu T'ARRÊTES à la question.

Transcris EXHAUSTIVEMENT le contenu de cette page :
- Énoncés des exercices, questions, sous-questions.
- Corrigés : raisonnements, calculs intermédiaires, conclusions.
- Définitions, théorèmes, résultats encadrés.

Règles de format :
- Formules mathématiques en LaTeX entre $...$ (ex : $\\int_0^1 f(x)\\,dx$).
- Vecteurs : $\\vec{AB}$. Ensembles : $\\mathbb{R}$, $\\mathbb{C}$.
- Schémas / figures : décris-les en français brièvement (axes, légendes, points).
- Tableaux de variation : reconstruis-les en texte structuré.
- Conserve la structure et la numérotation (1., 2.a, 3.1, etc.).
- Indique chaque nouvel exercice par une ligne commençant par le numéro RÉEL,
  par ex. "Exercice 1 (4 points)", "Exercice 2", "Problème (10 points)".
  N'écris JAMAIS "Exercice N" littéral si tu ne connais pas le numéro.

Ne réponds PAS aux exercices, transcris seulement.
Si la page est en-tête / page de garde / table des matières / vide,
réponds exactement : `PAGE_VIDE`.

Si le texte est MANUSCRIT : transcris au mieux. Pour les passages illisibles,
mets [???] (3 caractères) sans inventer. Conserve quand même la structure
visible (numéros de questions, encadrés, etc.)."""


# --------------------------------------------------------------------------- #
# Groq client                                                                  #
# --------------------------------------------------------------------------- #

_groq_client = None


def get_groq_client():
    global _groq_client
    if _groq_client is not None:
        return _groq_client
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        log.error("GROQ_API_KEY manquante (charge .env ou exporte la variable)")
        sys.exit(2)
    from groq import Groq

    _groq_client = Groq(api_key=key)
    return _groq_client


def _is_too_large_error(err: Exception) -> bool:
    s = str(err).lower()
    return any(t in s for t in ("413", "payload too large", "request_too_large", "too_large"))


# --------------------------------------------------------------------------- #
# Image → data URL (avec downsize si nécessaire)                              #
# --------------------------------------------------------------------------- #


def jpeg_to_data_url(path: Path, scale: float = 1.0) -> tuple[str, int]:
    """Charge un JPEG, applique un éventuel resize, recompresse JPEG q80."""
    with Image.open(path) as im:
        im = im.convert("RGB")
        if scale != 1.0:
            new_size = (max(1, int(im.width * scale)), max(1, int(im.height * scale)))
            im = im.resize(new_size, Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
    raw = buf.getvalue()
    b64 = base64.b64encode(raw).decode("ascii")
    return f"data:image/jpeg;base64,{b64}", len(raw)


def ocr_jpeg(path: Path) -> Optional[str]:
    """Renvoie le texte OCR'é (markdown/LaTeX) ou None si page vide / échec."""
    client = get_groq_client()
    last_err: Optional[Exception] = None

    for scale in RESIZE_STEPS:
        data_url, size = jpeg_to_data_url(path, scale=scale)
        if size > MAX_IMAGE_BYTES:
            log.debug("  %s : %d B à scale=%.2f, downsize…", path.name, size, scale)
            continue

        for attempt in range(3):
            try:
                completion = client.chat.completions.create(
                    model=VISION_MODEL,
                    temperature=0,
                    max_tokens=MAX_TOKENS,
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": OCR_PROMPT},
                                {"type": "image_url", "image_url": {"url": data_url}},
                            ],
                        }
                    ],
                )
                text = (completion.choices[0].message.content or "").strip()
                if not text or text == "PAGE_VIDE":
                    return None
                if len(text) < 40:
                    return None
                return text
            except Exception as e:
                last_err = e
                if _is_too_large_error(e):
                    log.info("  413 à scale=%.2f, downsize", scale)
                    break
                wait = 2 ** attempt
                log.warning("  OCR failed attempt=%d : %s — retry in %ds", attempt + 1, e, wait)
                time.sleep(wait)

    log.error("  Échec OCR définitif sur %s : %s", path.name, last_err)
    return None


# --------------------------------------------------------------------------- #
# Split en exercices                                                           #
# --------------------------------------------------------------------------- #

# Capture les en-têtes d'épreuve : "Exercice N", "Exercice n°N", "Problème N"
# ou "Problème" (sans numéro). Tolère **, ##, casse libre.
# Si "Exercice" apparaît sans chiffre derrière (ex: "Exercice N" littéral émis
# par erreur par l'OCR), on l'ignore via le lookahead obligatoire `\s+\d+`.
EXO_HEADER_RE = re.compile(
    r"""^\s*(?:\#{1,4}\s*)?(?:\*+)?\s*
    (?:
        (?:EXERCICE|Exercice|exercice)\s+(?:n[°o]\s*)?(?P<num1>\d+)
      |
        (?:PROBL[ÈE]ME|Probl[èe]me|probl[èe]me)(?:\s+(?:n[°o]\s*)?(?P<num2>\d+))?
    )
    \b[^\n]*$
    """,
    re.VERBOSE | re.MULTILINE,
)


def split_into_exercises(full_text: str) -> list[tuple[int, str]]:
    """Découpe un bloc texte en (numero, body) ordonné.

    Règles :
    - "Exercice N"               → numéro N (chiffre obligatoire).
    - "Exercice N" littéral      → ignoré (pas de chiffre, ne matche pas).
    - "Problème N"               → numéro N.
    - "Problème" sans numéro     → auto = (dernier numéro vu) + 1.
    - Mêmes numéros répétés (continuation page suivante) → fusionnés.

    Anomalies non détectables via regex (à patcher en post-traitement) :
    - Exo dont la suite démarre sur une nouvelle page : Groq peut ré-émettre
      "Exercice N" littéral (placeholder) — ce regex l'ignore, mais le body
      est attaché à l'exo précédent. Vérifier le découpage manuellement si
      un exo paraît artificiellement long ou court.
    - Problème en plusieurs parties (Partie A, Partie B) : si l'OCR n'écrit
      "Problème" qu'une fois, OK. Sinon, plusieurs entrées séparées sont
      créées — fusionner via un script de patch.
    """
    matches = list(EXO_HEADER_RE.finditer(full_text))
    if not matches:
        return []
    fragments: dict[int, list[str]] = {}
    order: list[int] = []
    last_num: Optional[int] = None
    for i, m in enumerate(matches):
        raw = m.group("num1") or m.group("num2")
        if raw is not None:
            num = int(raw)
        else:
            num = (last_num + 1) if last_num is not None else (max(fragments, default=0) + 1)
        last_num = num
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        body = full_text[start:end].strip()
        if num not in fragments:
            fragments[num] = []
            order.append(num)
        fragments[num].append(body)
    return [(n, "\n\n".join(fragments[n])) for n in order]


# --------------------------------------------------------------------------- #
# Per-session extraction                                                       #
# --------------------------------------------------------------------------- #


@dataclass
class Session:
    annee: int
    session: str
    pages_enonce: tuple[int, int]
    pages_corrige: tuple[int, int]
    # Overrides optionnels (utiles quand énoncé et corrigé sont dans des
    # dossiers/PDFs séparés, ou quand chaque session a son propre PDF).
    enonce_dir: Optional[str] = None
    enonce_pattern: Optional[str] = None
    corrige_dir: Optional[str] = None
    corrige_pattern: Optional[str] = None


def page_range(spec: list[int]) -> list[int]:
    """[5, 7] → [5,6,7] ; [9] → [9]."""
    if len(spec) == 1:
        return [spec[0]]
    a, b = spec[0], spec[1]
    return list(range(a, b + 1))


def ocr_pages(image_dir: Path, pattern: str, pages: list[int]) -> str:
    chunks: list[str] = []
    for p in pages:
        path = image_dir / pattern.format(page=p)
        if not path.exists():
            log.warning("  page %d : fichier introuvable %s", p, path.name)
            continue
        log.info("  OCR page %d (%s)", p, path.name)
        txt = ocr_jpeg(path)
        if txt:
            chunks.append(f"<!-- page {p} -->\n{txt}")
        else:
            log.warning("  page %d : OCR vide/échec", p)
    return "\n\n".join(chunks)


def make_exo_id(filiere_id: str, annee: int, session: str, matiere_id: str, n: int) -> str:
    code = SESSION_CODES.get(session, "sn" if session.lower().startswith("n") else "sc")
    return f"bac-{filiere_id.lower()}-{annee}-{code}-{matiere_id}-ex{n}"


def process_session(
    cfg: dict,
    sess: Session,
    skip_corrige: bool,
    dry_run: bool,
) -> list[dict]:
    global_dir = cfg.get("image_dir")
    global_pat = cfg.get("image_pattern")
    enonce_dir = Path(sess.enonce_dir or global_dir)
    enonce_pat = sess.enonce_pattern or global_pat
    corrige_dir = Path(sess.corrige_dir or global_dir)
    corrige_pat = sess.corrige_pattern or global_pat
    enonce_pages = page_range(list(sess.pages_enonce)) if sess.pages_enonce else []
    corrige_pages = page_range(list(sess.pages_corrige)) if sess.pages_corrige else []

    log.info("Session %d %s — énoncé p%s | corrigé p%s",
             sess.annee, sess.session,
             enonce_pages or "(skip)",
             corrige_pages if not skip_corrige else "(skip)")

    if dry_run:
        return []

    enonce_full = ocr_pages(enonce_dir, enonce_pat, enonce_pages) if enonce_pages else ""
    corrige_full = "" if skip_corrige else (
        ocr_pages(corrige_dir, corrige_pat, corrige_pages) if corrige_pages else ""
    )

    enonces = split_into_exercises(enonce_full) if enonce_full else []
    corriges = dict(split_into_exercises(corrige_full)) if corrige_full else {}

    # Cas 1 : pas d'énoncé extrait mais on a des corrigés découpés.
    # → On itère sur les numéros du corrigé et on produit des entrées
    #   avec ennonce_complet vide (le merger préservera l'énoncé existant).
    if not enonces and corriges:
        log.info("  Aucun énoncé OCR — itération sur les numéros du corrigé.")
        enonces = [(n, "") for n in sorted(corriges)]

    if not enonces:
        log.error("  Aucun 'Exercice N' détecté ni en énoncé ni en corrigé — bloc brut.")
        return [{
            "id": make_exo_id(cfg["filiere_id"], sess.annee, sess.session, cfg["matiere_id"], 0),
            "matiere_id": cfg["matiere_id"],
            "matiere": cfg["matiere_label"],
            "filiere_id": cfg["filiere_id"],
            "filiere": cfg["filiere_label"],
            "annee": sess.annee,
            "session": sess.session,
            "fichier": cfg["source_pdf_name"],
            "exercice_numero": 0,
            "ennonce_complet": enonce_full,
            "correction": corrige_full,
            "_warning": "split par exercice échoué — réviser manuellement",
            "_source_pages_enonce": enonce_pages,
            "_source_pages_corrige": corrige_pages if not skip_corrige else [],
        }]

    out: list[dict] = []
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for num, body in enonces:
        out.append({
            "id": make_exo_id(cfg["filiere_id"], sess.annee, sess.session, cfg["matiere_id"], num),
            "matiere_id": cfg["matiere_id"],
            "matiere": cfg["matiere_label"],
            "filiere_id": cfg["filiere_id"],
            "filiere": cfg["filiere_label"],
            "annee": sess.annee,
            "session": sess.session,
            "fichier": cfg["source_pdf_name"],
            "exercice_numero": num,
            "ennonce_complet": body,
            "correction": corriges.get(num, ""),
            "_source_pages_enonce": enonce_pages,
            "_source_pages_corrige": corrige_pages if not skip_corrige else [],
            "_extracted_at": now,
        })
    log.info("  → %d exercices extraits (%s)", len(out),
             ", ".join(f"n°{n}" for n, _ in enonces))
    return out


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #


def main() -> int:
    load_dotenv()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--config", required=True, help="JSON config décrivant le recueil")
    ap.add_argument("--output", required=True, help="Chemin du JSON de sortie")
    ap.add_argument("--only-session", help="Filtre 'ANNEE:Session' (ex: 2012:Normale)")
    ap.add_argument("--skip-corrige", action="store_true", help="Extraire seulement les énoncés")
    ap.add_argument("--dry-run", action="store_true", help="Liste les pages, pas d'appel API")
    args = ap.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8"))

    sessions = [Session(**s) for s in cfg["sessions"]]
    if args.only_session:
        annee, sess = args.only_session.split(":", 1)
        sessions = [s for s in sessions if s.annee == int(annee) and s.session == sess]
        if not sessions:
            log.error("Aucune session ne matche %s", args.only_session)
            return 1

    log.info("Recueil : %s — %d session(s) à traiter", cfg["source_pdf_name"], len(sessions))
    all_exos: list[dict] = []
    for s in sessions:
        try:
            all_exos.extend(process_session(cfg, s, args.skip_corrige, args.dry_run))
        except Exception as e:
            log.exception("Échec session %s %s : %s", s.annee, s.session, e)

    if args.dry_run:
        log.info("Dry run terminé.")
        return 0

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(all_exos, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info("✓ %d exercices écrits dans %s", len(all_exos), out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
