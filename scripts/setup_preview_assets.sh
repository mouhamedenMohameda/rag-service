#!/usr/bin/env bash
# Stage KaTeX + marked + mhchem dans /tmp/preview_assets pour
# que les previews HTML générés par render_exos_html.py marchent
# 100% offline. À relancer après reset de /tmp.
set -euo pipefail

DEST="${PREVIEW_ASSETS_DIR:-/tmp/preview_assets}"
APP_KATEX="/Users/mohameda/Documents/Bac/app/node_modules/katex/dist"

mkdir -p "$DEST"

if [[ -d "$APP_KATEX" ]]; then
  cp "$APP_KATEX/katex.min.css"                 "$DEST/"
  cp "$APP_KATEX/katex.min.js"                  "$DEST/"
  cp "$APP_KATEX/contrib/auto-render.min.js"    "$DEST/"
  cp "$APP_KATEX/contrib/mhchem.min.js"         "$DEST/"
  cp -r "$APP_KATEX/fonts"                      "$DEST/"
  echo "✓ KaTeX copié depuis $APP_KATEX"
else
  echo "⚠️  $APP_KATEX absent — utilise le fallback CDN dans le HTML"
fi

if [[ ! -s "$DEST/marked.min.js" ]]; then
  curl -fsSL -o "$DEST/marked.min.js" https://cdn.jsdelivr.net/npm/marked@13.0.0/marked.min.js
  echo "✓ marked téléchargé"
fi

echo "→ $DEST prêt ($(ls "$DEST" | wc -l | tr -d ' ') fichiers)"
