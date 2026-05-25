#!/usr/bin/env python3
"""Rend une liste d'exos (JSON) en HTML statique avec KaTeX/mhchem.

Pratique pour vérifier visuellement, sans lancer la stack Next.js, que :
- les énoncés sont complets et lisibles ;
- le LaTeX est syntaxiquement correct (KaTeX affiche en rouge ce qui casse) ;
- la correction est cohérente avec l'énoncé.

Usage :
    .venv/bin/python scripts/render_exos_html.py \\
        --source json_bac.json \\
        --filter "annee=2014" \\
        --out /tmp/preview_2014.html
    open /tmp/preview_2014.html

Filtres : "annee=2014", "matiere_id=math", "filiere_id=C", combinables avec
--filter répété. On peut aussi cibler des IDs précis : --id bac-c-2014-sn-math-ex1.
"""
from __future__ import annotations

import argparse
import html
import json
import sys
from pathlib import Path

HTML_TMPL = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>Preview exos</title>
<!-- Fonts KaTeX (file://) — peuplées par scripts/setup_preview_assets.sh -->
<style>__KATEX_CSS__</style>
<script>__KATEX_JS__</script>
<script>__AUTORENDER_JS__</script>
<script>__MHCHEM_JS__</script>
<script>__MARKED_JS__</script>
<style>
  body { font-family: -apple-system, system-ui, sans-serif; max-width: 1400px; margin: 24px auto; padding: 0 16px; color: #1e293b; }
  h1 { font-size: 22px; margin-bottom: 4px; }
  .meta-bar { color: #64748b; font-size: 13px; margin-bottom: 24px; }
  .exo { margin: 32px 0; padding: 16px; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; }
  .exo-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid #e2e8f0; }
  .exo-id { font-family: ui-monospace, monospace; font-size: 13px; color: #475569; }
  .exo-tags { font-size: 12px; color: #64748b; }
  .exo-tags .tag { display: inline-block; padding: 2px 8px; border-radius: 999px; background: #f1f5f9; margin-left: 6px; }
  .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 900px) { .cols { grid-template-columns: 1fr; } }
  .col { padding: 12px; background: #f8fafc; border-radius: 8px; min-height: 60px; }
  .col h3 { margin: 0 0 8px; font-size: 14px; color: #334155; text-transform: uppercase; letter-spacing: 0.5px; }
  .col-body { font-size: 14.5px; line-height: 1.55; }
  .col-body h1, .col-body h2, .col-body h3, .col-body h4 { margin: 14px 0 6px; }
  .col-body h1 { font-size: 18px; }
  .col-body h2 { font-size: 16.5px; }
  .col-body h3 { font-size: 15.5px; color: #475569; }
  .col-body h4 { font-size: 14.5px; color: #64748b; font-weight: 600; }
  .col-body p { margin: 8px 0; }
  .col-body ul, .col-body ol { padding-left: 22px; margin: 6px 0; }
  .col-body table { border-collapse: collapse; margin: 10px 0; font-size: 13.5px; }
  .col-body th, .col-body td { border: 1px solid #cbd5e1; padding: 4px 8px; }
  .col-body code { background: #e2e8f0; padding: 1px 4px; border-radius: 3px; font-size: 13px; }
  .col-body.raw { white-space: pre-wrap; }
  .col-body.empty { color: #94a3b8; font-style: italic; }
  .nav { position: sticky; top: 0; background: #fff; padding: 8px 0; margin-bottom: 16px; border-bottom: 1px solid #e2e8f0; z-index: 10; }
  .nav a { font-size: 12px; margin-right: 8px; text-decoration: none; color: #4f46e5; }
  .nav a:hover { text-decoration: underline; }
  .katex-error { color: #dc2626 !important; }
</style>
</head>
<body>
<h1>Preview exos</h1>
<div class="meta-bar">__META__</div>
<div class="nav">__NAV__</div>
__BODY__
<script>
// Étape 1 — markdown → HTML (marked en mode GFM, sans interpréter `_` au milieu des mots)
// Étape 2 — KaTeX rend les $...$ et $$...$$ dans le HTML produit.
function runPreview() {
  if (typeof marked === "undefined" || typeof renderMathInElement === "undefined") {
    // Affiche un bandeau d'erreur visible pour faciliter le diagnostic
    const banner = document.createElement("div");
    banner.style.cssText = "background:#fee;border:1px solid #f99;padding:12px;margin:12px 0;color:#900;font-size:13px";
    banner.textContent = "⚠️ Libs JS (marked/KaTeX) non chargées — LaTeX affiché en texte brut. Vérifie /tmp/preview_assets ou ta connexion CDN.";
    document.body.insertBefore(banner, document.body.firstChild);
    return;
  }
  marked.setOptions({ gfm: true, breaks: true, headerIds: false, mangle: false });
  document.querySelectorAll(".col-body.md.raw").forEach((el) => {
    const raw = el.textContent;
    if (!raw || !raw.trim() || raw.trim() === "(vide)") return;
    // Protège les blocs $$...$$ et $...$ contre l'interprétation markdown (ex: _f_k_ → <em>)
    // en encodant temporairement leur contenu.
    const stash = [];
    let work = raw
      .replace(/\\$\\$([\\s\\S]+?)\\$\\$/g, (_, m) => { stash.push(["$$", m]); return `@@MATH${stash.length-1}@@`; })
      .replace(/\\$([^\\$\\n]+?)\\$/g,    (_, m) => { stash.push(["$",  m]); return `@@MATH${stash.length-1}@@`; });
    let html = marked.parse(work);
    html = html.replace(/@@MATH(\d+)@@/g, (_, i) => {
      const [d, m] = stash[+i];
      return d + m + d;
    });
    el.innerHTML = html;
    el.classList.remove("raw");
  });
  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "$",  right: "$",  display: false },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true }
    ],
    throwOnError: false,
    strict: false,
    trust: true,
    ignoredTags: ["script", "noscript", "style", "textarea", "code"]
  });
}
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", runPreview);
} else {
  runPreview();
}
</script>
</body>
</html>
"""


def parse_filter(s: str) -> tuple[str, str]:
    if "=" not in s:
        raise argparse.ArgumentTypeError(f"filtre invalide: {s!r} (format: champ=valeur)")
    k, v = s.split("=", 1)
    return k.strip(), v.strip()


def matches(e: dict, filters: list[tuple[str, str]]) -> bool:
    for k, v in filters:
        if str(e.get(k)) != v:
            return False
    return True


def render(e: dict) -> str:
    eid = html.escape(e["id"])
    tags = []
    for k in ("matiere_id", "filiere_id", "annee", "session"):
        if e.get(k) is not None:
            tags.append(f'<span class="tag">{html.escape(str(e[k]))}</span>')
    if e.get("is_probleme"):
        tags.append('<span class="tag" style="background:#fef3c7">Problème</span>')
    if e.get("validated_by_admin"):
        tags.append('<span class="tag" style="background:#dcfce7">Validé</span>')
    enonce = (e.get("ennonce_complet") or "").strip()
    correction = (e.get("correction") or "").strip()
    chap = html.escape(e.get("chapitre") or "")
    return f"""
<div class="exo" id="exo-{eid}">
  <div class="exo-head">
    <div>
      <a class="exo-id" href="#exo-{eid}">{eid}</a>
      {f'<span style="margin-left:8px;color:#64748b">{chap}</span>' if chap else ''}
    </div>
    <div class="exo-tags">{''.join(tags)}</div>
  </div>
  <div class="cols">
    <div class="col">
      <h3>Énoncé · {len(enonce)} c</h3>
      <div class="col-body md raw {'empty' if not enonce else ''}">{html.escape(enonce) if enonce else '(vide)'}</div>
    </div>
    <div class="col">
      <h3>Correction · {len(correction)} c</h3>
      <div class="col-body md raw {'empty' if not correction else ''}">{html.escape(correction) if correction else '(vide)'}</div>
    </div>
  </div>
</div>
"""


ASSETS_DIR = Path("/tmp/preview_assets")


def load_asset(name: str) -> str:
    """Charge un fichier asset, ou retourne une string vide avec warning."""
    p = ASSETS_DIR / name
    if not p.exists():
        print(f"⚠️  Asset manquant : {p} — lance ./scripts/setup_preview_assets.sh", file=sys.stderr)
        return ""
    return p.read_text(encoding="utf-8")


def patch_katex_css(css: str) -> str:
    """Remappe les chemins de fonts vers file:/// pour le CSS inliné."""
    # Le CSS référence ./fonts/KaTeX_Main-Regular.woff2 etc. en relatif.
    # On rewrite vers file:///tmp/preview_assets/fonts/
    return css.replace("url(fonts/", f"url(file://{ASSETS_DIR}/fonts/")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--source", default="json_bac.json", help="JSON source (défaut: json_bac.json)")
    ap.add_argument("--filter", type=parse_filter, action="append", default=[], help="Filtre champ=valeur (répétable)")
    ap.add_argument("--id", action="append", default=[], help="IDs spécifiques (répétable)")
    ap.add_argument("--out", required=True, help="Chemin HTML de sortie")
    args = ap.parse_args()

    data = json.loads(Path(args.source).read_text(encoding="utf-8"))
    if args.id:
        wanted = set(args.id)
        items = [e for e in data if e.get("id") in wanted]
    else:
        items = [e for e in data if matches(e, args.filter)]
    items.sort(key=lambda e: (e.get("annee", 0), e.get("session", ""), str(e.get("exercice_numero", ""))))

    if not items:
        print("Aucun exo ne matche.", file=sys.stderr)
        return 1

    filt_repr = ", ".join(f"{k}={v}" for k, v in args.filter) or ("ids=" + ",".join(args.id) if args.id else "tous")
    meta = f"{args.source} · {len(items)} exos · filtres : {filt_repr}"
    nav = " · ".join(f'<a href="#exo-{html.escape(e["id"])}">{html.escape(e["id"])}</a>' for e in items)
    body = "\n".join(render(e) for e in items)

    out_html = (
        HTML_TMPL
        .replace("__KATEX_CSS__",     patch_katex_css(load_asset("katex.min.css")))
        .replace("__KATEX_JS__",      load_asset("katex.min.js"))
        .replace("__AUTORENDER_JS__", load_asset("auto-render.min.js"))
        .replace("__MHCHEM_JS__",     load_asset("mhchem.min.js"))
        .replace("__MARKED_JS__",     load_asset("marked.min.js"))
        .replace("__META__", html.escape(meta))
        .replace("__NAV__", nav)
        .replace("__BODY__", body)
    )
    Path(args.out).write_text(out_html, encoding="utf-8")
    print(f"✓ {len(items)} exos écrits dans {args.out}")
    print(f"  open {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
