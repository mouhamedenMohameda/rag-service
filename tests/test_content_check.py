"""Tests du contrôle qualité du contenu (content_check.py)."""
from __future__ import annotations

import importlib
import sys
import types
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "content"))

import content_check as cc  # noqa: E402


def _run(**attrs):
    rep, st = cc.check_module(types.SimpleNamespace(**attrs), katex=False)
    return rep, st


def test_latex_et_typographie_fautifs_detectes():
    texte = (
        "**1°) a)** Calculer $f(x)$.\n\n"
        "b) Montrer que le le réel $\\frac{1}{2$ convient.\n\n"
        "c) Calculer x^2 + 1.\n\n"
        "e) Résoudre (sur l'intervalle.\n\n"
        "**3°)** Tracer $\\sqrt{x}$ $ ."
    )
    rep, _ = _run(ENONCES={"t": {"enonce": texte}})
    errs = " | ".join(rep.errors)
    warns = " | ".join(rep.warnings)
    assert "nombre impair de « $ »" in errs
    assert "accolades déséquilibrées" in errs
    assert "exposant écrit hors de $…$" in errs
    assert "mot répété" in errs
    assert "parenthèses non équilibrées" in warns
    assert "numérotation des questions : [1, 3]" in warns
    assert "sous-questions ['a', 'b', 'c', 'e']" in warns


def test_texte_propre_sans_alerte():
    texte = (
        "**Exercice 1**\n\n**1°) a)** Calculer $f(2)$ (on pourra utiliser la question 2).\n\n"
        "b) En déduire $f'(x)$ (voir 1° a)).\n\n**2°)** Conclure."
    )
    rep, _ = _run(ENONCES={"t": {"enonce": texte}})
    assert rep.errors == []
    assert [w for w in rep.warnings if "orthographe" not in w and "pyspellchecker" not in w] == []


def test_parties_et_numerotation():
    texte = "**I.** Soit $g$.\n\n**1° a)** x\n\nb) y\n\n**II.** Soit $f$.\n\n**1° a)** x\n\nb) y\n\n**2°** z"
    labels = cc.question_labels(texte)
    assert labels == [("I.1", "a"), ("I.1", "b"), ("II.1", "a"), ("II.1", "b"), ("II.2", "")]


def test_correction_incomplete_detectee():
    enonce = "**1)** a) x\n\nb) y\n\n**2)** a) z\n\nb) t"
    correction = "**1) a)** r\n\n**b)** r\n\n**2) b)** r"
    rep, _ = _run(CORRECTIONS={"t": {"enonce": enonce, "correction": correction}})
    assert any("sans réponse" in w and "2 a)" in w for w in rep.warnings)


def test_controles_math():
    rep, st = _run(CHECKS={"t": [
        "racine(x - 2 - ln(x), 3.1, 3.2)",
        "same(D(x*ln(x)), ln(x) + 1)",
        "integ((2 - 2*x)*ln(x), 1, 2, -Rational(1, 2))",
        "en_racine(2*x**2 + ln(x), 0.54, 0.55, 2*x - (1 + ln(x))/x, (4*x**2 - 1)/x)",
        "une_seule(Rational(3, 7), [Rational(3, 7), 35, 210], 'A')",
        "racine(x - 2 - ln(x), 0.2, 0.3)",   # faux
        "same(D(x*ln(x)), ln(x))",            # faux
    ]})
    assert st["controles_math"] == 5
    assert len(rep.errors) == 2


def test_calcul_faux_et_racine_absente():
    if not cc._arith_available():
        pytest.skip("antlr4-python3-runtime absent")
    rep, st = _run(ENONCES={"t": {"enonce": "$\\dfrac{2 + 2i}{2 - 2i} = -i$ et $8 - 40 + 66 - 34 = 0$"}})
    assert st["calculs"] == 2 and len(rep.errors) == 1 and "calcul faux" in rep.errors[0]
    enonce = "Résoudre dans $\\mathbb{C}$ l'équation $z^2 - 8z + 20 = 0$."
    rep, _ = _run(CORRECTIONS={"t": {"enonce": enonce, "correction": "**1)** $z = 4 \\pm 3i$."}})
    assert any("racine(s)" in e for e in rep.errors)
    rep, _ = _run(CORRECTIONS={"t": {"enonce": enonce, "correction": "**1)** Solutions : $4 - 2i$ et $4 + 2i$."}})
    assert not [e for e in rep.errors if "racine" in e]


def test_avertissements_acceptes():
    texte = "**1)** a) x\n\nc) y\n\nb) z"
    rep, st = _run(ENONCES={"t": {"enonce": texte}}, ACCEPTED={"t": ["sous-questions ['a', 'c', 'b']"]})
    assert not [w for w in rep.warnings if "sous-questions" in w]
    assert st["acceptes"] == 1


@pytest.mark.parametrize("name", sorted(p.stem for p in (ROOT / "content").glob("*.py") if not p.stem.startswith("_")))
def test_contenu_versionne_sans_erreur(name):
    rep, _ = cc.check_module(importlib.import_module(name), katex=False, spelling=False)
    assert rep.errors == [], rep.errors[:5]


def test_valeur_approchee_fausse_detectee():
    if not cc._arith_available():
        pytest.skip("antlr4-python3-runtime absent")
    rep, st = _run(ENONCES={"t": {"enonce": "$e^{-2} \\approx 0{,}2$ et $\\sqrt{2} \\approx 1{,}41$ et $p(X = 0) = 0{,}6$"}})
    assert len(rep.errors) == 1 and "valeur approchée fausse" in rep.errors[0]


def test_numerotation_decimale():
    labels = cc.question_labels("**1.** Texte.\n\n**1.1.** a\n\n**1.2.** b\n\n**2.1.1.** c\n\nOn a $x = 1,5$.")
    assert labels == [("1", ""), ("1", ".1"), ("1", ".2"), ("2", ".1.1")]
    rep, _ = _run(CORRECTIONS={"t": {"enonce": "**1.** T\n\n**1.1.** a\n\n**1.2.** b", "correction": "**1.1.** r\n\n**1.2.** r"}})
    assert not [w for w in rep.warnings if "sans réponse" in w]
    rep, _ = _run(CORRECTIONS={"t": {"enonce": "**1.1.** a\n\n**1.2.** b", "correction": "**1.1.** r"}})
    assert any("sans réponse" in w and "1 .2)" in w for w in rep.warnings)
