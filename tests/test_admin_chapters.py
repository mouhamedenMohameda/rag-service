"""Tests de l'API chapitres sur une COPIE des données réelles.

Lancer depuis rag-service/ :  python -m pytest tests/test_admin_chapters.py -q
(ou directement : python tests/test_admin_chapters.py)
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from admin_api import AdminStore, build_admin_router  # noqa: E402
from admin_chapters import (  # noqa: E402
    NOT_PUBLISHED_MESSAGE,
    PublicationsStore,
    RegistryStore,
    _JsonFile,
    _pub_lock,
    build_chapters_routers,
)

KEY = "test-key"
H = {"X-Api-Key": KEY}
CH = {"filiere": "D", "matiere": "math", "chapitre": "Nombres complexes"}
BODY = {"filiere_id": "D", "matiere_id": "math", "chapitre": "Nombres complexes"}


def make_client(tmp: Path) -> TestClient:
    for name in ("json_bac.json", "notions_registry.json", "cours.json"):
        shutil.copy2(ROOT / name, tmp / name)
    backups = tmp / "json_backups"
    store = AdminStore(json_path=tmp / "json_bac.json", backup_dir=backups)
    courses = _JsonFile(tmp / "cours.json", backups, "cours", _pub_lock)
    pubs = PublicationsStore(tmp / "publications.json", backups)
    reg = RegistryStore(tmp / "notions_registry.json", backups)
    app = FastAPI()
    app.include_router(build_admin_router(store, api_key=KEY))
    a, c = build_chapters_routers(store, courses, pubs, reg, api_key=KEY)
    app.include_router(a)
    app.include_router(c)
    return TestClient(app)


def run() -> None:
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        cl = make_client(tmp)

        # Auth
        assert cl.get("/admin/chapters").status_code == 401
        assert cl.get("/catalog/chapter", params=CH).status_code == 401

        # Grille : D × math × Nombres complexes existe, en brouillon
        g = cl.get("/admin/chapters", headers=H).json()
        row = next(r for r in g["items"]
                   if (r["filiere_id"], r["matiere_id"], r["chapitre"]) == ("D", "math", "Nombres complexes"))
        assert row["status"] == "draft"
        assert row["checks"]["exercises"] >= 1
        assert row["checks"]["notions_curated"] is False

        # Non publié → « Pas encore disponible »
        r = cl.get("/catalog/chapter", params=CH, headers=H)
        assert r.status_code == 404
        assert r.json()["detail"]["message"] == NOT_PUBLISHED_MESSAGE

        # Publication refusée tant que les notions ne sont pas fixées
        assert cl.post("/admin/chapters/publish", json={**BODY, "published": True}, headers=H).status_code == 400

        # Atelier : notions suggérées depuis les exercices
        det = cl.get("/admin/chapters/detail", params=CH, headers=H).json()
        assert det["notions_curated"] is False
        suggested = [n["notion_id"] for n in det["notions"]]
        assert suggested, "aucune notion suggérée"
        ex_id = det["exercises"][0]["id"]

        # Notion inconnue / mauvaise matière refusées
        bad = cl.put("/admin/chapters/notions", json={**BODY, "notion_ids": ["math.nexiste-pas"]}, headers=H)
        assert bad.status_code == 400

        # Créer une notion canonique, idempotent sur le label
        n1 = cl.post("/admin/chapters/registry-notion",
                     json={"matiere_id": "math", "label": "Forme exponentielle d'un complexe"}, headers=H).json()
        n2 = cl.post("/admin/chapters/registry-notion",
                     json={"matiere_id": "math", "label": "forme exponentielle d'un complexe"}, headers=H).json()
        assert n1["created"] is True and n2["created"] is False and n1["notion_id"] == n2["notion_id"]

        # Fixer la liste
        chosen = [suggested[0], n1["notion_id"]]
        r = cl.put("/admin/chapters/notions", json={**BODY, "notion_ids": chosen + [chosen[0]]}, headers=H)
        assert r.status_code == 200 and r.json()["notion_ids"] == chosen

        # Valider un exercice + lui donner une correction et la nouvelle notion
        cl.patch(f"/admin/exercises/{ex_id}", headers=H, json={
            "validated_by_admin": True,
            "correction": "Correction de test $z = 1 + i$",
            "notion_ids": [suggested[0], n1["notion_id"]],
        })

        # Aperçu : l'exercice validé est visible, les autres sont comptés comme cachés
        pv = cl.get("/admin/chapters/preview", params=CH, headers=H).json()
        first = next(n for n in pv["notions"] if n["notion_id"] == suggested[0])
        assert any(o["id"] == ex_id and o["correction"] for o in first["occurrences"])
        assert all(o["id"] == ex_id for o in first["occurrences"])
        assert first["admin"]["hidden_unvalidated_exercises"] >= 0

        # Publier → visible élève, sans infos admin
        assert cl.post("/admin/chapters/publish", json={**BODY, "published": True}, headers=H).status_code == 200
        pub = cl.get("/catalog/chapter", params=CH, headers=H)
        assert pub.status_code == 200
        v = pub.json()
        assert v["status"] == "published" and "admin" not in v["notions"][0]
        lst = cl.get("/catalog/chapters", params={"filiere": "D"}, headers=H).json()
        assert [i["chapitre"] for i in lst["items"]] == ["Nombres complexes"]
        assert cl.get("/catalog/chapters", params={"filiere": "C"}, headers=H).json()["items"] == []

        # Même chapitre en série C reste non publié
        r = cl.get("/catalog/chapter", params={**CH, "filiere": "C"}, headers=H)
        assert r.status_code == 404

        # Dépublier → de nouveau indisponible
        cl.post("/admin/chapters/publish", json={**BODY, "published": False}, headers=H)
        assert cl.get("/catalog/chapter", params=CH, headers=H).status_code == 404

        # Les fichiers réels n'ont pas été touchés, des backups existent dans tmp
        assert json.loads((tmp / "publications.json").read_text())
        assert list((tmp / "json_backups").glob("publications-*.json"))
    print("OK — tous les tests chapitres passent")


def test_admin_chapters() -> None:
    run()


if __name__ == "__main__":
    run()
