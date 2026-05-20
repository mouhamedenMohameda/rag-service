# Évaluation RAG

Mesure la qualité du retrieval (et plus tard, des réponses générées) contre un
gold set de questions Bac mauritanien.

## Lancer

```bash
# Depuis le dossier rag-service/ (avec le service tournant sur :8001)
make eval

# Ou directement
python eval/eval.py --rag-url http://127.0.0.1:8001
```

Résultats imprimés en console + rapport markdown horodaté dans `eval/runs/`.

## Métriques (Phase 0)

- **Recall@5** : au moins une source attendue présente dans le top-5
- **MRR** : 1 / rang du premier match attendu (0 si aucun)
- **Latence p50 / p95** : sur l'endpoint `/search`

## Schéma de `gold.jsonl`

Une ligne JSON par cas de test :

```json
{
  "id": "math-001",
  "subject": "math",
  "query": "Étudier la fonction f(x) = ln(1+x) - x/(1+x)…",
  "expected_sources": ["BacC2017sn", "Bac C 2002 a 2012"],
  "reference_answer": "...",
  "style_must_have": ["A\\.N\\s*:", "\\\\boxed\\{"]
}
```

- `expected_sources` : substrings recherchées (case-insensitive) dans les noms
  de fichiers retournés. Tolère les variantes de nom.
- `reference_answer` et `style_must_have` : utilisés en Phase 1+ pour évaluer
  les réponses générées (citation accuracy, style score). Ignorés en Phase 0.

## Ajouter un cas

1. Trouver un exercice Bac avec un corrigé fiable dans `drive_archive/`.
2. Identifier le(s) PDF(s) qui devraient ressortir → `expected_sources`.
3. Ajouter une ligne dans `gold.jsonl`.
4. `make eval` pour vérifier que ça tourne.

## A/B test baseline vs hybrid (Phase 2)

Pour comparer le mode embeddings-only au mode hybride BM25+embeddings, bascule
via le `.env` puis redémarre le service :

```bash
# Baseline (embeddings seuls)
sed -i 's/^RAG_USE_BM25=.*/RAG_USE_BM25=false/' /opt/rag-service/.env || \
  echo 'RAG_USE_BM25=false' >> /opt/rag-service/.env
systemctl restart rag-service && sleep 3
make health   # vérifier "mode": "embeddings"
make eval     # rapport sauvé dans eval/runs/<timestamp>.md

# Hybride
sed -i 's/^RAG_USE_BM25=.*/RAG_USE_BM25=true/' /opt/rag-service/.env
systemctl restart rag-service && sleep 3
make health   # vérifier "mode": "hybrid"
make eval
```

Compare ensuite les deux rapports dans `eval/runs/`. Recall@5, MRR et latence
sont chiffrés ; le delta te dit si la fusion RRF aide.
