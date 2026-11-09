"""Fonctions log/exp — série C (2015-2025) : énoncés retranscrits des PDF officiels
+ corrections vérifiées.

- ENONCES : texte retranscrit depuis les sujets (drive_archive/annals/Sujets corrigés
  math/bac c), en remplacement du texte OCR (``replace_ocr``) ; chargé par
  ``scripts/load_enonces.py logexp_c --apply``.
- CORRECTIONS : correction de chaque exercice, calculs refaits par calcul formel
  (CHECKS en fin de fichier) ; chargé ensuite par
  ``scripts/load_corrections.py logexp_c --apply``.
Les erreurs ou coquilles du sujet sont signalées dans les notes et dans la correction.
"""

CH = "Fonctions Logarithmes et Exponentielles"
IP = "Intégration et Primitives"
SU = "Suites numériques"
FN = "Fonctions numériques (Limites et Continuité)"

ENONCES: dict[str, dict] = {}
CORRECTIONS: dict[str, dict] = {}


def _add(eid: str, enonce: str, correction: str, chapitres=None, note: str = "", chapitre: str = CH,
         note_correction: str = "") -> None:
    ENONCES[eid] = {"chapitre": chapitre, "chapitres": list(chapitres or []), "enonce": enonce.strip() + "\n",
                    "note": note, "replace_ocr": True}
    CORRECTIONS[eid] = {"enonce": enonce.strip() + "\n", "correction": correction.strip() + "\n",
                        "note": note_correction or note}


# ═══════════════════════════════ 2015 — session complémentaire ════════════════

_add("bac-c-2015-sc-math-ex4", r"""
**Exercice 4 (4 points)**

**1)** Soit la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = \dfrac{x + 1}{e^x}$.

a) Dresser le tableau de variation de $f$.

b) Tracer $(C)$, la courbe représentative de $f$ dans un repère orthonormé.

**2)** Soit $n \in \mathbb{N}^*$ et $f_n(x) = \dfrac{(1 + x)^n}{e^x}$. Pour tout $x \in \mathbb{R}$, on pose $F_n(x) = \displaystyle\int_{-1}^{x} f_n(t)\,dt$.

Montrer, à l'aide d'une intégration par parties, que pour tout $n \in \mathbb{N}^*$ et pour tout $x \in \mathbb{R}$ : $F_{n+1}(x) = (n + 1)F_n(x) - f_{n+1}(x)$.

**3)** Soit $I_n = F_n(0) = \displaystyle\int_{-1}^{0} f_n(t)\,dt$.

a) Vérifier que pour tout $n \in \mathbb{N}^*$, $I_{n+1} = (n + 1)I_n - 1$.

b) Montrer que la suite $(I_n)$ est décroissante et positive.

c) Montrer que pour tout $n \in \mathbb{N}^*$, $\dfrac{1}{n + 1} \le I_n \le \dfrac{1}{n}$. En déduire $\lim\limits_{n \to +\infty} I_n$.

**4)** Pour tout $n \in \mathbb{N}^*$, on pose $U_n = \dfrac{I_n}{n!}$.

a) Montrer que $U_{n+1} = U_n - \dfrac{1}{(n + 1)!}$. En déduire que $U_n = e - \displaystyle\sum_{k=0}^{n} \dfrac{1}{k!}$.

b) Calculer alors $\lim\limits_{n \to +\infty} \displaystyle\sum_{k=0}^{n} \dfrac{1}{k!}$.
""", r"""
**1) a)** $f(x) = (x + 1)e^{-x}$, donc $f'(x) = e^{-x} - (x + 1)e^{-x} = -xe^{-x}$, du signe de $-x$. $f(0) = 1$.

En $-\infty$ : $x + 1 \to -\infty$ et $e^{-x} \to +\infty$, donc $f(x) \to -\infty$. En $+\infty$ : $f(x) = \dfrac{x}{e^x} + \dfrac{1}{e^x} \to 0$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $-\infty$ | ↗ | $1$ | ↘ | $0$ |

**b)** $(C)$ coupe l'axe des abscisses en $(-1;0)$, a pour maximum $(0;1)$ et l'asymptote $y = 0$ en $+\infty$. En $-\infty$, $\dfrac{f(x)}{x} = \left(1 + \dfrac{1}{x}\right)e^{-x} \to +\infty$ : branche parabolique de direction $(Oy)$.

**2)** Par parties sur $[-1;x]$, avec $u(t) = (1 + t)^{n+1}$ et $v'(t) = e^{-t}$ ($u' = (n + 1)(1 + t)^n$, $v = -e^{-t}$) :
$$F_{n+1}(x) = \big[-(1 + t)^{n+1}e^{-t}\big]_{-1}^{x} + (n + 1)\int_{-1}^{x}(1 + t)^ne^{-t}\,dt = -f_{n+1}(x) + (n + 1)F_n(x),$$
car le crochet est nul en $t = -1$.

**3) a)** En $x = 0$ : $I_{n+1} = (n + 1)I_n - f_{n+1}(0) = (n + 1)I_n - 1$.

**b)** Sur $[-1;0]$, $0 \le 1 + t \le 1$, donc $0 \le (1 + t)^{n+1} \le (1 + t)^n$ et, en multipliant par $e^{-t} > 0$, $0 \le f_{n+1}(t) \le f_n(t)$. En intégrant (bornes dans l'ordre croissant) : $0 \le I_{n+1} \le I_n$.

$(I_n)$ est **décroissante** et **positive**.

**c)** $I_{n+1} \le I_n$ et $I_{n+1} = (n + 1)I_n - 1$ donnent $(n + 1)I_n - 1 \le I_n$, soit $nI_n \le 1$ : $I_n \le \dfrac{1}{n}$.

$I_{n+1} \ge 0$ donne $(n + 1)I_n \ge 1$ : $I_n \ge \dfrac{1}{n + 1}$.

D'après le théorème des gendarmes, $\lim\limits_{n \to +\infty} I_n = 0$.

**4) a)** $U_{n+1} = \dfrac{I_{n+1}}{(n + 1)!} = \dfrac{(n + 1)I_n - 1}{(n + 1)!} = \dfrac{I_n}{n!} - \dfrac{1}{(n + 1)!} = U_n - \dfrac{1}{(n + 1)!}$.

$U_1 = I_1 = \displaystyle\int_{-1}^{0}(1 + t)e^{-t}\,dt = \big[-(t + 2)e^{-t}\big]_{-1}^{0} = -2 + e$, donc $U_1 = e - \left(\dfrac{1}{0!} + \dfrac{1}{1!}\right)$.

Par récurrence, si $U_n = e - \displaystyle\sum_{k=0}^{n}\dfrac{1}{k!}$, alors $U_{n+1} = e - \displaystyle\sum_{k=0}^{n}\dfrac{1}{k!} - \dfrac{1}{(n + 1)!} = e - \sum_{k=0}^{n+1}\dfrac{1}{k!}$.

**b)** $0 \le U_n = \dfrac{I_n}{n!} \le \dfrac{1}{n \cdot n!} \to 0$, donc $\lim\limits_{n \to +\infty} U_n = 0$ et
$$\lim\limits_{n \to +\infty} \sum_{k=0}^{n} \dfrac{1}{k!} = e.$$
""", [IP, SU])

_add("bac-c-2015-sc-math-ex5", r"""
**Exercice 5 (5 points)**

Soit $f$ la fonction définie par $f(x) = x\ln(x + 1)$ et $(C)$ sa courbe représentative dans un repère orthonormé.

**1. a)** Justifier que $\lim\limits_{x \to -1^+} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$. Interpréter graphiquement.

b) Calculer $f'(x)$ et justifier que : si $-1 < x \le 0$ alors $f'(x) \le 0$ ; si $x \ge 0$ alors $f'(x) \ge 0$.

c) Dresser le tableau de variation de $f$.

**2. a)** Tracer la courbe $(C)$.

b) En remarquant que $\dfrac{x^2}{1 + x} = x - 1 + \dfrac{1}{1 + x}$, calculer $\displaystyle\int_0^1 \dfrac{x^2}{1 + x}\,dx$.

c) En utilisant une intégration par parties, calculer l'aire $A$ du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 0$ et $x = 1$.

**3)** Pour tout entier naturel non nul $n$, on pose : $U_n = \displaystyle\int_0^1 x^n\ln(1 + x)\,dx$.

a) Montrer que l'écriture précédente définit bien une suite numérique $(U_n)$. Justifier que $U_1 = \dfrac{1}{4}$.

b) Montrer que pour tout $n \in \mathbb{N}^*$ : $0 \le U_n \le \dfrac{\ln 2}{n + 1}$. En déduire $\lim\limits_{n \to +\infty} U_n$.

**4)** Pour tout $n \ge 2$ et pour tout réel $x$ de $[0;1]$, on pose : $S_n(x) = 1 - x + x^2 - x^3 + x^4 - \dots + (-x)^n$.

a) Justifier que : $S_n(x) = \dfrac{1}{1 + x} - (-1)^{n+1}\dfrac{x^{n+1}}{1 + x}$.

b) Montrer que : $\displaystyle\sum_{k=0}^{n} \dfrac{(-1)^k}{k + 1} = \ln 2 - (-1)^{n+1}\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx$.

c) En utilisant une intégration par parties, montrer que :
$$U_n = \dfrac{\ln 2}{n + 1} - \dfrac{(-1)^{n+1}}{n + 1}\left(\ln 2 - \sum_{k=0}^{n} \dfrac{(-1)^k}{k + 1}\right).$$

**5)** Soit $V_n = 1 - \dfrac{1}{2} + \dfrac{1}{3} - \dfrac{1}{4} + \dots + \dfrac{(-1)^n}{n + 1}$.

a) Montrer que : $\dfrac{1}{2(n + 2)} \le \displaystyle\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx \le \dfrac{1}{n + 2}$.

b) En déduire que : $\lim\limits_{n \to +\infty} V_n = \ln 2$.

c) En déduire $\lim\limits_{n \to +\infty} (n + 1)U_n$.
""", r"""
$f$ est définie pour $x + 1 > 0$, c'est-à-dire sur $]-1;+\infty[$ (le sujet écrit « sur $\mathbb{R}$ »).

**1. a)** En $-1^+$ : $x \to -1$ et $\ln(x + 1) \to -\infty$, donc $f(x) \to +\infty$ : la droite $x = -1$ est **asymptote verticale**. En $+\infty$ : $f(x) \to +\infty$, et $\dfrac{f(x)}{x} = \ln(x + 1) \to +\infty$ : **branche parabolique de direction $(Oy)$**.

**b)** $f'(x) = \ln(x + 1) + \dfrac{x}{x + 1}$.
- Si $-1 < x \le 0$ : $x + 1 \le 1$, donc $\ln(x + 1) \le 0$, et $\dfrac{x}{x + 1} \le 0$ : $f'(x) \le 0$.
- Si $x \ge 0$ : $\ln(x + 1) \ge 0$ et $\dfrac{x}{x + 1} \ge 0$ : $f'(x) \ge 0$.

**c)** $f(0) = 0$.

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $0$ | ↗ | $+\infty$ |

**2. a)** $(C)$ : asymptote $x = -1$, minimum $O(0;0)$ avec tangente horizontale, $f(1) = \ln 2$, branche parabolique verticale en $+\infty$.

**b)** $\displaystyle\int_0^1 \dfrac{x^2}{1 + x}\,dx = \left[\dfrac{x^2}{2} - x + \ln(1 + x)\right]_0^1 = \dfrac{1}{2} - 1 + \ln 2 = \ln 2 - \dfrac{1}{2}$.

**c)** Sur $[0;1]$, $f(x) \ge 0$. Par parties, avec $u = \ln(1 + x)$ et $v' = x$ :
$$A = \left[\dfrac{x^2}{2}\ln(1 + x)\right]_0^1 - \dfrac{1}{2}\int_0^1 \dfrac{x^2}{1 + x}\,dx = \dfrac{\ln 2}{2} - \dfrac{1}{2}\left(\ln 2 - \dfrac{1}{2}\right) = \dfrac{1}{4} \text{ u.a.}$$

**3) a)** Pour tout $n \ge 1$, $x \mapsto x^n\ln(1 + x)$ est continue sur $[0;1]$, donc $U_n$ existe : $(U_n)$ est bien définie. $U_1 = \displaystyle\int_0^1 x\ln(1 + x)\,dx = A = \dfrac{1}{4}$.

**b)** Sur $[0;1]$ : $0 \le \ln(1 + x) \le \ln 2$, donc $0 \le x^n\ln(1 + x) \le x^n\ln 2$, d'où
$$0 \le U_n \le \ln 2 \int_0^1 x^n\,dx = \dfrac{\ln 2}{n + 1}.$$

Par le théorème des gendarmes, $\lim\limits_{n \to +\infty} U_n = 0$.

**4) a)** $S_n(x)$ est la somme de $n + 1$ termes d'une suite géométrique de raison $-x \neq 1$ :
$$S_n(x) = \dfrac{1 - (-x)^{n+1}}{1 + x} = \dfrac{1}{1 + x} - (-1)^{n+1}\dfrac{x^{n+1}}{1 + x}.$$

**b)** On intègre sur $[0;1]$ : $\displaystyle\int_0^1 S_n(x)\,dx = \sum_{k=0}^{n} (-1)^k\int_0^1 x^k\,dx = \sum_{k=0}^{n}\dfrac{(-1)^k}{k + 1}$, et
$$\int_0^1 S_n(x)\,dx = \big[\ln(1 + x)\big]_0^1 - (-1)^{n+1}\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx = \ln 2 - (-1)^{n+1}\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx.$$

**c)** Par parties, avec $u = \ln(1 + x)$ et $v' = x^n$ ($v = \dfrac{x^{n+1}}{n + 1}$) :
$$U_n = \dfrac{\ln 2}{n + 1} - \dfrac{1}{n + 1}\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx.$$

D'après b), $\displaystyle\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx = (-1)^{n+1}\left(\ln 2 - \sum_{k=0}^{n}\dfrac{(-1)^k}{k + 1}\right)$ (car $(-1)^{2(n+1)} = 1$), d'où la formule demandée.

**5) a)** Sur $[0;1]$ : $1 \le 1 + x \le 2$, donc $\dfrac{x^{n+1}}{2} \le \dfrac{x^{n+1}}{1 + x} \le x^{n+1}$. En intégrant :
$$\dfrac{1}{2(n + 2)} \le \int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx \le \dfrac{1}{n + 2}.$$

**b)** $V_n = \displaystyle\sum_{k=0}^{n}\dfrac{(-1)^k}{k + 1}$, donc d'après 4) b), $|V_n - \ln 2| = \displaystyle\int_0^1 \dfrac{x^{n+1}}{1 + x}\,dx \le \dfrac{1}{n + 2} \to 0$ : $\lim\limits_{n \to +\infty} V_n = \ln 2$.

**c)** D'après 4) c) : $(n + 1)U_n = \ln 2 - (-1)^{n+1}(\ln 2 - V_n)$, et $\ln 2 - V_n \to 0$, donc
$$\lim\limits_{n \to +\infty}(n + 1)U_n = \ln 2.$$
""", [IP, SU], note="Le sujet écrit « f définie sur ℝ » : f(x) = x ln(x + 1) n'est définie que sur ]−1 ; +∞[ (corrigé dans l'énoncé, signalé dans la correction).")

# ═══════════════════════════════ 2015 — session normale ═══════════════════════

_add("bac-c-2015-sn-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = \dfrac{1}{1 + e^x}$ et $(C)$ sa courbe représentative dans un repère orthonormé.

**1. a)** Justifier que $\lim\limits_{x \to -\infty} f(x) = 1$ et $\lim\limits_{x \to +\infty} f(x) = 0$. Interpréter graphiquement.

b) Dresser le tableau de variation de $f$.

c) Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ que l'on déterminera. Donner l'expression de sa réciproque $f^{-1}(x)$. On note $(C')$ la courbe de $f^{-1}$ dans le même repère.

**2. a)** Vérifier que le point $\Omega\left(0;\dfrac{1}{2}\right)$ est un centre de symétrie de la courbe $(C)$.

b) Montrer que les courbes $(C)$ et $(C')$ se coupent en un seul point d'abscisse $\alpha$ telle que $0{,}4 < \alpha < 0{,}5$.

c) Tracer les courbes $(C)$ et $(C')$.

d) Calculer, en fonction de $\alpha$, l'aire $A$ du domaine plan limité par les courbes $(C)$ et $(C')$ et les axes des coordonnées (on pourra remarquer que $\dfrac{1}{e^x + 1} = \dfrac{e^{-x}}{e^{-x} + 1}$).

**3)** Pour tout entier $n \in \mathbb{N}^*$, on pose $I_n = \displaystyle\int_0^\alpha f^n(t)\,dt$, où $\alpha$ est le réel trouvé en 2. b).

a) Justifier que $I_1 = \alpha + \ln(2\alpha)$.

b) Vérifier que pour tout réel $x$ : $f'(x) = f^2(x) - f(x)$.

c) Montrer que pour tout $n \in \mathbb{N}^*$ : $I_{n+1} - I_n = \dfrac{1}{n}\left(\alpha^n - \dfrac{1}{2^n}\right)$.

d) Montrer que la suite $(I_n)$ est décroissante et positive. Que peut-on en déduire ?

**4. a)** Montrer que pour tout $n \in \mathbb{N}^*$ : $\alpha^{n+1} \le I_n \le \dfrac{\alpha}{2^n}$. En déduire $\lim\limits_{n \to +\infty} I_n$.

b) Montrer que $I_n = \alpha + \ln(2\alpha) + \displaystyle\sum_{k=1}^{n-1} \dfrac{1}{k}\left(\alpha^k - \dfrac{1}{2^k}\right)$. En déduire $\lim\limits_{n \to +\infty} \displaystyle\sum_{k=1}^{n-1} \dfrac{1}{k}\left(\alpha^k - \dfrac{1}{2^k}\right)$.
""", r"""
**1. a)** $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = 1$ ; $\lim\limits_{x \to +\infty} e^x = +\infty$, donc $\lim\limits_{x \to +\infty} f(x) = 0$.

Les droites $y = 1$ (en $-\infty$) et $y = 0$ (en $+\infty$) sont **asymptotes horizontales**.

**b)** $f'(x) = -\dfrac{e^x}{(1 + e^x)^2} < 0$ : $f$ est strictement décroissante, de $1$ à $0$. $f(0) = \dfrac{1}{2}$.

**c)** $f$ est continue et strictement décroissante : bijection de $\mathbb{R}$ sur $J = ]0;1[$.

Pour $y \in ]0;1[$ : $y = \dfrac{1}{1 + e^x} \iff e^x = \dfrac{1}{y} - 1 = \dfrac{1 - y}{y} \iff x = \ln\dfrac{1 - y}{y}$. Donc
$$f^{-1}(x) = \ln\left(\dfrac{1 - x}{x}\right), \quad x \in ]0;1[.$$

**2. a)** Pour tout réel $x$ : $f(-x) + f(x) = \dfrac{1}{1 + e^{-x}} + \dfrac{1}{1 + e^x} = \dfrac{e^x}{e^x + 1} + \dfrac{1}{1 + e^x} = 1 = 2 \times \dfrac{1}{2}$ : $\Omega\left(0;\dfrac{1}{2}\right)$ est centre de symétrie de $(C)$.

**b)** $M(x;y) \in (C) \cap (C') \iff y = f(x)$ et $x = f(y)$, avec $x \in ]0;1[$. Alors $x = f(f(x))$.

$|f'(t)| = \dfrac{e^t}{(1 + e^t)^2} \le \dfrac{1}{4}$ (car $(1 + e^t)^2 \ge 4e^t$), donc $k(x) = f(f(x)) - x$ a une dérivée $f'(f(x))f'(x) - 1 \le \dfrac{1}{16} - 1 < 0$ : $k$ est strictement décroissante et s'annule au plus une fois.

Sur la droite $y = x$ : $f(x) = x \iff x(1 + e^x) = 1$. La fonction $x \mapsto x(1 + e^x)$ est strictement croissante sur $[0;+\infty[$, avec $0{,}4(1 + e^{0{,}4}) \approx 0{,}997 < 1$ et $0{,}5(1 + e^{0{,}5}) \approx 1{,}32 > 1$. Elle prend donc la valeur $1$ une seule fois, en $\alpha \in ]0{,}4;0{,}5[$ ($\alpha \approx 0{,}401$).

Ce point $(\alpha;\alpha)$ est commun à $(C)$ et $(C')$, et c'est le seul.

**c)** $(C)$ : asymptotes $y = 1$ et $y = 0$, centre de symétrie $\Omega$, point $(\alpha;\alpha)$. $(C')$ est sa symétrique par rapport à $y = x$ : asymptotes verticales $x = 0$ et $x = 1$, centre de symétrie $\left(\dfrac{1}{2};0\right)$.

**d)** Le domaine est symétrique par rapport à la droite $y = x$ ; il est limité par l'axe $(Oy)$, $(C)$ de $(0;\frac{1}{2})$ à $(\alpha;\alpha)$, $(C')$ de $(\alpha;\alpha)$ à $(\frac{1}{2};0)$ et l'axe $(Ox)$. Sa moitié située au-dessus de $y = x$ a pour aire $\displaystyle\int_0^\alpha \big(f(x) - x\big)\,dx$, donc
$$A = 2\int_0^\alpha f(x)\,dx - \alpha^2.$$

Une primitive de $\dfrac{e^{-x}}{e^{-x} + 1}$ est $-\ln(1 + e^{-x})$, donc $\displaystyle\int_0^\alpha f(x)\,dx = \ln 2 - \ln(1 + e^{-\alpha})$.

Comme $\alpha(1 + e^\alpha) = 1$ : $e^\alpha = \dfrac{1 - \alpha}{\alpha}$, $e^{-\alpha} = \dfrac{\alpha}{1 - \alpha}$ et $1 + e^{-\alpha} = \dfrac{1}{1 - \alpha}$. Ainsi $\displaystyle\int_0^\alpha f(x)\,dx = \ln\big(2(1 - \alpha)\big)$ et
$$A = 2\ln\big(2(1 - \alpha)\big) - \alpha^2 \text{ u.a.} \approx 0{,}20 \text{ u.a.}$$

**3) a)** $I_1 = \ln\big(2(1 - \alpha)\big)$ (calculé en 2. d). Or $\ln(2\alpha) + \alpha = \ln(2\alpha e^\alpha) = \ln\left(2\alpha \times \dfrac{1 - \alpha}{\alpha}\right) = \ln\big(2(1 - \alpha)\big)$. Donc $I_1 = \alpha + \ln(2\alpha)$.

**b)** $f^2(x) - f(x) = f(x)\big(f(x) - 1\big) = \dfrac{1}{1 + e^x} \times \dfrac{-e^x}{1 + e^x} = -\dfrac{e^x}{(1 + e^x)^2} = f'(x)$.

**c)** $I_{n+1} - I_n = \displaystyle\int_0^\alpha f^{n-1}(t)\big(f^2(t) - f(t)\big)\,dt = \int_0^\alpha f^{n-1}(t)f'(t)\,dt = \left[\dfrac{f^n(t)}{n}\right]_0^\alpha$.

Comme $f(\alpha) = \alpha$ et $f(0) = \dfrac{1}{2}$ : $I_{n+1} - I_n = \dfrac{1}{n}\left(\alpha^n - \dfrac{1}{2^n}\right)$.

**d)** $0 < \alpha < \dfrac{1}{2}$, donc $\alpha^n < \dfrac{1}{2^n}$ et $I_{n+1} - I_n < 0$ : $(I_n)$ est **décroissante**. Comme $f > 0$, $I_n > 0$ : elle est **positive**. Décroissante et minorée, elle est **convergente**.

**4. a)** Sur $[0;\alpha]$, $f$ décroît de $\dfrac{1}{2}$ à $\alpha$ : $\alpha \le f(t) \le \dfrac{1}{2}$, donc $\alpha^n \le f^n(t) \le \dfrac{1}{2^n}$. En intégrant sur un intervalle de longueur $\alpha$ :
$$\alpha^{n+1} \le I_n \le \dfrac{\alpha}{2^n}.$$

Par le théorème des gendarmes, $\lim\limits_{n \to +\infty} I_n = 0$.

**b)** $I_n = I_1 + \displaystyle\sum_{k=1}^{n-1}(I_{k+1} - I_k) = \alpha + \ln(2\alpha) + \sum_{k=1}^{n-1}\dfrac{1}{k}\left(\alpha^k - \dfrac{1}{2^k}\right)$.

Comme $I_n \to 0$ :
$$\lim\limits_{n \to +\infty}\sum_{k=1}^{n-1}\dfrac{1}{k}\left(\alpha^k - \dfrac{1}{2^k}\right) = -\alpha - \ln(2\alpha) = -\ln\big(2(1 - \alpha)\big).$$
""", [IP, SU])

_add("bac-c-2015-sn-math-ex4", r"""
**Exercice 4 (5 points)**

**1)** On considère la fonction numérique $g$ définie sur $\mathbb{R}^*$ par : $g(x) = \dfrac{3x^3 - 12x^2 + 19x - 10}{x^3 - 4x^2 + 5x}$.

a) Déterminer $a$, $b$ et $c$ tels que pour tout $x$ de $\mathbb{R}^*$ : $g(x) = \dfrac{(x - 1)(ax^2 + bx + c)}{x(x^2 - 4x + 5)}$.

b) Étudier le signe de $g(x)$ sur $\mathbb{R}^*$.

**2)** On considère la fonction numérique $f$ définie sur $\mathbb{R}^*$ par : $f(x) = 3x - 3 + \ln\left(\dfrac{x^2 - 4x + 5}{x^2}\right)$, et soit $(C)$ sa courbe représentative dans un repère orthonormé.

a) Calculer $\lim\limits_{x \to 0} f(x)$, interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to -\infty} f(x)$.

c) Montrer que $(C)$ admet deux asymptotes dont l'une, notée $D$, est oblique. Étudier la position relative de $(C)$ et de $D$.

**3. a)** Vérifier que $f'(x) = g(x)$ où $g$ est la fonction définie en 1), et dresser le tableau de variation de $f$.

b) Démontrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$ dont on donnera un encadrement d'amplitude $5 \times 10^{-1}$.

c) Construire $(C)$.

**4)** On se propose dans cette question de calculer l'aire $S$ du domaine délimité par la courbe $(C)$ et les droites d'équations respectives : $y = 3x - 3$, $x = 3$ et $x = 2 + \sqrt{3}$.

a) Vérifier que pour tout réel $x$ on a : $\dfrac{2x^2 - 4x}{x^2 - 4x + 5} = 2\left(1 + \dfrac{2x - 4}{x^2 - 4x + 5} - \dfrac{1}{1 + (x - 2)^2}\right)$.

b) Calculer $A = \displaystyle\int_3^{2+\sqrt{3}} \dfrac{2x - 4}{x^2 - 4x + 5}\,dx$.

c) En posant $x = 2 + \tan t$ pour tout $t \in \left[0;\dfrac{\pi}{2}\right[$, calculer $B = \displaystyle\int_3^{2+\sqrt{3}} \dfrac{1}{1 + (x - 2)^2}\,dx$.

d) En utilisant une intégration par parties, calculer $J = \displaystyle\int_3^{2+\sqrt{3}} \ln(x^2 - 4x + 5)\,dx$ et $K = 2\displaystyle\int_3^{2+\sqrt{3}} \ln x\,dx$. En déduire l'aire $S$ exprimée en unité d'aire.
""", r"""
**1) a)** $3 - 12 + 19 - 10 = 0$ : $1$ est racine du numérateur. $(x - 1)(ax^2 + bx + c) = ax^3 + (b - a)x^2 + (c - b)x - c$, d'où $a = 3$, $b - a = -12$, $c = 10$ : $a = 3$, $b = -9$, $c = 10$ (on vérifie $c - b = 19$). Le dénominateur vaut $x(x^2 - 4x + 5)$.

**b)** $3x^2 - 9x + 10$ a un discriminant $81 - 120 < 0$ : il est toujours positif ; de même $x^2 - 4x + 5 = (x - 2)^2 + 1 > 0$. Donc $g(x)$ a le signe de $\dfrac{x - 1}{x}$ :
- $g(x) > 0$ sur $]-\infty;0[ \cup ]1;+\infty[$ ;
- $g(x) < 0$ sur $]0;1[$ ; $g(1) = 0$.

**2) a)** Quand $x \to 0$ : $\dfrac{x^2 - 4x + 5}{x^2} \to +\infty$, donc $\lim\limits_{x \to 0} f(x) = +\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** $\dfrac{x^2 - 4x + 5}{x^2} \to 1$ en $\pm\infty$, donc le logarithme tend vers $0$ : $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to -\infty} f(x) = -\infty$.

**c)** $f(x) - (3x - 3) = \ln\left(\dfrac{x^2 - 4x + 5}{x^2}\right) \to 0$ en $\pm\infty$ : $D : y = 3x - 3$ est **asymptote oblique** (en $+\infty$ et en $-\infty$). L'autre asymptote est $x = 0$.

$f(x) - (3x - 3) > 0 \iff x^2 - 4x + 5 > x^2 \iff x < \dfrac{5}{4}$. $(C)$ est au-dessus de $D$ sur $]-\infty;0[ \cup \left]0;\dfrac{5}{4}\right[$, au-dessous sur $\left]\dfrac{5}{4};+\infty\right[$, et elles se coupent en $\left(\dfrac{5}{4};\dfrac{3}{4}\right)$.

**3. a)** $f(x) = 3x - 3 + \ln(x^2 - 4x + 5) - 2\ln|x|$, donc
$$f'(x) = 3 + \dfrac{2x - 4}{x^2 - 4x + 5} - \dfrac{2}{x} = \dfrac{3x(x^2 - 4x + 5) + x(2x - 4) - 2(x^2 - 4x + 5)}{x(x^2 - 4x + 5)} = \dfrac{3x^3 - 12x^2 + 19x - 10}{x^3 - 4x^2 + 5x} = g(x).$$

$f(1) = \ln 2$.

| $x$ | $-\infty$ | | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $+\infty$ ‖ $+\infty$ | ↘ | $\ln 2$ | ↗ | $+\infty$ |

**b)** Sur $]0;+\infty[$, $f(x) \ge \ln 2 > 0$ : pas de solution. Sur $]-\infty;0[$, $f$ est continue et strictement croissante de $-\infty$ à $+\infty$ : une unique solution $\alpha$.

$f(-0{,}5) = -4{,}5 + \ln 29 \approx -1{,}13 < 0$ et $f(0^-) = +\infty$ ; plus finement $f(-0{,}4) \approx -0{,}46 < 0$ et $f(-0{,}3) \approx 0{,}35 > 0$. Donc $-0{,}5 < \alpha < 0$ (amplitude $5 \times 10^{-1}$), et même $-0{,}4 < \alpha < -0{,}3$ ($\alpha \approx -0{,}34$).

**c)** On trace l'asymptote $x = 0$, l'asymptote $D$, le point $\left(\dfrac{5}{4};\dfrac{3}{4}\right)$ commun à $(C)$ et $D$, le minimum $(1;\ln 2)$ et le point $(\alpha;0)$.

**4) a)** $1 + (x - 2)^2 = x^2 - 4x + 5$, donc
$$2\left(1 + \dfrac{2x - 4}{x^2 - 4x + 5} - \dfrac{1}{x^2 - 4x + 5}\right) = \dfrac{2(x^2 - 4x + 5) + 4x - 10}{x^2 - 4x + 5} = \dfrac{2x^2 - 4x}{x^2 - 4x + 5}.$$

**b)** $A = \big[\ln(x^2 - 4x + 5)\big]_3^{2+\sqrt{3}} = \ln 4 - \ln 2 = \ln 2$ (car $(\sqrt{3})^2 + 1 = 4$ et $1 + 1 = 2$).

**c)** Avec $x = 2 + \tan t$ : $dx = (1 + \tan^2 t)\,dt$ ; $x = 3 \iff t = \dfrac{\pi}{4}$ et $x = 2 + \sqrt{3} \iff t = \dfrac{\pi}{3}$.
$$B = \int_{\pi/4}^{\pi/3} \dfrac{1 + \tan^2 t}{1 + \tan^2 t}\,dt = \dfrac{\pi}{3} - \dfrac{\pi}{4} = \dfrac{\pi}{12}.$$

**d)** Par parties, avec $u = \ln(x^2 - 4x + 5)$ et $v' = 1$ :
$$J = \big[x\ln(x^2 - 4x + 5)\big]_3^{2+\sqrt{3}} - \int_3^{2+\sqrt{3}} \dfrac{2x^2 - 4x}{x^2 - 4x + 5}\,dx = (2 + \sqrt{3})\ln 4 - 3\ln 2 - 2\big((\sqrt{3} - 1) + A - B\big).$$

$$J = (2\sqrt{3} - 1)\ln 2 - 2\sqrt{3} + 2 + \dfrac{\pi}{6} \approx 0{,}77.$$

$$K = 2\big[x\ln x - x\big]_3^{2+\sqrt{3}} = 2(2 + \sqrt{3})\ln(2 + \sqrt{3}) - 6\ln 3 + 2 - 2\sqrt{3} \approx 1{,}77.$$

Sur $[3;2 + \sqrt{3}]$, $x > \dfrac{5}{4}$ : $(C)$ est au-dessous de $D$, et $f(x) - (3x - 3) = \ln(x^2 - 4x + 5) - 2\ln x$. Donc
$$S = \int_3^{2+\sqrt{3}}\big((3x - 3) - f(x)\big)\,dx = K - J \approx 1{,}01 \text{ u.a.}$$

*Remarque :* le sujet écrit les bornes de $J$ et $K$ « de $2$ à $2 + \sqrt{3}$ ». C'est une coquille : pour obtenir $S$ (et pour utiliser $A$ et $B$), les bornes sont $3$ et $2 + \sqrt{3}$.
""", note="Question 4 d) : le sujet écrit les intégrales J et K de 2 à 2 + √3 ; coquille, les bornes sont 3 et 2 + √3 (cohérence avec A, B et l'aire S). Corrigé dans l'énoncé, signalé dans la correction.")


# ═══════════════════════════════ 2016 — session complémentaire ════════════════

_add("bac-c-2016-sc-math-ex2", r"""
**Exercice 2 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par : $f(x) = (1 + x)e^{-x}$.

Soit $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Vérifier que : $\lim\limits_{x \to -\infty} f(x) = -\infty$, $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = +\infty$ et $\lim\limits_{x \to +\infty} f(x) = 0$.

b) Interpréter les limites précédentes.

**2. a)** Dresser le tableau de variation de $f$ et représenter sa courbe $(C)$.

b) Calculer l'aire $A$ du domaine plan délimité par $(C)$, l'axe des abscisses et les droites d'équations respectives $x = -1$ et $x = 0$.

**3)** Soit la fonction $f_n$ définie sur $\mathbb{R}$ par $f_n(x) = \dfrac{(1 + x)^ne^{-x}}{n!}$ où $n$ est entier naturel non nul.

Montrer que pour tout $x \in [-1;0]$ on a : $0 \le f_n(x) \le \dfrac{e}{n!}$.

**4)** Soit la suite $(I_n)$ définie pour tout $n \in \mathbb{N}^*$ par : $I_n = \displaystyle\int_{-1}^{0} f_n(x)\,dx = \int_{-1}^{0} \dfrac{(1 + x)^ne^{-x}}{n!}\,dx$.

a) En interprétant graphiquement $I_1$, donner sa valeur (on pourra utiliser la question 2. b)).

b) Montrer, à l'aide d'une intégration par parties, que pour tout $n \in \mathbb{N}^*$ : $I_{n+1} = I_n - \dfrac{1}{(n + 1)!}$.

**5)** Soit la suite $(U_n)$ définie pour tout $n \in \mathbb{N}^*$ par : $U_n = \displaystyle\sum_{k=0}^{n} \dfrac{1}{k!}$.

a) Montrer que pour tout $n \in \mathbb{N}^*$ : $I_n = e - U_n$.

b) Démontrer que pour tout $n \in \mathbb{N}^*$ : $0 \le I_n \le \dfrac{e}{n!}$. En déduire $\lim\limits_{n \to +\infty} I_n$.

c) En déduire $\lim\limits_{n \to +\infty} U_n$.
""", r"""
**1. a)** En $-\infty$ : $1 + x \to -\infty$ et $e^{-x} \to +\infty$, donc $f(x) \to -\infty$ ; $\dfrac{f(x)}{x} = \left(\dfrac{1}{x} + 1\right)e^{-x} \to +\infty$. En $+\infty$ : $f(x) = \dfrac{1}{e^x} + \dfrac{x}{e^x} \to 0$.

**b)** En $-\infty$, $(C)$ admet une **branche parabolique de direction $(Oy)$** ; en $+\infty$, la droite $y = 0$ (axe des abscisses) est **asymptote horizontale**.

**2. a)** $f'(x) = e^{-x} - (1 + x)e^{-x} = -xe^{-x}$, du signe de $-x$ ; $f(0) = 1$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $-\infty$ | ↗ | $1$ | ↘ | $0$ |

$(C)$ coupe l'axe des abscisses en $(-1;0)$, passe par son maximum $(0;1)$ avec une tangente horizontale.

**b)** Sur $[-1;0]$, $f(x) \ge 0$. Une primitive de $f$ est $F(x) = -(x + 2)e^{-x}$ (en effet $F'(x) = -e^{-x} + (x + 2)e^{-x} = (x + 1)e^{-x}$). Donc
$$A = \int_{-1}^{0} f(x)\,dx = F(0) - F(-1) = -2 + e = e - 2 \text{ u.a.}$$

**3)** Pour $x \in [-1;0]$ : $0 \le 1 + x \le 1$, donc $0 \le (1 + x)^n \le 1$ ; et $-x \le 1$, donc $0 < e^{-x} \le e$. D'où $0 \le f_n(x) \le \dfrac{e}{n!}$.

**4) a)** $f_1 = f$, donc $I_1$ est l'aire calculée en 2. b) : $I_1 = e - 2$.

**b)** Par parties, avec $u(x) = \dfrac{(1 + x)^{n+1}}{(n + 1)!}$ et $v'(x) = e^{-x}$ ($u'(x) = \dfrac{(1 + x)^n}{n!}$, $v(x) = -e^{-x}$) :
$$I_{n+1} = \left[-\dfrac{(1 + x)^{n+1}e^{-x}}{(n + 1)!}\right]_{-1}^{0} + \int_{-1}^{0}\dfrac{(1 + x)^ne^{-x}}{n!}\,dx = -\dfrac{1}{(n + 1)!} + I_n.$$

**5) a)** Par récurrence. Pour $n = 1$ : $e - U_1 = e - (1 + 1) = e - 2 = I_1$.

Si $I_n = e - U_n$, alors $I_{n+1} = e - U_n - \dfrac{1}{(n + 1)!} = e - U_{n+1}$.

**b)** D'après 3), en intégrant sur $[-1;0]$ (longueur $1$) : $0 \le I_n \le \dfrac{e}{n!}$. Comme $\dfrac{e}{n!} \to 0$, le théorème des gendarmes donne $\lim\limits_{n \to +\infty} I_n = 0$.

**c)** $U_n = e - I_n$, donc $\lim\limits_{n \to +\infty} U_n = e$.
""", [IP, SU], note="Question 4 a) : le sujet écrit « (On pourra utiliser A.2)) » ; il s'agit de l'aire A de la question 2. b).")

_add("bac-c-2016-sc-math-ex3", r"""
**Exercice 3 (5 points)**

On considère la fonction $f$ définie sur $\mathbb{R}$ par : $f(x) = \dfrac{e^{2x} - 1}{6e^x}$.

Soit $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Vérifier que $f$ est impaire et que $\lim\limits_{x \to -\infty} f(x) = -\infty$. En déduire $\lim\limits_{x \to +\infty} f(x)$.

b) Calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

c) Dresser le tableau de variation de $f$.

d) Montrer que l'équation $f(x) = x$ admet dans $\mathbb{R}$ trois solutions dont l'une $\alpha$ vérifie $2{,}8 < \alpha < 2{,}9$.

**2. a)** Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle que l'on déterminera.

b) Vérifier que pour tout réel $x$ : $\big(f(x)\big)^2 - \big(f'(x)\big)^2 = -\dfrac{1}{9}$. En déduire l'expression de $(f^{-1})'(x)$.

c) Soit $x$ un réel quelconque. Exprimer l'intégrale $I(x) = \displaystyle\int_0^x \dfrac{3}{\sqrt{9t^2 + 1}}\,dt$ en fonction de $f^{-1}(x)$.

**3)** Soit $r$ la rotation de centre $O$ et d'angle $\dfrac{\pi}{2}$. Pour tout point $M(x;y)$ on note $r(M) = M'$ et $r(C) = C_1$.

a) Donner l'expression complexe de la rotation $r$ puis écrire les coordonnées $x'$, $y'$ de $M'$ en fonction de $x$ et $y$.

b) Montrer que $(C_1)$ est la courbe représentative de la fonction $h$ définie sur $\mathbb{R}$ par : $h(x) = \ln\left(-3x + \sqrt{9x^2 + 1}\right)$.

c) Montrer que pour tout réel $x$, $h(-x) = f^{-1}(x)$. On note $(C')$ la courbe représentative de $f^{-1}$ dans le repère précédent.

**4. a)** Montrer que les courbes $(C)$ et $(C')$ se coupent en deux points autres que l'origine.

b) Construire, dans le même repère, les courbes $(C)$ et $(C')$ et calculer en fonction de $\alpha$ l'aire du domaine plan délimité par ces deux courbes ($\alpha$ est le nombre indiqué en 1. d)).
""", r"""
On remarque que $f(x) = \dfrac{e^x - e^{-x}}{6}$.

**1. a)** $f(-x) = \dfrac{e^{-x} - e^{x}}{6} = -f(x)$ pour tout réel $x$ : $f$ est **impaire**. En $-\infty$ : $e^x \to 0$ et $e^{-x} \to +\infty$, donc $f(x) \to -\infty$. Comme $f$ est impaire, $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $\dfrac{f(x)}{x} = \dfrac{e^x}{6x} - \dfrac{e^{-x}}{6x} \to +\infty$ en $+\infty$ : **branche parabolique de direction $(Oy)$** (de même en $-\infty$ par symétrie par rapport à $O$).

**c)** $f'(x) = \dfrac{e^x + e^{-x}}{6} > 0$ : $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$, avec $f(0) = 0$.

**d)** Soit $g(x) = f(x) - x$ ; $g$ est impaire et $g(0) = 0$. $g'(x) = \dfrac{e^x + e^{-x}}{6} - 1$ s'annule pour $e^x + e^{-x} = 6$, c'est-à-dire, avec $x > 0$, $e^x = 3 + 2\sqrt{2}$, soit $x_0 = \ln(3 + 2\sqrt{2}) \approx 1{,}76$.

Sur $[0;x_0]$, $g$ décroît : $g(x) < 0$ pour $0 < x \le x_0$. Sur $[x_0;+\infty[$, $g$ est continue, strictement croissante, de $g(x_0) < 0$ à $+\infty$ : elle s'annule une seule fois, en $\alpha$.

$g(2{,}8) \approx -0{,}07 < 0$ et $g(2{,}9) \approx 0{,}12 > 0$, donc $2{,}8 < \alpha < 2{,}9$ ($\alpha \approx 2{,}838$).

Comme $g$ est impaire, les solutions de $f(x) = x$ sont exactement $-\alpha$, $0$ et $\alpha$.

**2. a)** $f$ est continue et strictement croissante sur $\mathbb{R}$, de limites $-\infty$ et $+\infty$ : elle réalise une bijection de $\mathbb{R}$ sur $\mathbb{R}$.

**b)** $\big(f(x)\big)^2 - \big(f'(x)\big)^2 = \dfrac{(e^x - e^{-x})^2 - (e^x + e^{-x})^2}{36} = \dfrac{-4}{36} = -\dfrac{1}{9}$.

Comme $f'(x) > 0$ : $f'(x) = \sqrt{f(x)^2 + \dfrac{1}{9}} = \dfrac{\sqrt{9f(x)^2 + 1}}{3}$. Pour tout réel $x$, $f^{-1}$ est dérivable en $x$ et
$$(f^{-1})'(x) = \dfrac{1}{f'\big(f^{-1}(x)\big)} = \dfrac{3}{\sqrt{9x^2 + 1}}.$$

**c)** $f^{-1}$ est une primitive de $t \mapsto \dfrac{3}{\sqrt{9t^2 + 1}}$ et $f^{-1}(0) = 0$ (car $f(0) = 0$), donc $I(x) = f^{-1}(x) - f^{-1}(0) = f^{-1}(x)$.

**3) a)** $z' = e^{i\pi/2}z = iz$. Avec $z = x + iy$ : $iz = -y + ix$, donc $x' = -y$ et $y' = x$.

**b)** $M'(x';y') \in (C_1) \iff r^{-1}(M') \in (C)$. Or $r^{-1}(M')$ a pour coordonnées $(y';-x')$. Donc
$$M' \in (C_1) \iff -x' = f(y') \iff y' = f^{-1}(-x').$$

Calcul de $f^{-1}$ : $y = f(x) \iff e^{2x} - 6ye^x - 1 = 0 \iff e^x = 3y + \sqrt{9y^2 + 1}$ (seule racine positive de $X^2 - 6yX - 1 = 0$). Donc $f^{-1}(x) = \ln\left(3x + \sqrt{9x^2 + 1}\right)$ et
$$y' = \ln\left(-3x' + \sqrt{9x'^2 + 1}\right) = h(x').$$

$(C_1)$ est la courbe de $h$.

**c)** $h(-x) = \ln\left(3x + \sqrt{9x^2 + 1}\right) = f^{-1}(x)$.

**4. a)** $f$ étant strictement croissante, si $f(x) = y$ et $f(y) = x$ avec $x < y$, on aurait $f(x) < f(y)$, soit $y < x$ : impossible. Les points communs à $(C)$ et $(C')$ sont donc sur la droite $y = x$, et vérifient $f(x) = x$.

D'après 1. d), ce sont $O$, $(\alpha;\alpha)$ et $(-\alpha;-\alpha)$ : deux points autres que l'origine.

**b)** $(C')$ est la symétrique de $(C)$ par rapport à la droite $y = x$. Sur $[0;\alpha]$, $f(x) \le x \le f^{-1}(x)$ ; le domaine est symétrique par rapport à $O$ et par rapport à $y = x$. Son aire vaut
$$\mathcal{A} = 2\int_0^\alpha \big(f^{-1}(x) - f(x)\big)\,dx = 4\int_0^\alpha \big(x - f(x)\big)\,dx = 2\alpha^2 - 4\int_0^\alpha f(x)\,dx.$$

$\displaystyle\int_0^\alpha f(x)\,dx = \left[\dfrac{e^x + e^{-x}}{6}\right]_0^\alpha = f'(\alpha) - \dfrac{1}{3}$, et d'après 2. b) avec $f(\alpha) = \alpha$ : $f'(\alpha) = \dfrac{\sqrt{9\alpha^2 + 1}}{3}$. Donc
$$\mathcal{A} = 2\alpha^2 + \dfrac{4}{3} - \dfrac{4}{3}\sqrt{9\alpha^2 + 1} \text{ u.a.} \approx 6{,}02 \text{ u.a.}$$
""", [IP])

# ═══════════════════════════════ 2016 — session normale ═══════════════════════

_add("bac-c-2016-sn-math-ex3", r"""
**Exercice 3 (4 points)**

**1)** On considère la fonction $f$ définie sur $\mathbb{R}$ par : $\begin{cases} f(x) = xe^{\frac{1}{x}} & \text{si } x \neq 0 \\ f(0) = 0 \end{cases}$

Soit $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

a) Montrer que $\lim\limits_{x \to 0^-} f(x) = 0$ et que $\lim\limits_{x \to 0^+} f(x) = +\infty$. Interpréter.

b) Calculer et interpréter les limites suivantes : $\lim\limits_{x \to 0^-} \dfrac{f(x)}{x}$, $\lim\limits_{x \to -\infty} \big(f(x) - (x + 1)\big)$ et $\lim\limits_{x \to +\infty} \big(f(x) - (x + 1)\big)$.

c) Dresser le tableau de variation de $f$.

d) Construire, dans le repère précédent, la courbe $(C)$.

**2)** On définit pour tout entier $n \in \mathbb{N}^*$ la fonction $f_n$ par $\begin{cases} f_n(x) = xe^{\frac{n}{x}} & \text{si } x \neq 0 \\ f_n(0) = 0 \end{cases}$

Soit $(C_n)$ la courbe représentative de $f_n$ dans le repère précédent $(O;\vec{i},\vec{j})$.

a) Montrer que $(C_n)$ est l'image de $(C)$ par une homothétie $h_n$ de centre $O$ dont on précisera le rapport.

b) Montrer que tous les points $M_n$ de $(C_n)$ en lesquels la tangente est horizontale sont situés sur une même droite $\Delta$ dont on donnera une équation.

c) Sans étudier $f_2$, déduire de ce qui précède le tableau de variation de $f_2$ et la construction de sa courbe $(C_2)$ dans le même repère. Justifier.
""", r"""
**1) a)** Quand $x \to 0^-$ : $\dfrac{1}{x} \to -\infty$, donc $e^{1/x} \to 0$ et $f(x) \to 0 = f(0)$ : $f$ est **continue à gauche en $0$**.

Quand $x \to 0^+$ : avec $X = \dfrac{1}{x} \to +\infty$, $f(x) = \dfrac{e^X}{X} \to +\infty$ : la droite $x = 0$ est **asymptote verticale** (à droite).

**b)** $\lim\limits_{x \to 0^-} \dfrac{f(x)}{x} = \lim\limits_{x \to 0^-} e^{1/x} = 0$ : $f$ est dérivable à gauche en $0$ avec $f'_g(0) = 0$ ; $(C)$ admet en $O$ une **demi-tangente horizontale** (à gauche).

Avec $u = \dfrac{1}{x} \to 0$ quand $x \to \pm\infty$ :
$$f(x) - (x + 1) = x\big(e^{1/x} - 1\big) - 1 = \dfrac{e^u - 1 - u}{u} \to 0,$$
car $\dfrac{e^u - 1 - u}{u} = \dfrac{e^u - 1}{u} - 1 \to 1 - 1 = 0$. La droite $y = x + 1$ est **asymptote oblique** en $-\infty$ et en $+\infty$.

**c)** Pour $x \neq 0$ : $f'(x) = e^{1/x} + x \times \left(-\dfrac{1}{x^2}\right)e^{1/x} = e^{1/x}\,\dfrac{x - 1}{x}$, du signe de $\dfrac{x - 1}{x}$. $f(1) = e$. En $-\infty$, $f(x) \to -\infty$ ; en $+\infty$, $f(x) \to +\infty$.

| $x$ | $-\infty$ | | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $0$ ‖ $+\infty$ | ↘ | $e$ | ↗ | $+\infty$ |

**d)** On trace l'asymptote $y = x + 1$, l'asymptote verticale $x = 0$ (à droite), la demi-tangente horizontale en $O$ (à gauche) et le minimum local $(1;e)$ avec tangente horizontale.

**2) a)** Soit $h_n$ l'homothétie de centre $O$ et de rapport $n$ : elle associe à $M(x;y)$ le point $M'(nx;ny)$.

Pour $x \neq 0$ : $f_n(nx) = nx\,e^{\frac{n}{nx}} = n\,xe^{\frac{1}{x}} = nf(x)$, et $f_n(0) = 0 = nf(0)$. Donc $M(x;y) \in (C) \iff y = f(x) \iff ny = f_n(nx) \iff h_n(M) \in (C_n)$ : $(C_n) = h_n\big((C)\big)$, **rapport $n$**.

**b)** Une homothétie conserve la direction des droites : la tangente à $(C_n)$ en $h_n(M)$ est horizontale si et seulement si la tangente à $(C)$ en $M$ l'est. Sur $(C)$, cela se produit au point $(1;e)$ (et en $O$ pour la demi-tangente à gauche). Donc $M_n = h_n(1;e) = (n;ne)$ (et $O$).

(Directement : $f_n'(x) = e^{n/x}\,\dfrac{x - n}{x}$ s'annule pour $x = n$, et $f_n(n) = ne$.)

Tous ces points vérifient $y = ex$ : ils sont sur la droite $\Delta : y = ex$.

**c)** $(C_2) = h_2\big((C)\big)$, avec $h_2$ de rapport $2 > 0$ qui conserve l'ordre des abscisses et des ordonnées. Les variations de $f_2$ sont celles de $f$ avec les abscisses et les ordonnées multipliées par $2$ :

| $x$ | $-\infty$ | | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f_2(x)$ | $-\infty$ | ↗ | $0$ ‖ $+\infty$ | ↘ | $2e$ | ↗ | $+\infty$ |

$(C_2)$ admet l'asymptote verticale $x = 0$ (image de $x = 0$) et l'asymptote oblique $y = x + 2$ (image de $y = x + 1$ par $h_2$). On la construit point par point : à chaque point $M$ de $(C)$, on associe $M'$ tel que $\overrightarrow{OM'} = 2\overrightarrow{OM}$.
""", [FN], note="Le sujet écrit « On considère la fonction g définie sur ℝ par : f(x) = … » ; la fonction est f (corrigé dans l'énoncé).")

_add("bac-c-2016-sn-math-ex4", r"""
**Exercice 4 (4 points)**

Soit la fonction $f$ définie sur $]-1;+\infty[$ par $f(x) = \ln(x + 1) - \dfrac{x}{x + 1}$. Soit $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Montrer que $\lim\limits_{x \to -1^+} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$ puis calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$. Interpréter.

b) Dresser le tableau de variation de $f$.

c) Montrer que la courbe $(C)$ admet un point d'inflexion dont on donnera les coordonnées.

d) Tracer la courbe $(C)$.

**2. a)** Calculer $\displaystyle\int_0^x \ln(1 + t)\,dt$ et déterminer la primitive $F$ de $f$ sur $]-1;+\infty[$ qui s'annule en $0$ (on pourra écrire $f(x) = \ln(x + 1) - 1 + \dfrac{1}{x + 1}$).

b) Pour tout entier naturel $n \ge 1$, on note $A_n$ l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 0$ et $x = \dfrac{1}{n}$. Donner l'expression de $A_n$ en fonction de $n$.

**3)** Dans la suite de l'exercice on prendra $x$ réel tel que $x \in ]0;1[$ et $n$ un entier naturel non nul.

a) Montrer que pour tout $n$ : $\dfrac{1}{1 + x} = \displaystyle\sum_{k=1}^{n+1} (-1)^{k-1}x^{k-1} + \dfrac{(-1)^{n+1}x^{n+1}}{1 + x}$.

b) En déduire que : $\ln(1 + x) = \displaystyle\sum_{k=1}^{n+1} (-1)^{k-1}\dfrac{x^k}{k} + (-1)^{n+1}\int_0^x \dfrac{t^{n+1}}{1 + t}\,dt$.

c) En utilisant a) et b), montrer que : $f(x) = \displaystyle\sum_{k=1}^{n+1} (-1)^{k-1}\dfrac{1 - k}{k}x^k + \dfrac{(-1)^{n+2}x^{n+2}}{x + 1} + (-1)^{n+1}\int_0^x \dfrac{t^{n+1}}{1 + t}\,dt$.

d) Montrer que : $0 \le \displaystyle\int_0^x \dfrac{t^{n+1}}{1 + t}\,dt \le \dfrac{x^{n+2}}{n + 2}$.

e) En déduire que : $f(x) = \lim\limits_{n \to +\infty} \displaystyle\sum_{k=1}^{n+1} (-1)^{k-1}\dfrac{1 - k}{k}x^k$.
""", r"""
On peut écrire $f(x) = \ln(x + 1) - 1 + \dfrac{1}{x + 1}$, car $\dfrac{x}{x + 1} = 1 - \dfrac{1}{x + 1}$.

**1. a)** En $-1^+$, posons $u = x + 1 \to 0^+$ : $f(x) = \ln u - 1 + \dfrac{1}{u} = \dfrac{u\ln u - u + 1}{u}$. Comme $u\ln u \to 0$, le numérateur tend vers $1$ et $u \to 0^+$ : $f(x) \to +\infty$.

En $+\infty$ : $\ln(x + 1) \to +\infty$ et $\dfrac{x}{x + 1} \to 1$, donc $f(x) \to +\infty$.

$\dfrac{f(x)}{x} = \dfrac{\ln(x + 1)}{x + 1} \times \dfrac{x + 1}{x} - \dfrac{1}{x + 1} \to 0$.

**Interprétation :** la droite $x = -1$ est **asymptote verticale** ; en $+\infty$, $(C)$ admet une **branche parabolique de direction $(Ox)$**.

**b)** $f'(x) = \dfrac{1}{x + 1} - \dfrac{1}{(x + 1)^2} = \dfrac{x}{(x + 1)^2}$, du signe de $x$. $f(0) = 0$.

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $0$ | ↗ | $+\infty$ |

**c)** $f''(x) = -\dfrac{1}{(x + 1)^2} + \dfrac{2}{(x + 1)^3} = \dfrac{1 - x}{(x + 1)^3}$ : elle s'annule en changeant de signe en $x = 1$. $(C)$ admet le point d'inflexion $I\left(1;\ln 2 - \dfrac{1}{2}\right)$.

**d)** On trace l'asymptote $x = -1$, le minimum $O(0;0)$ (tangente horizontale), le point d'inflexion $I$ ($\ln 2 - \frac{1}{2} \approx 0{,}19$) et la branche parabolique.

**2. a)** Par parties ($u = \ln(1 + t)$, $v' = 1$, en prenant $v = 1 + t$) :
$$\int_0^x \ln(1 + t)\,dt = \big[(1 + t)\ln(1 + t)\big]_0^x - \int_0^x 1\,dt = (1 + x)\ln(1 + x) - x.$$

Donc $F(x) = \displaystyle\int_0^x f(t)\,dt = (1 + x)\ln(1 + x) - x - x + \ln(1 + x)$ :
$$F(x) = (x + 2)\ln(x + 1) - 2x.$$

**b)** Sur $\left[0;\dfrac{1}{n}\right]$, $f(x) \ge 0$, donc
$$A_n = F\left(\dfrac{1}{n}\right) = \left(\dfrac{1}{n} + 2\right)\ln\left(1 + \dfrac{1}{n}\right) - \dfrac{2}{n} \text{ u.a.}$$

**3) a)** $\displaystyle\sum_{k=1}^{n+1}(-1)^{k-1}x^{k-1} = \sum_{j=0}^{n}(-x)^j = \dfrac{1 - (-x)^{n+1}}{1 + x} = \dfrac{1}{1 + x} - \dfrac{(-1)^{n+1}x^{n+1}}{1 + x}$, d'où l'égalité.

**b)** On applique a) à $t \in [0;x]$ et on intègre de $0$ à $x$ : $\displaystyle\int_0^x \dfrac{dt}{1 + t} = \ln(1 + x)$ et $\displaystyle\int_0^x t^{k-1}\,dt = \dfrac{x^k}{k}$, d'où le résultat.

**c)** $f(x) = \ln(1 + x) - x \times \dfrac{1}{1 + x}$. D'après a), $x \times \dfrac{1}{1 + x} = \displaystyle\sum_{k=1}^{n+1}(-1)^{k-1}x^k + \dfrac{(-1)^{n+1}x^{n+2}}{1 + x}$. Avec b) :
$$f(x) = \sum_{k=1}^{n+1}(-1)^{k-1}\left(\dfrac{1}{k} - 1\right)x^k - \dfrac{(-1)^{n+1}x^{n+2}}{1 + x} + (-1)^{n+1}\int_0^x \dfrac{t^{n+1}}{1 + t}\,dt,$$
et $\dfrac{1}{k} - 1 = \dfrac{1 - k}{k}$, $-(-1)^{n+1} = (-1)^{n+2}$ : c'est l'égalité demandée.

**d)** Pour $t \in [0;x]$ : $1 + t \ge 1$, donc $0 \le \dfrac{t^{n+1}}{1 + t} \le t^{n+1}$. En intégrant ($x > 0$) : $0 \le \displaystyle\int_0^x \dfrac{t^{n+1}}{1 + t}\,dt \le \dfrac{x^{n+2}}{n + 2}$.

**e)** D'après c) et d) :
$$\left|f(x) - \sum_{k=1}^{n+1}(-1)^{k-1}\dfrac{1 - k}{k}x^k\right| \le \dfrac{x^{n+2}}{1 + x} + \dfrac{x^{n+2}}{n + 2} \le 2x^{n+2}.$$

Comme $0 < x < 1$, $x^{n+2} \to 0$, d'où $f(x) = \lim\limits_{n \to +\infty} \displaystyle\sum_{k=1}^{n+1}(-1)^{k-1}\dfrac{1 - k}{k}x^k$.
""", [IP, SU])

# ═══════════════════════════════ 2017 — session complémentaire ════════════════

_add("bac-c-2017-sc-math-ex4", r"""
**Exercice 4 (4 points)**

Pour tout entier naturel $n$ strictement supérieur à $1$, on définit la fonction $f_n$ sur $]0;+\infty[$ par : $f_n(x) = (\ln x)^n$, et on désigne par $(C_n)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Calculer $\lim\limits_{x \to +\infty} f_n(x)$ et discuter $\lim\limits_{x \to 0^+} f_n(x)$ suivant la parité de $n$.

b) Calculer $f_n'(x)$, dérivée de $f_n(x)$, et dresser le tableau de variations de $f_n$ (suivant la parité de $n$).

**2. a)** Étudier les positions relatives de $(C_2)$ et $(C_3)$.

b) Construire $(C_2)$ et $(C_3)$ dans le même repère.

Pour tout entier naturel $n$ strictement supérieur à $1$, on pose : $I_n = \dfrac{(-1)^n}{n!}\displaystyle\int_1^e f_n(x)\,dx$ et $u_n = \displaystyle\sum_{k=0}^{n} \dfrac{(-1)^k}{k!}$.

**3. a)** Montrer que $I_2 = \dfrac{e - 2}{2}$ (on procédera par intégration par parties).

b) Montrer que pour tout entier naturel $n$ strictement supérieur à $1$, on a : $I_{n+1} = \dfrac{(-1)^{n+1}}{(n + 1)!}e + I_n$.

c) Vérifier que $I_2 = -1 + e\,u_2$.

d) En déduire que $\forall n \ge 2$, $I_n = -1 + e\,u_n$.

**4. a)** Montrer que : $\forall x \in [1;e]$, $0 \le f_n(x) \le 1$. Déduire que $|I_n| \le \dfrac{e - 1}{n!}$.

b) Déduire la limite de $(I_n)$ puis celle de $(u_n)$.
""", r"""
**1. a)** En $+\infty$ : $\ln x \to +\infty$, donc $f_n(x) \to +\infty$.

En $0^+$ : $\ln x \to -\infty$, donc :
- si $n$ est **pair**, $\lim\limits_{x \to 0^+} f_n(x) = +\infty$ ;
- si $n$ est **impair**, $\lim\limits_{x \to 0^+} f_n(x) = -\infty$.

Dans les deux cas, la droite $x = 0$ est asymptote verticale. En $+\infty$, $\dfrac{f_n(x)}{x} \to 0$ : branche parabolique de direction $(Ox)$.

**b)** $f_n'(x) = \dfrac{n(\ln x)^{n-1}}{x}$ ; $f_n(1) = 0$.

**$n$ pair** ($n - 1$ impair) : $f_n'(x)$ a le signe de $\ln x$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f_n'(x)$ | | $-$ | $0$ | $+$ | |
| $f_n(x)$ | ‖ $+\infty$ | ↘ | $0$ | ↗ | $+\infty$ |

**$n$ impair** ($n - 1$ pair) : $f_n'(x) \ge 0$, nulle seulement en $x = 1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f_n'(x)$ | | $+$ | $0$ | $+$ | |
| $f_n(x)$ | ‖ $-\infty$ | ↗ | $0$ | ↗ | $+\infty$ |

(Pour $n$ impair, le point $(1;0)$ est un point d'inflexion à tangente horizontale.)

**2. a)** $f_3(x) - f_2(x) = (\ln x)^2(\ln x - 1)$, du signe de $\ln x - 1$ (et nul en $x = 1$) :
- sur $]0;1[ \cup ]1;e[$ : $(C_3)$ est **au-dessous** de $(C_2)$ ;
- sur $]e;+\infty[$ : $(C_3)$ est **au-dessus** de $(C_2)$ ;
- elles se coupent en $(1;0)$ et $(e;1)$.

**b)** $(C_2)$ : minimum $(1;0)$, asymptote $x = 0$ (vers $+\infty$). $(C_3)$ : point d'inflexion à tangente horizontale $(1;0)$, asymptote $x = 0$ (vers $-\infty$). Points communs $(1;0)$ et $(e;1)$.

**3. a)** Par parties, avec $u = (\ln x)^2$ et $v' = 1$ :
$$\int_1^e (\ln x)^2\,dx = \big[x(\ln x)^2\big]_1^e - 2\int_1^e \ln x\,dx = e - 2\big[x\ln x - x\big]_1^e = e - 2.$$

Donc $I_2 = \dfrac{(-1)^2}{2!}(e - 2) = \dfrac{e - 2}{2}$.

**b)** Par parties, avec $u = (\ln x)^{n+1}$ et $v' = 1$ :
$$\int_1^e (\ln x)^{n+1}\,dx = \big[x(\ln x)^{n+1}\big]_1^e - (n + 1)\int_1^e (\ln x)^n\,dx = e - (n + 1)\int_1^e (\ln x)^n\,dx.$$

En multipliant par $\dfrac{(-1)^{n+1}}{(n + 1)!}$ :
$$I_{n+1} = \dfrac{(-1)^{n+1}}{(n + 1)!}e - \dfrac{(-1)^{n+1}}{n!}\int_1^e (\ln x)^n\,dx = \dfrac{(-1)^{n+1}}{(n + 1)!}e + I_n.$$

**c)** $u_2 = 1 - 1 + \dfrac{1}{2} = \dfrac{1}{2}$, donc $-1 + e\,u_2 = \dfrac{e}{2} - 1 = \dfrac{e - 2}{2} = I_2$.

**d)** Par récurrence : vrai pour $n = 2$ ; si $I_n = -1 + e\,u_n$, alors
$$I_{n+1} = -1 + e\left(u_n + \dfrac{(-1)^{n+1}}{(n + 1)!}\right) = -1 + e\,u_{n+1}.$$

**4. a)** Pour $x \in [1;e]$ : $0 \le \ln x \le 1$, donc $0 \le (\ln x)^n \le 1$. Ainsi $0 \le \displaystyle\int_1^e f_n(x)\,dx \le e - 1$ et
$$|I_n| = \dfrac{1}{n!}\int_1^e f_n(x)\,dx \le \dfrac{e - 1}{n!}.$$

**b)** $\dfrac{e - 1}{n!} \to 0$, donc $\lim\limits_{n \to +\infty} I_n = 0$. Comme $u_n = \dfrac{1 + I_n}{e}$ :
$$\lim\limits_{n \to +\infty} u_n = \dfrac{1}{e}.$$
""", [IP, SU], note="Le sujet numérote deux sous-questions « c) » à la question 3 (la seconde devient d)), et écrit en 2. a) « positions relatives de et (C₂) et (C₃) » (coquille).")

# ═══════════════════════════════ 2017 — session normale ═══════════════════════

_add("bac-c-2017-sn-math-ex3", r"""
**Exercice 3 (5 points)**

Pour tout entier naturel $n$ on définit la fonction $f_n$ sur $\mathbb{R}$ par : $f_n(x) = \dfrac{e^{-nx}}{1 + e^{-x}}$ et soit $(C_n)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1)** Montrer que toutes les courbes $(C_n)$ passent par un point fixe à déterminer.

**2) a)** Dresser le tableau de variation de $f_0$.

b) On considère les points $M$ et $N$ de la courbe $(C_0)$ d'abscisses respectives $x$ et $-x$. Déterminer les coordonnées de $A$, milieu de $[MN]$. Que représente $A$ pour $(C_0)$ ?

**3) a)** Montrer que les courbes $(C_0)$ et $(C_1)$ sont symétriques par rapport à l'axe des ordonnées.

b) Déduire le tableau de variation de $f_1$.

c) Construire $(C_0)$ et $(C_1)$ dans le même repère.

**4)** On suppose que $n$ est strictement supérieur à $1$.

a) Montrer que $\lim\limits_{x \to +\infty} f_n(x) = 0$ et $\lim\limits_{x \to -\infty} f_n(x) = +\infty$ puis calculer $\lim\limits_{x \to -\infty} \dfrac{f_n(x)}{x}$. Interpréter.

b) Calculer $f_n'$ et dresser le tableau de variation de $f_n$.

**5)** Soit $(u_n)$ la suite définie par : $u_n = \displaystyle\int_0^1 f_n(x)\,dx$, $n \in \mathbb{N}$.

a) Justifier l'existence de $(u_n)$ puis vérifier que $u_0 = \ln\left(\dfrac{1 + e}{2}\right)$.

b) Vérifier que $u_0 + u_1 = 1$ et que $u_{n+1} + u_n = \dfrac{1 - e^{-n}}{n}$ puis déduire $u_1$ et $u_2$.

c) Montrer que $(u_n)$ est convergente et calculer sa limite.
""", r"""
**1)** Pour tout $n$ : $f_n(0) = \dfrac{1}{1 + 1} = \dfrac{1}{2}$. Toutes les courbes passent par le point $\left(0;\dfrac{1}{2}\right)$.

**2) a)** $f_0(x) = \dfrac{1}{1 + e^{-x}}$ ; $f_0'(x) = \dfrac{e^{-x}}{(1 + e^{-x})^2} > 0$. En $-\infty$, $e^{-x} \to +\infty$ et $f_0(x) \to 0$ ; en $+\infty$, $f_0(x) \to 1$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f_0'(x)$ | | $+$ | | $+$ | |
| $f_0(x)$ | $0$ | ↗ | $\frac{1}{2}$ | ↗ | $1$ |

Asymptotes horizontales : $y = 0$ en $-\infty$, $y = 1$ en $+\infty$.

**b)** $f_0(-x) = \dfrac{1}{1 + e^{x}} = \dfrac{e^{-x}}{e^{-x} + 1}$, donc $f_0(x) + f_0(-x) = \dfrac{1 + e^{-x}}{1 + e^{-x}} = 1$.

Le milieu de $[MN]$ est $A\left(\dfrac{x + (-x)}{2};\dfrac{f_0(x) + f_0(-x)}{2}\right) = \left(0;\dfrac{1}{2}\right)$, indépendant de $x$ : $A$ est **centre de symétrie** de $(C_0)$.

**3) a)** $f_1(x) = \dfrac{e^{-x}}{1 + e^{-x}} = \dfrac{1}{e^x + 1} = f_0(-x)$ : $M(x;y) \in (C_1) \iff M'(-x;y) \in (C_0)$. Les courbes sont symétriques par rapport à l'axe des ordonnées.

**b)** La symétrie par rapport à $(Oy)$ inverse le sens de variation : $f_1$ est strictement décroissante sur $\mathbb{R}$, de $1$ (en $-\infty$) à $0$ (en $+\infty$), avec $f_1(0) = \dfrac{1}{2}$.

**c)** $(C_0)$ et $(C_1)$ passent par $\left(0;\dfrac{1}{2}\right)$, ont pour asymptotes $y = 0$ et $y = 1$, et sont symétriques par rapport à $(Oy)$.

**4) a)** En $+\infty$ : $e^{-nx} \to 0$ et $1 + e^{-x} \to 1$, donc $f_n(x) \to 0$ (asymptote $y = 0$).

En $-\infty$, on écrit $f_n(x) = \dfrac{e^{-(n-1)x}}{e^x + 1}$ : $e^{-(n-1)x} \to +\infty$ (car $n - 1 > 0$) et $e^x + 1 \to 1$, donc $f_n(x) \to +\infty$.

$\dfrac{f_n(x)}{x} = \dfrac{e^{-(n-1)x}}{x} \times \dfrac{1}{e^x + 1}$. Avec $X = -(n - 1)x \to +\infty$ : $\dfrac{e^{-(n-1)x}}{x} = -(n - 1)\dfrac{e^X}{X} \to -\infty$. Donc $\lim\limits_{x \to -\infty} \dfrac{f_n(x)}{x} = -\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**b)** $f_n'(x) = \dfrac{-ne^{-nx}(1 + e^{-x}) + e^{-nx}e^{-x}}{(1 + e^{-x})^2} = -\dfrac{e^{-nx}\big(n + (n - 1)e^{-x}\big)}{(1 + e^{-x})^2} < 0$.

$f_n$ est strictement décroissante sur $\mathbb{R}$, de $+\infty$ à $0$, avec $f_n(0) = \dfrac{1}{2}$.

**5) a)** $f_n$ est continue sur $[0;1]$, donc $u_n$ existe pour tout $n$.
$$u_0 = \int_0^1 \dfrac{e^x}{e^x + 1}\,dx = \big[\ln(e^x + 1)\big]_0^1 = \ln(e + 1) - \ln 2 = \ln\left(\dfrac{1 + e}{2}\right).$$

**b)** $u_0 + u_1 = \displaystyle\int_0^1 \dfrac{1 + e^{-x}}{1 + e^{-x}}\,dx = 1$.

Pour $n \ge 1$ : $u_{n+1} + u_n = \displaystyle\int_0^1 \dfrac{e^{-nx}(e^{-x} + 1)}{1 + e^{-x}}\,dx = \int_0^1 e^{-nx}\,dx = \left[-\dfrac{e^{-nx}}{n}\right]_0^1 = \dfrac{1 - e^{-n}}{n}$.

Donc $u_1 = 1 - \ln\left(\dfrac{1 + e}{2}\right) \approx 0{,}380$ et $u_2 = (1 - e^{-1}) - u_1 = \ln\left(\dfrac{1 + e}{2}\right) - \dfrac{1}{e} \approx 0{,}252$.

**c)** Pour $x \in [0;1]$ : $f_{n+1}(x) = e^{-x}f_n(x) \le f_n(x)$, donc $u_{n+1} \le u_n$ : $(u_n)$ est décroissante. Elle est positive ($f_n > 0$), donc **convergente**.

De plus $0 \le u_n \le u_{n+1} + u_n = \dfrac{1 - e^{-n}}{n} \le \dfrac{1}{n}$ pour $n \ge 1$, donc $\lim\limits_{n \to +\infty} u_n = 0$.
""", [SU, IP])

_add("bac-c-2017-sn-math-ex4", r"""
**Exercice 4 (5 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par : $f(x) = \dfrac{\ln x}{x^2}$.

**1) a)** Dresser le tableau de variation de $f$.

b) Déduire que pour tout entier $n \ge 6$, l'équation $f(x) = \dfrac{1}{n}$ admet dans l'intervalle $\left[1;\sqrt{e}\right]$ une seule solution notée $a_n$.

c) Prouver que la suite $(a_n)$ est décroissante, en déduire qu'elle converge.

**2) a)** Montrer que pour tout entier $k$ strictement supérieur à $1$, on a : $\dfrac{\ln(k + 1)}{(k + 1)^2} \le \displaystyle\int_k^{k+1} \dfrac{\ln x}{x^2}\,dx \le \dfrac{\ln k}{k^2}$.

b) Utiliser une intégration par parties pour exprimer en fonction de $n$ l'intégrale : $\displaystyle\int_2^n \dfrac{\ln x}{x^2}\,dx$, $n \ge 2$.

**3)** Pour tout entier $n$ strictement supérieur à $1$, on pose : $S_n = \dfrac{\ln 2}{2^2} + \dfrac{\ln 3}{3^2} + \dfrac{\ln 4}{4^2} + \dots + \dfrac{\ln n}{n^2}$.

a) Montrer que $S_n - \dfrac{\ln 2}{2^2} \le \displaystyle\int_2^n \dfrac{\ln x}{x^2}\,dx \le S_n - \dfrac{\ln n}{n^2}$.

b) En déduire que : $\dfrac{1 + \ln 2}{2} - \dfrac{n + (n - 1)\ln n}{n^2} \le S_n \le \dfrac{2 + 3\ln 2}{4} - \dfrac{1 + \ln n}{n}$.

**4)** Pour tout entier naturel $n$ non nul, on pose : $u_n = \displaystyle\sum_{k=1}^{n} \dfrac{(\ln 2)^{k-1}}{k!}$ et $I_n = \dfrac{1}{n!}\displaystyle\int_1^2 \dfrac{(\ln x)^n}{x^2}\,dx$.

a) Montrer que : $\forall n \in \mathbb{N}^*$, $0 \le I_n \le \dfrac{(\ln 2)^n}{n!}$. En déduire la limite de $I_n$.

b) Montrer que : $\forall n \in \mathbb{N}^*$, $I_{n+1} = I_n - \dfrac{1}{2}\,\dfrac{(\ln 2)^{n+1}}{(n + 1)!}$.

c) En déduire que : $\forall n \in \mathbb{N}^*$, $I_n = \dfrac{1}{2} - \dfrac{1}{2}\left[\dfrac{\ln 2}{1!} + \dfrac{(\ln 2)^2}{2!} + \dots + \dfrac{(\ln 2)^n}{n!}\right]$.

d) Exprimer $(u_n)$ en fonction de $I_n$. En déduire la limite de $(u_n)$.
""", r"""
**1) a)** $f'(x) = \dfrac{\frac{1}{x} \times x^2 - 2x\ln x}{x^4} = \dfrac{1 - 2\ln x}{x^3}$, du signe de $1 - 2\ln x$ : positif pour $x < \sqrt{e}$, négatif pour $x > \sqrt{e}$. $f(\sqrt{e}) = \dfrac{1/2}{e} = \dfrac{1}{2e}$.

En $0^+$ : $\ln x \to -\infty$ et $\dfrac{1}{x^2} \to +\infty$, donc $f(x) \to -\infty$. En $+\infty$ : $f(x) = \dfrac{\ln x}{x} \times \dfrac{1}{x} \to 0$.

| $x$ | $0$ | | $\sqrt{e}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $\frac{1}{2e}$ | ↘ | $0$ |

**b)** Sur $\left[1;\sqrt{e}\right]$, $f$ est continue et strictement croissante, de $f(1) = 0$ à $f(\sqrt{e}) = \dfrac{1}{2e}$. Pour $n \ge 6$ : $n > 2e \approx 5{,}44$, donc $0 < \dfrac{1}{n} < \dfrac{1}{2e}$. L'équation $f(x) = \dfrac{1}{n}$ a donc une seule solution $a_n$ dans $\left[1;\sqrt{e}\right]$.

**c)** $f(a_{n+1}) = \dfrac{1}{n + 1} < \dfrac{1}{n} = f(a_n)$, avec $a_n$, $a_{n+1}$ dans $\left[1;\sqrt{e}\right]$ où $f$ est strictement croissante : $a_{n+1} < a_n$. La suite $(a_n)$ est **décroissante** et minorée par $1$, donc **convergente**.

(Sa limite $\ell \in [1;\sqrt{e}]$ vérifie $f(\ell) = 0$ par continuité, donc $\ell = 1$.)

**2) a)** Pour $k \ge 2$ : $k > \sqrt{e}$, donc $f$ est décroissante sur $[k;k + 1]$ et $f(k + 1) \le f(x) \le f(k)$. En intégrant sur cet intervalle de longueur $1$ :
$$\dfrac{\ln(k + 1)}{(k + 1)^2} \le \int_k^{k+1} \dfrac{\ln x}{x^2}\,dx \le \dfrac{\ln k}{k^2}.$$

**b)** Par parties, avec $u = \ln x$ et $v' = \dfrac{1}{x^2}$ ($v = -\dfrac{1}{x}$) :
$$\int_2^n \dfrac{\ln x}{x^2}\,dx = \left[-\dfrac{\ln x}{x}\right]_2^n + \int_2^n \dfrac{dx}{x^2} = -\dfrac{\ln n}{n} + \dfrac{\ln 2}{2} - \dfrac{1}{n} + \dfrac{1}{2} = \dfrac{1 + \ln 2}{2} - \dfrac{1 + \ln n}{n}.$$

**3) a)** En sommant 2) a) pour $k = 2, \dots, n - 1$ :
$$\sum_{k=3}^{n} \dfrac{\ln k}{k^2} \le \int_2^n \dfrac{\ln x}{x^2}\,dx \le \sum_{k=2}^{n-1} \dfrac{\ln k}{k^2},$$
c'est-à-dire $S_n - \dfrac{\ln 2}{2^2} \le \displaystyle\int_2^n \dfrac{\ln x}{x^2}\,dx \le S_n - \dfrac{\ln n}{n^2}$ (pour $n = 2$, les trois membres sont nuls).

**b)** Avec 2) b) :
- $S_n \le \dfrac{1 + \ln 2}{2} - \dfrac{1 + \ln n}{n} + \dfrac{\ln 2}{4} = \dfrac{2 + 3\ln 2}{4} - \dfrac{1 + \ln n}{n}$ ;
- $S_n \ge \dfrac{1 + \ln 2}{2} - \dfrac{1 + \ln n}{n} + \dfrac{\ln n}{n^2} = \dfrac{1 + \ln 2}{2} - \dfrac{n + n\ln n - \ln n}{n^2} = \dfrac{1 + \ln 2}{2} - \dfrac{n + (n - 1)\ln n}{n^2}$.

**4) a)** Pour $x \in [1;2]$ : $0 \le \ln x \le \ln 2$ et $0 < \dfrac{1}{x^2} \le 1$, donc $0 \le \dfrac{(\ln x)^n}{x^2} \le (\ln 2)^n$. En intégrant sur $[1;2]$ (longueur $1$) :
$$0 \le I_n \le \dfrac{(\ln 2)^n}{n!}.$$

Comme $0 < \ln 2 < 1$, $(\ln 2)^n \le 1$ et $\dfrac{1}{n!} \to 0$ : $\lim\limits_{n \to +\infty} I_n = 0$.

**b)** Par parties, avec $u = (\ln x)^{n+1}$ et $v' = \dfrac{1}{x^2}$ ($u' = \dfrac{(n + 1)(\ln x)^n}{x}$, $v = -\dfrac{1}{x}$) :
$$\int_1^2 \dfrac{(\ln x)^{n+1}}{x^2}\,dx = \left[-\dfrac{(\ln x)^{n+1}}{x}\right]_1^2 + (n + 1)\int_1^2 \dfrac{(\ln x)^n}{x^2}\,dx = -\dfrac{(\ln 2)^{n+1}}{2} + (n + 1)\int_1^2 \dfrac{(\ln x)^n}{x^2}\,dx.$$

En divisant par $(n + 1)!$ : $I_{n+1} = I_n - \dfrac{1}{2}\,\dfrac{(\ln 2)^{n+1}}{(n + 1)!}$.

**c)** $I_1 = \displaystyle\int_1^2 \dfrac{\ln x}{x^2}\,dx = \left[-\dfrac{\ln x + 1}{x}\right]_1^2 = -\dfrac{\ln 2 + 1}{2} + 1 = \dfrac{1}{2} - \dfrac{1}{2}\,\dfrac{\ln 2}{1!}$ : la formule est vraie pour $n = 1$. Si elle est vraie au rang $n$, b) ajoute le terme $-\dfrac{1}{2}\,\dfrac{(\ln 2)^{n+1}}{(n + 1)!}$ : elle est vraie au rang $n + 1$.

**d)** $\displaystyle\sum_{k=1}^{n}\dfrac{(\ln 2)^k}{k!} = \ln 2 \sum_{k=1}^{n}\dfrac{(\ln 2)^{k-1}}{k!} = u_n\ln 2$, donc $I_n = \dfrac{1}{2} - \dfrac{\ln 2}{2}u_n$, soit
$$u_n = \dfrac{1 - 2I_n}{\ln 2}.$$

Comme $I_n \to 0$ : $\lim\limits_{n \to +\infty} u_n = \dfrac{1}{\ln 2}$.
""", [IP, SU])

# ═══════════════════════════════ 2018 — session complémentaire ════════════════

_add("bac-c-2018-sc-math-ex2", r"""
**Exercice 2 (5 points)**

**I.** On considère la fonction numérique $f$ définie sur $[0;+\infty[$ par $\begin{cases} f(x) = (x + 1)e^{-\frac{1}{x}} & \forall x > 0 \\ f(0) = 0 \end{cases}$

On note $(C)$ sa courbe représentative dans un repère orthonormé d'unité graphique 4 cm.

**1° a)** Étudier la continuité et la dérivabilité de $f$ à droite de $0$.

b) Dresser le tableau de variations de $f$ sur $[0;+\infty[$.

**2° a)** Montrer que $\forall t \ge 0$, $0 \le e^{-t} + t - 1 \le \dfrac{t^2}{2}$.

b) En déduire que $\forall x > 0$, $-\dfrac{1}{x} \le f(x) - x \le \dfrac{1}{2x^2} - \dfrac{1}{2x}$.

c) En déduire que la courbe $(C)$ admet une asymptote oblique $\Delta$ dont on donnera l'équation.

**3°** Construire la courbe $(C)$ et la droite $\Delta$.

**4° a)** Montrer que $f$ réalise une bijection de $[0;+\infty[$ sur un intervalle $J$ que l'on précisera.

b) Construire la courbe $(C')$ de $f^{-1}$, où $f^{-1}$ est la réciproque de $f$.

**II.** $\forall n \in \mathbb{N}^*$, on définit sur $[0;+\infty[$ la fonction numérique $f_n$ par $\begin{cases} f_n(x) = \left(x + \dfrac{1}{n}\right)e^{-\frac{1}{x}} & \forall x > 0 \\ f_n(0) = 0 \end{cases}$

**1° a)** Montrer que $f_n$ est continue et dérivable à droite de $0$.

b) Étudier les variations de $f_n$ et en déduire que $\forall n \in \mathbb{N}^*$, l'équation $f_n(x) = \dfrac{1}{n}$ admet une unique solution $\alpha_n$ sur $]0;+\infty[$.

**2° a)** Soit $g_n(x) = f_n(x) - \dfrac{1}{n}$. Étudier sur $]0;+\infty[$ le signe de $g_{n+1}(x) - g_n(x)$ et en déduire que la suite $(\alpha_n)$ est strictement décroissante et qu'elle est convergente.

b) Montrer que $\forall n \in \mathbb{N}^*$, $\alpha_n = \dfrac{1}{n}\left(e^{\frac{1}{\alpha_n}} - 1\right)$. En déduire la limite de $\alpha_n$.
""", r"""
**I. 1° a)** Quand $x \to 0^+$ : $-\dfrac{1}{x} \to -\infty$, donc $e^{-1/x} \to 0$ et $f(x) \to 0 = f(0)$ : $f$ est **continue à droite en $0$**.

$\dfrac{f(x) - f(0)}{x} = \left(1 + \dfrac{1}{x}\right)e^{-1/x}$. Avec $X = \dfrac{1}{x} \to +\infty$ : $(1 + X)e^{-X} = e^{-X} + \dfrac{X}{e^X} \to 0$. $f$ est **dérivable à droite en $0$** et $f'_d(0) = 0$ : demi-tangente horizontale en $O$.

**b)** Pour $x > 0$ : $f'(x) = e^{-1/x} + (x + 1)\dfrac{1}{x^2}e^{-1/x} = \dfrac{x^2 + x + 1}{x^2}e^{-1/x} > 0$. En $+\infty$, $e^{-1/x} \to 1$ et $f(x) \to +\infty$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | $0$ | $+$ | |
| $f(x)$ | $0$ | ↗ | $+\infty$ |

**2° a)** Soit $\varphi(t) = e^{-t} + t - 1$ : $\varphi'(t) = 1 - e^{-t} \ge 0$ pour $t \ge 0$ et $\varphi(0) = 0$, donc $\varphi(t) \ge 0$.

Soit $\psi(t) = \dfrac{t^2}{2} - \varphi(t)$ : $\psi'(t) = t - 1 + e^{-t} = \varphi(t) \ge 0$ et $\psi(0) = 0$, donc $\psi(t) \ge 0$. D'où $0 \le e^{-t} + t - 1 \le \dfrac{t^2}{2}$.

**b)** Avec $t = \dfrac{1}{x}$ ($x > 0$) : $1 - \dfrac{1}{x} \le e^{-1/x} \le 1 - \dfrac{1}{x} + \dfrac{1}{2x^2}$. On multiplie par $x + 1 > 0$ :
- $(x + 1)\left(1 - \dfrac{1}{x}\right) = x - \dfrac{1}{x}$ ;
- $(x + 1)\left(1 - \dfrac{1}{x} + \dfrac{1}{2x^2}\right) = x - \dfrac{1}{x} + \dfrac{1}{2x} + \dfrac{1}{2x^2} = x - \dfrac{1}{2x} + \dfrac{1}{2x^2}$.

Donc $-\dfrac{1}{x} \le f(x) - x \le \dfrac{1}{2x^2} - \dfrac{1}{2x}$.

**c)** Les deux bornes tendent vers $0$ en $+\infty$, donc $\lim\limits_{x \to +\infty}\big(f(x) - x\big) = 0$ : la droite $\Delta : y = x$ est **asymptote oblique**. De plus, pour $x > 1$, $\dfrac{1}{2x^2} - \dfrac{1}{2x} = \dfrac{1 - x}{2x^2} < 0$ : $(C)$ est au-dessous de $\Delta$.

**3°** $(C)$ part de $O$ avec une demi-tangente horizontale, est croissante, passe par $\left(1;\dfrac{2}{e}\right)$ et se rapproche de $\Delta$ par-dessous.

**4° a)** $f$ est continue et strictement croissante sur $[0;+\infty[$ : bijection de $[0;+\infty[$ sur $J = [0;+\infty[$.

**b)** $(C')$ est la symétrique de $(C)$ par rapport à la droite $y = x$ ; elle admet en $O$ une demi-tangente verticale et l'asymptote $y = x$.

**II. 1° a)** Quand $x \to 0^+$ : $f_n(x) \to 0 = f_n(0)$ ; $\dfrac{f_n(x)}{x} = \left(1 + \dfrac{1}{nx}\right)e^{-1/x} \to 0$ (même calcul qu'en I). $f_n$ est continue et dérivable à droite en $0$, avec $f_n'(0) = 0$.

**b)** Pour $x > 0$ : $f_n'(x) = e^{-1/x}\left(1 + \dfrac{x + \frac{1}{n}}{x^2}\right) > 0$. $f_n$ est continue et strictement croissante sur $]0;+\infty[$, de $0$ (limite en $0^+$) à $+\infty$. Comme $\dfrac{1}{n} \in ]0;+\infty[$, l'équation $f_n(x) = \dfrac{1}{n}$ a une unique solution $\alpha_n > 0$.

**2° a)** $g_{n+1}(x) - g_n(x) = \left(\dfrac{1}{n + 1} - \dfrac{1}{n}\right)e^{-1/x} - \dfrac{1}{n + 1} + \dfrac{1}{n} = \left(\dfrac{1}{n} - \dfrac{1}{n + 1}\right)\left(1 - e^{-1/x}\right) > 0$ pour $x > 0$.

Donc $g_{n+1}(\alpha_n) > g_n(\alpha_n) = 0 = g_{n+1}(\alpha_{n+1})$. Comme $g_{n+1}$ est strictement croissante, $\alpha_n > \alpha_{n+1}$ : $(\alpha_n)$ est **strictement décroissante**. Elle est minorée par $0$, donc **convergente**.

**b)** $f_n(\alpha_n) = \dfrac{1}{n} \iff \left(\alpha_n + \dfrac{1}{n}\right)e^{-1/\alpha_n} = \dfrac{1}{n} \iff n\alpha_n + 1 = e^{1/\alpha_n} \iff \alpha_n = \dfrac{1}{n}\left(e^{\frac{1}{\alpha_n}} - 1\right)$.

Soit $\ell \ge 0$ la limite de $(\alpha_n)$. Si $\ell > 0$, alors $e^{1/\alpha_n} - 1 \to e^{1/\ell} - 1$ (réel) et $\alpha_n = \dfrac{1}{n}\left(e^{1/\alpha_n} - 1\right) \to 0$, ce qui contredit $\ell > 0$. Donc $\lim\limits_{n \to +\infty}\alpha_n = 0$.
""", [CH, SU], chapitre=FN)

_add("bac-c-2018-sc-math-ex4", r"""
**Exercice 4 (5 points)**

On définit la fonction $f$ sur $\mathbb{R}$ par $f(x) = -x + 2\ln(1 + e^x)$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**Partie A**

**1° a)** Donner le tableau de variation de $f$.

b) Démontrer que la courbe $(C)$ admet deux asymptotes $D$ et $D'$ que l'on déterminera et préciser leurs positions relatives par rapport à $(C)$.

c) Construire la courbe $(C)$ et ses asymptotes dans le même repère.

**2°** Soit $g$ la restriction de $f$ sur l'intervalle $I = [0;+\infty[$.

a) Montrer que $g$ est une bijection de l'intervalle $I$ sur un intervalle $J$ que l'on précisera.

b) Construire, dans le repère précédent, la courbe $(C')$ de $g^{-1}$.

**Partie B**

On considère la suite numérique $(u_n)$ par $u_0 = \ln 5$ et $\forall n \in \mathbb{N}^*$, $u_n = \displaystyle\int_0^{\ln 5} \big(f'(t)\big)^n\,dt$.

**1°** Calculer $u_1$.

**2° a)** Montrer que $\forall x \in [0;\ln 5]$, $0 \le f'(x) \le \dfrac{2}{3}$.

b) En déduire que $\forall n \in \mathbb{N}$, $0 \le u_n \le \left(\dfrac{2}{3}\right)^n \ln 5$.

c) Déterminer la limite de $(u_n)$.

**3° a)** Montrer que $\forall x \in [0;+\infty[$, $\big(f'(x)\big)^2 - 1 = -2f''(x)$.

b) Montrer que $\forall n \in \mathbb{N}$, $u_{n+2} - u_n = \dfrac{-2}{n + 1}\left(\dfrac{2}{3}\right)^{n+1}$.

c) En déduire que $\forall n \in \mathbb{N}^*$, $u_{2n} = \ln 5 - \displaystyle\sum_{k=1}^{n} \dfrac{2}{2k - 1}\left(\dfrac{2}{3}\right)^{2k-1}$ et $u_{2n+1} = \ln\left(\dfrac{9}{5}\right) - \displaystyle\sum_{k=1}^{n} \dfrac{1}{k}\left(\dfrac{2}{3}\right)^{2k}$.

**4°** $\forall n \in \mathbb{N}^*$, on pose $v_n = \displaystyle\sum_{p=1}^{2n} \dfrac{1}{p}\left(\dfrac{2}{3}\right)^p$. Montrer que $v_n = \ln 3 - \dfrac{u_{2n} + u_{2n+1}}{2}$ puis en déduire $\lim\limits_{n \to +\infty} v_n$.
""", r"""
**Partie A**

**1° a)** $f'(x) = -1 + \dfrac{2e^x}{1 + e^x} = \dfrac{e^x - 1}{e^x + 1}$, du signe de $x$. $f(0) = 2\ln 2$.

En $+\infty$ : $f(x) = -x + 2\big(x + \ln(1 + e^{-x})\big) = x + 2\ln(1 + e^{-x}) \to +\infty$. En $-\infty$ : $\ln(1 + e^x) \to 0$ et $f(x) \to +\infty$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $2\ln 2$ | ↗ | $+\infty$ |

(On remarque que $f$ est paire : $f(-x) = x + 2\ln(1 + e^{-x}) = x + 2\ln(1 + e^x) - 2x = f(x)$.)

**b)** En $+\infty$ : $f(x) - x = 2\ln(1 + e^{-x}) \to 0$ : $D : y = x$ est asymptote, et comme $2\ln(1 + e^{-x}) > 0$, $(C)$ est **au-dessus** de $D$.

En $-\infty$ : $f(x) - (-x) = 2\ln(1 + e^x) \to 0$ : $D' : y = -x$ est asymptote, et $(C)$ est **au-dessus** de $D'$.

**c)** $(C)$ est symétrique par rapport à $(Oy)$, de minimum $(0;2\ln 2)$ ($2\ln 2 \approx 1{,}39$), au-dessus de ses asymptotes $D$ et $D'$.

**2° a)** $g$ est continue et strictement croissante sur $[0;+\infty[$, de $2\ln 2$ à $+\infty$ : bijection de $I$ sur $J = [2\ln 2;+\infty[$.

**b)** $(C')$ est la symétrique de la partie de $(C)$ d'abscisses positives par rapport à la droite $y = x$ : elle part de $(2\ln 2;0)$ avec une tangente verticale et admet l'asymptote $y = x$.

**Partie B**

**1°** $u_1 = \displaystyle\int_0^{\ln 5} f'(t)\,dt = f(\ln 5) - f(0) = -\ln 5 + 2\ln 6 - 2\ln 2 = 2\ln 3 - \ln 5 = \ln\left(\dfrac{9}{5}\right)$.

**2° a)** $f''(x) = \dfrac{2e^x}{(1 + e^x)^2} > 0$ : $f'$ est croissante. Sur $[0;\ln 5]$ : $f'(0) = 0 \le f'(x) \le f'(\ln 5) = \dfrac{4}{6} = \dfrac{2}{3}$.

**b)** Pour $n \ge 1$ : $0 \le \big(f'(t)\big)^n \le \left(\dfrac{2}{3}\right)^n$ sur $[0;\ln 5]$, d'où en intégrant $0 \le u_n \le \left(\dfrac{2}{3}\right)^n\ln 5$. Pour $n = 0$ : $u_0 = \ln 5$ convient.

**c)** $\left(\dfrac{2}{3}\right)^n \to 0$, donc $\lim\limits_{n \to +\infty} u_n = 0$.

**3° a)** $\big(f'(x)\big)^2 - 1 = \dfrac{(e^x - 1)^2 - (e^x + 1)^2}{(e^x + 1)^2} = \dfrac{-4e^x}{(e^x + 1)^2} = -2f''(x)$ (vrai pour tout réel $x$).

**b)** $u_{n+2} - u_n = \displaystyle\int_0^{\ln 5}\big(f'(t)\big)^n\Big(\big(f'(t)\big)^2 - 1\Big)\,dt = -2\int_0^{\ln 5}\big(f'(t)\big)^nf''(t)\,dt = -2\left[\dfrac{\big(f'(t)\big)^{n+1}}{n + 1}\right]_0^{\ln 5}$, donc
$$u_{n+2} - u_n = \dfrac{-2}{n + 1}\left(\dfrac{2}{3}\right)^{n+1}.$$

(Pour $n = 0$, on utilise $u_0 = \ln 5 = \displaystyle\int_0^{\ln 5} 1\,dt$ : la formule reste vraie.)

**c)** En appliquant b) à $n = 2k - 2$ ($k \ge 1$) : $u_{2k} - u_{2k-2} = -\dfrac{2}{2k - 1}\left(\dfrac{2}{3}\right)^{2k-1}$. En sommant de $k = 1$ à $n$ :
$$u_{2n} = u_0 - \sum_{k=1}^{n}\dfrac{2}{2k - 1}\left(\dfrac{2}{3}\right)^{2k-1} = \ln 5 - \sum_{k=1}^{n}\dfrac{2}{2k - 1}\left(\dfrac{2}{3}\right)^{2k-1}.$$

En appliquant b) à $n = 2k - 1$ : $u_{2k+1} - u_{2k-1} = -\dfrac{2}{2k}\left(\dfrac{2}{3}\right)^{2k} = -\dfrac{1}{k}\left(\dfrac{2}{3}\right)^{2k}$. En sommant :
$$u_{2n+1} = u_1 - \sum_{k=1}^{n}\dfrac{1}{k}\left(\dfrac{2}{3}\right)^{2k} = \ln\left(\dfrac{9}{5}\right) - \sum_{k=1}^{n}\dfrac{1}{k}\left(\dfrac{2}{3}\right)^{2k}.$$

**4°** On sépare dans $v_n$ les indices impairs $p = 2k - 1$ et pairs $p = 2k$ ($1 \le k \le n$) :
$$v_n = \sum_{k=1}^{n}\dfrac{1}{2k - 1}\left(\dfrac{2}{3}\right)^{2k-1} + \sum_{k=1}^{n}\dfrac{1}{2k}\left(\dfrac{2}{3}\right)^{2k} = \dfrac{\ln 5 - u_{2n}}{2} + \dfrac{\ln\frac{9}{5} - u_{2n+1}}{2}.$$

Comme $\ln 5 + \ln\dfrac{9}{5} = \ln 9 = 2\ln 3$ : $v_n = \ln 3 - \dfrac{u_{2n} + u_{2n+1}}{2}$.

Puisque $u_n \to 0$ : $\lim\limits_{n \to +\infty} v_n = \ln 3$.
""", [SU, IP])

# ═══════════════════════════════ 2018 — session normale ═══════════════════════

_add("bac-c-2018-sn-math-ex4", r"""
**Exercice 4 (4 points)**

**1° a)** Résoudre l'équation différentielle $(E) : y'' - 6y' + 8y = 0$.

b) Déterminer la solution $y_0$ de $(E)$ dont la courbe passe par le point $A(0;-1)$ et admet en ce point une tangente horizontale.

**2°** Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = e^{4x} - 2e^{2x}$ et $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

a) Calculer et interpréter les limites suivantes : $\lim\limits_{x \to -\infty} f(x)$, $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

b) Dresser le tableau de variations de $f$.

**3°** Soit $g$ la restriction de $f$ sur l'intervalle $I = ]-\infty;0]$.

a) Montrer que $g$ réalise une bijection de l'intervalle $I$ sur un intervalle $J$ que l'on déterminera.

b) Calculer et interpréter $\lim\limits_{x \to -1} \dfrac{g^{-1}(x)}{x + 1}$ où $g^{-1}$ est la réciproque de $g$.

c) Soit $(C')$ la courbe de $g^{-1}$. Montrer que les courbes $(C)$ et $(C')$ se coupent en un unique point $B$ d'abscisse $\alpha$ telle que $-0{,}6 < \alpha < -0{,}5$.

d) Tracer dans le même repère les courbes $(C)$ et $(C')$.

e) Donner l'expression de $g^{-1}(x)$.

**4°** Soit $S$ l'aire de la partie du plan délimitée par les courbes $(C)$, $(C')$ et les axes de coordonnées.

a) Montrer que $S = 2\displaystyle\int_\alpha^0 \big(x - f(x)\big)\,dx$.

b) Calculer la valeur de $S$ en fonction de $\alpha$ et en donner une valeur approchée à $10^{-2}$ près.
""", r"""
**1° a)** Équation caractéristique : $r^2 - 6r + 8 = 0$, de racines $r = 2$ et $r = 4$. Les solutions de $(E)$ sont les fonctions $y(x) = ae^{2x} + be^{4x}$, $a$ et $b$ réels.

**b)** $y(0) = a + b = -1$ et $y'(0) = 2a + 4b = 0$ (tangente horizontale). Donc $a = -2b$, puis $-b = -1$ : $b = 1$, $a = -2$.
$$y_0(x) = e^{4x} - 2e^{2x}.$$

**2° a)** En $-\infty$ : $e^{4x} \to 0$ et $e^{2x} \to 0$, donc $f(x) \to 0$ : la droite $y = 0$ est **asymptote horizontale** en $-\infty$.

En $+\infty$ : $f(x) = e^{4x}\left(1 - 2e^{-2x}\right) \to +\infty$, et $\dfrac{f(x)}{x} = \dfrac{e^{4x}}{x}\left(1 - 2e^{-2x}\right) \to +\infty$ : **branche parabolique de direction $(Oy)$**.

**b)** $f'(x) = 4e^{4x} - 4e^{2x} = 4e^{2x}(e^{2x} - 1)$, du signe de $x$. $f(0) = -1$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $0$ | ↘ | $-1$ | ↗ | $+\infty$ |

**3° a)** $g$ est continue et strictement décroissante sur $]-\infty;0]$, de $0$ (limite non atteinte) à $-1$ : bijection de $I$ sur $J = [-1;0[$.

**b)** $g^{-1}(-1) = 0$, donc $\dfrac{g^{-1}(x)}{x + 1} = \dfrac{g^{-1}(x) - g^{-1}(-1)}{x - (-1)}$ : c'est le taux d'accroissement de $g^{-1}$ en $-1$ (avec $x \to -1^+$, car $x \in J$). Comme $g'(0) = 0$, $g^{-1}$ n'est pas dérivable en $-1$ : pour $x \in ]-1;0[$, $g^{-1}(x) < 0$ et $x + 1 > 0$, et
$$\lim\limits_{x \to -1^+}\dfrac{g^{-1}(x)}{x + 1} = -\infty.$$

**Interprétation :** $(C')$ admet au point $(-1;0)$ une **demi-tangente verticale** (symétrique de la tangente horizontale de $(C)$ en $(0;-1)$).

**c)** Un point $M(x;y)$ est commun à $(C)$ et $(C')$ si $x \in [-1;0[$, $y = g(x)$ et $x = g(y)$ ; donc $g(g(x)) = x$.

Sur $]-\infty;0]$, avec $u = e^{2x} \in ]0;1]$ : $|g'(x)| = 4u(1 - u) \le 1$ (car $(2u - 1)^2 \ge 0$), avec égalité seulement pour $u = \dfrac{1}{2}$. La fonction $k(x) = g(g(x)) - x$ a pour dérivée $g'(g(x))\,g'(x) - 1 \le 0$, nulle au plus en un point isolé : $k$ est strictement décroissante et s'annule au plus une fois.

Sur la droite $y = x$ : $h(x) = e^{4x} - 2e^{2x} - x$ vérifie $h(-0{,}6) \approx 0{,}09 > 0$ et $h(-0{,}5) \approx -0{,}10 < 0$. Elle s'annule donc en un $\alpha \in ]-0{,}6;-0{,}5[$ ($\alpha \approx -0{,}553$), et $B(\alpha;\alpha)$ est commun à $(C)$ et $(C')$. C'est le seul point commun.

**d)** $(C')$ est la symétrique de la partie de $(C)$ d'abscisses négatives par rapport à $y = x$ : elle va de $(-1;0)$ (demi-tangente verticale) vers $-\infty$ quand $x \to 0^-$ (asymptote $x = 0$) et passe par $B$.

**e)** Pour $x \in [-1;0[$ : $y = g^{-1}(x) \iff x = e^{4y} - 2e^{2y}$ avec $y \le 0$. En posant $X = e^{2y} \in ]0;1]$ : $X^2 - 2X - x = 0$, d'où $X = 1 - \sqrt{1 + x}$ (la racine $1 + \sqrt{1 + x}$ est $\ge 1$, et vaut $1$ seulement si $x = -1$, cas déjà couvert). Donc
$$g^{-1}(x) = \dfrac{1}{2}\ln\left(1 - \sqrt{1 + x}\right).$$

**4° a)** Le domaine est limité par l'axe $(Oy)$ (de $(0;-1)$ à $O$), l'axe $(Ox)$ (de $O$ à $(-1;0)$), $(C')$ de $(-1;0)$ à $B$ et $(C)$ de $B$ à $(0;-1)$. Il est symétrique par rapport à la droite $y = x$. Sur $[\alpha;0]$, $f(x) \le x$ ; la moitié du domaine située sous la droite $y = x$ a pour aire $\displaystyle\int_\alpha^0\big(x - f(x)\big)\,dx$. Donc $S = 2\displaystyle\int_\alpha^0\big(x - f(x)\big)\,dx$.

**b)** $\displaystyle\int_\alpha^0\big(x - f(x)\big)\,dx = \left[\dfrac{x^2}{2} - \dfrac{e^{4x}}{4} + e^{2x}\right]_\alpha^0 = \dfrac{3}{4} - \dfrac{\alpha^2}{2} + \dfrac{e^{4\alpha}}{4} - e^{2\alpha}$.

Comme $f(\alpha) = \alpha$ : $e^{4\alpha} = \alpha + 2e^{2\alpha}$, donc $\dfrac{e^{4\alpha}}{4} - e^{2\alpha} = \dfrac{\alpha}{4} - \dfrac{e^{2\alpha}}{2}$. Ainsi
$$S = \dfrac{3}{2} - \alpha^2 + \dfrac{\alpha}{2} - e^{2\alpha} \text{ u.a.}$$

Avec $e^{2\alpha} = 1 - \sqrt{1 + \alpha}$ (car $g^{-1}(\alpha) = \alpha$) : $S = \dfrac{1}{2} - \alpha^2 + \dfrac{\alpha}{2} + \sqrt{1 + \alpha} \approx 0{,}59$ u.a.
""", [CH], chapitre="Équations différentielles")

_add("bac-c-2018-sn-math-ex5", r"""
**Exercice 5 (5 points)**

**Partie A**

Soit la fonction $f$ définie sur $]-1;+\infty[$ par $f(x) = \dfrac{x}{x + 1} - (x + 1)\ln(x + 1)$.

On note $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1.** Montrer que $\lim\limits_{x \to -1^+} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = -\infty$ puis calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$. Interpréter graphiquement.

**2. a)** Calculer $f'(x)$ et $f''(x)$ puis étudier les variations de $f'$.

b) Calculer $f'(0)$ et en déduire le signe de $f'(x)$.

**3. a)** Dresser le tableau de variation de $f$.

b) Tracer la courbe $(C)$.

**4. a)** Calculer $\displaystyle\int_0^x \dfrac{t}{t + 1}\,dt$ et, à l'aide d'une intégration par parties, calculer $\displaystyle\int_0^x (t + 1)\ln(1 + t)\,dt$.

b) En déduire la primitive $F$ de $f$ sur $]-1;+\infty[$ qui s'annule en $0$.

c) Calculer l'aire $A_n$ du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 0$ et $x = n$, pour $n$ un entier naturel $n \ge 1$.

**Partie B**

Soit $(U_n)$ la suite définie $\forall n \ge 1$ par $U_n = \dfrac{1}{2}f(1) + \dfrac{1}{3}f(2) + \dfrac{1}{4}f(3) + \dots + \dfrac{1}{n}f(n - 1) = \displaystyle\sum_{k=1}^{n-1} \dfrac{1}{k + 1}f(k)$.

**1°** Posons $\forall n \ge 1$ : $V_n = \dfrac{1}{n + 1}f(n)$.

a) Vérifier que $\forall n \ge 1$, $V_n = \dfrac{1}{n + 1} - \dfrac{1}{(n + 1)^2} - \ln(n + 1)$.

b) En déduire que $U_n = \displaystyle\sum_{k=1}^{n} \dfrac{1}{k} - \sum_{k=1}^{n} \dfrac{1}{k^2} - \ln(n!)$.

**2°** Notons $\forall n \ge 1$, $S_n = \displaystyle\sum_{k=1}^{n} \dfrac{1}{k}$ et $S'_n = \displaystyle\sum_{k=1}^{n} \dfrac{1}{k^2}$.

a) Montrer que $\forall k \ge 1$ : $\dfrac{1}{k + 1} \le \displaystyle\int_k^{k+1} \dfrac{dt}{t} \le \dfrac{1}{k}$ puis en déduire que $\dfrac{1}{n} + \ln n \le S_n \le 1 + \ln n$.

b) Montrer que $\forall k \ge 1$ : $\dfrac{1}{(k + 1)^2} \le \displaystyle\int_k^{k+1} \dfrac{dt}{t^2} \le \dfrac{1}{k^2}$ puis en déduire que $1 - \dfrac{1}{n} + \dfrac{1}{n^2} \le S'_n \le 2 - \dfrac{1}{n}$.

c) En déduire que $\forall n \ge 1$ : $\dfrac{2}{n} - 2 \le U_n + \ln\big((n - 1)!\big) \le \dfrac{1}{n} - \dfrac{1}{n^2}$.
""", r"""
**Partie A**

**1.** En $-1^+$ : $x \to -1$ et $x + 1 \to 0^+$, donc $\dfrac{x}{x + 1} \to -\infty$ ; et $(x + 1)\ln(x + 1) \to 0$ (car $u\ln u \to 0$ en $0^+$). Donc $\lim\limits_{x \to -1^+} f(x) = -\infty$.

En $+\infty$ : $\dfrac{x}{x + 1} \to 1$ et $(x + 1)\ln(x + 1) \to +\infty$, donc $f(x) \to -\infty$.

$\dfrac{f(x)}{x} = \dfrac{1}{x + 1} - \dfrac{x + 1}{x}\ln(x + 1) \to -\infty$.

**Interprétation :** la droite $x = -1$ est **asymptote verticale** ; en $+\infty$, **branche parabolique de direction $(Oy)$**.

**2. a)** $f'(x) = \dfrac{1}{(x + 1)^2} - \ln(x + 1) - 1$ et $f''(x) = -\dfrac{2}{(x + 1)^3} - \dfrac{1}{x + 1} < 0$ sur $]-1;+\infty[$ : $f'$ est **strictement décroissante**.

**b)** $f'(0) = 1 - 0 - 1 = 0$. Comme $f'$ est strictement décroissante : $f'(x) > 0$ sur $]-1;0[$ et $f'(x) < 0$ sur $]0;+\infty[$.

**3. a)** $f(0) = 0$.

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $0$ | ↘ | $-\infty$ |

**b)** $(C)$ admet l'asymptote $x = -1$, le maximum $O(0;0)$ avec tangente horizontale (l'axe des abscisses), et une branche parabolique verticale vers le bas ; $(C)$ est entièrement sous l'axe des abscisses, sauf en $O$.

**4. a)** $\displaystyle\int_0^x \dfrac{t}{t + 1}\,dt = \int_0^x\left(1 - \dfrac{1}{t + 1}\right)dt = x - \ln(x + 1)$.

Par parties, avec $u = \ln(1 + t)$ et $v' = t + 1$ ($v = \frac{(t + 1)^2}{2}$) :
$$\int_0^x (t + 1)\ln(1 + t)\,dt = \left[\dfrac{(t + 1)^2}{2}\ln(1 + t)\right]_0^x - \int_0^x \dfrac{t + 1}{2}\,dt = \dfrac{(x + 1)^2}{2}\ln(x + 1) - \dfrac{(x + 1)^2 - 1}{4}.$$

**b)** $F(x) = \displaystyle\int_0^x f(t)\,dt = x - \ln(x + 1) - \dfrac{(x + 1)^2}{2}\ln(x + 1) + \dfrac{x^2 + 2x}{4}$.

**c)** Sur $[0;n]$, $f(x) \le 0$, donc
$$A_n = -\int_0^n f(x)\,dx = -F(n) = \left(\dfrac{(n + 1)^2}{2} + 1\right)\ln(n + 1) - n - \dfrac{n^2 + 2n}{4} \text{ u.a.}$$

**Partie B**

**1° a)** $V_n = \dfrac{1}{n + 1}\left(\dfrac{n}{n + 1} - (n + 1)\ln(n + 1)\right) = \dfrac{n}{(n + 1)^2} - \ln(n + 1)$, et $\dfrac{n}{(n + 1)^2} = \dfrac{(n + 1) - 1}{(n + 1)^2} = \dfrac{1}{n + 1} - \dfrac{1}{(n + 1)^2}$.

**b)** $U_n = \displaystyle\sum_{k=1}^{n-1} V_k = \sum_{k=1}^{n-1}\dfrac{1}{k + 1} - \sum_{k=1}^{n-1}\dfrac{1}{(k + 1)^2} - \sum_{k=1}^{n-1}\ln(k + 1)$. Avec $j = k + 1$ :
$$U_n = \left(\sum_{j=1}^{n}\dfrac{1}{j} - 1\right) - \left(\sum_{j=1}^{n}\dfrac{1}{j^2} - 1\right) - \ln(2 \times 3 \times \dots \times n) = \sum_{k=1}^{n}\dfrac{1}{k} - \sum_{k=1}^{n}\dfrac{1}{k^2} - \ln(n!).$$

**2° a)** Pour $t \in [k;k + 1]$ : $\dfrac{1}{k + 1} \le \dfrac{1}{t} \le \dfrac{1}{k}$ ; en intégrant sur un intervalle de longueur $1$, on obtient l'encadrement. En sommant de $k = 1$ à $n - 1$ :
$$S_n - 1 \le \int_1^n \dfrac{dt}{t} = \ln n \le S_n - \dfrac{1}{n},$$
d'où $\dfrac{1}{n} + \ln n \le S_n \le 1 + \ln n$ (pour $n = 1$ : $1 \le 1 \le 1$).

**b)** De même avec $\dfrac{1}{t^2}$ : en sommant de $k = 1$ à $n - 1$, $S'_n - 1 \le \displaystyle\int_1^n \dfrac{dt}{t^2} = 1 - \dfrac{1}{n} \le S'_n - \dfrac{1}{n^2}$, d'où $1 - \dfrac{1}{n} + \dfrac{1}{n^2} \le S'_n \le 2 - \dfrac{1}{n}$.

**c)** $U_n + \ln\big((n - 1)!\big) = S_n - S'_n - \ln(n!) + \ln\big((n - 1)!\big) = S_n - \ln n - S'_n$. D'après a) et b) :
- $S_n - \ln n - S'_n \ge \dfrac{1}{n} - 2 + \dfrac{1}{n} = \dfrac{2}{n} - 2$ ;
- $S_n - \ln n - S'_n \le 1 - 1 + \dfrac{1}{n} - \dfrac{1}{n^2} = \dfrac{1}{n} - \dfrac{1}{n^2}$.
""", [SU, IP], note="Le sujet numérote deux fois la question « 3. » dans la partie A (la seconde, sur les intégrales, devient 4.).")

# ═══════════════════════════════ 2019 ═════════════════════════════════════════

_add("bac-c-2019-sc-math-ex4", r"""
**Exercice 4**

Soit la fonction $f$ définie sur $]0;+\infty[$ par : $f(x) = \dfrac{3\ln x}{1 + x^3}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité graphique 2 cm.

**1.** Pour tout réel strictement positif $x$, on pose $u(x) = 1 + x^3(1 - 3\ln x)$.

a) Calculer $\lim\limits_{x \to 0^+} u(x)$ et $\lim\limits_{x \to +\infty} u(x)$.

b) Dresser le tableau de variation de $u$.

c) Montrer que l'équation $u(x) = 0$ admet une unique solution $\alpha$ et que $1{,}5 \le \alpha \le 1{,}6$. En déduire le signe de $u(x)$.

**2. a)** Calculer et interpréter graphiquement $\lim\limits_{x \to 0^+} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$.

b) Montrer que $\forall x > 0$, $f'(x) = \dfrac{3u(x)}{x(1 + x^3)^2}$ et dresser le tableau de variation de $f$.

c) Vérifier que $f(\alpha) = \dfrac{1}{\alpha^3}$ et tracer la courbe $(C)$.

**3.** Pour tout entier $n$ strictement positif, on définit la suite $(v_n)$ par $v_n = \displaystyle\int_1^e \dfrac{(\ln t)^n}{1 + t^3}\,dt$.

a) Montrer que la suite $(v_n)$ est décroissante et minorée puis en déduire qu'elle est convergente.

b) Montrer que $\forall n \ge 1$, $\dfrac{1}{1 + e^3}\displaystyle\int_1^e (\ln t)^n\,dt \le v_n \le \int_1^e (\ln t)^n\,dt$.

**4.** On note, pour tout entier $n$ strictement positif, $w_n = \displaystyle\int_1^e (\ln t)^n\,dt$.

a) Justifier que la suite $(w_n)$ est décroissante.

b) À l'aide d'une intégration par parties, montrer que $\forall n \ge 1$, $w_{n+1} = e - (n + 1)w_n$.

c) Montrer que $\forall n \ge 1$, $\dfrac{e}{n + 2} \le w_n \le \dfrac{e}{n + 1}$. En déduire $\lim\limits_{n \to +\infty} w_n$.

d) Justifier que $\dfrac{w_n}{1 + e^3} \le v_n \le \dfrac{w_n}{2}$ puis en déduire $\lim\limits_{n \to +\infty} v_n$.
""", r"""
$f$ n'est définie que pour $x > 0$ (à cause de $\ln x$), donc sur $]0;+\infty[$ (le sujet écrit « sur $]-1;+\infty[$ »).

**1. a)** En $0^+$ : $x^3\ln x \to 0$ et $x^3 \to 0$, donc $u(x) \to 1$. En $+\infty$ : $1 - 3\ln x \to -\infty$ et $x^3 \to +\infty$, donc $u(x) \to -\infty$.

**b)** $u'(x) = 3x^2(1 - 3\ln x) + x^3 \times \left(-\dfrac{3}{x}\right) = -9x^2\ln x$, du signe de $-\ln x$. $u(1) = 2$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $u'(x)$ | | $+$ | $0$ | $-$ | |
| $u(x)$ | $1$ | ↗ | $2$ | ↘ | $-\infty$ |

**c)** Sur $]0;1]$, $u(x) > 1 > 0$. Sur $[1;+\infty[$, $u$ est continue et strictement décroissante de $2$ à $-\infty$ : elle s'annule une seule fois, en $\alpha$. $u(1{,}5) \approx 0{,}27 > 0$ et $u(1{,}6) \approx -0{,}68 < 0$, donc $1{,}5 \le \alpha \le 1{,}6$ ($\alpha \approx 1{,}53$).

$u(x) > 0$ sur $]0;\alpha[$, $u(\alpha) = 0$, $u(x) < 0$ sur $]\alpha;+\infty[$.

**2. a)** En $0^+$ : $3\ln x \to -\infty$ et $1 + x^3 \to 1$, donc $f(x) \to -\infty$ : la droite $x = 0$ est **asymptote verticale**. En $+\infty$ : $f(x) = \dfrac{3\ln x}{x^3} \times \dfrac{x^3}{1 + x^3} \to 0$ : la droite $y = 0$ est **asymptote horizontale**.

**b)** $f'(x) = \dfrac{\frac{3}{x}(1 + x^3) - 3\ln x \times 3x^2}{(1 + x^3)^2} = \dfrac{3(1 + x^3 - 3x^3\ln x)}{x(1 + x^3)^2} = \dfrac{3u(x)}{x(1 + x^3)^2}$, du signe de $u(x)$.

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $\frac{1}{\alpha^3}$ | ↘ | $0$ |

**c)** $u(\alpha) = 0 \iff 1 + \alpha^3 = 3\alpha^3\ln\alpha \iff 3\ln\alpha = \dfrac{1 + \alpha^3}{\alpha^3}$, donc $f(\alpha) = \dfrac{3\ln\alpha}{1 + \alpha^3} = \dfrac{1}{\alpha^3}$ ($\approx 0{,}28$).

$(C)$ coupe l'axe des abscisses en $(1;0)$, a pour maximum $\left(\alpha;\dfrac{1}{\alpha^3}\right)$ et les asymptotes $x = 0$ et $y = 0$.

**3. a)** Pour $t \in [1;e]$ : $0 \le \ln t \le 1$, donc $0 \le (\ln t)^{n+1} \le (\ln t)^n$ et, en divisant par $1 + t^3 > 0$ puis en intégrant, $0 \le v_{n+1} \le v_n$. $(v_n)$ est **décroissante** et **minorée par $0$**, donc **convergente**.

**b)** Pour $t \in [1;e]$ : $2 \le 1 + t^3 \le 1 + e^3$, donc $\dfrac{1}{1 + e^3} \le \dfrac{1}{1 + t^3} \le \dfrac{1}{2} \le 1$. En multipliant par $(\ln t)^n \ge 0$ et en intégrant :
$$\dfrac{1}{1 + e^3}\int_1^e (\ln t)^n\,dt \le v_n \le \dfrac{1}{2}\int_1^e (\ln t)^n\,dt \le \int_1^e (\ln t)^n\,dt.$$

**4. a)** Comme en 3. a) : $0 \le (\ln t)^{n+1} \le (\ln t)^n$ sur $[1;e]$, donc $w_{n+1} \le w_n$.

**b)** Par parties, avec $u = (\ln t)^{n+1}$ et $v' = 1$ :
$$w_{n+1} = \big[t(\ln t)^{n+1}\big]_1^e - (n + 1)\int_1^e (\ln t)^n\,dt = e - (n + 1)w_n.$$

**c)** $w_{n+1} \le w_n$ donne $e - (n + 1)w_n \le w_n$, soit $w_n \ge \dfrac{e}{n + 2}$. $w_{n+1} \ge 0$ donne $(n + 1)w_n \le e$, soit $w_n \le \dfrac{e}{n + 1}$. Par le théorème des gendarmes, $\lim\limits_{n \to +\infty} w_n = 0$.

**d)** C'est l'encadrement intermédiaire obtenu en 3. b) : $\dfrac{w_n}{1 + e^3} \le v_n \le \dfrac{w_n}{2}$. Comme $w_n \to 0$, $\lim\limits_{n \to +\infty} v_n = 0$.
""", [SU, IP], note="Le sujet écrit « f définie sur ]−1 ; +∞[ » : à cause de ln x, f n'est définie que sur ]0 ; +∞[ (corrigé dans l'énoncé, signalé dans la correction).")

_add("bac-c-2019-sn-math-ex5", r"""
**Exercice 5 (4 points)**

Soit $f$ la fonction définie par $f(x) = \dfrac{1}{\sqrt{1 + e^x}}$.

**1°** Étudier les variations de $f$ et tracer sa courbe $\Gamma$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**2°** Montrer que l'équation $f(x) = x$ admet une unique solution $\alpha$ et que $0{,}5 < \alpha < 0{,}6$.

*(Le sujet original indique $0{,}7 < \alpha < 0{,}8$ : cet encadrement est faux, voir la correction.)*

**3°** Soit $A$ l'aire du domaine délimité par $\Gamma$, $(Ox)$ et les droites d'équations $x = \alpha$ et $x = \ln 3$.

a) Montrer que $A = \displaystyle\int_\alpha^{\ln 3} \dfrac{dx}{\sqrt{1 + e^x}}$.

b) En posant $t = \dfrac{1}{\sqrt{1 + e^x}}$, montrer que $A = \displaystyle\int_\alpha^{\frac{1}{2}} \dfrac{2\,dt}{t^2 - 1}$.

c) Déterminer les réels $a$ et $b$ tels que $\dfrac{2}{t^2 - 1} = \dfrac{a}{t - 1} + \dfrac{b}{t + 1}$ et en déduire la valeur de $A$.

**4°** Soit $(I_n)$ la suite définie pour tout $n \in \mathbb{N}^*$ par $I_n = \displaystyle\int_\alpha^{\ln 3} \big(f(t)\big)^{2n}\,dt$ et $S_n = \displaystyle\sum_{k=1}^{n} I_k = I_1 + I_2 + \dots + I_n$.

a) Montrer pour tout $n \in \mathbb{N}^*$ que $\dfrac{\ln 3 - \alpha}{2^{2n}} \le I_n \le (\ln 3 - \alpha)\alpha^{2n}$ puis en déduire $\lim\limits_{n \to +\infty} I_n$.

b) Montrer que $\forall x \in \mathbb{R}$, $2f'(x) = \big(f(x)\big)^3 - f(x)$ $\quad (1)$.

c) En déduire que $\forall x \in \mathbb{R}$, $\big(f(x)\big)^2 = 1 + 2\left(\dfrac{f'(x)}{f(x)}\right)$ puis en déduire $I_1$.

**5° a)** Montrer à l'aide de l'égalité $(1)$ que $\forall n \in \mathbb{N}^*$, $I_{n+1} - I_n = \dfrac{1}{n}\left(\dfrac{1}{2^{2n}} - \alpha^{2n}\right)$.

b) Montrer que $I_{n+1} = \ln\left(\dfrac{3e^{-\alpha}}{4\alpha^2}\right) + \displaystyle\sum_{k=1}^{n} \dfrac{1}{k}\left(\dfrac{1}{2^{2k}} - \alpha^{2k}\right)$.

c) En déduire que $\lim\limits_{n \to +\infty}\left(\displaystyle\sum_{k=1}^{n} \dfrac{1}{k}\left(\alpha^{2k} - \dfrac{1}{2^{2k}}\right)\right) = \ln\left(\dfrac{3}{4(1 - \alpha^2)}\right)$.
""", r"""
**1°** $f$ est définie sur $\mathbb{R}$ ($1 + e^x > 0$). $f(x) = (1 + e^x)^{-1/2}$, donc $f'(x) = -\dfrac{e^x}{2(1 + e^x)^{3/2}} < 0$ : $f$ est strictement décroissante. En $-\infty$, $f(x) \to 1$ ; en $+\infty$, $f(x) \to 0$ ; $f(0) = \dfrac{1}{\sqrt{2}}$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $-$ | |
| $f(x)$ | $1$ | ↘ | $0$ |

$\Gamma$ admet les asymptotes horizontales $y = 1$ (en $-\infty$) et $y = 0$ (en $+\infty$).

**2°** $h(x) = f(x) - x$ est continue et strictement décroissante sur $\mathbb{R}$, de $+\infty$ à $-\infty$ : l'équation $f(x) = x$ a une unique solution $\alpha$.

$h(0{,}5) \approx 0{,}614 - 0{,}5 > 0$ et $h(0{,}6) \approx 0{,}595 - 0{,}6 < 0$, donc $0{,}5 < \alpha < 0{,}6$ ($\alpha \approx 0{,}596$).

**Le sujet demande de montrer $0{,}7 < \alpha < 0{,}8$ : c'est faux**, car $f(0{,}7) \approx 0{,}576 < 0{,}7$, donc $h(0{,}7) < 0$ et $\alpha < 0{,}7$.

**3° a)** $f > 0$ et $\alpha < \ln 3$ ($\ln 3 \approx 1{,}10$), donc $A = \displaystyle\int_\alpha^{\ln 3} f(x)\,dx = \int_\alpha^{\ln 3}\dfrac{dx}{\sqrt{1 + e^x}}$.

**b)** $t = \dfrac{1}{\sqrt{1 + e^x}} \iff 1 + e^x = \dfrac{1}{t^2} \iff x = \ln(1 - t^2) - 2\ln t$, avec $t \in ]0;1[$. Alors $dx = \left(\dfrac{-2t}{1 - t^2} - \dfrac{2}{t}\right)dt = \dfrac{-2}{t(1 - t^2)}\,dt$.

Pour $x = \alpha$ : $t = f(\alpha) = \alpha$ ; pour $x = \ln 3$ : $t = \dfrac{1}{\sqrt{4}} = \dfrac{1}{2}$. Donc
$$A = \int_\alpha^{1/2} t \times \dfrac{-2}{t(1 - t^2)}\,dt = \int_\alpha^{1/2}\dfrac{2\,dt}{t^2 - 1}.$$

**c)** $\dfrac{1}{t - 1} - \dfrac{1}{t + 1} = \dfrac{2}{t^2 - 1}$ : $a = 1$, $b = -1$. Pour $t \in ]0;1[$ :
$$A = \left[\ln\dfrac{1 - t}{1 + t}\right]_\alpha^{1/2} = \ln\dfrac{1}{3} - \ln\dfrac{1 - \alpha}{1 + \alpha} = \ln\left(\dfrac{1 + \alpha}{3(1 - \alpha)}\right) \text{ u.a.} \approx 0{,}28 \text{ u.a.}$$

**4° a)** Sur $[\alpha;\ln 3]$, $f$ décroît de $f(\alpha) = \alpha$ à $f(\ln 3) = \dfrac{1}{2}$ : $\dfrac{1}{2} \le f(t) \le \alpha$, donc $\dfrac{1}{2^{2n}} \le f(t)^{2n} \le \alpha^{2n}$. En intégrant sur un intervalle de longueur $\ln 3 - \alpha$ :
$$\dfrac{\ln 3 - \alpha}{2^{2n}} \le I_n \le (\ln 3 - \alpha)\alpha^{2n}.$$

Comme $0 < \alpha < 1$, $\alpha^{2n} \to 0$ : $\lim\limits_{n \to +\infty} I_n = 0$.

**b)** $f(x)^3 - f(x) = (1 + e^x)^{-3/2} - (1 + e^x)^{-1/2} = (1 + e^x)^{-3/2}\big(1 - (1 + e^x)\big) = -\dfrac{e^x}{(1 + e^x)^{3/2}} = 2f'(x)$.

**c)** En divisant $(1)$ par $f(x) > 0$ : $f(x)^2 - 1 = \dfrac{2f'(x)}{f(x)}$, d'où $f(x)^2 = 1 + 2\dfrac{f'(x)}{f(x)}$. Alors
$$I_1 = \int_\alpha^{\ln 3}\left(1 + 2\dfrac{f'(t)}{f(t)}\right)dt = \ln 3 - \alpha + 2\big[\ln f(t)\big]_\alpha^{\ln 3} = \ln 3 - \alpha + 2\ln\dfrac{1}{2} - 2\ln\alpha = \ln\left(\dfrac{3e^{-\alpha}}{4\alpha^2}\right).$$

**5° a)** $I_{n+1} - I_n = \displaystyle\int_\alpha^{\ln 3} f^{2n-1}(t)\big(f^3(t) - f(t)\big)\,dt = \int_\alpha^{\ln 3} 2f^{2n-1}(t)f'(t)\,dt = \left[\dfrac{f^{2n}(t)}{n}\right]_\alpha^{\ln 3} = \dfrac{1}{n}\left(\dfrac{1}{2^{2n}} - \alpha^{2n}\right)$.

**b)** $I_{n+1} = I_1 + \displaystyle\sum_{k=1}^{n}(I_{k+1} - I_k) = \ln\left(\dfrac{3e^{-\alpha}}{4\alpha^2}\right) + \sum_{k=1}^{n}\dfrac{1}{k}\left(\dfrac{1}{2^{2k}} - \alpha^{2k}\right)$.

**c)** Comme $I_{n+1} \to 0$ : $\displaystyle\sum_{k=1}^{n}\dfrac{1}{k}\left(\alpha^{2k} - \dfrac{1}{2^{2k}}\right) \to \ln\left(\dfrac{3e^{-\alpha}}{4\alpha^2}\right)$.

Or $f(\alpha) = \alpha$ donne $1 + e^\alpha = \dfrac{1}{\alpha^2}$, soit $e^\alpha = \dfrac{1 - \alpha^2}{\alpha^2}$ et $\dfrac{e^{-\alpha}}{\alpha^2} = \dfrac{1}{1 - \alpha^2}$. Donc la limite vaut $\ln\left(\dfrac{3}{4(1 - \alpha^2)}\right)$.
""", [IP, SU], note="Question 2° : le sujet demande de montrer 0,7 < α < 0,8, ce qui est faux (α ≈ 0,596, donc 0,5 < α < 0,6). L'énoncé donne le bon encadrement et signale l'erreur ; la correction le démontre.")

# ═══════════════════════════════ 2020 ═════════════════════════════════════════

_add("bac-c-2020-sn-math-ex4", r"""
**Exercice 4 (4 points)**

**I. 1°** On considère la fonction numérique $f$ définie sur $[0;+\infty[$ par $f(0) = 0$ et $\forall x > 0$, $f(x) = x\ln\left(\dfrac{x + 1}{x}\right)$.

On note $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

a) Étudier la continuité et la dérivabilité de $f$ à droite de $0$ (on pourra écrire $f(x) = x\ln(x + 1) - x\ln x$).

b) Pour tout $x \in ]0;+\infty[$, calculer $f'(x)$ et montrer que $f''(x) = \dfrac{-1}{x(x + 1)^2}$.

c) Étudier les variations de $f'$ et en déduire que $\forall x > 0$, $f'(x) > 0$.

**2° a)** Montrer que $\lim\limits_{x \to +\infty} f(x) = 1$. Interpréter graphiquement.

b) Dresser le tableau de variations de la fonction $f$ et tracer sa courbe $(C)$.

**II.** Soit $g$ la fonction définie sur $]0;+\infty[$ par : $g(x) = -\dfrac{1}{x}\big(f(x) - 1\big) = \dfrac{1}{x} - \ln\left(\dfrac{x + 1}{x}\right)$.

**1° a)** Montrer que pour tout entier naturel $n \ge 1$, on a : $g(n) = \dfrac{1}{n} - \displaystyle\int_n^{n+1} \dfrac{1}{x}\,dx$.

b) Justifier que $\forall n \ge 1$, on a : $\dfrac{1}{n + 1} \le \displaystyle\int_n^{n+1} \dfrac{1}{x}\,dx \le \dfrac{1}{n}$ et en déduire que $0 \le g(n) \le \dfrac{1}{n(n + 1)}$.

**2°** Pour tout entier naturel $n \ge 1$, on définit la suite $(U_n)$ par :
$$U_n = \dfrac{1}{n(n + 1)} + \dfrac{1}{(n + 1)(n + 2)} + \dots + \dfrac{1}{2n(2n + 1)} = \sum_{k=n}^{2n} \dfrac{1}{k(k + 1)}.$$

a) Montrer que $\forall n \ge 1$, $0 \le g(n) + g(n + 1) + g(n + 2) + \dots + g(2n) \le U_n$.

b) Justifier que $\forall k \in \mathbb{N}^*$, $\dfrac{1}{k(k + 1)} = \dfrac{1}{k} - \dfrac{1}{k + 1}$ et en déduire que $\forall n \ge 1$, $U_n = \dfrac{n + 1}{n(2n + 1)}$.

c) Calculer $\lim\limits_{n \to +\infty} U_n$ et en déduire que $\lim\limits_{n \to +\infty}\big[g(n) + g(n + 1) + \dots + g(2n)\big] = 0$.
""", r"""
**I. 1° a)** Pour $x > 0$ : $f(x) = x\ln(x + 1) - x\ln x$. Quand $x \to 0^+$ : $x\ln(x + 1) \to 0$ et $x\ln x \to 0$, donc $f(x) \to 0 = f(0)$ : $f$ est **continue à droite en $0$**.

$\dfrac{f(x) - f(0)}{x} = \ln\left(\dfrac{x + 1}{x}\right) = \ln\left(1 + \dfrac{1}{x}\right) \to +\infty$ : $f$ **n'est pas dérivable à droite en $0$** ; $(C)$ admet en $O$ une **demi-tangente verticale**.

**b)** $f'(x) = \ln\left(\dfrac{x + 1}{x}\right) + x\left(\dfrac{1}{x + 1} - \dfrac{1}{x}\right) = \ln\left(\dfrac{x + 1}{x}\right) - \dfrac{1}{x + 1}$.

$f''(x) = \dfrac{1}{x + 1} - \dfrac{1}{x} + \dfrac{1}{(x + 1)^2} = \dfrac{x(x + 1) - (x + 1)^2 + x}{x(x + 1)^2} = \dfrac{-1}{x(x + 1)^2}$.

**c)** $f''(x) < 0$ : $f'$ est strictement décroissante sur $]0;+\infty[$. En $+\infty$ : $\ln\left(1 + \dfrac{1}{x}\right) \to 0$ et $\dfrac{1}{x + 1} \to 0$, donc $f'(x) \to 0$. Une fonction strictement décroissante de limite $0$ en $+\infty$ est strictement positive : $\forall x > 0$, $f'(x) > 0$.

**2° a)** Avec $u = \dfrac{1}{x} \to 0^+$ : $f(x) = \dfrac{\ln(1 + u)}{u} \to 1$. La droite $y = 1$ est **asymptote horizontale** en $+\infty$.

**b)** $f$ est strictement croissante de $0$ à $1$ :

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | |
| $f(x)$ | $0$ | ↗ | $1$ |

$(C)$ part de $O$ avec une demi-tangente verticale, passe par $(1;\ln 2)$ et reste sous l'asymptote $y = 1$.

**II.** $-\dfrac{1}{x}\big(f(x) - 1\big) = \dfrac{1}{x} - \ln\left(\dfrac{x + 1}{x}\right)$ : les deux écritures de $g$ coïncident.

**1° a)** $\displaystyle\int_n^{n+1}\dfrac{dx}{x} = \ln(n + 1) - \ln n = \ln\left(\dfrac{n + 1}{n}\right)$, donc $g(n) = \dfrac{1}{n} - \displaystyle\int_n^{n+1}\dfrac{dx}{x}$.

**b)** Pour $x \in [n;n + 1]$ : $\dfrac{1}{n + 1} \le \dfrac{1}{x} \le \dfrac{1}{n}$ ; en intégrant sur cet intervalle de longueur $1$, on obtient l'encadrement. Alors
$$0 = \dfrac{1}{n} - \dfrac{1}{n} \le g(n) \le \dfrac{1}{n} - \dfrac{1}{n + 1} = \dfrac{1}{n(n + 1)}.$$

**2° a)** En sommant l'encadrement de 1° b) pour $k = n, n + 1, \dots, 2n$ :
$$0 \le g(n) + g(n + 1) + \dots + g(2n) \le \sum_{k=n}^{2n}\dfrac{1}{k(k + 1)} = U_n.$$

**b)** $\dfrac{1}{k} - \dfrac{1}{k + 1} = \dfrac{(k + 1) - k}{k(k + 1)} = \dfrac{1}{k(k + 1)}$. La somme est télescopique :
$$U_n = \sum_{k=n}^{2n}\left(\dfrac{1}{k} - \dfrac{1}{k + 1}\right) = \dfrac{1}{n} - \dfrac{1}{2n + 1} = \dfrac{n + 1}{n(2n + 1)}.$$

**c)** $U_n = \dfrac{n + 1}{2n^2 + n} \to 0$. Par le théorème des gendarmes, $\lim\limits_{n \to +\infty}\big[g(n) + g(n + 1) + \dots + g(2n)\big] = 0$.
""", [SU, IP])

_add("bac-c-2020-sn-math-ex5", r"""
**Exercice 5 (5 points)**

**1°** Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (x + 2)e^{-x}$ et $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

a) Calculer et interpréter les limites suivantes : $\lim\limits_{x \to -\infty} f(x)$ ; $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x}$.

b) Dresser le tableau de variations de $f$ et tracer sa courbe représentative $(C)$.

**2°** Soit $g$ la restriction de $f$ sur l'intervalle $I = [-1;+\infty[$.

a) Montrer que $g$ réalise une bijection de l'intervalle $I$ sur un intervalle $J$ à déterminer.

b) Tracer dans le repère précédent la courbe $(C')$ de la fonction $g^{-1}$ où $g^{-1}$ est la réciproque de $g$.

**3°** Pour tout entier naturel non nul $n$, on pose : $I_n = \displaystyle\int_{-2}^{0} \dfrac{(x + 2)^ne^{-x}}{n!}\,dx$ et $U_n = \displaystyle\sum_{k=0}^{n} \dfrac{2^k}{k!}$.

a) Vérifier que pour tout $x \in [-2;0]$ on a : $0 \le \dfrac{(x + 2)^n}{n!}e^{-x} \le \dfrac{2^n}{n!}e^2$.

b) Justifier à l'aide d'une intégration par parties que $I_1 = e^2 - 3$.

c) Montrer que pour tout $n \in \mathbb{N}^*$ : $I_{n+1} = I_n - \dfrac{2^{n+1}}{(n + 1)!}$ puis en déduire que $\forall n \in \mathbb{N}^*$, $I_n = e^2 - U_n$.

**4°** Soit $v_n = \dfrac{2^n}{n!}$. Montrer que $\forall n \ge 2$, $v_{n+1} \le \dfrac{2}{3}v_n$ puis en déduire que $\forall n \ge 2$, $v_n \le 2 \times \left(\dfrac{2}{3}\right)^{n-2}$ et préciser la limite de $(v_n)$.

**5°** En utilisant la question 3° a), justifier que $0 \le I_n \le 2e^2 \times v_n$ puis en déduire $\lim\limits_{n \to +\infty} I_n$ et $\lim\limits_{n \to +\infty} U_n$.
""", r"""
**1° a)** En $-\infty$ : $x + 2 \to -\infty$ et $e^{-x} \to +\infty$, donc $f(x) \to -\infty$. $\dfrac{f(x)}{x} = \left(1 + \dfrac{2}{x}\right)e^{-x} \to +\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

En $+\infty$ : $f(x) = \dfrac{x}{e^x} + \dfrac{2}{e^x} \to 0$ : la droite $y = 0$ est **asymptote horizontale** en $+\infty$.

**b)** $f'(x) = e^{-x} - (x + 2)e^{-x} = -(x + 1)e^{-x}$, du signe de $-(x + 1)$. $f(-1) = e$.

| $x$ | $-\infty$ | | $-1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $-\infty$ | ↗ | $e$ | ↘ | $0$ |

$(C)$ coupe $(Ox)$ en $(-2;0)$ et $(Oy)$ en $(0;2)$.

**2° a)** $g$ est continue et strictement décroissante sur $[-1;+\infty[$, de $e$ à $0$ (limite non atteinte) : bijection de $I$ sur $J = ]0;e]$.

**b)** $(C')$ est la symétrique de la partie de $(C)$ d'abscisses $\ge -1$ par rapport à $y = x$ : elle part de $(e;-1)$ avec une tangente verticale, passe par $(2;0)$ et admet l'asymptote verticale $x = 0$ (vers $+\infty$).

**3° a)** Pour $x \in [-2;0]$ : $0 \le x + 2 \le 2$, donc $0 \le (x + 2)^n \le 2^n$ ; et $-x \le 2$, donc $0 < e^{-x} \le e^2$. D'où l'encadrement.

**b)** Par parties, avec $u = x + 2$ et $v' = e^{-x}$ :
$$I_1 = \big[-(x + 2)e^{-x}\big]_{-2}^{0} + \int_{-2}^{0}e^{-x}\,dx = -2 + \big[-e^{-x}\big]_{-2}^{0} = -2 - 1 + e^2 = e^2 - 3.$$

**c)** Par parties, avec $u = \dfrac{(x + 2)^{n+1}}{(n + 1)!}$ et $v' = e^{-x}$ :
$$I_{n+1} = \left[-\dfrac{(x + 2)^{n+1}e^{-x}}{(n + 1)!}\right]_{-2}^{0} + \int_{-2}^{0}\dfrac{(x + 2)^ne^{-x}}{n!}\,dx = -\dfrac{2^{n+1}}{(n + 1)!} + I_n.$$

Par récurrence : $I_1 = e^2 - 3 = e^2 - (1 + 2) = e^2 - U_1$ ; si $I_n = e^2 - U_n$, alors $I_{n+1} = e^2 - U_n - \dfrac{2^{n+1}}{(n + 1)!} = e^2 - U_{n+1}$.

**4°** $v_{n+1} = \dfrac{2}{n + 1}v_n$, et pour $n \ge 2$, $\dfrac{2}{n + 1} \le \dfrac{2}{3}$, donc $v_{n+1} \le \dfrac{2}{3}v_n$.

Par récurrence, avec $v_2 = 2$ : $v_n \le 2\left(\dfrac{2}{3}\right)^{n-2}$. Comme $v_n > 0$ et $\left(\dfrac{2}{3}\right)^{n-2} \to 0$ : $\lim\limits_{n \to +\infty} v_n = 0$.

**5°** En intégrant l'encadrement de 3° a) sur $[-2;0]$ (longueur $2$) : $0 \le I_n \le 2 \times \dfrac{2^n}{n!}e^2 = 2e^2v_n$. Donc $\lim\limits_{n \to +\infty} I_n = 0$ et, puisque $U_n = e^2 - I_n$, $\lim\limits_{n \to +\infty} U_n = e^2$.
""", [IP, SU])

# ═══════════════════════════════ 2021 ═════════════════════════════════════════

_add("bac-c-2021-sn-math-ex4", r"""
**Exercice 4 (4 points)**

Soit $f$ la fonction définie sur l'intervalle $I = ]-1;+\infty[$ par $f(x) = 1 + (x + 1)\ln(x + 1) - \big(\ln(x + 1)\big)^2$.

On note $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1.** Calculer et interpréter les limites suivantes : $\lim\limits_{x \to -1^+} f(x)$, $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

**2.** Pour tout réel $x > -1$, on note $u(x) = x + 1 - \ln(x + 1)$ et $v(x) = x\ln(x + 1)$.

a) Montrer que la fonction $v$ est positive sur chacun des intervalles $]-1;0[$ et $]0;+\infty[$.

b) Étudier les variations de la fonction $u$ puis en déduire qu'elle est positive sur $]-1;+\infty[$.

c) Montrer que $\forall x > -1$, $f'(x) = \dfrac{u(x) + v(x)}{x + 1}$ où $f'$ est la dérivée de $f$.

d) Dresser le tableau de variation de $f$.

**3.** Montrer que $f$ réalise une bijection de $I$ sur un intervalle $J$ à déterminer.

**4.** Soit $g(x) = f(x) - x$.

a) Étudier les variations de $g$ et justifier que l'équation $g(x) = 0$ admet sur $I$ une unique solution $\alpha$.

b) Vérifier que $-0{,}7 < \alpha < -0{,}6$. En déduire la position relative de $(C)$ et la droite $\Delta$ d'équation $y = x$.

**5.** Construire la droite $\Delta$ et les courbes $(C)$ et $(C')$ ($(C')$ étant la courbe de la réciproque $f^{-1}$ de $f$).
""", r"""
On note $L = \ln(x + 1)$.

**1.** En $-1^+$ : $L \to -\infty$, $(x + 1)L \to 0$ et $L^2 \to +\infty$, donc $f(x) \to -\infty$ : la droite $x = -1$ est **asymptote verticale**.

En $+\infty$ : $f(x) = 1 + L(x + 1 - L)$ ; $L \to +\infty$ et $x + 1 - L \to +\infty$ (car $\dfrac{L}{x + 1} \to 0$), donc $f(x) \to +\infty$.

$\dfrac{f(x)}{x} = \dfrac{1}{x} + \dfrac{x + 1}{x}L - \dfrac{L^2}{x}$ ; $\dfrac{L^2}{x} \to 0$ et $\dfrac{x + 1}{x}L \to +\infty$, donc $\dfrac{f(x)}{x} \to +\infty$ : **branche parabolique de direction $(Oy)$**.

**2. a)** Sur $]-1;0[$ : $x < 0$ et $x + 1 < 1$, donc $\ln(x + 1) < 0$ : $v(x) > 0$. Sur $]0;+\infty[$ : $x > 0$ et $\ln(x + 1) > 0$ : $v(x) > 0$. (Et $v(0) = 0$.)

**b)** $u'(x) = 1 - \dfrac{1}{x + 1} = \dfrac{x}{x + 1}$, du signe de $x$ : $u$ décroît sur $]-1;0]$ et croît sur $[0;+\infty[$, de minimum $u(0) = 1 > 0$. Donc $u(x) > 0$ sur $]-1;+\infty[$.

**c)** $f'(x) = L + (x + 1)\dfrac{1}{x + 1} - \dfrac{2L}{x + 1} = \dfrac{(x + 1)L + (x + 1) - 2L}{x + 1} = \dfrac{x + 1 + (x - 1)L}{x + 1}$.

Or $u(x) + v(x) = x + 1 - L + xL = x + 1 + (x - 1)L$. Donc $f'(x) = \dfrac{u(x) + v(x)}{x + 1}$.

**d)** $u > 0$, $v \ge 0$ et $x + 1 > 0$ : $f'(x) > 0$. $f(0) = 1$.

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | | $+$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $1$ | ↗ | $+\infty$ |

**3.** $f$ est continue et strictement croissante sur $I$, de $-\infty$ à $+\infty$ : bijection de $I$ sur $J = \mathbb{R}$.

**4. a)** $g'(x) = f'(x) - 1 = \dfrac{x + 1 + (x - 1)L - (x + 1)}{x + 1} = \dfrac{(x - 1)\ln(x + 1)}{x + 1}$.

- Sur $]-1;0[$ : $x - 1 < 0$ et $L < 0$ : $g' > 0$.
- Sur $]0;1[$ : $x - 1 < 0$ et $L > 0$ : $g' < 0$.
- Sur $]1;+\infty[$ : $g' > 0$.

$g(0) = 1$ et $g(1) = 1 + 2\ln 2 - (\ln 2)^2 - 1 = \ln 2\,(2 - \ln 2) > 0$. Sur $[0;+\infty[$, $g \ge g(1) > 0$ : pas de solution. Sur $]-1;0]$, $g$ est continue et strictement croissante, de $-\infty$ à $1$ : une unique solution $\alpha$.

**b)** $g(-0{,}7) = 1 + 0{,}3\ln 0{,}3 - (\ln 0{,}3)^2 + 0{,}7 \approx -0{,}11 < 0$ et $g(-0{,}6) = 1 + 0{,}4\ln 0{,}4 - (\ln 0{,}4)^2 + 0{,}6 \approx 0{,}39 > 0$, donc $-0{,}7 < \alpha < -0{,}6$.

$g(x) < 0$ sur $]-1;\alpha[$ : $(C)$ est **au-dessous** de $\Delta$ ; $g(x) > 0$ sur $]\alpha;+\infty[$ : $(C)$ est **au-dessus** de $\Delta$ ; ils se coupent en $(\alpha;\alpha)$.

**5.** $(C)$ : asymptote $x = -1$, passe par $(0;1)$ et $(\alpha;\alpha)$, branche parabolique verticale. $(C')$ est la symétrique de $(C)$ par rapport à $\Delta$ : asymptote horizontale $y = -1$ en $-\infty$, passe par $(1;0)$ et $(\alpha;\alpha)$, branche parabolique de direction $(Ox)$.
""", [FN])

# ═══════════════════════════════ 2022 — session complémentaire ════════════════

_add("bac-c-2022-sc-math-ex4", r"""
**Exercice 4 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (x^2 + 1)e^{-x}$. On note $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Calculer $\lim\limits_{x \to +\infty} f(x)$, interpréter graphiquement cette limite.

b) Calculer $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x}$, interpréter graphiquement ce résultat.

**2. a)** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

b) Montrer que $f$ admet une fonction réciproque, notée $f^{-1}$, définie sur un intervalle à préciser.

c) Dresser le tableau de variation de $f^{-1}$.

**3. a)** Montrer que la courbe $(C)$ admet deux points d'inflexion à préciser.

b) Déterminer une équation de la tangente $T$ à $(C)$ au point d'abscisse $0$.

c) Construire $T$, $(C)$ et $(C')$ ($(C')$ étant la courbe représentative de $f^{-1}$).

**4. a)** Soit $F(x) = (ax^2 + bx + c)e^{-x}$. Déterminer $a$, $b$ et $c$ tels que $F$ soit une primitive de $f$.

b) Montrer que la suite de terme général $u_n = \displaystyle\int_0^n f(x)\,dx$ est croissante puis exprimer $u_n$ en fonction de $n$.
""", r"""
**1. a)** $f(x) = \dfrac{x^2}{e^x} + \dfrac{1}{e^x} \to 0$ en $+\infty$ : la droite $y = 0$ est **asymptote horizontale** en $+\infty$.

**b)** En $-\infty$ : $x^2 + 1 \to +\infty$ et $e^{-x} \to +\infty$, donc $f(x) \to +\infty$. $\dfrac{f(x)}{x} = \left(x + \dfrac{1}{x}\right)e^{-x} \to -\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**2. a)** $f'(x) = 2xe^{-x} - (x^2 + 1)e^{-x} = -(x^2 - 2x + 1)e^{-x} = -(x - 1)^2e^{-x} \le 0$, nulle seulement en $x = 1$. $f(1) = \dfrac{2}{e}$.

| $x$ | $-\infty$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $-$ | |
| $f(x)$ | $+\infty$ | ↘ | $\frac{2}{e}$ | ↘ | $0$ |

**b)** $f$ est continue et strictement décroissante sur $\mathbb{R}$ (sa dérivée ne s'annule qu'en un point), de $+\infty$ à $0$ : c'est une bijection de $\mathbb{R}$ sur $]0;+\infty[$. Sa réciproque $f^{-1}$ est définie sur $]0;+\infty[$.

**c)** $f^{-1}$ a le même sens de variation que $f$ :

| $x$ | $0$ | | $\frac{2}{e}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f^{-1}(x)$ | $+\infty$ | ↘ | $1$ | ↘ | $-\infty$ |

($f^{-1}$ n'est pas dérivable en $\frac{2}{e}$, car $f'(1) = 0$ : tangente verticale en $\left(\frac{2}{e};1\right)$.)

**3. a)** $f''(x) = -2(x - 1)e^{-x} + (x - 1)^2e^{-x} = (x - 1)(x - 3)e^{-x}$ : elle s'annule en changeant de signe en $x = 1$ et en $x = 3$. $(C)$ a deux points d'inflexion : $\left(1;\dfrac{2}{e}\right)$ et $\left(3;\dfrac{10}{e^3}\right)$.

**b)** $f(0) = 1$ et $f'(0) = -1$ : $T : y = -x + 1$.

**c)** $(C)$ : asymptote $y = 0$ en $+\infty$, tangente horizontale au point d'inflexion $\left(1;\frac{2}{e}\right)$, passe par $(0;1)$ avec la tangente $T$. $(C')$ est la symétrique de $(C)$ par rapport à la droite $y = x$ (asymptote verticale $x = 0$, tangente verticale en $\left(\frac{2}{e};1\right)$).

**4. a)** $F'(x) = (2ax + b)e^{-x} - (ax^2 + bx + c)e^{-x} = \big(-ax^2 + (2a - b)x + b - c\big)e^{-x}$. $F' = f$ si et seulement si $-a = 1$, $2a - b = 0$ et $b - c = 1$, soit $a = -1$, $b = -2$, $c = -3$ :
$$F(x) = -(x^2 + 2x + 3)e^{-x}.$$

**b)** $u_{n+1} - u_n = \displaystyle\int_n^{n+1} f(x)\,dx > 0$ car $f > 0$ : $(u_n)$ est **croissante**.
$$u_n = F(n) - F(0) = 3 - (n^2 + 2n + 3)e^{-n}.$$
""", [IP, SU])

_add("bac-c-2022-sc-math-ex5", r"""
**Exercice 5 (5 points)**

**1°** Soit $f$ la fonction définie sur $I = ]0;1]$ par $f(x) = (1 - x)^2\ln x$ et soit $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 2 cm.

a) Calculer $\lim\limits_{x \to 0^+} f(x)$ puis interpréter graphiquement le résultat.

b) Étudier la dérivabilité de $f$ à gauche de $1$ et interpréter graphiquement.

c) Montrer que $\forall x \in I$, $f'(x) \ge 0$ puis dresser le tableau de variation de $f$.

d) Montrer que $f$ réalise une bijection de $I$ sur un intervalle $J$ à déterminer.

e) Tracer, dans le repère $(O;\vec{i},\vec{j})$, les courbes $\Gamma$ et $\Gamma'$ ($\Gamma'$ étant la courbe représentative de $f^{-1}$).

**2°** Pour tout entier naturel $n$ non nul, on définit la fonction $f_n$ sur $I = ]0;1]$ par $f_n(x) = (1 - x)^n\ln x$. On pose $F_n(x) = \displaystyle\int_x^1 f_n(t)\,dt$, $x \in I$.

a) En utilisant une intégration par parties, montrer que pour tout $x$ de $I$, on a :
$$F_n(x) = \dfrac{(1 - x)^{n+1}\ln x}{n + 1} + \dfrac{1}{n + 1}\int_x^1 \dfrac{(1 - t)^{n+1}}{t}\,dt.$$

b) Vérifier que $\forall t \in ]0;1]$, $1 + (1 - t) + (1 - t)^2 + (1 - t)^3 + \dots + (1 - t)^n = \dfrac{1 - (1 - t)^{n+1}}{t}$.

c) Déduire que pour tout $x$ de $I$, $\displaystyle\int_x^1 \dfrac{(1 - t)^{n+1}}{t}\,dt = -\ln x - \sum_{k=0}^{n} \dfrac{1}{k + 1}(1 - x)^{k+1}$.

d) Déduire que pour tout $x$ de $I$, $(n + 1)F_n(x) = \big(-1 + (1 - x)^{n+1}\big)\ln x - \displaystyle\sum_{k=1}^{n+1} \dfrac{(1 - x)^k}{k}$.
""", r"""
**1° a)** En $0^+$ : $(1 - x)^2 \to 1$ et $\ln x \to -\infty$, donc $f(x) \to -\infty$ : la droite $x = 0$ (axe des ordonnées) est **asymptote verticale**.

**b)** $\dfrac{f(x) - f(1)}{x - 1} = \dfrac{(1 - x)^2\ln x}{x - 1} = (x - 1)\ln x \to 0$ quand $x \to 1^-$. $f$ est dérivable à gauche en $1$ avec $f'_g(1) = 0$ : $\Gamma$ admet au point $(1;0)$ une **demi-tangente horizontale**.

**c)** $f'(x) = -2(1 - x)\ln x + \dfrac{(1 - x)^2}{x} = (1 - x)\left(-2\ln x + \dfrac{1 - x}{x}\right)$.

Pour $x \in ]0;1]$ : $1 - x \ge 0$, $-2\ln x \ge 0$ et $\dfrac{1 - x}{x} \ge 0$, donc $f'(x) \ge 0$ (et $f'(x) > 0$ sur $]0;1[$).

| $x$ | $0$ | | $1$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ |
| $f(x)$ | ‖ $-\infty$ | ↗ | $0$ |

**d)** $f$ est continue et strictement croissante sur $]0;1]$ : bijection de $I$ sur $J = ]-\infty;0]$.

**e)** $\Gamma$ : asymptote $x = 0$, arrive en $(1;0)$ avec une demi-tangente horizontale. $\Gamma'$ est sa symétrique par rapport à $y = x$ : asymptote horizontale $y = 0$ en $-\infty$, arrive en $(0;1)$ avec une demi-tangente verticale.

**2° a)** Par parties sur $[x;1]$, avec $u(t) = \ln t$ et $v'(t) = (1 - t)^n$ ($u' = \dfrac{1}{t}$, $v = -\dfrac{(1 - t)^{n+1}}{n + 1}$) :
$$F_n(x) = \left[-\dfrac{(1 - t)^{n+1}\ln t}{n + 1}\right]_x^1 + \dfrac{1}{n + 1}\int_x^1\dfrac{(1 - t)^{n+1}}{t}\,dt = \dfrac{(1 - x)^{n+1}\ln x}{n + 1} + \dfrac{1}{n + 1}\int_x^1\dfrac{(1 - t)^{n+1}}{t}\,dt.$$

**b)** Somme de $n + 1$ termes d'une suite géométrique de raison $1 - t \neq 1$ (car $t \neq 0$) : $\displaystyle\sum_{k=0}^{n}(1 - t)^k = \dfrac{1 - (1 - t)^{n+1}}{1 - (1 - t)} = \dfrac{1 - (1 - t)^{n+1}}{t}$.

**c)** D'après b), $\dfrac{(1 - t)^{n+1}}{t} = \dfrac{1}{t} - \displaystyle\sum_{k=0}^{n}(1 - t)^k$. En intégrant sur $[x;1]$, avec $\displaystyle\int_x^1(1 - t)^k\,dt = \left[-\dfrac{(1 - t)^{k+1}}{k + 1}\right]_x^1 = \dfrac{(1 - x)^{k+1}}{k + 1}$ :
$$\int_x^1\dfrac{(1 - t)^{n+1}}{t}\,dt = -\ln x - \sum_{k=0}^{n}\dfrac{(1 - x)^{k+1}}{k + 1}.$$

**d)** On multiplie a) par $n + 1$ et on remplace l'intégrale par c) :
$$(n + 1)F_n(x) = (1 - x)^{n+1}\ln x - \ln x - \sum_{k=0}^{n}\dfrac{(1 - x)^{k+1}}{k + 1} = \big(-1 + (1 - x)^{n+1}\big)\ln x - \sum_{k=1}^{n+1}\dfrac{(1 - x)^k}{k}.$$
""", [IP])

# ═══════════════════════════════ 2022 — session normale ═══════════════════════

_add("bac-c-2022-sn-math-ex4", r"""
**Exercice 4 (4 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = x - 3 - \dfrac{3\ln x}{x}$ et $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1.** Soit $u$ la fonction définie sur $]0;+\infty[$ par $u(x) = x^2 - 3 + 3\ln x$.

a) Dresser le tableau de variations de la fonction $u$.

b) Montrer que l'équation $u(x) = 0$ admet une unique solution $\alpha$ et que $1{,}4 < \alpha < 1{,}41$.

c) En déduire le signe de $u(x)$ sur $]0;+\infty[$.

**2. a)** Calculer les limites suivantes : $\lim\limits_{x \to 0^+} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$.

b) Montrer que la courbe $(C)$ admet une asymptote oblique $D$ et étudier sa position relative par rapport à $(C)$.

**3. a)** Montrer que $f'(x) = \dfrac{u(x)}{x^2}$ puis dresser le tableau de variation de $f$.

b) Construire la courbe $(C)$.

**4.** Calculer l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = e$.

**5.** Soit $\varphi$ la restriction de $f$ sur l'intervalle $I = ]0;\alpha]$.

a) Montrer que $\varphi$ réalise une bijection de $I$ sur un intervalle $J$ à déterminer.

b) Construire, dans le repère précédent, la courbe $(C')$ de la réciproque $\varphi^{-1}$ de $\varphi$.
""", r"""
**1. a)** $u'(x) = 2x + \dfrac{3}{x} > 0$ sur $]0;+\infty[$. En $0^+$, $u(x) \to -\infty$ ; en $+\infty$, $u(x) \to +\infty$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $u'(x)$ | | $+$ | |
| $u(x)$ | $-\infty$ | ↗ | $+\infty$ |

**b)** $u$ est continue et strictement croissante de $-\infty$ à $+\infty$ : l'équation $u(x) = 0$ a une unique solution $\alpha$. $u(1{,}4) \approx -0{,}031 < 0$ et $u(1{,}41) \approx 0{,}019 > 0$, donc $1{,}4 < \alpha < 1{,}41$.

**c)** $u(x) < 0$ sur $]0;\alpha[$, $u(\alpha) = 0$, $u(x) > 0$ sur $]\alpha;+\infty[$.

**2. a)** En $0^+$ : $\dfrac{\ln x}{x} \to -\infty$, donc $-\dfrac{3\ln x}{x} \to +\infty$ et $f(x) \to +\infty$ (asymptote verticale $x = 0$). En $+\infty$ : $\dfrac{\ln x}{x} \to 0$ et $f(x) \to +\infty$.

**b)** $f(x) - (x - 3) = -\dfrac{3\ln x}{x} \to 0$ en $+\infty$ : $D : y = x - 3$ est **asymptote oblique**.
- Sur $]0;1[$ : $\ln x < 0$, donc $(C)$ est **au-dessus** de $D$ ;
- sur $]1;+\infty[$ : $(C)$ est **au-dessous** de $D$ ;
- ils se coupent en $(1;-2)$.

**3. a)** $f'(x) = 1 - 3\,\dfrac{\frac{1}{x} \times x - \ln x}{x^2} = \dfrac{x^2 - 3 + 3\ln x}{x^2} = \dfrac{u(x)}{x^2}$, du signe de $u(x)$.

Comme $u(\alpha) = 0$ : $3\ln\alpha = 3 - \alpha^2$, donc $f(\alpha) = \alpha - 3 - \dfrac{3 - \alpha^2}{\alpha} = 2\alpha - 3 - \dfrac{3}{\alpha} \approx -2{,}32$.

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**b)** On trace l'asymptote $x = 0$, l'asymptote $D$, le point $(1;-2)$ commun à $(C)$ et $D$, et le minimum $(\alpha;f(\alpha))$.

**4.** Sur $[1;e]$ : $f$ est négative ($f(1) = -2$, $f(e) = e - 3 - \dfrac{3}{e} \approx -1{,}39$ et le minimum $f(\alpha)$ est négatif). Une primitive de $f$ est $x \mapsto \dfrac{x^2}{2} - 3x - \dfrac{3}{2}(\ln x)^2$. L'aire vaut
$$\mathcal{A} = -\int_1^e f(x)\,dx = -\left[\dfrac{x^2}{2} - 3x - \dfrac{3}{2}(\ln x)^2\right]_1^e = -\left(\dfrac{e^2}{2} - 3e - \dfrac{3}{2} - \dfrac{1}{2} + 3\right) = 3e - 1 - \dfrac{e^2}{2} \text{ u.a.} \approx 3{,}46 \text{ u.a.}$$

**5. a)** $\varphi$ est continue et strictement décroissante sur $]0;\alpha]$, de $+\infty$ à $f(\alpha)$ : bijection de $I$ sur $J = [f(\alpha);+\infty[ = \left[2\alpha - 3 - \dfrac{3}{\alpha};+\infty\right[$.

**b)** $(C')$ est la symétrique de la partie de $(C)$ d'abscisses dans $]0;\alpha]$ par rapport à la droite $y = x$ : elle part du point $(f(\alpha);\alpha)$ avec une tangente verticale et admet l'asymptote horizontale $y = 0$ en $+\infty$.
""", [IP])

# ═══════════════════════════════ 2023 ═════════════════════════════════════════

_add("bac-c-2023-sn-math-ex4", r"""
**Exercice 4 (4 points)**

Soit $f$ la fonction définie sur $]-1;+\infty[$ par $f(x) = \dfrac{1 + \ln(2x + 2)}{2(x + 1)}$.

On note $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 2 cm.

**1.** Calculer $\lim\limits_{x \to -1^+} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$.

**2.** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

**3. a)** Montrer que la courbe $(C)$ admet un point d'inflexion $A$ à préciser.

b) Justifier que la tangente $T$ à $(C)$ en $A$ a pour équation $y = -\dfrac{1}{e}x - \dfrac{1}{e} + \dfrac{2}{\sqrt{e}}$.

**4.** Déterminer l'intersection de $(C)$ avec les axes de coordonnées.

**5.** Soit $g$ la restriction de $f$ sur l'intervalle $I = \left[-\dfrac{1}{2};+\infty\right[$. Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ à préciser. On note $g^{-1}$ sa réciproque.

**6.** Construire $T$, $(C)$ et $(C')$ dans le repère $(O;\vec{i},\vec{j})$ ($(C')$ étant la courbe de $g^{-1}$).

**7. a)** Montrer que, sur l'intervalle $I$, l'équation $f(x) = x$ admet une unique solution $\alpha$ et que $0{,}6 < \alpha < 0{,}7$.

b) Calculer l'aire en $\text{cm}^2$ du domaine plan $D$ délimité par les axes de coordonnées et les courbes $(C)$ et $(C')$.
""", r"""
On pose $w = 2x + 2 > 0$ : $f(x) = \dfrac{1 + \ln w}{w}$.

**1.** En $-1^+$ : $w \to 0^+$, $1 + \ln w \to -\infty$, donc $f(x) \to -\infty$ (asymptote verticale $x = -1$). En $+\infty$ : $f(x) = \dfrac{1}{w} + \dfrac{\ln w}{w} \to 0$ (asymptote horizontale $y = 0$).

**2.** $f'(x) = 2 \times \dfrac{\frac{1}{w} \times w - (1 + \ln w)}{w^2} = \dfrac{-2\ln w}{w^2} = \dfrac{-\ln(2x + 2)}{2(x + 1)^2}$.

$f'(x) > 0 \iff 2x + 2 < 1 \iff x < -\dfrac{1}{2}$. $f\left(-\dfrac{1}{2}\right) = \dfrac{1 + 0}{1} = 1$.

| $x$ | $-1$ | | $-\frac{1}{2}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $1$ | ↘ | $0$ |

**3. a)** $f''(x) = 2 \times \dfrac{d}{dw}\left(\dfrac{-2\ln w}{w^2}\right) = -4\,\dfrac{w - 2w\ln w}{w^4} = \dfrac{-4(1 - 2\ln w)}{w^3}$.

$f''$ s'annule en changeant de signe pour $\ln w = \dfrac{1}{2}$, soit $w = \sqrt{e}$, c'est-à-dire $x_A = \dfrac{\sqrt{e}}{2} - 1$. Alors $f(x_A) = \dfrac{1 + \frac{1}{2}}{\sqrt{e}} = \dfrac{3}{2\sqrt{e}}$.

Point d'inflexion : $A\left(\dfrac{\sqrt{e}}{2} - 1;\dfrac{3}{2\sqrt{e}}\right)$.

**b)** $f'(x_A) = \dfrac{-2 \times \frac{1}{2}}{e} = -\dfrac{1}{e}$. Donc
$$T : y = -\dfrac{1}{e}\left(x - \dfrac{\sqrt{e}}{2} + 1\right) + \dfrac{3}{2\sqrt{e}} = -\dfrac{1}{e}x - \dfrac{1}{e} + \dfrac{1}{2\sqrt{e}} + \dfrac{3}{2\sqrt{e}} = -\dfrac{1}{e}x - \dfrac{1}{e} + \dfrac{2}{\sqrt{e}}$$
(car $\dfrac{\sqrt{e}}{2e} = \dfrac{1}{2\sqrt{e}}$).

**4.** Avec l'axe des ordonnées : $f(0) = \dfrac{1 + \ln 2}{2}$, point $\left(0;\dfrac{1 + \ln 2}{2}\right)$.

Avec l'axe des abscisses : $f(x) = 0 \iff \ln(2x + 2) = -1 \iff 2x + 2 = e^{-1} \iff x = \dfrac{1}{2e} - 1$, point $\left(\dfrac{1}{2e} - 1;0\right)$.

**5.** $g$ est continue et strictement décroissante sur $\left[-\dfrac{1}{2};+\infty\right[$, de $1$ à $0$ (limite non atteinte) : bijection de $I$ sur $J = ]0;1]$.

**6.** $(C)$ : asymptotes $x = -1$ et $y = 0$, maximum $\left(-\frac{1}{2};1\right)$, point d'inflexion $A$ avec la tangente $T$. $(C')$ est la symétrique de la partie de $(C)$ d'abscisses $\ge -\frac{1}{2}$ par rapport à $y = x$ : elle part de $\left(1;-\frac{1}{2}\right)$ avec une tangente verticale et admet l'asymptote verticale $x = 0$.

**7. a)** Sur $I$, $h(x) = f(x) - x$ est continue et strictement décroissante, de $h\left(-\frac{1}{2}\right) = \dfrac{3}{2}$ à $-\infty$ : une unique solution $\alpha$. $f(0{,}6) = \dfrac{1 + \ln 3{,}2}{3{,}2} \approx 0{,}676 > 0{,}6$ et $f(0{,}7) = \dfrac{1 + \ln 3{,}4}{3{,}4} \approx 0{,}654 < 0{,}7$, donc $0{,}6 < \alpha < 0{,}7$ ($\alpha \approx 0{,}662$).

**b)** Le domaine $D$ est limité par l'axe $(Oy)$, $(C)$ de $\left(0;f(0)\right)$ à $(\alpha;\alpha)$, $(C')$ de $(\alpha;\alpha)$ à $\left(f(0);0\right)$ et l'axe $(Ox)$ ; il est symétrique par rapport à $y = x$. Sur $[0;\alpha]$, $f(x) \ge x$, donc
$$\mathcal{A} = 2\int_0^\alpha\big(f(x) - x\big)\,dx.$$

Une primitive de $f$ est $x \mapsto \dfrac{\big(1 + \ln(2x + 2)\big)^2}{4}$. Comme $f(\alpha) = \alpha$ : $1 + \ln(2\alpha + 2) = 2\alpha(\alpha + 1)$, d'où
$$\int_0^\alpha f(x)\,dx = \alpha^2(\alpha + 1)^2 - \dfrac{(1 + \ln 2)^2}{4}.$$

$$\mathcal{A} = 2\alpha^2(\alpha + 1)^2 - \alpha^2 - \dfrac{(1 + \ln 2)^2}{2} \text{ u.a.} \approx 0{,}551 \text{ u.a.}$$

L'unité d'aire vaut $2 \times 2 = 4\ \text{cm}^2$ : $\mathcal{A} = 8\alpha^2(\alpha + 1)^2 - 4\alpha^2 - 2(1 + \ln 2)^2\ \text{cm}^2 \approx 2{,}20\ \text{cm}^2$.
""", [IP])

_add("bac-c-2023-sn-math-ex5", r"""
**Exercice 5 (5 points)**

On considère la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = \dfrac{1}{1 + e^x}$ et on note $\Gamma$ sa courbe représentative dans un repère orthonormal $(O;\vec{i},\vec{j})$.

**1. a)** Calculer et interpréter graphiquement $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$.

b) Calculer $f'(x)$ puis dresser le tableau de variation de $f$.

**2. a)** Calculer $f(x) + f(-x)$. En déduire que le point $I\left(0;\dfrac{1}{2}\right)$ est centre de symétrie pour $\Gamma$.

b) Montrer que $I$ est un point d'inflexion pour $\Gamma$ et déterminer une équation de la tangente $T$ à $\Gamma$ en $I$.

c) Construire $\Gamma$ et sa tangente $T$ en $I$ dans le repère $(O;\vec{i},\vec{j})$.

**3.** On considère la suite $(I_n)$ définie par : $I_0 = \displaystyle\int_0^1 f(x)\,dx$ et $\forall n \in \mathbb{N}^*$, $I_n = \displaystyle\int_0^1 \dfrac{e^{-nx}}{1 + e^x}\,dx$.

a) Calculer $I_0$ et montrer que $(I_n)$ est décroissante et convergente.

b) Calculer $I_n + I_{n+1}$.

c) Montrer que $\forall n \in \mathbb{N}^*$, $\dfrac{1 - e^{-n-1}}{2(n + 1)} \le I_n \le \dfrac{1 - e^{-n}}{2n}$ puis en déduire $\lim\limits_{n \to +\infty} I_n$ et $\lim\limits_{n \to +\infty} (nI_n)$.
""", r"""
**1. a)** En $-\infty$ : $e^x \to 0$, donc $f(x) \to 1$ : asymptote horizontale $y = 1$. En $+\infty$ : $e^x \to +\infty$, donc $f(x) \to 0$ : asymptote horizontale $y = 0$.

**b)** $f'(x) = -\dfrac{e^x}{(1 + e^x)^2} < 0$ : $f$ est strictement décroissante sur $\mathbb{R}$, de $1$ à $0$, avec $f(0) = \dfrac{1}{2}$.

**2. a)** $f(-x) = \dfrac{1}{1 + e^{-x}} = \dfrac{e^x}{e^x + 1}$, donc $f(x) + f(-x) = \dfrac{1 + e^x}{1 + e^x} = 1 = 2 \times \dfrac{1}{2}$ : $I\left(0;\dfrac{1}{2}\right)$ est centre de symétrie de $\Gamma$.

**b)** $f''(x) = -\dfrac{e^x(1 + e^x)^2 - e^x \times 2e^x(1 + e^x)}{(1 + e^x)^4} = \dfrac{e^x(e^x - 1)}{(1 + e^x)^3}$, du signe de $x$ : elle s'annule en changeant de signe en $0$, donc $I$ est un **point d'inflexion**.

$f'(0) = -\dfrac{1}{4}$ : $T : y = -\dfrac{1}{4}x + \dfrac{1}{2}$.

**c)** $\Gamma$ : asymptotes $y = 1$ et $y = 0$, symétrique par rapport à $I$, traverse sa tangente $T$ en $I$.

**3. a)** $I_0 = \displaystyle\int_0^1\dfrac{e^{-x}}{e^{-x} + 1}\,dx = \big[-\ln(1 + e^{-x})\big]_0^1 = \ln 2 - \ln\left(1 + \dfrac{1}{e}\right) = \ln\left(\dfrac{2e}{e + 1}\right)$.

Pour $x \in [0;1]$ : $e^{-(n+1)x} \le e^{-nx}$, donc $I_{n+1} \le I_n$ ($I_1 \le I_0$ aussi, car $I_0 = \displaystyle\int_0^1 \dfrac{e^{-0x}}{1 + e^x}\,dx$). $(I_n)$ est **décroissante** ; elle est positive, donc **convergente**.

**b)** $I_n + I_{n+1} = \displaystyle\int_0^1\dfrac{e^{-nx}(1 + e^{-x})}{1 + e^x}\,dx = \int_0^1 e^{-nx}e^{-x}\,dx = \left[-\dfrac{e^{-(n+1)x}}{n + 1}\right]_0^1 = \dfrac{1 - e^{-(n+1)}}{n + 1}$ (car $1 + e^{-x} = e^{-x}(e^x + 1)$).

**c)** $(I_n)$ décroissante : $2I_{n+1} \le I_n + I_{n+1} \le 2I_n$.
- $2I_n \ge I_n + I_{n+1} = \dfrac{1 - e^{-n-1}}{n + 1}$, d'où $I_n \ge \dfrac{1 - e^{-n-1}}{2(n + 1)}$ ;
- avec b) au rang $n - 1$ : $2I_n \le I_{n-1} + I_n = \dfrac{1 - e^{-n}}{n}$, d'où $I_n \le \dfrac{1 - e^{-n}}{2n}$.

Les deux bornes tendent vers $0$ : $\lim\limits_{n \to +\infty} I_n = 0$. En multipliant par $n$ : $\dfrac{n(1 - e^{-n-1})}{2(n + 1)} \le nI_n \le \dfrac{1 - e^{-n}}{2}$, et les deux bornes tendent vers $\dfrac{1}{2}$ : $\lim\limits_{n \to +\infty} nI_n = \dfrac{1}{2}$.
""", [IP, SU])

# ═══════════════════════════════ 2024 — session complémentaire ════════════════

_add("bac-c-2024-sc-math-ex2", r"""
**Exercice 2 (4 points)**

Soit $f$ la fonction définie par $f(0) = 0$ et $\forall x \in ]0;+\infty[$, $f(x) = x^2(1 - \ln x)$ et soit $(\Gamma)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1.** Étudier la continuité et la dérivabilité de $f$ en $0^+$.

**2. a)** Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ puis interpréter graphiquement.

b) Calculer $f'(x)$, $\forall x \in ]0;+\infty[$ et dresser le tableau de variation de $f$.

**3.** Déterminer les points d'intersection de $(\Gamma)$ avec l'axe $(Ox)$ puis construire $(\Gamma)$.

**4. a)** Soit $h$ la restriction de $f$ sur l'intervalle $\left]\sqrt{e};+\infty\right[$, montrer que $h$ admet une réciproque.

b) Dresser le tableau de variation de $h^{-1}$, réciproque de $h$, puis construire sa courbe dans le repère précédent.
""", r"""
**1.** Quand $x \to 0^+$ : $x^2 \to 0$ et $x^2\ln x \to 0$, donc $f(x) \to 0 = f(0)$ : $f$ est **continue à droite en $0$**.

$\dfrac{f(x) - f(0)}{x} = x(1 - \ln x) = x - x\ln x \to 0$ : $f$ est **dérivable à droite en $0$** avec $f'_d(0) = 0$ ; $(\Gamma)$ admet en $O$ une demi-tangente horizontale.

**2. a)** En $+\infty$ : $x^2 \to +\infty$ et $1 - \ln x \to -\infty$, donc $f(x) \to -\infty$. $\dfrac{f(x)}{x} = x(1 - \ln x) \to -\infty$ : **branche parabolique de direction $(Oy)$**.

**b)** $f'(x) = 2x(1 - \ln x) + x^2 \times \left(-\dfrac{1}{x}\right) = x(1 - 2\ln x)$, du signe de $1 - 2\ln x$ : positif pour $x < \sqrt{e}$, négatif pour $x > \sqrt{e}$. $f(\sqrt{e}) = e\left(1 - \dfrac{1}{2}\right) = \dfrac{e}{2}$.

| $x$ | $0$ | | $\sqrt{e}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | $0$ | $+$ | $0$ | $-$ | |
| $f(x)$ | $0$ | ↗ | $\frac{e}{2}$ | ↘ | $-\infty$ |

**3.** $f(x) = 0 \iff x = 0$ ou $\ln x = 1 \iff x = 0$ ou $x = e$. $(\Gamma)$ coupe $(Ox)$ en $O$ et en $(e;0)$.

$(\Gamma)$ part de $O$ (demi-tangente horizontale), monte jusqu'au maximum $\left(\sqrt{e};\dfrac{e}{2}\right)$ ($\sqrt{e} \approx 1{,}65$, $\frac{e}{2} \approx 1{,}36$), coupe $(Ox)$ en $(e;0)$ puis descend vers $-\infty$.

**4. a)** $h$ est continue et strictement décroissante sur $\left]\sqrt{e};+\infty\right[$ : c'est une bijection de $\left]\sqrt{e};+\infty\right[$ sur $\left]-\infty;\dfrac{e}{2}\right[$, donc elle admet une réciproque $h^{-1}$.

**b)** $h^{-1}$ est définie sur $\left]-\infty;\dfrac{e}{2}\right[$ et a le même sens de variation que $h$ :

| $x$ | $-\infty$ | | $\frac{e}{2}$ |
|---|---|---|---|
| $h^{-1}(x)$ | $+\infty$ | ↘ | $\sqrt{e}$ |

Sa courbe est la symétrique de celle de $h$ par rapport à la droite $y = x$ : elle passe par $(0;e)$, a une branche parabolique de direction $(Ox)$ en $-\infty$ et se termine au voisinage du point $\left(\frac{e}{2};\sqrt{e}\right)$ (non atteint) avec une tangente verticale.
""", [FN])

_add("bac-c-2024-sc-math-ex5", r"""
**Exercice 5 (4 points)**

Pour tout entier naturel $n$ non nul, on définit la fonction $f_n(x) = \dfrac{e^{-x}}{(2 - x)^n}$ sur $]-\infty;2[$ et soit $(C_n)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Montrer que $\lim\limits_{x \to -\infty} f_n(x) = +\infty$ puis calculer et interpréter graphiquement $\lim\limits_{x \to 2^-} f_n(x)$.

b) Montrer que $\forall x < 2$, $f_n'(x) = \dfrac{e^{-x}(x - 2 + n)}{(2 - x)^{n+1}}$ et dresser le tableau de variation de $f_n$.

c) Étudier la position relative des courbes $(C_n)$ et $(C_{n+1})$.

**2.** Pour tout entier naturel $n$ non nul, on pose $I_n = \displaystyle\int_{-1}^{1} f_n(x)\,dx$ et $S_n = \displaystyle\sum_{k=1}^{n} (k - 2)I_k$.

a) Justifier que $\lim\limits_{n \to +\infty} I_n = 0$.

b) Montrer que $\forall x < 2$, $f_n'(x) = -f_n(x) + nf_{n+1}(x)$, $n \in \mathbb{N}^*$.

c) Déduire que $\forall n \in \mathbb{N}^*$, $nI_{n+1} - I_n = \dfrac{1}{e} - \dfrac{e}{3^n}$.

d) Justifier que $\forall n \in \mathbb{N}^*$, $S_n = -I_n + \dfrac{n - 1}{e} + \dfrac{e}{2}\left(\dfrac{1}{3^{n-1}} - 1\right)$. En déduire $\lim\limits_{n \to +\infty} S_n$ et $\lim\limits_{n \to +\infty} \dfrac{S_n}{n}$.
""", r"""
**1. a)** En $-\infty$, posons $X = 2 - x \to +\infty$ : $e^{-x} = e^{X - 2}$, donc $f_n(x) = e^{-2}\,\dfrac{e^X}{X^n} \to +\infty$ (croissance comparée).

En $2^-$ : $e^{-x} \to e^{-2} > 0$ et $(2 - x)^n \to 0^+$, donc $f_n(x) \to +\infty$ : la droite $x = 2$ est **asymptote verticale**.

**b)** $f_n(x) = e^{-x}(2 - x)^{-n}$, donc
$$f_n'(x) = -e^{-x}(2 - x)^{-n} + ne^{-x}(2 - x)^{-n-1} = \dfrac{e^{-x}\big(-(2 - x) + n\big)}{(2 - x)^{n+1}} = \dfrac{e^{-x}(x - 2 + n)}{(2 - x)^{n+1}}.$$

Pour $x < 2$, $f_n'(x)$ a le signe de $x - (2 - n)$. $f_n(2 - n) = \dfrac{e^{n-2}}{n^n}$.

| $x$ | $-\infty$ | | $2 - n$ | | $2$ |
|---|---|---|---|---|---|
| $f_n'(x)$ | | $-$ | $0$ | $+$ | |
| $f_n(x)$ | $+\infty$ | ↘ | $\frac{e^{n-2}}{n^n}$ | ↗ | $+\infty$ ‖ |

**c)** $f_{n+1}(x) - f_n(x) = \dfrac{e^{-x}}{(2 - x)^{n+1}}\big(1 - (2 - x)\big) = \dfrac{e^{-x}(x - 1)}{(2 - x)^{n+1}}$, du signe de $x - 1$ :
- sur $]-\infty;1[$, $(C_{n+1})$ est **au-dessous** de $(C_n)$ ;
- sur $]1;2[$, $(C_{n+1})$ est **au-dessus** de $(C_n)$ ;
- elles se coupent au point $\left(1;\dfrac{1}{e}\right)$.

**2. a)** Pour $x \in [-1;1]$ : $0 < e^{-x} \le e$, donc $0 \le f_n(x) \le \dfrac{e}{(2 - x)^n}$. Pour $n \ge 2$ :
$$0 \le I_n \le e\int_{-1}^{1}(2 - x)^{-n}\,dx = e\left[\dfrac{(2 - x)^{1-n}}{n - 1}\right]_{-1}^{1} = \dfrac{e}{n - 1}\left(1 - \dfrac{1}{3^{n-1}}\right) \le \dfrac{e}{n - 1}.$$

Par le théorème des gendarmes, $\lim\limits_{n \to +\infty} I_n = 0$.

**b)** D'après 1. b) : $f_n'(x) = \dfrac{-e^{-x}(2 - x)}{(2 - x)^{n+1}} + \dfrac{ne^{-x}}{(2 - x)^{n+1}} = -f_n(x) + nf_{n+1}(x)$.

**c)** En intégrant b) sur $[-1;1]$ : $f_n(1) - f_n(-1) = -I_n + nI_{n+1}$, avec $f_n(1) = \dfrac{e^{-1}}{1} = \dfrac{1}{e}$ et $f_n(-1) = \dfrac{e}{3^n}$. Donc $nI_{n+1} - I_n = \dfrac{1}{e} - \dfrac{e}{3^n}$.

**d)** On somme c) pour $k = 1, \dots, n$ :
$$\sum_{k=1}^{n}(kI_{k+1} - I_k) = \dfrac{n}{e} - e\sum_{k=1}^{n}\dfrac{1}{3^k} = \dfrac{n}{e} - \dfrac{e}{2}\left(1 - \dfrac{1}{3^n}\right).$$

Le membre de gauche vaut $\displaystyle\sum_{j=2}^{n+1}(j - 1)I_j - \sum_{j=1}^{n}I_j = \sum_{j=2}^{n}(j - 2)I_j + nI_{n+1} - I_1 = S_n + nI_{n+1}$ (car le terme $j = 1$ de $S_n$ vaut $-I_1$).

Donc $S_n = \dfrac{n}{e} - \dfrac{e}{2} + \dfrac{e}{2 \times 3^n} - nI_{n+1}$, et avec $nI_{n+1} = I_n + \dfrac{1}{e} - \dfrac{e}{3^n}$ :
$$S_n = -I_n + \dfrac{n - 1}{e} - \dfrac{e}{2} + \dfrac{3e}{2 \times 3^n} = -I_n + \dfrac{n - 1}{e} + \dfrac{e}{2}\left(\dfrac{1}{3^{n-1}} - 1\right).$$

Comme $I_n \to 0$ et $\dfrac{1}{3^{n-1}} \to 0$ : $\lim\limits_{n \to +\infty} S_n = +\infty$ et $\lim\limits_{n \to +\infty}\dfrac{S_n}{n} = \dfrac{1}{e}$.
""", [IP, SU])

# ═══════════════════════════════ 2025 ═════════════════════════════════════════

_add("bac-c-2025-sn-math-ex4", r"""
**Exercice 4 (4 points)**

On considère la fonction $f$ définie sur $]-1;+\infty[$ par $f(x) = \dfrac{1 + \ln(x + 1)}{x + 1}$ et soit $C$ sa courbe représentative dans un repère orthonormé.

**1. a)** Montrer que $\lim\limits_{x \to -1^+} f(x) = -\infty$ et calculer $\lim\limits_{x \to +\infty} f(x)$, interpréter graphiquement.

b) Montrer que pour tout $x$ de $]-1;+\infty[$, $f'(x) = \dfrac{-\ln(x + 1)}{(x + 1)^2}$.

c) Dresser le tableau de variation de $f$.

**2.** Soit $g$ la restriction de $f$ sur $[0;+\infty[$. Montrer que $\forall n \in \mathbb{N}^*$, l'équation $g(x) = \dfrac{1}{n}$ admet une unique solution $a_n$ sur $[0;+\infty[$ puis vérifier que $\forall n \in \mathbb{N}^*$, $a_{n+1} > a_n$.

**3. a)** Construire la courbe $C$ et ses asymptotes.

b) Déterminer l'aire de la partie du plan délimitée par la courbe $C$, l'axe des abscisses et les droites d'équations respectives $x = 0$ et $x = 1$.

**4.** Pour tout entier naturel $n$ non nul, on pose $I_n = \displaystyle\int_0^1 t^nf(t)\,dt$.

a) Montrer que $(I_n)$ est décroissante et déduire qu'elle est convergente.

b) Montrer que $\forall n \in \mathbb{N}^*$, $\dfrac{1 + \ln 2}{2} \times \dfrac{1}{n + 1} \le I_n \le \dfrac{1}{n + 1}$ puis déduire la limite de $(I_n)$.
""", r"""
**1. a)** En $-1^+$ : $1 + \ln(x + 1) \to -\infty$ et $x + 1 \to 0^+$, donc $f(x) \to -\infty$ : la droite $x = -1$ est **asymptote verticale**.

En $+\infty$ : $f(x) = \dfrac{1}{x + 1} + \dfrac{\ln(x + 1)}{x + 1} \to 0$ : la droite $y = 0$ est **asymptote horizontale**.

**b)** $f'(x) = \dfrac{\frac{1}{x + 1}(x + 1) - \big(1 + \ln(x + 1)\big)}{(x + 1)^2} = \dfrac{-\ln(x + 1)}{(x + 1)^2}$.

**c)** $f'(x)$ a le signe de $-\ln(x + 1)$ : positif sur $]-1;0[$, négatif sur $]0;+\infty[$. $f(0) = 1$.

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $1$ | ↘ | $0$ |

**2.** $g$ est continue et strictement décroissante sur $[0;+\infty[$, de $1$ à $0$ (limite non atteinte) : bijection de $[0;+\infty[$ sur $]0;1]$. Pour $n \ge 1$, $\dfrac{1}{n} \in ]0;1]$ : l'équation $g(x) = \dfrac{1}{n}$ a une unique solution $a_n \ge 0$ (avec $a_1 = 0$).

$g(a_{n+1}) = \dfrac{1}{n + 1} < \dfrac{1}{n} = g(a_n)$ et $g$ est strictement décroissante, donc $a_{n+1} > a_n$.

**3. a)** $C$ : asymptotes $x = -1$ et $y = 0$, maximum $(0;1)$, coupe l'axe des abscisses en $\left(\dfrac{1}{e} - 1;0\right)$ (car $\ln(x + 1) = -1$).

**b)** Sur $[0;1]$, $f(x) > 0$. Une primitive de $f$ est $x \mapsto \ln(x + 1) + \dfrac{\big(\ln(x + 1)\big)^2}{2}$. L'aire vaut
$$\mathcal{A} = \int_0^1 f(x)\,dx = \ln 2 + \dfrac{(\ln 2)^2}{2} \text{ u.a.} \approx 0{,}93 \text{ u.a.}$$

**4. a)** Sur $[0;1]$ : $f(t) \ge 0$ et $t^{n+1} \le t^n$, donc $t^{n+1}f(t) \le t^nf(t)$ et $I_{n+1} \le I_n$ : $(I_n)$ est **décroissante**. Elle est minorée par $0$, donc **convergente**.

**b)** Sur $[0;1]$, $f$ décroît de $f(0) = 1$ à $f(1) = \dfrac{1 + \ln 2}{2}$ : $\dfrac{1 + \ln 2}{2} \le f(t) \le 1$. En multipliant par $t^n \ge 0$ et en intégrant ($\displaystyle\int_0^1 t^n\,dt = \dfrac{1}{n + 1}$) :
$$\dfrac{1 + \ln 2}{2} \times \dfrac{1}{n + 1} \le I_n \le \dfrac{1}{n + 1}.$$

Par le théorème des gendarmes, $\lim\limits_{n \to +\infty} I_n = 0$.
""", [IP, SU])

_add("bac-c-2025-sn-math-ex5", r"""
**Exercice 5 (5 points)**

On considère la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = \dfrac{1}{\sqrt{1 + e^x}}$ et soit $C$ sa courbe représentative dans un repère orthonormé.

**1. a)** Calculer $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$ puis interpréter graphiquement.

b) Calculer $f'(x)$, $\forall x \in \mathbb{R}$ ($f'$ est la dérivée de $f$). Dresser le tableau de variation de $f$.

c) Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ à préciser.

**2.** Soit $g$ la fonction réciproque de $f$.

a) Dresser le tableau de variation de $g$.

b) Déterminer l'expression de $g(x)$ sur $J$ puis montrer que $\forall x \in J$, $g'(x) = \dfrac{-2}{x(1 - x^2)}$.

**3.** Pour tout entier naturel non nul $n$, on pose $S_n(t) = \displaystyle\sum_{k=0}^{n-1} t^{2k-1}$ avec $t \in ]0;1[$.

a) Montrer que $S_n(t) = -\dfrac{1}{2}\,g'(t)\big(1 - t^{2n}\big)$.

b) Déduire que $\left(-\dfrac{1}{2} + \dfrac{1}{2 \times 2^{2n}}\right)\ln\dfrac{3}{8} \le \displaystyle\int_{\frac{1}{3}}^{\frac{1}{2}} S_n(t)\,dt \le \left(-\dfrac{1}{2} + \dfrac{1}{2 \times 3^{2n}}\right)\ln\dfrac{3}{8}$.

c) Calculer $\displaystyle\int_{\frac{1}{3}}^{\frac{1}{2}} S_n(t)\,dt$ et en déduire que $\lim\limits_{n \to +\infty}\left[\displaystyle\sum_{k=1}^{n-1} \dfrac{1}{2k}\left(\dfrac{1}{4^k} - \dfrac{1}{9^k}\right)\right] = \ln\left(\dfrac{4}{3}\sqrt{\dfrac{2}{3}}\right)$.
""", r"""
**1. a)** En $-\infty$ : $e^x \to 0$, donc $f(x) \to 1$ : asymptote horizontale $y = 1$. En $+\infty$ : $\sqrt{1 + e^x} \to +\infty$, donc $f(x) \to 0$ : asymptote horizontale $y = 0$.

**b)** $f(x) = (1 + e^x)^{-1/2}$, donc $f'(x) = -\dfrac{1}{2}e^x(1 + e^x)^{-3/2} = -\dfrac{e^x}{2(1 + e^x)\sqrt{1 + e^x}} < 0$. $f(0) = \dfrac{1}{\sqrt{2}}$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $-$ | |
| $f(x)$ | $1$ | ↘ | $0$ |

**c)** $f$ est continue et strictement décroissante sur $\mathbb{R}$, de $1$ à $0$ (limites non atteintes) : bijection de $\mathbb{R}$ sur $J = ]0;1[$.

**2. a)** $g$ est définie sur $]0;1[$ et a le même sens de variation que $f$ :

| $x$ | $0$ | | $1$ |
|---|---|---|---|
| $g(x)$ | $+\infty$ | ↘ | $-\infty$ |

**b)** Pour $y \in ]0;1[$ : $y = \dfrac{1}{\sqrt{1 + e^x}} \iff 1 + e^x = \dfrac{1}{y^2} \iff e^x = \dfrac{1 - y^2}{y^2} \iff x = \ln\left(\dfrac{1 - y^2}{y^2}\right)$. Donc, pour $x \in J$ :
$$g(x) = \ln(1 - x^2) - 2\ln x.$$

$g'(x) = \dfrac{-2x}{1 - x^2} - \dfrac{2}{x} = \dfrac{-2x^2 - 2(1 - x^2)}{x(1 - x^2)} = \dfrac{-2}{x(1 - x^2)}$.

**3. a)** $S_n(t) = \dfrac{1}{t}\displaystyle\sum_{k=0}^{n-1}(t^2)^k = \dfrac{1}{t} \times \dfrac{1 - t^{2n}}{1 - t^2}$ (suite géométrique de raison $t^2 \neq 1$). Or $-\dfrac{1}{2}g'(t) = \dfrac{1}{t(1 - t^2)}$, donc $S_n(t) = -\dfrac{1}{2}g'(t)\big(1 - t^{2n}\big)$.

**b)** Pour $t \in \left[\dfrac{1}{3};\dfrac{1}{2}\right]$ : $\dfrac{1}{3^{2n}} \le t^{2n} \le \dfrac{1}{2^{2n}}$, donc $1 - \dfrac{1}{2^{2n}} \le 1 - t^{2n} \le 1 - \dfrac{1}{3^{2n}}$ ; et $-\dfrac{1}{2}g'(t) > 0$. En intégrant :
$$\left(1 - \dfrac{1}{2^{2n}}\right)K \le \int_{1/3}^{1/2}S_n(t)\,dt \le \left(1 - \dfrac{1}{3^{2n}}\right)K, \quad K = -\dfrac{1}{2}\int_{1/3}^{1/2}g'(t)\,dt = -\dfrac{1}{2}\left(g\left(\dfrac{1}{2}\right) - g\left(\dfrac{1}{3}\right)\right).$$

$g\left(\dfrac{1}{2}\right) = \ln\dfrac{3}{4} + 2\ln 2 = \ln 3$ et $g\left(\dfrac{1}{3}\right) = \ln\dfrac{8}{9} + 2\ln 3 = \ln 8$, donc $K = -\dfrac{1}{2}\ln\dfrac{3}{8}$. Ainsi $\left(1 - \dfrac{1}{2^{2n}}\right)K = \left(-\dfrac{1}{2} + \dfrac{1}{2 \times 2^{2n}}\right)\ln\dfrac{3}{8}$, et de même pour la borne de droite : c'est l'encadrement demandé.

**c)** $S_n(t) = \dfrac{1}{t} + \displaystyle\sum_{k=1}^{n-1}t^{2k-1}$, donc
$$\int_{1/3}^{1/2}S_n(t)\,dt = \ln\dfrac{3}{2} + \sum_{k=1}^{n-1}\left[\dfrac{t^{2k}}{2k}\right]_{1/3}^{1/2} = \ln\dfrac{3}{2} + \sum_{k=1}^{n-1}\dfrac{1}{2k}\left(\dfrac{1}{4^k} - \dfrac{1}{9^k}\right).$$

Les deux bornes de b) tendent vers $-\dfrac{1}{2}\ln\dfrac{3}{8} = \dfrac{1}{2}\ln\dfrac{8}{3}$. Donc
$$\lim\limits_{n \to +\infty}\sum_{k=1}^{n-1}\dfrac{1}{2k}\left(\dfrac{1}{4^k} - \dfrac{1}{9^k}\right) = \dfrac{1}{2}\ln\dfrac{8}{3} - \ln\dfrac{3}{2} = \ln\left(\dfrac{2}{3}\sqrt{\dfrac{8}{3}}\right) = \ln\left(\dfrac{4}{3}\sqrt{\dfrac{2}{3}}\right),$$
car $\dfrac{2}{3}\sqrt{\dfrac{8}{3}} = \dfrac{2}{3} \times 2\sqrt{\dfrac{2}{3}}$.
""", [IP, SU])

# ─────────────────────────────────────────────────────────────────────────────
# Contrôles mathématiques (énoncés et corrections), rejoués par scripts/check_content.py.
CHECKS: dict[str, list[str]] = {
    "bac-c-2015-sc-math-ex4": [
        "same(D((x + 1)*exp(-x)), -x*exp(-x))",
        "all(close(Integral((1 + t)**(k + 1)*exp(-t), (t, -1, 0)).doit(), (k + 1)*Integral((1 + t)**k*exp(-t), (t, -1, 0)).doit() - 1) for k in range(1, 6))",
        "close(Integral((1 + t)*exp(-t), (t, -1, 0)).doit(), E - 2)",
        "all(Rational(1, k + 1) <= Integral((1 + t)**k*exp(-t), (t, -1, 0)).evalf() <= Rational(1, k) for k in range(1, 8))",
        "all(close(Integral((1 + t)**k*exp(-t), (t, -1, 0)).doit()/factorial(k), E - sum(1/factorial(j) for j in range(k + 1))) for k in range(1, 7))",
    ],
    "bac-c-2015-sc-math-ex5": [
        "same(D(x*log(x + 1)), log(x + 1) + x/(x + 1))",
        "integ(x**2/(1 + x), 0, 1, log(2) - Rational(1, 2)) and integ(x*log(1 + x), 0, 1, Rational(1, 4))",
        "all(close(Integral(t**k*log(1 + t), (t, 0, 1)).doit(), log(2)/(k + 1) - (-1)**(k + 1)/Integer(k + 1)*(log(2) - sum(Rational((-1)**j, j + 1) for j in range(k + 1)))) for k in range(1, 6))",
        "all(close(sum(Rational((-1)**j, j + 1) for j in range(k + 1)), log(2) - (-1)**(k + 1)*Integral(t**(k + 1)/(1 + t), (t, 0, 1)).doit()) for k in range(2, 7))",
    ],
    "bac-c-2015-sn-math-ex3": [
        "same(D(1/(1 + exp(x))), -exp(x)/(1 + exp(x))**2)",
        "same((1/(1 + exp(x))).subs(x, log((1 - Rational(1, 3))/Rational(1, 3))), Rational(1, 3) + 0*x)",
        "same(1/(1 + exp(-x)) + 1/(1 + exp(x)), 1 + 0*x)",
        "racine(x*(1 + exp(x)) - 1, 0.4, 0.5)",
        "en_racine(x*(1 + exp(x)) - 1, 0.4, 0.5, 2*Integral(1/(1 + exp(t)), (t, 0, x)).doit() - x**2, 2*log(2*(1 - x)) - x**2)",
        "en_racine(x*(1 + exp(x)) - 1, 0.4, 0.5, x + log(2*x), log(2*(1 - x)))",
        "same(D(1/(1 + exp(x))), (1/(1 + exp(x)))**2 - 1/(1 + exp(x)))",
        "all(close(Integral(1/(1 + exp(t))**(k + 1) - 1/(1 + exp(t))**k, (t, 0, a)).evalf(), (a**k - Rational(1, 2**k))/k, 1e-8) for a in [nsolve(x*(1 + exp(x)) - 1, x, 0.4)] for k in (1, 2, 3, 4))",
        "all(a**(k + 1) <= Integral(1/(1 + exp(t))**k, (t, 0, a)).evalf() <= a/2**k for a in [nsolve(x*(1 + exp(x)) - 1, x, 0.4)] for k in (1, 2, 3, 4))",
    ],
    "bac-c-2015-sn-math-ex4": [
        "same((x - 1)*(3*x**2 - 9*x + 10), 3*x**3 - 12*x**2 + 19*x - 10)",
        "same(D(3*x - 3 + log((x**2 - 4*x + 5)/x**2)), (3*x**3 - 12*x**2 + 19*x - 10)/(x**3 - 4*x**2 + 5*x))",
        "racine(3*x - 3 + log((x**2 - 4*x + 5)/x**2), -0.4, -0.3)",
        "same(2*(1 + (2*x - 4)/(x**2 - 4*x + 5) - 1/(1 + (x - 2)**2)), (2*x**2 - 4*x)/(x**2 - 4*x + 5))",
        "integ((2*x - 4)/(x**2 - 4*x + 5), 3, 2 + sqrt(3), log(2)) and integ(1/(1 + (x - 2)**2), 3, 2 + sqrt(3), pi/12)",
        "integ(log(x**2 - 4*x + 5), 3, 2 + sqrt(3), (2*sqrt(3) - 1)*log(2) - 2*sqrt(3) + 2 + pi/6)",
        "integ(2*log(x), 3, 2 + sqrt(3), 2*(2 + sqrt(3))*log(2 + sqrt(3)) - 6*log(3) + 2 - 2*sqrt(3))",
        "integ(-log((x**2 - 4*x + 5)/x**2), 3, 2 + sqrt(3), 2*(2 + sqrt(3))*log(2 + sqrt(3)) - 6*log(3) + 2 - 2*sqrt(3) - ((2*sqrt(3) - 1)*log(2) - 2*sqrt(3) + 2 + pi/6))",
    ],
    "bac-c-2016-sc-math-ex2": [
        "same(D((1 + x)*exp(-x)), -x*exp(-x)) and same(D(-(x + 2)*exp(-x)), (1 + x)*exp(-x))",
        "integ((1 + x)*exp(-x), -1, 0, E - 2)",
        "all(close(Integral((1 + t)**(k + 1)*exp(-t), (t, -1, 0)).doit()/factorial(k + 1), Integral((1 + t)**k*exp(-t), (t, -1, 0)).doit()/factorial(k) - 1/factorial(k + 1)) for k in range(1, 6))",
        "all(close(Integral((1 + t)**k*exp(-t), (t, -1, 0)).doit()/factorial(k), E - sum(1/factorial(j) for j in range(k + 1))) for k in range(1, 7))",
    ],
    "bac-c-2016-sc-math-ex3": [
        "same((exp(2*x) - 1)/(6*exp(x)), (exp(x) - exp(-x))/6)",
        "same(((exp(2*x) - 1)/(6*exp(x)))**2 - D((exp(2*x) - 1)/(6*exp(x)))**2, -Rational(1, 9) + 0*x)",
        "racine((exp(x) - exp(-x))/6 - x, 2.8, 2.9)",
        "same(((exp(x) - exp(-x))/6).subs(x, log(3*x + sqrt(9*x**2 + 1))), x)",
        "same(D(log(3*x + sqrt(9*x**2 + 1))), 3/sqrt(9*x**2 + 1))",
        "same(log(-3*x + sqrt(9*x**2 + 1)).subs(x, -x), log(3*x + sqrt(9*x**2 + 1)))",
        "en_racine((exp(x) - exp(-x))/6 - x, 2.8, 2.9, 4*Integral(t - (exp(t) - exp(-t))/6, (t, 0, x)).doit(), 2*x**2 + Rational(4, 3) - Rational(4, 3)*sqrt(9*x**2 + 1))",
        "all(close(Integral(log(3*t + sqrt(9*t**2 + 1)) - (exp(t) - exp(-t))/6, (t, 0, a)).evalf()*2, 2*a**2 + Rational(4, 3) - Rational(4, 3)*sqrt(9*a**2 + 1), 1e-8) for a in [nsolve((exp(x) - exp(-x))/6 - x, x, 2.85)])",
    ],
    "bac-c-2016-sn-math-ex3": [
        "same(D(x*exp(1/x)), exp(1/x)*(x - 1)/x)",
        "lim(x*exp(1/x) - (x + 1), oo, 0) and lim(x*exp(1/x) - (x + 1), -oo, 0)",
        "lim(x*exp(1/x), 0, oo, '+') and lim(x*exp(1/x), 0, 0, '-') and lim(exp(1/x), 0, 0, '-')",
        "all(same((x*exp(k/x)).subs(x, k*x), k*x*exp(1/x)) for k in (1, 2, 3, 5))",
        "all(same(D(x*exp(k/x)), exp(k/x)*(x - k)/x) for k in (1, 2, 3, 5))",
    ],
    "bac-c-2016-sn-math-ex4": [
        "same(log(x + 1) - x/(x + 1), log(x + 1) - 1 + 1/(x + 1))",
        "same(D(log(x + 1) - x/(x + 1)), x/(x + 1)**2) and same(D(log(x + 1) - x/(x + 1), 2), (1 - x)/(x + 1)**3)",
        "lim(log(x + 1) - x/(x + 1), -1, oo, '+') and lim((log(x + 1) - x/(x + 1))/x, oo, 0)",
        "same(D((x + 2)*log(x + 1) - 2*x), log(x + 1) - x/(x + 1)) and same(Integral(log(1 + t), (t, 0, x)).doit(), (1 + x)*log(1 + x) - x)",
        "integ(log(x + 1) - x/(x + 1), 0, Rational(1, 3), (Rational(1, 3) + 2)*log(Rational(4, 3)) - Rational(2, 3))",
        "all(same(sum((-1)**(k - 1)*x**(k - 1) for k in range(1, m + 2)) + (-1)**(m + 1)*x**(m + 1)/(1 + x), 1/(1 + x)) for m in range(1, 6))",
        "all(close(sum((-1)**(k - 1)*Rational(1 - k, k)*Rational(1, 2)**k for k in range(1, m + 2)) + (-1)**(m + 2)*Rational(1, 2)**(m + 2)/Rational(3, 2) + (-1)**(m + 1)*Integral(t**(m + 1)/(1 + t), (t, 0, Rational(1, 2))).doit(), log(Rational(3, 2)) - Rational(1, 3)) for m in range(1, 6))",
    ],
    "bac-c-2017-sc-math-ex4": [
        "all(same(D(log(x)**k), k*log(x)**(k - 1)/x) for k in (2, 3, 4, 5))",
        "integ(log(x)**2, 1, E, E - 2)",
        "all(close((-1)**(k + 1)/factorial(k + 1)*Integral(log(t)**(k + 1), (t, 1, E)).doit(), (-1)**(k + 1)*E/factorial(k + 1) + (-1)**k/factorial(k)*Integral(log(t)**k, (t, 1, E)).doit()) for k in range(2, 7))",
        "all(close((-1)**k/factorial(k)*Integral(log(t)**k, (t, 1, E)).doit(), -1 + E*sum(Rational((-1)**j, 1)/factorial(j) for j in range(k + 1))) for k in range(2, 8))",
        "same(log(x)**3 - log(x)**2, log(x)**2*(log(x) - 1))",
    ],
    "bac-c-2017-sn-math-ex3": [
        "same(1/(1 + exp(-x)) + 1/(1 + exp(x)), 1 + 0*x) and same(exp(-x)/(1 + exp(-x)), 1/(1 + exp(x)))",
        "all(same(D(exp(-k*x)/(1 + exp(-x))), -exp(-k*x)*(k + (k - 1)*exp(-x))/(1 + exp(-x))**2) for k in (0, 1, 2, 3, 5))",
        "integ(1/(1 + exp(-x)), 0, 1, log((1 + E)/2)) and integ(exp(-x)/(1 + exp(-x)), 0, 1, 1 - log((1 + E)/2))",
        "integ(exp(-2*x)/(1 + exp(-x)), 0, 1, log((1 + E)/2) - exp(-1))",
        "all(close(Integral(exp(-(k + 1)*t)/(1 + exp(-t)) + exp(-k*t)/(1 + exp(-t)), (t, 0, 1)).evalf(), (1 - exp(-k))/k) for k in range(1, 6))",
        "lim(exp(-3*x)/(1 + exp(-x))/x, -oo, -oo)",
    ],
    "bac-c-2017-sn-math-ex4": [
        "same(D(log(x)/x**2), (1 - 2*log(x))/x**3) and same((log(x)/x**2).subs(x, sqrt(E)), 1/(2*E))",
        "N(2*E) > 5 and N(2*E) < 6",
        "all(N(log(k + 1)/(k + 1)**2) <= N(Integral(log(t)/t**2, (t, k, k + 1))) <= N(log(k)/k**2) for k in range(2, 9))",
        "all(close(Integral(log(t)/t**2, (t, 2, k)).doit(), (1 + log(2))/2 - (1 + log(k))/k) for k in (2, 3, 5, 10))",
        "all((1 + log(2))/2 - (m + (m - 1)*log(m))/m**2 <= sum(log(k)/k**2 for k in range(2, m + 1)) + 0 <= (2 + 3*log(2))/4 - (1 + log(m))/m for m in range(2, 12))",
        "all(close(Integral(log(t)**k/t**2, (t, 1, 2)).doit()/factorial(k), Rational(1, 2) - Rational(1, 2)*sum(log(2)**j/factorial(j) for j in range(1, k + 1))) for k in range(1, 6))",
        "all(0 <= N(Integral(log(t)**k/t**2, (t, 1, 2))/factorial(k)) <= N(log(2)**k/factorial(k)) for k in range(1, 6))",
    ],
    "bac-c-2018-sc-math-ex2": [
        "same(D((x + 1)*exp(-1/x)), (x**2 + x + 1)/x**2*exp(-1/x))",
        "lim((x + 1)*exp(-1/x)/x, 0, 0, '+') and lim((x + 1)*exp(-1/x) - x, oo, 0)",
        "same((x + 1)*(1 - 1/x + 1/(2*x**2)) - x, 1/(2*x**2) - 1/(2*x))",
        "all(-1/v <= N((v + 1)*exp(-1/v) - v) <= 1/(2*v**2) - 1/(2*v) for v in (0.3, 1, 2.5, 7, 40))",
        "all(same((Rational(1, k + 1) - Rational(1, k))*exp(-1/x) - Rational(1, k + 1) + Rational(1, k), (Rational(1, k) - Rational(1, k + 1))*(1 - exp(-1/x))) for k in (1, 2, 5))",
        "all(en_racine((x + Rational(1, k))*exp(-1/x) - Rational(1, k), 0.05, 5, x, (exp(1/x) - 1)/k) for k in (1, 2, 3, 5))",
    ],
    "bac-c-2018-sc-math-ex4": [
        "same(D(-x + 2*log(1 + exp(x))), (exp(x) - 1)/(exp(x) + 1))",
        "same(-x + 2*log(1 + exp(x)), x + 2*log(1 + exp(-x)))",
        "same(D(-x + 2*log(1 + exp(x)))**2 - 1, -2*D(-x + 2*log(1 + exp(x)), 2))",
        "integ((exp(x) - 1)/(exp(x) + 1), 0, log(5), log(Rational(9, 5))) and same(((exp(x) - 1)/(exp(x) + 1)).subs(x, log(5)) + 0*x, Rational(2, 3) + 0*x)",
        "all(close(Integral(((exp(t) - 1)/(exp(t) + 1))**(k + 2) - ((exp(t) - 1)/(exp(t) + 1))**k, (t, 0, log(5))).evalf(), -Rational(2, k + 1)*Rational(2, 3)**(k + 1)) for k in range(0, 5))",
        "all(close(sum(Rational(1, p)*Rational(2, 3)**p for p in range(1, 2*m + 1)), log(3) - (Integral(((exp(t) - 1)/(exp(t) + 1))**(2*m), (t, 0, log(5))).evalf() + Integral(((exp(t) - 1)/(exp(t) + 1))**(2*m + 1), (t, 0, log(5))).evalf())/2) for m in (1, 2, 3))",
    ],
    "bac-c-2018-sn-math-ex4": [
        "simplify(D(exp(4*x) - 2*exp(2*x), 2) - 6*D(exp(4*x) - 2*exp(2*x)) + 8*(exp(4*x) - 2*exp(2*x))) == 0",
        "same(D(exp(4*x) - 2*exp(2*x)), 4*exp(2*x)*(exp(2*x) - 1))",
        "racine(exp(4*x) - 2*exp(2*x) - x, -0.6, -0.5)",
        "all(close((exp(4*x) - 2*exp(2*x)).subs(x, log(1 - sqrt(1 + v))/2), v) and log(1 - sqrt(1 + v))/2 <= 0 for v in (Rational(-9, 10), Rational(-1, 2), Rational(-1, 10)))",
        "en_racine(exp(4*x) - 2*exp(2*x) - x, -0.6, -0.5, 2*Integral(t - exp(4*t) + 2*exp(2*t), (t, x, 0)).doit(), Rational(3, 2) - x**2 + x/2 - exp(2*x))",
        "en_racine(exp(4*x) - 2*exp(2*x) - x, -0.6, -0.5, Rational(3, 2) - x**2 + x/2 - exp(2*x), Rational(1, 2) - x**2 + x/2 + sqrt(1 + x))",
    ],
    "bac-c-2018-sn-math-ex5": [
        "same(D(x/(x + 1) - (x + 1)*log(x + 1)), 1/(x + 1)**2 - log(x + 1) - 1)",
        "same(D(x/(x + 1) - (x + 1)*log(x + 1), 2), -2/(x + 1)**3 - 1/(x + 1))",
        "same(D(x - log(x + 1) - (x + 1)**2/2*log(x + 1) + (x**2 + 2*x)/4), x/(x + 1) - (x + 1)*log(x + 1))",
        "integ(-(x/(x + 1) - (x + 1)*log(x + 1)), 0, 3, (Rational(16, 2) + 1)*log(4) - 3 - Rational(15, 4))",
        "all(close(Rational(1, k + 1)*(Rational(k, k + 1) - (k + 1)*log(k + 1)), Rational(1, k + 1) - Rational(1, (k + 1)**2) - log(k + 1)) for k in range(1, 6))",
        "all(close(sum(Rational(1, k + 1)*(Rational(k, k + 1) - (k + 1)*log(k + 1)) for k in range(1, m)), sum(Rational(1, k) for k in range(1, m + 1)) - sum(Rational(1, k**2) for k in range(1, m + 1)) - log(factorial(m))) for m in range(1, 7))",
        "all(Rational(2, m) - 2 <= N(sum(Rational(1, k) for k in range(1, m + 1)) - sum(Rational(1, k**2) for k in range(1, m + 1)) - log(m)) <= Rational(1, m) - Rational(1, m**2) for m in range(1, 15))",
    ],
    "bac-c-2019-sc-math-ex4": [
        "same(D(1 + x**3*(1 - 3*log(x))), -9*x**2*log(x))",
        "racine(1 + x**3*(1 - 3*log(x)), 1.5, 1.6)",
        "same(D(3*log(x)/(1 + x**3)), 3*(1 + x**3*(1 - 3*log(x)))/(x*(1 + x**3)**2))",
        "en_racine(1 + x**3*(1 - 3*log(x)), 1.5, 1.6, 3*log(x)/(1 + x**3), 1/x**3)",
        "all(close(Integral(log(t)**(k + 1), (t, 1, E)).doit(), E - (k + 1)*Integral(log(t)**k, (t, 1, E)).doit()) for k in range(1, 6))",
        "all(E/(k + 2) <= N(Integral(log(t)**k, (t, 1, E))) <= E/(k + 1) for k in range(1, 8))",
        "all(N(Integral(log(t)**k, (t, 1, E)))/(1 + N(E**3)) <= N(Integral(log(t)**k/(1 + t**3), (t, 1, E))) <= N(Integral(log(t)**k, (t, 1, E)))/2 for k in (1, 2, 4))",
    ],
    "bac-c-2019-sn-math-ex5": [
        "same(D(1/sqrt(1 + exp(x))), -exp(x)/(2*(1 + exp(x))**Rational(3, 2)))",
        "racine(1/sqrt(1 + exp(x)) - x, 0.5, 0.6) and not racine(1/sqrt(1 + exp(x)) - x, 0.7, 0.8)",
        "same(2*D(1/sqrt(1 + exp(x))), (1/sqrt(1 + exp(x)))**3 - 1/sqrt(1 + exp(x)))",
        "same(2/(x**2 - 1), 1/(x - 1) - 1/(x + 1))",
        "en_racine(1/sqrt(1 + exp(x)) - x, 0.5, 0.6, Integral(1/sqrt(1 + exp(t)), (t, x, log(3))).evalf() + 0*x, log((1 + x)/(3*(1 - x))))",
        "en_racine(1/sqrt(1 + exp(x)) - x, 0.5, 0.6, Integral(1/(1 + exp(t)), (t, x, log(3))).evalf() + 0*x, log(3*exp(-x)/(4*x**2)))",
        "en_racine(1/sqrt(1 + exp(x)) - x, 0.5, 0.6, log(3*exp(-x)/(4*x**2)), log(3/(4*(1 - x**2))))",
        "all(close(Integral((1 + exp(t))**(-k - 1) - (1 + exp(t))**(-k), (t, a, log(3))).evalf(), (Rational(1, 2**(2*k)) - a**(2*k))/k, 1e-8) for a in [nsolve(1/sqrt(1 + exp(x)) - x, x, 0.6)] for k in (1, 2, 3))",
    ],
    "bac-c-2020-sn-math-ex4": [
        "same(D(x*log((x + 1)/x)), log((x + 1)/x) - 1/(x + 1)) and same(D(x*log((x + 1)/x), 2), -1/(x*(x + 1)**2))",
        "lim(x*log((x + 1)/x), oo, 1) and lim(log((x + 1)/x), 0, oo, '+')",
        "all(0 <= N(Rational(1, k) - log(Rational(k + 1, k))) <= Rational(1, k*(k + 1)) for k in range(1, 20))",
        "all(sum(Rational(1, k*(k + 1)) for k in range(m, 2*m + 1)) == Rational(m + 1, m*(2*m + 1)) for m in range(1, 9))",
    ],
    "bac-c-2020-sn-math-ex5": [
        "same(D((x + 2)*exp(-x)), -(x + 1)*exp(-x))",
        "integ((x + 2)*exp(-x), -2, 0, E**2 - 3)",
        "all(close(Integral((t + 2)**k*exp(-t), (t, -2, 0)).doit()/factorial(k), E**2 - sum(Integer(2)**j/factorial(j) for j in range(k + 1))) for k in range(1, 7))",
        "all(Integer(2)**m/factorial(m) <= 2*Rational(2, 3)**(m - 2) for m in range(2, 15))",
    ],
    "bac-c-2021-sn-math-ex4": [
        "same(D(1 + (x + 1)*log(x + 1) - log(x + 1)**2), (x + 1 - log(x + 1) + x*log(x + 1))/(x + 1))",
        "same(D(1 + (x + 1)*log(x + 1) - log(x + 1)**2 - x), (x - 1)*log(x + 1)/(x + 1))",
        "racine(1 + (x + 1)*log(x + 1) - log(x + 1)**2 - x, -0.7, -0.6)",
        "close(1 + 2*log(2) - log(2)**2 - 1, log(2)*(2 - log(2))) and N(log(2)*(2 - log(2))) > 0",
        "lim(1 + (x + 1)*log(x + 1) - log(x + 1)**2, -1, -oo, '+')",
    ],
    "bac-c-2022-sc-math-ex4": [
        "same(D((x**2 + 1)*exp(-x)), -(x - 1)**2*exp(-x)) and same(D((x**2 + 1)*exp(-x), 2), (x - 1)*(x - 3)*exp(-x))",
        "same(D(-(x**2 + 2*x + 3)*exp(-x)), (x**2 + 1)*exp(-x))",
        "integ((x**2 + 1)*exp(-x), 0, 4, 3 - 27*exp(-4))",
        "lim((x**2 + 1)*exp(-x)/x, -oo, -oo)",
    ],
    "bac-c-2022-sc-math-ex5": [
        "same(D((1 - x)**2*log(x)), (1 - x)*(-2*log(x) + (1 - x)/x))",
        "lim((x - 1)*log(x), 1, 0, '-')",
        "all(same(sum((1 - x)**j for j in range(k + 1)), (1 - (1 - x)**(k + 1))/x) for k in (1, 2, 4))",
        "all(close((k + 1)*Integral((1 - t)**k*log(t), (t, Rational(1, 3), 1)).doit(), (-1 + Rational(2, 3)**(k + 1))*log(Rational(1, 3)) - sum(Rational(2, 3)**j/j for j in range(1, k + 2))) for k in (1, 2, 3, 4))",
    ],
    "bac-c-2022-sn-math-ex4": [
        "same(D(x - 3 - 3*log(x)/x), (x**2 - 3 + 3*log(x))/x**2)",
        "racine(x**2 - 3 + 3*log(x), 1.4, 1.41)",
        "en_racine(x**2 - 3 + 3*log(x), 1.4, 1.41, x - 3 - 3*log(x)/x, 2*x - 3 - 3/x)",
        "integ(-(x - 3 - 3*log(x)/x), 1, E, 3*E - 1 - E**2/2)",
    ],
    "bac-c-2023-sn-math-ex4": [
        "same(D((1 + log(2*x + 2))/(2*(x + 1))), -log(2*x + 2)/(2*(x + 1)**2))",
        "same(D((1 + log(2*x + 2))/(2*(x + 1)), 2).subs(x, sqrt(E)/2 - 1) + 0*x, 0*x)",
        "same(((1 + log(2*x + 2))/(2*(x + 1))).subs(x, sqrt(E)/2 - 1) + 0*x, 3/(2*sqrt(E)) + 0*x)",
        "same(D((1 + log(2*x + 2))/(2*(x + 1))).subs(x, sqrt(E)/2 - 1)*(x - sqrt(E)/2 + 1) + 3/(2*sqrt(E)), -x/E - 1/E + 2/sqrt(E))",
        "racine((1 + log(2*x + 2))/(2*(x + 1)) - x, 0.6, 0.7)",
        "same(D((1 + log(2*x + 2))**2/4), (1 + log(2*x + 2))/(2*(x + 1)))",
        "en_racine((1 + log(2*x + 2))/(2*(x + 1)) - x, 0.6, 0.7, 2*Integral((1 + log(2*t + 2))/(2*(t + 1)) - t, (t, 0, x)).doit(), 2*x**2*(x + 1)**2 - x**2 - (1 + log(2))**2/2)",
    ],
    "bac-c-2023-sn-math-ex5": [
        "same(D(1/(1 + exp(x)), 2), exp(x)*(exp(x) - 1)/(1 + exp(x))**3)",
        "integ(1/(1 + exp(x)), 0, 1, log(2*E/(E + 1)))",
        "all(close(Integral(exp(-k*t)/(1 + exp(t)) + exp(-(k + 1)*t)/(1 + exp(t)), (t, 0, 1)).evalf(), (1 - exp(-(k + 1)))/(k + 1)) for k in range(0, 5))",
        "all((1 - exp(-k - 1))/(2*(k + 1)) <= N(Integral(exp(-k*t)/(1 + exp(t)), (t, 0, 1))) <= (1 - exp(-k))/(2*k) for k in range(1, 8))",
    ],
    "bac-c-2024-sc-math-ex2": [
        "same(D(x**2*(1 - log(x))), x*(1 - 2*log(x))) and same((x**2*(1 - log(x))).subs(x, sqrt(E)) + 0*x, E/2 + 0*x)",
        "lim(x*(1 - log(x)), 0, 0, '+') and lim(x*(1 - log(x)), oo, -oo)",
    ],
    "bac-c-2024-sc-math-ex5": [
        "all(same(D(exp(-x)/(2 - x)**k), exp(-x)*(x - 2 + k)/(2 - x)**(k + 1)) for k in (1, 2, 3))",
        "all(same(D(exp(-x)/(2 - x)**k), -exp(-x)/(2 - x)**k + k*exp(-x)/(2 - x)**(k + 1)) for k in (1, 2, 3))",
        "all(close(k*Integral(exp(-t)/(2 - t)**(k + 1), (t, -1, 1)).evalf() - Integral(exp(-t)/(2 - t)**k, (t, -1, 1)).evalf(), 1/E - E/Integer(3)**k) for k in (1, 2, 3, 4))",
        "all(close(sum((j - 2)*Integral(exp(-t)/(2 - t)**j, (t, -1, 1)).evalf() for j in range(1, m + 1)), -Integral(exp(-t)/(2 - t)**m, (t, -1, 1)).evalf() + (m - 1)/E + E/2*(Rational(1, 3**(m - 1)) - 1), 1e-8) for m in (1, 2, 3, 5))",
    ],
    "bac-c-2025-sn-math-ex4": [
        "same(D((1 + log(x + 1))/(x + 1)), -log(x + 1)/(x + 1)**2)",
        "integ((1 + log(x + 1))/(x + 1), 0, 1, log(2) + log(2)**2/2)",
        "all((1 + log(2))/2/(k + 1) <= N(Integral(t**k*(1 + log(t + 1))/(t + 1), (t, 0, 1))) <= Rational(1, k + 1) for k in range(1, 8))",
    ],
    "bac-c-2025-sn-math-ex5": [
        "all(close((1/sqrt(1 + exp(x))).subs(x, log(1 - v**2) - 2*log(v)), v) and close(D(log(1 - x**2) - 2*log(x)).subs(x, v), -2/(v*(1 - v**2))) for v in (Rational(1, 5), Rational(1, 2), Rational(4, 5)))",
        "all(same(sum(x**(2*j - 1) for j in range(k)), -Rational(1, 2)*D(log(1 - x**2) - 2*log(x))*(1 - x**(2*k))) for k in (1, 2, 4))",
        "close((log(1 - x**2) - 2*log(x)).subs(x, Rational(1, 2)), log(3)) and close((log(1 - x**2) - 2*log(x)).subs(x, Rational(1, 3)), log(8))",
        "all(close(Integral(sum(t**(2*j - 1) for j in range(k)), (t, Rational(1, 3), Rational(1, 2))).doit(), log(Rational(3, 2)) + sum(Rational(1, 2*j)*(Rational(1, 4**j) - Rational(1, 9**j)) for j in range(1, k))) for k in (1, 2, 4))",
        "close(log(8/Integer(3))/2 - log(Rational(3, 2)), log(Rational(4, 3)*sqrt(Rational(2, 3))))",
    ],
}
