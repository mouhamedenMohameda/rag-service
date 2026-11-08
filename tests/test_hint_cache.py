"""Tests du cache des indices : python tests/test_hint_cache.py (depuis rag-service/)."""
from __future__ import annotations

import json
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

import hint_cache  # noqa: E402
from hint_cache import HintCacheStore, build_hint_cache_router  # noqa: E402

H = {"X-Api-Key": "k"}
KEY = "a" * 64


def run() -> None:
    with tempfile.TemporaryDirectory() as d:
        store = HintCacheStore(Path(d) / "hint_cache")
        app = FastAPI()
        app.include_router(build_hint_cache_router(store, api_key="k"))
        cl = TestClient(app)

        assert cl.get(f"/cache/hints/{KEY}").status_code == 401            # sans clé
        assert cl.get("/cache/hints/../../etc", headers=H).status_code in (400, 404)
        assert cl.get("/cache/hints/xyz", headers=H).status_code == 400    # clé invalide
        assert cl.get(f"/cache/hints/{KEY}", headers=H).status_code == 404  # absent
        assert cl.put(f"/cache/hints/{KEY}", headers=H, json={"content": ""}).status_code == 422

        r = cl.put(f"/cache/hints/{KEY}", headers=H, json={"content": "Indice $x$", "model": "m", "usage_total": 12})
        assert r.status_code == 200
        r = cl.get(f"/cache/hints/{KEY}", headers=H)
        assert r.status_code == 200 and r.json()["content"] == "Indice $x$" and r.json()["hits"] == 1
        assert cl.get(f"/cache/hints/{KEY}", headers=H).json()["hits"] == 2
        assert cl.get("/cache/hints-stats", headers=H).json() == {"entries": 1, "hits": 2}

        # Fichier écrit atomiquement, sans .tmp résiduel
        files = list((Path(d) / "hint_cache").rglob("*"))
        assert not [f for f in files if f.suffix == ".tmp"]

        # Expiré → absent
        f = Path(d) / "hint_cache" / KEY[:2] / f"{KEY}.json"
        data = json.loads(f.read_text())
        data["created_ts"] = time.time() - hint_cache.TTL_SECONDS - 10
        f.write_text(json.dumps(data))
        assert cl.get(f"/cache/hints/{KEY}", headers=H).status_code == 404
    print("OK — cache des indices")


def test_hint_cache() -> None:
    run()


if __name__ == "__main__":
    run()
