.PHONY: eval eval-quiet ingest serve health

PYTHON ?= python3
RAG_URL ?= http://127.0.0.1:8001

# ─── Eval ────────────────────────────────────────────────────────────────
# `make eval` exécute eval/eval.py contre le service local. Exit ≠ 0 si
# le recall@5 passe sous le seuil — utile pour CI / pre-deploy.

eval:
	$(PYTHON) eval/eval.py --rag-url $(RAG_URL)

eval-quiet:
	$(PYTHON) eval/eval.py --rag-url $(RAG_URL) --quiet

# ─── Service ─────────────────────────────────────────────────────────────

serve:
	$(PYTHON) server.py

ingest:
	$(PYTHON) ingest.py

health:
	@curl -s $(RAG_URL)/health | $(PYTHON) -m json.tool
