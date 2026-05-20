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
#   3) Matière : physique et chimie ensemble (PDF unique), puis math, puis svt
#   4) Numéro d'exercice ASC
_SESSION_ORDER = {"normale": 0, "complementaire": 1, "complémentaire": 1}
_MAT_ORDER = {"physique": 0, "chimie": 1, "math": 2, "svt": 3}


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
    PAS modifier matiere_id / fichier / annee depuis l'UI (sinon dérive de
    schéma garantie).
    """

    ennonce_complet: Optional[str] = None
    notions_traitees: Optional[list[str]] = None
    chapitre: Optional[str] = None
    validated_by_admin: Optional[bool] = None


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
        return {
            "total": len(data),
            "validated": validated,
            "remaining": len(data) - validated,
            "validated_pct": round(validated / max(1, len(data)) * 100, 1),
            "by_matiere": dict(Counter(e.get("matiere_id", "?") for e in data)),
            "by_year": dict(sorted(Counter(e.get("annee") for e in data).items())),
            "top_chapitres": dict(
                Counter(e.get("chapitre", "?") for e in data if e.get("chapitre")).most_common(15)
            ),
        }

    # ── Liste ───────────────────────────────────────────────────────────────
    @router.get("/exercises", dependencies=[Depends(require_admin)])
    def list_exercises(
        matiere: Optional[str] = Query(None, description="math|physique|chimie|svt"),
        filiere: Optional[str] = Query(None, description="C|D|TM|M"),
        annee: Optional[int] = Query(None),
        validated: Optional[bool] = Query(None),
        q: Optional[str] = Query(None, description="recherche texte libre"),
        sort: str = Query("chronological", description="chronological|unvalidated_first|id"),
        limit: int = Query(50, ge=1, le=500),
        offset: int = Query(0, ge=0),
    ) -> dict[str, Any]:
        data = store.load()
        if matiere:
            data = [e for e in data if e.get("matiere_id") == matiere]
        if filiere:
            data = [e for e in data if e.get("filiere_id") == filiere]
        if annee:
            data = [e for e in data if e.get("annee") == annee]
        if validated is not None:
            data = [e for e in data if bool(e.get("validated_by_admin")) == validated]
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
                "matiere_id": e.get("matiere_id"),
                "filiere_id": e.get("filiere_id"),
                "fichier": e.get("fichier"),
                "annee": e.get("annee"),
                "session": e.get("session"),
                "chapitre": e.get("chapitre"),
                "notions_count": len(e.get("notions_traitees") or []),
                "ennonce_preview": (e.get("ennonce_complet") or "")[:140],
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
                data[i] = e
                store.save(data)
                log.info("PATCH %s → %s", eid, list(patch.keys()))
                return e
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
