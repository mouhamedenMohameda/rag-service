"""Admin Courses API — génération et édition de cours par notion.

Source de vérité :
  - ``/opt/rag-service/notions_registry.json`` : catalogue canonique des notions
  - ``/opt/rag-service/notions_map.json``      : notion_id → exos liés
  - ``/opt/rag-service/json_bac.json``         : énoncés des exos (lus via AdminStore)
  - ``/opt/rag-service/cours.json``            : cours générés/édités (NOUVEAU)

Cours par notion (1 cours unique par notion, indépendant de la filière). Format
Markdown + LaTeX inline ($...$, $$...$$, \\ce{...}), compatible avec le
composant ``MathText`` du frontend (KaTeX + mhchem).

Routes :
  - GET   /admin/courses/notions                  Liste notions filtrables
  - GET   /admin/courses/{notion_id}              Détail cours
  - POST  /admin/courses/{notion_id}/generate     Génère via Groq (idempotent
                                                  si force=False et déjà présent)
  - PATCH /admin/courses/{notion_id}              Édition manuelle
  - DELETE /admin/courses/{notion_id}             Supprime (à régénérer)

Auth : ``X-Api-Key`` = S2S key, comme le reste de l'admin.
"""
from __future__ import annotations

import json
import logging
import os
import shutil
import threading
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Header, Query
from pydantic import BaseModel

log = logging.getLogger("rag-admin-courses")

_lock = threading.RLock()


# ─── Store cours.json ────────────────────────────────────────────────────────


class CoursesStore:
    """JSON-file-as-database pour les cours générés.

    Schema : ``{ notion_id: CourseEntry }`` où ``CourseEntry`` =
        - content        : str (Markdown + LaTeX)
        - model          : str (ex. 'llama-3.3-70b-versatile')
        - generated_at   : str (ISO datetime)
        - edited_at      : str | None
        - validated_by_admin : bool
        - notion_label   : str (snapshot du label au moment de génération)
        - context_exo_ids: list[str] (snapshot des exos utilisés comme contexte)
    """

    def __init__(self, path: Path, backup_dir: Path, max_backups: int = 20):
        self.path = path
        self.backup_dir = backup_dir
        self.max_backups = max_backups
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def load(self) -> dict[str, dict]:
        if not self.path.exists():
            return {}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            log.error("cours.json corrompu (%s)", e)
            raise HTTPException(500, f"cours.json corrompu : {e}. Voir backups.")

    def save(self, data: dict[str, dict]) -> None:
        with _lock:
            if self.path.exists():
                stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                shutil.copy2(self.path, self.backup_dir / f"cours-{stamp}.json")
                backups = sorted(self.backup_dir.glob("cours-*.json"))
                for old in backups[: -self.max_backups]:
                    old.unlink(missing_ok=True)
            tmp = self.path.with_suffix(".json.tmp")
            tmp.write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            tmp.replace(self.path)


# ─── Lecture du registry + map (read-only depuis l'API) ──────────────────────


def _load_registry(root: Path) -> dict:
    p = root / "notions_registry.json"
    if not p.exists():
        raise HTTPException(500, "notions_registry.json absent.")
    return json.loads(p.read_text(encoding="utf-8"))


def _load_map(root: Path) -> dict:
    p = root / "notions_map.json"
    if not p.exists():
        raise HTTPException(500, "notions_map.json absent.")
    return json.loads(p.read_text(encoding="utf-8"))


# ─── Schemas Pydantic ────────────────────────────────────────────────────────


class CourseUpdate(BaseModel):
    content: Optional[str] = None
    validated_by_admin: Optional[bool] = None


class CourseGenerateRequest(BaseModel):
    force: bool = False  # si True, écrase un cours existant
    max_context_exos: int = 5  # nb d'exos à passer au LLM comme contexte


# ─── Prompt système pour la génération ──────────────────────────────────────


COURSE_SYSTEM = """Tu es un professeur expert du Bac mauritanien (séries C et D).
On te donne une NOTION atomique du programme et 3 à 5 ÉNONCÉS d'exercices Bac
qui la mettent en jeu. Tu rédiges un cours **structuré et pédagogique**,
adapté à un élève de terminale qui révise.

STRUCTURE EXIGÉE — utilise EXACTEMENT ces 6 sections, dans cet ordre :

## 1. Notions de base
Définitions et rappels indispensables. Court (3-6 lignes).

## 2. Propriétés essentielles
Théorèmes, formules clés, relations à savoir par cœur. Présente sous forme
de liste à puces ou de blocs « Propriété : ... ». Numérote si utile.

## 3. Méthode de résolution
Étapes type à suivre face à un exercice de cette notion. Style :
« 1. Identifier ... ; 2. Calculer ... ; 3. Vérifier ... ».

## 4. Exemple type Bac
**Choisis 1 des énoncés fournis** et résous-le étape par étape, en explicitant
chaque étape de la méthode ci-dessus. Énonce avant de résoudre.

## 5. Pièges fréquents
3 à 6 erreurs typiques que les élèves font sur cette notion, sous forme de
liste « ❌ Erreur : ... → ✅ Correct : ... » (sans emoji si tu préfères).

## 6. Pour aller plus loin
Une ou deux remarques avancées (lien avec d'autres notions, cas particuliers,
extensions hors-programme mais culturellement utiles).

RÈGLES DE FORMAT :
- Markdown avec LaTeX inline ``$...$`` et bloc ``$$...$$``.
- Équations chimiques avec ``\\ce{...}`` (PC/SVT uniquement).
- Pas de ``\\documentclass``, pas de section ``# Cours sur ...`` redondante.
- Le titre principal sera ajouté par l'UI. Tu commences DIRECTEMENT par ``## 1. Notions de base``.
- Pas de phrase d'intro ni de conclusion en dehors de ces 6 sections.
- Le ton doit être direct, pas de blabla. L'élève est en révision intense.

Réponds uniquement en Markdown brut, sans entourer d'``` ```.
"""


def _build_user_prompt(
    label: str,
    matiere_id: str,
    chapitre: str,
    exos_context: list[dict],
) -> str:
    """Construit le user prompt avec contexte d'exos."""
    lines = [
        f"NOTION : « {label} »",
        f"Matière : {matiere_id}",
        f"Chapitre : {chapitre or '(non spécifié)'}",
        "",
        f"ÉNONCÉS D'EXERCICES Bac mettant en jeu cette notion ({len(exos_context)} exos) :",
        "",
    ]
    for i, e in enumerate(exos_context, 1):
        ennonce = (e.get("ennonce_complet") or "").strip()
        # Tronquer si trop long pour rester dans la fenêtre contexte
        if len(ennonce) > 1500:
            ennonce = ennonce[:1500] + "…"
        lines.append(f"--- Exo {i} ({e['id']}, Bac {e.get('annee')} série {e.get('filiere_id')}, "
                     f"session {e.get('session', '?')}) ---")
        lines.append(ennonce)
        lines.append("")
    return "\n".join(lines)


def _call_groq_for_course(
    user_prompt: str,
    model: str = "llama-3.3-70b-versatile",
) -> str:
    """Appelle Groq pour générer le cours. Renvoie le markdown brut."""
    try:
        from groq import Groq
    except ImportError as e:
        raise HTTPException(500, f"Package 'groq' manquant : {e}")
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise HTTPException(500, "GROQ_API_KEY absente sur le serveur.")

    client = Groq(api_key=api_key)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": COURSE_SYSTEM},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4,
        max_tokens=3500,
    )
    content = (resp.choices[0].message.content or "").strip()
    if not content:
        raise HTTPException(502, "Groq a renvoyé une réponse vide.")
    # Nettoyer un éventuel ``` autour
    if content.startswith("```"):
        # retire la 1re ligne (```markdown ou ```)
        content = content.split("\n", 1)[1] if "\n" in content else content[3:]
        if content.rstrip().endswith("```"):
            content = content.rstrip()[:-3].rstrip()
    return content


# ─── Router ─────────────────────────────────────────────────────────────────


def build_courses_router(
    json_bac_store,  # AdminStore (lecture des énoncés)
    courses_store: CoursesStore,
    root: Path,
    api_key: str,
) -> APIRouter:
    router = APIRouter(prefix="/admin/courses", tags=["admin-courses"])

    def require_admin(x_api_key: Optional[str] = Header(default=None)) -> None:
        if not x_api_key or x_api_key != api_key:
            raise HTTPException(401, "Admin auth requise.")

    # ── Liste des notions (avec stats + has_course) ─────────────────────────
    @router.get("/notions", dependencies=[Depends(require_admin)])
    def list_notions(
        matiere: Optional[str] = Query(None, description="math|pc|svt"),
        filiere: Optional[str] = Query(None, description="C|D ; filtre les "
                                       "notions qui ont au moins 1 exo de cette filière"),
        min_exos: int = Query(1, ge=1, description="ne montrer que les notions "
                              "liées à ≥N exos"),
        has_course: Optional[bool] = Query(None, description="true=déjà généré, "
                                           "false=à générer, None=tous"),
        q: Optional[str] = Query(None, description="recherche dans le label"),
        sort: str = Query("nb_exos_desc",
                          description="nb_exos_desc|nb_exos_asc|label|notion_id"),
        limit: int = Query(200, ge=1, le=1000),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        registry = _load_registry(root)
        mp = _load_map(root)
        courses = courses_store.load()
        bac = json_bac_store.load()
        # Index exo_id → filieres pour filtrage
        exo_filiere = {e["id"]: e.get("filiere_id") for e in bac}

        items = []
        for nid, reg_entry in registry.items():
            if matiere and reg_entry.get("matiere_id") != matiere:
                continue
            map_entry = mp.get(nid, {})
            exos = map_entry.get("exercices") or []
            if filiere:
                exos = [ex for ex in exos if exo_filiere.get(ex["id"]) == filiere]
            nb = len(exos)
            if nb < min_exos:
                continue
            filieres = sorted({exo_filiere.get(ex["id"]) for ex in exos
                               if exo_filiere.get(ex["id"])})
            label = reg_entry.get("label", "")
            if q and q.lower() not in label.lower() and q.lower() not in nid.lower():
                continue
            course = courses.get(nid)
            if has_course is True and not course:
                continue
            if has_course is False and course:
                continue
            items.append({
                "notion_id": nid,
                "label": label,
                "matiere_id": reg_entry.get("matiere_id"),
                "chapitre": reg_entry.get("chapitre"),
                "nb_exos": nb,
                "filieres": filieres,
                "has_course": bool(course),
                "course_generated_at": course.get("generated_at") if course else None,
                "course_edited_at": course.get("edited_at") if course else None,
                "course_validated": bool(course.get("validated_by_admin")) if course else False,
            })

        # Tri
        if sort == "nb_exos_desc":
            items.sort(key=lambda x: (-x["nb_exos"], x["notion_id"]))
        elif sort == "nb_exos_asc":
            items.sort(key=lambda x: (x["nb_exos"], x["notion_id"]))
        elif sort == "label":
            items.sort(key=lambda x: x["label"].lower())
        else:  # notion_id
            items.sort(key=lambda x: x["notion_id"])

        total = len(items)
        items = items[offset : offset + limit]

        # Stats globales (avant pagination)
        all_total = sum(1 for nid, e in registry.items()
                        if (not matiere or e.get("matiere_id") == matiere))
        with_course = sum(1 for nid in courses if nid in registry
                          and (not matiere or registry[nid].get("matiere_id") == matiere))

        return {
            "items": items,
            "total": total,
            "offset": offset,
            "limit": limit,
            "stats": {
                "total_notions": all_total,
                "with_course": with_course,
                "without_course": all_total - with_course,
            },
        }

    # ── Détail d'un cours (et de sa notion) ─────────────────────────────────
    @router.get("/{notion_id}", dependencies=[Depends(require_admin)])
    def get_course(notion_id: str) -> dict[str, Any]:
        registry = _load_registry(root)
        if notion_id not in registry:
            raise HTTPException(404, f"Notion '{notion_id}' inconnue.")
        mp = _load_map(root)
        bac = json_bac_store.load()
        by_id = {e["id"]: e for e in bac}
        reg_entry = registry[notion_id]
        exos_refs = mp.get(notion_id, {}).get("exercices") or []
        exos = []
        for ex in exos_refs:
            e = by_id.get(ex["id"])
            if not e:
                continue
            exos.append({
                "id": e["id"],
                "annee": e.get("annee"),
                "session": e.get("session"),
                "filiere_id": e.get("filiere_id"),
                "matiere_id": e.get("matiere_id"),
                "exercice_numero": e.get("exercice_numero"),
                "ennonce_preview": (e.get("ennonce_complet") or "")[:160],
            })

        courses = courses_store.load()
        course = courses.get(notion_id)

        return {
            "notion_id": notion_id,
            "label": reg_entry.get("label"),
            "matiere_id": reg_entry.get("matiere_id"),
            "chapitre": reg_entry.get("chapitre"),
            "exos": exos,
            "course": course,  # None si pas généré
        }

    # ── Génération via Groq ─────────────────────────────────────────────────
    @router.post("/{notion_id}/generate", dependencies=[Depends(require_admin)])
    def generate_course(notion_id: str, body: CourseGenerateRequest) -> dict[str, Any]:
        registry = _load_registry(root)
        if notion_id not in registry:
            raise HTTPException(404, f"Notion '{notion_id}' inconnue.")
        courses = courses_store.load()
        if notion_id in courses and not body.force:
            raise HTTPException(409, "Cours déjà existant. Utilise force=true pour écraser.")

        reg_entry = registry[notion_id]
        label = reg_entry.get("label", "")
        matiere_id = reg_entry.get("matiere_id", "")
        chapitre = reg_entry.get("chapitre", "")

        # Récupérer les exos liés (max N)
        mp = _load_map(root)
        bac = json_bac_store.load()
        by_id = {e["id"]: e for e in bac}
        exos_refs = mp.get(notion_id, {}).get("exercices") or []
        # On préfère les exos avec énoncé long (≥200 char)
        candidates = []
        for ex in exos_refs:
            e = by_id.get(ex["id"])
            if not e:
                continue
            if len((e.get("ennonce_complet") or "").strip()) < 200:
                continue
            candidates.append(e)
        if not candidates:
            raise HTTPException(400, f"Aucun exo avec énoncé exploitable pour '{notion_id}'.")
        exos_context = candidates[: body.max_context_exos]
        context_exo_ids = [e["id"] for e in exos_context]

        user_prompt = _build_user_prompt(label, matiere_id, chapitre, exos_context)
        model = "llama-3.3-70b-versatile"
        log.info("Génération cours notion=%s model=%s nb_exos=%d",
                 notion_id, model, len(exos_context))
        content = _call_groq_for_course(user_prompt, model=model)

        now = datetime.utcnow().isoformat(timespec="seconds")
        entry = {
            "content": content,
            "model": model,
            "generated_at": now,
            "edited_at": None,
            "validated_by_admin": False,
            "notion_label": label,
            "context_exo_ids": context_exo_ids,
        }
        with _lock:
            courses = courses_store.load()  # re-load pour sécurité multi-thread
            courses[notion_id] = entry
            courses_store.save(courses)

        return {
            "notion_id": notion_id,
            "label": label,
            "course": entry,
        }

    # ── Édition manuelle ────────────────────────────────────────────────────
    @router.patch("/{notion_id}", dependencies=[Depends(require_admin)])
    def update_course(notion_id: str, update: CourseUpdate) -> dict[str, Any]:
        with _lock:
            courses = courses_store.load()
            if notion_id not in courses:
                raise HTTPException(404, "Pas de cours pour cette notion.")
            entry = courses[notion_id]
            if update.content is not None:
                entry["content"] = update.content
                entry["edited_at"] = datetime.utcnow().isoformat(timespec="seconds")
            if update.validated_by_admin is not None:
                entry["validated_by_admin"] = bool(update.validated_by_admin)
            courses[notion_id] = entry
            courses_store.save(courses)
        return {"notion_id": notion_id, "course": entry}

    # ── Suppression ─────────────────────────────────────────────────────────
    @router.delete("/{notion_id}", dependencies=[Depends(require_admin)])
    def delete_course(notion_id: str) -> dict:
        with _lock:
            courses = courses_store.load()
            if notion_id not in courses:
                raise HTTPException(404, "Pas de cours pour cette notion.")
            del courses[notion_id]
            courses_store.save(courses)
        return {"ok": True, "notion_id": notion_id}

    return router
