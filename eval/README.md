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
