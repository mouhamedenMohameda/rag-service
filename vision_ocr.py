"""OCR Vision via Groq (llama-4-scout) pour les pages scannées des PDFs.

Activé uniquement si GROQ_API_KEY est défini dans l'environnement. Sinon,
les fonctions renvoient None et l'appelant skip silencieusement la page.
"""

from __future__ import annotations

import base64
import logging
import os
import time
from typing import Optional

import fitz  # PyMuPDF

log = logging.getLogger("vision-ocr")

VISION_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
MAX_TOKENS = 1200
# Groq Vision a un plafond ~4 MB par image. Avec PNG zoom 2x on dépasse
# régulièrement sur les pages denses, donc on rend en JPEG qualité 80.
# Tentatives en cascade : 1.5x → 1.0x → 0.75x si trop grand.
RENDER_ZOOMS = [1.5, 1.0, 0.75]
JPEG_QUALITY = 80
MAX_IMAGE_BYTES = 3_500_000  # marge sous la limite Groq 4 MB

_groq_client = None


def get_groq_client():
    """Initialise le client Groq paresseusement. Renvoie None si pas de clé."""
    global _groq_client
    if _groq_client is not None:
        return _groq_client
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        return None
    try:
        from groq import Groq

        _groq_client = Groq(api_key=key)
        return _groq_client
    except ImportError:
        log.warning("Package 'groq' non installé — OCR Vision désactivé")
        return None


def render_page_to_data_url(page: "fitz.Page", zoom: float = 1.5) -> tuple[str, int]:
    """Render une page PDF en JPEG base64 (data URL). Retourne (url, raw_size).

    JPEG 80 est typiquement 5-10× plus léger qu'un PNG équivalent et reste
    largement lisible pour de l'OCR de texte imprimé/manuscrit.
    """
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    # Supprime le canal alpha si présent (JPEG ne le supporte pas)
    if pix.alpha:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    img_bytes = pix.tobytes("jpeg", jpg_quality=JPEG_QUALITY)
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return f"data:image/jpeg;base64,{b64}", len(img_bytes)


OCR_PROMPT = """Tu es un OCR spécialisé pour les annales du Baccalauréat C mauritanien
(corrigés Bac C / Bac D, séries Mathématiques et Sciences naturelles).

Transcris EXHAUSTIVEMENT le contenu de cette page :
- Énoncés des exercices, questions, sous-questions.
- Corrigés : raisonnements, calculs intermédiaires, conclusions.
- Définitions, théorèmes, résultats encadrés.

Règles de format :
- Formules mathématiques en LaTeX entre $...$ (ex : $\\int_0^1 f(x)\\,dx$).
- Équations chimiques : $H_2O$, $CH_3-COOH$.
- Schémas / tableaux : décris-les en français brièvement (axes, légendes).
- Conserve la structure (numérotation : 1., 2.a, 3.1, etc.).

Ne réponds PAS aux exercices, transcris seulement.
Si la page est vide, illisible ou ne contient pas de contenu pédagogique,
réponds exactement : `PAGE_VIDE`."""


def _is_too_large_error(err: Exception) -> bool:
    """Détecte un 413 (Payload Too Large) dans une erreur Groq SDK."""
    s = str(err).lower()
    return (
        "413" in s
        or "payload too large" in s
        or "request entity too large" in s
        or "request_too_large" in s
    )


def ocr_page_via_vision(page: "fitz.Page") -> Optional[str]:
    """Tente d'extraire le texte d'une page scannée via Groq Vision.

    Retourne le texte transcrit, ou None si :
    - le client Groq n'est pas dispo (pas de clé)
    - l'API a renvoyé PAGE_VIDE
    - une erreur réseau persistante (après retries + downgrades de zoom)
    """
    client = get_groq_client()
    if client is None:
        return None

    last_err: Optional[Exception] = None

    # Cascade : essaie zoom 1.5 → 1.0 → 0.75 si 413. Sur chaque zoom, 3 retries.
    for zoom in RENDER_ZOOMS:
        data_url, raw_size = render_page_to_data_url(page, zoom=zoom)
        # Pre-check : si déjà trop gros même avant envoi, downgrade direct
        if raw_size > MAX_IMAGE_BYTES:
            log.debug("Image trop grosse (%d bytes) à zoom %.2f, downgrade", raw_size, zoom)
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
            except Exception as e:  # pragma: no cover (réseau)
                last_err = e
                if _is_too_large_error(e):
                    log.info("413 à zoom %.2f, downgrade au zoom suivant", zoom)
                    break  # sors de la boucle retries → passe au prochain zoom
                wait = 2 ** attempt
                log.warning("Vision OCR failed (attempt %d) : %s — retry in %ds", attempt + 1, e, wait)
                time.sleep(wait)

    log.error("Vision OCR définitivement échoué (tous zooms) : %s", last_err)
    return None
