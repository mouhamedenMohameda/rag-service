"""SVT — chapitre « Immunologie » (séries C et D) :
énoncés retranscrits des PDF officiels, avec les documents (figures) découpés dans
le sujet, + corrections croisées avec les corrigés officiels quand ils existent.

Figures : app/public/static/figures/svt/<id>-docN.jpg (chemin public /static/figures/svt/…).

- ENONCES : ``scripts/load_enonces.py svt_immuno --apply``
- CORRECTIONS : ``scripts/load_corrections.py svt_immuno --apply``
"""

CH = "Immunologie"
FIG = "/static/figures/svt/"

ENONCES: dict[str, dict] = {}
CORRECTIONS: dict[str, dict] = {}


def fig(eid: str, n: int | str, legende: str) -> str:
    return f"![{legende}]({FIG}{eid}-doc{n}.jpg)"


def _add(eid: str, enonce: str, correction: str, chapitres=None, note: str = "") -> None:
    ENONCES[eid] = {"chapitre": CH, "chapitres": list(chapitres or []), "enonce": enonce.strip() + "\n",
                    "note": note, "replace_ocr": True}
    CORRECTIONS[eid] = {"enonce": enonce.strip() + "\n", "correction": correction.strip() + "\n", "note": note}


# ═══════════════════════════════ C 2017 — session normale ═════════════════════

E = "bac-c-2017-sn-svt-ex3"
_add(E, rf"""
**Immunité (4 points)**

Le document ci-contre représente la structure d'une molécule d'anticorps sécrétée par une cellule $X$.

{fig(E, 1, "Structure d'une molécule d'anticorps : site A à l'extrémité des deux bras, site B à la base")}

**1.** Quelle est la nature chimique des anticorps et quelle est leur dénomination exacte ?

**2.** Identifiez la cellule $X$ et précisez son origine.

**3.** Nommez les sites $A$ et $B$.

**4.** Déduisez deux fonctions d'un anticorps.
""", r"""
**1.** Les anticorps sont des **protéines** (glycoprotéines) ; leur dénomination exacte est **immunoglobulines** (Ig).

**2.** La cellule $X$ est un **plasmocyte**. Il provient de la différenciation d'un **lymphocyte B** : un lymphocyte B qui a reconnu un antigène est activé, se multiplie (clone) et se différencie en plasmocytes sécréteurs d'anticorps.

**3.**
- Site $A$ (extrémité des bras, parties variables des chaînes) : **site de fixation de l'antigène**, ou site variable ; sa forme est complémentaire d'un déterminant antigénique précis.
- Site $B$ (base de la molécule, partie constante) : **site effecteur**, ou site constant ; il se fixe sur des récepteurs des cellules phagocytaires et active le complément.

**4.**
- **Neutralisation de l'antigène** : grâce à ses sites $A$, l'anticorps se lie spécifiquement à l'antigène et forme avec lui un complexe immun qui le neutralise.
- **Élimination du complexe immun** : grâce à son site $B$, l'anticorps favorise la phagocytose du complexe immun par les macrophages (et l'activation du complément).
""", note="Correction conforme au corrigé officiel (protéines, immunoglobulines ; plasmocyte issu des LB ; site A variable, site B constant ; neutralisation de l'antigène), complétée : le corrigé cite comme seconde fonction une « aide à l'immunité spécifique » ; la correction précise le rôle du site constant dans l'élimination du complexe immun (phagocytose, complément).")


# ─────────────────────────────────────────────────────────────────────────────
CHECKS: dict[str, list[str]] = {}
