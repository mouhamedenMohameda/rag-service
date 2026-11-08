"""Admin Chapters API — publication des chapitres par série.

L'admin décide quels chapitres (série × matière × chapitre) sont visibles par
les élèves. Tant qu'un chapitre est en brouillon (« draft »), aucun élève n'y a
accès : le catalogue public répond « Pas encore disponible ».

Source de vérité :
  - ``publications.json`` (NOUVEAU) : statut + liste de notions retenue par
    chapitre. Clé = ``"<filiere>|<matiere>|<chapitre>"``.
  - ``json_bac.json``          : exercices (lus via AdminStore)
  - ``notions_registry.json``  : labels des notions (une notion peut être créée
    depuis l'atelier chapitre)
  - ``cours.json``             : cours par notion (via CoursesStore)

Règles de visibilité côté élève (identiques dans l'aperçu admin) :
  - seuls les chapitres ``published`` sont servis ;
  - seuls les exercices ``validated_by_admin`` apparaissent ;
  - la correction n'est montrée que si l'exercice est validé ET non vide ;
  - le cours d'une notion n'est montré que s'il est ``validated_by_admin``.

Routes admin (``X-Api-Key`` S2S) :
  - GET  /admin/chapters                      grille série × matière × chapitre
  - GET  /admin/chapters/detail               atelier d'un chapitre
  - GET  /admin/chapters/preview              vue élève (avec infos admin)
  - PUT  /admin/chapters/notions              fixe la liste de notions du chapitre
  - POST /admin/chapters/publish              publie / dépublie
  - POST /admin/chapters/registry-notion      crée une notion canonique

Routes catalogue (S2S, appelées par Next.js pour les élèves) :
  - GET  /catalog/chapters                    chapitres publiés d'une série
  - GET  /catalog/chapter                     vue élève d'un chapitre publié
"""
from __future__ import annotations

import json
import logging
import re
import shutil
import threading
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Query
from pydantic import BaseModel

log = logging.getLogger("rag-admin-chapters")

_pub_lock = threading.RLock()
_reg_lock = threading.RLock()

FILIERES = ("C", "D")
MATIERES = ("math", "pc", "svt")
_PC_ALIASES = ("pc", "physique", "chimie")
_SESSION_ORDER = {"normale": 0, "complementaire": 1, "complémentaire": 1}

NOT_PUBLISHED_MESSAGE = "Pas encore disponible"


# ─── Helpers ────────────────────────────────────────────────────────────────


def chapter_key(filiere: str, matiere: str, chapitre: str) -> str:
    return f"{filiere}|{matiere}|{chapitre.strip()}"


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def _mat_match(e: dict, matiere: str) -> bool:
    em = e.get("matiere_id") or ""
    if matiere == "pc":
        return em in _PC_ALIASES
    return em == matiere


def _canon_matiere(m: str) -> str:
    return "pc" if m in _PC_ALIASES else m


def _chapters_of(e: dict) -> set[str]:
    out: set[str] = set()
    c = (e.get("chapitre") or "").strip()
    if c:
        out.add(c)
    for c2 in e.get("chapitres") or []:
        if isinstance(c2, str) and c2.strip():
            out.add(c2.strip())
    return out


def _in_chapter(e: dict, filiere: str, matiere: str, chapitre: str) -> bool:
    return (
        e.get("filiere_id") == filiere
        and _mat_match(e, matiere)
        and chapitre.strip() in _chapters_of(e)
    )


def _has_correction(e: dict) -> bool:
    return bool((e.get("correction") or "").strip())


def _sort_key(e: dict) -> tuple:
    try:
        annee = int(e.get("annee") or 0)
    except (TypeError, ValueError):
        annee = 0
    sess = _SESSION_ORDER.get(str(e.get("session") or "").strip().lower(), 9)
    try:
        num = int(e.get("exercice_numero"))
    except (TypeError, ValueError):
        num = 999
    # Plus récent d'abord pour l'élève et l'admin.
    return (-annee, sess, num)


def _slug(text: str) -> str:
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:60] or "notion"


def _validate_scope(filiere: str, matiere: str) -> str:
    if filiere not in FILIERES:
        raise HTTPException(400, f"filiere doit être {' ou '.join(FILIERES)}.")
    m = _canon_matiere(matiere)
    if m not in MATIERES:
        raise HTTPException(400, "matiere doit être math, pc ou svt.")
    return m


# ─── Stores ─────────────────────────────────────────────────────────────────


class _JsonFile:
    """Fichier JSON avec backup horodaté + écriture atomique (même schéma que
    AdminStore / CoursesStore)."""

    def __init__(self, path: Path, backup_dir: Path, prefix: str, lock, max_backups: int = 20):
        self.path = path
        self.backup_dir = backup_dir
        self.prefix = prefix
        self.lock = lock
        self.max_backups = max_backups
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def load(self) -> dict:
        if not self.path.exists():
            return {}
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            log.error("%s corrompu (%s)", self.path.name, e)
            raise HTTPException(500, f"{self.path.name} corrompu : {e}. Voir backups.")

    def save(self, data: dict) -> None:
        with self.lock:
            if self.path.exists():
                stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                shutil.copy2(self.path, self.backup_dir / f"{self.prefix}-{stamp}.json")
                backups = sorted(self.backup_dir.glob(f"{self.prefix}-*.json"))
                for old in backups[: -self.max_backups]:
                    old.unlink(missing_ok=True)
            tmp = self.path.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            tmp.replace(self.path)


class PublicationsStore(_JsonFile):
    def __init__(self, path: Path, backup_dir: Path):
        super().__init__(path, backup_dir, "publications", _pub_lock)

    def get(self, filiere: str, matiere: str, chapitre: str) -> Optional[dict]:
        return self.load().get(chapter_key(filiere, matiere, chapitre))

    def is_published(self, filiere: str, matiere: str, chapitre: str) -> bool:
        p = self.get(filiere, matiere, chapitre)
        return bool(p and p.get("status") == "published")

    def upsert(self, filiere: str, matiere: str, chapitre: str, **fields: Any) -> dict:
        with self.lock:
            data = self.load()
            key = chapter_key(filiere, matiere, chapitre)
            entry = data.get(key) or {
                "filiere_id": filiere,
                "matiere_id": matiere,
                "chapitre": chapitre.strip(),
                "status": "draft",
                "notion_ids": None,  # None = liste pas encore fixée par l'admin
                "published_at": None,
            }
            entry.update(fields)
            entry["updated_at"] = _now()
            data[key] = entry
            self.save(data)
            return entry


class RegistryStore(_JsonFile):
    def __init__(self, path: Path, backup_dir: Path):
        super().__init__(path, backup_dir, "notions_registry", _reg_lock)


# ─── Schemas ────────────────────────────────────────────────────────────────


class ChapterRef(BaseModel):
    filiere_id: str
    matiere_id: str
    chapitre: str


class ChapterNotionsUpdate(ChapterRef):
    notion_ids: list[str]


class ChapterPublish(ChapterRef):
    published: bool


class RegistryNotionCreate(BaseModel):
    matiere_id: str
    label: str


# ─── Calculs ────────────────────────────────────────────────────────────────


def _suggested_notions(exos: list[dict]) -> list[str]:
    c = Counter(n for e in exos for n in (e.get("notion_ids") or []))
    return [n for n, _ in c.most_common()]


def _readiness(exos: list[dict], notion_ids: Optional[list[str]], courses: dict) -> dict:
    validated = [e for e in exos if e.get("validated_by_admin")]
    nids = notion_ids or []
    curated = set(nids)
    lessons_validated = sum(
        1 for n in nids if (courses.get(n) or {}).get("validated_by_admin")
    )
    uncovered = [
        e.get("id") for e in exos if not curated.intersection(e.get("notion_ids") or [])
    ]
    checks = {
        "exercises": len(exos),
        "exercises_validated": len(validated),
        "corrections_ready": sum(1 for e in validated if _has_correction(e)),
        "notions_curated": notion_ids is not None,
        "notions": len(nids),
        "lessons_validated": lessons_validated,
        "exercises_without_chapter_notion": uncovered if notion_ids is not None else [],
    }
    checks["ready"] = bool(
        exos
        and notion_ids is not None
        and nids
        and len(validated) == len(exos)
        and checks["corrections_ready"] == len(exos)
        and lessons_validated == len(nids)
        and not uncovered
    )
    return checks


def build_student_view(
    data: list[dict],
    registry: dict,
    courses: dict,
    filiere: str,
    matiere: str,
    chapitre: str,
    notion_ids: list[str],
    with_admin_info: bool = False,
) -> dict:
    """Ce que voit l'élève pour un chapitre : par notion, le cours validé et
    les exercices validés de la même série (toutes années, tous chapitres) où
    la notion apparaît, avec leur correction si disponible."""
    scope = [
        e for e in data
        if e.get("filiere_id") == filiere and _mat_match(e, matiere) and not e.get("is_skeleton")
    ]
    notions_out = []
    for nid in notion_ids:
        reg = registry.get(nid) or {}
        course = courses.get(nid) or {}
        linked = sorted((e for e in scope if nid in (e.get("notion_ids") or [])), key=_sort_key)
        visible = [e for e in linked if e.get("validated_by_admin")]
        item: dict[str, Any] = {
            "notion_id": nid,
            "label": reg.get("label") or nid,
            "lesson": course.get("content") if course.get("validated_by_admin") else None,
            "years": sorted({int(e["annee"]) for e in visible if e.get("annee")}),
            "occurrences": [
                {
                    "id": e.get("id"),
                    "annee": e.get("annee"),
                    "session": e.get("session"),
                    "exercice_numero": e.get("exercice_numero"),
                    "chapitre": e.get("chapitre"),
                    "enonce": e.get("ennonce_complet") or "",
                    "correction": (e.get("correction") or None) if _has_correction(e) else None,
                }
                for e in visible
            ],
        }
        if with_admin_info:
            item["admin"] = {
                "hidden_unvalidated_exercises": len(linked) - len(visible),
                "lesson_exists": bool(course.get("content")),
                "lesson_hidden_unvalidated": bool(course.get("content"))
                and not course.get("validated_by_admin"),
            }
        notions_out.append(item)
    return {
        "filiere_id": filiere,
        "matiere_id": matiere,
        "chapitre": chapitre.strip(),
        "notions": notions_out,
    }


# ─── Routers ────────────────────────────────────────────────────────────────


def build_chapters_routers(
    json_bac_store,  # AdminStore
    courses_store,  # CoursesStore
    publications: PublicationsStore,
    registry_store: RegistryStore,
    api_key: str,
) -> tuple[APIRouter, APIRouter]:
    admin = APIRouter(prefix="/admin/chapters", tags=["admin-chapters"])
    catalog = APIRouter(prefix="/catalog", tags=["catalog"])

    def require_key(x_api_key: Optional[str] = Header(default=None)) -> None:
        if not x_api_key or x_api_key != api_key:
            raise HTTPException(401, "Auth S2S requise.")

    def _effective_notions(pub: Optional[dict], exos: list[dict]) -> tuple[list[str], bool]:
        if pub and pub.get("notion_ids") is not None:
            return list(pub["notion_ids"]), True
        return _suggested_notions(exos), False

    # ── Grille ───────────────────────────────────────────────────────────────
    @admin.get("", dependencies=[Depends(require_key)])
    def grid(
        filiere: Optional[str] = Query(None),
        matiere: Optional[str] = Query(None),
    ) -> dict[str, Any]:
        data = json_bac_store.load()
        pubs = publications.load()
        courses = courses_store.load()

        buckets: dict[tuple[str, str, str], list[dict]] = {}
        unassigned: Counter = Counter()
        for e in data:
            f = e.get("filiere_id")
            m = _canon_matiere(e.get("matiere_id") or "")
            if f not in FILIERES or m not in MATIERES:
                continue
            if filiere and f != filiere:
                continue
            if matiere and m != matiere:
                continue
            chs = _chapters_of(e)
            if not chs:
                unassigned[(f, m)] += 1
            for c in chs:
                buckets.setdefault((f, m, c), []).append(e)
        # Chapitres créés côté publications mais sans exercice (rare)
        for p in pubs.values():
            k = (p["filiere_id"], p["matiere_id"], p["chapitre"])
            if (filiere and k[0] != filiere) or (matiere and k[1] != matiere):
                continue
            buckets.setdefault(k, [])

        rows = []
        for (f, m, c), exos in buckets.items():
            pub = pubs.get(chapter_key(f, m, c))
            nids, curated = _effective_notions(pub, exos)
            years = sorted({int(e["annee"]) for e in exos if e.get("annee")})
            rows.append({
                "filiere_id": f,
                "matiere_id": m,
                "chapitre": c,
                "status": (pub or {}).get("status", "draft"),
                "published_at": (pub or {}).get("published_at"),
                "years": [years[0], years[-1]] if years else None,
                "checks": _readiness(exos, nids if curated else None, courses),
            })
        rows.sort(key=lambda r: (r["filiere_id"], MATIERES.index(r["matiere_id"]), -r["checks"]["exercises"]))
        return {
            "items": rows,
            "unassigned": [
                {"filiere_id": f, "matiere_id": m, "exercises": n}
                for (f, m), n in sorted(unassigned.items())
            ],
        }

    # ── Atelier ──────────────────────────────────────────────────────────────
    @admin.get("/detail", dependencies=[Depends(require_key)])
    def detail(
        filiere: str = Query(...),
        matiere: str = Query(...),
        chapitre: str = Query(...),
    ) -> dict[str, Any]:
        m = _validate_scope(filiere, matiere)
        data = json_bac_store.load()
        registry = registry_store.load()
        courses = courses_store.load()
        pub = publications.get(filiere, m, chapitre)
        exos = sorted((e for e in data if _in_chapter(e, filiere, m, chapitre)), key=_sort_key)
        nids, curated = _effective_notions(pub, exos)
        in_chapter_count = Counter(n for e in exos for n in (e.get("notion_ids") or []))

        def notion_row(nid: str) -> dict:
            course = courses.get(nid) or {}
            return {
                "notion_id": nid,
                "label": (registry.get(nid) or {}).get("label") or nid,
                "known": nid in registry,
                "exercises_in_chapter": in_chapter_count.get(nid, 0),
                "has_course": bool(course.get("content")),
                "course_validated": bool(course.get("validated_by_admin")),
            }

        others = [n for n in _suggested_notions(exos) if n not in set(nids)]
        return {
            "filiere_id": filiere,
            "matiere_id": m,
            "chapitre": chapitre.strip(),
            "status": (pub or {}).get("status", "draft"),
            "published_at": (pub or {}).get("published_at"),
            "notions_curated": curated,
            "notions": [notion_row(n) for n in nids],
            "other_notions_in_exercises": [notion_row(n) for n in others],
            "exercises": [
                {
                    "id": e.get("id"),
                    "titre": e.get("titre"),
                    "annee": e.get("annee"),
                    "session": e.get("session"),
                    "exercice_numero": e.get("exercice_numero"),
                    "notion_ids": e.get("notion_ids") or [],
                    "has_correction": _has_correction(e),
                    "validated_by_admin": bool(e.get("validated_by_admin")),
                    "is_skeleton": bool(e.get("is_skeleton")),
                    "ennonce_preview": (e.get("ennonce_complet") or "")[:160],
                }
                for e in exos
            ],
            "checks": _readiness(exos, nids if curated else None, courses),
        }

    @admin.get("/preview", dependencies=[Depends(require_key)])
    def preview(
        filiere: str = Query(...),
        matiere: str = Query(...),
        chapitre: str = Query(...),
    ) -> dict[str, Any]:
        m = _validate_scope(filiere, matiere)
        data = json_bac_store.load()
        pub = publications.get(filiere, m, chapitre)
        exos = [e for e in data if _in_chapter(e, filiere, m, chapitre)]
        nids, _ = _effective_notions(pub, exos)
        view = build_student_view(
            data, registry_store.load(), courses_store.load(),
            filiere, m, chapitre, nids, with_admin_info=True,
        )
        view["status"] = (pub or {}).get("status", "draft")
        return view

    @admin.put("/notions", dependencies=[Depends(require_key)])
    def set_notions(body: ChapterNotionsUpdate) -> dict[str, Any]:
        m = _validate_scope(body.filiere_id, body.matiere_id)
        registry = registry_store.load()
        cleaned: list[str] = []
        for nid in body.notion_ids:
            nid = nid.strip()
            if not nid or nid in cleaned:
                continue
            reg = registry.get(nid)
            if not reg:
                raise HTTPException(400, f"Notion inconnue : {nid}")
            if _canon_matiere(reg.get("matiere_id") or "") != m:
                raise HTTPException(400, f"La notion {nid} n'est pas de la matière {m}.")
            cleaned.append(nid)
        entry = publications.upsert(body.filiere_id, m, body.chapitre, notion_ids=cleaned)
        log.info("Notions %s → %d", chapter_key(body.filiere_id, m, body.chapitre), len(cleaned))
        return entry

    @admin.post("/publish", dependencies=[Depends(require_key)])
    def publish(body: ChapterPublish) -> dict[str, Any]:
        m = _validate_scope(body.filiere_id, body.matiere_id)
        current = publications.get(body.filiere_id, m, body.chapitre) or {}
        if body.published and not current.get("notion_ids"):
            raise HTTPException(
                400, "Fixe d'abord la liste des notions du chapitre avant de publier."
            )
        entry = publications.upsert(
            body.filiere_id, m, body.chapitre,
            status="published" if body.published else "draft",
            published_at=_now() if body.published else current.get("published_at"),
        )
        log.warning("%s %s", "PUBLISH" if body.published else "UNPUBLISH",
                    chapter_key(body.filiere_id, m, body.chapitre))
        return entry

    @admin.post("/registry-notion", dependencies=[Depends(require_key)])
    def create_registry_notion(body: RegistryNotionCreate) -> dict[str, Any]:
        m = _canon_matiere(body.matiere_id)
        if m not in MATIERES:
            raise HTTPException(400, "matiere doit être math, pc ou svt.")
        label = body.label.strip()
        if len(label) < 3:
            raise HTTPException(400, "Label trop court.")
        with _reg_lock:
            registry = registry_store.load()
            for nid, v in registry.items():
                if (v.get("label") or "").strip().lower() == label.lower() and \
                        _canon_matiere(v.get("matiere_id") or "") == m:
                    return {"notion_id": nid, "created": False, **v}
            base = f"{m}.{_slug(label)}"
            nid, i = base, 2
            while nid in registry:
                nid, i = f"{base}-{i}", i + 1
            registry[nid] = {"label": label, "matiere_id": m, "aliases": []}
            registry_store.save(registry)
        log.info("Registry: nouvelle notion %s", nid)
        return {"notion_id": nid, "created": True, "label": label, "matiere_id": m, "aliases": []}

    # ── Catalogue élèves ─────────────────────────────────────────────────────
    @catalog.get("/chapters", dependencies=[Depends(require_key)])
    def published_chapters(
        filiere: str = Query(...),
        matiere: Optional[str] = Query(None),
    ) -> dict[str, Any]:
        if filiere not in FILIERES:
            raise HTTPException(400, "filiere invalide.")
        registry = registry_store.load()
        items = []
        for p in publications.load().values():
            if p.get("status") != "published" or p.get("filiere_id") != filiere:
                continue
            if matiere and p.get("matiere_id") != _canon_matiere(matiere):
                continue
            items.append({
                "matiere_id": p["matiere_id"],
                "chapitre": p["chapitre"],
                "notions": [
                    {"notion_id": n, "label": (registry.get(n) or {}).get("label") or n}
                    for n in p.get("notion_ids") or []
                ],
            })
        return {"filiere_id": filiere, "items": items}

    @catalog.get("/chapter", dependencies=[Depends(require_key)])
    def published_chapter(
        filiere: str = Query(...),
        matiere: str = Query(...),
        chapitre: str = Query(...),
    ) -> dict[str, Any]:
        m = _validate_scope(filiere, matiere)
        pub = publications.get(filiere, m, chapitre)
        if not pub or pub.get("status") != "published":
            raise HTTPException(
                404, {"code": "not_published", "message": NOT_PUBLISHED_MESSAGE}
            )
        view = build_student_view(
            json_bac_store.load(), registry_store.load(), courses_store.load(),
            filiere, m, chapitre, pub.get("notion_ids") or [],
        )
        view["status"] = "published"
        return view

    return admin, catalog
