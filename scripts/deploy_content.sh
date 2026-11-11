#!/usr/bin/env bash
# Déploie en UNE commande tout le contenu vérifié (énoncés, corrections, figures) :
#   bash /opt/rag-service/scripts/deploy_content.sh
#
# 1. site (APP_DIR, défaut /opt/debloquemoi) : git pull ; s'il y a du nouveau
#    (figures, code) → npm run build + redémarrage du service APP_SERVICE ;
# 2. rag-service : git pull, puis pour chaque module de content/ :
#    load_enonces.py (s'il définit ENONCES) puis load_corrections.py (s'il
#    définit CORRECTIONS), toujours avec le contrôle qualité préalable ;
#    un module déjà chargé est simplement « déjà à jour » (rien n'est réécrit) ;
# 3. redémarrage de rag-service et rapport d'avancement.
# Les exercices validés par l'admin ne sont jamais modifiés.
set -uo pipefail

RS="${RS_DIR:-/opt/rag-service}"
APP="${APP_DIR:-/opt/debloquemoi}"
APP_SERVICE="${APP_SERVICE:-debloquemoi}"
PY="$RS/.venv/bin/python"
fail=0

echo "══ Site ($APP)"
if [ -d "$APP/.git" ]; then
  cd "$APP"
  before=$(git rev-parse HEAD)
  git pull --ff-only -q || { echo "✗ git pull du site impossible"; fail=1; }
  if [ "$(git rev-parse HEAD)" != "$before" ]; then
    echo "  nouveautés → build"
    if npm run build >/tmp/deploy_build.log 2>&1; then
      systemctl restart "$APP_SERVICE" && echo "  ✓ site reconstruit et redémarré ($APP_SERVICE)" \
        || { echo "✗ redémarrage de $APP_SERVICE impossible (APP_SERVICE=… pour changer le nom)"; fail=1; }
    else
      echo "✗ npm run build a échoué (voir /tmp/deploy_build.log) — le site n'a PAS été redémarré"; fail=1
    fi
  else
    echo "  déjà à jour"
  fi
else
  echo "  (dossier introuvable, étape sautée)"
fi

echo "══ Contenu ($RS)"
cd "$RS"
git pull --ff-only -q || { echo "✗ git pull de rag-service impossible"; exit 1; }

read -r -a ENO <<<"$($PY - <<'PYEOF'
import importlib, pathlib, sys
sys.path[:0] = ["content", "."]
for p in sorted(pathlib.Path("content").glob("*.py")):
    if p.stem.startswith("_"): continue
    m = importlib.import_module(p.stem)
    if hasattr(m, "ENONCES"): print(p.stem, end=" ")
PYEOF
)"
read -r -a COR <<<"$($PY - <<'PYEOF'
import importlib, pathlib, sys
sys.path[:0] = ["content", "."]
for p in sorted(pathlib.Path("content").glob("*.py")):
    if p.stem.startswith("_"): continue
    m = importlib.import_module(p.stem)
    if hasattr(m, "CORRECTIONS"): print(p.stem, end=" ")
PYEOF
)"

for m in "${ENO[@]}"; do
  out=$("$PY" scripts/load_enonces.py "$m" --apply 2>&1); rc=$?
  new=$(grep -c "^  + " <<<"$out")
  if [ $rc -ne 0 ] || grep -q "✗\|Arrêt" <<<"$out"; then
    echo "✗ énoncés $m :"; grep -E "✗|Arrêt|erreur" <<<"$out" | head -20; fail=1
  else
    echo "  énoncés    $m : $new nouveau(x)"
  fi
done
for m in "${COR[@]}"; do
  out=$("$PY" scripts/load_corrections.py "$m" --apply 2>&1); rc=$?
  new=$(grep -c "^  + " <<<"$out")
  if [ $rc -ne 0 ] || grep -q "✗\|Arrêt" <<<"$out"; then
    echo "✗ corrections $m :"; grep -E "✗|Arrêt|erreur" <<<"$out" | head -20; fail=1
  else
    echo "  corrections $m : $new nouvelle(s)"
  fi
done

systemctl restart rag-service && echo "  ✓ rag-service redémarré" || { echo "✗ redémarrage rag-service impossible"; fail=1; }

echo
"$PY" scripts/progress_report.py --short | tail -14
[ $fail -eq 0 ] && echo "✓ Déploiement terminé sans erreur." || echo "⚠ Déploiement terminé AVEC des erreurs (voir ✗ ci-dessus)."
exit $fail
