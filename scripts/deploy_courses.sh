#!/usr/bin/env bash
# Déploie le générateur de cours + les 50 cours générés vers le VPS de prod.
#
# Usage :
#   ./scripts/deploy_courses.sh             # backup + sync + restart + healthcheck
#   ./scripts/deploy_courses.sh --code-only # ne synchronise que les .py, pas cours.json
#   ./scripts/deploy_courses.sh --dry-run   # affiche les commandes sans les exécuter
#
# Pré-requis :
#   - Clé SSH config'd pour root@$VPS_HOST
#   - Fichiers existants en local : course_generator.py, katex_validator.py,
#     admin_courses.py, scripts/batch_generate_courses.py, cours.json

set -euo pipefail

VPS_HOST="${VPS_HOST:-5.189.153.144}"
VPS_USER="${VPS_USER:-root}"
VPS_PATH="${VPS_PATH:-/opt/rag-service}"
CODE_ONLY=0
DRY_RUN=0

for arg in "$@"; do
  case "$arg" in
    --code-only) CODE_ONLY=1 ;;
    --dry-run)   DRY_RUN=1 ;;
    *) echo "Argument inconnu : $arg"; exit 1 ;;
  esac
done

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

run() {
  if [[ $DRY_RUN -eq 1 ]]; then
    echo "  [DRY-RUN] $*"
  else
    echo "→ $*"
    eval "$@"
  fi
}

echo "▶ Déploiement vers ${VPS_USER}@${VPS_HOST}:${VPS_PATH}"
echo

# 1. Backup distant de cours.json (si on va l'écraser)
if [[ $CODE_ONLY -eq 0 ]]; then
  STAMP=$(date +%Y%m%d-%H%M%S)
  echo "▶ Backup cours.json distant"
  run "ssh ${VPS_USER}@${VPS_HOST} 'test -f ${VPS_PATH}/cours.json && cp ${VPS_PATH}/cours.json ${VPS_PATH}/cours.json.bak-${STAMP} || true'"
  echo
fi

# 2. Vérifier la clé Groq distante
echo "▶ Vérification GROQ_API_KEY sur le VPS"
HAS_KEY=$(ssh "${VPS_USER}@${VPS_HOST}" "grep -c '^GROQ_API_KEY=' ${VPS_PATH}/.env 2>/dev/null || echo 0" || echo 0)
if [[ "$HAS_KEY" == "0" ]]; then
  echo "  ⚠️  GROQ_API_KEY absente sur le VPS. La régénération à la demande via l'API ne fonctionnera pas."
  echo "      Ajoute-la avec : ssh ${VPS_USER}@${VPS_HOST} 'echo GROQ_API_KEY=gsk_... >> ${VPS_PATH}/.env'"
else
  echo "  ✓ GROQ_API_KEY présente"
fi
echo

# 3. Sync des fichiers
echo "▶ Synchronisation des fichiers"
FILES=(
  "course_generator.py"
  "katex_validator.py"
  "admin_courses.py"
  "scripts/batch_generate_courses.py"
)
if [[ $CODE_ONLY -eq 0 ]]; then
  FILES+=("cours.json")
fi

# Vérifie l'existence locale
for f in "${FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "  ❌ Fichier local manquant : $f"
    exit 1
  fi
done

# rsync avec préservation de l'arborescence relative
for f in "${FILES[@]}"; do
  run "rsync -avh '$f' '${VPS_USER}@${VPS_HOST}:${VPS_PATH}/$f'"
done
echo

# 4. Vérifier l'import Python avant restart (évite de mettre prod en rade)
echo "▶ Sanity-check des imports sur le VPS"
run "ssh ${VPS_USER}@${VPS_HOST} 'cd ${VPS_PATH} && .venv/bin/python -c \"import course_generator, katex_validator, admin_courses; print(\\\"OK imports\\\")\"'"
echo

# 5. Redémarrer le service
echo "▶ Redémarrage du service systemd"
run "ssh ${VPS_USER}@${VPS_HOST} 'systemctl restart rag-service && sleep 1 && systemctl is-active rag-service'"
echo

# 6. Healthcheck
echo "▶ Healthcheck"
run "ssh ${VPS_USER}@${VPS_HOST} 'curl -s http://127.0.0.1:8001/health'"
echo

# 7. Vérification finale du nombre de cours
echo "▶ Vérification : combien de cours math sont servis ?"
run "ssh ${VPS_USER}@${VPS_HOST} 'RAG_KEY=\$(grep ^RAG_S2S_KEY ${VPS_PATH}/.env | cut -d= -f2-) && curl -s -H \"X-Api-Key: \$RAG_KEY\" \"http://127.0.0.1:8001/admin/courses/notions?matiere=math&has_course=true&limit=1\" | python3 -c \"import json,sys; d=json.load(sys.stdin); print(f\\\"Cours math en prod : {d[\\\\\\\"stats\\\\\\\"][\\\\\\\"with_course\\\\\\\"]}\\\")\"'"
echo

echo "✅ Déploiement terminé"
echo
echo "Prochaines étapes côté UI :"
echo "  1. Ouvrir l'admin Débloque-moi → Cours → matière=math, has_course=true"
echo "  2. Vérifier le rendu KaTeX sur quelques notions (similitude, intégrales)"
echo "  3. Si une notion a un cours médiocre : régénérer via le bouton, le nouveau"
echo "     prompt s'appliquera automatiquement."
