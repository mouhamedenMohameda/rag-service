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
RENDER_ZOOM = 2  # 2x = ~144 DPI, suffisant pour reconnaissance

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


def render_page_to_data_url(page: "fitz.Page") -> str:
    """Render une page PDF en PNG base64 (data URL) pour envoi à Vision API."""
    pix = page.get_pixmap(matrix=fitz.Matrix(RENDER_ZOOM, RENDER_ZOOM))
    img_bytes = pix.tobytes("png")
    b64 = base64.b64encode(img_bytes).decode("ascii")
    return f"data:image/png;base64,{b64}"


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


def ocr_page_via_vision(page: "fitz.Page") -> Optional[str]:
    """Tente d'extraire le texte d'une page scannée via Groq Vision.

    Retourne le texte transcrit, ou None si :
    - le client Groq n'est pas dispo (pas de clé)
    - l'API a renvoyé PAGE_VIDE
    - une erreur réseau est survenue (après retry)
    """
    client = get_groq_client()
    if client is None:
        return None

    data_url = render_page_to_data_url(page)

    last_err: Optional[Exception] = None
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
                # Probablement une réponse vide ou un message d'erreur model-side
                return None
            return text
        except Exception as e:  # pragma: no cover (réseau)
            last_err = e
            wait = 2 ** attempt
            log.warning("Vision OCR failed (attempt %d) : %s — retry in %ds", attempt + 1, e, wait)
            time.sleep(wait)
    log.error("Vision OCR définitivement échoué : %s", last_err)
    return None
