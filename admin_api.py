"""Admin API — édition manuelle du JSON Bac (énoncés + notions).

Source de vérité : ``/opt/rag-service/json_bac.json`` (schéma flat + champ
``validated_by_admin``). Sauvegarde automatique avant chaque écriture dans
``json_backups/`` (rotation : on garde les 20 plus récents).

Routes :
- GET  /admin/stats                       résumé global
- GET  /admin/exercises                   liste paginée + filtres
- GET  /admin/exercises/{id}              détail d'un exercice
- PATCH /admin/exercises/{id}             édition partielle
- GET  /admin/exercises/{id}/neighbors    prev/next pour navigation

Auth : header ``X-Api-Key`` = la même clé S2S que le reste du service. La
page Next.js /admin/exercices proxy les appels avec cette clé après avoir
vérifié que l'utilisateur connecté est admin.
"""
from __future__ import annotations

import json
import logging
import shutil
import threading
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Header, Query
from pydantic import BaseModel

log = logging.getLogger("rag-admin")

_lock = threading.RLock()


# Ordre canonique de tri chronologique pour l'admin :
#   1) Année DESC (plus récente d'abord)
#   2) Session : normale (0) avant complémentaire (1)
#   3) Matière : pc (sciences physiques) → math → svt (legacy physique/chimie
#      conservé pour les vieilles entrées non encore migrées)
#   4) Numéro d'exercice ASC
_SESSION_ORDER = {"normale": 0, "complementaire": 1, "complémentaire": 1}
_MAT_ORDER = {"pc": 0, "physique": 0, "chimie": 0, "math": 1, "svt": 2}


_MATIERE_LABEL = {
    "math": "Mathématiques",
    "pc": "Sciences Physiques",
    "svt": "Sciences Naturelles",
}


def _session_code(session: str) -> str:
    s = (session or "").strip().lower()
    return "sn" if "normal" in s else ("sc" if "compl" in s else "x")


def make_skeleton_id(filiere: str, annee: int, session: str, mat_id: str, ex_num: int) -> str:
    return f"bac-{filiere.lower()}-{annee}-{_session_code(session)}-{mat_id}-ex{ex_num}"


def make_skeleton_titre(filiere: str, annee: int, session: str, ex_num: int, mat_id: str) -> str:
    label = _MATIERE_LABEL.get(mat_id, mat_id)
    return f"BAC {filiere} {annee} Session {session.lower()} exo {ex_num} ({label})"


def _chronological_key(e: dict) -> tuple:
    try:
        annee = int(e.get("annee") or 0)
    except (TypeError, ValueError):
        annee = 0
    sess = str(e.get("session") or "").strip().lower()
    sess_rank = _SESSION_ORDER.get(sess, 9)
    mat_rank = _MAT_ORDER.get(e.get("matiere_id", ""), 9)
    raw = e.get("exercice_numero")
    try:
        ex_num = int(raw)
    except (TypeError, ValueError):
        # Si c'est un string non-numérique (ex. "BAC-2022-..."), on met à la fin.
        ex_num = 999
    return (-annee, sess_rank, mat_rank, ex_num)


# ─── Store ──────────────────────────────────────────────────────────────────


class AdminStore:
    """JSON-file-as-database avec backup auto + lock."""

    def __init__(self, json_path: Path, backup_dir: Path, max_backups: int = 20):
        self.json_path = json_path
        self.backup_dir = backup_dir
        self.max_backups = max_backups
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def load(self) -> list[dict]:
        if not self.json_path.exists():
            return []
        try:
            return json.loads(self.json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            log.error("JSON corrompu (%s) — voir json_backups/", e)
            raise HTTPException(500, f"JSON corrompu : {e}. Restaurer depuis backup.")

    def save(self, data: list[dict]) -> None:
        with _lock:
            # 1) Backup snapshot avant toute écriture (si fichier existe).
            if self.json_path.exists():
                stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                shutil.copy2(self.json_path, self.backup_dir / f"json_bac-{stamp}.json")
                # Rotation : on garde les plus récents
                backups = sorted(self.backup_dir.glob("json_bac-*.json"))
                for old in backups[: -self.max_backups]:
                    old.unlink(missing_ok=True)
            # 2) Écriture atomique : write tmp + rename
            tmp = self.json_path.with_suffix(".json.tmp")
            tmp.write_text(
                json.dumps(data, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            tmp.replace(self.json_path)


# ─── Schemas Pydantic ───────────────────────────────────────────────────────


class ExerciceUpdate(BaseModel):
    """Update partiel — seuls les champs présents sont modifiés.

    Volontairement limité aux champs éditables par l'admin : on ne laisse
    PAS modifier matiere_id / fichier / annee / filiere depuis l'UI (sinon
    dérive de schéma garantie ; pour la filière utiliser les scripts CLI).
    """

    ennonce_complet: Optional[str] = None
    correction: Optional[str] = None
    notions_traitees: Optional[list[str]] = None
    chapitre: Optional[str] = None
    fichier: Optional[str] = None
    validated_by_admin: Optional[bool] = None


class ExerciceCreate(BaseModel):
    """Création manuelle d'un exercice depuis l'UI (ex: « +Ajouter un exo »
    dans une session). Le serveur calcule l'id et le titre canoniques."""

    filiere_id: str
    matiere_id: str
    annee: int
    session: str
    exercice_numero: int


# ─── Router ─────────────────────────────────────────────────────────────────


def build_admin_router(store: AdminStore, api_key: str) -> APIRouter:
    router = APIRouter(prefix="/admin", tags=["admin"])

    def require_admin(x_api_key: Optional[str] = Header(default=None)) -> None:
        if not x_api_key or x_api_key != api_key:
            raise HTTPException(401, "Admin auth requise.")

    # ── Stats ───────────────────────────────────────────────────────────────
    @router.get("/stats", dependencies=[Depends(require_admin)])
    def stats() -> dict[str, Any]:
        data = store.load()
        validated = sum(1 for e in data if e.get("validated_by_admin"))
        skeletons = sum(1 for e in data if e.get("is_skeleton"))
        return {
            "total": len(data),
            "validated": validated,
            "remaining": len(data) - validated,
            "validated_pct": round(validated / max(1, len(data)) * 100, 1),
            "skeletons": skeletons,
            "filled": len(data) - skeletons,
            "by_matiere": dict(Counter(e.get("matiere_id", "?") for e in data)),
            "by_filiere": dict(Counter(e.get("filiere_id", "?") for e in data)),
            "by_year": dict(sorted(Counter(e.get("annee") for e in data).items())),
            "top_chapitres": dict(
                Counter(e.get("chapitre", "?") for e in data if e.get("chapitre")).most_common(15)
            ),
        }

    # ── Liste ───────────────────────────────────────────────────────────────
    @router.get("/exercises", dependencies=[Depends(require_admin)])
    def list_exercises(
        matiere: Optional[str] = Query(None, description="math|pc|svt"),
        filiere: Optional[str] = Query(None, description="C|D"),
        annee: Optional[int] = Query(None),
        validated: Optional[bool] = Query(None),
        skeleton: Optional[bool] = Query(None, description="true = squelettes vides seulement"),
        q: Optional[str] = Query(None, description="recherche texte libre"),
        sort: str = Query("chronological", description="chronological|unvalidated_first|id"),
        limit: int = Query(50, ge=1, le=2000),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        data = store.load()
        if matiere:
            # Accepte les anciens matiere_id "physique"/"chimie" comme aliases de "pc"
            if matiere == "pc":
                data = [e for e in data if e.get("matiere_id") in ("pc", "physique", "chimie")]
            else:
                data = [e for e in data if e.get("matiere_id") == matiere]
        if filiere:
            data = [e for e in data if e.get("filiere_id") == filiere]
        if annee:
            data = [e for e in data if e.get("annee") == annee]
        if validated is not None:
            data = [e for e in data if bool(e.get("validated_by_admin")) == validated]
        if skeleton is not None:
            data = [e for e in data if bool(e.get("is_skeleton")) == skeleton]
        if q:
            ql = q.lower()
            data = [
                e for e in data
                if ql in (e.get("ennonce_complet") or "").lower()
                or ql in (e.get("chapitre") or "").lower()
                or ql in (e.get("id") or "").lower()
                or ql in (e.get("fichier") or "").lower()
            ]
        if sort == "unvalidated_first":
            data.sort(key=lambda e: (bool(e.get("validated_by_admin")), _chronological_key(e)))
        elif sort == "id":
            data.sort(key=lambda e: e.get("id", ""))
        else:  # chronological (défaut) : année récente d'abord, normale avant
               # complémentaire, physique+chimie ensemble, puis ex_num.
            data.sort(key=_chronological_key)
        total = len(data)
        # Pour la liste on renvoie un payload allégé (pas l'énoncé complet) pour
        # éviter de charger 81×1ko à chaque rafraîchissement du tableau.
        items = [
            {
                "id": e.get("id"),
                "titre": e.get("titre"),
                "matiere_id": e.get("matiere_id"),
                "filiere_id": e.get("filiere_id"),
                "fichier": e.get("fichier"),
                "annee": e.get("annee"),
                "session": e.get("session"),
                "exercice_numero": e.get("exercice_numero"),
                "chapitre": e.get("chapitre"),
                "notions_count": len(e.get("notions_traitees") or []),
                "ennonce_preview": (e.get("ennonce_complet") or "")[:140],
                "has_correction": bool((e.get("correction") or "").strip()),
                "is_skeleton": bool(e.get("is_skeleton")),
                "validated_by_admin": bool(e.get("validated_by_admin")),
                "updated_at": e.get("updated_at"),
            }
            for e in data[offset : offset + limit]
        ]
        return {"total": total, "limit": limit, "offset": offset, "items": items}

    # ── Détail ──────────────────────────────────────────────────────────────
    @router.get("/exercises/{eid}", dependencies=[Depends(require_admin)])
    def get_exercise(eid: str) -> dict:
        data = store.load()
        for e in data:
            if e.get("id") == eid:
                return e
        raise HTTPException(404, "Exercice introuvable.")

    # ── Update partiel ──────────────────────────────────────────────────────
    @router.patch("/exercises/{eid}", dependencies=[Depends(require_admin)])
    def update_exercise(eid: str, body: ExerciceUpdate) -> dict:
        data = store.load()
        for i, e in enumerate(data):
            if e.get("id") == eid:
                patch = body.model_dump(exclude_unset=True)
                for k, v in patch.items():
                    e[k] = v
                e["updated_at"] = datetime.now().isoformat(timespec="seconds")
                # Si l'admin a renseigné énoncé OU correction, l'entrée n'est
                # plus un "squelette vide".
                if (e.get("ennonce_complet") or "").strip() or (e.get("correction") or "").strip():
                    e["is_skeleton"] = False
                data[i] = e
                store.save(data)
                log.info("PATCH %s → %s", eid, list(patch.keys()))
                return e
        raise HTTPException(404, "Exercice introuvable.")

    # ── Création ────────────────────────────────────────────────────────────
    @router.post("/exercises", dependencies=[Depends(require_admin)])
    def create_exercise(body: ExerciceCreate) -> dict:
        """Crée un exo squelette pour une (filière, matière, année, session,
        ex_num) précise. Refuse si un exo avec le même id existe déjà."""
        if body.filiere_id not in ("C", "D"):
            raise HTTPException(400, "filiere_id doit être C ou D.")
        if body.matiere_id not in ("math", "pc", "svt"):
            raise HTTPException(400, "matiere_id doit être math, pc ou svt.")
        sess = body.session.strip()
        if not any(s in sess.lower() for s in ("normal", "compl")):
            raise HTTPException(400, "session doit être 'Normale' ou 'Complémentaire'.")
        new_id = make_skeleton_id(body.filiere_id, body.annee, sess, body.matiere_id, body.exercice_numero)
        data = store.load()
        if any(e.get("id") == new_id for e in data):
            raise HTTPException(409, f"Un exo avec id={new_id} existe déjà.")
        new_entry = {
            "id": new_id,
            "titre": make_skeleton_titre(body.filiere_id, body.annee, sess, body.exercice_numero, body.matiere_id),
            "matiere_id": body.matiere_id,
            "matiere": _MATIERE_LABEL.get(body.matiere_id, body.matiere_id),
            "filiere_id": body.filiere_id,
            "filiere": f"Série {body.filiere_id}",
            "annee": body.annee,
            "session": sess,
            "exercice_numero": body.exercice_numero,
            "fichier": "",
            "chapitre": "",
            "notions_traitees": [],
            "ennonce_complet": "",
            "correction": "",
            "donnees_fournies": {},
            "validated_by_admin": False,
            "is_skeleton": True,
            "updated_at": datetime.now().isoformat(timespec="seconds"),
        }
        data.append(new_entry)
        store.save(data)
        log.info("POST création %s", new_id)
        return new_entry

    # ── Suppression ─────────────────────────────────────────────────────────
    @router.delete("/exercises/{eid}", dependencies=[Depends(require_admin)])
    def delete_exercise(eid: str) -> dict:
        data = store.load()
        for i, e in enumerate(data):
            if e.get("id") == eid:
                deleted = data.pop(i)
                store.save(data)
                log.warning("DELETE %s (validated=%s)", eid, deleted.get("validated_by_admin"))
                return {"deleted": True, "id": eid}
        raise HTTPException(404, "Exercice introuvable.")

    # ── Voisins (prev/next) ─────────────────────────────────────────────────
    @router.get("/exercises/{eid}/neighbors", dependencies=[Depends(require_admin)])
    def neighbors(
        eid: str,
        only_unvalidated: bool = Query(False),
        matiere: Optional[str] = Query(None),
        filiere: Optional[str] = Query(None),
    ) -> dict:
        """Renvoie l'id précédent et suivant dans la liste filtrée. Permet à
        l'UI de naviguer "exo suivant à corriger" sans recharger la liste.

        Même ordre que la liste : chronologique par défaut, mais on garde
        l'option "non validés en premier" via flag.
        """
        data = store.load()
        if matiere:
            data = [e for e in data if e.get("matiere_id") == matiere]
        if filiere:
            data = [e for e in data if e.get("filiere_id") == filiere]
        if only_unvalidated:
            data = [e for e in data if not e.get("validated_by_admin")]
        # Tri identique à la liste pour cohérence prev/next
        data.sort(key=lambda e: (bool(e.get("validated_by_admin")), _chronological_key(e))
                  if only_unvalidated else _chronological_key(e))
        ids = [e.get("id") for e in data]
        if eid not in ids:
            return {"prev": None, "next": None, "position": None, "total": len(ids)}
        idx = ids.index(eid)
        return {
            "prev": ids[idx - 1] if idx > 0 else None,
            "next": ids[idx + 1] if idx < len(ids) - 1 else None,
            "position": idx + 1,
            "total": len(ids),
        }

    return router
