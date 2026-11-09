"""Corrections des exercices log/exp de maths série D 2015-2024.

Les énoncés sont ceux de ``enonces_logexp_d`` (retranscrits et vérifiés sur les
PDF officiels). Chaque correction a été rédigée puis contrôlée :
  - calculs refaits par calcul formel (sympy) — voir CHECKS en fin de fichier ;
  - réponses comparées au corrigé officiel quand il existe ; les erreurs du
    sujet ou du corrigé officiel sont signalées dans la correction ;
  - contrôle automatique (scripts/check_content.py) : 0 erreur.

Chargé par ``scripts/load_corrections.py corrections_logexp_d`` :
un exercice validé par l'admin n'est jamais modifié.
"""
from enonces_logexp_d import ENONCES as _E

CORRECTIONS: dict[str, dict] = {}


def _add(eid: str, correction: str, note: str = "") -> None:
    CORRECTIONS[eid] = {"enonce": _E[eid]["enonce"], "correction": correction.strip() + "\n", "note": note}


# ═══════════════════════════════════ 2015 ═════════════════════════════════════

_add("bac-d-2015-sn-math-ex3", r"""
**1. a)** $\lim\limits_{x \to 0^+} x\ln x = 0$, donc $\lim\limits_{x \to 0^+} f(x) = -3 = f(0)$ : $f$ est continue à droite en $0$.

**b)** Pour $x > 0$ : $\dfrac{f(x) - f(0)}{x} = \dfrac{3x - 2x\ln x}{x} = 3 - 2\ln x$.

Comme $\lim\limits_{x \to 0^+} \ln x = -\infty$, on obtient $\lim\limits_{x \to 0^+} \dfrac{f(x) - f(0)}{x} = +\infty$ (et non $-\infty$ comme l'écrit le sujet).

Interprétation : $f$ n'est pas dérivable à droite en $0$ et $(C)$ admet au point $(0;-3)$ une **demi-tangente verticale**, dirigée vers le haut.

**c)** $f(x) = x(3 - 2\ln x) - 3$ avec $3 - 2\ln x \to -\infty$, donc $\lim\limits_{x \to +\infty} f(x) = -\infty$.

**2. a)** $f'(x) = 3 - 2\ln x - 2x \times \dfrac{1}{x} = 1 - 2\ln x$, et $f'(\sqrt{e}) = 1 - 2 \times \dfrac{1}{2} = 0$.

**b)** $f'(x) > 0 \iff \ln x < \dfrac{1}{2} \iff x < \sqrt{e}$. $f(\sqrt{e}) = 3\sqrt{e} - 3 - \sqrt{e} = 2\sqrt{e} - 3 \approx 0{,}30$.

| $x$ | $0$ | | $\sqrt{e}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $-3$ | ↗ | $2\sqrt{e} - 3$ | ↘ | $-\infty$ |

**3. a)** $f(1) = 0$ et $f'(1) = 1$ : $(T) : y = x - 1$.

**b)** Sur $[0;\sqrt{e}]$, $f$ s'annule seulement en $1$ ($f$ strictement croissante). Sur $[\sqrt{e};+\infty[$, $f$ est continue et strictement décroissante de $2\sqrt{e} - 3 > 0$ à $-\infty$ : elle s'annule une seule fois, en $\alpha$.

$f(2{,}3) \approx 0{,}069 > 0$ et $f(2{,}4) \approx -0{,}002 < 0$, donc $2{,}3 \le \alpha \le 2{,}4$ ($\alpha \approx 2{,}397$).

**c)** $f(x) < 0$ sur $[0;1[$, $f(x) > 0$ sur $]1;\alpha[$, et $f(x) < 0$ sur $]\alpha;+\infty[$ ; $f(1) = f(\alpha) = 0$.

**4) a)** $g'(x) = x - \left(2x\ln x + x^2 \times \dfrac{1}{x}\right) = -2x\ln x$, donc $3x - 3 + g'(x) = 3x - 3 - 2x\ln x = f(x)$.

**b)** $F(x) = \dfrac{3x^2}{2} - 3x + g(x) = 2x^2 - 3x - x^2\ln x$ est une primitive de $f$ sur $]0;+\infty[$.

**5) a)** $U_{n+1} - U_n = \displaystyle\int_{\frac{1}{n+1}}^{\frac{1}{n}} f(x)\,dx$. Sur $\left[\dfrac{1}{n + 1};\dfrac{1}{n}\right] \subset\, ]0;1]$, $f(x) \le 0$ (et $f < 0$ sauf peut-être en $1$), donc $U_{n+1} - U_n < 0$ : $(U_n)$ est **décroissante**.

**b)** $U_n = F(1) - F\left(\dfrac{1}{n}\right)$ avec $F(1) = -1$ et $F\left(\dfrac{1}{n}\right) = \dfrac{2}{n^2} - \dfrac{3}{n} + \dfrac{\ln n}{n^2}$ :
$$U_n = -1 + \dfrac{3}{n} - \dfrac{2}{n^2} - \dfrac{\ln n}{n^2}.$$

**c)** $\lim\limits_{n \to +\infty} \dfrac{\ln n}{n^2} = 0$, donc $\lim\limits_{n \to +\infty} U_n = -1$.
""", note="Question 1. b) : le sujet demande de montrer que la limite vaut −∞ ; elle vaut +∞ (= lim (3 − 2 ln x)). La correction le signale.")

_add("bac-d-2015-sn-math-ex4", r"""
**1. a)** $\lim\limits_{x \to +\infty}(x - 2) = +\infty$ et $\lim\limits_{x \to +\infty}(1 + e^x) = +\infty$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$.

$\dfrac{f(x)}{x} = \left(1 - \dfrac{2}{x}\right)(1 + e^x) \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** $f(x) - (x - 2) = (x - 2)e^x = xe^x - 2e^x \to 0$ en $-\infty$ : la droite $(D) : y = x - 2$ est **asymptote oblique** à $(C)$ en $-\infty$.

**2. a)** $f'(x) = (1 + e^x) + (x - 2)e^x = 1 + (x - 1)e^x$ et $f''(x) = e^x + (x - 1)e^x = xe^x$.

**b)** $f''$ s'annule en $0$ en changeant de signe : $(C)$ a un point d'inflexion $A(0;f(0)) = (0;-4)$.

**c)** $f''(x)$ a le signe de $x$ : $f'$ décroît sur $]-\infty;0]$ et croît sur $[0;+\infty[$. $f'(0) = 0$, $\lim\limits_{-\infty} f' = 1$ et $\lim\limits_{+\infty} f' = +\infty$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f''(x)$ | | $-$ | $0$ | $+$ | |
| $f'(x)$ | $1$ | ↘ | $0$ | ↗ | $+\infty$ |

Donc $f'(x) \ge 0$ pour tout $x$, et $f'(x) = 0$ seulement pour $x = 0$.

**3. a)** $f$ est strictement croissante sur $\mathbb{R}$ (sa dérivée ne s'annule qu'en un point).

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $-4$ | ↗ | $+\infty$ |

**b)** $f$ est continue et strictement croissante : elle réalise une bijection de $\mathbb{R}$ sur $J = \mathbb{R}$.

**4. a)** $f(0) = -4$ : point $(0;-4)$. $f(x) = 0 \iff x = 2$ (car $1 + e^x > 0$) : point $(2;0)$.

**b)** La tangente est parallèle à $(D)$ $\iff f'(x) = 1 \iff (x - 1)e^x = 0 \iff x = 1$.

$B(1;f(1)) = (1;-1 - e)$ et $T : y = (x - 1) - 1 - e$, soit $T : y = x - 2 - e$.

**c)** On trace $(D)$, $T$ (parallèle à $(D)$, en dessous), le point d'inflexion $(0;-4)$, le point $(2;0)$, puis $(C')$, symétrique de $(C)$ par rapport à $y = x$.

**d)** $x - 2 = (2 + m)e^{-x} \iff (x - 2)e^x = 2 + m \iff f(x) - (x - 2) = 2 + m \iff f(x) = x + m$.

On cherche les points communs à $(C)$ et à la droite $D_m : y = x + m$, parallèle à $(D)$.

La fonction $h(x) = (x - 2)e^x$ a pour dérivée $(x - 1)e^x$ : elle décroît de $0$ (en $-\infty$) jusqu'à $h(1) = -e$, puis croît jusqu'à $+\infty$. L'équation $h(x) = 2 + m$ a :
- **aucune solution** si $m < -2 - e$ ($D_m$ sous $T$) ;
- **une solution** ($x = 1$) si $m = -2 - e$ ($D_m = T$) ;
- **deux solutions** si $-2 - e < m < -2$ ($D_m$ entre $T$ et $(D)$) ;
- **une solution** si $m \ge -2$.

**5. a)** $I = \left[\dfrac{x^2}{2} - 2x - 2e^x\right]_0^2 = (2 - 4 - 2e^2) - (-2) = -2e^2$.

**b)** Par parties, avec $u = x$ et $v' = e^x$ : $J = \big[xe^x\big]_0^2 - \displaystyle\int_0^2 e^x\,dx = 2e^2 - (e^2 - 1) = e^2 + 1$.

**c)** $f(x) = (x - 2 - 2e^x) + xe^x$, donc $\displaystyle\int_0^2 f(x)\,dx = I + J = 1 - e^2$.

Sur $[0;2]$, $f(x) \le 0$ (car $x - 2 \le 0$), donc l'aire vaut $-(I + J) = e^2 - 1 \approx 6{,}39$ u.a.
""")

_add("bac-d-2015-sc-math-ex3", r"""
**1) a)** $\lim\limits_{x \to +\infty} g(x) = +\infty$. En $-\infty$, $2xe^x \to 0$ et $e^x \to 0$, donc $\lim\limits_{x \to -\infty} g(x) = 1$.

**b)** $g'(x) = 2e^x + (2x + 1)e^x = (2x + 3)e^x$, du signe de $2x + 3$. $g\left(-\dfrac{3}{2}\right) = 1 - 2e^{-3/2} \approx 0{,}55$.

| $x$ | $-\infty$ | | $-\frac{3}{2}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $-$ | $0$ | $+$ | |
| $g(x)$ | $1$ | ↘ | $1 - 2e^{-3/2}$ | ↗ | $+\infty$ |

**c)** Le minimum de $g$ est $1 - 2e^{-3/2} > 0$, donc $g(x) > 0$ pour tout réel $x$.

**2) a)** En $-\infty$ : $x + 2 \to -\infty$ et $(2x - 1)e^x \to 0$, donc $f(x) \to -\infty$. En $+\infty$ : $f(x) \to +\infty$.

**b)** $\dfrac{f(x)}{x} = 1 + \dfrac{2}{x} + \left(2 - \dfrac{1}{x}\right)e^x \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**c)** $f(x) - (x + 2) = (2x - 1)e^x \to 0$ en $-\infty$ : $D : y = x + 2$ est **asymptote oblique** en $-\infty$.

Cette différence a le signe de $2x - 1$ : $(C)$ est au-dessous de $D$ sur $\left]-\infty;\dfrac{1}{2}\right[$, au-dessus sur $\left]\dfrac{1}{2};+\infty\right[$, et elles se coupent en $\left(\dfrac{1}{2};\dfrac{5}{2}\right)$.

**3)** $f'(x) = 1 + 2e^x + (2x - 1)e^x = 1 + (2x + 1)e^x = g(x) > 0$ : $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**4. a)** $f$ est continue et strictement croissante : bijection de $\mathbb{R}$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : l'équation $f(x) = 0$ a une unique solution $\alpha$.

**Attention, le sujet contient une erreur :** $f(-0{,}86) \approx -0{,}011$ et $f(-0{,}85) \approx -0{,}004$ sont **tous deux négatifs**, donc $\alpha$ n'est pas entre $-0{,}86$ et $-0{,}85$. En revanche $f(-0{,}84) \approx 0{,}003 > 0$, donc
$$-0{,}85 < \alpha < -0{,}84 \quad (\alpha \approx -0{,}844).$$

**5) a)** La tangente est parallèle à $D$ $\iff f'(x) = 1 \iff (2x + 1)e^x = 0 \iff x = -\dfrac{1}{2}$ : le point $A$ est unique.

$f\left(-\dfrac{1}{2}\right) = \dfrac{3}{2} - 2e^{-1/2} \approx 0{,}29$, donc $A\left(-\dfrac{1}{2};\dfrac{3}{2} - 2e^{-1/2}\right)$ et
$$T : y = x + 2 - 2e^{-1/2}.$$

**b)** On trace $D$, $T$ (parallèle à $D$, en dessous), $A$, le point $\left(\dfrac{1}{2};\dfrac{5}{2}\right)$, le point $(0;1)$ et le point $(\alpha;0)$.

**c)** $(2x - 1)e^x - m + 2 = 0 \iff (2x - 1)e^x = m - 2 \iff f(x) = x + m$ : on cherche les points communs à $(C)$ et à $D_m : y = x + m$.

$h(x) = (2x - 1)e^x$ a pour dérivée $(2x + 1)e^x$ : elle décroît de $0$ (en $-\infty$) jusqu'à $h\left(-\dfrac{1}{2}\right) = -2e^{-1/2}$, puis croît jusqu'à $+\infty$. L'équation $h(x) = m - 2$ a :
- **aucune solution** si $m < 2 - 2e^{-1/2}$ ;
- **une solution** ($x = -\frac{1}{2}$) si $m = 2 - 2e^{-1/2}$ ($D_m = T$) ;
- **deux solutions** si $2 - 2e^{-1/2} < m < 2$ ;
- **une solution** si $m \ge 2$.
""", note="Question 4. b) : l'encadrement du sujet (−0,86 < α < −0,85) est faux ; α ≈ −0,844, donc −0,85 < α < −0,84. La correction le signale.")

_add("bac-d-2015-sc-math-ex4", r"""
**Partie A**

**1. a)** $\lim\limits_{x \to 0^+} g(x) = -\infty$ et $\lim\limits_{x \to +\infty} g(x) = +\infty$.

**b)** $g'(x) = 4x + \dfrac{1}{x} > 0$ : $g$ est strictement croissante sur $]0;+\infty[$, de $-\infty$ à $+\infty$.

**2. a)** $g$ est continue et strictement croissante : elle réalise une bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\alpha$. $g(0{,}54) \approx -0{,}033 < 0$ et $g(0{,}55) \approx 0{,}007 > 0$, donc $0{,}54 < \alpha < 0{,}55$.

**c)** $g(x) < 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) > 0$ sur $]\alpha;+\infty[$.

**Partie B**

**1. a)** $\dfrac{1 + \ln x}{x} = \dfrac{1}{x}(1 + \ln x) \to -\infty$ en $0^+$, donc $\lim\limits_{x \to 0^+} f(x) = +\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** $\dfrac{1 + \ln x}{x} = \dfrac{1}{x} + \dfrac{\ln x}{x} \to 0$ en $+\infty$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - 2x\big) = 0$.

La droite $(\Delta) : y = 2x$ est **asymptote oblique** à $(C)$ en $+\infty$.

**c)** $f(x) - 2x = -\dfrac{1 + \ln x}{x}$ a le signe de $-(1 + \ln x)$ : $(C)$ est au-dessus de $(\Delta)$ sur $\left]0;\dfrac{1}{e}\right[$, au-dessous sur $\left]\dfrac{1}{e};+\infty\right[$, et elles se coupent en $\left(\dfrac{1}{e};\dfrac{2}{e}\right)$.

**2. a)** $f'(x) = 2 - \dfrac{\frac{1}{x} \cdot x - (1 + \ln x)}{x^2} = 2 + \dfrac{\ln x}{x^2} = \dfrac{2x^2 + \ln x}{x^2} = \dfrac{g(x)}{x^2}$.

**b)** $f'(x)$ a le signe de $g(x)$ :

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**c)** $g(\alpha) = 0$ donne $\ln\alpha = -2\alpha^2$, donc
$$f(\alpha) = 2\alpha - \dfrac{1 - 2\alpha^2}{\alpha} = \dfrac{2\alpha^2 - 1 + 2\alpha^2}{\alpha} = \dfrac{4\alpha^2 - 1}{\alpha}.$$

Avec $\alpha \approx 0{,}548$ : $f(\alpha) \approx 0{,}37$.

**3. a)** $f\left(\dfrac{1}{e}\right) = \dfrac{2}{e}$ et $f'\left(\dfrac{1}{e}\right) = 2 + \dfrac{-1}{1/e^2} = 2 - e^2$, donc
$$(T) : y = (2 - e^2)\left(x - \dfrac{1}{e}\right) + \dfrac{2}{e} = (2 - e^2)x + e.$$

**b)** On trace l'asymptote $x = 0$, l'asymptote $(\Delta) : y = 2x$, le point $\left(\dfrac{1}{e};\dfrac{2}{e}\right)$ avec la tangente $(T)$, et le minimum $(\alpha;f(\alpha))$. L'unité est 2 cm.

**4. a)** Une primitive de $\dfrac{1 + \ln x}{x} = \dfrac{1}{x} + \dfrac{1}{x}\ln x$ est $\ln x + \dfrac{(\ln x)^2}{2}$, donc
$$F(x) = x^2 - \ln x - \dfrac{(\ln x)^2}{2}.$$

**b)** Le minimum de $f$ est $f(\alpha) = \dfrac{4\alpha^2 - 1}{\alpha} > 0$ (car $4\alpha^2 \approx 1{,}2 > 1$), donc $f > 0$ et l'aire vaut
$$\int_{1/e}^{1} f(x)\,dx = F(1) - F\left(\dfrac{1}{e}\right) = 1 - \left(\dfrac{1}{e^2} + 1 - \dfrac{1}{2}\right) = \dfrac{1}{2} - \dfrac{1}{e^2} \text{ u.a.} \approx 0{,}36 \text{ u.a.}$$

(Avec l'unité de 2 cm, 1 u.a. $= 4$ cm², soit environ $1{,}46$ cm².)
""")

# ═══════════════════════════════════ 2016 ═════════════════════════════════════

_add("bac-d-2016-sn-math-ex3", r"""
**1) a)** $g'(x) = -1 + e^x$.

**b)** $g'(x) > 0 \iff x > 0$ : $g$ décroît sur $]-\infty;0]$ et croît sur $[0;+\infty[$. Son minimum est $g(0) = 2 > 0$, donc $g(x) > 0$ pour tout réel $x$.

**2. a)** En $-\infty$ : $xe^{-x} \to -\infty$ ($x \to -\infty$ et $e^{-x} \to +\infty$), donc $\lim\limits_{x \to -\infty} f(x) = -\infty$.

$\dfrac{f(x)}{x} = 1 - \dfrac{1}{x} + e^{-x} \to +\infty$ en $-\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**b)** En $+\infty$ : $xe^{-x} = \dfrac{x}{e^x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $f(x) - (x - 1) = xe^{-x} \to 0$. La droite $(\Delta) : y = x - 1$ est **asymptote oblique** en $+\infty$.

$f(x) - (x - 1) = xe^{-x}$ a le signe de $x$ : $(C)$ est au-dessous de $(\Delta)$ pour $x < 0$, au-dessus pour $x > 0$, et elles se coupent en $(0;-1)$.

**3. a)** $f'(x) = 1 + e^{-x} - xe^{-x} = \dfrac{e^x + 1 - x}{e^x} = \dfrac{g(x)}{e^x}$.

**b)** $f'(x) > 0$ : $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**4. a)** Tangente parallèle à $(\Delta)$ $\iff f'(x) = 1 \iff (1 - x)e^{-x} = 0 \iff x = 1$.

$A\left(1;e^{-1}\right)$ et $T : y = (x - 1) + e^{-1}$, soit $T : y = x - 1 + \dfrac{1}{e}$.

**b)** On trace $(\Delta)$, $T$ (parallèle à $(\Delta)$, au-dessus), le point $A$ et le point $(0;-1)$.

**5) a)** $H'(x) = -e^{-x} + (x + 1)e^{-x} = xe^{-x} = f(x) - x + 1$.

Donc $F(x) = \dfrac{x^2}{2} - x + H(x) = \dfrac{x^2}{2} - x - (x + 1)e^{-x}$ est une primitive de $f$.

**b)** Sur $[1;3]$, $(C)$ est au-dessus de $(\Delta)$, donc l'aire vaut
$$\int_1^3 xe^{-x}\,dx = H(3) - H(1) = -4e^{-3} + 2e^{-1} \text{ u.a.} \approx 0{,}54 \text{ u.a.}$$
""")

_add("bac-d-2016-sn-math-ex4", r"""
**Partie A**

**1. a)** $g'(x) = 3x^2 + \dfrac{4}{x} > 0$ sur $]0;+\infty[$ : $g$ est strictement croissante.

**b)** $\lim\limits_{x \to 0^+} g(x) = -\infty$ et $\lim\limits_{x \to +\infty} g(x) = +\infty$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $g'(x)$ | ‖ | $+$ | |
| $g(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ |

**2. a)** $g$ est continue et strictement croissante : bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\alpha$. $g(1{,}1) \approx -0{,}29 < 0$ et $g(1{,}2) \approx 0{,}46 > 0$, donc $1{,}1 < \alpha < 1{,}2$.

**c)** $g(x) < 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) > 0$ sur $]\alpha;+\infty[$.

**Partie B**

**1. a)** En $0^+$ : $\ln x \to -\infty$ et $\dfrac{1}{x^2} \to +\infty$, donc $-\dfrac{2\ln x}{x^2} \to +\infty$ et $\lim\limits_{x \to 0^+} f(x) = +\infty$. La droite $x = 0$ est **asymptote verticale**.

**b)** $\dfrac{\ln x}{x^2} = \dfrac{1}{x} \times \dfrac{\ln x}{x} \to 0$ en $+\infty$. Donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - (x - 1)\big) = 0$.

$\Delta : y = x - 1$ est **asymptote oblique** en $+\infty$.

**c)** $f(x) - (x - 1) = -\dfrac{2\ln x}{x^2}$ a le signe de $-\ln x$ : $(C)$ est au-dessus de $\Delta$ sur $]0;1[$, au-dessous sur $]1;+\infty[$, et elles se coupent en $(1;0)$.

**2. a)** $f'(x) = 1 - 2\,\dfrac{\frac{1}{x} \cdot x^2 - 2x\ln x}{x^4} = 1 - \dfrac{2(1 - 2\ln x)}{x^3} = \dfrac{x^3 - 2 + 4\ln x}{x^3} = \dfrac{g(x)}{x^3}$.

**b)** $g(\alpha) = 0$ donne $\ln\alpha = \dfrac{2 - \alpha^3}{4}$, donc
$$f(\alpha) = \alpha - 1 - \dfrac{2 - \alpha^3}{2\alpha^2} = \dfrac{2\alpha^3 - 2\alpha^2 - 2 + \alpha^3}{2\alpha^2} = \dfrac{3\alpha^3 - 2\alpha^2 - 2}{2\alpha^2}.$$

(Numériquement, $f(\alpha) \approx -0{,}06$.)

**c)** $f'(x)$ a le signe de $g(x)$ :

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**3. a)** $f(1) = 0$ et $f'(1) = g(1) = -1$ : $T : y = -(x - 1)$, soit $y = -x + 1$.

Les coefficients directeurs de $T$ et de $\Delta$ sont $-1$ et $1$, de produit $-1$ : dans un repère orthonormé, $T$ est **perpendiculaire** à $\Delta$.

**b)** $f(1) = 0$ avec $1 < \alpha$, et $f$ décroissante sur $]0;\alpha]$, donc $f(\alpha) < 0$. Sur $[\alpha;+\infty[$, $f$ est continue et strictement croissante de $f(\alpha) < 0$ à $+\infty$ : elle s'annule une seule fois, en $\beta$.

$f(1{,}3) \approx -0{,}010 < 0$ et $f(1{,}4) \approx 0{,}057 > 0$, donc $1{,}3 < \beta < 1{,}4$ ($\beta \approx 1{,}318$).

**c)** On trace l'asymptote $x = 0$, l'asymptote $\Delta$, la tangente $T$ en $A(1;0)$, le minimum $(\alpha;f(\alpha))$ et le point $B(\beta;0)$.

**d)** Pour $x > 0$, en divisant par $x^2$ :
$$2x^3 - (m + 1)x^2 - 2\ln x = 0 \iff 2x - m - 1 - \dfrac{2\ln x}{x^2} = 0 \iff f(x) = -x + m.$$

On cherche les points communs à $(C)$ et à la droite $D_m : y = -x + m$, parallèle à $T$.

Posons $k(x) = f(x) + x = 2x - 1 - \dfrac{2\ln x}{x^2}$ : $k'(x) = \dfrac{2x^3 - 2 + 4\ln x}{x^3}$. Le numérateur est strictement croissant et s'annule en $1$. Donc $k$ décroît sur $]0;1]$, croît sur $[1;+\infty[$, avec $k(1) = 1$ et $k \to +\infty$ aux deux bornes. Ainsi :
- si $m < 1$ : **aucune solution** ;
- si $m = 1$ : **une solution**, $x = 1$ ($D_1 = T$) ;
- si $m > 1$ : **deux solutions**.

**4) a)** Sur $[1;\beta]$, $f(x) \le 0$ ($f(1) = f(\beta) = 0$ et $f$ négative entre les deux), donc $S = -\displaystyle\int_1^\beta f(x)\,dx$.

**b)** Par parties, avec $u = \ln x$ et $v' = \dfrac{1}{x^2}$ ($u' = \dfrac{1}{x}$, $v = -\dfrac{1}{x}$) :
$$I = \left[-\dfrac{\ln x}{x}\right]_1^\beta + \int_1^\beta \dfrac{dx}{x^2} = -\dfrac{\ln\beta}{\beta} - \dfrac{1}{\beta} + 1.$$

$$S = -\left[\dfrac{x^2}{2} - x\right]_1^\beta + 2I = -\dfrac{\beta^2}{2} + \beta - \dfrac{1}{2} + 2 - \dfrac{2}{\beta} - \dfrac{2\ln\beta}{\beta}.$$

Comme $f(\beta) = 0$, $\dfrac{2\ln\beta}{\beta} = \beta(\beta - 1)$, d'où
$$S = -\dfrac{3}{2}\beta^2 + 2\beta + \dfrac{3}{2} - \dfrac{2}{\beta} \text{ u.a.} \approx 0{,}013 \text{ u.a.}$$
""")

_add("bac-d-2016-sc-math-ex3", r"""
**1. a)** $\lim\limits_{x \to -\infty} xe^x = 0$ et $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $\lim\limits_{x \to -\infty}\big(f(x) - (x - 1)\big) = \lim\limits_{x \to -\infty}(x - 1)e^x = 0$.

La droite $y = x - 1$ est **asymptote oblique** à $(C)$ en $-\infty$.

**b)** $f(x) = (x - 1)(e^x + 1)$, produit de deux facteurs qui tendent vers $+\infty$ : $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**c)** $\dfrac{f(x)}{x} = \left(1 - \dfrac{1}{x}\right)(e^x + 1) \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**2. a)** $f'(x) = e^x + xe^x - e^x + 1 = xe^x + 1$ et $f''(x) = e^x + xe^x = (x + 1)e^x$.

**b)** $f'(-1) = -e^{-1} + 1 = 1 - \dfrac{1}{e} > 0$.

**c)** $f''(x)$ a le signe de $x + 1$ : $f'$ décroît sur $]-\infty;-1]$ et croît sur $[-1;+\infty[$. Son minimum est $f'(-1) = 1 - \dfrac{1}{e} > 0$, donc $f'(x) > 0$ pour tout $x$.

**3.** $f$ est strictement croissante sur $\mathbb{R}$ :

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $+\infty$ |

**4.** $f(0) = -2$ : point $(0;-2)$. $f(x) = 0 \iff x = 1$ (car $e^x + 1 > 0$) : point $(1;0)$.

On trace l'asymptote $y = x - 1$ en $-\infty$, ces deux points et la branche parabolique verticale.

**5. a)** $f'(x) - e^x + x - 2 = xe^x + 1 - e^x + x - 2 = xe^x - e^x + x - 1 = f(x)$.

Une primitive de $f$ est donc $F(x) = f(x) - e^x + \dfrac{x^2}{2} - 2x$, soit
$$F(x) = (x - 2)e^x + \dfrac{x^2}{2} - x - 1.$$

**b)** Le domaine est compris entre $x = 0$ et $x = 1$, où $f(x) \le 0$ :
$$S = -\int_0^1 f(x)\,dx = -\big(F(1) - F(0)\big) = -\left(-e - \dfrac{3}{2} + 3\right) = e - \dfrac{3}{2} \approx 1{,}22 \text{ cm}^2.$$
""")

_add("bac-d-2016-sc-math-ex4", r"""
**1. a)** $\lim\limits_{x \to 0^+} f(x) = +\infty$ (car $-\ln x \to +\infty$) : la droite $x = 0$ est asymptote verticale. $f(x) = x\left(1 - \dfrac{2}{x} - \dfrac{\ln x}{x}\right)$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $\dfrac{f(x)}{x} \to 1$ et $f(x) - x = -2 - \ln x \to -\infty$ : $(C)$ a en $+\infty$ une **branche parabolique de direction la droite $y = x$**.

**2.** $f'(x) = 1 - \dfrac{1}{x} = \dfrac{x - 1}{x}$. $f(1) = -1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $-1$ | ↗ | $+\infty$ |

**3.** $f(e) = e - 3$ et $f'(e) = 1 - \dfrac{1}{e}$ :
$$T : y = \left(1 - \dfrac{1}{e}\right)(x - e) + e - 3 = \left(1 - \dfrac{1}{e}\right)x - 2.$$

**4. a)** Sur $]0;1]$, $f$ décroît strictement de $+\infty$ à $-1$ : une seule solution $\alpha$. Sur $[1;+\infty[$, $f$ croît strictement de $-1$ à $+\infty$ : une seule solution $\beta$.

$f(0{,}1) \approx 0{,}40 > 0$ et $f(0{,}2) \approx -0{,}19 < 0$, donc $0{,}1 < \alpha < 0{,}2$. $f(3{,}1) \approx -0{,}03 < 0$ et $f(3{,}2) \approx 0{,}04 > 0$, donc $3{,}1 < \beta < 3{,}2$.

$f(x) = 0 \iff x - 2 = \ln x \iff e^{x-2} = x \iff e^x = e^2x$. Donc
$$\dfrac{e^\alpha}{e^\beta} = \dfrac{e^2\alpha}{e^2\beta} = \dfrac{\alpha}{\beta}.$$

**b)** $f(x) > 0$ sur $]0;\alpha[ \cup ]\beta;+\infty[$, $f(x) < 0$ sur $]\alpha;\beta[$, et $f(\alpha) = f(\beta) = 0$.

**5. a)** Sur $I = [1;+\infty[$, $g$ est continue et strictement croissante : bijection de $I$ sur $J = [-1;+\infty[$.

**b)** $g(e) = e - 3$ et $g'(e) = 1 - \dfrac{1}{e} \neq 0$, donc
$$\left(g^{-1}\right)'(e - 3) = \dfrac{1}{g'(e)} = \dfrac{1}{1 - \frac{1}{e}} = \dfrac{e}{e - 1}.$$

**6.** $(C)$ : asymptote $x = 0$, minimum $(1;-1)$, points $(\alpha;0)$ et $(\beta;0)$, tangente $T$ en $A(e;e - 3)$. $(C')$ est la symétrique de la partie de $(C)$ d'abscisses $x \ge 1$ par rapport à $y = x$ : elle part de $(-1;1)$ avec une tangente horizontale.

**7. a)** Par parties, avec $u = \ln x$ et $v' = 1$ : $\displaystyle\int_1^e \ln x\,dx = \big[x\ln x\big]_1^e - \int_1^e dx = e - (e - 1) = 1$.

**b)** Sur $[1;e]$, $f(x) < 0$ (car $1 \le x \le e < \beta$). L'aire vaut
$$-\int_1^e f(x)\,dx = -\left(\left[\dfrac{x^2}{2} - 2x\right]_1^e - 1\right) = -\left(\dfrac{e^2}{2} - 2e + \dfrac{3}{2} - 1\right) = 2e - \dfrac{e^2}{2} - \dfrac{1}{2} \text{ u.a.} \approx 1{,}24 \text{ u.a.}$$
""")

# ═══════════════════════════════════ 2017 ═════════════════════════════════════

_add("bac-d-2017-sn-math-ex3", r"""
**1° a)** $\lim\limits_{x \to +\infty} e^{-x} = 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - (2x - 2)\big) = 0$.

La droite $y = 2x - 2$ est **asymptote oblique** à $(C)$ en $+\infty$, et $(C)$ est au-dessus ($e^{-x} > 0$).

**b)** En $-\infty$ : $e^{-x} \to +\infty$ l'emporte, et $f(x) = e^{-x}\left(1 + (2x - 2)e^x\right)$ avec $(2x - 2)e^x \to 0$, donc $\lim\limits_{x \to -\infty} f(x) = +\infty$.

$\dfrac{f(x)}{x} = \dfrac{e^{-x}}{x} + 2 - \dfrac{2}{x} \to -\infty$ (car $\dfrac{e^{-x}}{x} \to -\infty$) : **branche parabolique de direction $(Oy)$** en $-\infty$.

**2° a)** $f'(x) = -e^{-x} + 2$, et $f'(-\ln 2) = -e^{\ln 2} + 2 = 0$.

**b)** $f'(x) > 0 \iff e^{-x} < 2 \iff -x < \ln 2 \iff x > -\ln 2$. $f(-\ln 2) = 2 - 2\ln 2 - 2 = -2\ln 2 \approx -1{,}39$.

| $x$ | $-\infty$ | | $-\ln 2$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $-2\ln 2$ | ↗ | $+\infty$ |

**3° a)** Sur $]-\infty;-\ln 2]$, $f$ est continue, strictement décroissante de $+\infty$ à $-2\ln 2 < 0$ : une seule solution $\alpha$. Sur $[-\ln 2;+\infty[$, elle est strictement croissante de $-2\ln 2$ à $+\infty$ : une seule solution $\beta$.

$f(-1{,}7) = e^{1{,}7} - 5{,}4 \approx 0{,}07 > 0$ et $f(-1{,}6) = e^{1{,}6} - 5{,}2 \approx -0{,}25 < 0$, donc $-1{,}7 < \alpha < -1{,}6$.

$f(0{,}7) = e^{-0{,}7} - 0{,}6 \approx -0{,}10 < 0$ et $f(0{,}8) = e^{-0{,}8} - 0{,}4 \approx 0{,}05 > 0$, donc $0{,}7 < \beta < 0{,}8$.

**b)** On trace l'asymptote $y = 2x - 2$, le minimum $(-\ln 2;-2\ln 2) \approx (-0{,}69;-1{,}39)$, les points $(\alpha;0)$, $(\beta;0)$ et $(0;-1)$, et la branche parabolique verticale en $-\infty$.

**4° a)** $\dfrac{u_{n+1}}{u_n} = e^{-1}$ : $(u_n)$ est géométrique de raison $e^{-1}$ et de premier terme $u_0 = 1 > 0$. Comme $0 < e^{-1} < 1$, elle est **décroissante**.

**b)** $v_{n+1} - v_n = 2$ : $(v_n)$ est arithmétique de raison $2 > 0$, donc **croissante**.

**c)** Non : $\lim\limits_{n \to +\infty} u_n = 0$ et $\lim\limits_{n \to +\infty} v_n = +\infty$, donc $v_n - u_n$ ne tend pas vers $0$.

**5° a)** $f(k) = u_k + v_k$, donc
$$S_n = \sum_{k=0}^{n} e^{-k} + \sum_{k=0}^{n}(2k - 2) = \dfrac{1 - e^{-(n+1)}}{1 - e^{-1}} + (n + 1)(n - 2).$$

**b)** Le premier terme tend vers $\dfrac{1}{1 - e^{-1}} = \dfrac{e}{e - 1}$ et le second vers $+\infty$ : $\lim\limits_{n \to +\infty} S_n = +\infty$.

$\dfrac{(n + 1)(n - 2)}{n^2} \to 1$ et le premier terme divisé par $n^2$ tend vers $0$, donc $\lim\limits_{n \to +\infty} \dfrac{S_n}{n^2} = 1$.
""")

_add("bac-d-2017-sn-math-ex4", r"""
**1° a)** $g(x) = \dfrac{1 - x\ln x}{x} + 1$ et $x\ln x \to 0$ en $0^+$, donc $\lim\limits_{x \to 0^+} g(x) = +\infty$. En $+\infty$ : $\lim\limits_{x \to +\infty} g(x) = -\infty$.

**b)** $g'(x) = -\dfrac{1}{x^2} - \dfrac{1}{x} < 0$ : $g$ est strictement décroissante sur $]0;+\infty[$, de $+\infty$ à $-\infty$.

**c)** $g$ est continue et strictement décroissante : elle réalise une bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**d)** $0 \in J$ : une unique solution $\alpha$. $g(3{,}5) \approx 0{,}033 > 0$ et $g(3{,}6) \approx -0{,}003 < 0$, donc $3{,}5 < \alpha < 3{,}6$ ($\alpha \approx 3{,}591$).

$g(x) > 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) < 0$ sur $]\alpha;+\infty[$.

**2° a)** En $0^+$ : $2 - 2x \to 2$ et $\ln x - 2 \to -\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**.

En $+\infty$ : $2 - 2x \to -\infty$ et $\ln x - 2 \to +\infty$, donc $\lim\limits_{x \to +\infty} f(x) = -\infty$.

$\dfrac{f(x)}{x} = \left(\dfrac{2}{x} - 2\right)(\ln x - 2) \to -\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** $f'(x) = -2(\ln x - 2) + (2 - 2x) \times \dfrac{1}{x} = -2\ln x + 4 + \dfrac{2}{x} - 2 = 2\left(\dfrac{1}{x} + 1 - \ln x\right) = 2g(x)$.

**c)** $f'(x)$ a le signe de $g(x)$ :

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $f(\alpha)$ | ↘ | $-\infty$ |

**3° a)** $g(\alpha) = 0$ donne $\ln\alpha = \dfrac{1}{\alpha} + 1$, donc $\ln\alpha - 2 = \dfrac{1}{\alpha} - 1 = \dfrac{1 - \alpha}{\alpha}$ et
$$f(\alpha) = 2(1 - \alpha) \times \dfrac{1 - \alpha}{\alpha} = \dfrac{2(1 - \alpha)^2}{\alpha}.$$

(Avec $\alpha \approx 3{,}59$ : $f(\alpha) \approx 3{,}74$.)

**b)** $f(1) = 0$ et $f'(1) = 2g(1) = 4$ : $T : y = 4(x - 1) = 4x - 4$.

**c)** $f(x) = 0 \iff x = 1$ ou $\ln x = 2 \iff x = 1$ ou $x = e^2$. Donc $x_B = e^2 \approx 7{,}389$, et $7{,}38 < x_B < 7{,}39$.

**4° a)** **Attention, le sujet contient une erreur :** il demande de prendre $\alpha = 1{,}8$ et $f(\alpha) = 2{,}7$. Ces valeurs contredisent la question 1° d) ($3{,}5 < \alpha < 3{,}6$). Pour le tracé, on utilise les vraies valeurs : $\alpha \approx 3{,}59$ et $f(\alpha) \approx 3{,}74$.

On trace l'asymptote $x = 0$, le maximum $(\alpha;f(\alpha)) \approx (3{,}59;3{,}74)$, les points $A(1;0)$ et $B(e^2;0)$, et la tangente $T$ en $A$.

**b)** $f(x) - 4(x - 1) = (2 - 2x)\ln x - 2(2 - 2x) - 4x + 4 = (2 - 2x)\ln x$, donc
$$(2 - 2x)\ln x = m \iff f(x) = 4x - 4 + m.$$

On cherche les points communs à $\Gamma$ et à la droite $D_m : y = 4x - 4 + m$, parallèle à $T$.

Posons $k(x) = (2 - 2x)\ln x$. Alors $k'(x) = -2\ln x + \dfrac{2}{x} - 2$ et $k''(x) = -\dfrac{2}{x} - \dfrac{2}{x^2} < 0$. Donc $k'$ est décroissante et s'annule en $1$ : $k$ croît sur $]0;1]$, décroît sur $[1;+\infty[$, avec $k(1) = 0$ et $k \to -\infty$ aux deux bornes. Ainsi :
- si $m > 0$ : **aucune solution** ;
- si $m = 0$ : **une solution**, $x = 1$ ($D_0 = T$) ;
- si $m < 0$ : **deux solutions**.

**5° a)** Par parties, avec $u = \ln x$ et $v' = 2 - 2x$ ($u' = \dfrac{1}{x}$, $v = 2x - x^2$) :
$$\int_1^2 (2 - 2x)\ln x\,dx = \big[(2x - x^2)\ln x\big]_1^2 - \int_1^2 (2 - x)\,dx = 0 - \left[2x - \dfrac{x^2}{2}\right]_1^2 = -\left(2 - \dfrac{3}{2}\right) = -\dfrac{1}{2}.$$

**b)** Sur $[1;2]$, $2 - 2x \le 0$ et $\ln x - 2 < 0$, donc $f(x) \ge 0$. L'aire vaut
$$\int_1^2 f(x)\,dx = \int_1^2 (2 - 2x)\ln x\,dx - 2\int_1^2 (2 - 2x)\,dx = -\dfrac{1}{2} - 2\big[2x - x^2\big]_1^2 = -\dfrac{1}{2} + 2 = \dfrac{3}{2} \text{ u.a.}$$
""", note="Question 4° a) : le sujet impose α = 1,8 et f(α) = 2,7, valeurs fausses (α ≈ 3,59, f(α) ≈ 3,74) ; la correction le signale et utilise les vraies valeurs.")

_add("bac-d-2017-sc-math-ex3", r"""
**1° a)** En $-\infty$ : $x + 2 \to -\infty$ et $1 + e^{-x} \to +\infty$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$.

$\dfrac{f(x)}{x} = \left(1 + \dfrac{2}{x}\right)(1 + e^{-x}) \to +\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**b)** $f(x) = (x + 2) + (x + 2)e^{-x} = x + 2 + \dfrac{x}{e^x} + \dfrac{2}{e^x}$.

En $+\infty$ : $\dfrac{x}{e^x} \to 0$ et $\dfrac{2}{e^x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - (x + 2)\big) = 0$.

**c)** La droite $D : y = x + 2$ est **asymptote oblique** à $\Gamma$ en $+\infty$.

**d)** $f(x) - (x + 2) = (x + 2)e^{-x}$ a le signe de $x + 2$ : $\Gamma$ est au-dessous de $D$ sur $]-\infty;-2[$, au-dessus sur $]-2;+\infty[$, et elles se coupent en $(-2;0)$.

**2° a)** $f'(x) = 1 + e^{-x} - (x + 2)e^{-x} = 1 - (x + 1)e^{-x}$.

**b)** $f''(x) = -e^{-x} + (x + 1)e^{-x} = xe^{-x}$, du signe de $x$ : $f'$ décroît sur $]-\infty;0]$ et croît sur $[0;+\infty[$. Son minimum est $f'(0) = 0$.

Donc $f'(x) \ge 0$ pour tout $x$, avec égalité seulement en $x = 0$.

**c)** $f$ est strictement croissante sur $\mathbb{R}$ :

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $4$ | ↗ | $+\infty$ |

**3° a)** Tangente parallèle à $D$ $\iff f'(x) = 1 \iff (x + 1)e^{-x} = 0 \iff x = -1$.

$f(-1) = 1 \times (1 + e) = 1 + e$, donc $A(-1;1 + e)$ et $T : y = (x + 1) + 1 + e$, soit $T : y = x + 2 + e$.

**b)** $f(0) = 4$ : point $(0;4)$. $f(x) = 0 \iff x = -2$ : point $(-2;0)$.

**c)** On trace $D$, $T$ (parallèle à $D$, au-dessus), $A(-1;1 + e) \approx (-1;3{,}72)$, les points $(-2;0)$ et $(0;4)$. En $(0;4)$, $f''$ s'annule en changeant de signe : c'est un point d'inflexion, où la tangente est horizontale ($f'(0) = 0$).

**4° a)** $I = \displaystyle\int_{-2}^{0} 2e^{-x}\,dx = \big[-2e^{-x}\big]_{-2}^{0} = -2 + 2e^2 = 2e^2 - 2$.

**b)** Par parties, avec $u = x$ et $v' = e^{-x}$ ($v = -e^{-x}$) :
$$J = \big[-xe^{-x}\big]_{-2}^{0} + \int_{-2}^{0} e^{-x}\,dx = (0 - 2e^2) + \big[-e^{-x}\big]_{-2}^{0} = -2e^2 + (-1 + e^2) = -e^2 - 1.$$

**c)** Sur $[-2;0]$, $\Gamma$ est au-dessus de $D$, donc l'aire vaut
$$\int_{-2}^{0}\big(f(x) - (x + 2)\big)\,dx = \int_{-2}^{0}(xe^{-x} + 2e^{-x})\,dx = J + I = e^2 - 3 \text{ u.a.} \approx 4{,}39 \text{ u.a.}$$

**5°** $x + 2 = (m - 2)e^x \iff (x + 2)e^{-x} = m - 2 \iff f(x) - (x + 2) = m - 2 \iff f(x) = x + m$.

On cherche les points communs à $\Gamma$ et à la droite $D_m : y = x + m$, parallèle à $D$.

$h(x) = (x + 2)e^{-x}$ a pour dérivée $-(x + 1)e^{-x}$ : elle croît de $-\infty$ jusqu'à $h(-1) = e$, puis décroît vers $0$ (sans l'atteindre). L'équation $h(x) = m - 2$ a :
- **aucune solution** si $m > 2 + e$ ($D_m$ au-dessus de $T$) ;
- **une solution** ($x = -1$) si $m = 2 + e$ ($D_m = T$) ;
- **deux solutions** si $2 < m < 2 + e$ ;
- **une solution** si $m \le 2$.
""")

_add("bac-d-2017-sc-math-ex4", r"""
**1° a)** $\lim\limits_{x \to 0^+} x\ln x = 0$, donc $\lim\limits_{x \to 0^+} u(x) = 1$ ; et $\lim\limits_{x \to +\infty} u(x) = +\infty$.

**b)** $u'(x) = \ln x + 1$, qui s'annule pour $x = \dfrac{1}{e}$ (négative avant, positive après). $u\left(\dfrac{1}{e}\right) = 1 - \dfrac{1}{e}$.

| $x$ | $0$ | | $\frac{1}{e}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $u'(x)$ | | $-$ | $0$ | $+$ | |
| $u(x)$ | $1$ | ↘ | $1 - \frac{1}{e}$ | ↗ | $+\infty$ |

**c)** Le minimum de $u$ est $1 - \dfrac{1}{e}$, donc $u(x) \ge 1 - \dfrac{1}{e} > 0$ : $u(x) > 0$ pour tout $x > 0$.

**2° a)** En $0^+$ : $2x - 1 + \ln x \to -\infty$ et $x - 1 \to -1$, donc $\lim\limits_{x \to 0^+} f(x) = +\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** En $1$ : le numérateur tend vers $1$, et $x - 1 \to 0^-$ (à gauche) ou $0^+$ (à droite). Donc $\lim\limits_{x \to 1^-} f(x) = -\infty$ et $\lim\limits_{x \to 1^+} f(x) = +\infty$ : la droite $x = 1$ est **asymptote verticale**.

**3° a)** $\dfrac{2x - 1 + \ln x}{x - 1} = \dfrac{2(x - 1) + 1 + \ln x}{x - 1} = 2 + \dfrac{1}{x - 1} + \dfrac{\ln x}{x - 1}$.

**b)** En $+\infty$ : $\dfrac{1}{x - 1} \to 0$ et $\dfrac{\ln x}{x - 1} = \dfrac{\ln x}{x} \times \dfrac{x}{x - 1} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = 2$ : $(\Delta) : y = 2$ est **asymptote horizontale** en $+\infty$.

**c)** $f(x) - 2 = \dfrac{1 + \ln x}{x - 1}$. Le numérateur s'annule en $\dfrac{1}{e}$, le dénominateur en $1$.

| $x$ | $0$ | | $\frac{1}{e}$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $1 + \ln x$ | | $-$ | $0$ | $+$ | | $+$ | |
| $x - 1$ | | $-$ | | $-$ | ‖ | $+$ | |
| $f(x) - 2$ | | $+$ | $0$ | $-$ | ‖ | $+$ | |

$(C)$ est au-dessus de $(\Delta)$ sur $\left]0;\dfrac{1}{e}\right[ \cup ]1;+\infty[$ et au-dessous sur $\left]\dfrac{1}{e};1\right[$ ; elles se coupent en $\left(\dfrac{1}{e};2\right)$.

**4° a)**
$$f'(x) = \dfrac{\left(2 + \frac{1}{x}\right)(x - 1) - (2x - 1 + \ln x)}{(x - 1)^2} = \dfrac{-\frac{1}{x} - \ln x}{(x - 1)^2} = \dfrac{-(1 + x\ln x)}{x(x - 1)^2} = \dfrac{-u(x)}{x(x - 1)^2}.$$

**b)** $u(x) > 0$, donc $f'(x) < 0$ sur $D_f$ :

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | ‖ | $-$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $-\infty$ ‖ $+\infty$ | ↘ | $2$ |

**5° a)** Sur $]0;1[$, $g$ est continue et strictement décroissante de $+\infty$ à $-\infty$ : bijection de $]0;1[$ sur $I = \mathbb{R}$.

**b)** $g^{-1}$ est définie sur $\mathbb{R}$, strictement décroissante, à valeurs dans $]0;1[$ :

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $g^{-1}(x)$ | $1$ | ↘ | $0$ |

**6° a)** Sur $]1;+\infty[$, $f(x) > 2 > 0$ : pas de point d'intersection. Sur $]0;1[$, $g$ est une bijection sur $\mathbb{R}$ : elle s'annule une seule fois, en $\alpha$.

$f(0{,}6) \approx 0{,}78 > 0$ et $f(0{,}8) \approx -1{,}88 < 0$, donc $0{,}6 < \alpha < 0{,}8$ ($\alpha \approx 0{,}687$, solution de $2x - 1 + \ln x = 0$).

**b)** On trace les asymptotes $x = 0$, $x = 1$ et $(\Delta) : y = 2$, le point $\left(\dfrac{1}{e};2\right)$ et le point $A(\alpha;0)$.

$(C')$ est la symétrique de la branche de $(C)$ sur $]0;1[$ par rapport à $y = x$ : elle a les asymptotes horizontales $y = 0$ (en $+\infty$) et $y = 1$ (en $-\infty$).
""")

# ═══════════════════════════════════ 2018 ═════════════════════════════════════

_add("bac-d-2018-sn-math-ex4", r"""
**1° a)** En $0^+$ : $x\ln x \to 0$, donc le numérateur $2 + x + x\ln x \to 2$ et le dénominateur $x \to 0^+$ : $\lim\limits_{x \to 0^+} f(x) = +\infty$. La droite $x = 0$ est **asymptote verticale**.

**b)** $f(x) = \dfrac{2}{x} + \dfrac{x}{x} + \dfrac{x\ln x}{x} = \dfrac{2}{x} + 1 + \ln x$.

**c)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \dfrac{2}{x^2} + \dfrac{1}{x} + \dfrac{\ln x}{x} \to 0$ : **branche parabolique de direction $(Ox)$** en $+\infty$.

**2° a)** $f'(x) = -\dfrac{2}{x^2} + \dfrac{1}{x} = \dfrac{x - 2}{x^2}$. $f(2) = 2 + \ln 2 \approx 2{,}69$.

| $x$ | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $2 + \ln 2$ | ↗ | $+\infty$ |

**b)** $f(1) = 3$ et $f'(1) = -1$ : $T : y = -(x - 1) + 3$, soit $T : y = -x + 4$.

**3° a)** Sur $I = ]0;2]$, $g$ est continue et strictement décroissante : bijection de $I$ sur $J = [2 + \ln 2;+\infty[$.

**b)** $g^{-1}$ est définie sur $J$, strictement décroissante, de $g^{-1}(2 + \ln 2) = 2$ vers $0$ en $+\infty$.

| $x$ | $2 + \ln 2$ | | $+\infty$ |
|---|---|---|---|
| $g^{-1}(x)$ | $2$ | ↘ | $0$ |

**c)** $g(1) = 3$ et $g'(1) = -1 \neq 0$, donc $\left(g^{-1}\right)'(3) = \dfrac{1}{g'(1)} = -1$.

**d)** $(C)$ : asymptote $x = 0$, minimum $(2;2 + \ln 2)$, tangente $T$ en $(1;3)$. $(C')$ est la symétrique de la partie de $(C)$ sur $]0;2]$ par rapport à $y = x$ : elle part de $(2 + \ln 2;2)$ avec une tangente verticale et a l'asymptote $y = 0$.

**4° a)** $h(x) = \dfrac{2}{x} + 1 + \ln x - x$, donc
$$h'(x) = -\dfrac{2}{x^2} + \dfrac{1}{x} - 1 = -\dfrac{x^2 - x + 2}{x^2} < 0,$$
car $x^2 - x + 2$ a un discriminant négatif ($1 - 8 < 0$). $\lim\limits_{x \to 0^+} h(x) = +\infty$ et $\lim\limits_{x \to +\infty} h(x) = -\infty$ (car $\ln x - x \to -\infty$).

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $h'(x)$ | ‖ | $-$ | |
| $h(x)$ | ‖ $+\infty$ | ↘ | $-\infty$ |

**b)** $h$ est continue et strictement décroissante de $+\infty$ à $-\infty$ : une unique solution $\alpha$. $h(2) = \ln 2 > 0$ et $h(3) = \dfrac{2}{3} - 2 + \ln 3 \approx -0{,}23 < 0$, donc $2 < \alpha < 3$ ($\alpha \approx 2{,}74$).

$h(\alpha) = 0$ signifie $f(\alpha) - \alpha = 0$, soit $f(\alpha) = \alpha$. Comme $h$ est décroissante, pour $x \ge \alpha$ : $h(x) \le h(\alpha) = 0$, soit $f(x) - x \le 0$.

**5° a)** $u_0 = 3 \ge \alpha$. Si $u_n \ge \alpha$, alors, comme $f$ est croissante sur $[2;+\infty[$ et $\alpha > 2$ : $u_{n+1} = f(u_n) \ge f(\alpha) = \alpha$. Par récurrence, $u_n \ge \alpha$ pour tout $n$.

**b)** $u_{n+1} - u_n = f(u_n) - u_n \le 0$ (d'après 4° b, car $u_n \ge \alpha$) : $(u_n)$ est **décroissante**. Elle est décroissante et minorée par $\alpha$, donc **convergente**.

**6° a)** Par parties, avec $u = \ln x$ et $v' = 1$ : $K = \big[x\ln x\big]_1^e - \displaystyle\int_1^e dx = e - (e - 1) = 1$.

**b)** $f(x) \ge 2 + \ln 2 > 0$, donc l'aire vaut
$$\int_1^e \left(\dfrac{2}{x} + 1 + \ln x\right)dx = 2\big[\ln x\big]_1^e + (e - 1) + K = 2 + e - 1 + 1 = e + 2 \text{ u.a.} \approx 4{,}72 \text{ u.a.}$$
""")

_add("bac-d-2018-sn-math-ex3", r"""
**1° a)** En $-\infty$ : $2xe^{-x} \to -\infty$ ($x \to -\infty$, $e^{-x} \to +\infty$), donc $\lim\limits_{x \to -\infty} f(x) = -\infty$. En $+\infty$ : $2xe^{-x} = \dfrac{2x}{e^x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $\dfrac{f(x)}{x} = 2 - \dfrac{1}{x} + 2e^{-x} \to +\infty$ en $-\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**c)** $f(x) - (2x - 1) = 2xe^{-x} \to 0$ en $+\infty$ : $D : y = 2x - 1$ est **asymptote oblique** en $+\infty$.

$2xe^{-x}$ a le signe de $x$ : $(C)$ est au-dessous de $D$ pour $x < 0$, au-dessus pour $x > 0$, et elles se coupent en $(0;-1)$.

**2° a)** $f'(x) = 2 + 2e^{-x} - 2xe^{-x} = 2 + (2 - 2x)e^{-x}$ et
$$f''(x) = -2e^{-x} - (2 - 2x)e^{-x} = (2x - 4)e^{-x}.$$

**b)** $f''$ s'annule en $2$ en changeant de signe : $A(2;f(2)) = \left(2;3 + 4e^{-2}\right) \approx (2;3{,}54)$ est un point d'inflexion.

**c)** $f''(x)$ a le signe de $2x - 4$ : $f'$ décroît sur $]-\infty;2]$ et croît sur $[2;+\infty[$. Son minimum est $f'(2) = 2 - 2e^{-2} > 0$, donc $f'(x) > 0$ pour tout $x$.

**d)** $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**3° a)** $f$ est continue et strictement croissante de $\mathbb{R}$ sur $\mathbb{R}$ : elle s'annule une seule fois, en $\alpha$.

$f(0{,}2) = -0{,}6 + 0{,}4e^{-0{,}2} \approx -0{,}27 < 0$ et $f(0{,}3) = -0{,}4 + 0{,}6e^{-0{,}3} \approx 0{,}04 > 0$, donc $0{,}2 < \alpha < 0{,}3$.

**b)** Tangente parallèle à $D$ $\iff f'(x) = 2 \iff (2 - 2x)e^{-x} = 0 \iff x = 1$.

$B\left(1;1 + \dfrac{2}{e}\right)$ et $T : y = 2(x - 1) + 1 + \dfrac{2}{e}$, soit $T : y = 2x - 1 + \dfrac{2}{e}$.

**c)** On trace $D$, $T$ (parallèle à $D$, au-dessus), $B \approx (1;1{,}74)$, le point d'inflexion $A$, le point $(0;-1)$ et le point $(\alpha;0)$.

**d)** $-m - 1 + 2xe^{-x} = 0 \iff 2xe^{-x} = m + 1 \iff f(x) - (2x - 1) = m + 1 \iff f(x) = 2x + m$.

On cherche les points communs à $(C)$ et à $D_m : y = 2x + m$, parallèle à $D$.

$k(x) = 2xe^{-x}$ a pour dérivée $(2 - 2x)e^{-x}$ : elle croît de $-\infty$ jusqu'à $k(1) = \dfrac{2}{e}$, puis décroît vers $0$ (sans l'atteindre). L'équation $k(x) = m + 1$ a :
- **aucune solution** si $m > \dfrac{2}{e} - 1$ ;
- **une solution** ($x = 1$) si $m = \dfrac{2}{e} - 1$ ($D_m = T$) ;
- **deux solutions** si $-1 < m < \dfrac{2}{e} - 1$ ;
- **une solution** si $m \le -1$.
""")

_add("bac-d-2018-sc-math-ex3", r"""
**1° a)** $f(x) = x\left(1 + \dfrac{2}{x} - \dfrac{e^x}{x}\right)$ avec $\dfrac{e^x}{x} \to +\infty$, donc $\lim\limits_{x \to +\infty} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = -\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $f(x) - (x + 2) = -e^x \to 0$ : la droite $D : y = x + 2$ est **asymptote oblique** à $\Gamma$ en $-\infty$.

**c)** $f(x) - (x + 2) = -e^x < 0$ : $\Gamma$ est toujours **au-dessous** de $D$.

**2° a)** $f'(x) = 1 - e^x$, positive pour $x < 0$ et négative pour $x > 0$. $f(0) = 1$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $-\infty$ | ↗ | $1$ | ↘ | $-\infty$ |

**b)** Sur $]-\infty;0]$, $f$ croît strictement de $-\infty$ à $1$ : une seule solution $\alpha$. Sur $[0;+\infty[$, elle décroît strictement de $1$ à $-\infty$ : une seule solution $\beta$.

$f(-1{,}9) \approx -0{,}05 < 0$ et $f(-1{,}8) \approx 0{,}03 > 0$, donc $-1{,}9 < \alpha < -1{,}8$. $f(1{,}1) \approx 0{,}10 > 0$ et $f(1{,}2) \approx -0{,}12 < 0$, donc $1{,}1 < \beta < 1{,}2$.

**c)** Si $f(x) = 0$, alors $e^x = x + 2$ et $x + f'(x) = x + 1 - e^x = x + 1 - (x + 2) = -1$.

Donc $\alpha + f'(\alpha) = -1 = \beta + f'(\beta)$.

**3° a)** Sur $I = ]-\infty;0]$, $h$ est continue et strictement croissante : c'est une bijection de $I$ sur $]-\infty;1]$, qui admet une réciproque $h^{-1}$.

**b)** $h^{-1}$ est définie sur $]-\infty;1]$, strictement croissante, à valeurs dans $]-\infty;0]$ :

| $x$ | $-\infty$ | | $1$ |
|---|---|---|---|
| $h^{-1}(x)$ | $-\infty$ | ↗ | $0$ |

**c)** $h(\alpha) = 0$ et $h'(\alpha) = 1 - e^\alpha = 1 - (\alpha + 2) = -(1 + \alpha) \neq 0$, donc
$$\left(h^{-1}\right)'(0) = \dfrac{1}{h'(\alpha)} = \dfrac{-1}{1 + \alpha}.$$

**4° a)** $D$ a pour coefficient directeur $1$. Une tangente perpendiculaire à $D$ a pour coefficient directeur $-1$ : $f'(x) = -1 \iff e^x = 2 \iff x = \ln 2$.

$f(\ln 2) = \ln 2 + 2 - 2 = \ln 2$, donc $A(\ln 2;\ln 2)$ et $T : y = -(x - \ln 2) + \ln 2$, soit $T : y = -x + 2\ln 2$.

**b)** $\Gamma$ : asymptote $D$ en $-\infty$, maximum $(0;1)$, points $(\alpha;0)$ et $(\beta;0)$, tangente $T$ en $A \approx (0{,}69;0{,}69)$. $\Gamma'$ est la symétrique de la partie de $\Gamma$ sur $]-\infty;0]$ par rapport à $y = x$ : elle passe par $(0;\alpha)$, finit en $(1;0)$ avec une tangente verticale, et a l'asymptote $y = x - 2$ en $-\infty$.
""")

_add("bac-d-2018-sc-math-ex4", r"""
**Partie A**

**1° a)** $\lim\limits_{x \to 0^+} g(x) = +\infty$ (car $-2\ln x \to +\infty$) et $\lim\limits_{x \to +\infty} g(x) = -\infty$.

**b)** $g'(x) = -1 - \dfrac{2}{x} < 0$ : $g$ est strictement décroissante sur $]0;+\infty[$, de $+\infty$ à $-\infty$.

**2° a)** $g$ est continue et strictement décroissante : bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\lambda$. $g(1{,}8) \approx 0{,}02 > 0$ et $g(1{,}9) \approx -0{,}18 < 0$, donc $1{,}8 \le \lambda \le 1{,}9$.

**c)** $g(x) > 0$ sur $]0;\lambda[$, $g(\lambda) = 0$, et $g(x) < 0$ sur $]\lambda;+\infty[$.

**Partie B**

**1° a)** En $0^+$ : $x - 1 + \ln x \to -\infty$ et $\dfrac{1}{x^2} \to +\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** $f(x) = \dfrac{1}{x} - \dfrac{1}{x^2} + \dfrac{1}{x} \times \dfrac{\ln x}{x} \to 0$ en $+\infty$ : l'axe des abscisses ($y = 0$) est **asymptote horizontale** en $+\infty$.

**2° a)**
$$f'(x) = \dfrac{\left(1 + \frac{1}{x}\right)x^2 - 2x(x - 1 + \ln x)}{x^4} = \dfrac{-x^2 + 3x - 2x\ln x}{x^4} = \dfrac{-x + 3 - 2\ln x}{x^3} = \dfrac{g(x)}{x^3}.$$

**b)** $g(\lambda) = 0$ donne $\ln\lambda = \dfrac{3 - \lambda}{2}$, donc
$$f(\lambda) = \dfrac{\lambda - 1 + \frac{3 - \lambda}{2}}{\lambda^2} = \dfrac{\lambda + 1}{2\lambda^2}.$$

Avec $\lambda \approx 1{,}81$ : $f(\lambda) \approx 0{,}43$, soit $0{,}4$ à $10^{-1}$ près.

**c)** $f'(x)$ a le signe de $g(x)$ :

| $x$ | $0$ | | $\lambda$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $f(\lambda)$ | ↘ | $0$ |

**3° a)** $f(1) = 0$ et $f'(1) = g(1) = 2$ : $T : y = 2(x - 1) = 2x - 2$.

**b)** On trace l'asymptote $x = 0$, l'asymptote $y = 0$, le maximum $(\lambda;f(\lambda)) \approx (1{,}81;0{,}43)$, le point $(1;0)$ et la tangente $T$.

**c)** Pour $x > 0$ : $\ln x = 1 - x + 2x^3 + mx^2 \iff x - 1 + \ln x = 2x^3 + mx^2 \iff f(x) = 2x + m$ (en divisant par $x^2$).

On cherche les points communs à $(C)$ et à $D_m : y = 2x + m$, parallèle à $T$.

Posons $k(x) = f(x) - 2x$ : $k'(x) = \dfrac{g(x) - 2x^3}{x^3} = \dfrac{-2x^3 - x + 3 - 2\ln x}{x^3}$. Le numérateur est strictement décroissant et s'annule en $1$. Donc $k$ croît sur $]0;1]$, décroît sur $[1;+\infty[$, avec $k(1) = -2$ et $k \to -\infty$ aux deux bornes. Ainsi :
- si $m > -2$ : **aucune solution** ;
- si $m = -2$ : **une solution**, $x = 1$ ($D_{-2} = T$) ;
- si $m < -2$ : **deux solutions**.

**4° a)** Par parties, avec $u = \ln x$ et $v' = \dfrac{1}{x^2}$ ($v = -\dfrac{1}{x}$) :
$$J = \left[-\dfrac{\ln x}{x}\right]_1^e + \int_1^e \dfrac{dx}{x^2} = -\dfrac{1}{e} + \left[-\dfrac{1}{x}\right]_1^e = -\dfrac{1}{e} - \dfrac{1}{e} + 1 = 1 - \dfrac{2}{e}.$$

**b)** Sur $[1;e]$, $x - 1 \ge 0$ et $\ln x \ge 0$, donc $f(x) \ge 0$. L'aire vaut
$$\int_1^e \left(\dfrac{1}{x} - \dfrac{1}{x^2}\right)dx + J = \left[\ln x + \dfrac{1}{x}\right]_1^e + 1 - \dfrac{2}{e} = \dfrac{1}{e} + 1 - \dfrac{2}{e} = 1 - \dfrac{1}{e} \text{ u.a.} \approx 0{,}63 \text{ u.a.}$$
""")

# ═══════════════════════════════════ 2019 ═════════════════════════════════════

_add("bac-d-2019-sn-math-ex4", r"""
**1° a)** $\lim\limits_{x \to 0^+} g(x) = +\infty$ (car $\dfrac{1}{x} \to +\infty$ et $-\ln x \to +\infty$) et $\lim\limits_{x \to +\infty} g(x) = -\infty$.

**b)** $g'(x) = -\dfrac{1}{x^2} - \dfrac{1}{x} < 0$ : $g$ est strictement décroissante sur $]0;+\infty[$, de $+\infty$ à $-\infty$.

**c)** $g$ est continue et strictement décroissante de $+\infty$ à $-\infty$ : une unique solution $\alpha$. $g(1{,}7) \approx 0{,}06 > 0$ et $g(1{,}8) \approx -0{,}03 < 0$, donc $1{,}7 < \alpha < 1{,}8$.

**d)** $g(x) > 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) < 0$ sur $]\alpha;+\infty[$.

**2° a)** En $0^+$ : $x - 1 \to -1$ et $1 - \ln x \to +\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**.

En $+\infty$ : $x - 1 \to +\infty$ et $1 - \ln x \to -\infty$, donc $\lim\limits_{x \to +\infty} f(x) = -\infty$.

$\dfrac{f(x)}{x} = \left(1 - \dfrac{1}{x}\right)(1 - \ln x) \to -\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** $f'(x) = (1 - \ln x) + (x - 1) \times \left(-\dfrac{1}{x}\right) = 1 - \ln x - 1 + \dfrac{1}{x} = \dfrac{1}{x} - \ln x = g(x)$.

**c)**

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $f(\alpha)$ | ↘ | $-\infty$ |

**3° a)** $g(\alpha) = 0$ donne $\ln\alpha = \dfrac{1}{\alpha}$, donc $f(\alpha) = (\alpha - 1)\left(1 - \dfrac{1}{\alpha}\right) = \dfrac{(\alpha - 1)^2}{\alpha}$ ($\approx 0{,}33$).

**b)** $f(x) = 0 \iff x = 1$ ou $\ln x = 1 \iff x = 1$ ou $x = e$ : points $(1;0)$ et $(e;0)$.

**4° a)** Sur $I = [\alpha;+\infty[$, $h$ est continue et strictement décroissante, de $f(\alpha)$ à $-\infty$ : bijection de $I$ sur $J = ]-\infty;f(\alpha)]$.

**b)** $e > \alpha$ et $h(e) = 0$, avec $h'(e) = g(e) = \dfrac{1}{e} - 1 \neq 0$, donc
$$\left(h^{-1}\right)'(0) = \dfrac{1}{h'(e)} = \dfrac{1}{\frac{1}{e} - 1} = \dfrac{e}{1 - e} \approx -1{,}58.$$

**c)** $\Gamma$ : asymptote $x = 0$, maximum $(\alpha;f(\alpha)) \approx (1{,}76;0{,}33)$, points $(1;0)$ et $(e;0)$. $\Gamma'$ est la symétrique de la partie de $\Gamma$ sur $[\alpha;+\infty[$ par rapport à $y = x$ : elle part de $(f(\alpha);\alpha)$ avec une tangente verticale et passe par $(0;e)$.

**5° a)** Par parties, avec $u = \ln x$ et $v' = x - 1$ ($u' = \dfrac{1}{x}$, $v = \dfrac{x^2}{2} - x$) :
$$\int_1^e (x - 1)\ln x\,dx = \left[\left(\dfrac{x^2}{2} - x\right)\ln x\right]_1^e - \int_1^e \left(\dfrac{x}{2} - 1\right)dx = \dfrac{e^2}{2} - e - \left[\dfrac{x^2}{4} - x\right]_1^e = \dfrac{e^2 - 3}{4}.$$

**b)** Sur $[1;e]$, $x - 1 \ge 0$ et $1 - \ln x \ge 0$, donc $f(x) \ge 0$. L'aire vaut
$$\int_1^e (x - 1)\,dx - \int_1^e (x - 1)\ln x\,dx = \left(\dfrac{e^2}{2} - e + \dfrac{1}{2}\right) - \dfrac{e^2 - 3}{4} = \dfrac{e^2 - 4e + 5}{4} \text{ u.a.} \approx 0{,}38 \text{ u.a.}$$
""")

_add("bac-d-2019-sc-math-ex3", r"""
**1° a)** $(x + 1)^2\ln(x + 1) - (x + 1) = (x + 1)\big[(x + 1)\ln(x + 1) - 1\big]$ (mise en facteur de $x + 1$).

**b)** Quand $x \to -1^+$ : $(x + 1)\ln(x + 1) \to 0$, donc $(x + 1)\ln(x + 1) - 1 \to -1$ et $x + 1 \to 0$. D'où
$$\lim\limits_{x \to -1^+} f(x) = 0 \qquad \text{et} \qquad \lim\limits_{x \to -1^+} \dfrac{f(x)}{x + 1} = \lim\limits_{x \to -1^+}\big[(x + 1)\ln(x + 1) - 1\big] = -1.$$

**c)** $\lim\limits_{x \to -1^+} f(x) = 0 = f(-1)$ : $f$ est continue à droite en $-1$.

$\dfrac{f(x) - f(-1)}{x - (-1)} = \dfrac{f(x)}{x + 1} \to -1$ : $f$ est dérivable à droite en $-1$, avec $f'_d(-1) = -1$. La courbe a au point $(-1;0)$ une demi-tangente de coefficient directeur $-1$.

**d)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \dfrac{x + 1}{x}\big[(x + 1)\ln(x + 1) - 1\big] \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**2° a)** $f'(x) = 2(x + 1)\ln(x + 1) + (x + 1)^2 \times \dfrac{1}{x + 1} - 1 = 2(x + 1)\ln(x + 1) + x$.

**b)** Pour $-1 < x < 0$ : $0 < x + 1 < 1$, donc $\ln(x + 1) < 0$ et $2(x + 1)\ln(x + 1) < 0$. De plus $x < 0$, donc $f'(x) < 0$.

Pour $x > 0$ : $\ln(x + 1) > 0$ et $x > 0$, donc $f'(x) > 0$. Et $f'(0) = 0$.

**c)** $f(0) = -1$.

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $0$ | ↘ | $-1$ | ↗ | $+\infty$ |

**3° a)** Sur $[0;+\infty[$, $g$ est continue et strictement croissante : bijection de $[0;+\infty[$ sur $J = [-1;+\infty[$.

**b)** $0 \in J$ : une unique solution $\alpha$. $g(0{,}7) \approx -0{,}17 < 0$ et $g(0{,}8) \approx 0{,}10 > 0$, donc $0{,}7 \le \alpha \le 0{,}8$ ($\alpha \approx 0{,}763$).

**c)** $g(\alpha) = 0$ et $\alpha + 1 \neq 0$, donc $(\alpha + 1)\ln(\alpha + 1) = 1$. Alors $g'(\alpha) = 2 \times 1 + \alpha = \alpha + 2$, et
$$\left(g^{-1}\right)'(0) = \dfrac{1}{g'(\alpha)} = \dfrac{1}{\alpha + 2} \approx 0{,}36.$$

**4°** $(C)$ part de $(-1;0)$ avec une demi-tangente de pente $-1$, descend jusqu'au minimum $(0;-1)$, puis remonte en passant par $(\alpha;0)$.

$(C')$ est la symétrique de la partie de $(C)$ sur $[0;+\infty[$ par rapport à $y = x$. Elle part de $(-1;0)$ avec une tangente verticale (car $g'(0) = 0$) et passe par $(0;\alpha)$.
""")

_add("bac-d-2019-sc-math-ex4", r"""
**1° a)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ (produit de deux facteurs tendant vers $+\infty$) et $\dfrac{f(x)}{x} = \left(2 - \dfrac{2}{x}\right)(1 + e^x) \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $f(x) - (2x - 2) = (2x - 2)e^x = 2xe^x - 2e^x \to 0$.

**c)** La droite $D : y = 2x - 2$ est **asymptote oblique** à $\Gamma$ en $-\infty$.

$f(x) - (2x - 2) = (2x - 2)e^x$ a le signe de $x - 1$ : $\Gamma$ est au-dessous de $D$ sur $]-\infty;1[$, au-dessus sur $]1;+\infty[$, et elles se coupent en $(1;0)$.

**2° a)** $f'(x) = 2(1 + e^x) + (2x - 2)e^x = 2 + 2xe^x$ et $f''(x) = 2e^x + 2xe^x = (2x + 2)e^x$.

**b)** $f''(x)$ a le signe de $x + 1$ : $f'$ décroît sur $]-\infty;-1]$ et croît sur $[-1;+\infty[$. Son minimum est $f'(-1) = 2 - \dfrac{2}{e} > 0$, donc $f'(x) > 0$ pour tout $x$.

**c)** $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**3° a)** $f(x) = 0 \iff x = 1$ (car $1 + e^x > 0$) : le point d'intersection est $(1;0)$.

**b)** $f(0) = -4$ et $f'(0) = 2$ : $T : y = 2x - 4$.

**c)** On trace $D$, $T$ (parallèle à $D$, au-dessous), le point $(0;-4)$, le point $(1;0)$ et le point d'inflexion $(-1;f(-1)) = \left(-1;-4 - \dfrac{4}{e}\right)$.

**d)** $(2x - 2)e^x = 2 + m \iff f(x) - (2x - 2) = 2 + m \iff f(x) = 2x + m$.

On cherche les points communs à $\Gamma$ et à $D_m : y = 2x + m$, parallèle à $D$ (et à $T$, qui est $D_{-4}$).

$h(x) = (2x - 2)e^x$ a pour dérivée $2xe^x$ : elle décroît de $0$ (en $-\infty$) jusqu'à $h(0) = -2$, puis croît jusqu'à $+\infty$. L'équation $h(x) = 2 + m$ a :
- **aucune solution** si $m < -4$ ;
- **une solution** ($x = 0$) si $m = -4$ ($D_m = T$) ;
- **deux solutions** si $-4 < m < -2$ ;
- **une solution** si $m \ge -2$.

**4° a)** Par parties, avec $u = 2x - 2$ et $v' = e^x$ :
$$I = \big[(2x - 2)e^x\big]_0^1 - \int_0^1 2e^x\,dx = (0 + 2) - 2(e - 1) = 4 - 2e.$$

**b)** Sur $[0;1]$, $f(x) \le 0$ (car $2x - 2 \le 0$). Or $\displaystyle\int_0^1 f(x)\,dx = \int_0^1 (2x - 2)\,dx + I = -1 + 4 - 2e = 3 - 2e$. Donc
$$A = 2e - 3 \text{ u.a.} \approx 2{,}44 \text{ u.a.}$$
""")

# ═══════════════════════════════════ 2020 ═════════════════════════════════════

_add("bac-d-2020-sn-math-ex3", r"""
**1° a)** $\lim\limits_{x \to +\infty} e^{-x} = 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - (x - 2)\big) = \lim\limits_{x \to +\infty} e^{-x} = 0$.

**b)** $(\Delta) : y = x - 2$ est **asymptote oblique** à $(C)$ en $+\infty$. Comme $f(x) - (x - 2) = e^{-x} > 0$, $(C)$ est toujours **au-dessus** de $(\Delta)$.

**2° a)** $f(x) = \dfrac{(x - 2)e^x + 1}{e^x} = \dfrac{xe^x - 2e^x + 1}{e^x}$, et $\dfrac{f(x)}{x} = 1 - \dfrac{2}{x} + \dfrac{e^{-x}}{x} = 1 - \dfrac{2}{x} + \dfrac{1}{xe^x}$.

**b)** En $-\infty$ : $xe^x - 2e^x + 1 \to 1$ et $e^x \to 0^+$, donc $\lim\limits_{x \to -\infty} f(x) = +\infty$.

$xe^x \to 0^-$, donc $\dfrac{1}{xe^x} \to -\infty$ et $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = -\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**3°** $f'(x) = 1 - e^{-x}$ ; $f'(x) > 0 \iff e^{-x} < 1 \iff x > 0$. $f(0) = -1$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $-1$ | ↗ | $+\infty$ |

**4° a)** Sur $]-\infty;0]$, $f$ décroît strictement de $+\infty$ à $-1$ : une solution $\beta < 0$. Sur $[0;+\infty[$, elle croît strictement de $-1$ à $+\infty$ : une solution $\alpha > 0$. Donc $\beta < \alpha$.

$f(1{,}8) = -0{,}2 + e^{-1{,}8} \approx -0{,}03 < 0$ et $f(1{,}9) = -0{,}1 + e^{-1{,}9} \approx 0{,}05 > 0$, donc $1{,}8 < \alpha < 1{,}9$ ($\beta \approx -1{,}15$).

**b)** $f(\alpha) = 0$ donne $e^{-\alpha} = 2 - \alpha$, donc $f'(\alpha) = 1 - (2 - \alpha) = \alpha - 1$.

**5°** On trace $(\Delta)$, le minimum $(0;-1)$, les points $(\beta;0)$ et $(\alpha;0)$, avec la branche parabolique verticale en $-\infty$. $(C)$ est au-dessus de $(\Delta)$ et s'en rapproche en $+\infty$.
""")

_add("bac-d-2020-sn-math-ex4", r"""
**1° a)** $\lim\limits_{x \to 0^+} x\ln x = 0$, donc $\lim\limits_{x \to 0^+} f(x) = 0 = f(0)$ : $f$ est continue à droite en $0$.

**b)** $\dfrac{f(x) - f(0)}{x - 0} = 1 - \ln x \to +\infty$ quand $x \to 0^+$ : $f$ n'est pas dérivable à droite en $0$ ; $(\Gamma)$ a en $O$ une **demi-tangente verticale**.

**c)** $f(x) = x(1 - \ln x)$ avec $1 - \ln x \to -\infty$, donc $\lim\limits_{x \to +\infty} f(x) = -\infty$, et $\dfrac{f(x)}{x} = 1 - \ln x \to -\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**2°** $f'(x) = 1 - \ln x - 1 = -\ln x$ : positive sur $]0;1[$, négative sur $]1;+\infty[$. $f(1) = 1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $0$ | ↗ | $1$ | ↘ | $-\infty$ |

**3° a)** $f(x) = 0 \iff x = 0$ ou $\ln x = 1 \iff x = 0$ ou $x = e$ : points $O(0;0)$ et $(e;0)$.

**b)** $f(e) = 0$ et $f'(e) = -1$ : $(T) : y = -(x - e)$, soit $(T) : y = -x + e$.

**4° a)** Sur $I = [1;+\infty[$, $g$ est continue et strictement décroissante, de $1$ à $-\infty$ : bijection de $I$ sur $J = ]-\infty;1]$.

**b)** $g(e) = 0$ et $g'(e) = -1$, donc $\left(g^{-1}\right)'(0) = \dfrac{1}{g'(e)} = -1$.

**c)** $(\Gamma)$ part de $O$ avec une demi-tangente verticale, monte jusqu'à $(1;1)$, redescend en coupant l'axe en $(e;0)$ où la tangente est $(T)$. $(\Gamma')$ est la symétrique de la partie sur $[1;+\infty[$ par rapport à $y = x$ : elle finit en $(1;1)$ avec une tangente verticale et passe par $(0;e)$.

**d)** $2x - x\ln x = m \iff f(x) + x = m \iff f(x) = -x + m$ (pour $x > 0$).

On cherche les points communs à $(\Gamma)$ (privée de $O$) et à la droite $D_m : y = -x + m$, parallèle à $(T)$.

$k(x) = 2x - x\ln x$ a pour dérivée $1 - \ln x$ : elle croît de $0$ (en $0^+$, sans l'atteindre) jusqu'à $k(e) = e$, puis décroît jusqu'à $-\infty$. L'équation $k(x) = m$ a :
- **aucune solution** si $m > e$ ;
- **une solution** ($x = e$) si $m = e$ ($D_m = (T)$) ;
- **deux solutions** si $0 < m < e$ ;
- **une solution** si $m \le 0$.

**5° a)** Par parties, avec $u = \ln x$ et $v' = x$ ($v = \dfrac{x^2}{2}$) :
$$A = \left[\dfrac{x^2}{2}\ln x\right]_1^e - \int_1^e \dfrac{x}{2}\,dx = \dfrac{e^2}{2} - \left[\dfrac{x^2}{4}\right]_1^e = \dfrac{e^2}{2} - \dfrac{e^2 - 1}{4} = \dfrac{e^2 + 1}{4}.$$

**b)** Sur $[1;e]$, $f(x) = x(1 - \ln x) \ge 0$. L'aire vaut
$$\int_1^e x\,dx - A = \dfrac{e^2 - 1}{2} - \dfrac{e^2 + 1}{4} = \dfrac{e^2 - 3}{4} \text{ u.a.} \approx 1{,}10 \text{ u.a.}$$
""")

_add("bac-d-2020-sc-math-ex3", r"""
**1° a)** $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = +\infty$ et $\lim\limits_{x \to -\infty}\big(f(x) - (-3x + 2)\big) = 0$.

La droite $y = -3x + 2$ est **asymptote oblique** à $(C)$ en $-\infty$, et $(C)$ est au-dessus ($e^x > 0$).

**b)** $f(x) = x\left(-3 + \dfrac{2}{x} + \dfrac{e^x}{x}\right)$ avec $\dfrac{e^x}{x} \to +\infty$ : $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$. **Branche parabolique de direction $(Oy)$**.

**2° a)** $f'(x) = -3 + e^x$.

**b)** $f'(\ln 3) = -3 + 3 = 0$. Comme $\exp$ est croissante : $f'(x) < 0$ pour $x < \ln 3$ et $f'(x) > 0$ pour $x > \ln 3$.

**c)** $f(\ln 3) = -3\ln 3 + 2 + 3 = 5 - 3\ln 3 \approx 1{,}70$.

| $x$ | $-\infty$ | | $\ln 3$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $5 - 3\ln 3$ | ↗ | $+\infty$ |

**3° a)** $f(2n) = -6n + 2 + e^{2n} = -(6n - 2) + e^{2n} = v_n - u_n$.

**b)** $u_{n+1} - u_n = 6$ : $(u_n)$ est arithmétique de raison $6$ et de premier terme $u_0 = -2$, et $\lim\limits_{n \to +\infty} u_n = +\infty$.

**c)** $\dfrac{v_{n+1}}{v_n} = e^2$ : $(v_n)$ est géométrique de raison $e^2$ et de premier terme $v_0 = 1$. Comme $e^2 > 1$ et $v_0 > 0$, elle est **croissante**.

**d)** $f(0) + f(2) + \dots + f(2020) = \displaystyle\sum_{n=0}^{1010}(v_n - u_n)$, soit $1011$ termes :
$$\sum_{n=0}^{1010} v_n = \dfrac{e^{2 \times 1011} - 1}{e^2 - 1} = \dfrac{e^{2022} - 1}{e^2 - 1}, \qquad \sum_{n=0}^{1010} u_n = 1011 \times \dfrac{u_0 + u_{1010}}{2} = 1011 \times \dfrac{-2 + 6058}{2} = 3\,061\,308.$$

$$S = \dfrac{e^{2022} - 1}{e^2 - 1} - 3\,061\,308.$$
""")

_add("bac-d-2020-sc-math-ex4", r"""
**1° a)** $\lim\limits_{x \to 0^+} x\ln x = 0$, donc $\lim\limits_{x \to 0^+} g(x) = -2$. $g(x) = x(1 - 2\ln x) - 2$, donc $\lim\limits_{x \to +\infty} g(x) = -\infty$.

**b)** $g'(x) = 1 - 2\ln x - 2 = -1 - 2\ln x$, et $g'\left(\dfrac{1}{\sqrt{e}}\right) = -1 - 2 \times \left(-\dfrac{1}{2}\right) = 0$.

**c)** $g\left(\dfrac{1}{\sqrt{e}}\right) = \dfrac{1}{\sqrt{e}} - 2 - \dfrac{2}{\sqrt{e}} \times \left(-\dfrac{1}{2}\right) = \dfrac{2}{\sqrt{e}} - 2 \approx -0{,}79$.

$g'(x) > 0 \iff \ln x < -\dfrac{1}{2} \iff x < \dfrac{1}{\sqrt{e}}$.

| $x$ | $0$ | | $\frac{1}{\sqrt{e}}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $+$ | $0$ | $-$ | |
| $g(x)$ | $-2$ | ↗ | $\frac{2}{\sqrt{e}} - 2$ | ↘ | $-\infty$ |

**d)** Le maximum de $g$ est $\dfrac{2}{\sqrt{e}} - 2 < 0$ (car $\sqrt{e} > 1$), donc $g(x) < 0$ pour tout $x > 0$.

**2° a)**
- En $0^+$ : $\ln x \to -\infty$ et $(x - 2)^2 \to 4$, donc $f(x) \to -\infty$ ;
- en $2$ (à gauche et à droite) : $\ln x \to \ln 2 > 0$ et $(x - 2)^2 \to 0^+$, donc $f(x) \to +\infty$ ;
- en $+\infty$ : $f(x) = \dfrac{\ln x}{x} \times \dfrac{x}{(x - 2)^2} \to 0 \times 0 = 0$.

**b)** Les trois asymptotes sont les droites $x = 0$ et $x = 2$ (verticales) et $y = 0$ (horizontale, en $+\infty$).

**3° a)**
$$f'(x) = \dfrac{\frac{1}{x}(x - 2)^2 - 2(x - 2)\ln x}{(x - 2)^4} = \dfrac{\frac{x - 2}{x} - 2\ln x}{(x - 2)^3} = \dfrac{x - 2 - 2x\ln x}{x(x - 2)^3} = \dfrac{g(x)}{x(x - 2)^3}.$$

**b)** $g(x) < 0$ et $x > 0$. Sur $]0;2[$, $(x - 2)^3 < 0$, donc $f'(x) > 0$. Sur $]2;+\infty[$, $(x - 2)^3 > 0$, donc $f'(x) < 0$.

| $x$ | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | ‖ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ ‖ $+\infty$ | ↘ | $0$ |

**4° a)** $f(1) = 0$ et $f'(1) = \dfrac{g(1)}{1 \times (-1)^3} = \dfrac{-1}{-1} = 1$ : $T : y = x - 1$.

**b)** On trace les trois asymptotes, le point $A(1;0)$ et la tangente $T$. La branche de droite est au-dessus de l'axe des abscisses et s'en rapproche en $+\infty$.

**5° a)** Sur $[3;4]$, $\ln x > 0$, donc $f(x) > 0$ et $S = \displaystyle\int_3^4 f(x)\,dx$.

**b)** Par parties, avec $u = \ln x$ et $v' = \dfrac{1}{(x - 2)^2}$ ($u' = \dfrac{1}{x}$, $v = -\dfrac{1}{x - 2}$) :
$$S = \left[\dfrac{-\ln x}{x - 2}\right]_3^4 + \int_3^4 \dfrac{1}{x(x - 2)}\,dx.$$

**c)** $\dfrac{1}{2}\left(\dfrac{1}{x - 2} - \dfrac{1}{x}\right) = \dfrac{1}{2} \times \dfrac{x - (x - 2)}{x(x - 2)} = \dfrac{1}{x(x - 2)}$. Donc
$$\int_3^4 \dfrac{dx}{x(x - 2)} = \dfrac{1}{2}\big[\ln(x - 2) - \ln x\big]_3^4 = \dfrac{1}{2}\big(\ln 2 - \ln 4 + \ln 3\big) = \dfrac{1}{2}\ln\dfrac{3}{2}.$$

**d)** $\left[\dfrac{-\ln x}{x - 2}\right]_3^4 = -\dfrac{\ln 4}{2} + \ln 3 = \ln 3 - \ln 2 = \ln\dfrac{3}{2}$, donc
$$S = \ln\dfrac{3}{2} + \dfrac{1}{2}\ln\dfrac{3}{2} = \dfrac{3}{2}\ln\dfrac{3}{2} \text{ u.a.} \approx 0{,}61 \text{ u.a.}$$
""")

# ═══════════════════════════════════ 2021 ═════════════════════════════════════

_add("bac-d-2021-sn-math-ex3", r"""
**1° a)** En $-\infty$ : $x + 2 \to -\infty$ et $e^{-x} \to +\infty$, donc $(x + 2)e^{-x} \to -\infty$ et $\lim\limits_{x \to -\infty} f(x) = -\infty$.

$\dfrac{f(x)}{x} = \dfrac{1}{x} + \left(1 + \dfrac{2}{x}\right)e^{-x} \to +\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**b)** $f(x) = 1 + (x + 2)e^{-x} = 1 + \dfrac{x}{e^x} + \dfrac{2}{e^x}$. En $+\infty$, $\dfrac{x}{e^x} \to 0$ et $\dfrac{2}{e^x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = 1$ : la droite $y = 1$ est **asymptote horizontale** en $+\infty$.

**2°** $f'(x) = e^{-x} - (x + 2)e^{-x} = -(x + 1)e^{-x}$, du signe de $-(x + 1)$. $f(-1) = 1 + e$.

| $x$ | $-\infty$ | | $-1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | |
| $f(x)$ | $-\infty$ | ↗ | $1 + e$ | ↘ | $1$ |

**3°** Sur $[-1;+\infty[$, $f(x) > 1 > 0$ : pas de solution. Sur $]-\infty;-1]$, $f$ croît strictement de $-\infty$ à $1 + e$ : une seule solution $\alpha$.

$f(-2{,}2) = 1 - 0{,}2e^{2{,}2} \approx -0{,}81 < 0$ et $f(-2) = 1 > 0$, donc $-2{,}2 < \alpha < -2$ ($\alpha \approx -2{,}12$).

**4° a)** $f''(x) = -e^{-x} + (x + 1)e^{-x} = xe^{-x}$ s'annule en $0$ en changeant de signe. $f(0) = 3$ : $I(0;3)$ est un point d'inflexion.

$f'(0) = -1$, donc $T : y = -x + 3$.

**b)** On trace l'asymptote $y = 1$, le maximum $(-1;1 + e) \approx (-1;3{,}72)$, le point d'inflexion $I(0;3)$ avec $T$, et le point $(\alpha;0)$.

**5° a)** La partie fermée par $(C)$ et les axes est comprise entre $x = \alpha$ et $x = 0$, où $f(x) \ge 0$. L'unité est 1 cm, donc $S = \displaystyle\int_\alpha^0 f(x)\,dx$ cm².

**b)** $h'(x) = -e^{-x} + (x + 3)e^{-x} = (x + 2)e^{-x}$, donc $1 + h'(x) = f(x)$. Une primitive de $f$ est $F(x) = x + h(x) = x - (x + 3)e^{-x}$.

**c)** $f(\alpha) = 0$ donne $(\alpha + 2)e^{-\alpha} = -1$, soit $e^{-\alpha} = \dfrac{-1}{\alpha + 2}$ (car $\alpha + 2 \neq 0$). Donc
$$S = F(0) - F(\alpha) = -3 - \alpha + (\alpha + 3)e^{-\alpha} = -3 - \alpha - \dfrac{\alpha + 3}{\alpha + 2} = \dfrac{-(\alpha + 3)(\alpha + 2) - (\alpha + 3)}{\alpha + 2} = \dfrac{-(\alpha + 3)^2}{\alpha + 2}.$$

(Numériquement, $S \approx 6{,}45$ cm².)
""")

_add("bac-d-2021-sn-math-ex4", r"""
**1° a)** $g'(x) = 2x - \dfrac{2}{x} = \dfrac{2(x^2 - 1)}{x}$ : négative sur $]0;1[$, nulle en $1$, positive sur $]1;+\infty[$.

**b)** $g(1) = 3$. C'est le minimum de $g$, donc $g(x) \ge 3 > 0$ sur $I$.

**2° a)** En $0^+$ : $\dfrac{\ln x}{x} \to -\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**. En $+\infty$ : $\dfrac{\ln x}{x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $f(x) - (x - 2) = \dfrac{2\ln x}{x} \to 0$ en $+\infty$ : $\Delta : y = x - 2$ est **asymptote oblique**.

Cette différence a le signe de $\ln x$ : $\Gamma$ est au-dessous de $\Delta$ sur $]0;1[$, au-dessus sur $]1;+\infty[$, et elles se coupent en $(1;-1)$.

**3° a)** $f'(x) = 1 + 2\,\dfrac{\frac{1}{x} \cdot x - \ln x}{x^2} = \dfrac{x^2 + 2 - 2\ln x}{x^2} = \dfrac{g(x)}{x^2}$.

**b)** $g(x) > 0$, donc $f'(x) > 0$ : $f$ est strictement croissante sur $I$, de $-\infty$ à $+\infty$.

**c)** $f$ est continue et strictement croissante de $-\infty$ à $+\infty$ : $\Gamma$ coupe $(Ox)$ en un seul point $A(\beta;0)$.

$f(1{,}47) \approx -0{,}006 < 0$ et $f(1{,}48) \approx 0{,}010 > 0$, donc $1{,}47 < \beta < 1{,}48$.

**4° a)** $f(e) = e - 2 + \dfrac{2}{e}$ et $f'(e) = \dfrac{g(e)}{e^2} = \dfrac{e^2}{e^2} = 1$ :
$$T : y = (x - e) + e - 2 + \dfrac{2}{e} = x - 2 + \dfrac{2}{e}.$$

$T$ est parallèle à $\Delta$.

**b)** On trace l'asymptote $x = 0$, $\Delta$, le point $(1;-1)$ commun à $\Gamma$ et $\Delta$, le point $A(\beta;0)$ et la tangente $T$ au point d'abscisse $e$.

**c)** Pour $x > 0$ : $(m + 2)x = 2\ln x \iff \dfrac{2\ln x}{x} = m + 2 \iff f(x) - (x - 2) = m + 2 \iff f(x) = x + m$.

On cherche les points communs à $\Gamma$ et à $D_m : y = x + m$, parallèle à $\Delta$ et à $T$.

$k(x) = \dfrac{2\ln x}{x}$ a pour dérivée $\dfrac{2(1 - \ln x)}{x^2}$ : elle croît de $-\infty$ jusqu'à $k(e) = \dfrac{2}{e}$, puis décroît vers $0$ (sans l'atteindre). L'équation $k(x) = m + 2$ a :
- **aucune solution** si $m > \dfrac{2}{e} - 2$ ;
- **une solution** ($x = e$) si $m = \dfrac{2}{e} - 2$ ($D_m = T$) ;
- **deux solutions** si $-2 < m < \dfrac{2}{e} - 2$ ;
- **une solution** si $m \le -2$.

**5° a)** $f$ est continue et strictement croissante : bijection de $I$ sur $J = \mathbb{R}$.

**b)** $f(1) = 1 - 2 + 0 = -1$, donc $f^{-1}(-1) = 1$. $f'(1) = g(1) = 3$, donc $\left(f^{-1}\right)'(-1) = \dfrac{1}{f'(1)} = \dfrac{1}{3}$.

**c)** $(\Gamma')$ est la symétrique de $\Gamma$ par rapport à $y = x$ : elle passe par $(-1;1)$ et $(0;\beta)$, a l'asymptote horizontale $y = 0$ en $-\infty$ et l'asymptote oblique $y = x + 2$ en $+\infty$.
""")

_add("bac-d-2021-sc-math-ex3", r"""
**1° a)** En $0^+$ : $4x^2 + 1 + 2\ln x \to -\infty$ et $2x^2 \to 0^+$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** $f(x) = 2 + \dfrac{1}{2x^2} + \dfrac{\ln x}{x^2}$, et $\dfrac{\ln x}{x^2} = \dfrac{1}{x} \times \dfrac{\ln x}{x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = 2$ : $(D) : y = 2$ est **asymptote horizontale** en $+\infty$.

**2° a)** $f'(x) = -\dfrac{1}{x^3} + \dfrac{\frac{1}{x} \cdot x^2 - 2x\ln x}{x^4} = -\dfrac{1}{x^3} + \dfrac{1 - 2\ln x}{x^3} = \dfrac{-2\ln x}{x^3}$.

**b)** $f'(x)$ a le signe de $-\ln x$. $f(1) = \dfrac{5}{2}$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $\frac{5}{2}$ | ↘ | $2$ |

**3° a)** Sur $I = [1;+\infty[$, $g$ est continue et strictement décroissante de $\dfrac{5}{2}$ vers $2$ (sans l'atteindre) : bijection de $I$ sur $J = \left]2;\dfrac{5}{2}\right]$.

**b)** $g^{-1}$ est définie sur $J$, strictement décroissante, de $+\infty$ (quand $x \to 2^+$) à $g^{-1}\left(\frac{5}{2}\right) = 1$.

| $x$ | $2$ | | $\frac{5}{2}$ |
|---|---|---|---|
| $g^{-1}(x)$ | ‖ $+\infty$ | ↘ | $1$ |

**4° a)** Sur $[1;+\infty[$, $f(x) > 2 > 0$ : pas de solution. Sur $]0;1]$, $f$ croît strictement de $-\infty$ à $\dfrac{5}{2}$ : une seule solution $x_0$.

$f(0{,}4) \approx -0{,}60 < 0$ et $f(0{,}5) \approx 1{,}23 > 0$, donc $0{,}4 < x_0 < 0{,}5$.

**b)** $(C)$ : asymptotes $x = 0$ et $(D) : y = 2$, maximum $\left(1;\frac{5}{2}\right)$, point $(x_0;0)$. $(C')$ est la symétrique de la partie de $(C)$ sur $[1;+\infty[$ par rapport à $y = x$ : elle part de $\left(\frac{5}{2};1\right)$ avec une tangente verticale et a l'asymptote verticale $x = 2$.

**5° a)** Par parties, avec $u = \ln x$ et $v' = \dfrac{1}{x^2}$ ($v = -\dfrac{1}{x}$) :
$$I = \left[-\dfrac{\ln x}{x}\right]_1^e + \int_1^e \dfrac{dx}{x^2} = -\dfrac{1}{e} + 1 - \dfrac{1}{e} = 1 - \dfrac{2}{e}.$$

**b)** Sur $[1;e]$, $f(x) > 2 > 0$, donc
$$A = \int_1^e \left(2 + \dfrac{1}{2x^2}\right)dx + I = 2(e - 1) + \dfrac{1}{2}\left(1 - \dfrac{1}{e}\right) + 1 - \dfrac{2}{e} = 2e - \dfrac{1}{2} - \dfrac{5}{2e} \text{ u.a.} \approx 4{,}02 \text{ u.a.}$$
""")

_add("bac-d-2021-sc-math-ex4", r"""
**1° a)** En $-\infty$ : $(2x - 2)e^x = 2xe^x - 2e^x \to 0$, donc $\lim\limits_{x \to -\infty} h(x) = -2$. En $+\infty$ : $\lim\limits_{x \to +\infty} h(x) = +\infty$.

**b)** $h'(x) = 2e^x + (2x - 2)e^x = 2xe^x$, du signe de $x$. $h(0) = -4$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $h'(x)$ | | $-$ | $0$ | $+$ | |
| $h(x)$ | $-2$ | ↘ | $-4$ | ↗ | $+\infty$ |

**c)** Sur $]-\infty;0]$, $h(x) < -2 < 0$ : pas de solution. Sur $[0;+\infty[$, $h$ croît strictement de $-4$ à $+\infty$ : une seule solution $\alpha$.

$h(1{,}2) = 0{,}4e^{1{,}2} - 2 \approx -0{,}67 < 0$ et $h(1{,}3) = 0{,}6e^{1{,}3} - 2 \approx 0{,}20 > 0$, donc $1{,}2 < \alpha < 1{,}3$ ($\alpha \approx 1{,}28$).

**d)** $h(x) < 0$ sur $]-\infty;\alpha[$, $h(\alpha) = 0$, et $h(x) > 0$ sur $]\alpha;+\infty[$.

**2° a)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \left(2 - \dfrac{4}{x}\right)(e^x - 1) \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** En $-\infty$ : $2x - 4 \to -\infty$ et $e^x - 1 \to -1$, donc $\lim\limits_{x \to -\infty} f(x) = +\infty$.

$f(x) - (-2x + 4) = (2x - 4)e^x \to 0$ : $(\Delta) : y = -2x + 4$ est **asymptote oblique** en $-\infty$.

Cette différence a le signe de $x - 2$ : $\Gamma$ est au-dessous de $(\Delta)$ sur $]-\infty;2[$, au-dessus sur $]2;+\infty[$, et elles se coupent en $(2;0)$.

**3° a)** $f'(x) = 2(e^x - 1) + (2x - 4)e^x = (2x - 2)e^x - 2 = h(x)$.

**b)**

| $x$ | $-\infty$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**c)** $h(\alpha) = 0$ donne $e^\alpha = \dfrac{1}{\alpha - 1}$ (car $\alpha \neq 1$), donc
$$f(\alpha) = (2\alpha - 4)\left(\dfrac{1}{\alpha - 1} - 1\right) = (2\alpha - 4) \times \dfrac{2 - \alpha}{\alpha - 1} = -\dfrac{2(\alpha - 2)^2}{\alpha - 1}.$$

(Numériquement, $f(\alpha) \approx -3{,}74$.)

**4° a)** $f(0) = -4 \times 0 = 0$ : $\Gamma$ passe par $O$. $f(x) = 0 \iff x = 2$ ou $e^x = 1 \iff x = 2$ ou $x = 0$ : points $O(0;0)$ et $(2;0)$.

**b)** On trace $(\Delta)$, le minimum $(\alpha;f(\alpha))$ — avec la valeur conseillée $\alpha \approx 1{,}3$, on a $f(1{,}3) \approx -3{,}74$ —, les points $O$ et $(2;0)$, et la branche parabolique verticale en $+\infty$.
""")

# ═══════════════════ Équations différentielles + étude (D) ═══════════════════

_add("bac-d-2019-sn-math-ex3", r"""
**A. 1°** L'équation caractéristique $r^2 - 4r + 4 = 0$ s'écrit $(r - 2)^2 = 0$ : racine double $r = 2$. La solution générale est
$$y(x) = (Ax + B)e^{2x}, \quad A, B \in \mathbb{R}.$$

**2°** $h(0) = B = -1$. $h'(x) = \big(A + 2(Ax + B)\big)e^{2x}$, donc $h'(0) = A + 2B = -1$, d'où $A = 1$. Ainsi $h(x) = (x - 1)e^{2x}$.

**B. 1° a)** En $-\infty$ : $x - 1 \to -\infty$ et $2 + e^{2x} \to 2$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$. En $+\infty$ : $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \left(1 - \dfrac{1}{x}\right)(2 + e^{2x}) \to +\infty$ : **branche parabolique de direction $(Oy)$**.

**b)** $f(x) - (2x - 2) = (x - 1)e^{2x} \to 0$ en $-\infty$ : $D : y = 2x - 2$ est **asymptote oblique** en $-\infty$.

Cette différence a le signe de $x - 1$ : $(C)$ est au-dessous de $D$ sur $]-\infty;1[$, au-dessus sur $]1;+\infty[$, et elles se coupent en $(1;0)$.

**2° a)** $f'(x) = (2 + e^{2x}) + (x - 1) \times 2e^{2x} = 2 + (2x - 1)e^{2x}$ et $f''(x) = 2e^{2x} + 2(2x - 1)e^{2x} = 4xe^{2x}$.

**b)** $f''$ s'annule en $0$ en changeant de signe, et $f(0) = -3$ : $A(0;-3)$ est un point d'inflexion.

**c)** $f''(x)$ a le signe de $x$ : $f'$ décroît sur $]-\infty;0]$ et croît sur $[0;+\infty[$. Son minimum est $f'(0) = 1 > 0$, donc $f'(x) > 0$ sur $\mathbb{R}$.

**d)** $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**3° a)** Tangente parallèle à $D$ $\iff f'(x) = 2 \iff (2x - 1)e^{2x} = 0 \iff x = \dfrac{1}{2}$.

$f\left(\dfrac{1}{2}\right) = -\dfrac{1}{2}(2 + e) = -1 - \dfrac{e}{2}$, donc $B\left(\dfrac{1}{2};-1 - \dfrac{e}{2}\right)$ et
$$T : y = 2\left(x - \dfrac{1}{2}\right) - 1 - \dfrac{e}{2} = 2x - 2 - \dfrac{e}{2}.$$

**b)** On trace $D$, $T$ (parallèle à $D$, au-dessous), $B \approx (0{,}5;-2{,}36)$, le point d'inflexion $A(0;-3)$ et le point $(1;0)$.

**c)** $x - 1 = me^{-2x} \iff (x - 1)e^{2x} = m \iff f(x) - (2x - 2) = m \iff f(x) = 2x - 2 + m$.

On cherche les points communs à $(C)$ et à la droite $D_m : y = 2x - 2 + m$, parallèle à $D$.

$h(x) = (x - 1)e^{2x}$ a pour dérivée $(2x - 1)e^{2x}$ : elle décroît de $0$ (en $-\infty$) jusqu'à $h\left(\frac{1}{2}\right) = -\dfrac{e}{2}$, puis croît jusqu'à $+\infty$. L'équation $h(x) = m$ a :
- **aucune solution** si $m < -\dfrac{e}{2}$ ;
- **une solution** ($x = \frac{1}{2}$) si $m = -\dfrac{e}{2}$ ($D_m = T$) ;
- **deux solutions** si $-\dfrac{e}{2} < m < 0$ ;
- **une solution** si $m \ge 0$.
""")

_add("bac-d-2022-sn-math-ex4", r"""
**I. 1°** L'équation caractéristique $r^2 + 2r + 1 = 0$ s'écrit $(r + 1)^2 = 0$ : racine double $r = -1$. La solution générale est
$$y(x) = (Ax + B)e^{-x}, \quad A, B \in \mathbb{R}.$$

**2°** $h(0) = B = -1$ et $h(-1) = (-A + B)e = 0$, d'où $A = B = -1$. Donc $h(x) = -(x + 1)e^{-x}$.

**II. 1° a)** En $-\infty$ : $x + 1 \to -\infty$ et $e^{-x} \to +\infty$, donc $-(x + 1)e^{-x} \to +\infty$ et $\lim\limits_{x \to -\infty} f(x) = +\infty$.

$\dfrac{f(x)}{x} = -\left(1 + \dfrac{1}{x}\right)e^{-x} - \dfrac{1}{x} \to -\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**b)** En $+\infty$ : $(x + 1)e^{-x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = -1$ : $(\Delta) : y = -1$ est **asymptote horizontale** en $+\infty$.

$f(x) - (-1) = -(x + 1)e^{-x}$ a le signe de $-(x + 1)$ : $\Gamma$ est au-dessus de $(\Delta)$ sur $]-\infty;-1[$, au-dessous sur $]-1;+\infty[$, et elles se coupent en $(-1;-1)$.

**2° a)** $f'(x) = -e^{-x} + (x + 1)e^{-x} = xe^{-x}$, du signe de $x$.

**b)** $f(0) = -2$.

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $-2$ | ↗ | $-1$ |

**3° a)** Sur $[0;+\infty[$, $f(x) < -1 < 0$ : pas de solution. Sur $]-\infty;0]$, $f$ décroît strictement de $+\infty$ à $-2$ : une seule solution $\alpha$.

$f(-1{,}3) = 0{,}3e^{1{,}3} - 1 \approx 0{,}10 > 0$ et $f(-1{,}2) = 0{,}2e^{1{,}2} - 1 \approx -0{,}34 < 0$, donc $-1{,}3 < \alpha < -1{,}2$.

**b)** $f''(x) = e^{-x} - xe^{-x} = (1 - x)e^{-x}$ s'annule en $1$ en changeant de signe : $A\left(1;-\dfrac{2}{e} - 1\right) \approx (1;-1{,}74)$ est un point d'inflexion.

**c)** On trace $(\Delta)$, le minimum $(0;-2)$, le point d'inflexion $A$, le point $(-1;-1)$ et le point $(\alpha;0)$.
""")

_add("bac-d-2023-sn-math-ex3", r"""
**1° a)** En $-\infty$ : $x^2 - x - 1 \to +\infty$ et $e^{-x} \to +\infty$, donc $\lim\limits_{x \to -\infty} f(x) = +\infty$.

$\dfrac{f(x)}{x} = \left(x - 1 - \dfrac{1}{x}\right)e^{-x} + \dfrac{1}{x} \to -\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**b)** En $+\infty$ : $x^2e^{-x} \to 0$, $xe^{-x} \to 0$ et $e^{-x} \to 0$, donc $\lim\limits_{x \to +\infty} f(x) = 1$ : $(\Delta) : y = 1$ est **asymptote horizontale** en $+\infty$.

**c)** $x^2 - x - 1$ a pour racines $x_1 = \dfrac{1 - \sqrt{5}}{2} \approx -0{,}62$ et $x_2 = \dfrac{1 + \sqrt{5}}{2} \approx 1{,}62$ : il est positif à l'extérieur de $[x_1;x_2]$ et négatif à l'intérieur.

$f(x) - 1 = (x^2 - x - 1)e^{-x}$ a le même signe : $\Gamma$ est au-dessus de $(\Delta)$ sur $]-\infty;x_1[ \cup ]x_2;+\infty[$, au-dessous sur $]x_1;x_2[$, et elles se coupent aux points d'abscisses $x_1$ et $x_2$.

**2° a)** $f'(x) = (2x - 1)e^{-x} - (x^2 - x - 1)e^{-x} = (-x^2 + 3x)e^{-x} = x(3 - x)e^{-x}$.

$f(0) = 0$ et $f(3) = 1 + 5e^{-3} \approx 1{,}25$.

| $x$ | $-\infty$ | | $0$ | | $3$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | $0$ | $-$ | |
| $f(x)$ | $+\infty$ | ↘ | $0$ | ↗ | $1 + 5e^{-3}$ | ↘ | $1$ |

**b)** On trace $(\Delta)$, le minimum $O(0;0)$, le maximum $(3;1 + 5e^{-3})$ et les points d'abscisses $x_1$ et $x_2$ sur $(\Delta)$.

**3° a)** $f''(x) = (2x - 3)e^{-x} - (-x^2 + 3x)e^{-x} = (x^2 - 5x + 3)e^{-x}$. Donc
$$f'' + 2f' + f = \big(x^2 - 5x + 3 + 2(-x^2 + 3x) + x^2 - x - 1\big)e^{-x} + 1 = 2e^{-x} + 1.$$

**b)** D'après a), $f = 2e^{-x} + 1 - f'' - 2f'$, donc une primitive de $f$ est
$$F(x) = -2e^{-x} + x - f'(x) - 2f(x).$$

Sur $[0;1] \subset [x_1;x_2]$, $\Gamma$ est au-dessous de $(\Delta)$, donc $A = \displaystyle\int_0^1 \big(1 - f(x)\big)\,dx = 1 - \big(F(1) - F(0)\big)$.

$F(0) = -2 - 0 - 0 = -2$ et $F(1) = -\dfrac{2}{e} + 1 - \dfrac{2}{e} - 2\left(1 - \dfrac{1}{e}\right) = -1 - \dfrac{2}{e}$, donc $\displaystyle\int_0^1 f(x)\,dx = 1 - \dfrac{2}{e}$ et
$$A = \dfrac{2}{e} \text{ u.a.} \approx 0{,}74 \text{ u.a.}$$
""")

# ═══════════════════════════════ 2022 — 2024 ══════════════════════════════════

_add("bac-d-2022-sn-math-ex5", r"""
**1° a)** $\lim\limits_{x \to 0^+} x^2\ln x = 0$ et $\lim\limits_{x \to 0^+} x^2 = 0$, donc $\lim\limits_{x \to 0^+} f(x) = 1$.

Interprétation : $(C)$ « part » du point $(0;1)$, qui ne lui appartient pas ($f$ n'est pas définie en $0$, mais se prolonge par continuité en posant $f(0) = 1$).

**b)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = x(2\ln x - 1) + \dfrac{1}{x} \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**2° a)** $f'(x) = 2x(2\ln x - 1) + x^2 \times \dfrac{2}{x} = 4x\ln x - 2x + 2x = 4x\ln x$.

**b)** $f'(x)$ a le signe de $\ln x$. $f(1) = -1 + 1 = 0$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $1$ | ↘ | $0$ | ↗ | $+\infty$ |

**3° a)** Sur $I = [1;+\infty[$, $g$ est continue et strictement croissante : bijection de $I$ sur $J = [0;+\infty[$.

**b)** $g^{-1}$ est définie sur $[0;+\infty[$, strictement croissante, de $g^{-1}(0) = 1$ à $+\infty$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $g^{-1}(x)$ | $1$ | ↗ | $+\infty$ |

**4°** $(C)$ part de $(0;1)$ (point exclu), descend jusqu'à $(1;0)$ où elle est tangente à l'axe des abscisses ($f'(1) = 0$), puis remonte : $f(\sqrt{e}) = 1$ et $f(e) = e^2 + 1 \approx 8{,}39$.

$(C')$ est la symétrique de la partie de $(C)$ sur $[1;+\infty[$ par rapport à $y = x$ : elle part de $(0;1)$ avec une tangente verticale.

**5° a)** Par parties, avec $u = \ln x$ et $v' = x^2$ ($u' = \dfrac{1}{x}$, $v = \dfrac{x^3}{3}$) :
$$K = \left[\dfrac{x^3}{3}\ln x\right]_1^e - \int_1^e \dfrac{x^2}{3}\,dx = \dfrac{e^3}{3} - \dfrac{e^3 - 1}{9} = \dfrac{2e^3 + 1}{9}.$$

**b)** $f(x) \ge 0$ (son minimum est $0$), donc
$$A = \int_1^e (2x^2\ln x - x^2 + 1)\,dx = 2K - \dfrac{e^3 - 1}{3} + (e - 1) = \dfrac{e^3 + 9e - 4}{9} \text{ u.a.} \approx 4{,}51 \text{ u.a.}$$
""")

_add("bac-d-2022-sc-math-ex3", r"""
**1° a)** $\lim\limits_{x \to -\infty} xe^x = 0$, donc $\lim\limits_{x \to -\infty} h(x) = 1$ ; et $\lim\limits_{x \to +\infty} h(x) = +\infty$.

**b)** $h'(x) = e^x + xe^x = (x + 1)e^x$, du signe de $x + 1$. $h(-1) = 1 - \dfrac{1}{e} \approx 0{,}63$.

| $x$ | $-\infty$ | | $-1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $h'(x)$ | | $-$ | $0$ | $+$ | |
| $h(x)$ | $1$ | ↘ | $1 - \frac{1}{e}$ | ↗ | $+\infty$ |

**c)** Le minimum de $h$ est $1 - \dfrac{1}{e} > 0$, donc $h(x) > 0$ pour tout réel $x$.

**2. a)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \left(1 - \dfrac{1}{x}\right)e^x + 1 \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**b)** En $-\infty$ : $(x - 1)e^x = xe^x - e^x \to 0$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $f(x) - x = (x - 1)e^x \to 0$ : $(\Delta) : y = x$ est **asymptote oblique** en $-\infty$.

**c)** $f(x) - x = (x - 1)e^x$ a le signe de $x - 1$ : $\Gamma$ est au-dessous de $(\Delta)$ sur $]-\infty;1[$, au-dessus sur $]1;+\infty[$, et elles se coupent en $(1;1)$.

**3. a)** $f'(x) = e^x + (x - 1)e^x + 1 = xe^x + 1 = h(x)$.

**b)** $h(x) > 0$ : $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**c)** On trace $(\Delta)$, les points $(0;-1)$ et $(1;1)$, et la branche parabolique verticale en $+\infty$. $f'' = h'$ s'annule en $-1$ en changeant de signe : $\left(-1;-1 - \dfrac{2}{e}\right) \approx (-1;-1{,}74)$ est un point d'inflexion.
""")

_add("bac-d-2022-sc-math-ex4", r"""
**1. a)** En $0^+$ : $x + 1 + \ln x \to -\infty$ et $x \to 0^+$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** $f(x) = 1 + \dfrac{1}{x} + \dfrac{\ln x}{x} \to 1$ en $+\infty$ : $(D) : y = 1$ est **asymptote horizontale** en $+\infty$.

**2. a)** $f'(x) = -\dfrac{1}{x^2} + \dfrac{1 - \ln x}{x^2} = -\dfrac{\ln x}{x^2}$.

**b)** $f'(x)$ a le signe de $-\ln x$. $f(1) = 2$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $2$ | ↘ | $1$ |

**c)** Sur $[1;+\infty[$, $f(x) > 1 > 0$ : pas de solution. Sur $]0;1]$, $f$ croît strictement de $-\infty$ à $2$ : une seule solution $x_0$.

$f(0{,}27) \approx -0{,}15 < 0$ et $f(0{,}28) \approx 0{,}03 > 0$, donc $0{,}27 < x_0 < 0{,}28$.

**3. a)** Sur $I = ]0;1]$, $g$ est continue et strictement croissante : bijection de $I$ sur $J = ]-\infty;2]$.

**b)** $g^{-1}$ est définie sur $]-\infty;2]$, strictement croissante, de $0$ (en $-\infty$) à $g^{-1}(2) = 1$.

| $x$ | $-\infty$ | | $2$ |
|---|---|---|---|
| $g^{-1}(x)$ | $0$ | ↗ | $1$ |

**4. a)** $(C)$ : asymptotes $x = 0$ et $(D) : y = 1$, maximum $(1;2)$, point $(x_0;0)$. $(C')$ est la symétrique de la partie de $(C)$ sur $]0;1]$ par rapport à $y = x$ : elle a l'asymptote $y = 0$ en $-\infty$ et se termine en $(2;1)$ avec une tangente verticale.

**b)** Pour $x > 0$ : $(m - 1)x = 1 + \ln x \iff m = 1 + \dfrac{1 + \ln x}{x} \iff f(x) = m$.

On cherche les points communs à $(C)$ et à la droite horizontale $y = m$ :
- si $m > 2$ : **aucune solution** ;
- si $m = 2$ : **une solution**, $x = 1$ ;
- si $1 < m < 2$ : **deux solutions** (une dans $]0;1[$, une dans $]1;+\infty[$) ;
- si $m \le 1$ : **une solution**, dans $]0;1[$.

**5. a)** $\displaystyle\int_1^e \dfrac{\ln x}{x}\,dx = \left[\dfrac{(\ln x)^2}{2}\right]_1^e = \dfrac{1}{2}$.

**b)** Sur $[1;e]$, $f(x) > 1 > 0$, donc
$$A = \int_1^e \left(1 + \dfrac{1}{x}\right)dx + \dfrac{1}{2} = (e - 1) + 1 + \dfrac{1}{2} = e + \dfrac{1}{2} \text{ u.a.} \approx 3{,}22 \text{ u.a.}$$
""")

_add("bac-d-2023-sn-math-ex5", r"""
**I. 1° a)** $\lim\limits_{x \to 0^+} 3\ln x = -\infty$, donc $\lim\limits_{x \to 0^+} g(x) = -\infty$ ; et $\lim\limits_{x \to +\infty} g(x) = +\infty$.

**b)** $g'(x) = 2x + \dfrac{3}{x} > 0$ : $g$ est strictement croissante sur $]0;+\infty[$, de $-\infty$ à $+\infty$.

**2° a)** $g$ est continue et strictement croissante de $-\infty$ à $+\infty$ : une unique solution $\alpha$. $g(1{,}6) \approx -0{,}03 < 0$ et $g(1{,}7) \approx 0{,}48 > 0$, donc $1{,}6 < \alpha < 1{,}7$.

**b)** $g(x) < 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) > 0$ sur $]\alpha;+\infty[$.

**II. 1° a)** En $0^+$ : $1 - 3\ln x \to +\infty$ et $\dfrac{1}{x} \to +\infty$, donc $\lim\limits_{x \to 0^+} f(x) = +\infty$ : la droite $x = 0$ est **asymptote verticale**.

**b)** $\dfrac{1 - 3\ln x}{x} = \dfrac{1}{x} - 3\dfrac{\ln x}{x} \to 0$ en $+\infty$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - x + 2\big) = 0$ : $(D) : y = x - 2$ est **asymptote oblique** en $+\infty$.

**c)** $f(x) - (x - 2) = \dfrac{1 - 3\ln x}{x}$ a le signe de $1 - 3\ln x$, qui s'annule pour $x = e^{1/3}$. $(C)$ est au-dessus de $(D)$ sur $\left]0;e^{1/3}\right[$, au-dessous sur $\left]e^{1/3};+\infty\right[$, et elles se coupent en $\left(e^{1/3};e^{1/3} - 2\right)$.

**2° a)** $f'(x) = 1 + \dfrac{-\frac{3}{x} \cdot x - (1 - 3\ln x)}{x^2} = 1 + \dfrac{-4 + 3\ln x}{x^2} = \dfrac{x^2 - 4 + 3\ln x}{x^2} = \dfrac{g(x)}{x^2}$.

**b)** $g(\alpha) = 0$ donne $3\ln\alpha = 4 - \alpha^2$, donc
$$f(\alpha) = \alpha - 2 + \dfrac{1 - 4 + \alpha^2}{\alpha} = \dfrac{\alpha^2 - 2\alpha + \alpha^2 - 3}{\alpha} = \dfrac{2\alpha^2 - 2\alpha - 3}{\alpha} \approx -0{,}66.$$

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**3° a)** Sur $I = ]0;\alpha]$, $h$ est continue et strictement décroissante : bijection de $I$ sur $J = [f(\alpha);+\infty[$.

**b)** $h^{-1}$ est définie sur $J$, strictement décroissante, de $h^{-1}(f(\alpha)) = \alpha$ vers $0$ en $+\infty$.

| $x$ | $f(\alpha)$ | | $+\infty$ |
|---|---|---|---|
| $h^{-1}(x)$ | $\alpha$ | ↘ | $0$ |

**4°** $(C)$ : asymptote $x = 0$, asymptote $(D)$, point commun $\left(e^{1/3};e^{1/3} - 2\right) \approx (1{,}40;-0{,}60)$, minimum $(\alpha;f(\alpha)) \approx (1{,}61;-0{,}66)$. $(C')$ est la symétrique de la partie de $(C)$ sur $]0;\alpha]$ par rapport à $y = x$ : elle part de $(f(\alpha);\alpha)$ avec une tangente verticale et a l'asymptote $y = 0$ en $+\infty$.
""")

_add("bac-d-2024-sn-math-ex3", r"""
**1. a)** $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$ ; et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $\dfrac{f(x)}{x} = 1 - \dfrac{3}{x} + \dfrac{1}{2} \times \dfrac{e^x}{x} \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**c)** $f(x) - (x - 3) = \dfrac{1}{2}e^x \to 0$ en $-\infty$ : $D : y = x - 3$ est **asymptote oblique** en $-\infty$. Comme $\dfrac{1}{2}e^x > 0$, $\Gamma$ est toujours **au-dessus** de $D$.

**2)** $f'(x) = 1 + \dfrac{1}{2}e^x > 0$ : $f$ est strictement croissante sur $\mathbb{R}$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $+\infty$ |

**3. a)** $f$ est continue et strictement croissante de $-\infty$ à $+\infty$ : une unique solution $\alpha$.

$f(1{,}2) = -1{,}8 + \dfrac{1}{2}e^{1{,}2} \approx -0{,}14 < 0$ et $f(1{,}3) = -1{,}7 + \dfrac{1}{2}e^{1{,}3} \approx 0{,}13 > 0$, donc $1{,}2 < \alpha < 1{,}3$.

**b)** On trace $D$, le point $(0;-2{,}5)$, le point $(\alpha;0)$, et la branche parabolique verticale en $+\infty$ ; $\Gamma$ est au-dessus de $D$ et s'en rapproche en $-\infty$.
""")

_add("bac-d-2024-sn-math-ex5", r"""
**I. 1.** $u'(x) = 2 - \dfrac{1}{x} = \dfrac{2x - 1}{x}$ : négative sur $\left]0;\dfrac{1}{2}\right[$, positive sur $\left]\dfrac{1}{2};+\infty\right[$. $u\left(\dfrac{1}{2}\right) = 1 - 1 - \ln\dfrac{1}{2} = \ln 2$.

$\lim\limits_{x \to 0^+} u(x) = +\infty$ (car $-\ln x \to +\infty$) et $\lim\limits_{x \to +\infty} u(x) = +\infty$ (car $u(x) = x\left(2 - \frac{1}{x} - \frac{\ln x}{x}\right)$).

| $x$ | $0$ | | $\frac{1}{2}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $u'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $u(x)$ | ‖ $+\infty$ | ↘ | $\ln 2$ | ↗ | $+\infty$ |

**2.** Le minimum de $u$ est $\ln 2 > 0$, donc $u(x) > 0$ sur $]0;+\infty[$.

**II. 1. a)** $\lim\limits_{x \to 0^+} x\ln x = 0$, donc $\lim\limits_{x \to 0^+} g(x) = -2 = g(0)$ : $g$ est continue à droite en $0$.

**b)** $\dfrac{g(x) - g(0)}{x} = \dfrac{x^2 - x\ln x}{x} = x - \ln x \to +\infty$ quand $x \to 0^+$ : $g$ n'est pas dérivable à droite en $0$, et $(C)$ a au point $(0;-2)$ une **demi-tangente verticale**.

**c)** $g(x) = x\left(x - \dfrac{2}{x} - \ln x\right)$ et $x - \ln x \to +\infty$, donc $\lim\limits_{x \to +\infty} g(x) = +\infty$ et $\dfrac{g(x)}{x} = x - \ln x - \dfrac{2}{x} \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**2. a)** $g'(x) = 2x - \ln x - 1 = u(x) > 0$ : $g$ est strictement croissante sur $[0;+\infty[$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $g'(x)$ | | $+$ | |
| $g(x)$ | $-2$ | ↗ | $+\infty$ |

**b)** $g(1) = -1$ et $g'(1) = u(1) = 1$ : $(T) : y = x - 2$.

**c)** $g$ est continue et strictement croissante de $-2$ à $+\infty$ : elle s'annule une seule fois, en $\alpha$. $g(1{,}7) \approx -0{,}01 < 0$ et $g(1{,}8) \approx 0{,}18 > 0$, donc $1{,}7 < \alpha < 1{,}8$.

**d)** $g''(x) = u'(x) = \dfrac{2x - 1}{x}$ s'annule en $\dfrac{1}{2}$ en changeant de signe : $B\left(\dfrac{1}{2};g\left(\dfrac{1}{2}\right)\right)$ est un point d'inflexion, avec
$$g\left(\dfrac{1}{2}\right) = \dfrac{1}{4} - 2 - \dfrac{1}{2}\ln\dfrac{1}{2} = -\dfrac{7}{4} + \dfrac{\ln 2}{2} \approx -1{,}40.$$

**3.** $(C)$ part de $(0;-2)$ avec une demi-tangente verticale, passe par le point d'inflexion $B$, par $(1;-1)$ où la tangente est $(T)$, coupe l'axe en $A(\alpha;0)$, puis a une branche parabolique verticale.
""")


# ─────────────────────────────────────────────────────────────────────────────
# Contrôles mathématiques des corrections (rejoués par scripts/check_content.py).
CHECKS: dict[str, list[str]] = {
    "bac-d-2022-sn-math-ex5": [
        "lim(x**2*(2*log(x) - 1) + 1, 0, 1, '+') and same(D(x**2*(2*log(x) - 1) + 1), 4*x*log(x))",
        "close((x**2*(2*log(x) - 1) + 1).subs(x, sqrt(E)), 1) and close((x**2*(2*log(x) - 1) + 1).subs(x, E), E**2 + 1)",
        "integ(x**2*log(x), 1, E, (2*E**3 + 1)/9) and integ(x**2*(2*log(x) - 1) + 1, 1, E, (E**3 + 9*E - 4)/9)",
    ],
    "bac-d-2022-sc-math-ex3": [
        "same(D(x*exp(x) + 1), (x + 1)*exp(x)) and close((x*exp(x) + 1).subs(x, -1), 1 - 1/E)",
        "same(D((x - 1)*exp(x) + x), x*exp(x) + 1) and close(((x - 1)*exp(x) + x).subs(x, -1), -1 - 2/E)",
    ],
    "bac-d-2022-sc-math-ex4": [
        "same(D((x + 1 + log(x))/x), -log(x)/x**2) and racine((x + 1 + log(x))/x, 0.27, 0.28)",
        "same(1 + (1 + log(x))/x, (x + 1 + log(x))/x)",
        "integ((x + 1 + log(x))/x, 1, E, E + Rational(1, 2))",
    ],
    "bac-d-2023-sn-math-ex5": [
        "racine(x**2 - 4 + 3*log(x), 1.6, 1.7)",
        "same(D(x - 2 + (1 - 3*log(x))/x), (x**2 - 4 + 3*log(x))/x**2)",
        "en_racine(x**2 - 4 + 3*log(x), 1.6, 1.7, x - 2 + (1 - 3*log(x))/x, (2*x**2 - 2*x - 3)/x)",
        "abs(float(((2*x**2 - 2*x - 3)/x).subs(x, root_in(x**2 - 4 + 3*log(x), 1.6, 1.7))) + 0.656) < 0.001",
    ],
    "bac-d-2024-sn-math-ex3": [
        "racine(x - 3 + exp(x)/2, 1.2, 1.3)",
    ],
    "bac-d-2024-sn-math-ex5": [
        "same(D(2*x - 1 - log(x)), (2*x - 1)/x) and close((2*x - 1 - log(x)).subs(x, Rational(1, 2)), log(2))",
        "same(D(x**2 - 2 - x*log(x)), 2*x - 1 - log(x)) and lim(x - log(x), 0, oo, '+')",
        "racine(x**2 - 2 - x*log(x), 1.7, 1.8)",
        "close((x**2 - 2 - x*log(x)).subs(x, Rational(1, 2)), -Rational(7, 4) + log(2)/2)",
    ],
    "bac-d-2021-sn-math-ex3": [
        "same(D(1 + (x + 2)*exp(-x)), -(x + 1)*exp(-x)) and same(D(1 + (x + 2)*exp(-x), 2), x*exp(-x))",
        "racine(1 + (x + 2)*exp(-x), -2.2, -2)",
        "same(1 + D(-(x + 3)*exp(-x)), 1 + (x + 2)*exp(-x))",
        "en_racine(1 + (x + 2)*exp(-x), -2.2, -2, -3 - x + (x + 3)*exp(-x), -(x + 3)**2/(x + 2))",
        "en_racine(1 + (x + 2)*exp(-x), -2.2, -2, Integral(1 + (t + 2)*exp(-t), (t, x, 0)).doit(), -(x + 3)**2/(x + 2))",
    ],
    "bac-d-2021-sn-math-ex4": [
        "same(D(x - 2 + 2*log(x)/x), (x**2 + 2 - 2*log(x))/x**2)",
        "racine(x - 2 + 2*log(x)/x, 1.47, 1.48)",
        "close(D(x - 2 + 2*log(x)/x).subs(x, E), 1) and close((x - 2 + 2*log(x)/x).subs(x, E), E - 2 + 2/E)",
        "same(D(2*log(x)/x), 2*(1 - log(x))/x**2) and close((2*log(x)/x).subs(x, E), 2/E)",
        "close((x - 2 + 2*log(x)/x).subs(x, 1), -1) and close(D(x - 2 + 2*log(x)/x).subs(x, 1), 3)",
    ],
    "bac-d-2021-sc-math-ex3": [
        "same(D((4*x**2 + 1 + 2*log(x))/(2*x**2)), -2*log(x)/x**3)",
        "close(((4*x**2 + 1 + 2*log(x))/(2*x**2)).subs(x, 1), Rational(5, 2))",
        "racine((4*x**2 + 1 + 2*log(x))/(2*x**2), 0.4, 0.5)",
        "integ(log(x)/x**2, 1, E, 1 - 2/E) and integ((4*x**2 + 1 + 2*log(x))/(2*x**2), 1, E, 2*E - Rational(1, 2) - 5/(2*E))",
    ],
    "bac-d-2021-sc-math-ex4": [
        "same(D((2*x - 2)*exp(x) - 2), 2*x*exp(x)) and racine((2*x - 2)*exp(x) - 2, 1.2, 1.3)",
        "same(D((2*x - 4)*(exp(x) - 1)), (2*x - 2)*exp(x) - 2)",
        "en_racine((2*x - 2)*exp(x) - 2, 1.2, 1.3, (2*x - 4)*(exp(x) - 1), -2*(x - 2)**2/(x - 1))",
        "abs(float(((2*x - 4)*(exp(x) - 1)).subs(x, root_in((2*x - 2)*exp(x) - 2, 1.2, 1.3))) + 3.74) < 0.005",
        "abs(float(((2*x - 4)*(exp(x) - 1)).subs(x, 1.3)) + 3.74) < 0.005",
    ],
    "bac-d-2019-sn-math-ex3": [
        "same(D((x - 1)*exp(2*x), 2) - 4*D((x - 1)*exp(2*x)) + 4*(x - 1)*exp(2*x), 0*x)",
        "same(D((x - 1)*(2 + exp(2*x))), 2 + (2*x - 1)*exp(2*x)) and same(D((x - 1)*(2 + exp(2*x)), 2), 4*x*exp(2*x))",
        "close(((x - 1)*(2 + exp(2*x))).subs(x, Rational(1, 2)), -1 - E/2)",
        "close(((x - 1)*exp(2*x)).subs(x, Rational(1, 2)), -E/2)",
    ],
    "bac-d-2022-sn-math-ex4": [
        "same(D(-(x + 1)*exp(-x), 2) + 2*D(-(x + 1)*exp(-x)) - (x + 1)*exp(-x), 0*x)",
        "same(D(-(x + 1)*exp(-x) - 1), x*exp(-x)) and same(D(-(x + 1)*exp(-x) - 1, 2), (1 - x)*exp(-x))",
        "racine(-(x + 1)*exp(-x) - 1, -1.3, -1.2)",
        "close((-(x + 1)*exp(-x) - 1).subs(x, 1), -2/E - 1)",
    ],
    "bac-d-2023-sn-math-ex3": [
        "same(D((x**2 - x - 1)*exp(-x) + 1), x*(3 - x)*exp(-x))",
        "same(D((x**2 - x - 1)*exp(-x) + 1, 2), (x**2 - 5*x + 3)*exp(-x))",
        "close(((x**2 - x - 1)*exp(-x) + 1).subs(x, 3), 1 + 5*exp(-3))",
        "same(D(-2*exp(-x) + x - D((x**2 - x - 1)*exp(-x) + 1) - 2*((x**2 - x - 1)*exp(-x) + 1)), (x**2 - x - 1)*exp(-x) + 1)",
        "integ(1 - ((x**2 - x - 1)*exp(-x) + 1), 0, 1, 2/E)",
    ],
    "bac-d-2019-sn-math-ex4": [
        "racine(1/x - log(x), 1.7, 1.8) and same(D((x - 1)*(1 - log(x))), 1/x - log(x))",
        "en_racine(1/x - log(x), 1.7, 1.8, (x - 1)*(1 - log(x)), (x - 1)**2/x)",
        "close(1/(1/E - 1), E/(1 - E))",
        "integ((x - 1)*log(x), 1, E, (E**2 - 3)/4) and integ((x - 1)*(1 - log(x)), 1, E, (E**2 - 4*E + 5)/4)",
    ],
    "bac-d-2019-sc-math-ex3": [
        "lim(((x + 1)**2*log(x + 1) - (x + 1))/(x + 1), -1, -1, '+')",
        "same(D((x + 1)**2*log(x + 1) - (x + 1)), 2*(x + 1)*log(x + 1) + x)",
        "close(((x + 1)**2*log(x + 1) - (x + 1)).subs(x, 0), -1)",
        "racine((x + 1)**2*log(x + 1) - (x + 1), 0.7, 0.8)",
        "en_racine((x + 1)**2*log(x + 1) - (x + 1), 0.7, 0.8, 2*(x + 1)*log(x + 1) + x, x + 2)",
    ],
    "bac-d-2019-sc-math-ex4": [
        "same(D((2*x - 2)*(1 + exp(x))), 2 + 2*x*exp(x)) and same(D((2*x - 2)*(1 + exp(x)), 2), (2*x + 2)*exp(x))",
        "close((2 + 2*x*exp(x)).subs(x, -1), 2 - 2/E)",
        "close(((2*x - 2)*(1 + exp(x))).subs(x, 0), -4) and close(((2*x - 2)*(1 + exp(x))).subs(x, -1), -4 - 4/E)",
        "close(((2*x - 2)*exp(x)).subs(x, 0), -2) and same(D((2*x - 2)*exp(x)), 2*x*exp(x))",
        "integ((2*x - 2)*exp(x), 0, 1, 4 - 2*E) and integ(-(2*x - 2)*(1 + exp(x)), 0, 1, 2*E - 3)",
    ],
    "bac-d-2020-sn-math-ex3": [
        "same(x - 2 + exp(-x), (x*exp(x) - 2*exp(x) + 1)/exp(x))",
        "racine(x - 2 + exp(-x), 1.8, 1.9) and racine(x - 2 + exp(-x), -1.2, -1.1)",
        "en_racine(x - 2 + exp(-x), 1.8, 1.9, 1 - exp(-x), x - 1)",
    ],
    "bac-d-2020-sn-math-ex4": [
        "lim(1 - log(x), 0, oo, '+') and same(D(x - x*log(x)), -log(x))",
        "close(D(x - x*log(x)).subs(x, E), -1) and close((x - x*log(x)).subs(x, E), 0)",
        "same(D(2*x - x*log(x)), 1 - log(x)) and close((2*x - x*log(x)).subs(x, E), E)",
        "integ(x*log(x), 1, E, (E**2 + 1)/4) and integ(x - x*log(x), 1, E, (E**2 - 3)/4)",
    ],
    "bac-d-2020-sc-math-ex3": [
        "close((-3*x + 2 + exp(x)).subs(x, log(3)), 5 - 3*log(3))",
        "sum(6*k - 2 for k in range(1011)) == 3061308",
        "close(sum(exp(2*k) for k in range(4)), (exp(8) - 1)/(exp(2) - 1))",
    ],
    "bac-d-2020-sc-math-ex4": [
        "close((x - 2 - 2*x*log(x)).subs(x, 1/sqrt(E)), 2/sqrt(E) - 2)",
        "same(D(log(x)/(x - 2)**2), (x - 2 - 2*x*log(x))/(x*(x - 2)**3))",
        "close(D(log(x)/(x - 2)**2).subs(x, 1), 1)",
        "integ(1/(x*(x - 2)), 3, 4, log(Rational(3, 2))/2)",
        "integ(log(x)/(x - 2)**2, 3, 4, Rational(3, 2)*log(Rational(3, 2)))",
    ],
    "bac-d-2018-sn-math-ex4": [
        "same((2 + x + x*log(x))/x, 2/x + 1 + log(x)) and same(D(2/x + 1 + log(x)), (x - 2)/x**2)",
        "close((2/x + 1 + log(x)).subs(x, 2), 2 + log(2)) and close(D(2/x + 1 + log(x)).subs(x, 1), -1)",
        "same(D(2/x + 1 + log(x) - x), -(x**2 - x + 2)/x**2)",
        "racine(2/x + 1 + log(x) - x, 2, 3)",
        "integ(2/x + 1 + log(x), 1, E, E + 2)",
    ],
    "bac-d-2018-sn-math-ex3": [
        "same(D(2*x - 1 + 2*x*exp(-x), 2), (2*x - 4)*exp(-x))",
        "close((2*x - 1 + 2*x*exp(-x)).subs(x, 2), 3 + 4*exp(-2)) and close(D(2*x - 1 + 2*x*exp(-x)).subs(x, 2), 2 - 2*exp(-2))",
        "racine(2*x - 1 + 2*x*exp(-x), 0.2, 0.3)",
        "close((2*x - 1 + 2*x*exp(-x)).subs(x, 1), 1 + 2/E)",
        "close((2*x*exp(-x)).subs(x, 1), 2/E) and same(D(2*x*exp(-x)), (2 - 2*x)*exp(-x))",
    ],
    "bac-d-2018-sc-math-ex3": [
        "racine(x + 2 - exp(x), -1.9, -1.8) and racine(x + 2 - exp(x), 1.1, 1.2)",
        "en_racine(x + 2 - exp(x), -1.9, -1.8, x + 1 - exp(x), -1) and en_racine(x + 2 - exp(x), 1.1, 1.2, x + 1 - exp(x), -1)",
        "en_racine(x + 2 - exp(x), -1.9, -1.8, 1/(1 - exp(x)), -1/(1 + x))",
        "close((x + 2 - exp(x)).subs(x, log(2)), log(2)) and close(D(x + 2 - exp(x)).subs(x, log(2)), -1)",
    ],
    "bac-d-2018-sc-math-ex4": [
        "racine(-x + 3 - 2*log(x), 1.8, 1.9)",
        "same(D((x - 1 + log(x))/x**2), (-x + 3 - 2*log(x))/x**3)",
        "en_racine(-x + 3 - 2*log(x), 1.8, 1.9, (x - 1 + log(x))/x**2, (x + 1)/(2*x**2))",
        "close(D((x - 1 + log(x))/x**2).subs(x, 1), 2)",
        "same(D((x - 1 + log(x))/x**2 - 2*x), (-2*x**3 - x + 3 - 2*log(x))/x**3)",
        "close(((x - 1 + log(x))/x**2 - 2*x).subs(x, 1), -2)",
        "integ(log(x)/x**2, 1, E, 1 - 2/E) and integ((x - 1 + log(x))/x**2, 1, E, 1 - 1/E)",
    ],
    "bac-d-2017-sn-math-ex3": [
        "close((-exp(-x) + 2).subs(x, -log(2)), 0) and close((exp(-x) + 2*x - 2).subs(x, -log(2)), -2*log(2))",
        "racine(exp(-x) + 2*x - 2, -1.7, -1.6) and racine(exp(-x) + 2*x - 2, 0.7, 0.8)",
        "lim(exp(-x)/x, -oo, -oo)",
        "all(close(sum(exp(-j) + 2*j - 2 for j in range(k + 1)), (1 - exp(-(k + 1)))/(1 - exp(-1)) + (k + 1)*(k - 2)) for k in range(6))",
    ],
    "bac-d-2017-sn-math-ex4": [
        "same(D(1/x + 1 - log(x)), -1/x**2 - 1/x)",
        "racine(1/x + 1 - log(x), 3.5, 3.6)",
        "same(D((2 - 2*x)*(log(x) - 2)), 2*(1/x + 1 - log(x)))",
        "en_racine(1/x + 1 - log(x), 3.5, 3.6, (2 - 2*x)*(log(x) - 2), 2*(1 - x)**2/x)",
        "close(D((2 - 2*x)*(log(x) - 2)).subs(x, 1), 4)",
        "same((2 - 2*x)*(log(x) - 2) - 4*(x - 1), (2 - 2*x)*log(x))",
        "same(D((2 - 2*x)*log(x), 2), -2/x - 2/x**2) and close(D((2 - 2*x)*log(x)).subs(x, 1), 0)",
        "integ((2 - 2*x)*log(x), 1, 2, -Rational(1, 2)) and integ((2 - 2*x)*(log(x) - 2), 1, 2, Rational(3, 2))",
    ],
    "bac-d-2017-sc-math-ex3": [
        "same(D((x + 2)*(1 + exp(-x))), 1 - (x + 1)*exp(-x)) and same(D((x + 2)*(1 + exp(-x)), 2), x*exp(-x))",
        "close(((x + 2)*(1 + exp(-x))).subs(x, -1), 1 + E)",
        "integ(2*exp(-x), -2, 0, 2*E**2 - 2) and integ(x*exp(-x), -2, 0, -E**2 - 1)",
        "integ((x + 2)*exp(-x), -2, 0, E**2 - 3)",
        "same(D((x + 2)*exp(-x)), -(x + 1)*exp(-x)) and close(((x + 2)*exp(-x)).subs(x, -1), E)",
    ],
    "bac-d-2017-sc-math-ex4": [
        "same(D(1 + x*log(x)), log(x) + 1) and close((1 + x*log(x)).subs(x, 1/E), 1 - 1/E)",
        "same((2*x - 1 + log(x))/(x - 1), 2 + 1/(x - 1) + log(x)/(x - 1))",
        "same(D((2*x - 1 + log(x))/(x - 1)), -(1 + x*log(x))/(x*(x - 1)**2))",
        "lim((2*x - 1 + log(x))/(x - 1), oo, 2) and lim((2*x - 1 + log(x))/(x - 1), 1, -oo, '-')",
        "racine((2*x - 1 + log(x))/(x - 1), 0.6, 0.8)",
        "close(((2*x - 1 + log(x))/(x - 1)).subs(x, 1/E), 2)",
    ],
    "bac-d-2015-sn-math-ex3": [
        "lim(3 - 2*log(x), 0, oo, '+')",
        "same(D(3*x - 3 - 2*x*log(x)), 1 - 2*log(x))",
        "close((3*x - 3 - 2*x*log(x)).subs(x, sqrt(E)), 2*sqrt(E) - 3)",
        "racine(3*x - 3 - 2*x*log(x), 2.3, 2.4)",
        "same(D(x**2/2 - x**2*log(x)), -2*x*log(x))",
        "same(D(2*x**2 - 3*x - x**2*log(x)), 3*x - 3 - 2*x*log(x))",
        "all(close(Integral(3*x - 3 - 2*x*log(x), (x, Rational(1, k), 1)).evalf(30), -1 + Rational(3, k) - Rational(2, k**2) - log(k)/k**2) for k in (1, 2, 5))",
    ],
    "bac-d-2015-sn-math-ex4": [
        "same(D((x - 2)*(1 + exp(x))), 1 + (x - 1)*exp(x)) and same(D((x - 2)*(1 + exp(x)), 2), x*exp(x))",
        "lim(1 + (x - 1)*exp(x), -oo, 1)",
        "close(((x - 2)*(1 + exp(x))).subs(x, 1), -1 - E)",
        "close(((x - 2)*exp(x)).subs(x, 1), -E)",
        "integ(x - 2 - 2*exp(x), 0, 2, -2*E**2) and integ(x*exp(x), 0, 2, E**2 + 1)",
        "integ(-(x - 2)*(1 + exp(x)), 0, 2, E**2 - 1)",
    ],
    "bac-d-2015-sc-math-ex3": [
        "same(D((2*x + 1)*exp(x) + 1), (2*x + 3)*exp(x))",
        "close(((2*x + 1)*exp(x) + 1).subs(x, -Rational(3, 2)), 1 - 2*exp(-Rational(3, 2)))",
        "same(D(x + 2 + (2*x - 1)*exp(x)), 1 + (2*x + 1)*exp(x))",
        "close((x + 2 + (2*x - 1)*exp(x)).subs(x, Rational(1, 2)), Rational(5, 2))",
        "racine(x + 2 + (2*x - 1)*exp(x), -0.85, -0.84)",
        "close((x + 2 + (2*x - 1)*exp(x)).subs(x, -Rational(1, 2)), Rational(3, 2) - 2*exp(-Rational(1, 2)))",
        "close(((2*x - 1)*exp(x)).subs(x, -Rational(1, 2)), -2*exp(-Rational(1, 2)))",
    ],
    "bac-d-2015-sc-math-ex4": [
        "racine(2*x**2 + log(x), 0.54, 0.55)",
        "same(D(2*x - (1 + log(x))/x), (2*x**2 + log(x))/x**2)",
        "en_racine(2*x**2 + log(x), 0.54, 0.55, 2*x - (1 + log(x))/x, (4*x**2 - 1)/x)",
        "abs(float(((4*x**2 - 1)/x).subs(x, root_in(2*x**2 + log(x), 0.54, 0.55))) - 0.369) < 0.001",
        "close((2*x - (1 + log(x))/x).subs(x, 1/E), 2/E) and close(D(2*x - (1 + log(x))/x).subs(x, 1/E), 2 - E**2)",
        "same(D(x**2 - log(x) - log(x)**2/2), 2*x - (1 + log(x))/x)",
        "integ(2*x - (1 + log(x))/x, 1/E, 1, Rational(1, 2) - exp(-2))",
    ],
    "bac-d-2016-sn-math-ex3": [
        "same(D(1 - x + exp(x)), -1 + exp(x)) and close((1 - x + exp(x)).subs(x, 0), 2)",
        "same(D(x - 1 + x*exp(-x)), (1 - x + exp(x))*exp(-x))",
        "solve(Eq(D(x - 1 + x*exp(-x)), 1), x) == [1]",
        "same(D(x**2/2 - x - (x + 1)*exp(-x)), x - 1 + x*exp(-x))",
        "integ(x*exp(-x), 1, 3, 2*exp(-1) - 4*exp(-3))",
    ],
    "bac-d-2016-sn-math-ex4": [
        "racine(x**3 - 2 + 4*log(x), 1.1, 1.2)",
        "same(D(x - 1 - 2*log(x)/x**2), (x**3 - 2 + 4*log(x))/x**3)",
        "en_racine(x**3 - 2 + 4*log(x), 1.1, 1.2, x - 1 - 2*log(x)/x**2, (3*x**3 - 2*x**2 - 2)/(2*x**2))",
        "close(D(x - 1 - 2*log(x)/x**2).subs(x, 1), -1)",
        "racine(x - 1 - 2*log(x)/x**2, 1.3, 1.4)",
        "same((2*x**3 - (3 + 1)*x**2 - 2*log(x))/x**2, (x - 1 - 2*log(x)/x**2) - (-x + 3))",
        "close((2*x - 1 - 2*log(x)/x**2).subs(x, 1), 1) and same(D(2*x - 1 - 2*log(x)/x**2), (2*x**3 - 2 + 4*log(x))/x**3)",
        "en_racine(x - 1 - 2*log(x)/x**2, 1.3, 1.4, -Integral(t - 1 - 2*log(t)/t**2, (t, 1, x)).doit(), -Rational(3, 2)*x**2 + 2*x + Rational(3, 2) - 2/x)",
        "same(Integral(log(t)/t**2, (t, 1, x)).doit(), -log(x)/x - 1/x + 1)",
    ],
    "bac-d-2016-sc-math-ex3": [
        "same(x*exp(x) - exp(x) + x - 1, (x - 1)*(exp(x) + 1))",
        "same(D(x*exp(x) - exp(x) + x - 1), x*exp(x) + 1) and same(D(x*exp(x) - exp(x) + x - 1, 2), (x + 1)*exp(x))",
        "close((x*exp(x) + 1).subs(x, -1), 1 - exp(-1))",
        "same(D((x - 2)*exp(x) + x**2/2 - x - 1), x*exp(x) - exp(x) + x - 1)",
        "integ(-(x*exp(x) - exp(x) + x - 1), 0, 1, E - Rational(3, 2))",
    ],
    "bac-d-2016-sc-math-ex4": [
        "same(D(x - 2 - log(x)), (x - 1)/x)",
        "same((1 - 1/E)*(x - E) + E - 3, (1 - 1/E)*x - 2)",
        "racine(x - 2 - log(x), 0.1, 0.2) and racine(x - 2 - log(x), 3.1, 3.2)",
        "close(1/D(x - 2 - log(x)).subs(x, E), E/(E - 1))",
        "integ(log(x), 1, E, 1)",
        "integ(-(x - 2 - log(x)), 1, E, 2*E - E**2/2 - Rational(1, 2))",
    ],
}
