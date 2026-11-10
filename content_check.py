"""Contrôle qualité du contenu pédagogique (énoncés, corrections, cours) avant
chargement dans les données.

Contrôles, pour chaque texte :
  1. LaTeX — délimiteurs $ / $$ appariés, accolades, \\left/\\right,
     \\begin/\\end ; rendu réel de chaque formule par KaTeX (comme dans l'app) ;
     notations mathématiques écrites hors de $…$.
  2. Orthographe — mots hors formules comparés à un dictionnaire français
     (pyspellchecker) + vocabulaire mathématique autorisé.
  3. Typographie — mot répété (« le le »), parenthèses non fermées,
     espace avant une virgule ou un point, double espace.
  4. Logique des questions — numérotation continue (1, 2, 3… ; a, b, c…),
     pas de doublon, renvois « question 3° b) » vers une question existante.
  5. Correction — chaque question de l'énoncé a sa réponse dans la
     correction (même numéro / même lettre), ordre respecté.
  6. Mathématiques — contrôles enregistrés dans le module de contenu
     (``CHECKS = {id: ["expression sympy vraie", …]}``) : racines, encadrements,
     dérivées, valeurs à vérifier… rejoués à chaque contrôle.

Niveaux : ERREUR (bloque le chargement) et ATTENTION (à relire).
Utilisé par scripts/check_content.py et par les scripts de chargement.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# ─────────────────────────────── résultats ────────────────────────────────────


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def err(self, where: str, msg: str) -> None:
        self.errors.append(f"{where} : {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where} : {msg}")

    def extend(self, other: "Report") -> None:
        self.errors += other.errors
        self.warnings += other.warnings


# ─────────────────────────────── découpage ────────────────────────────────────

_MATH_RE = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def split_math(text: str) -> tuple[list[tuple[str, bool]], str]:
    """Renvoie (formules [(source, display)], texte hors formules)."""
    formulas: list[tuple[str, bool]] = []

    def repl(m: re.Match) -> str:
        if m.group(1) is not None:
            formulas.append((m.group(1), True))
        else:
            formulas.append((m.group(2), False))
        return "⟨math⟩"

    plain = _MATH_RE.sub(repl, text)
    plain = _IMG_RE.sub(lambda m: m.group(1), plain)  # image Markdown : on garde la légende
    return formulas, plain


_IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")


def check_images(where: str, text: str, rep: "Report") -> None:
    """Images Markdown : chemin public /static/… et fichier présent dans app/public (si le dossier est là)."""
    roots = [os.environ.get("APP_PUBLIC_DIR", ""), str(Path(__file__).resolve().parent.parent / "app" / "public")]
    root = next((r for r in roots if r and Path(r).is_dir()), None)
    for m in _IMG_RE.finditer(text):
        url = m.group(2)
        if not m.group(1).strip():
            rep.warn(where, f"image sans légende : {url}")
        if not url.startswith("/static/"):
            rep.err(where, f"image hors de /static/ (non servie sans session) : {url}")
            continue
        if root and not (Path(root) / url.lstrip("/")).is_file():
            rep.err(where, f"image introuvable dans app/public : {url}")


# ─────────────────────────────── 1. LaTeX ─────────────────────────────────────


def _forbidden_patterns() -> list[tuple[str, str]]:
    try:
        from katex_validator import FORBIDDEN_PATTERNS  # même liste que pour les cours générés
        return list(FORBIDDEN_PATTERNS)
    except Exception:  # pragma: no cover
        return [(r"\\mathds\b", "\\mathds non supporté"), (r"\\\(", "délimiteur \\( interdit"),
                (r"\\\[", "délimiteur \\[ interdit")]


def check_latex_structure(where: str, text: str, rep: Report) -> None:
    for pat, msg in _forbidden_patterns():
        if re.search(pat, text):
            rep.err(where, msg)
    unescaped = re.sub(r"\\\$", "", text)
    if unescaped.count("$$") % 2:
        rep.err(where, "nombre impair de « $$ »")
    if unescaped.replace("$$", "").count("$") % 2:
        rep.err(where, "nombre impair de « $ » (formule non fermée)")
    formulas, plain = split_math(text)
    for src, _ in formulas:
        depth = 0
        for ch in re.sub(r"\\[{}]", "", src):
            depth += ch == "{"
            depth -= ch == "}"
            if depth < 0:
                break
        if depth != 0:
            rep.err(where, f"accolades déséquilibrées dans ${src[:60]}$")
        if src.count("\\left") != src.count("\\right"):
            rep.err(where, f"\\left/\\right non appariés dans ${src[:60]}$")
        begins = re.findall(r"\\begin\{(\w+\*?)\}", src)
        ends = re.findall(r"\\end\{(\w+\*?)\}", src)
        if begins != ends[::-1] and sorted(begins) != sorted(ends):
            rep.err(where, f"\\begin/\\end non appariés dans ${src[:60]}$")
        if re.search(r"\\(R|N|Z|Q|C)\b(?!\w)", src):
            rep.warn(where, f"macro courte (\\R, \\N…) : préférer \\mathbb{{…}} dans ${src[:50]}$")
    # notations mathématiques hors formules
    for pat, label in [(r"\\(frac|ln|lim|sqrt|vec|int|infty|alpha|mathbb)\b", "commande LaTeX"),
                       (r"(?<![\w*])[a-zA-Z]\^[\w{(]", "exposant"),
                       (r"(?<![\w*])[a-zA-Z]_[\w{]", "indice")]:
        m = re.search(pat, plain)
        if m:
            ctx = plain[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")
            rep.err(where, f"{label} écrit hors de $…$ : « {ctx} »")


def _find_katex() -> str | None:
    env = os.environ.get("KATEX_JS")
    if env and Path(env).exists():
        return env
    for base in (ROOT.parent / "app", Path("/opt/debloquemoi"), ROOT):
        p = base / "node_modules" / "katex" / "dist" / "katex.js"
        if p.exists():
            return str(p)
    return None


def katex_render_all(items: list[tuple[str, str, bool]]) -> tuple[list[tuple[str, str, str]], str | None]:
    """Rend toutes les formules avec KaTeX (node). Renvoie (échecs, avertissement)."""
    katex = _find_katex()
    node = shutil.which("node")
    if not katex or not node:
        return [], "KaTeX/node introuvable : rendu des formules non vérifié (définir KATEX_JS)"
    script = (
        "const k=require(process.argv[1]);let d='';process.stdin.on('data',c=>d+=c);"
        "process.stdin.on('end',()=>{const a=JSON.parse(d),o=[];"
        "for(const [w,s,disp] of a){try{k.renderToString(s,{displayMode:disp,throwOnError:true,strict:'ignore'})}"
        "catch(e){o.push([w,s,String(e.message).slice(0,120)])}}"
        "process.stdout.write(JSON.stringify(o))})"
    )
    out = subprocess.run([node, "-e", script, katex], input=json.dumps(items),
                         capture_output=True, text=True, timeout=180)
    if out.returncode != 0:
        return [], f"échec de node/KaTeX : {out.stderr[:200]}"
    return [tuple(x) for x in json.loads(out.stdout or "[]")], None


# ─────────────────────────────── 2-3. Orthographe et typographie ──────────────

# Mots corrects absents du dictionnaire (vocabulaire mathématique, sigles…).
WHITELIST = set("""
orthonormé orthonormée orthonormal orthonormale repère repères bijection bijective bijections réciproque réciproques
asymptote asymptotes asymptotique abscisse abscisses ordonnée ordonnées affixe affixes conjugué conjugués
barycentre isobarycentre homothétie homothéties similitude similitudes translation rotation linéarisation
dérivabilité dérivable dérivables primitive primitives intégrale intégrales intégration exponentielle exponentielles
logarithme logarithmes népérien neperien décimal trigonométrique trigonométriques imaginaire imaginaires
complexe complexes polynôme polynômes trinôme trinômes discriminant parabole hyperbole ellipse équilatère excentricité
directrice directrices foyer foyers sommet sommets tangente tangentes inflexion parallélogramme rectangle isocèle
encadrement encadrer majorée minorée majorant minorant monotone convergente divergente géométrique arithmétique
indiscernables équiprobables espérance variance probabilité probabilités événement événements évènement évènements
qcm sujet bac série séries session complémentaire normale exercice exercices énoncé énoncés corrigé corrigés
sympy katex latex ipn igenrse pdf ocr mauritanie mauritanien mauritanienne nouakchott
cm unité unités ua mru dm mm km ml
ln log exp sin cos tan lim inf sup max min arg re im
cf ex éq resp
géométriquement inéquation inéquations croissances binôme euler linéariser moivre factorise factoriser horner
binomiale binomiales ième ièmes colinéaires colinéaire triplet triplets
fig newton newtons oscillateur oscillateurs radians linéairement paramétriques élongation élongations
anti doc docs gamétogenèse germinale germinales légendez légender cytoplasme dupliqué dupliqués endomètre folliculaire
folliculaires fœtale granulosa haploïde diploïde lutéale lutéales métaphase prophase anaphase télophase oviducte
ovocyte ovocytes ovogenèse spermatocyte spermatocytes spermatogenèse spermatide spermatides séminifère séminifères
thèque thèques œstradiol œstrogène œstrogènes progestérone ovariectomie antrum chorionique gnrh fsh lh hcg hpl
gonadotrope gonadotropes graaf hypersécrétion hyposécrétion hypophysaire hypothalamus hypothalamique lactogène
mifépristone progestatif progestatifs placentaire prolactine pronucléus rétrocontrôle trophoblaste nidation
spermatogonie spermatogonies ovogonie ovogonies testostérone leydig sertoli castration castré castrée ovulation
menstruation menstruel menstruelle hypophyse ovarien ovarienne ovariens ovariennes utérin utérine utérins
pubère puberté gestation lutéinisante folliculostimulante endométrial pelvien muqueuse ménopause atrésie
spermatozoïde spermatozoïdes acrosome zygote embryon méiose mitose chromatide chromatides gonade gonades
galiléen galiléenne géocentrique héliocentrique géostationnaire tangentielle kepler antineutrino nucléide nucléides
nucléon nucléons xénon webcam mev kev radioactivité désintégration vectoriellement plasmatique hypophysaires gestatif hypothalamo vitro cavitaire mme fivete autosome autosomes caryotype caryotypes cytochalasine gonosome gonosomes porteuse rétrocontrôles scan
""".split())

_WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿŒœÆæ]+(?:['’][A-Za-zÀ-ÖØ-öø-ÿ]+)?")
_SPELL = None


def _speller():
    global _SPELL
    if _SPELL is None:
        try:
            from spellchecker import SpellChecker  # type: ignore
            _SPELL = SpellChecker(language="fr", distance=1)
        except Exception:  # pragma: no cover
            _SPELL = False
    return _SPELL


def check_spelling(where: str, plain: str, rep: Report, extra_ok: set[str]) -> None:
    sp = _speller()
    if sp is False:
        rep.warn(where, "pyspellchecker absent : orthographe non vérifiée (pip install pyspellchecker)")
        return
    text = re.sub(r"\*\*|__|`[^`]*`|https?://\S+", " ", plain)
    words = []
    for w in _WORD_RE.findall(text):
        base = re.split(r"['’]", w)[-1] if re.match(r"^[ldjnmstcqu]+['’]", w, re.I) else w
        if len(base) <= 2 or base.isupper() or any(c.isdigit() for c in base):
            continue
        lw = base.lower()
        if lw in WHITELIST or lw in extra_ok:
            continue
        words.append(lw)
    unknown = sorted(sp.unknown(words))
    if unknown:
        rep.warn(where, "mots inconnus du dictionnaire (à vérifier) : " + ", ".join(unknown[:25]))


def check_typography(where: str, plain: str, rep: Report) -> None:
    for m in re.finditer(r"\b(\w+)\s+\1\b", plain, re.I):
        w = m.group(1).lower()
        a, b = m.group(0).split()[0], m.group(0).split()[-1]
        if a != b and (a[0].isupper() != b[0].isupper()):
            continue  # « Madame A a », « De Graaf » : pas une répétition
        if w not in {"nous", "vous", "tous"} and not w.isdigit():
            rep.err(where, f"mot répété : « {m.group(0)} »")
    stack = 0
    # étiquettes de questions « 1°) », « a) », « II) » en début de ligne (ou après **)
    no_labels = re.sub(r"(?m)(^|\*\*|\n)\s*(?:\d+\s*(?:°\s*\)?|\)|\.(?!\d))|[a-h]\)|[IVX]+\s*[.)])(\s*\**\s*[a-h]\))?", r"\1", plain)
    txt = no_labels.replace("**", "")
    unmatched = False
    label_closers = 0
    for i, ch in enumerate(txt):
        if ch == "(":
            stack += 1
        elif ch == ")":
            # « 3) », « 1° d) », « b) » : renvoi à une question, pas forcément une fermante
            if re.search(r"(?:\d\s*°?\s*|(?<![\w⟩])[a-h])$", txt[max(0, i - 6):i]):
                label_closers += 1
            elif stack:
                stack -= 1
            else:
                unmatched = True
    if unmatched or stack > label_closers:
        rep.warn(where, "parenthèses non équilibrées dans le texte (hors formules)")
    if re.search(r"\s[,.](?!\d)", plain):
        rep.warn(where, "espace avant une virgule ou un point")
    if re.search(r"[^\s|]  +[^\s|]", plain):
        rep.warn(where, "double espace")


# ─────────────────────────────── 4-5. Questions ───────────────────────────────

def question_labels(text: str) -> list[tuple[str, str]]:
    """Liste ordonnée des étiquettes (numéro, lettre) d'un énoncé ou d'une correction."""
    labels: list[tuple[str, str]] = []
    part = ""
    current = ""
    for line in text.splitlines():
        s = line.strip()
        mpart = re.match(r"^\**\s*(?:Partie\s+([A-Z]|[IVX]+)\b\s*:?|([IVX]+)\s*[.)\-–]|([A-D])\s*[.)\-–](?!\d))\s*\**\s*", s)
        if mpart:
            part = next(g for g in mpart.groups() if g) + "."
            current = ""
            s = s[mpart.end():]
        md = re.match(r"^\**\s*(\d+)((?:\.\d+)+)\.?(?!\d|,)", s)  # numérotation décimale 1.1. / 2.1.1.
        if md:
            current = f"{part}{md.group(1)}"
            labels.append((current, md.group(2)))
            continue
        m = re.match(r"^\**\s*(\d+)\s*(?:°\s*\)?|\)|\.(?![\d,]))\s*\**\s*(?:([a-h])\))?", s)
        if m:
            current = f"{part}{m.group(1)}"
            labels.append((current, m.group(2) or ""))
            continue
        m = re.match(r"^\**\s*([a-h])\)", s)
        if m and current:
            labels.append((current, m.group(1)))
    return labels


def check_questions(where: str, text: str, rep: Report) -> list[tuple[str, str]]:
    labels = question_labels(text)
    tops: list[str] = []
    subs: dict[str, list[str]] = {}
    for num, sub in labels:
        if num not in tops:
            tops.append(num)
        if sub:
            subs.setdefault(num, []).append(sub)
    # continuité par partie
    by_part: dict[str, list[int]] = {}
    for t in tops:
        mm = re.match(r"([A-Za-z]*\.?)(\d+)$", t)
        if mm:
            by_part.setdefault(mm.group(1), []).append(int(mm.group(2)))
    for part, nums in by_part.items():
        if nums != list(range(1, len(nums) + 1)):
            rep.warn(where, f"numérotation des questions {('partie ' + part + ' ') if part else ''}: {nums}")
    for num, letters in subs.items():
        letters = [x for x in letters if not x.startswith(".")]
        if not letters:
            continue
        expected = [chr(ord("a") + i) for i in range(len(letters))]
        if letters != expected:
            rep.warn(where, f"question {num} : sous-questions {letters} (attendu {expected})")
    # renvois
    for m in re.finditer(r"question\s+(\d+)\s*°?\s*(?:([a-h])\)|\)?)", text, re.I):
        num, sub = m.group(1), m.group(2)
        nums = {re.sub(r"^[A-Za-z]*\.?", "", t) for t in tops}
        if num not in nums:
            rep.warn(where, f"renvoi vers la question {num} qui n'existe pas")
        elif sub and not any(re.sub(r'^[A-Za-z]*\.?', '', n) == num and s == sub for n, s in labels):
            rep.warn(where, f"renvoi vers la question {num} {sub}) introuvable")
    return labels


def check_correction_coverage(where: str, enonce: str, correction: str, rep: Report) -> None:
    q = [l for l in question_labels(enonce)]
    a = set(question_labels(correction))
    a_nums = {n for n, _ in a}
    missing = []
    for num, sub in q:
        if (num, sub) in a or (not sub and num in a_nums):
            continue
        if sub.startswith(".") and any(n == num and s.startswith(sub + ".") for n, s in a):
            continue  # en-tête 2.1 dont les sous-questions 2.1.1, 2.1.2 sont traitées
        if sub and (num, "") in a and not any(n == num and s for n, s in a):
            continue  # correction groupée pour la question entière
        missing.append(f"{num}{(' ' + sub + ')') if sub else ''}")
    if missing:
        rep.warn(where, "questions sans réponse repérée dans la correction : " + ", ".join(missing[:15]))


# ─────────────────────────────── 6. Mathématiques ─────────────────────────────


def math_namespace() -> dict:
    """Fonctions disponibles dans CHECKS (expressions en x réel ; ln = log, e = E).

    same(a, b)                 a et b égales (évaluées en plusieurs points du domaine)
    racine(f, a, b)            f change de signe sur ]a;b[ et s'y annule
    en_racine(f, a, b, u, v)   u = v au point où f s'annule dans ]a;b[ (ex. f(α) = formule)
    integ(e, a, b, val)        intégrale de e sur [a;b] égale à val
    lim(e, x0, val)            limite de e en x0 (x0 = oo, -oo ou « 0+ » via dir)
    close(a, b)                égalité numérique de deux expressions sans variable
    une_seule(v, [opts], "B")  QCM : seule l'option B vaut v
    nb_egaux(v, [opts])        QCM : nombre d'options égales à v (0 = sujet sans bonne réponse)
    """
    import sympy as sp

    x = sp.Symbol("x", real=True)
    pts = (-2.7, -1.6, -0.55, 0.23, 0.61, 1.37, 2.4, 3.3, 5.9)

    def num(e, p):
        try:
            v = complex(sp.N(sp.sympify(e).subs(x, p), 20))
        except Exception:
            return None
        if v != v or abs(v) == float("inf") or abs(v.imag) > 1e-12:
            return None
        return v.real

    def same(a, b, points=pts):
        n = 0
        for p in points:
            va, vb = num(a, p), num(b, p)
            if va is None or vb is None:
                continue
            if abs(va - vb) > 1e-8 * max(1.0, abs(va)):
                return False
            n += 1
        return n >= 3

    def root_in(f, a, b):
        a, b = float(sp.N(a)), float(sp.N(b))
        fa, fb = num(f, a), num(f, b)
        if fa is None or fb is None or fa * fb >= 0:
            return None
        r = sp.nsolve(f, x, (sp.Float(a), sp.Float(b)), solver="bisect", tol=1e-25)
        return r if a < float(r) < b else None

    def racine(f, a, b):
        return root_in(f, a, b) is not None

    def en_racine(f, a, b, u, v):
        r = root_in(f, a, b)
        return r is not None and abs(num(u, r) - num(v, r)) < 1e-8 * max(1.0, abs(num(u, r)))

    def integ(e, a, b, val):
        return abs(complex(sp.Integral(e, (x, a, b)).evalf(30)) - complex(sp.N(val, 30))) < 1e-9

    def lim(e, x0, val, d="+-"):
        return sp.limit(e, x, x0, d if d != "+-" else ("+" if x0 != sp.oo else "-")) == val

    def close(a, b, tol=1e-9):
        return abs(complex(sp.N(a, 30)) - complex(sp.N(b, 30))) < tol

    def nb_egaux(v, options):
        """Nombre d'options d'un QCM égales à la vraie valeur v (doit valoir 1)."""
        return sum(1 for o in options if close(v, o))

    def une_seule(v, options, lettre):
        """QCM : exactement une option vaut v, et c'est l'option « lettre » (A, B, C…)."""
        idx = [i for i, o in enumerate(options) if close(v, o)]
        return idx == ["ABCDEF".index(lettre)]

    ns = {name: getattr(sp, name) for name in dir(sp) if not name.startswith("_")}
    ns.update(x=x, t=sp.Symbol("t", real=True), z=sp.Symbol("z"), n=sp.Symbol("n", integer=True, positive=True), I=sp.I, e=sp.E, E=sp.E, pi=sp.pi, ln=sp.log, oo=sp.oo, D=lambda f, k=1: sp.diff(f, x, k),
              same=same, racine=racine, nb_egaux=nb_egaux, une_seule=une_seule, en_racine=en_racine, integ=integ, lim=lim, close=close,
              root_in=root_in)
    return ns


def run_checks(where: str, exprs: list[str], rep: Report, ns: dict | None = None) -> int:
    ns = ns or math_namespace()
    ok = 0
    for expr in exprs:
        try:
            res = eval(expr, dict(ns))  # noqa: S307 — contenu écrit par nous, versionné
        except Exception as e:  # pragma: no cover
            rep.err(where, f"contrôle math impossible à évaluer « {expr} » : {e}")
            continue
        if res is True or getattr(res, "is_true", False) or res == True:  # noqa: E712
            ok += 1
        else:
            rep.err(where, f"contrôle math FAUX : {expr}")
    return ok


# ─────────────────────────────── 7. Calculs écrits ────────────────────────────
# Toute égalité purement numérique écrite dans un texte (« $P(2) = 8 - 40 + 66 - 34 = 0$ »
# est vérifiée sur sa partie numérique « 8 - 40 + 66 - 34 = 0 ») est recalculée.

_ARITH_SKIP = re.compile(r"\\(iff|Rightarrow|Leftrightarrow|equiv|approx|text|quad|mathrm|in|notin|ne|neq|leq|geq|le|ge|lim|to|sum|int|prod|vec|overrightarrow|overline|bar|pm|mp|cdots|ldots|dots|mathbb|binom|begin|cap|cup|subset|forall|exists|wedge|vee)\\b|[<>;:,|!]|\\\{|\\\}|\\[|\\]")
_ARITH_CMDS = {"frac", "sqrt", "pi", "times", "cdot", "cos", "sin", "ln", "exp"}


def _numeric(s: str):
    import sympy as sp
    from sympy.parsing.latex import parse_latex
    s = s.strip()
    for a, b in (("\\dfrac", "\\frac"), ("\\tfrac", "\\frac"), ("\\,", ""), ("\\!", ""), ("\\left", ""),
                 ("\\right", ""), ("\\Big", ""), ("\\big", "")):
        s = s.replace(a, b)
    if not s or not re.search(r"\d|(?<![a-zA-Z\\])i(?![a-zA-Z])", s):
        return None
    if s.count("(") != s.count(")") or s.count("{") != s.count("}"):
        return None
    if not set(re.findall(r"\\([a-zA-Z]+)", s)) <= _ARITH_CMDS:
        return None
    rest = re.sub(r"(?<![a-zA-Z])e(?=\^)", "", re.sub(r"\\[a-zA-Z]+", "", s))
    if re.search(r"[a-hj-zA-Z]", rest) or re.search(r"i[a-zA-Z]|[a-zA-Z]i", rest):
        return None
    try:
        v = parse_latex(s)
    except Exception:
        return None
    v = v.xreplace({x: {"i": sp.I, "e": sp.E, "pi": sp.pi}.get(x.name, x) for x in v.free_symbols})
    return None if v.free_symbols else v


def check_arithmetic(where: str, formulas: list[tuple[str, bool]], rep: Report) -> int:
    import sympy as sp
    n = 0
    for f, _ in formulas:
        f = f.replace("{,}", ".")
        for seg in re.split(r"\\(?:iff|Rightarrow|Leftrightarrow|quad|qquad|text\{[^}]*\})|,\s|;|\\\\|&", f):
            if "=" not in seg or _ARITH_SKIP.search(seg):
                continue
            parts = seg.split("=")
            vals = [_numeric(p) for p in parts]
            for a, b, pa, pb in zip(vals, vals[1:], parts, parts[1:]):
                if a is None or b is None:
                    continue
                try:
                    va, d = complex(sp.N(a, 30)), complex(sp.N(a - b, 30))
                except Exception:
                    continue
                n += 1
                if abs(d) > 1e-9 * max(1.0, abs(va)):
                    rep.err(where, f"calcul faux : « {pa.strip()} = {pb.strip()} » ({sp.N(a, 6)} ≠ {sp.N(b, 6)})")
        # Valeurs approchées « a ≈ 0,05 » : l'écart doit rester dans la précision affichée.
        for seg in re.split(r"\\(?:iff|Rightarrow|Leftrightarrow|quad|qquad|text\{[^}]*\})|,\s|;|\\\\|&", f):
            if "\\approx" not in seg and "\\simeq" not in seg:
                continue
            pieces = re.split(r"\\approx|\\simeq", seg)
            for left, right in zip(pieces, pieces[1:]):
                lt, rt = left.split("=")[-1].strip(), right.split("=")[0].strip()
                m = re.fullmatch(r"-?\s*\d+(?:\.(\d+))?", rt)
                if not m:
                    continue
                a = _numeric(lt)
                if a is None:
                    continue
                try:
                    va = complex(sp.N(a, 30))
                except Exception:
                    continue
                if abs(va.imag) > 1e-12:
                    continue
                tol = 0.6 * 10.0 ** (-len(m.group(1) or ""))  # arrondi (pas troncature)
                n += 1
                if abs(va.real - float(rt.replace(" ", ""))) > tol:
                    rep.err(where, f"valeur approchée fausse : « {lt} ≈ {rt} » (vaut {va.real:.6g})")
    return n


def check_roots(where: str, enonce: str, correction: str, rep: Report) -> int:
    """Équations polynomiales en z de l'énoncé (« … = 0 », P(z) défini) : chaque racine
    exacte doit apparaître dans la correction. Renvoie le nombre de racines vérifiées."""
    import sympy as sp
    from sympy.parsing.latex import parse_latex

    z = sp.Symbol("z")

    def parse(s: str):
        for a, b in (("\\dfrac", "\\frac"), ("\\left", ""), ("\\right", ""), ("\\,", ""), ("\\big", ""), ("\\Big", "")):
            s = s.replace(a, b)
        v = parse_latex(s)
        return v.xreplace({q: {"i": sp.I, "e": sp.E, "pi": sp.pi}.get(q.name, q) for q in v.free_symbols})

    polys = []
    for f, _ in split_math(enonce)[0]:
        m = re.match(r"^\s*(?:\(?E_?\d*'?\)?\s*:\s*)?(.*z.*)=\s*0\s*$", f)
        if not m:
            continue
        e = m.group(1)
        if re.search(r"[PpQf]\(z\)", e):
            mm = re.search(r"%s\s*=\s*([^$]+)\$" % re.escape(e.strip()), enonce)
            if not mm:
                continue
            e = mm.group(1)
        try:
            p = sp.expand(parse(e))
            if p.free_symbols == {z} and sp.degree(p, z) >= 2:
                polys.append(p)
        except Exception:
            continue
    roots = set()
    for p in polys:
        roots |= set(sp.solve(p, z))
    if not roots:
        return 0
    vals = []
    for f, _ in split_math(correction)[0]:
        for seg in re.split(r"=|\\pm|:|,|;|\\text\{[^}]*\}|\\quad|\\ |\\\{|\\\}|\\iff|\bou\b|\bet\b", f):
            v = _numeric(seg)
            if v is not None and isinstance(v, sp.Expr):
                vals.append(v)

    def eq(r, v):
        try:
            return abs(complex(sp.N(r - v))) < 1e-9
        except Exception:
            return False

    missing = [r for r in roots if not any(eq(r, v) for v in vals)]
    if missing:
        rep.err(where, "racine(s) de l'équation de l'énoncé absente(s) de la correction : "
                + ", ".join(sp.sstr(r) for r in missing))
    return len(roots) - len(missing)


def _arith_available() -> bool:
    try:
        from sympy.parsing.latex import parse_latex
        parse_latex("1+1")
        return True
    except Exception:
        return False

# ─────────────────────────────── module complet ───────────────────────────────


def check_module(mod, *, katex: bool = True, spelling: bool = True) -> tuple[Report, dict]:
    """Contrôle un module de contenu (ENONCES, CORRECTIONS, NOTIONS, CHECKS)."""
    rep = Report()
    stats = {"textes": 0, "formules": 0, "controles_math": 0, "calculs": 0}
    arith = _arith_available()
    if not arith:
        rep.warn("calculs", "antlr4-python3-runtime==4.11 absent : calculs écrits non revérifiés")
    texts: list[tuple[str, str]] = []
    extra_ok = {w.lower() for w in getattr(mod, "SPELLING_OK", [])}

    for eid, item in getattr(mod, "ENONCES", {}).items():
        texts.append((f"{eid} [énoncé]", item["enonce"]))
    for eid, item in getattr(mod, "CORRECTIONS", {}).items():
        if item.get("enonce"):
            texts.append((f"{eid} [énoncé]", item["enonce"]))
        if item.get("correction"):
            texts.append((f"{eid} [correction]", item["correction"]))
            if item.get("enonce"):
                check_correction_coverage(eid, item["enonce"], item["correction"], rep)
                if arith:
                    stats["racines"] = stats.get("racines", 0) + check_roots(eid, item["enonce"], item["correction"], rep)
    for n in getattr(mod, "NOTIONS", []):
        texts.append((f"{n['id']} [cours]", n.get("lesson", "")))

    katex_items: list[tuple[str, str, bool]] = []
    for where, text in texts:
        stats["textes"] += 1
        check_latex_structure(where, text, rep)
        formulas, plain = split_math(text)
        stats["formules"] += len(formulas)
        if arith:
            stats["calculs"] += check_arithmetic(where, formulas, rep)
        katex_items += [(where, s, d) for s, d in formulas]
        if spelling:
            check_spelling(where, plain, rep, extra_ok)
        check_typography(where, plain, rep)
        check_images(where, text, rep)
        if "[cours]" not in where:
            check_questions(where, text, rep)

    if katex and katex_items:
        fails, warn = katex_render_all(katex_items)
        if warn:
            rep.warn("KaTeX", warn)
        for where, src, msg in fails:
            rep.err(where, f"KaTeX : {msg} — ${src[:70]}$")

    checks = getattr(mod, "CHECKS", {})
    if checks:
        ns = math_namespace()
        for eid, exprs in checks.items():
            stats["controles_math"] += run_checks(eid, exprs, rep, ns)

    # Avertissements relus à la main et acceptés : ACCEPTED = {id: ["extrait du message", …]}
    accepted = getattr(mod, "ACCEPTED", {})
    kept = []
    for w in rep.warnings:
        if any(w.startswith(eid) and any(frag in w for frag in frags) for eid, frags in accepted.items()):
            stats["acceptes"] = stats.get("acceptes", 0) + 1
        else:
            kept.append(w)
    rep.warnings = kept
    return rep, stats
