"""Cache des réponses IA des indices (partagé web + mobile).

Le site Next.js calcule une clé (sha256 de tout ce qui détermine la réponse)
et demande ici si la réponse existe déjà : si oui, aucun appel IA n'est fait.

Stockage : un fichier JSON par clé dans ``<dossier des données>/hint_cache/``
(même dossier que json_bac.json, déjà accessible en écriture par le service),
écriture atomique. Aucune donnée élève n'est stockée : seulement le texte de la
réponse IA, le modèle et la date.

Routes (``X-Api-Key`` S2S) :
  GET  /cache/hints/{key}   → 200 {content, model, created_at, hits} | 404
  PUT  /cache/hints/{key}   body {content, model, usage_total} → 200
  GET  /cache/hints-stats   → {entries, hits}
"""
from __future__ import annotations

import json
import os
import re
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException
from pydantic import BaseModel, Field

KEY_RE = re.compile(r"^[0-9a-f]{64}$")
TTL_SECONDS = 180 * 24 * 3600  # 6 mois
MAX_CONTENT = 60_000


class HintCacheStore:
    def __init__(self, root: Path):
        self.root = Path(root)
        self._lock = threading.Lock()

    def _file(self, key: str) -> Path:
        return self.root / key[:2] / f"{key}.json"

    def get(self, key: str) -> Optional[dict]:
        f = self._file(key)
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (FileNotFoundError, ValueError):
            return None
        created = data.get("created_ts", 0)
        if not data.get("content") or time.time() - created > TTL_SECONDS:
            return None
        # Compteur de réutilisations (best-effort, sert aux stats).
        with self._lock:
            data["hits"] = int(data.get("hits", 0)) + 1
            self._write(f, data)
        return data

    def put(self, key: str, content: str, model: str, usage_total: int) -> None:
        now = time.time()
        data = {
            "content": content,
            "model": model,
            "usage_total": usage_total,
            "created_ts": now,
            "created_at": datetime.fromtimestamp(now, timezone.utc).isoformat(),
            "hits": 0,
        }
        with self._lock:
            self._write(self._file(key), data)

    def stats(self) -> dict:
        entries = hits = 0
        if self.root.exists():
            for f in self.root.glob("*/*.json"):
                entries += 1
                try:
                    hits += int(json.loads(f.read_text(encoding="utf-8")).get("hits", 0))
                except (ValueError, OSError):
                    pass
        return {"entries": entries, "hits": hits}

    @staticmethod
    def _write(path: Path, data: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False)
            os.replace(tmp, path)
        except BaseException:
            try:
                os.unlink(tmp)
            except OSError:
                pass
            raise


class HintCachePut(BaseModel):
    content: str = Field(min_length=1, max_length=MAX_CONTENT)
    model: str = Field(default="", max_length=200)
    usage_total: int = 0


def build_hint_cache_router(store: HintCacheStore, api_key: str) -> APIRouter:
    def require_key(x_api_key: Optional[str] = Header(default=None)) -> None:
        if not x_api_key or x_api_key != api_key:
            raise HTTPException(status_code=401, detail="Clé API invalide")

    router = APIRouter(dependencies=[Depends(require_key)], tags=["hint-cache"])

    def check(key: str) -> None:
        if not KEY_RE.match(key):
            raise HTTPException(status_code=400, detail="Clé de cache invalide")

    @router.get("/cache/hints/{key}")
    def get_hint(key: str) -> dict:
        check(key)
        data = store.get(key)
        if data is None:
            raise HTTPException(status_code=404, detail="absent")
        return {k: data[k] for k in ("content", "model", "created_at", "hits")}

    @router.put("/cache/hints/{key}")
    def put_hint(key: str, body: HintCachePut) -> dict:
        check(key)
        store.put(key, body.content, body.model, body.usage_total)
        return {"ok": True}

    @router.get("/cache/hints-stats")
    def hint_stats() -> dict:
        return store.stats()

    return router
