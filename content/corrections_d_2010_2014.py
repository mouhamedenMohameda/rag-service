"""Corrections des exercices de maths série D 2010-2014.

Les énoncés sont ceux de ``enonces_d_2010_2014`` (retranscrits et vérifiés sur
les PDF officiels). Chaque correction a été rédigée puis contrôlée :
  - calculs refaits par calcul formel (sympy) — voir CHECKS en fin de fichier ;
  - réponses comparées au corrigé officiel quand il existe ; quand le corrigé
    officiel se trompe, la correction donne la vraie réponse et le signale ;
  - contrôle automatique (scripts/check_content.py) : 0 erreur.

Chargé par ``scripts/load_corrections.py corrections_d_2010_2014`` :
un exercice validé par l'admin n'est jamais modifié.
"""
from enonces_d_2010_2014 import ENONCES as _E

CORRECTIONS: dict[str, dict] = {}


def _add(eid: str, correction: str, note: str = "") -> None:
    CORRECTIONS[eid] = {"enonce": _E[eid]["enonce"], "correction": correction.strip() + "\n", "note": note}


# ═════════════════════════════ 2010 — session normale ═════════════════════════

_add("bac-d-2010-sn-math-ex1", r"""
| N° question | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Réponse exacte | A | A | B | C | C |

**1)** Le tableau n'est pas défini en $-2$ (double barre) et l'est en $1$ : $D_f = \mathbb{R}\setminus\{-2\}$. **Réponse A.**

**2)** Sur chacun des trois intervalles, $f$ est continue et strictement monotone et $0$ est compris entre les valeurs extrêmes :
- sur $]-\infty;-2[$, $f$ croît de $-3$ à $+\infty$ ;
- sur $]-2;1]$, $f$ décroît de $+\infty$ à $-4$ ;
- sur $[1;+\infty[$, $f$ croît de $-4$ à $+\infty$.

Donc $f(x) = 0$ a exactement une solution sur chaque intervalle, soit 3 solutions. **Réponse A.**

**3)** $\lim\limits_{x \to -2} f(x) = +\infty$ : la droite d'équation $x = -2$ est asymptote. **Réponse B.** (L'autre asymptote, $y = -3$ en $-\infty$, n'est pas proposée.)

**4)** $D_f$ n'est pas symétrique par rapport à $0$ ($2 \in D_f$ mais $-2 \notin D_f$) : $f$ n'est ni paire ni impaire. **Réponse C.**

**5)** $f'(1) = 0$ et $f(1) = -4$ : la tangente est horizontale, d'équation $y = -4$. **Réponse C.**
""")

_add("bac-d-2010-sn-math-ex2", r"""
**1°) a)** $p(3) = 27 - 9 - 12 - 6 = 0$.

**b)** $(z - 3)(z^2 + az + b) = z^3 + (a - 3)z^2 + (b - 3a)z - 3b$. Par identification : $a - 3 = -1$, $b - 3a = -4$ et $-3b = -6$, d'où $a = 2$ et $b = 2$ (on vérifie $2 - 6 = -4$).

$$p(z) = (z - 3)(z^2 + 2z + 2).$$

**c)** $z^2 + 2z + 2 = 0$ : $\Delta = 4 - 8 = -4 = (2i)^2$, d'où $z = \dfrac{-2 \pm 2i}{2} = -1 \pm i$.

$$S = \{3 ;\ -1 + i ;\ -1 - i\}.$$

**2°) a)** On place $A(3;2)$, $B(-1;1)$, $C(-1;-1)$ et $D(3;0)$ : l'abscisse est la partie réelle de l'affixe, l'ordonnée sa partie imaginaire.

**b)** Milieu de $[AC]$ : $\dfrac{z_A + z_C}{2} = \dfrac{3 + 2i - 1 - i}{2} = 1 + \dfrac{1}{2}i$.

Milieu de $[BD]$ : $\dfrac{z_B + z_D}{2} = \dfrac{-1 + i + 3}{2} = 1 + \dfrac{1}{2}i$.

Les deux milieux ont la même affixe.

**c)** Les diagonales $[AC]$ et $[BD]$ ont le même milieu : $ABCD$ est un **parallélogramme**.

(Ce n'est ni un rectangle ni un losange : $AB = |z_B - z_A| = |-4 - i| = \sqrt{17}$ et $AD = |z_D - z_A| = |-2i| = 2$ sont différents, et $\overrightarrow{AB} \cdot \overrightarrow{AD} = (-4)(0) + (-1)(-2) = 2 \neq 0$.)

**d)** $|z - 3| = |z + 1 - i| \iff |z - z_D| = |z - z_B| \iff MD = MB$.

L'ensemble cherché est la **médiatrice du segment $[BD]$**.

Avec $z = x + iy$ : $(x - 3)^2 + y^2 = (x + 1)^2 + (y - 1)^2 \iff -6x + 9 = 2x - 2y + 2 \iff y = 4x - \dfrac{7}{2}$.

C'est la droite passant par le milieu $\left(1;\dfrac{1}{2}\right)$ de $[BD]$, perpendiculaire à $(BD)$.
""")

_add("bac-d-2010-sn-math-ex3", r"""
**1. a)** $U_1 = \dfrac{1 + 1 + 1}{1 \times 2} = \dfrac{3}{2}$, $U_2 = \dfrac{4 + 2 + 1}{2 \times 3} = \dfrac{7}{6}$, $U_3 = \dfrac{9 + 3 + 1}{3 \times 4} = \dfrac{13}{12}$.

**b)** $U_2 - U_1 = -\dfrac{1}{3}$ et $U_3 - U_2 = -\dfrac{1}{12}$ : ces différences ne sont pas égales, donc $(U_n)$ n'est pas arithmétique.

$\dfrac{U_2}{U_1} = \dfrac{7}{9}$ et $\dfrac{U_3}{U_2} = \dfrac{13}{14}$ : ces quotients ne sont pas égaux, donc $(U_n)$ n'est pas géométrique.

$U_n = \dfrac{n(n + 1) + 1}{n(n + 1)} = 1 + \dfrac{1}{n(n + 1)}$ et $\lim\limits_{n \to +\infty} \dfrac{1}{n(n + 1)} = 0$, donc $(U_n)$ converge vers $1$.

**2°) a)** $V_n = \dfrac{n^2 - 1}{n} = n - \dfrac{1}{n}$, donc
$$V_{n+1} - V_n = (n + 1) - \dfrac{1}{n + 1} - n + \dfrac{1}{n} = 1 + \dfrac{1}{n} - \dfrac{1}{n + 1} = 1 + \dfrac{1}{n(n + 1)} = U_n.$$

**b)** Les termes se simplifient deux à deux (somme télescopique) :
$$S_n = (V_2 - V_1) + (V_3 - V_2) + \dots + (V_{n+1} - V_n) = V_{n+1} - V_1.$$

Comme $V_1 = 0$ : $S_n = V_{n+1} = \dfrac{(n + 1)^2 - 1}{n + 1} = \dfrac{n(n + 2)}{n + 1}$.

**3)** Pour $n \ge 2$, $V_n = \dfrac{(n - 1)(n + 1)}{n} > 0$, donc $W_n$ est bien défini, et
$$S'_n = \ln V_2 + \dots + \ln V_n = \ln\left(\prod_{k=2}^{n} \dfrac{(k - 1)(k + 1)}{k}\right).$$

Or $\displaystyle\prod_{k=2}^{n}(k - 1) = (n - 1)!$, $\displaystyle\prod_{k=2}^{n}(k + 1) = \dfrac{(n + 1)!}{2}$ et $\displaystyle\prod_{k=2}^{n} k = n!$.

Donc $S'_n = \ln\left[\dfrac{(n - 1)!\,(n + 1)!}{2\,n!}\right] = \ln\left[\dfrac{(n + 1)!}{2n}\right]$, car $\dfrac{(n - 1)!}{n!} = \dfrac{1}{n}$.
""")

_add("bac-d-2010-sn-math-ex4", r"""
**1. a)** $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$ ; $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $f(x) - (x + 2) = e^x$ et $\lim\limits_{x \to -\infty} e^x = 0$ : la droite $(\Delta) : y = x + 2$ est **asymptote oblique** à $(C)$ en $-\infty$. Comme $e^x > 0$, $(C)$ est au-dessus de $(\Delta)$.

$\dfrac{f(x)}{x} = 1 + \dfrac{2}{x} + \dfrac{e^x}{x}$ et $\lim\limits_{x \to +\infty} \dfrac{e^x}{x} = +\infty$, donc $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$ : $(C)$ admet en $+\infty$ une **branche parabolique de direction $(Oy)$**.

**2)** $f'(x) = 1 + e^x > 0$ : $f$ est strictement croissante sur $\mathbb{R}$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $+\infty$ |

**3°)** $f$ est continue et strictement croissante sur $\mathbb{R}$ : elle réalise une bijection de $\mathbb{R}$ sur $J = \left]\lim\limits_{-\infty} f ; \lim\limits_{+\infty} f\right[ = \mathbb{R}$.

**4°)** $0 \in J$, donc l'équation $f(x) = 0$ admet une unique solution $\alpha$.

$f(-2{,}5) = -0{,}5 + e^{-2{,}5} \approx -0{,}418 < 0$ et $f(-2) = e^{-2} \approx 0{,}135 > 0$, donc $-2{,}5 < \alpha < -2$ (en fait $\alpha \approx -2{,}12$).

**5°)** $(C)$ passe par $(0;3)$ et $(\alpha;0)$, admet l'asymptote $y = x + 2$ en $-\infty$ et une branche parabolique verticale en $+\infty$.

$(C')$ est la symétrique de $(C)$ par rapport à la droite $y = x$ : elle passe par $(3;0)$ et $(0;\alpha)$, admet l'asymptote $y = x - 2$ en $-\infty$ et une branche parabolique de direction $(Ox)$ en $+\infty$.

**6. a)** Les primitives de $f$ sont $x \mapsto \dfrac{x^2}{2} + 2x + e^x + c$. $F(0) = 1 + c = 0$ donne $c = -1$ :
$$F(x) = \dfrac{x^2}{2} + 2x + e^x - 1.$$

**b)** Sur $[\alpha;0]$, $f$ est croissante et $f(\alpha) = 0$, donc $f \ge 0$ et
$$A(\alpha) = \int_\alpha^0 f(x)\,dx = F(0) - F(\alpha) = -\left(\dfrac{\alpha^2}{2} + 2\alpha + e^\alpha - 1\right) \text{ u.a.}$$

Comme $f(\alpha) = 0$, $e^\alpha = -\alpha - 2$, d'où
$$A(\alpha) = -\left(\dfrac{\alpha^2}{2} + 2\alpha - \alpha - 2 - 1\right) = -\dfrac{\alpha^2}{2} - \alpha + 3 = \dfrac{6 - 2\alpha - \alpha^2}{2} \text{ cm}^2.$$

(Numériquement, $A(\alpha) \approx 2{,}87$ cm².)

**7. a)** $(T) : y = f'(\alpha)(x - \alpha) + f(\alpha)$ avec $f(\alpha) = 0$ et $f'(\alpha) = 1 + e^\alpha = 1 - \alpha - 2 = -(\alpha + 1)$ :
$$(T) : y = -(\alpha + 1)(x - \alpha).$$

**b)** $f(\alpha) = 0$ et $f'(\alpha) \neq 0$, donc $f^{-1}$ est dérivable en $0$ et
$$\left(f^{-1}\right)'(0) = \dfrac{1}{f'(\alpha)} = \dfrac{1}{-(\alpha + 1)} = \dfrac{-1}{\alpha + 1}.$$

**8) a)** $g(x)$ existe si et seulement si $f(x) > 0$. Comme $f$ est strictement croissante et $f(\alpha) = 0$ : $f(x) > 0 \iff x > \alpha$.
$$D_g = ]\alpha;+\infty[.$$

**b)** $g'(x) = \dfrac{f'(x)}{f(x)} = \dfrac{1 + e^x}{x + 2 + e^x} > 0$ sur $D_g$ : $g$ est strictement croissante.

$\lim\limits_{x \to \alpha^+} f(x) = 0^+$ donc $\lim\limits_{x \to \alpha^+} g(x) = -\infty$ ; $\lim\limits_{x \to +\infty} g(x) = +\infty$.

| $x$ | $\alpha$ | | $+\infty$ |
|---|---|---|---|
| $g'(x)$ | ‖ | $+$ | |
| $g(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ |

**c)** Éléments pour le tracé de $(\Gamma)$ :
- la droite $x = \alpha$ est asymptote verticale ;
- $g(0) = \ln 3 \approx 1{,}10$ ;
- $g(x) = 0 \iff f(x) = 1 \iff x + 1 + e^x = 0$, de solution $x \approx -1{,}28$ ;
- $g(x) - x = \ln\big(1 + (x + 2)e^{-x}\big) \xrightarrow[x \to +\infty]{} 0$ : la droite $y = x$ est asymptote à $(\Gamma)$ en $+\infty$, et $(\Gamma)$ est au-dessus.
""")

# ═════════════════════════ 2010 — session complémentaire ══════════════════════

_add("bac-d-2010-sc-math-ex1", r"""
| Question | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | B | A | B | C | C | (voir ci-dessous) |

**1)** $U_{10} = U_5 + 5r = 17 + 15 = 32$. **Réponse B.**

**2)** $U_0 + \dots + U_n = (n + 1)\dfrac{U_0 + U_n}{2} = (n + 1)\dfrac{11 + 10n}{2}$. Pour $n = 19$ : $20 \times \dfrac{201}{2} = 2010$. Comme la somme augmente avec $n$, c'est la seule valeur. **Réponse A.**

**3)** Somme de termes d'une suite géométrique de raison $2$ : $S_n = \dfrac{2^{n+1} - 1}{2 - 1} = 2^{n+1} - 1$. **Réponse B.**

**4)** $|U_n| = \dfrac{1}{|(-1)^n + n^2|} \le \dfrac{1}{n^2 - 1}$ pour $n \ge 2$, qui tend vers $0$ : $(U_n)$ converge vers $0$. **Réponse C.**

**5)** $\dfrac{U_{n+1}}{U_n} = \dfrac{10}{n + 1}$ (termes positifs) : ce quotient est $> 1$ pour $n < 9$, égal à $1$ pour $n = 9$ et $< 1$ pour $n > 9$. La suite croît jusqu'au rang 9, puis décroît : elle est **non monotone**. **Réponse C.**

**6)** Telle qu'elle est imprimée, aucune des trois réponses n'est vraie en général. Avec $U_n \le V_n$ et $(U_n)$ croissante, on sait seulement que $V_n \ge U_n \ge U_0$ : $(V_n)$ est **minorée**.
- A est fausse : $U_n = n$, $V_n = n + 1$ (alors $(U_n)$ n'est pas bornée).
- B est fausse : même exemple.
- C est fausse : $U_n = 0$, $V_n = 1$ ($(V_n)$ converge).

Le corrigé officiel retient **A** : c'est juste seulement si, en plus, $(V_n)$ est décroissante. On a alors $U_0 \le U_n \le V_n \le V_0$, donc $(U_n)$ est bornée (et $(V_n)$ aussi).
""", note="QCM Q6 : aucune réponse exacte telle qu'imprimée ; le corrigé officiel retient A (vrai seulement si (Vₙ) est en plus décroissante). La correction l'explique.")

_add("bac-d-2010-sc-math-ex2", r"""
**1.** $\Delta' = (-2)^2 - 13 = -9 = (3i)^2$, donc $z = 2 \pm 3i$ : $z_1 = 2 + 3i$ et $z_2 = 2 - 3i$.

**2. a)** $z_A = 1 + z_1 = 3 + 3i = 3\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$.

$z_B = i + z_2 = 2 - 2i = 2\sqrt{2}\left(\cos\left(-\dfrac{\pi}{4}\right) + i\sin\left(-\dfrac{\pi}{4}\right)\right)$.

**b)** On place $A(3;3)$ et $B(2;-2)$.

$\dfrac{z_A}{z_B} = \dfrac{3(1 + i)}{2(1 - i)} = \dfrac{3}{2}i$ : c'est un imaginaire pur, donc $(\overrightarrow{OB}, \overrightarrow{OA}) \equiv \dfrac{\pi}{2} \ [2\pi]$.

Le triangle $OAB$ est **rectangle en $O$** (il n'est pas isocèle : $OA = 3\sqrt{2}$ et $OB = 2\sqrt{2}$).

**c)** $OACB$ est un parallélogramme $\iff \overrightarrow{OA} = \overrightarrow{BC} \iff z_C - z_B = z_A \iff z_C = z_A + z_B = 5 + i$.

Comme l'angle en $O$ est droit, $OACB$ est même un **rectangle**.

**d)** $\dfrac{z - 2 + 2i}{z - 3 - 3i} = \dfrac{z - z_B}{z - z_A}$, défini pour $M \neq A$.

Ce nombre est imaginaire pur $\iff M = B$ ou $(\overrightarrow{MA}, \overrightarrow{MB}) \equiv \dfrac{\pi}{2} \ [\pi]$.

$\Gamma$ est le **cercle de diamètre $[AB]$ privé du point $A$** : centre $\left(\dfrac{5}{2};\dfrac{1}{2}\right)$, rayon $\dfrac{AB}{2} = \dfrac{|-1 - 5i|}{2} = \dfrac{\sqrt{26}}{2}$. Il passe par $O$ et par $C$ (angles droits en $O$ et en $C$).
""")

_add("bac-d-2010-sc-math-ex3", r"""
**1. a)** $f(x) = \dfrac{1 + x\ln x}{x}$ et $\lim\limits_{x \to 0^+} x\ln x = 0$, donc le numérateur tend vers $1$ et $\lim\limits_{x \to 0^+} f(x) = +\infty$.

La droite d'équation $x = 0$ (l'axe des ordonnées) est **asymptote verticale** à $(C)$.

**b)** $\lim\limits_{x \to +\infty} \dfrac{1}{x} = 0$ et $\lim\limits_{x \to +\infty} \ln x = +\infty$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$.

$f(x) - \ln x = \dfrac{1}{x}$, donc $\lim\limits_{x \to +\infty} \big(f(x) - \ln x\big) = 0$ : les courbes $(C)$ et $\Gamma$ sont **asymptotes** en $+\infty$, et $(C)$ est au-dessus de $\Gamma$ (car $\dfrac{1}{x} > 0$).

**2. a)** $f'(x) = -\dfrac{1}{x^2} + \dfrac{1}{x} = \dfrac{x - 1}{x^2}$.

**b)** $f'(x)$ a le signe de $x - 1$ ; $f(1) = 1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $1$ | ↗ | $+\infty$ |

**3. a)** $\ln'(x) = \dfrac{1}{x} > 0$ : $\ln$ est strictement croissante sur $]0;+\infty[$, de $-\infty$ (en $0^+$) à $+\infty$, et $\ln 1 = 0$.

**b)** $(C)$ a pour minimum le point $(1;1)$, l'asymptote $x = 0$ et se rapproche de $\Gamma$ par-dessus en $+\infty$. $\Gamma$ passe par $(1;0)$ et $(e;1)$.

**4. a)** Sur $I = ]1;+\infty[$, $h$ est continue et strictement croissante, donc elle réalise une bijection de $I$ sur
$$J = \left]\lim\limits_{x \to 1^+} h(x) ; \lim\limits_{x \to +\infty} h(x)\right[ = ]1;+\infty[.$$

**b)** $f'(1) = 0$ : $(C)$ a une tangente horizontale au point $(1;1)$. Par symétrie par rapport à $y = x$, $(C')$ a au point $(1;1)$ une (demi-)tangente **verticale**, d'équation $x = 1$.

$(C')$ est définie pour $x \in J = ]1;+\infty[$ : elle est entièrement **à droite** de cette tangente.

**c)** $(C')$ est la symétrique de la partie de $(C)$ située sur $]1;+\infty[$ par rapport à la droite $y = x$.

**5. a)** Par parties, avec $u = \ln x$ et $v' = 1$ ($u' = \dfrac{1}{x}$, $v = x$) :
$$A = \big[x\ln x\big]_1^e - \int_1^e 1\,dx = e - (e - 1) = 1.$$

**b)** Sur $[1;e]$, $f(x) \ge 1 > 0$, donc
$$S = \int_1^e \left(\dfrac{1}{x} + \ln x\right)dx = \big[\ln x\big]_1^e + A = 1 + 1 = 2 \text{ u.a.} = 2 \text{ cm}^2.$$
""", note="Le corrigé officiel écrit à tort, en 4. a), que h est décroissante de ]1;+∞[ sur ]0;1] : h est croissante et J = ]1;+∞[.")

_add("bac-d-2010-sc-math-ex4", r"""
**1. a)** $e^x - 1 > 0 \iff x > 0$.
- $\lim\limits_{x \to 0^+} f(x) = +\infty$ (numérateur $\to 1$, dénominateur $\to 0^+$) ;
- $\lim\limits_{x \to 0^-} f(x) = -\infty$ (dénominateur $\to 0^-$) ;
- $\lim\limits_{x \to -\infty} f(x) = \dfrac{0}{0 - 1} = 0$ ;
- $\lim\limits_{x \to +\infty} f(x) = \lim\limits_{x \to +\infty} \dfrac{1}{1 - e^{-x}} = 1$.

**b)** $(C)$ a trois asymptotes : la droite $x = 0$ (verticale), la droite $y = 0$ (horizontale en $-\infty$) et la droite $y = 1$ (horizontale en $+\infty$).

**2. a)** $f'(x) = \dfrac{e^x(e^x - 1) - e^x \cdot e^x}{(e^x - 1)^2} = \dfrac{-e^x}{(e^x - 1)^2} = -\dfrac{e^x}{e^x - 1} \times \dfrac{1}{e^x - 1} = -\dfrac{f(x)}{e^x - 1}$.

**b)** $f'(x) < 0$ sur $\mathbb{R}^*$ :

| $x$ | $-\infty$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | ‖ | $-$ | |
| $f(x)$ | $0$ | ↘ | $-\infty$ ‖ $+\infty$ | ↘ | $1$ |

**3. a)** Sur $I = ]0;+\infty[$, $g$ est continue et strictement décroissante : elle réalise une bijection de $I$ sur $J = ]1;+\infty[$.

**b)** Pour $x \in J$ et $t \in I$ : $g(t) = x \iff e^t = x(e^t - 1) \iff e^t(x - 1) = x \iff e^t = \dfrac{x}{x - 1}$ (avec $x > 1$).
$$g^{-1}(x) = \ln\left(\dfrac{x}{x - 1}\right), \quad x \in ]1;+\infty[.$$

**4. a)** Pour tout $x \neq 0$, on a $-x \neq 0$ et
$$f(-x) + f(x) = \dfrac{e^{-x}}{e^{-x} - 1} + \dfrac{e^x}{e^x - 1} = \dfrac{1}{1 - e^x} + \dfrac{e^x}{e^x - 1} = \dfrac{e^x - 1}{e^x - 1} = 1 = 2 \times \dfrac{1}{2}.$$

Donc $\Omega\left(0;\dfrac{1}{2}\right)$ est centre de symétrie de $(C)$.

**b)** $(C)$ : deux branches symétriques par rapport à $\Omega$, asymptotes $x = 0$, $y = 0$ et $y = 1$.

$(C')$ est la symétrique de la branche de droite par rapport à $y = x$ : asymptotes $x = 1$ (verticale) et $y = 0$ (en $+\infty$).

**5. a)** Sur $I$, $e^x - 1 > 0$ et $f = \dfrac{u'}{u}$ avec $u(x) = e^x - 1$ : $F(x) = \ln(e^x - 1)$ est une primitive de $f$.

**b)** $f > 0$ sur $I$, donc
$$U_n = \int_{1/n}^{1} f(x)\,dx = \ln(e - 1) - \ln\left(e^{1/n} - 1\right) \text{ u.a.}$$

**c)** $\lim\limits_{n \to +\infty} e^{1/n} - 1 = 0^+$, donc $\lim\limits_{n \to +\infty} \ln\left(e^{1/n} - 1\right) = -\infty$ et $\lim\limits_{n \to +\infty} U_n = +\infty$.

Interprétation : l'aire du domaine compris entre $(C)$, l'axe des abscisses et les droites $x = 0$ et $x = 1$ est infinie, à cause de l'asymptote verticale $x = 0$.
""")

# ═════════════════════════════ 2011 — session normale ═════════════════════════

_add("bac-d-2011-sn-math-ex1", r"""
| Question | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | A | C | B | B | A | B (voir ci-dessous) |

À chaque cours, le tirage se fait parmi 7 jetons équiprobables, et les 6 cours sont indépendants (le jeton est remis dans l'enveloppe). $X$ suit donc la **loi binomiale** de paramètres $n = 6$ et $p = \dfrac{4}{7}$.

**1)** $p(\text{garçon}) = \dfrac{3}{7}$. **Réponse A.**

**2)** $p(\text{fille}) = \dfrac{4}{7}$. **Réponse C.**

**3)** Sur 6 cours, le nombre de filles interrogées va de $0$ à $6$ : $X(\Omega) = \{0,1,\dots,6\}$. **Réponse B.**

**4)** « Exactement cinq garçons » sur 6 cours, c'est « exactement une fille » : $p(A) = C_6^5\left(\dfrac{3}{7}\right)^5\left(\dfrac{4}{7}\right)$. **Réponse B.**

**5)** L'événement contraire de $B$ est « aucune fille », c'est-à-dire 6 garçons : $p(B) = 1 - \left(\dfrac{3}{7}\right)^6$. **Réponse A.**

**6)** $E(X) = np = 6 \times \dfrac{4}{7} = \dfrac{24}{7} \approx 3{,}43$.

Cette valeur n'est pas proposée. Le corrigé officiel retient **B** ($3$), l'entier le plus proche du nombre moyen de filles interrogées. Retiens que l'espérance exacte est $\dfrac{24}{7}$.
""", note="QCM Q6 : E(X) = 24/7 ≈ 3,43 n'est pas proposé ; la correction donne B (3, entier le plus proche, choix du corrigé officiel) en le disant.")

_add("bac-d-2011-sn-math-ex2", r"""
**1. a)** $p(1) = 1 - 5 + 12 - 8 = 0$.

**b)** $(z - 1)(z^2 + az + b) = z^3 + (a - 1)z^2 + (b - a)z - b$. Par identification : $a - 1 = -5$ et $-b = -8$, d'où $a = -4$ et $b = 8$ (on vérifie $b - a = 12$).

$$p(z) = (z - 1)(z^2 - 4z + 8).$$

**c)** $z^2 - 4z + 8 = 0$ : $\Delta' = 4 - 8 = -4 = (2i)^2$, d'où $z = 2 \pm 2i$.

$$S = \{1 ;\ 2 + 2i ;\ 2 - 2i\}.$$

**2. a)**
- $|z_1| = 1$ et $\arg z_1 \equiv 0 \ [2\pi]$ ;
- $|z_2| = \sqrt{4 + 4} = 2\sqrt{2}$ et $z_2 = 2\sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right)$, donc $\arg z_2 \equiv \dfrac{\pi}{4} \ [2\pi]$ ;
- $z_3 = \overline{z_2}$, donc $|z_3| = 2\sqrt{2}$ et $\arg z_3 \equiv -\dfrac{\pi}{4} \ [2\pi]$.

**b)** On place $A(1;0)$, $B(2;2)$ et $C(2;-2)$.

**3. a)** $\dfrac{z_2}{z_3} = \dfrac{2 + 2i}{2 - 2i} = \dfrac{1 + i}{1 - i} = \dfrac{(1 + i)^2}{2} = \dfrac{2i}{2} = i$.

Donc $\left|\dfrac{z_2}{z_3}\right| = 1$, soit $OB = OC$, et $(\overrightarrow{OC}, \overrightarrow{OB}) \equiv \arg i = \dfrac{\pi}{2} \ [2\pi]$.

Le triangle $OBC$ est **rectangle isocèle en $O$**.

**b)** Pour $z \neq 2 + 2i$ : $\left|\dfrac{z - 1}{z - 2 - 2i}\right| = 1 \iff |z - z_1| = |z - z_2| \iff MA = MB$.

$\Gamma$ est la **médiatrice du segment $[AB]$**.

Avec $z = x + iy$ : $(x - 1)^2 + y^2 = (x - 2)^2 + (y - 2)^2 \iff 2x + 4y - 7 = 0$, droite passant par le milieu $\left(\dfrac{3}{2};1\right)$ de $[AB]$.
""")

_add("bac-d-2011-sn-math-ex3", r"""
**1.** $\lim\limits_{x \to -\infty} xe^x = 0$ et $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = 0$ : l'axe des abscisses ($y = 0$) est **asymptote** à $(C)$ en $-\infty$.

$\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \dfrac{x + 2}{x}e^x$, donc $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$ : $(C)$ a une **branche parabolique de direction $(Oy)$** en $+\infty$.

**2.** $f'(x) = e^x + (x + 2)e^x = (x + 3)e^x$, du signe de $x + 3$. $f(-3) = -e^{-3} \approx -0{,}05$.

| $x$ | $-\infty$ | | $-3$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $0$ | ↘ | $-e^{-3}$ | ↗ | $+\infty$ |

**3.** Avec l'axe des ordonnées : $f(0) = 2$, point $(0;2)$.

Avec l'axe des abscisses : $f(x) = 0 \iff x + 2 = 0$ (car $e^x > 0$), point $(-2;0)$.

**4. a)** $f(x) + e^x = (x + 2)e^x + e^x = (x + 3)e^x = f'(x)$.

Donc $f(x) = f'(x) - e^x$, et $F(x) = f(x) - e^x = (x + 1)e^x$ est une primitive de $f$ sur $\mathbb{R}$.

**b)** Le domaine est compris entre $x = -2$ et $x = 0$, où $f(x) \ge 0$ :
$$S = \int_{-2}^{0} f(x)\,dx = F(0) - F(-2) = 1 - (-e^{-2}) = 1 + e^{-2} \approx 1{,}14 \text{ cm}^2.$$

**5. a)** $U_1 = f(1) = 3e$ et $U_2 = f\left(\dfrac{1}{2}\right) = \dfrac{5}{2}\sqrt{e}$.

La suite $\left(\dfrac{1}{n}\right)$ est décroissante et ses termes sont dans $]0;1]$, intervalle où $f$ est croissante. Donc, pour $n \ge 1$ : $\dfrac{1}{n + 1} < \dfrac{1}{n} \Rightarrow f\left(\dfrac{1}{n + 1}\right) < f\left(\dfrac{1}{n}\right)$, soit $U_{n+1} < U_n$ : $(U_n)$ est **décroissante**.

**b)** $\lim\limits_{n \to +\infty} \dfrac{1}{n} = 0$ et $f$ est continue en $0$, donc $\lim\limits_{n \to +\infty} U_n = f(0) = 2$.
""")

_add("bac-d-2011-sn-math-ex4", r"""
**1. a)** $\dfrac{1 + \ln x}{x} = \dfrac{1}{x}(1 + \ln x)$ avec $\lim\limits_{x \to 0^+} \dfrac{1}{x} = +\infty$ et $\lim\limits_{x \to 0^+}(1 + \ln x) = -\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$.

La droite $x = 0$ est **asymptote verticale** à $(C)$.

**b)** $\lim\limits_{x \to +\infty} \dfrac{1}{x} = 0$ et $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et
$$\lim\limits_{x \to +\infty} \big(f(x) - (x - 1)\big) = \lim\limits_{x \to +\infty} \dfrac{1 + \ln x}{x} = 0.$$

La droite $\Delta : y = x - 1$ est **asymptote oblique** à $(C)$ en $+\infty$.

**c)** $f(x) - (x - 1) = \dfrac{1 + \ln x}{x}$ a le signe de $1 + \ln x$ (car $x > 0$), qui s'annule pour $x = \dfrac{1}{e}$ :
- sur $\left]0;\dfrac{1}{e}\right[$, $(C)$ est **au-dessous** de $\Delta$ ;
- sur $\left]\dfrac{1}{e};+\infty\right[$, $(C)$ est **au-dessus** de $\Delta$ ;
- elles se coupent au point $\left(\dfrac{1}{e};\dfrac{1}{e} - 1\right)$.

**2. a)** $g\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{1}{2} - \ln\left(2^{-1/2}\right) = \dfrac{1}{2} + \dfrac{\ln 2}{2} = \dfrac{1 + \ln 2}{2}$.

**b)** $g'(x) = 2x - \dfrac{1}{x} = \dfrac{2x^2 - 1}{x}$.

**c)** Sur $]0;+\infty[$, $g'(x)$ a le signe de $2x^2 - 1$ : négatif sur $\left]0;\dfrac{1}{\sqrt{2}}\right]$, positif sur $\left[\dfrac{1}{\sqrt{2}};+\infty\right[$.

| $x$ | $0$ | | $\frac{1}{\sqrt{2}}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $g(x)$ | ‖ $+\infty$ | ↘ | $\frac{1 + \ln 2}{2}$ | ↗ | $+\infty$ |

Le minimum de $g$ est $\dfrac{1 + \ln 2}{2} > 0$, donc $g(x) > 0$ pour tout $x > 0$.

**3. a)** $f'(x) = 1 + \dfrac{\frac{1}{x} \cdot x - (1 + \ln x)}{x^2} = 1 - \dfrac{\ln x}{x^2} = \dfrac{x^2 - \ln x}{x^2} = \dfrac{g(x)}{x^2}$.

**b)** $f'(x) > 0$ : $f$ est strictement croissante sur $]0;+\infty[$, de $-\infty$ à $+\infty$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ |

**4. a)** $f$ est continue et strictement croissante sur $]0;+\infty[$ : elle réalise une bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**b)** $0 \in J$, donc l'équation $f(x) = 0$ a une unique solution $\alpha$.

$f\left(\dfrac{1}{e}\right) = \dfrac{1}{e} - 1 + 0 \approx -0{,}63 < 0$ et $f\left(\dfrac{1}{2}\right) = -\dfrac{1}{2} + 2(1 - \ln 2) = \dfrac{3}{2} - 2\ln 2 \approx 0{,}11 > 0$.

Donc $\dfrac{1}{e} < \alpha < \dfrac{1}{2}$ (en fait $\alpha \approx 0{,}472$).

**5. a)** La tangente est parallèle à $\Delta$ (coefficient directeur $1$) $\iff f'(x) = 1 \iff \ln x = 0 \iff x = 1$.

$f(1) = 1$ : c'est le point $(1;1)$, et la tangente y a pour équation $(T) : y = x$.

**b)** On trace $\Delta$, $(T)$, l'asymptote $x = 0$, le point $\left(\dfrac{1}{e};\dfrac{1}{e} - 1\right)$ commun à $(C)$ et $\Delta$, le point $(\alpha;0)$ et le point de contact $(1;1)$.

**c)** Pour $x > 0$ :
$$(m + 1)x - 1 - \ln x = 0 \iff m + 1 = \dfrac{1 + \ln x}{x} \iff f(x) - (x - 1) = m + 1 \iff f(x) = x + m.$$

Les solutions sont les abscisses des points communs à $(C)$ et à la droite $D_m : y = x + m$, parallèle à $\Delta$.

La fonction $h(x) = \dfrac{1 + \ln x}{x}$ a pour dérivée $h'(x) = -\dfrac{\ln x}{x^2}$ : elle croît de $-\infty$ à $h(1) = 1$ sur $]0;1]$, puis décroît de $1$ vers $0$ (sans l'atteindre) sur $[1;+\infty[$. Donc :
- si $m > 0$ : **aucune solution** ($D_m$ est au-dessus de $(T)$) ;
- si $m = 0$ : **une solution**, $x = 1$ ($D_0 = (T)$ est tangente) ;
- si $-1 < m < 0$ : **deux solutions** ($D_m$ est entre $\Delta$ et $(T)$) ;
- si $m \le -1$ : **une solution**, dans $\left]0;\dfrac{1}{e}\right]$ ($D_m$ est $\Delta$ ou au-dessous).

**6. a)** Pour $x \ge 1$, $1 + \ln x > 0$, donc $(C)$ est au-dessus de $\Delta$ et
$$U_n = \int_n^{n+1} \dfrac{1 + \ln x}{x}\,dx = \left[\ln x + \dfrac{(\ln x)^2}{2}\right]_n^{n+1} = \ln\left(\dfrac{n + 1}{n}\right) + \dfrac{\big(\ln(n + 1)\big)^2 - (\ln n)^2}{2} \text{ cm}^2.$$

**b)** $\ln\left(\dfrac{n + 1}{n}\right) = \ln\left(1 + \dfrac{1}{n}\right) \to 0$.

De plus $\big(\ln(n + 1)\big)^2 - (\ln n)^2 = \ln\left(1 + \dfrac{1}{n}\right)\big(\ln(n + 1) + \ln n\big)$, avec $0 < \ln\left(1 + \dfrac{1}{n}\right) \le \dfrac{1}{n}$. Ce produit est donc compris entre $0$ et $\dfrac{2\ln(n + 1)}{n}$, qui tend vers $0$.

Donc $\lim\limits_{n \to +\infty} U_n = 0$ : l'aire entre $(C)$ et $\Delta$ sur une bande de largeur $1$ tend vers $0$, car $(C)$ se rapproche de son asymptote.
""")

# ═════════════════════════ 2011 — session complémentaire ══════════════════════

_add("bac-d-2011-sc-math-ex1", r"""
| Question | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | B | B | B | A | (aucune, voir 5) | (aucune, voir 6) |

**1)** $\dfrac{f(4 - x) + f(x)}{2} = 4$ : les points d'abscisses $x$ et $4 - x$ de $(C)$ sont symétriques par rapport à $\Omega(2;4)$, centre de symétrie de $(C)$. **Réponse B.**

**2)** $\lim\limits_{x \to +\infty} f(x) = 5$ : la droite $y = 5$ est asymptote horizontale. **Réponse B.**

**3)** En posant $x = 4 - t$ : $f(x) = 8 - f(t)$ et $t \to +\infty$ quand $x \to -\infty$, donc $\lim\limits_{x \to -\infty} f(x) = 8 - 5 = 3$. **Réponse B.**

**4)** Si $x_1 < x_2 \le 2$, alors $4 - x_1 > 4 - x_2 \ge 2$, donc $f(4 - x_1) > f(4 - x_2)$, c'est-à-dire $8 - f(x_1) > 8 - f(x_2)$, soit $f(x_1) < f(x_2)$. Donc $f$ est aussi croissante sur $]-\infty;2]$, donc croissante sur $\mathbb{R}$. **Réponse A.**

**5)** $p(X \ge 75) = \dfrac{11 + 4 + 1}{20} = \dfrac{16}{20} = \dfrac{4}{5}$.

Cette valeur n'est pas proposée. La réponse C, $\dfrac{3}{4} = \dfrac{1 + 3 + 11}{20}$, est la probabilité d'avoir **au plus** 75 cl. Le sujet a sans doute voulu écrire « au plus ».

**6)** $E(X) = \dfrac{74{,}8 \times 1 + 74{,}9 \times 3 + 75 \times 11 + 75{,}1 \times 4 + 75{,}2 \times 1}{20} = \dfrac{1500{,}1}{20} = 75{,}005$.

Aucune réponse proposée n'est exacte. La plus proche est **A** ($75{,}001$).

*Attention :* le corrigé officiel donne A à la question 2 et C à la question 4. Les bonnes réponses sont **B** et **A**, démontrées ci-dessus.
""", note="QCM : Q5 et Q6 sans réponse exacte (4/5 et 75,005) ; le corrigé officiel se trompe aussi en Q2 (A au lieu de B) et Q4 (C au lieu de A). La correction donne la vérité.")

_add("bac-d-2011-sc-math-ex2", r"""
**1. a)** $f(a) = (1 + i)^2 - 2(1 + i) = 2i - 2 - 2i = -2$.

$f(b) = (1 + i\sqrt{3})^2 - 2(1 + i\sqrt{3}) = 1 - 3 + 2i\sqrt{3} - 2 - 2i\sqrt{3} = -4$.

**b)** $z^2 - 2z + 2 = 0 \iff f(z) = -2$ : $a = 1 + i$ est solution. Les coefficients sont réels, donc $\overline{a} = 1 - i$ l'est aussi.
$$S_1 = \{1 + i ;\ 1 - i\}.$$

$z^2 - 2z + 4 = 0 \iff f(z) = -4$ : de même, $b$ et $\overline{b}$ sont solutions.
$$S_2 = \{1 + i\sqrt{3} ;\ 1 - i\sqrt{3}\}.$$

**2. a)** $a = \sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right) = \sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right) = \sqrt{2}\,e^{i\frac{\pi}{4}}$.

$b = 2\left(\dfrac{1}{2} + i\dfrac{\sqrt{3}}{2}\right) = 2\left(\cos\dfrac{\pi}{3} + i\sin\dfrac{\pi}{3}\right) = 2e^{i\frac{\pi}{3}}$.

**b)** $c = (1 + i)(1 + i\sqrt{3}) = 1 + i\sqrt{3} + i - \sqrt{3} = (1 - \sqrt{3}) + i(1 + \sqrt{3})$.

$c = \sqrt{2}e^{i\frac{\pi}{4}} \times 2e^{i\frac{\pi}{3}} = 2\sqrt{2}\,e^{i\frac{7\pi}{12}}$.

**c)** En identifiant les deux écritures de $c$ : $2\sqrt{2}\cos\dfrac{7\pi}{12} = 1 - \sqrt{3}$ et $2\sqrt{2}\sin\dfrac{7\pi}{12} = 1 + \sqrt{3}$.
$$\cos\dfrac{7\pi}{12} = \dfrac{1 - \sqrt{3}}{2\sqrt{2}} = \dfrac{\sqrt{2} - \sqrt{6}}{4}, \qquad \sin\dfrac{7\pi}{12} = \dfrac{1 + \sqrt{3}}{2\sqrt{2}} = \dfrac{\sqrt{2} + \sqrt{6}}{4}.$$
""")

_add("bac-d-2011-sc-math-ex3", r"""
**1. a)** $U_2 = \dfrac{4}{4} = 1$, $U_3 = \dfrac{9}{8}$, $U_4 = \dfrac{16}{16} = 1$, $U_5 = \dfrac{25}{32}$.

**b)** $n^2 > 0$ et $2^n > 0$, donc $U_n > 0$.

$U_2 < U_3$ et $U_3 > U_4$ : la suite n'est ni croissante ni décroissante, elle est **non monotone**.

$U_3 - U_2 = \dfrac{1}{8}$ et $U_4 - U_3 = -\dfrac{1}{8}$ : elle n'est pas arithmétique.

$\dfrac{U_3}{U_2} = \dfrac{9}{8}$ et $\dfrac{U_4}{U_3} = \dfrac{8}{9}$ : elle n'est pas géométrique.

**2. a)** $\dfrac{U_{n+1}}{U_n} = \dfrac{(n + 1)^2}{2^{n+1}} \times \dfrac{2^n}{n^2} = \dfrac{1}{2}\left(\dfrac{n + 1}{n}\right)^2$.

**b)** Pour $n \ge 5$ : $1 < \dfrac{n + 1}{n} = 1 + \dfrac{1}{n} \le \dfrac{6}{5}$, donc
$$0 < \dfrac{U_{n+1}}{U_n} \le \dfrac{1}{2} \times \dfrac{36}{25} = \dfrac{18}{25} \le \dfrac{3}{4}.$$

**3. a)** Pour $n \ge 5$, $U_n > 0$ et $\dfrac{U_{n+1}}{U_n} < 1$, donc $U_{n+1} < U_n$ : $(U_n)$ est **décroissante à partir du rang 5**.

**b)** Elle est décroissante à partir du rang 5 et minorée par $0$ : elle est **convergente**.

**4. a)** Par récurrence sur $n \ge 5$, montrons que $0 < U_n \le \dfrac{25}{32}\left(\dfrac{3}{4}\right)^{n-5}$.
- Pour $n = 5$ : $U_5 = \dfrac{25}{32}$, il y a égalité.
- Si c'est vrai au rang $n$, alors $0 < U_{n+1} \le \dfrac{3}{4}U_n \le \dfrac{25}{32}\left(\dfrac{3}{4}\right)^{n+1-5}$ (d'après 2. b).

Pour $n \ge 6$, l'inégalité est stricte, car $\dfrac{U_{n+1}}{U_n} \le \dfrac{18}{25} < \dfrac{3}{4}$.

*Remarque :* le sujet écrit l'inégalité stricte « $<$ » dès $n = 5$. Elle est fausse pour $n = 5$, où il y a égalité. Elle est vraie pour $n \ge 6$.

**b)** $0 < \dfrac{3}{4} < 1$, donc $\lim\limits_{n \to +\infty}\left(\dfrac{3}{4}\right)^{n-5} = 0$. D'après le théorème des gendarmes : $\lim\limits_{n \to +\infty} U_n = 0$.
""", note="Question 4. a) : le sujet écrit 0 < Uₙ < (25/32)(3/4)ⁿ⁻⁵ dès n = 5 ; pour n = 5 il y a égalité. La correction le signale (inégalité stricte vraie pour n ≥ 6).")

_add("bac-d-2011-sc-math-ex4", r"""
**1.** $\lim\limits_{x \to 0^+} \ln x = -\infty$, donc $\lim\limits_{x \to 0^+} f(x) = -\infty$ : la droite $x = 0$ est **asymptote verticale**.

$\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = 2 - \dfrac{1}{x} + \dfrac{\ln x}{x}$, donc $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = 2$.

De plus $f(x) - 2x = -1 + \ln x \to +\infty$ : $(C)$ a en $+\infty$ une **branche parabolique de direction la droite $y = 2x$**.

**2. a)** $f'(x) = 2 + \dfrac{1}{x} > 0$ sur $]0;+\infty[$.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ |

**b)** $f$ est continue et strictement croissante sur $]0;+\infty[$ : elle réalise une bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**c)** $f^{-1}$ est définie sur $\mathbb{R}$, strictement croissante (même sens que $f$), à valeurs dans $]0;+\infty[$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f^{-1}(x)$ | $0$ | ↗ | $+\infty$ |

**3.** $0 \in J$ : l'équation $f(x) = 0$ a une unique solution $\alpha$.

$f(0{,}6) = 0{,}2 + \ln 0{,}6 \approx -0{,}31 < 0$ et $f(0{,}7) = 0{,}4 + \ln 0{,}7 \approx 0{,}04 > 0$, donc $0{,}6 < \alpha < 0{,}7$ ($\alpha \approx 0{,}687$).

**4. a)** Tangente parallèle à $y = 3x \iff f'(x) = 3 \iff \dfrac{1}{x} = 1 \iff x = 1$.

$f(1) = 1$ : c'est le point $(1;1)$, où la tangente a pour équation $y = 3x - 2$.

**b)** On trace l'asymptote $x = 0$, les points $(\alpha;0)$ et $(1;1)$ avec la tangente $y = 3x - 2$, et la branche parabolique de direction $y = 2x$.

**5. a)** Par parties, avec $u = \ln t$ et $v' = 1$ ($u' = \dfrac{1}{t}$, $v = t$) :
$$\int_\alpha^1 \ln t\,dt = \big[t\ln t\big]_\alpha^1 - \int_\alpha^1 dt = -\alpha\ln\alpha - (1 - \alpha) = \alpha - 1 - \alpha\ln\alpha.$$

Comme $f(\alpha) = 0$, $\ln\alpha = 1 - 2\alpha$, d'où $\displaystyle\int_\alpha^1 \ln t\,dt = \alpha - 1 - \alpha(1 - 2\alpha) = 2\alpha^2 - 1$.

**b)** Sur $[\alpha;1]$, $f(x) \ge 0$ ($f$ croissante, $f(\alpha) = 0$), donc l'aire vaut
$$\int_\alpha^1 (2x - 1)\,dx + \int_\alpha^1 \ln x\,dx = \big[x^2 - x\big]_\alpha^1 + 2\alpha^2 - 1 = (\alpha - \alpha^2) + 2\alpha^2 - 1 = \alpha^2 + \alpha - 1 \text{ cm}^2.$$

(Numériquement, environ $0{,}16$ cm².)

**6. a)** Pour tout réel $x$ : $f(e^x) = 2e^x - 1 + x = g(x)$, donc $g = f \circ \exp$.

$\exp$ est strictement croissante de $\mathbb{R}$ sur $]0;+\infty[$, et $f$ est strictement croissante sur $]0;+\infty[$ : $g$ est strictement croissante sur $\mathbb{R}$.

$\lim\limits_{x \to -\infty} g(x) = \lim\limits_{X \to 0^+} f(X) = -\infty$ et $\lim\limits_{x \to +\infty} g(x) = \lim\limits_{X \to +\infty} f(X) = +\infty$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $g(x)$ | $-\infty$ | ↗ | $+\infty$ |

**b)** $g(x) - (x - 1) = 2e^x \to 0$ en $-\infty$ : la droite $y = x - 1$ est **asymptote oblique** à $\Gamma$ en $-\infty$, et $\Gamma$ est au-dessus ($2e^x > 0$).

**c)** $\dfrac{g(x)}{x} = 1 - \dfrac{1}{x} + 2\dfrac{e^x}{x} \to +\infty$ en $+\infty$ : **branche parabolique de direction $(Oy)$**.

**d)** $g(x) = 0 \iff f(e^x) = 0 \iff e^x = \alpha \iff x = \ln\alpha$.

Le point d'intersection a pour abscisse $\ln\alpha = 1 - 2\alpha \approx -0{,}37$.

**e)** On trace l'asymptote $y = x - 1$, le point $(\ln\alpha;0)$ et le point $(0;g(0)) = (0;1)$.
""")

# ═════════════════════════════ 2012 — session normale ═════════════════════════

_add("bac-d-2012-sn-math-ex1", r"""
| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | A | B | B | A | B | C |

**1)** « Les deux lampes sont défaillantes » $= F \cap G$ : $p(F \cap G) = 0{,}1$. **Réponse A.**

**2)** « Au moins une est défaillante » $= F \cup G$ : $p(F \cup G) = p(F) + p(G) - p(F \cap G) = 0{,}2 + 0{,}3 - 0{,}1 = 0{,}4$. **Réponse B.**

**3)** « Les deux fonctionnent » est l'événement contraire de $F \cup G$ : $1 - 0{,}4 = 0{,}6$. **Réponse B.**

**4)** « Exactement une est défaillante » $= (F \cup G)$ privé de $(F \cap G)$ : $0{,}4 - 0{,}1 = 0{,}3$. **Réponse A.**

**5)** $p_G(\overline{F}) = \dfrac{p(\overline{F} \cap G)}{p(G)} = \dfrac{p(G) - p(F \cap G)}{p(G)} = \dfrac{0{,}3 - 0{,}1}{0{,}3} = \dfrac{2}{3}$. **Réponse B.**

**6)** $X \in \{0;1;2\}$ avec $p(X = 0) = 0{,}6$, $p(X = 1) = 0{,}3$ et $p(X = 2) = 0{,}1$ :
$$E(X) = 0 \times 0{,}6 + 1 \times 0{,}3 + 2 \times 0{,}1 = 0{,}5.$$
**Réponse C.**

*Attention :* le corrigé officiel donne B à la question 4 et A à la question 5. Les calculs ci-dessus montrent que les bonnes réponses sont **A** ($0{,}3$) et **B** ($\dfrac{2}{3}$).
""", note="Le corrigé officiel se trompe aux questions 4 (B au lieu de A) et 5 (A au lieu de B) ; la correction donne les bonnes réponses.")

_add("bac-d-2012-sn-math-ex2", r"""
**1. a)** $\Delta' = (-2)^2 - 5 = -1 = i^2$, donc $z = 2 \pm i$ : $z_1 = 2 + i$ et $z_2 = 2 - i$.

**b)** $z_3 = i + z_1 = 2 + 2i = 2\sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right) = 2\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$.

**2) a)** $z_A = 2 + i$ et $z_B = -1 - i + 2 - i = 1 - 2i$. On place $A(2;1)$ et $B(1;-2)$.

$\dfrac{z_A}{z_B} = \dfrac{2 + i}{1 - 2i} = \dfrac{(2 + i)(1 + 2i)}{5} = \dfrac{5i}{5} = i$.

Donc $OA = OB$ et $(\overrightarrow{OB}, \overrightarrow{OA}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $OAB$ est **rectangle isocèle en $O$**.

**b)** $OACB$ est un parallélogramme $\iff \overrightarrow{OA} = \overrightarrow{BC} \iff z_C = z_A + z_B = 3 - i$.

Avec 2) a), $OACB$ est même un **carré**.

**3) a)** $\omega = f(3 - i) = \dfrac{1 - 2i}{2 + i} = \dfrac{(1 - 2i)(2 - i)}{5} = \dfrac{-5i}{5} = -i$.

Comme $f(z) = \dfrac{z - z_A}{z - z_B}$ : $\dfrac{z_C - z_A}{z_C - z_B} = -i$. Donc $CA = CB$ et $(\overrightarrow{CB}, \overrightarrow{CA}) \equiv -\dfrac{\pi}{2} \ [2\pi]$ : le triangle $ACB$ est rectangle isocèle en $C$ (ce qui confirme que $OACB$ est un carré).

**b)** $|f(z)| = 1 \iff MA = MB$ : $\Gamma_1$ est la **médiatrice de $[AB]$**. Elle passe par $O$ et par $C$.

**c)** $f(z)$ est imaginaire pur $\iff M = A$ ou $(\overrightarrow{MB}, \overrightarrow{MA}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AB]$ privé de $B$**. Il passe par $O$ et par $C$.

**d)** $f(z) - 1 = \dfrac{(z - z_A) - (z - z_B)}{z - z_B} = \dfrac{z_B - z_A}{z - z_B} = \dfrac{-1 - 3i}{z - z_B}$, donc $|f(z) - 1| = \dfrac{\sqrt{10}}{MB}$.

$|f(z) - 1| = \sqrt{10} \iff MB = 1$ : $\Gamma_3$ est le **cercle de centre $B$ et de rayon $1$**.
""")

_add("bac-d-2012-sn-math-ex3", r"""
**1. a)** $\lim\limits_{x \to +\infty} e^{-2x-1} = 0$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \big(f(x) - (3x - 1)\big) = 0$.

La droite $(D) : y = 3x - 1$ est **asymptote oblique** à $(C)$ en $+\infty$, et $(C)$ est au-dessus de $(D)$ (car $e^{-2x-1} > 0$).

**b)** $\lim\limits_{x \to -\infty} e^{-2x-1} = +\infty$, donc $\lim\limits_{x \to -\infty} f(x) = +\infty$.

$\dfrac{f(x)}{x} = \dfrac{e^{-2x-1}}{x} + 3 - \dfrac{1}{x}$, et $\dfrac{e^{-2x-1}}{x} \to -\infty$ (numérateur $\to +\infty$, $x \to -\infty$). Donc $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = -\infty$ : **branche parabolique de direction $(Oy)$** en $-\infty$.

**2. a)** $f'(x) = -2e^{-2x-1} + 3$.

$f'(x) > 0 \iff e^{-2x-1} < \dfrac{3}{2} \iff -2x - 1 < \ln\dfrac{3}{2} \iff x > x_0$, avec $x_0 = -\dfrac{1 + \ln\frac{3}{2}}{2} \approx -0{,}70$.

$f'$ est négative sur $]-\infty;x_0[$, nulle en $x_0$, positive sur $]x_0;+\infty[$.

**b)** $f(x_0) = \dfrac{3}{2} + 3x_0 - 1 = -1 - \dfrac{3}{2}\ln\dfrac{3}{2} \approx -1{,}61$.

| $x$ | $-\infty$ | | $x_0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $+\infty$ | ↘ | $f(x_0) \approx -1{,}61$ | ↗ | $+\infty$ |

**3. a)** Sur $]-\infty;x_0]$, $f$ est continue et strictement décroissante de $+\infty$ à $f(x_0) < 0$ : l'équation $f(x) = 0$ a une unique solution $\alpha$. De même sur $[x_0;+\infty[$, elle a une unique solution $\beta$. Il y a donc exactement deux solutions.

$f(-1{,}3) = e^{1{,}6} - 4{,}9 \approx 0{,}05 > 0$ et $f(-1{,}2) = e^{1{,}4} - 4{,}6 \approx -0{,}54 < 0$, donc $-1{,}3 < \alpha < -1{,}2$.

$f(0{,}2) = e^{-1{,}4} - 0{,}4 \approx -0{,}15 < 0$ et $f(0{,}3) = e^{-1{,}6} - 0{,}1 \approx 0{,}10 > 0$, donc $0{,}2 < \beta < 0{,}3$.

**b)** On trace l'asymptote $y = 3x - 1$, le minimum $(x_0;f(x_0))$, les points $(\alpha;0)$, $(\beta;0)$ et $(0;e^{-1} - 1) \approx (0;-0{,}63)$, et la branche parabolique verticale en $-\infty$.

**4) a)** $\dfrac{U_{n+1}}{U_n} = \dfrac{e^{-2n-3}}{e^{-2n-1}} = e^{-2}$ : $(U_n)$ est géométrique de raison $e^{-2}$ et de premier terme $U_0 = e^{-1} > 0$. Comme $0 < e^{-2} < 1$, elle est **décroissante**.

**b)** $V_{n+1} - V_n = 3$ : $(V_n)$ est arithmétique de raison $3 > 0$, donc **croissante**.

**c)** Non. Pour être adjacentes, il faudrait que $V_n - U_n$ tende vers $0$. Or $\lim\limits_{n \to +\infty} U_n = 0$ et $\lim\limits_{n \to +\infty} V_n = +\infty$, donc $V_n - U_n \to +\infty$.

**5) a)** $f(k) = U_k + V_k$, donc
$$S_n = \sum_{k=0}^{n} U_k + \sum_{k=0}^{n} V_k = e^{-1}\,\dfrac{1 - e^{-2(n+1)}}{1 - e^{-2}} + \dfrac{(n + 1)(3n - 2)}{2}.$$

**b)** Le premier terme tend vers $\dfrac{e^{-1}}{1 - e^{-2}}$ et le second vers $+\infty$ : $\lim\limits_{n \to +\infty} S_n = +\infty$.

$\dfrac{S_n}{n^2} = \dfrac{1}{n^2} \times (\text{terme borné}) + \dfrac{(n + 1)(3n - 2)}{2n^2}$, donc $\lim\limits_{n \to +\infty} \dfrac{S_n}{n^2} = \dfrac{3}{2}$.
""")

_add("bac-d-2012-sn-math-ex4", r"""
**1. a)** $\dfrac{2x + 1}{x + 1} \to 2$ et $\ln(x + 1) \to +\infty$, donc $\lim\limits_{x \to +\infty} f(x) = -\infty$.

$\dfrac{f(x)}{x} = \dfrac{2x + 1}{x(x + 1)} - \dfrac{\ln(x + 1)}{x + 1} \times \dfrac{x + 1}{x} \to 0$ : $(C)$ a en $+\infty$ une **branche parabolique de direction $(Ox)$**.

**b)** $f(x) = \dfrac{2x + 1 - (x + 1)\ln(x + 1)}{x + 1}$. Quand $x \to -1^+$ : $(x + 1)\ln(x + 1) \to 0$, donc le numérateur tend vers $-1$, et le dénominateur tend vers $0^+$.

Donc $\lim\limits_{x \to -1^+} f(x) = -\infty$ : la droite $x = -1$ est **asymptote verticale**.

**2. a)** $\dfrac{2x + 1}{x + 1} = 2 - \dfrac{1}{x + 1}$, donc
$$f'(x) = \dfrac{1}{(x + 1)^2} - \dfrac{1}{x + 1} = \dfrac{1 - (x + 1)}{(x + 1)^2} = \dfrac{-x}{(x + 1)^2}.$$

$f'(0) = 0$ et $f(0) = 1$ : $(C)$ a au point $(0;1)$ une tangente horizontale d'équation $y = 1$.

**b)** $f'(x)$ a le signe de $-x$ :

| $x$ | $-1$ | | $0$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $1$ | ↘ | $-\infty$ |

**3. a)** $f''(x) = \dfrac{-(x + 1)^2 + 2x(x + 1)}{(x + 1)^4} = \dfrac{x - 1}{(x + 1)^3}$.

Sur $]-1;+\infty[$, $(x + 1)^3 > 0$ : $f''$ s'annule en $1$ en changeant de signe. $(C)$ a donc un point d'inflexion $A\left(1;\dfrac{3}{2} - \ln 2\right)$, avec $\dfrac{3}{2} - \ln 2 \approx 0{,}81$.

**b)** $f'(1) = -\dfrac{1}{4}$ :
$$(T) : y = -\dfrac{1}{4}(x - 1) + \dfrac{3}{2} - \ln 2 = -\dfrac{1}{4}x + \dfrac{7}{4} - \ln 2.$$

**4. a)** Sur $I = [0;+\infty[$, $g$ est continue et strictement décroissante : elle réalise une bijection de $I$ sur $J = ]-\infty;1]$.

**b)** $g^{-1}$ est définie sur $]-\infty;1]$, strictement décroissante (même sens que $g$), de $+\infty$ (en $-\infty$) à $g^{-1}(1) = 0$.

| $x$ | $-\infty$ | | $1$ |
|---|---|---|---|
| $g^{-1}(x)$ | $+\infty$ | ↘ | $0$ |

**c)** $\dfrac{3 - 2\ln 2}{2} = \dfrac{3}{2} - \ln 2 = g(1)$ et $g'(1) = -\dfrac{1}{4} \neq 0$, donc
$$\left(g^{-1}\right)'\left(\dfrac{3 - 2\ln 2}{2}\right) = \dfrac{1}{g'(1)} = -4.$$

**5. a)** Sur $]-1;0]$, $f$ est continue, strictement croissante de $-\infty$ à $1$ : une seule solution $\alpha$. Sur $[0;+\infty[$, $f$ est strictement décroissante de $1$ à $-\infty$ : une seule solution $\beta$.

$f(-0{,}7) = -\dfrac{0{,}4}{0{,}3} - \ln 0{,}3 \approx -0{,}13 < 0$ et $f(-0{,}6) = -\dfrac{0{,}2}{0{,}4} - \ln 0{,}4 \approx 0{,}42 > 0$, donc $-0{,}7 < \alpha < -0{,}6$.

$f(5{,}3) \approx 0{,}0007 > 0$ et $f(5{,}4) \approx -0{,}01 < 0$, donc $5{,}3 < \beta < 5{,}4$.

**b)** Les points d'intersection avec les axes sont $(0;1)$, $(\alpha;0)$ et $(\beta;0)$. On place aussi le point d'inflexion $A(1;0{,}81)$, les tangentes $y = 1$ et $(T)$, et l'asymptote $x = -1$.

**c)** $(C')$ est la symétrique, par rapport à la droite $y = x$, de la partie de $(C)$ d'abscisses $x \ge 0$. Elle passe par $(1;0)$ et $(0;\beta)$.

**6. a)** $f$ est continue sur $]-1;+\infty[$, donc elle y admet des primitives.

**b)** $F'(x) = a - \ln(x + 1) - \dfrac{x + b}{x + 1}$.

$F' = f \iff a - \dfrac{x + b}{x + 1} = \dfrac{2x + 1}{x + 1} \iff a(x + 1) - x - b = 2x + 1$ pour tout $x$, soit $a - 1 = 2$ et $a - b = 1$. D'où $a = 3$ et $b = 2$ :
$$F(x) = 3x - (x + 2)\ln(x + 1).$$

**c)** Sur $[0;\beta]$, $f$ décroît de $1$ à $0$, donc $f \ge 0$ et l'aire vaut
$$\mathcal{A} = F(\beta) - F(0) = 3\beta - (\beta + 2)\ln(\beta + 1) \text{ cm}^2.$$

Comme $f(\beta) = 0$, $\ln(\beta + 1) = \dfrac{2\beta + 1}{\beta + 1}$, d'où $\mathcal{A} = 3\beta - \dfrac{(\beta + 2)(2\beta + 1)}{\beta + 1}$.

Avec $\beta \approx 5{,}305$ : $\mathcal{A} \approx 2{,}46$ cm².
""")

# ═════════════════════════ 2012 — session complémentaire ══════════════════════

_add("bac-d-2012-sc-math-ex1", r"""
| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | A | B | A | A | B | C |

**1)** $V_{n+1} = U_{n+1} - 1 = 3U_n - 3 = 3V_n$ : $(V_n)$ est **géométrique** de raison $3$, avec $V_0 = 1$, donc $V_n = 3^n$. **Réponse A.**

**2)** $T_n = \ln(3^n) = n\ln 3$ : $T_{n+1} - T_n = \ln 3$, suite **arithmétique**. **Réponse B.**

**3)** $U_n = 1 + 3^n$, donc $W_n = U_{n+1} - U_n = 3^{n+1} - 3^n = 2 \times 3^n$, suite **croissante**. **Réponse A.**

**4)** $U_n = V_n + 1 = 1 + 3^n$. **Réponse A.**

**5)** $S_n = \displaystyle\sum_{k=0}^{n}(1 + 3^k) = (n + 1) + \dfrac{3^{n+1} - 1}{2} = n + \dfrac{1}{2} + \dfrac{3^{n+1}}{2}$. **Réponse B.**

**6)** $3 > 1$, donc $\lim\limits_{n \to +\infty} 3^n = +\infty$ et $\lim\limits_{n \to +\infty} U_n = +\infty$. **Réponse C.**
""")

_add("bac-d-2012-sc-math-ex2", r"""
**1)** $\Delta' = (-1)^2 - 5 = -4 = (2i)^2$, donc $z = 1 \pm 2i$ : $S = \{1 - 2i ;\ 1 + 2i\}$.

**2)** $p = f(1 - 2i) = \dfrac{1 - 2i - 2 - i}{1 - 2i + 3 + 2i} = \dfrac{-1 - 3i}{4} = -\dfrac{1}{4} - \dfrac{3}{4}i$.

**3) a)** On place $A(2;1)$, $B(-3;-2)$ et $C(1;2)$.

**b)** $q = f(z_C) = \dfrac{1 + 2i - 2 - i}{1 + 2i + 3 + 2i} = \dfrac{-1 + i}{4 + 4i} = \dfrac{(-1 + i)(4 - 4i)}{32} = \dfrac{8i}{32} = \dfrac{i}{4}$.

Sous forme trigonométrique : $q = \dfrac{1}{4}\left(\cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}\right)$.

Comme $f(z) = \dfrac{z - z_A}{z - z_B}$ : $q = \dfrac{z_C - z_A}{z_C - z_B}$, donc $(\overrightarrow{CB}, \overrightarrow{CA}) \equiv \dfrac{\pi}{2} \ [2\pi]$. Le triangle $ABC$ est **rectangle en $C$** (avec $CA = \dfrac{1}{4}CB$).

**c)**
- $|f(z)| = 1 \iff MA = MB$ : $\Gamma_1$ est la **médiatrice de $[AB]$**.
- $f(z)$ imaginaire pur $\iff M = A$ ou $(\overrightarrow{MB}, \overrightarrow{MA}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AB]$ privé de $B$**. Il passe par $C$.
- $f(z) - 1 = \dfrac{z_B - z_A}{z - z_B} = \dfrac{-5 - 3i}{z - z_B}$, donc $|f(z) - 1| = \dfrac{\sqrt{34}}{MB}$. Ainsi $|f(z) - 1| = 2\sqrt{34} \iff MB = \dfrac{1}{2}$ : $\Gamma_3$ est le **cercle de centre $B$ et de rayon $\dfrac{1}{2}$**.
""")

_add("bac-d-2012-sc-math-ex3", r"""
**1.** $\lim\limits_{x \to 0^+} f(x) = +\infty$ (car $-2\ln x \to +\infty$) : la droite $x = 0$ est **asymptote verticale**.

$f(x) = x\left(1 - \dfrac{2}{x} - 2\dfrac{\ln x}{x}\right)$, donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = 1$.

$f(x) - x = -2 - 2\ln x \to -\infty$ : $(C)$ a en $+\infty$ une **branche parabolique de direction la droite $y = x$**.

**2.** $f'(x) = 1 - \dfrac{2}{x} = \dfrac{x - 2}{x}$, du signe de $x - 2$. $f(2) = -2\ln 2 \approx -1{,}39$.

| $x$ | $0$ | | $2$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $-2\ln 2$ | ↗ | $+\infty$ |

**3.** $f(1) = -1$ et $f'(1) = -1$ : $T : y = -(x - 1) - 1$, soit $T : y = -x$.

**4.** Sur $]0;2]$, $f$ est continue et strictement décroissante de $+\infty$ à $-2\ln 2 < 0$ : une unique solution $\alpha$. Sur $[2;+\infty[$, elle est strictement croissante de $-2\ln 2$ à $+\infty$ : une unique solution $\beta$.

$f(0{,}4) \approx 0{,}23 > 0$ et $f(0{,}5) \approx -0{,}11 < 0$, donc $0{,}4 < \alpha < 0{,}5$. $f(5{,}3) \approx -0{,}04 < 0$ et $f(5{,}4) \approx 0{,}03 > 0$, donc $5{,}3 < \beta < 5{,}4$.

$f(x) = 0 \iff x - 2 = 2\ln x \iff e^{x - 2} = x^2 \iff e^x = e^2x^2$.

Donc $\alpha^2 e^\beta = \alpha^2 \times e^2\beta^2$ et $\beta^2 e^\alpha = \beta^2 \times e^2\alpha^2$ : ces deux nombres sont égaux, $\alpha^2 e^\beta = \beta^2 e^\alpha$.

**5. a)** Sur $I = ]0;2[$, $g$ est continue et strictement décroissante : elle réalise une bijection de $I$ sur $J = ]-2\ln 2;+\infty[$.

**b)** $g(1) = -1$ et $g'(1) = -1 \neq 0$, donc $\left(g^{-1}\right)'(-1) = \dfrac{1}{g'(1)} = -1$.

**6. a)** $(C)$ a pour minimum le point $(2;-2\ln 2)$ et coupe l'axe des abscisses en $\alpha$ et $\beta$. $(C')$ est la symétrique de la partie de $(C)$ d'abscisses dans $]0;2[$ par rapport à la droite $y = x$.

**b)** $2x - 2 - m - 2\ln x = 0 \iff x - 2 - 2\ln x = -x + m \iff f(x) = -x + m$.

Les solutions sont les abscisses des points communs à $(C)$ et à la droite $D_m : y = -x + m$, parallèle à $T$.

Posons $k(x) = f(x) + x = 2x - 2 - 2\ln x$. Alors $k'(x) = 2 - \dfrac{2}{x}$, donc $k$ décroît sur $]0;1]$ et croît sur $[1;+\infty[$, avec un minimum $k(1) = 0$ et des limites $+\infty$ aux deux bornes. Ainsi :
- si $m < 0$ : **aucune solution** ;
- si $m = 0$ : **une solution**, $x = 1$ ($D_0 = T$ est tangente à $(C)$ en $A$) ;
- si $m > 0$ : **deux solutions**.

**7. a)** Par parties, avec $u = \ln x$ et $v' = 1$ :
$$\int_1^2 \ln x\,dx = \big[x\ln x\big]_1^2 - \int_1^2 dx = 2\ln 2 - 1.$$

**b)** Sur $[1;2]$, $f$ décroît de $-1$ à $-2\ln 2$ : $f(x) < 0$. L'aire vaut
$$\mathcal{A} = -\int_1^2 f(x)\,dx = -\left(\left[\dfrac{x^2}{2} - 2x\right]_1^2 - 2(2\ln 2 - 1)\right) = -\left(-\dfrac{1}{2} - 4\ln 2 + 2\right) = 4\ln 2 - \dfrac{3}{2} \text{ u.a.}$$

(Environ $1{,}27$ u.a.)
""")

_add("bac-d-2012-sc-math-ex4", r"""
**1. a)** $\lim\limits_{x \to -\infty} xe^x = 0$, donc $\lim\limits_{x \to -\infty} g(x) = -1$ ; $\lim\limits_{x \to +\infty} g(x) = +\infty$.

**b)** $g'(x) = e^x + xe^x = (x + 1)e^x$, du signe de $x + 1$. $g(-1) = -\dfrac{1}{e} - 1 \approx -1{,}37$.

| $x$ | $-\infty$ | | $-1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $-$ | $0$ | $+$ | |
| $g(x)$ | $-1$ | ↘ | $-1 - \frac{1}{e}$ | ↗ | $+\infty$ |

**2. a)** Sur $]-\infty;-1]$, $g(x) \le -1 < 0$ (elle décroît de $-1$, valeur non atteinte, à $-1 - \frac{1}{e}$) : pas de solution.

Sur $[-1;+\infty[$, $g$ est continue et strictement croissante de $-1 - \frac{1}{e}$ à $+\infty$ : une unique solution $\alpha$.

$g(0{,}5) = 0{,}5e^{0{,}5} - 1 \approx -0{,}18 < 0$ et $g(0{,}6) = 0{,}6e^{0{,}6} - 1 \approx 0{,}09 > 0$, donc $0{,}5 < \alpha < 0{,}6$.

**b)** Si $x \le -1$, $g(x) < 0$. Si $-1 \le x \le \alpha$, $g(x) \le g(\alpha) = 0$ ($g$ croissante). Si $x \ge \alpha$, $g(x) \ge g(\alpha) = 0$.

**3. a)** Pour tout réel $x$, $e^x \ge 1 + x > x$, donc $e^x - x > 0$.
- En $-1$ : le numérateur tend vers $e^{-1} + 1 > 0$, et $x + 1 \to 0^-$ (à gauche) ou $0^+$ (à droite). Donc $\lim\limits_{x \to -1^-} f(x) = -\infty$ et $\lim\limits_{x \to -1^+} f(x) = +\infty$ : la droite $x = -1$ est **asymptote verticale**.
- $f(x) = \dfrac{\frac{e^x}{x} - 1}{1 + \frac{1}{x}} \to \dfrac{0 - 1}{1} = -1$ en $-\infty$ : la droite $y = -1$ est **asymptote horizontale** en $-\infty$.
- $f(x) = \dfrac{e^x}{x} \times \dfrac{1 - xe^{-x}}{1 + \frac{1}{x}} \to +\infty$ en $+\infty$, et $\dfrac{f(x)}{x} = \dfrac{e^x - x}{x(x + 1)} \to +\infty$ : **branche parabolique de direction $(Oy)$**.

**b)** $f'(x) = \dfrac{(e^x - 1)(x + 1) - (e^x - x)}{(x + 1)^2} = \dfrac{xe^x + e^x - x - 1 - e^x + x}{(x + 1)^2} = \dfrac{xe^x - 1}{(x + 1)^2} = \dfrac{g(x)}{(x + 1)^2}$.

**c)** $f'(x)$ a le signe de $g(x)$ :

| $x$ | $-\infty$ | | $-1$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | $-1$ | ↘ | $-\infty$ ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**d)** $g(\alpha) = 0$ donne $e^\alpha = \dfrac{1}{\alpha}$, d'où
$$f(\alpha) = \dfrac{\frac{1}{\alpha} - \alpha}{\alpha + 1} = \dfrac{1 - \alpha^2}{\alpha(\alpha + 1)} = \dfrac{1 - \alpha^2}{\alpha^2 + \alpha}.$$

Avec $\alpha \approx 0{,}567$ : $f(\alpha) \approx 0{,}76$, soit $f(\alpha) \approx 0{,}8$ à $10^{-1}$ près.

**4.** On trace les asymptotes $x = -1$ et $y = -1$, le minimum local $(\alpha;f(\alpha)) \approx (0{,}57;0{,}76)$, le point $(0;1)$ et la branche parabolique verticale en $+\infty$.
""")

# ═════════════════════════════ 2013 — session normale ═════════════════════════

_add("bac-d-2013-sn-math-ex1", r"""
| Question | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Réponse | A | B | A | C | A |

Les tirages sont simultanés : ce sont des combinaisons de 2 boules parmi 6, toutes équiprobables.

**1)** $C_6^2 = 15$ tirages possibles. **Réponse A.**

**2)** $p(A_0) = \dfrac{C_4^2}{C_6^2} = \dfrac{6}{15}$. **Réponse B.**

**3)** $p(A_1) = \dfrac{C_4^1 \times C_2^1}{15} = \dfrac{8}{15}$. **Réponse A.**

**4)** $p(A_2) = \dfrac{C_2^2}{15} = \dfrac{1}{15}$. **Réponse C.**

**5)** $E(X) = 0 \times \dfrac{6}{15} + 1 \times \dfrac{8}{15} + 2 \times \dfrac{1}{15} = \dfrac{10}{15} = \dfrac{2}{3}$. **Réponse A.**
""")

_add("bac-d-2013-sn-math-ex2", r"""
**1. a)** $\Delta' = 1 - 10 = -9 = (3i)^2$, donc $z = -1 \pm 3i$ : $z_1 = -1 + 3i$ et $z_2 = -1 - 3i$.

**b)** $\Delta' = 4 - 20 = -16 = (4i)^2$, donc $z = 2 \pm 4i$ : $z_3 = 2 + 4i$ et $z_4 = 2 - 4i$.

**2) a)** On place $A(-1;3)$, $B(-1;-3)$, $K(2;4)$, $L(2;-4)$ et $E(2;2)$.

**b)** $z_E = 2 + 4i - 2i = 2 + 2i = 2\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$.

**c)** $z_B - z_A = -6i$ et $z_L - z_E = -6i$ : $\overrightarrow{AB} = \overrightarrow{EL}$, donc $ABLE$ est un **parallélogramme**.

(Ce n'est ni un rectangle ni un losange : $\overrightarrow{AB} \cdot \overrightarrow{AE} = 0 \times 3 + (-6)(-1) = 6 \neq 0$, et $AB = 6 \neq AE = \sqrt{10}$.)

$z_K - z_A = 3 + i$ et $z_E - z_A = 3 - i$, donc $AK = AE = \sqrt{10}$ : le triangle $AKE$ est **isocèle en $A$**.

Il n'est pas rectangle : $KE = 2$, et $\dfrac{z_E - z_A}{z_K - z_A} = \dfrac{3 - i}{3 + i} = \dfrac{4 - 3i}{5}$ n'est pas imaginaire pur.

**3)** $f(z) = \dfrac{z - z_K}{z - z_A}$, défini pour $M \neq A$.
- $|f(z)| = 1 \iff MK = MA$ : $\Gamma_1$ est la **médiatrice de $[AK]$**.
- $f(z) - 1 = \dfrac{z_A - z_K}{z - z_A} = \dfrac{-3 - i}{z - z_A}$, donc $|f(z) - 1| = \dfrac{\sqrt{10}}{MA}$. Ainsi $|f(z) - 1| = \sqrt{10} \iff MA = 1$ : $\Gamma_2$ est le **cercle de centre $A$ et de rayon $1$**.
""")

_add("bac-d-2013-sn-math-ex3", r"""
**1. a)** $U_1 = 3 \times 6 + 0 - 13 = 5$, $U_2 = 3 \times 5 + 10 - 13 = 12$, $U_3 = 3 \times 12 + 20 - 13 = 43$.

**b)** $U_1 - U_0 = -1$ et $U_2 - U_1 = 7$ : la suite n'est pas arithmétique.

$\dfrac{U_1}{U_0} = \dfrac{5}{6}$ et $\dfrac{U_2}{U_1} = \dfrac{12}{5}$ : elle n'est pas géométrique.

**2) a)** $V_{n+1} = U_{n+1} + 5(n + 1) - 4 = 3U_n + 10n - 13 + 5n + 1 = 3U_n + 15n - 12 = 3(U_n + 5n - 4) = 3V_n$.

$(V_n)$ est géométrique de raison $3$ et de premier terme $V_0 = U_0 - 4 = 2$. Donc $V_n = 2 \times 3^n$.

**b)** $V_n \ge 2013 \iff 3^n \ge 1006{,}5$. Or $3^6 = 729$ et $3^7 = 2187$, et $(V_n)$ est croissante.

C'est donc **à partir du terme $V_7$** ($V_7 = 4374$).

**c)** $U_n = V_n - 5n + 4 = 2 \times 3^n - 5n + 4$.

**3)**
$$S_n = 2\sum_{k=0}^{n} 3^k - 5\sum_{k=0}^{n} k + 4(n + 1) = 2 \times \dfrac{3^{n+1} - 1}{2} - \dfrac{5n(n + 1)}{2} + 4(n + 1).$$

Donc $S_n = 3^{n+1} - 1 - \dfrac{5n(n + 1)}{2} + 4(n + 1) = 3^{n+1} + 3 + \dfrac{3n - 5n^2}{2}$.

(Vérification : $S_1 = 6 + 5 = 11 = 9 + 3 - 1$.)
""")

_add("bac-d-2013-sn-math-ex4", r"""
**Partie A**

**1. a)** $\lim\limits_{x \to 0^+} g(x) = 0 - 3 - \infty = -\infty$ et $\lim\limits_{x \to +\infty} g(x) = +\infty$.

**b)** $g'(x) = 3x^2 + \dfrac{2}{x} > 0$ sur $]0;+\infty[$ : $g$ est strictement croissante.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $g'(x)$ | ‖ | $+$ | |
| $g(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ |

**2. a)** $g$ est continue et strictement croissante : elle réalise une bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\alpha$. $g(1{,}34) \approx -0{,}009 < 0$ et $g(1{,}35) \approx 0{,}06 > 0$, donc $1{,}34 \le \alpha \le 1{,}35$.

**c)** $g(x) < 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) > 0$ sur $]\alpha;+\infty[$.

**Partie B**

**1. a)** En $0^+$ : $1 - \ln x \to +\infty$ et $\dfrac{1}{x^2} \to +\infty$, donc $\dfrac{1 - \ln x}{x^2} \to +\infty$ et $\lim\limits_{x \to 0^+} f(x) = +\infty$.

En $+\infty$ : $\dfrac{1 - \ln x}{x^2} = \dfrac{1}{x^2} - \dfrac{1}{x} \times \dfrac{\ln x}{x} \to 0$. Donc $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty}\big(f(x) - (x - 2)\big) = 0$.

**b)** La droite $x = 0$ est **asymptote verticale** ; la droite $\Delta : y = x - 2$ est **asymptote oblique** en $+\infty$.

**c)** $d(x) = \dfrac{1 - \ln x}{x^2}$ a le signe de $1 - \ln x$.

| $x$ | $0$ | | $e$ | | $+\infty$ |
|---|---|---|---|---|---|
| $d(x)$ | ‖ | $+$ | $0$ | $-$ | |

$\Gamma$ est au-dessus de $\Delta$ sur $]0;e[$ et au-dessous sur $]e;+\infty[$ ; elles se coupent au point $(e;e - 2)$.

**2. a)** $f'(x) = 1 + \dfrac{-\frac{1}{x} \cdot x^2 - 2x(1 - \ln x)}{x^4} = 1 + \dfrac{-3 + 2\ln x}{x^3} = \dfrac{x^3 - 3 + 2\ln x}{x^3} = \dfrac{g(x)}{x^3}$.

Comme $x^3 > 0$, $f'(x)$ a le même signe que $g(x)$.

**b)** $g(\alpha) = 0$ donne $\ln\alpha = \dfrac{3 - \alpha^3}{2}$, donc
$$f(\alpha) = \alpha - 2 + \dfrac{1 - \frac{3 - \alpha^3}{2}}{\alpha^2} = \alpha - 2 + \dfrac{\alpha^3 - 1}{2\alpha^2} = \dfrac{3\alpha^3 - 4\alpha^2 - 1}{2\alpha^2}.$$

Avec $\alpha \approx 1{,}341$ : $f(\alpha) \approx -0{,}27$, soit $f(\alpha) \approx -0{,}3$ à $10^{-1}$ près.

**c)**

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**3. a)** $f(1) = -1 + 1 = 0$ et $f'(1) = g(1) = -2$ : $T : y = -2(x - 1)$, soit $y = -2x + 2$.

**b)** $f(1) = 0$ et $1 < \alpha$ : $A(1;0)$ est sur l'axe des abscisses. Sur $[\alpha;+\infty[$, $f$ est continue et strictement croissante de $f(\alpha) < 0$ à $+\infty$ : elle s'annule une seule fois, en $\beta$.

$f(1{,}9) \approx -0{,}0008 < 0$ et $f(2) = \dfrac{1 - \ln 2}{4} \approx 0{,}08 > 0$, donc $1{,}9 \le \beta \le 2$ ($\beta \approx 1{,}901$).

**c)** On trace l'asymptote $x = 0$, l'asymptote $\Delta$, le point $(e;e - 2)$ commun avec $\Delta$, les points $A(1;0)$ et $(\beta;0)$, la tangente $T$ et le minimum $(\alpha;f(\alpha))$.

**4) a)** Pour $x \ge 3 > e$, $d(x) < 0$ : $\Gamma$ est au-dessous de $\Delta$. L'aire vaut
$$I_n = \int_3^n \big((x - 2) - f(x)\big)\,dx = \int_3^n \dfrac{-1 + \ln x}{x^2}\,dx.$$

**b)** Par parties, avec $u = \ln x$ et $v' = \dfrac{1}{x^2}$ ($u' = \dfrac{1}{x}$, $v = -\dfrac{1}{x}$) :
$$J_n = \left[-\dfrac{\ln x}{x}\right]_3^n + \int_3^n \dfrac{dx}{x^2} = -\dfrac{\ln n}{n} + \dfrac{\ln 3}{3} + \dfrac{1}{3} - \dfrac{1}{n}.$$

$$I_n = J_n - \int_3^n \dfrac{dx}{x^2} = J_n - \left(\dfrac{1}{3} - \dfrac{1}{n}\right) = \dfrac{\ln 3}{3} - \dfrac{\ln n}{n}.$$

**c)** $\lim\limits_{n \to +\infty} \dfrac{\ln n}{n} = 0$, donc $\lim\limits_{n \to +\infty} I_n = \dfrac{\ln 3}{3} \approx 0{,}37$ cm².
""", note="Énoncé : g(x) = x³ − 3 + 2 ln x (le PDF retapé écrit x², coquille) — la correction suit la version cohérente.")

# ═════════════════════════ 2013 — session complémentaire ══════════════════════

_add("bac-d-2013-sc-math-ex1", r"""
| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | B | C | C | A | B | A |

**1)** $U_n = U_0 + nr = 15 + 3n$. **Réponse B.**

**2)** $U_{10} = 15 + 30 = 45$. **Réponse C.**

**3)** $U_0 + \dots + U_n = (n + 1)\dfrac{U_0 + U_n}{2} = (n + 1)\dfrac{30 + 3n}{2}$. Pour $n = 7$ : $8 \times \dfrac{51}{2} = 204$. **Réponse C.**

**4)** $V_n = \dfrac{1}{15 + 3n} \to 0$ : $(V_n)$ est convergente (elle est décroissante, et $\dfrac{V_1}{V_0} = \dfrac{15}{18} \neq \dfrac{V_2}{V_1} = \dfrac{18}{21}$, donc elle n'est pas géométrique). **Réponse A.**

**5)** $\dfrac{T_{n+1}}{T_n} = e^{U_{n+1} - U_n} = e^3$ : $(T_n)$ est géométrique de raison $e^3$. **Réponse B.**

**6)** $W_n \ge V_n > 0$ : $(W_n)$ est minorée par $0$. Rien n'impose qu'elle soit décroissante ou divergente (par exemple $W_n = V_n$ converge). **Réponse A.**
""", note="Question 3 : blanc du PDF complété en « + Uₙ = 204 » (n = 7).")

_add("bac-d-2013-sc-math-ex2", r"""
**1)** $\Delta' = 9 - 18 = -9 = (3i)^2$, donc $S = \{3 - 3i ;\ 3 + 3i\}$.

**2)** $\Delta' = (\sqrt{3})^2 - 4 = -1 = i^2$, donc $S' = \{\sqrt{3} - i ;\ \sqrt{3} + i\}$.

**3)** $u = 3 + 3i = 3\sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right) = 3\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right) = 3\sqrt{2}\,e^{i\frac{\pi}{4}}$.

$v = \sqrt{3} - i = 2\left(\dfrac{\sqrt{3}}{2} - \dfrac{1}{2}i\right) = 2\left(\cos\left(-\dfrac{\pi}{6}\right) + i\sin\left(-\dfrac{\pi}{6}\right)\right) = 2e^{-i\frac{\pi}{6}}$.

**4) a)** $w = (3 + 3i)(\sqrt{3} - i) = 3\sqrt{3} - 3i + 3\sqrt{3}\,i + 3 = (3 + 3\sqrt{3}) + i(3\sqrt{3} - 3)$.

**b)** $w = uv = 3\sqrt{2} \times 2\,e^{i\left(\frac{\pi}{4} - \frac{\pi}{6}\right)} = 6\sqrt{2}\,e^{i\frac{\pi}{12}} = 6\sqrt{2}\left(\cos\dfrac{\pi}{12} + i\sin\dfrac{\pi}{12}\right)$.

**c)** En identifiant les parties réelles et imaginaires :
$$\cos\dfrac{\pi}{12} = \dfrac{3 + 3\sqrt{3}}{6\sqrt{2}} = \dfrac{\sqrt{2} + \sqrt{6}}{4}, \qquad \sin\dfrac{\pi}{12} = \dfrac{3\sqrt{3} - 3}{6\sqrt{2}} = \dfrac{\sqrt{6} - \sqrt{2}}{4}.$$
""")

_add("bac-d-2013-sc-math-ex3", r"""
**1. a)** $\lim\limits_{x \to -1^+} \ln(x + 1) = -\infty$, donc $\lim\limits_{x \to -1^+} f(x) = -\infty$ ; et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $\dfrac{f(x)}{x} = 1 - \dfrac{2}{x} + \dfrac{\ln(x + 1)}{x + 1} \times \dfrac{x + 1}{x} \to 1$, et $f(x) - x = -2 + \ln(x + 1) \to +\infty$.

$(C)$ a en $+\infty$ une **branche parabolique de direction la droite $y = x$**. (La droite $x = -1$ est asymptote verticale, d'après 1. a.)

**2.** $f'(x) = 1 + \dfrac{1}{x + 1} > 0$ sur $I$ : $f$ est strictement croissante.

| $x$ | $-1$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $+\infty$ |

**3. a)** $f$ est continue et strictement croissante sur $I$ : elle réalise une bijection de $I$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\alpha$. $f(1{,}2) = -0{,}8 + \ln 2{,}2 \approx -0{,}01 < 0$ et $f(1{,}3) = -0{,}7 + \ln 2{,}3 \approx 0{,}13 > 0$, donc $1{,}2 < \alpha < 1{,}3$.

**c)** On trace l'asymptote $x = -1$, les points $(0;-2)$ et $(\alpha;0)$, et la branche parabolique de direction $y = x$.

**4) a)** $u'(x) = \ln(x + 1) + (x + 1) \times \dfrac{1}{x + 1} = \ln(x + 1) + 1$.

Donc $u'(x) + x - 3 = \ln(x + 1) + x - 2 = f(x)$.

**b)** $F(x) = u(x) + \dfrac{x^2}{2} - 3x + c$, et $F(0) = 0$ donne $c = 0$ :
$$F(x) = (x + 1)\ln(x + 1) + \dfrac{x^2}{2} - 3x.$$

**c)** Sur $[0;\alpha]$, $f(x) \le 0$ ($f$ croissante, $f(\alpha) = 0$). L'aire vaut $\mathcal{A} = -\displaystyle\int_0^\alpha f(x)\,dx = -F(\alpha)$.

Comme $f(\alpha) = 0$, $\ln(\alpha + 1) = 2 - \alpha$, donc $F(\alpha) = (\alpha + 1)(2 - \alpha) + \dfrac{\alpha^2}{2} - 3\alpha = -\dfrac{\alpha^2}{2} - 2\alpha + 2$.
$$\mathcal{A} = \dfrac{\alpha^2}{2} + 2\alpha - 2 \text{ u.a.} \approx 1{,}15 \text{ u.a.}$$

**5) a)** $f^{-1}$ est définie sur $\mathbb{R}$, strictement croissante, à valeurs dans $]-1;+\infty[$ :
- $\lim\limits_{x \to -\infty} f^{-1}(x) = -1$ ;
- $\lim\limits_{x \to +\infty} f^{-1}(x) = +\infty$ ;
- en posant $y = f^{-1}(x)$, on a $\dfrac{f^{-1}(x)}{x} = \dfrac{y}{f(y)}$ avec $y \to +\infty$, donc $\lim\limits_{x \to +\infty} \dfrac{f^{-1}(x)}{x} = 1$ (car $\dfrac{f(y)}{y} \to 1$).

**b)** $f(0) = -2$ et $f'(0) = 2$, donc $\left(f^{-1}\right)'(-2) = \dfrac{1}{f'(0)} = \dfrac{1}{2}$.

La tangente à $(C')$ au point $(-2;0)$ a pour équation $y = \dfrac{1}{2}(x + 2)$.
""")

_add("bac-d-2013-sc-math-ex4", r"""
**1) a)** $\lim\limits_{x \to +\infty} g(x) = +\infty$. En $-\infty$ : $(2x + 3)e^{x+1} = 2e\,xe^x + 3e^{x+1} \to 0$, donc $\lim\limits_{x \to -\infty} g(x) = 1$.

**b)** $g'(x) = 2e^{x+1} + (2x + 3)e^{x+1} = (2x + 5)e^{x+1}$, du signe de $2x + 5$.

$g\left(-\dfrac{5}{2}\right) = -2e^{-3/2} + 1 \approx 0{,}55$.

| $x$ | $-\infty$ | | $-\frac{5}{2}$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $-$ | $0$ | $+$ | |
| $g(x)$ | $1$ | ↘ | $1 - 2e^{-3/2}$ | ↗ | $+\infty$ |

**c)** Le minimum de $g$ est $1 - 2e^{-3/2} > 0$ (car $e^{3/2} > 2$), donc $g(x) > 0$ pour tout réel $x$.

**2) a)** En $-\infty$ : $x - 3 \to -\infty$ et $(2x + 1)e^{x+1} \to 0$, donc $f(x) \to -\infty$. En $+\infty$ : $f(x) \to +\infty$.

**b)** $\dfrac{f(x)}{x} = 1 - \dfrac{3}{x} + \left(2 + \dfrac{1}{x}\right)e^{x+1} \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**c)** $f(x) - (x - 3) = (2x + 1)e^{x+1} \to 0$ en $-\infty$ : la droite $D : y = x - 3$ est **asymptote oblique** en $-\infty$.

Cette différence a le signe de $2x + 1$ : $(C)$ est au-dessous de $D$ sur $\left]-\infty;-\dfrac{1}{2}\right[$ et au-dessus sur $\left]-\dfrac{1}{2};+\infty\right[$. Elles se coupent en $\left(-\dfrac{1}{2};-\dfrac{7}{2}\right)$.

**3. a)** $f'(x) = 1 + 2e^{x+1} + (2x + 1)e^{x+1} = 1 + (2x + 3)e^{x+1} = g(x)$.

**b)** $f'(x) = g(x) > 0$ : $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

**4. a)** $f$ est continue et strictement croissante : elle réalise une bijection de $\mathbb{R}$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\alpha$. $f(0) = -3 + e \approx -0{,}28 < 0$ et $f(0{,}1) = -2{,}9 + 1{,}2e^{1{,}1} \approx 0{,}70 > 0$, donc $0 < \alpha < 0{,}1$ ($\alpha \approx 0{,}03$).

**c)** $f(\alpha) = 0 \iff (2\alpha + 1)e^{\alpha+1} = 3 - \alpha \iff e^{\alpha+1} = \dfrac{3 - \alpha}{2\alpha + 1}$ (car $2\alpha + 1 > 0$ et $3 - \alpha > 0$).

En prenant le logarithme : $\alpha + 1 = \ln\left(\dfrac{3 - \alpha}{2\alpha + 1}\right)$, soit $\ln\left(\dfrac{3 - \alpha}{2\alpha + 1}\right) - \alpha = 1$.

**5. a)** La tangente est parallèle à $D$ $\iff f'(x) = 1 \iff (2x + 3)e^{x+1} = 0 \iff x = -\dfrac{3}{2}$ : le point $A$ est unique.

$f\left(-\dfrac{3}{2}\right) = -\dfrac{3}{2} - 3 - 2e^{-1/2} = -\dfrac{9}{2} - 2e^{-1/2}$, donc
$$T : y = \left(x + \dfrac{3}{2}\right) - \dfrac{9}{2} - 2e^{-1/2} = x - 3 - 2e^{-1/2}.$$

**b)** On trace $D$, $T$ (parallèle à $D$, en dessous), le point $A\left(-\dfrac{3}{2};f\left(-\dfrac{3}{2}\right)\right) \approx (-1{,}5;-5{,}71)$, le point $\left(-\dfrac{1}{2};-\dfrac{7}{2}\right)$ et le point $(\alpha;0)$.

**c)** $(2x + 1)e^{x+1} - m - 3 = 0 \iff x - 3 + (2x + 1)e^{x+1} = x + m \iff f(x) = x + m$.

On cherche les points communs à $(C)$ et à la droite $D_m : y = x + m$, parallèle à $D$ et à $T$.

La fonction $h(x) = (2x + 1)e^{x+1}$ a pour dérivée $(2x + 3)e^{x+1}$ : elle décroît de $0$ (en $-\infty$) jusqu'à $h\left(-\dfrac{3}{2}\right) = -2e^{-1/2}$, puis croît jusqu'à $+\infty$. Avec $h(x) = m + 3$ :
- si $m < -3 - 2e^{-1/2}$ ($D_m$ sous $T$) : **aucune solution** ;
- si $m = -3 - 2e^{-1/2}$ ($D_m = T$) : **une solution**, $x = -\dfrac{3}{2}$ ;
- si $-3 - 2e^{-1/2} < m < -3$ ($D_m$ entre $T$ et $D$) : **deux solutions** ;
- si $m \ge -3$ ($D_m$ est $D$ ou au-dessus) : **une solution**.
""")

# ═════════════════════════════ 2014 — session normale ═════════════════════════

_add("bac-d-2014-sn-math-ex1", r"""
| Question n° | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Réponse | C | B | B | C | B |

La cage contient deux couples blancs (2 mâles blancs, 2 femelles blanches) et 2 femelles grises. On tire 2 oiseaux simultanément : $C_6^2 = 15$ tirages équiprobables.

**1)** $C_6^2$. **Réponse C.**

**2)** Deux oiseaux gris : un seul tirage (les 2 femelles grises), donc $p_1 = \dfrac{1}{15}$. **Réponse B.**

**3)** Même couleur : 2 blancs parmi 4 ($C_4^2 = 6$) ou 2 gris ($1$), soit $p_2 = \dfrac{7}{15}$. **Réponse B.**

**4)** Même sexe : 2 femelles parmi 4 ($6$) ou 2 mâles ($1$), soit $p_3 = \dfrac{7}{15}$. **Réponse C.**

**5)** Parmi les 7 tirages de même couleur, ceux de même sexe sont : femelle blanche + femelle blanche ($1$), mâle blanc + mâle blanc ($1$) et les 2 grises ($1$), soit 3 tirages.
$$p_4 = \dfrac{3}{7}.$$
**Réponse B.**
""")

_add("bac-d-2014-sn-math-ex2", r"""
**1.** $(E_1)$ : $\Delta' = 1 - 17 = -16 = (4i)^2$, donc $S_1 = \{1 - 4i ;\ 1 + 4i\}$.

$(E_2)$ : $\Delta' = 16 - 17 = -1 = i^2$, donc $S_2 = \{-4 - i ;\ -4 + i\}$.

**2) a)** On place $A(-4;-1)$, $B(1;-4)$ et $C(4;1)$.

$z_B - z_A = 5 - 3i$ et $z_C - z_B = 3 + 5i = i(5 - 3i)$. Donc $BC = BA$ et $(\overrightarrow{AB}, \overrightarrow{BC}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $ABC$ est **rectangle isocèle en $B$**.

**b)** $\alpha = f(-1 + 4i) = \dfrac{-2 + 8i}{3 + 5i} = \dfrac{(-2 + 8i)(3 - 5i)}{34} = \dfrac{34 + 34i}{34} = 1 + i$.

Sous forme trigonométrique : $\alpha = \sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$.

**c)** $f(z) = \dfrac{z - z_B}{z - z_A}$, défini pour $M \neq A$. $|f(z)| = 1 \iff MB = MA$ : $\Gamma_1$ est la **médiatrice de $[AB]$**.

**d)** $f(z)$ est imaginaire pur $\iff M = B$ ou $(\overrightarrow{MA}, \overrightarrow{MB}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AB]$ privé de $A$**.

**3) a)** $\dfrac{\alpha}{2} = \dfrac{1 + i}{2}$, donc
$$z_1 = \dfrac{(1 + i)(4 + i)}{2} = \dfrac{3 + 5i}{2}, \qquad z_2 = \dfrac{(1 + i)(3 + 5i)}{4} = \dfrac{-2 + 8i}{4} = \dfrac{-1 + 4i}{2}.$$

**b)** $V_{n+1} = |z_{n+1}| = \left|\dfrac{\alpha}{2}\right| |z_n| = \dfrac{\sqrt{2}}{2}V_n$ : $(V_n)$ est géométrique de raison $\dfrac{\sqrt{2}}{2}$ et de premier terme $V_0 = |4 + i| = \sqrt{17}$.

**c)** $OM_k = V_k$, donc
$$S_n = \sqrt{17}\,\dfrac{1 - \left(\frac{\sqrt{2}}{2}\right)^{n+1}}{1 - \frac{\sqrt{2}}{2}}.$$

Comme $0 < \dfrac{\sqrt{2}}{2} < 1$ : $\lim\limits_{n \to +\infty} S_n = \dfrac{\sqrt{17}}{1 - \frac{\sqrt{2}}{2}} = \dfrac{2\sqrt{17}}{2 - \sqrt{2}} = \sqrt{17}\,(2 + \sqrt{2}) \approx 14{,}08$.
""")

_add("bac-d-2014-sn-math-ex3", r"""
**1. a)** $\lim\limits_{x \to -\infty} e^x = 0$, donc $\lim\limits_{x \to -\infty} f(x) = -\infty$ ; et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

**b)** $f(x) - (2x - 1) = 2e^x \to 0$ en $-\infty$ : la droite $(D) : y = 2x - 1$ est **asymptote oblique** à $(C)$ en $-\infty$, et $(C)$ est au-dessus.

$\dfrac{f(x)}{x} = 2 - \dfrac{1}{x} + 2\dfrac{e^x}{x} \to +\infty$ en $+\infty$ : **branche parabolique de direction $(Oy)$**.

**2. a)** $f'(x) = 2 + 2e^x > 0$ : $f$ est strictement croissante sur $\mathbb{R}$, de $-\infty$ à $+\infty$.

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $-\infty$ | ↗ | $+\infty$ |

**b)** $f$ est continue et strictement croissante : elle réalise une bijection de $\mathbb{R}$ sur $J = \mathbb{R}$.

**c)** $0 \in J$ : une unique solution $\alpha$. $f(-0{,}3) = -1{,}6 + 2e^{-0{,}3} \approx -0{,}12 < 0$ et $f(-0{,}2) = -1{,}4 + 2e^{-0{,}2} \approx 0{,}24 > 0$, donc $-0{,}3 < \alpha < -0{,}2$.

**3)** $(C)$ passe par $(0;1)$ et $(\alpha;0)$, a l'asymptote $y = 2x - 1$ en $-\infty$ et une branche parabolique verticale en $+\infty$.

$(C')$ est sa symétrique par rapport à $y = x$ : elle passe par $(1;0)$ et $(0;\alpha)$, a l'asymptote $y = \dfrac{x + 1}{2}$ en $-\infty$ et une branche parabolique de direction $(Ox)$ en $+\infty$.

**4. a)** $f(\alpha) = 0$ donne $2e^\alpha = 1 - 2\alpha$, donc $f'(\alpha) = 2 + 2e^\alpha = 3 - 2\alpha$ :
$$(T) : y = (3 - 2\alpha)(x - \alpha).$$

**b)** $\left(f^{-1}\right)'(0) = \dfrac{1}{f'(\alpha)} = \dfrac{1}{3 - 2\alpha} = \dfrac{1}{-2\alpha + 3}$.

**5) a)** $U_n = (2n - 1) + 2e^n = a_n + g_n$ :
- $a_n = 2n - 1$ est arithmétique de premier terme $a_0 = -1$ et de raison $2$ ;
- $g_n = 2e^n$ est géométrique de premier terme $g_0 = 2$ et de raison $e$.

**b)**
$$S_n = \sum_{k=0}^{n}(2k - 1) + 2\sum_{k=0}^{n} e^k = (n + 1)\dfrac{-1 + 2n - 1}{2} + 2\,\dfrac{e^{n+1} - 1}{e - 1} = n^2 - 1 + \dfrac{2\left(e^{n+1} - 1\right)}{e - 1}.$$

$\lim\limits_{n \to +\infty} S_n = +\infty$.
""")

_add("bac-d-2014-sn-math-ex4", r"""
**Partie A**

**1. a)** $\lim\limits_{x \to 0^+} g(x) = -\infty$ et $\lim\limits_{x \to +\infty} g(x) = +\infty$.

**b)** $g'(x) = 1 + \dfrac{3}{x} > 0$ : $g$ est strictement croissante sur $]0;+\infty[$, de $-\infty$ à $+\infty$.

**2. a)** $g$ est continue et strictement croissante de $]0;+\infty[$ sur $\mathbb{R}$, qui contient $0$ : une unique solution $\alpha$.

$g(1{,}59) \approx -0{,}02 < 0$ et $g(1{,}60) \approx 0{,}01 > 0$, donc $1{,}59 < \alpha < 1{,}60$.

**b)** $g(x) < 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) > 0$ sur $]\alpha;+\infty[$.

**Partie B**

**1. a)** En $0^+$ : $\dfrac{x - 3}{x} \to -\infty$ et $\ln x \to -\infty$, donc d'après (1), $f(x) \to +\infty$.

En $+\infty$ : $\dfrac{x - 3}{x} \to 1$ et $\ln x \to +\infty$, donc $f(x) \to +\infty$.

D'après (2), $f(x) - \ln x = -3\dfrac{\ln x}{x} \to 0$.

**b)** La droite $x = 0$ est **asymptote verticale**. En $+\infty$, $(C)$ et la courbe de $\ln$ sont **asymptotes** l'une à l'autre ; pour $x > 1$, $(C)$ est au-dessous ($-3\frac{\ln x}{x} < 0$).

**2. a)** D'après (2) : $f'(x) = \dfrac{1}{x} - 3\,\dfrac{\frac{1}{x} \cdot x - \ln x}{x^2} = \dfrac{x - 3 + 3\ln x}{x^2} = \dfrac{g(x)}{x^2}$.

Comme $x^2 > 0$, $f'(x)$ et $g(x)$ ont le même signe.

**b)** $g(\alpha) = 0$ donne $\ln\alpha = \dfrac{3 - \alpha}{3}$, donc
$$f(\alpha) = \dfrac{\alpha - 3}{\alpha} \times \dfrac{3 - \alpha}{3} = \dfrac{-(\alpha - 3)^2}{3\alpha}.$$

Avec $\alpha \approx 1{,}597$ : $f(\alpha) \approx -0{,}41$, soit $f(\alpha) \approx -0{,}4$ à $10^{-1}$ près.

**c)**

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | ‖ $+\infty$ | ↘ | $f(\alpha)$ | ↗ | $+\infty$ |

**3. a)** $f(1) = 0$ et $f'(1) = g(1) = -2$ : $T : y = -2(x - 1)$, soit $y = -2x + 2$.

**b)** $f(x) = 0 \iff x - 3 = 0$ ou $\ln x = 0 \iff x = 3$ ou $x = 1$. Les points d'intersection sont $(1;0)$ et $(3;0)$.

On trace l'asymptote $x = 0$, le minimum $(\alpha;f(\alpha))$, les points $(1;0)$ et $(3;0)$, la tangente $T$ et la courbe de $\ln$ dont $(C)$ se rapproche en $+\infty$.

**c)** Pour $x > 0$ : $x\ln x - 3\ln x = (x - 3)\ln x = x\,f(x)$, donc l'équation s'écrit
$$x\big(2x - m + f(x)\big) = 0 \iff f(x) = -2x + m.$$

Les solutions sont les abscisses des points communs à $(C)$ et à la droite $D_m : y = -2x + m$, parallèle à $T$.

Posons $k(x) = f(x) + 2x$ : $k'(x) = \dfrac{2x^2 + x - 3 + 3\ln x}{x^2}$. Le numérateur est strictement croissant et s'annule en $1$. Donc $k$ décroît sur $]0;1]$, croît sur $[1;+\infty[$, avec $k(1) = 2$ et $k \to +\infty$ aux deux bornes. Ainsi :
- si $m < 2$ : **aucune solution** ;
- si $m = 2$ : **une solution**, $x = 1$ ($D_2 = T$) ;
- si $m > 2$ : **deux solutions**.

**4. a)** $J = \displaystyle\int_1^e \dfrac{\ln x}{x}\,dx = \left[\dfrac{(\ln x)^2}{2}\right]_1^e = \dfrac{1}{2}$.

**b)** Par parties, avec $u = \ln x$ et $v' = 1$ : $I = \big[x\ln x\big]_1^e - \displaystyle\int_1^e dx = e - (e - 1) = 1$.

**c)** Sur $[1;e]$ : $x - 3 < 0$ (car $e < 3$) et $\ln x \ge 0$, donc $f(x) \le 0$. L'aire est donc $S = -\displaystyle\int_1^e f(x)\,dx$.

D'après (2) : $\displaystyle\int_1^e f(x)\,dx = I - 3J = 1 - \dfrac{3}{2} = -\dfrac{1}{2}$, d'où $S = \dfrac{1}{2}$ u.a.
""", note="Partie B 3a : « au point d'abscisse 1 » (abscisse manquante dans le sujet, reprise du corrigé officiel).")

# ═════════════════════════ 2014 — session complémentaire ══════════════════════

_add("bac-d-2014-sc-math-ex1", r"""
| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | A | B | B | C | A | C |

Les 8 questions sont indépendantes et, à chacune, la probabilité de bien répondre au hasard est $\dfrac{1}{4}$. $X$ suit donc la **loi binomiale** de paramètres $n = 8$ et $p = \dfrac{1}{4}$.

**1)** $X(\Omega) = \{0,1,\dots,8\}$. **Réponse A.**

**2)** $p(A) = p(X = 8) = \left(\dfrac{1}{4}\right)^8$. **Réponse B.**

**3)** $p(B) = p(X = 0) = \left(\dfrac{3}{4}\right)^8$. **Réponse B.**

**4)** $C$ est l'événement contraire de $B$ : $p(C) = 1 - \left(\dfrac{3}{4}\right)^8$. **Réponse C.**

**5)** $p(D) = p(X = 2) = C_8^2\left(\dfrac{1}{4}\right)^2\left(\dfrac{3}{4}\right)^6$. **Réponse A.**

**6)** $E(X) = np = 8 \times \dfrac{1}{4} = 2$. **Réponse C.**
""")

_add("bac-d-2014-sc-math-ex2", r"""
**1) a)**
$$z_1 = \dfrac{(-1 + 7i)(3 - 4i)}{25} = \dfrac{25 + 25i}{25} = 1 + i, \qquad z_2 = (1 + i)^2 = 2i, \qquad z_3 = \dfrac{(4 - 8i)(1 - 3i)}{10} = \dfrac{-20 - 20i}{10} = -2 - 2i.$$

**b)**
- $z_1 = \sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$ ;
- $z_2 = 2\left(\cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}\right)$ ;
- $z_3 = 2\sqrt{2}\left(\cos\left(-\dfrac{3\pi}{4}\right) + i\sin\left(-\dfrac{3\pi}{4}\right)\right)$.

**2. a)** On place $A(1;1)$, $B(0;2)$ et $C(-2;-2)$. Leurs affixes sont $z_1$, $z_2$ et $z_3$.

**b)** $\dfrac{z_C - z_A}{z_B - z_A} = \dfrac{-3 - 3i}{-1 + i} = \dfrac{(-3 - 3i)(-1 - i)}{2} = \dfrac{6i}{2} = 3i$.

C'est un imaginaire pur, donc $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $ABC$ est **rectangle en $A$**.

**c)** $\left|\dfrac{z + 2 + 2i}{z - 2i}\right| = 1 \iff |z - z_C| = |z - z_B| \iff MC = MB$ (avec $M \neq B$, automatique sur cet ensemble).

$\Delta$ est la **médiatrice de $[BC]$**.

**d)** $ABCD$ est un parallélogramme $\iff \overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = 1 + i - 2 - 2i - 2i = -1 - 3i$.

Comme l'angle en $A$ est droit, $ABCD$ est même un **rectangle**.

**3)** $\Delta' = 1 - 10 = -9 = (3i)^2$, donc $S = \{-1 - 3i ;\ -1 + 3i\}$.
""")

_add("bac-d-2014-sc-math-ex3", r"""
**1. a)** $f(x) = x^2e^x + 2xe^x + e^x$, et chacun des termes tend vers $0$ en $-\infty$. Donc $\lim\limits_{x \to -\infty} f(x) = 0$ : l'axe des abscisses ($y = 0$) est **asymptote** à $(C)$ en $-\infty$.

**b)** $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\dfrac{f(x)}{x} = \dfrac{(x + 1)^2}{x}e^x \to +\infty$ : **branche parabolique de direction $(Oy)$** en $+\infty$.

**2. a)** $f'(x) = (2x + 2)e^x + (x^2 + 2x + 1)e^x = (x^2 + 4x + 3)e^x = (x + 1)(x + 3)e^x$.

$f'$ s'annule en $-3$ et en $-1$ : $(C)$ a deux tangentes horizontales :
- au point $\left(-3;4e^{-3}\right)$, d'équation $y = 4e^{-3}$ ;
- au point $(-1;0)$, d'équation $y = 0$.

**b)**

| $x$ | $-\infty$ | | $-3$ | | $-1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
| $f(x)$ | $0$ | ↗ | $4e^{-3}$ | ↘ | $0$ | ↗ | $+\infty$ |

($4e^{-3} \approx 0{,}2$.)

**3)** $f(x) = 0 \iff (x + 1)^2 = 0 \iff x = -1$ : le seul point commun avec l'axe des abscisses est $(-1;0)$, où $(C)$ est tangente à l'axe. Avec l'axe des ordonnées : $f(0) = 1$, point $(0;1)$.

**4) a)** Sur $[0;+\infty[$, $g$ est continue et strictement croissante : elle réalise une bijection de $[0;+\infty[$ sur $J = [1;+\infty[$.

**b)** $f(0) = 1$ et $f'(0) = 3$ : $T : y = 3x + 1$.

$g(0) = 1$ et $g'(0) = 3 \neq 0$, donc $\left(g^{-1}\right)'(1) = \dfrac{1}{g'(0)} = \dfrac{1}{3}$.

**5. a)** $F'(x) = (2ax + b)e^x + (ax^2 + bx + c)e^x = \big(ax^2 + (2a + b)x + b + c\big)e^x$.

$F' = f \iff a = 1$, $2a + b = 2$ et $b + c = 1$, soit $a = 1$, $b = 0$ et $c = 1$ :
$$F(x) = (x^2 + 1)e^x.$$

**b)** $f \ge 0$, donc l'aire vaut
$$\int_{-1}^{0} f(x)\,dx = F(0) - F(-1) = 1 - 2e^{-1} \approx 0{,}26 \text{ cm}^2.$$
""")

_add("bac-d-2014-sc-math-ex4", r"""
**Partie A**

**1. a)** $\lim\limits_{x \to 0^+} g(x) = +\infty$ (car $-\ln x \to +\infty$) et $\lim\limits_{x \to +\infty} g(x) = -\infty$.

**b)** $g'(x) = -1 - \dfrac{1}{x} < 0$ : $g$ est strictement décroissante sur $]0;+\infty[$, de $+\infty$ à $-\infty$.

**2. a)** $g$ est continue et strictement décroissante : elle réalise une bijection de $]0;+\infty[$ sur $J = \mathbb{R}$.

**b)** $0 \in J$ : une unique solution $\alpha$. $g(1{,}55) \approx 0{,}012 > 0$ et $g(1{,}56) \approx -0{,}005 < 0$, donc $1{,}55 \le \alpha \le 1{,}56$.

**c)** $g(x) > 0$ sur $]0;\alpha[$, $g(\alpha) = 0$, et $g(x) < 0$ sur $]\alpha;+\infty[$.

**Partie B**

**1. a)** En $0^+$ : $1 - \dfrac{1}{x} \to -\infty$ et $1 - \ln x \to +\infty$, donc $f(x) \to -\infty$.

En $+\infty$ : $1 - \dfrac{1}{x} \to 1$ et $1 - \ln x \to -\infty$, donc $f(x) \to -\infty$.

$\dfrac{f(x)}{x} = \left(1 - \dfrac{1}{x}\right)\left(\dfrac{1}{x} - \dfrac{\ln x}{x}\right) \to 1 \times 0 = 0$.

**b)** La droite $x = 0$ est **asymptote verticale** ; en $+\infty$, $(C)$ a une **branche parabolique de direction $(Ox)$**.

**2. a)**
$$f'(x) = \dfrac{1}{x^2}(1 - \ln x) + \left(1 - \dfrac{1}{x}\right)\left(-\dfrac{1}{x}\right) = \dfrac{1 - \ln x - (x - 1)}{x^2} = \dfrac{2 - x - \ln x}{x^2} = \dfrac{g(x)}{x^2}.$$

**b)** $g(\alpha) = 0$ donne $\ln\alpha = 2 - \alpha$, donc
$$f(\alpha) = \dfrac{\alpha - 1}{\alpha}\,(1 - 2 + \alpha) = \dfrac{(\alpha - 1)^2}{\alpha}.$$

Avec $\alpha \approx 1{,}557$ : $f(\alpha) \approx 0{,}2$ à $10^{-1}$ près.

**c)**

| $x$ | $0$ | | $\alpha$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | ‖ | $+$ | $0$ | $-$ | |
| $f(x)$ | ‖ $-\infty$ | ↗ | $f(\alpha)$ | ↘ | $-\infty$ |

**3)** $f(x) = 0 \iff 1 - \dfrac{1}{x} = 0$ ou $1 - \ln x = 0 \iff x = 1$ ou $x = e$. Les points d'intersection sont $(1;0)$ et $(e;0)$.

On trace l'asymptote $x = 0$, le maximum $(\alpha;f(\alpha))$ et ces deux points.

**4. a)** Par parties, avec $u = \ln t$ et $v' = 1$ :
$$I = \int_1^x \ln t\,dt = \big[t\ln t\big]_1^x - \int_1^x dt = x\ln x - x + 1.$$

**b)** Une primitive de $\ln x$ est $x\ln x - x$, une primitive de $\dfrac{1}{x}$ est $\ln x$, et une primitive de $\dfrac{\ln x}{x}$ est $\dfrac{(\ln x)^2}{2}$. Donc
$$F(x) = x - (x\ln x - x) - \ln x + \dfrac{(\ln x)^2}{2} = 2x - x\ln x - \ln x + \dfrac{(\ln x)^2}{2}.$$

**c)** Sur $[1;e]$, $1 - \dfrac{1}{x} \ge 0$ et $1 - \ln x \ge 0$, donc $f(x) \ge 0$ et
$$S = F(e) - F(1) = \left(2e - e - 1 + \dfrac{1}{2}\right) - 2 = e - \dfrac{5}{2} \text{ u.a.} \approx 0{,}22 \text{ u.a.}$$
""")


# ─────────────────────────────────────────────────────────────────────────────
# Contrôles mathématiques des corrections (rejoués par scripts/check_content.py).
CHECKS: dict[str, list[str]] = {
    "bac-d-2014-sn-math-ex1": [
        "binomial(6, 2) == 15 and binomial(4, 2) + 1 == 7",
        "Rational(1 + 1 + 1, 7) == Rational(3, 7)",
    ],
    "bac-d-2014-sn-math-ex2": [
        "set(solve(z**2 - 2*z + 17, z)) == {1 + 4*I, 1 - 4*I} and set(solve(z**2 + 8*z + 17, z)) == {-4 + I, -4 - I}",
        "expand(I*(5 - 3*I)) == 3 + 5*I",
        "simplify((-1 + 4*I - 1 + 4*I)/(-1 + 4*I + 4 + I)) == 1 + I",
        "expand((1 + I)/2*(4 + I)) == Rational(3, 2) + 5*I/2 and expand((1 + I)/2*(Rational(3, 2) + 5*I/2)) == -Rational(1, 2) + 2*I",
        "close(sqrt(17)/(1 - sqrt(2)/2), sqrt(17)*(2 + sqrt(2)))",
        "all(close(sum(Abs(((1 + I)/2)**j*(4 + I)) for j in range(k + 1)), sqrt(17)*(1 - (sqrt(2)/2)**(k + 1))/(1 - sqrt(2)/2)) for k in range(5))",
    ],
    "bac-d-2014-sn-math-ex3": [
        "racine(2*x - 1 + 2*exp(x), -0.3, -0.2)",
        "en_racine(2*x - 1 + 2*exp(x), -0.3, -0.2, D(2*x - 1 + 2*exp(x)), 3 - 2*x)",
        "all(close(sum(2*j - 1 + 2*exp(j) for j in range(k + 1)), k**2 - 1 + 2*(exp(k + 1) - 1)/(E - 1)) for k in range(6))",
    ],
    "bac-d-2014-sn-math-ex4": [
        "same(D(x - 3 + 3*log(x)), 1 + 3/x)",
        "same(D(log(x) - 3*log(x)/x), (x - 3 + 3*log(x))/x**2)",
        "abs(float((-(x - 3)**2/(3*x)).subs(x, root_in(x - 3 + 3*log(x), 1.59, 1.60))) + 0.411) < 0.001",
        "close(D((x - 3)*log(x)/x).subs(x, 1), -2)",
        "same(D((x - 3)*log(x)/x + 2*x), (2*x**2 + x - 3 + 3*log(x))/x**2)",
        "close(((x - 3)*log(x)/x + 2*x).subs(x, 1), 2)",
        "integ(log(x)/x, 1, E, Rational(1, 2)) and integ(log(x), 1, E, 1)",
        "integ(-(x - 3)*log(x)/x, 1, E, Rational(1, 2))",
    ],
    "bac-d-2014-sc-math-ex1": [
        "8*Rational(1, 4) == 2",
    ],
    "bac-d-2014-sc-math-ex2": [
        "simplify((-1 + 7*I)/(3 + 4*I)) == 1 + I and expand((1 + I)**2) == 2*I and simplify((4 - 8*I)/(1 + 3*I)) == -2 - 2*I",
        "close(-2 - 2*I, 2*sqrt(2)*exp(-3*I*pi/4))",
        "simplify((-3 - 3*I)/(-1 + I)) == 3*I",
        "(1 + I) + (-2 - 2*I) - 2*I == -1 - 3*I",
        "set(solve(z**2 + 2*z + 10, z)) == {-1 + 3*I, -1 - 3*I}",
    ],
    "bac-d-2014-sc-math-ex3": [
        "same(D((x + 1)**2*exp(x)), (x + 1)*(x + 3)*exp(x))",
        "close(((x + 1)**2*exp(x)).subs(x, -3), 4*exp(-3))",
        "same(D((x**2 + 1)*exp(x)), (x + 1)**2*exp(x))",
        "integ((x + 1)**2*exp(x), -1, 0, 1 - 2*exp(-1))",
    ],
    "bac-d-2014-sc-math-ex4": [
        "racine(2 - x - log(x), 1.55, 1.56)",
        "same(D((1 - 1/x)*(1 - log(x))), (2 - x - log(x))/x**2)",
        "abs(float(((x - 1)**2/x).subs(x, root_in(2 - x - log(x), 1.55, 1.56))) - 0.199) < 0.001",
        "same(D(2*x - x*log(x) - log(x) + log(x)**2/2), (1 - 1/x)*(1 - log(x)))",
        "integ((1 - 1/x)*(1 - log(x)), 1, E, E - Rational(5, 2))",
        "same(Integral(log(t), (t, 1, x)).doit(), x*log(x) - x + 1)",
    ],
    "bac-d-2013-sn-math-ex1": [
        "binomial(6, 2) == 15 and Rational(binomial(4, 2), 15) == Rational(6, 15)",
        "Rational(4*2, 15) + Rational(6, 15) + Rational(1, 15) == 1",
        "Rational(8, 15) + 2*Rational(1, 15) == Rational(2, 3)",
    ],
    "bac-d-2013-sn-math-ex2": [
        "set(solve(z**2 + 2*z + 10, z)) == {-1 + 3*I, -1 - 3*I} and set(solve(z**2 - 4*z + 20, z)) == {2 + 4*I, 2 - 4*I}",
        "(-1 - 3*I) - (-1 + 3*I) == (2 - 4*I) - (2 + 2*I)",
        "Abs(3 + I) == Abs(3 - I) and close((3 - I)/(3 + I), Rational(4, 5) - 3*I/5)",
        "close(Abs(-3 - I), sqrt(10))",
    ],
    "bac-d-2013-sn-math-ex3": [
        "[6, 3*6 + 0 - 13, 3*5 + 10 - 13, 3*12 + 20 - 13] == [6, 5, 12, 43]",
        "all(2*3**k - 5*k + 4 + 5*k - 4 == 2*3**k for k in range(8))",
        "2*3**6 < 2013 <= 2*3**7",
        "all(sum(2*3**j - 5*j + 4 for j in range(k + 1)) == 3**(k + 1) + 3 + Rational(3*k - 5*k**2, 2) for k in range(10))",
    ],
    "bac-d-2013-sn-math-ex4": [
        "same(D(x**3 - 3 + 2*log(x)), 3*x**2 + 2/x)",
        "racine(x**3 - 3 + 2*log(x), 1.34, 1.35)",
        "same(D(x - 2 + (1 - log(x))/x**2), (x**3 - 3 + 2*log(x))/x**3)",
        "en_racine(x**3 - 3 + 2*log(x), 1.34, 1.35, x - 2 + (1 - log(x))/x**2, (3*x**3 - 4*x**2 - 1)/(2*x**2))",
        "abs(float((x - 2 + (1 - log(x))/x**2).subs(x, root_in(x**3 - 3 + 2*log(x), 1.34, 1.35))) + 0.266) < 0.001",
        "close((x - 2 + (1 - log(x))/x**2).subs(x, 1), 0) and close(D(x - 2 + (1 - log(x))/x**2).subs(x, 1), -2)",
        "racine(x - 2 + (1 - log(x))/x**2, 1.9, 2)",
        "integ((-1 + log(x))/x**2, 3, 10, log(3)/3 - log(10)/10)",
        "integ(log(x)/x**2, 3, 10, -log(10)/10 + log(3)/3 + Rational(1, 3) - Rational(1, 10))",
    ],
    "bac-d-2013-sc-math-ex1": [
        "15 + 3*10 == 45 and Rational(8*(30 + 21), 2) == 204",
        "Rational(15, 18) != Rational(18, 21)",
    ],
    "bac-d-2013-sc-math-ex2": [
        "set(solve(z**2 - 6*z + 18, z)) == {3 + 3*I, 3 - 3*I}",
        "set(solve(z**2 - 2*sqrt(3)*z + 4, z)) == {sqrt(3) + I, sqrt(3) - I}",
        "close(3 + 3*I, 3*sqrt(2)*exp(I*pi/4)) and close(sqrt(3) - I, 2*exp(-I*pi/6))",
        "simplify((3 + 3*I)*(sqrt(3) - I) - ((3 + 3*sqrt(3)) + I*(3*sqrt(3) - 3))) == 0",
        "close((3 + 3*I)*(sqrt(3) - I), 6*sqrt(2)*exp(I*pi/12))",
        "close(cos(pi/12), (sqrt(2) + sqrt(6))/4) and close(sin(pi/12), (sqrt(6) - sqrt(2))/4)",
    ],
    "bac-d-2013-sc-math-ex3": [
        "lim((x - 2 + log(x + 1))/x, oo, 1)",
        "racine(x - 2 + log(x + 1), 1.2, 1.3)",
        "same(D((x + 1)*log(x + 1)) + x - 3, x - 2 + log(x + 1))",
        "same(D((x + 1)*log(x + 1) + x**2/2 - 3*x), x - 2 + log(x + 1))",
        "en_racine(x - 2 + log(x + 1), 1.2, 1.3, -((x + 1)*log(x + 1) + x**2/2 - 3*x), x**2/2 + 2*x - 2)",
        "close((x - 2 + log(x + 1)).subs(x, 0), -2) and close(D(x - 2 + log(x + 1)).subs(x, 0), 2)",
    ],
    "bac-d-2013-sc-math-ex4": [
        "lim((2*x + 3)*exp(x + 1) + 1, -oo, 1)",
        "same(D((2*x + 3)*exp(x + 1) + 1), (2*x + 5)*exp(x + 1))",
        "close(((2*x + 3)*exp(x + 1) + 1).subs(x, -Rational(5, 2)), 1 - 2*exp(-Rational(3, 2))) and float(1 - 2*exp(-Rational(3, 2))) > 0",
        "same(D(x - 3 + (2*x + 1)*exp(x + 1)), (2*x + 3)*exp(x + 1) + 1)",
        "racine(x - 3 + (2*x + 1)*exp(x + 1), 0, 0.1)",
        "close((x - 3 + (2*x + 1)*exp(x + 1)).subs(x, -Rational(1, 2)), -Rational(7, 2))",
        "close((x - 3 + (2*x + 1)*exp(x + 1)).subs(x, -Rational(3, 2)), -Rational(9, 2) - 2*exp(-Rational(1, 2)))",
        "close(((2*x + 1)*exp(x + 1)).subs(x, -Rational(3, 2)), -2*exp(-Rational(1, 2)))",
    ],
    "bac-d-2012-sn-math-ex1": [
        "close(0.2 + 0.3 - 0.1, 0.4) and close(1 - 0.4, 0.6) and close(0.4 - 0.1, 0.3)",
        "(Rational(3, 10) - Rational(1, 10))/Rational(3, 10) == Rational(2, 3)",
        "close(0*0.6 + 1*0.3 + 2*0.1, 0.5) and close(0.6 + 0.3 + 0.1, 1)",
    ],
    "bac-d-2012-sn-math-ex2": [
        "simplify((2 + I)/(1 - 2*I)) == I and (2 + I) + (1 - 2*I) == 3 - I",
        "simplify((3 - I - 2 - I)/(3 - I - 1 + 2*I)) == -I",
        "close(Abs((-1 - 3*I)), sqrt(10))",
        "close(2 + 2*I, 2*sqrt(2)*exp(I*pi/4))",
    ],
    "bac-d-2012-sn-math-ex3": [
        "lim(exp(-2*x - 1)/x, -oo, -oo)",
        "close((-2*exp(-2*x - 1) + 3).subs(x, -(1 + log(Rational(3, 2)))/2), 0)",
        "close((exp(-2*x - 1) + 3*x - 1).subs(x, -(1 + log(Rational(3, 2)))/2), -1 - Rational(3, 2)*log(Rational(3, 2)))",
        "racine(exp(-2*x - 1) + 3*x - 1, -1.3, -1.2) and racine(exp(-2*x - 1) + 3*x - 1, 0.2, 0.3)",
        "all(close(sum(exp(-2*j - 1) + 3*j - 1 for j in range(k + 1)), exp(-1)*(1 - exp(-2*(k + 1)))/(1 - exp(-2)) + Rational((k + 1)*(3*k - 2), 2)) for k in range(6))",
        "lim(Rational(3, 2)*(x + 1)*(3*x - 2)/(3*x**2), oo, Rational(3, 2))",
    ],
    "bac-d-2012-sn-math-ex4": [
        "lim((2*x + 1)/(x + 1) - log(x + 1), -1, -oo, '+')",
        "same(D((2*x + 1)/(x + 1) - log(x + 1)), -x/(x + 1)**2)",
        "same(D((2*x + 1)/(x + 1) - log(x + 1), 2), (x - 1)/(x + 1)**3)",
        "close(((2*x + 1)/(x + 1) - log(x + 1)).subs(x, 1), Rational(3, 2) - log(2))",
        "close(D((2*x + 1)/(x + 1) - log(x + 1)).subs(x, 1), -Rational(1, 4))",
        "same(D(3*x - (x + 2)*log(x + 1)), (2*x + 1)/(x + 1) - log(x + 1))",
        "en_racine((2*x + 1)/(x + 1) - log(x + 1), 5.3, 5.4, 3*x - (x + 2)*log(x + 1), 3*x - (x + 2)*(2*x + 1)/(x + 1))",
        "en_racine((2*x + 1)/(x + 1) - log(x + 1), 5.3, 5.4, Integral((2*t + 1)/(t + 1) - log(t + 1), (t, 0, x)).doit(), 3*x - (x + 2)*log(x + 1))",
        "abs(float((3*x - (x + 2)*log(x + 1)).subs(x, root_in((2*x + 1)/(x + 1) - log(x + 1), 5.3, 5.4))) - 2.46) < 0.005",
    ],
    "bac-d-2012-sc-math-ex1": [
        "1 + 3**0 == 2",
        "all((lambda u: u)(1 + 3**(k + 1)) == 3*(1 + 3**k) - 2 for k in range(10))",
        "all(sum(1 + 3**j for j in range(k + 1)) == k + Rational(1, 2) + Rational(3**(k + 1), 2) for k in range(10))",
    ],
    "bac-d-2012-sc-math-ex2": [
        "set(solve(z**2 - 2*z + 5, z)) == {1 + 2*I, 1 - 2*I}",
        "simplify((1 - 2*I - 2 - I)/(1 - 2*I + 3 + 2*I)) == -Rational(1, 4) - 3*I/4",
        "simplify((1 + 2*I - 2 - I)/(1 + 2*I + 3 + 2*I)) == I/4",
        "close(Abs(-5 - 3*I), sqrt(34))",
    ],
    "bac-d-2012-sc-math-ex3": [
        "lim(x - 2 - 2*log(x), 0, oo, '+') and lim((x - 2 - 2*log(x))/x, oo, 1)",
        "same(D(x - 2 - 2*log(x)), (x - 2)/x)",
        "close((x - 2 - 2*log(x)).subs(x, 2), -2*log(2)) and close((x - 2 - 2*log(x)).subs(x, 1), -1)",
        "same(D(2*x - 2 - 2*log(x)), 2 - 2/x) and close((2*x - 2 - 2*log(x)).subs(x, 1), 0)",
        "integ(log(x), 1, 2, 2*log(2) - 1)",
        "integ(-(x - 2 - 2*log(x)), 1, 2, 4*log(2) - Rational(3, 2))",
    ],
    "bac-d-2012-sc-math-ex4": [
        "same(D(x*exp(x) - 1), (x + 1)*exp(x)) and close((x*exp(x) - 1).subs(x, -1), -1 - exp(-1))",
        "lim((exp(x) - x)/(x + 1), -1, -oo, '-') and lim((exp(x) - x)/(x + 1), -1, oo, '+')",
        "lim((exp(x) - x)/(x*(x + 1)), oo, oo)",
        "en_racine(x*exp(x) - 1, 0.5, 0.6, (exp(x) - x)/(x + 1), (1 - x**2)/(x**2 + x))",
        "abs(float(((exp(x) - x)/(x + 1)).subs(x, root_in(x*exp(x) - 1, 0.5, 0.6))) - 0.763) < 0.001",
    ],
    "bac-d-2011-sn-math-ex1": [
        "6*Rational(4, 7) == Rational(24, 7)",
        "close(binomial(6, 5)*Rational(3, 7)**5*Rational(4, 7), binomial(6, 1)*Rational(4, 7)*Rational(3, 7)**5)",
    ],
    "bac-d-2011-sn-math-ex2": [
        "set(solve(z**3 - 5*z**2 + 12*z - 8, z)) == {1, 2 + 2*I, 2 - 2*I}",
        "simplify((2 + 2*I)/(2 - 2*I)) == I",
        "all(close(Abs(t + I*(Rational(7, 4) - t/2) - 1), Abs(t + I*(Rational(7, 4) - t/2) - 2 - 2*I)) for t in [-1, 0, 2, 5])",
    ],
    "bac-d-2011-sn-math-ex3": [
        "lim((x + 2)*exp(x), -oo, 0) and lim((x + 2)*exp(x)/x, oo, oo)",
        "same(D((x + 2)*exp(x)), (x + 3)*exp(x))",
        "same(D((x + 1)*exp(x)), (x + 2)*exp(x))",
        "integ((x + 2)*exp(x), -2, 0, 1 + exp(-2))",
        "close(((x + 2)*exp(x)).subs(x, 1), 3*E) and close(((x + 2)*exp(x)).subs(x, Rational(1, 2)), Rational(5, 2)*sqrt(E))",
    ],
    "bac-d-2011-sn-math-ex4": [
        "lim(x - 1 + (1 + log(x))/x, 0, -oo, '+') and lim((1 + log(x))/x, oo, 0)",
        "same(D(x - 1 + (1 + log(x))/x), (x**2 - log(x))/x**2)",
        "close((x**2 - log(x)).subs(x, 1/sqrt(2)), (1 + log(2))/2)",
        "racine(x - 1 + (1 + log(x))/x, 1/E, 0.5)",
        "close((x - 1 + (1 + log(x))/x).subs(x, Rational(1, 2)), Rational(3, 2) - 2*log(2))",
        "solve(Eq(D(x - 1 + (1 + log(x))/x), 1), x) == [1] and close((x - 1 + (1 + log(x))/x).subs(x, 1), 1)",
        "same(D((1 + log(x))/x), -log(x)/x**2)",
        "integ((1 + log(x))/x, 3, 4, log(Rational(4, 3)) + (log(4)**2 - log(3)**2)/2)",
        "lim(log(1 + 1/x) + (log(x + 1)**2 - log(x)**2)/2, oo, 0)",
    ],
    "bac-d-2011-sc-math-ex1": [
        "Rational(11 + 4 + 1, 20) == Rational(4, 5) and Rational(1 + 3 + 11, 20) == Rational(3, 4)",
        "(Rational(748, 10) + 3*Rational(749, 10) + 11*75 + 4*Rational(751, 10) + Rational(752, 10))/20 == Rational(75005, 1000)",
    ],
    "bac-d-2011-sc-math-ex2": [
        "expand((1 + I)**2 - 2*(1 + I)) == -2 and expand((1 + sqrt(3)*I)**2 - 2*(1 + sqrt(3)*I)) == -4",
        "set(solve(z**2 - 2*z + 2, z)) == {1 + I, 1 - I} and set(solve(z**2 - 2*z + 4, z)) == {1 + sqrt(3)*I, 1 - sqrt(3)*I}",
        "simplify((1 + I)*(1 + sqrt(3)*I) - ((1 - sqrt(3)) + I*(1 + sqrt(3)))) == 0",
        "close((1 + I)*(1 + sqrt(3)*I), 2*sqrt(2)*exp(7*I*pi/12))",
        "close(cos(7*pi/12), (sqrt(2) - sqrt(6))/4) and close(sin(7*pi/12), (sqrt(2) + sqrt(6))/4)",
    ],
    "bac-d-2011-sc-math-ex3": [
        "[Rational(k**2, 2**k) for k in (2, 3, 4, 5)] == [1, Rational(9, 8), 1, Rational(25, 32)]",
        "all(Rational((k + 1)**2, 2**(k + 1)) <= Rational(25, 32)*Rational(3, 4)**(k - 5) for k in range(5, 40))",
        "Rational(5**2, 2**5) == Rational(25, 32)*Rational(3, 4)**0",
        "all(Rational((k + 1)**2, 2**(k + 1)) < Rational(25, 32)*Rational(3, 4)**(k + 1 - 5) for k in range(5, 40))",
    ],
    "bac-d-2011-sc-math-ex4": [
        "lim((2*x - 1 + log(x))/x, oo, 2) and lim(log(x) - 1, oo, oo)",
        "racine(2*x - 1 + log(x), 0.6, 0.7)",
        "close((2*x - 1 + log(x)).subs(x, 1), 1)",
        "en_racine(2*x - 1 + log(x), 0.6, 0.7, Integral(log(t), (t, x, 1)).doit(), 2*x**2 - 1)",
        "en_racine(2*x - 1 + log(x), 0.6, 0.7, Integral(2*t - 1 + log(t), (t, x, 1)).doit(), x**2 + x - 1)",
        "same((2*x - 1 + log(x)).subs(x, exp(x)), x - 1 + 2*exp(x))",
        "en_racine(2*x - 1 + log(x), 0.6, 0.7, log(x), 1 - 2*x)",
        "lim((x - 1 + 2*exp(x))/x, oo, oo)",
    ],
    "bac-d-2010-sn-math-ex2": [
        "expand((z - 3)*(z**2 + 2*z + 2)) == expand(z**3 - z**2 - 4*z - 6)",
        "set(solve(z**3 - z**2 - 4*z - 6, z)) == {3, -1 + I, -1 - I}",
        "simplify(((3 + 2*I) + (-1 - I))/2 - ((-1 + I) + 3)/2) == 0",
        "Abs(-4 - I) == sqrt(17) and (-4)*0 + (-1)*(-2) == 2",
        # médiatrice de [BD] : y = 4x - 7/2  <=>  |z - 3| = |z + 1 - i|
        "all(close(Abs(t + I*(4*t - Rational(7, 2)) - 3), Abs(t + I*(4*t - Rational(7, 2)) + 1 - I)) for t in [-2, 0, 1, 3])",
    ],
    "bac-d-2010-sn-math-ex3": [
        "[Rational(k**2 + k + 1, k*(k + 1)) for k in (1, 2, 3)] == [Rational(3, 2), Rational(7, 6), Rational(13, 12)]",
        "Rational(7, 6) - Rational(3, 2) != Rational(13, 12) - Rational(7, 6)",
        "Rational(7, 6)/Rational(3, 2) != Rational(13, 12)/Rational(7, 6)",
        "all(sum(Rational(j**2 + j + 1, j*(j + 1)) for j in range(1, k + 1)) == Rational(k*(k + 2), k + 1) for k in range(1, 12))",
        "all(close(sum(log(Rational(j**2 - 1, j)) for j in range(2, k + 1)), log(factorial(k + 1)/(2*Integer(k)))) for k in range(2, 10))",
        "lim((x**2 + x + 1)/(x*(x + 1)), oo, 1)",
    ],
    "bac-d-2010-sn-math-ex4": [
        "lim(exp(x), -oo, 0) and lim((x + 2 + exp(x))/x, oo, oo)",
        "racine(x + 2 + exp(x), -2.5, -2)",
        "same(D(x**2/2 + 2*x + exp(x) - 1), x + 2 + exp(x)) and close((x**2/2 + 2*x + exp(x) - 1).subs(x, 0), 0)",
        "en_racine(x + 2 + exp(x), -2.5, -2, -(x**2/2 + 2*x + exp(x) - 1), (6 - 2*x - x**2)/2)",
        "abs(float(((6 - 2*x - x**2)/2).subs(x, root_in(x + 2 + exp(x), -2.5, -2))) - 2.87) < 0.01",
        "en_racine(x + 2 + exp(x), -2.5, -2, 1 + exp(x), -(x + 1))",
        "racine(x + 1 + exp(x), -1.3, -1.25)",
        "lim(log(x + 2 + exp(x)) - x, oo, 0)",
        "close(log(3), 1.0986122886681098, 1e-12)",
    ],
    "bac-d-2010-sc-math-ex1": [
        "17 + 5*3 == 32",
        "[k for k in range(60) if Rational((k + 1)*(11 + 10*k), 2) == 2010] == [19]",
        "all(10**(k + 1)*factorial(k) > 10**k*factorial(k + 1) for k in range(0, 9))",
        "10**10*factorial(9) == 10**9*factorial(10)",
        "all(10**(k + 1)*factorial(k) < 10**k*factorial(k + 1) for k in range(10, 30))",
    ],
    "bac-d-2010-sc-math-ex2": [
        "set(solve(z**2 - 4*z + 13, z)) == {2 + 3*I, 2 - 3*I}",
        "close(3 + 3*I, 3*sqrt(2)*exp(I*pi/4)) and close(2 - 2*I, 2*sqrt(2)*exp(-I*pi/4))",
        "simplify((3 + 3*I)/(2 - 2*I)) == Rational(3, 2)*I",
        "(3 + 3*I) + (2 - 2*I) == 5 + I",
        "close(Abs((5 + I) - (Rational(5, 2) + I/2)), sqrt(26)/2) and close(Abs(0 - (Rational(5, 2) + I/2)), sqrt(26)/2)",
    ],
    "bac-d-2010-sc-math-ex3": [
        "lim(1/x + log(x), 0, oo, '+')",
        "same(D(1/x + log(x)), (x - 1)/x**2)",
        "close((1/x + log(x)).subs(x, 1), 1)",
        "integ(log(x), 1, E, 1)",
        "integ(1/x + log(x), 1, E, 2)",
    ],
    "bac-d-2010-sc-math-ex4": [
        "lim(exp(x)/(exp(x) - 1), 0, oo, '+') and lim(exp(x)/(exp(x) - 1), 0, -oo, '-')",
        "lim(exp(x)/(exp(x) - 1), -oo, 0) and lim(exp(x)/(exp(x) - 1), oo, 1)",
        "same(D(exp(x)/(exp(x) - 1)), -exp(x)/(exp(x) - 1)**2)",
        "same(log(x/(x - 1)), log(x/(x - 1))) and all(close((exp(x)/(exp(x) - 1)).subs(x, log(Rational(p, p - 1))), p) for p in (2, 3, 7))",
        "same(exp(-x)/(exp(-x) - 1) + exp(x)/(exp(x) - 1), 1 + 0*x)",
        "integ(exp(x)/(exp(x) - 1), Rational(1, 3), 1, log(E - 1) - log(exp(Rational(1, 3)) - 1))",
    ],
}
