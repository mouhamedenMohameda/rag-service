"""Corrections refaites par Claude pour les exercices de math Bac C 2007-2014.

Chaque entrée : CORRECTIONS["bac-c-<année>-<sn|sc>-math-ex<n>"] = correction_string

Style : reprend la méthodologie des corrigés mauritaniens originaux
(T.V., A.H., B.P., I.P.P., \\Leftrightarrow, \\boxed, tableaux markdown).
"""

CORRECTIONS = {}

# ============================================================================
# BAC C 2014 — Session Normale (déjà faits dans la conversation précédente)
# ============================================================================

CORRECTIONS["bac-c-2014-sn-math-ex1"] = r"""## Exercice 1

### 1) Calcul de $P(2i)$ et résolution de $P(z)=0$

$P(2i)=(2i)^3+(1-2i)(2i)^2+(1-2i)(2i)-2i$

$=-8i+(1-2i)(-4)+(2i+4)-2i$

$=-8i-4+8i+2i+4-2i=0$

Donc $P(2i)=0$, c'est-à-dire $2i$ est racine de $P$.

Division de $P(z)$ par $(z-2i)$ :

| | $1$ | $1-2i$ | $1-2i$ | $-2i$ |
|---|---|---|---|---|
| $2i$ | $\downarrow$ | $2i$ | $2i$ | $2i$ |
| | $1$ | $1$ | $1$ | $0$ |

D'où $P(z)=(z-2i)(z^2+z+1)$.

$P(z)=0 \Leftrightarrow z=2i \text{ ou } z^2+z+1=0$

Pour $z^2+z+1=0$ : $\Delta=1-4=-3=(i\sqrt 3)^2$

$z=\dfrac{-1\pm i\sqrt 3}{2}$

Comme $\Im(2i)=2$, $\Im\!\left(-\dfrac{1}{2}+i\dfrac{\sqrt 3}{2}\right)=\dfrac{\sqrt 3}{2}$ et $\Im\!\left(-\dfrac{1}{2}-i\dfrac{\sqrt 3}{2}\right)=-\dfrac{\sqrt 3}{2}$, on a $\Im z_0\geq\Im z_1\geq\Im z_2$ avec :

$$z_0=2i,\quad z_1=-\dfrac{1}{2}+i\dfrac{\sqrt 3}{2},\quad z_2=-\dfrac{1}{2}-i\dfrac{\sqrt 3}{2}$$

### 2) a) Équation cartésienne de $(BC)$

$B\!\left(-\dfrac{1}{2},\dfrac{\sqrt 3}{2}\right)$ et $C\!\left(-\dfrac{1}{2},-\dfrac{\sqrt 3}{2}\right)$ ont la même abscisse $-\dfrac{1}{2}$.

Donc $(BC):\ x=-\dfrac{1}{2}\Leftrightarrow 2x+1=0$. $\quad\blacksquare$

### 2) b) Image de $(BC)\setminus\{B,C\}$ par $f$

Soit $M\in(BC)\setminus\{B,C\}$, alors $z=-\dfrac{1}{2}+iy$ avec $y\in\mathbb R\setminus\!\left\{\pm\dfrac{\sqrt 3}{2}\right\}$.

D'après l'indication, $z^2+z+1=\left(z+\dfrac{1}{2}\right)^2+\dfrac{3}{4}=(iy)^2+\dfrac{3}{4}=\dfrac{3}{4}-y^2$.

Or $y\neq\pm\dfrac{\sqrt 3}{2}\Rightarrow\dfrac{3}{4}-y^2\neq 0$.

D'où $z'=f(z)=\dfrac{1}{\frac{3}{4}-y^2}\in\mathbb R$.

Donc $M'$ est situé sur l'axe des abscisses. $\quad\blacksquare$

### 3) a) Si $|z|=1$, alors $f(z)=\dfrac{\bar z}{1+z+\bar z}$

$|z|=1\Leftrightarrow z\bar z=1$. En multipliant le numérateur et le dénominateur de $f(z)$ par $\bar z$ :

$f(z)=\dfrac{1}{z^2+z+1}=\dfrac{\bar z}{\bar z\, z^2+\bar z\, z+\bar z}=\dfrac{\bar z}{z(z\bar z)+1+\bar z}=\dfrac{\bar z}{z+1+\bar z}=\dfrac{\bar z}{1+z+\bar z} \quad\blacksquare$

### 3) b) Cas $z=e^{i\theta}$

Si $z=e^{i\theta}$ avec $\theta\in[-\pi,\pi]\setminus\left\{\pm\dfrac{2\pi}{3}\right\}$, alors $\bar z=e^{-i\theta}$ et $|z|=1$.

$1+z+\bar z=1+e^{i\theta}+e^{-i\theta}=1+2\cos\theta\neq 0$ (car $\theta\neq\pm\dfrac{2\pi}{3}$).

$f(z)=\dfrac{e^{-i\theta}}{1+2\cos\theta}=\dfrac{\cos\theta-i\sin\theta}{1+2\cos\theta} \quad\blacksquare$

### 4) a) Lieu de $M'$ quand $M$ décrit le cercle unité privé de $B$ et $C$

D'après 3)b) : $\begin{cases}x'=\dfrac{\cos\theta}{1+2\cos\theta}\\ y'=\dfrac{-\sin\theta}{1+2\cos\theta}\end{cases}$

$x'^2+y'^2=\dfrac{\cos^2\theta+\sin^2\theta}{(1+2\cos\theta)^2}=\dfrac{1}{(1+2\cos\theta)^2}$

$2x'-1=\dfrac{2\cos\theta-(1+2\cos\theta)}{1+2\cos\theta}=\dfrac{-1}{1+2\cos\theta}$

D'où $(2x'-1)^2=\dfrac{1}{(1+2\cos\theta)^2}=x'^2+y'^2$.

Donc $M'$ appartient à la courbe $\Gamma$ d'équation $x^2+y^2=(2x-1)^2$. $\quad\blacksquare$

### 4) b) Nature de $\Gamma$

$\Gamma:\ x^2+y^2=(2x-1)^2=4x^2-4x+1$

$\Leftrightarrow 3x^2-4x-y^2+1=0$

$\Leftrightarrow 3\!\left(x^2-\dfrac{4}{3}x\right)-y^2=-1$

$\Leftrightarrow 3\!\left(x-\dfrac{2}{3}\right)^2-\dfrac{4}{3}-y^2=-1$

$\Leftrightarrow 3\!\left(x-\dfrac{2}{3}\right)^2-y^2=\dfrac{1}{3}$

$\Leftrightarrow \dfrac{(x-\frac{2}{3})^2}{\frac{1}{9}}-\dfrac{y^2}{\frac{1}{3}}=1$

$\Gamma$ est donc une **hyperbole** de paramètres $a^2=\dfrac{1}{9}$, $b^2=\dfrac{1}{3}$, soit $a=\dfrac{1}{3}$, $b=\dfrac{\sqrt 3}{3}$.

* **Centre** : $\Omega\!\left(\dfrac{2}{3},\,0\right)$
* **Sommets** : $S_1\!\left(1,0\right)$ et $S_2\!\left(\dfrac{1}{3},0\right)$ (car $\dfrac{2}{3}\pm\dfrac{1}{3}$)
* **Excentricité** : $c^2=a^2+b^2=\dfrac{1}{9}+\dfrac{3}{9}=\dfrac{4}{9}\Rightarrow c=\dfrac{2}{3}$, d'où $e=\dfrac{c}{a}=\dfrac{2/3}{1/3}=2$

Construction : hyperbole d'axe focal $(Ox)$, centrée en $\Omega(2/3,0)$, sommets en $(1/3,0)$ et $(1,0)$, asymptotes $y=\pm\sqrt 3\,(x-2/3)$.
"""

CORRECTIONS["bac-c-2014-sn-math-ex2"] = r"""## Exercice 2

### 1) a) Tableau de variation de $f(x)=xe^x$

$D_f=\mathbb R$ ; $f$ est continue et dérivable sur $\mathbb R$.

* $\displaystyle\lim_{x\to-\infty}xe^x=0$ (croissance comparée)
* $\displaystyle\lim_{x\to+\infty}xe^x=+\infty$

$f'(x)=e^x+xe^x=(x+1)e^x$, du signe de $x+1$.

$f'(x)=0\Leftrightarrow x=-1$ ; $f(-1)=-e^{-1}=-\dfrac{1}{e}$

**T.V. de $f$** :

| $x$ | $-\infty$ | | $-1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f'(x)$ | | $-$ | $0$ | $+$ | |
| $f(x)$ | $0$ | $\searrow$ | $-\frac{1}{e}$ | $\nearrow$ | $+\infty$ |

### 1) b) Tracé de $(C)$

* $y=0$ est A.H. à $(C)$ en $-\infty$.
* $\displaystyle\lim_{x\to+\infty}\dfrac{f(x)}{x}=\lim_{x\to+\infty}e^x=+\infty$ : $(C)$ admet une B.P. de direction $(Oy)$ en $+\infty$.
* $(C)\cap(Ox)=(C)\cap(Oy)=\{O(0,0)\}$.
* Minimum local en $x=-1$ de valeur $-1/e$.

### 1) c) $f$ vérifie $y''-2y'+y=0$

$f(x)=xe^x$, $f'(x)=(x+1)e^x$, $f''(x)=e^x+(x+1)e^x=(x+2)e^x$

$f''(x)-2f'(x)+f(x)=(x+2)e^x-2(x+1)e^x+xe^x=e^x\big[(x+2)-2(x+1)+x\big]=e^x\cdot 0=0$

Donc $f$ est solution de $y''-2y'+y=0$. $\quad\blacksquare$

### 1) d) Aire du domaine

$\forall x\in[0,1]$, $f(x)=xe^x\geq 0$, donc :

$\mathcal A=\displaystyle\int_0^1 xe^x\,dx$

I.P.P. : on pose $\begin{cases}u(x)=x\\ v'(x)=e^x\end{cases}\Rightarrow\begin{cases}u'(x)=1\\ v(x)=e^x\end{cases}$

$\mathcal A=\big[xe^x\big]_0^1-\displaystyle\int_0^1 e^x\,dx=e-\big[e^x\big]_0^1=e-(e-1)=1$

D'où $\boxed{\mathcal A=1\text{ u.a.}}$

### 2) a) $I_1=-1$

$I_n=(-1)^n\displaystyle\int_0^1 x^n e^x\,dx$, donc $I_1=-\displaystyle\int_0^1 xe^x\,dx=-\mathcal A=-1$. $\quad\blacksquare$

### 2) b) Encadrement et limite de $I_n$

Sur $[0,1]$ : $1\leq e^x\leq e$, donc en multipliant par $x^n\geq 0$ :

$x^n\leq x^n e^x\leq e\cdot x^n$

En intégrant sur $[0,1]$ : $\displaystyle\int_0^1 x^n\,dx\leq\int_0^1 x^n e^x\,dx\leq e\int_0^1 x^n\,dx$

Or $|I_n|=\displaystyle\int_0^1 x^n e^x\,dx$ (intégrand positif) et $\displaystyle\int_0^1 x^n\,dx=\dfrac{1}{n+1}$.

D'où $\boxed{\dfrac{1}{n+1}\leq|I_n|\leq\dfrac{e}{n+1}}$

Comme $\dfrac{1}{n+1}\to 0$ et $\dfrac{e}{n+1}\to 0$, par encadrement $|I_n|\to 0$, donc $\displaystyle\lim_{n\to+\infty}I_n=0$.

### 2) c) Relation de récurrence

I.P.P. dans $\displaystyle\int_0^1 x^{n+1}e^x\,dx$ : $\begin{cases}u(x)=x^{n+1}\\ v'(x)=e^x\end{cases}\Rightarrow\begin{cases}u'(x)=(n+1)x^n\\ v(x)=e^x\end{cases}$

$\displaystyle\int_0^1 x^{n+1}e^x\,dx=\big[x^{n+1}e^x\big]_0^1-(n+1)\int_0^1 x^n e^x\,dx=e-(n+1)\int_0^1 x^n e^x\,dx$

D'où :

$I_{n+1}=(-1)^{n+1}\!\left[e-(n+1)\displaystyle\int_0^1 x^n e^x\,dx\right]=(-1)^{n+1}e+(n+1)(-1)^n\int_0^1 x^n e^x\,dx$

$\boxed{I_{n+1}=(-1)^{n+1}e+(n+1)I_n} \quad\blacksquare$

### 2) d) Calcul de $J$

**Remarque :** d'après l'énoncé du sujet, l'intégrand comporte un facteur $e^x$ (manquant dans la transcription) : $J=\displaystyle\int_0^1\dfrac{(x^3+4x^2-3x-6)\,e^x}{x+1}\,dx$, sinon la valeur de $J$ ne serait pas de la forme $ae+b$.

Division euclidienne de $x^3+4x^2-3x-6$ par $x+1$ :

| | $1$ | $4$ | $-3$ | $-6$ |
|---|---|---|---|---|
| $-1$ | $\downarrow$ | $-1$ | $-3$ | $6$ |
| | $1$ | $3$ | $-6$ | $0$ |

D'où $x^3+4x^2-3x-6=(x+1)(x^2+3x-6)$ et :

$J=\displaystyle\int_0^1(x^2+3x-6)e^x\,dx=\int_0^1 x^2 e^x\,dx+3\int_0^1 xe^x\,dx-6\int_0^1 e^x\,dx$

Or $\displaystyle\int_0^1 x^n e^x\,dx=(-1)^n I_n$, donc :

* $\displaystyle\int_0^1 x^2 e^x\,dx=I_2$
* $\displaystyle\int_0^1 xe^x\,dx=-I_1=1$
* $\displaystyle\int_0^1 e^x\,dx=e-1$

Calcul de $I_2$ via la récurrence : $I_2=(-1)^2 e+2I_1=e+2(-1)=e-2$

D'où :

$J=(e-2)+3\cdot 1-6(e-1)=e-2+3-6e+6=-5e+7$

$\boxed{J=7-5e}\quad\text{avec }a=-5,\ b=7.$
"""

CORRECTIONS["bac-c-2014-sn-math-ex3"] = r"""## Exercice 3

### 1) a) Continuité de $f$ à droite en $0$

$f(0)=0$. Pour $x>0$ : $f(x)=x\ln\!\left(1+\dfrac{1}{x}\right)=x\ln(x+1)-x\ln x$.

* $\displaystyle\lim_{x\to 0^+}x\ln(x+1)=0\cdot\ln 1=0$
* $\displaystyle\lim_{x\to 0^+}x\ln x=0$ (croissance comparée)

D'où $\displaystyle\lim_{x\to 0^+}f(x)=0=f(0)$, donc $f$ est continue à droite en $0$. $\quad\blacksquare$

### 1) b) Dérivabilité à droite en $0$

$\displaystyle\lim_{x\to 0^+}\dfrac{f(x)-f(0)}{x-0}=\lim_{x\to 0^+}\ln\!\left(1+\dfrac{1}{x}\right)=+\infty$

Donc $f$ n'est pas dérivable à droite en $0$.

**Interprétation graphique :** $(\mathcal C_f)$ admet au point d'abscisse $0$ une demi-tangente verticale dirigée vers le haut.

### 1) c) Limite en $+\infty$

Posons $t=\dfrac{1}{x}$. Quand $x\to+\infty$, $t\to 0^+$ et :

$f(x)=x\ln\!\left(1+\dfrac{1}{x}\right)=\dfrac{1}{t}\ln(1+t)=\dfrac{\ln(1+t)}{t}\xrightarrow[t\to 0^+]{}1$

Donc $\displaystyle\lim_{x\to+\infty}f(x)=1$.

**Interprétation :** la droite $y=1$ est une A.H. à $(\mathcal C_f)$ en $+\infty$.

### 2) a) Calcul et signe de $f'(x)$

Pour $x>0$ :

$f'(x)=\ln\!\left(1+\dfrac{1}{x}\right)+x\cdot\dfrac{-\frac{1}{x^2}}{1+\frac{1}{x}}=\ln\!\left(1+\dfrac{1}{x}\right)-\dfrac{1}{x+1}$

Calcul de $f''(x)$ :

$f''(x)=\dfrac{-1/x^2}{1+\frac{1}{x}}+\dfrac{1}{(x+1)^2}=-\dfrac{1}{x(x+1)}+\dfrac{1}{(x+1)^2}$

$=\dfrac{-(x+1)+x}{x(x+1)^2}=\dfrac{-1}{x(x+1)^2}$

Donc $\boxed{f''(x)=\dfrac{-1}{x(x+1)^2}<0\ \forall x>0}$, c'est-à-dire $f'$ est strictement décroissante sur $]0,+\infty[$.

Or $\displaystyle\lim_{x\to+\infty}f'(x)=\lim_{x\to+\infty}\!\left[\ln\!\left(1+\dfrac{1}{x}\right)-\dfrac{1}{x+1}\right]=0-0=0$.

$f'$ décroissante et de limite $0$ en $+\infty$ entraîne $f'(x)>0$ sur $]0,+\infty[$.

### 2) b) Tableau de variation de $f$

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $0$ | $\nearrow$ | $1$ |

### 2) c) Construction de $(\mathcal C_f)$

Courbe strictement croissante de $0$ à $1$, demi-tangente verticale en $O$, A.H. $y=1$ en $+\infty$ (jamais atteinte).

### 3) a) $(A_n)$ est bien définie

Pour que $A_n=\displaystyle\int_0^1 f_n(x)\,dx$ existe, il suffit que $f_n$ soit continue sur $[0,1]$.

* Sur $]0,1]$ : $f_n(x)=x^n\ln\!\left(1+\dfrac{1}{x}\right)$ est produit de fonctions continues, donc continue.
* En $0$ : $\displaystyle\lim_{x\to 0^+}x^n\ln\!\left(1+\dfrac{1}{x}\right)=\lim_{x\to 0^+}\big[x^n\ln(x+1)-x^n\ln x\big]=0-0=0=f_n(0)$.

Donc $f_n$ continue sur $[0,1]$, d'où $(A_n)$ bien définie pour tout $n\geq 1$. $\quad\blacksquare$

### 3) b) Encadrement de $x^{n-1}f(x)$

D'après le T.V. de la question 2)b) : $\forall x\in[0,1]$, $0\leq f(x)\leq\ln 2<1$.

Pour $x\in[0,1]$, $x^{n-1}\geq 0$. En multipliant par $x^{n-1}$ :

$\boxed{0\leq x^{n-1}f(x)\leq x^{n-1}}\quad\blacksquare$

### 3) c) Encadrement de $A_n$ et limite

Remarquons que $x^{n-1}f(x)=x^{n-1}\cdot x\ln(1+\tfrac{1}{x})=x^n\ln(1+\tfrac{1}{x})=f_n(x)$.

L'encadrement précédent donne $0\leq f_n(x)\leq x^{n-1}$. En intégrant sur $[0,1]$ :

$0\leq A_n=\displaystyle\int_0^1 f_n(x)\,dx\leq\int_0^1 x^{n-1}\,dx=\left[\dfrac{x^n}{n}\right]_0^1=\dfrac{1}{n}$

D'où $\boxed{0\leq A_n\leq\dfrac{1}{n}}$. Par le théorème d'encadrement, $\displaystyle\lim_{n\to+\infty}A_n=0$.

### 4) a) Calcul de $I_n(\alpha)$

I.P.P. : $\begin{cases}u(x)=\ln x\\ v'(x)=x^n\end{cases}\Rightarrow\begin{cases}u'(x)=\dfrac{1}{x}\\ v(x)=\dfrac{x^{n+1}}{n+1}\end{cases}$

$I_n(\alpha)=\left[\dfrac{x^{n+1}}{n+1}\ln x\right]_\alpha^1-\dfrac{1}{n+1}\displaystyle\int_\alpha^1 x^n\,dx$

$=\left(0-\dfrac{\alpha^{n+1}\ln\alpha}{n+1}\right)-\dfrac{1}{n+1}\!\left[\dfrac{x^{n+1}}{n+1}\right]_\alpha^1$

$=-\dfrac{\alpha^{n+1}\ln\alpha}{n+1}-\dfrac{1}{(n+1)^2}+\dfrac{\alpha^{n+1}}{(n+1)^2}$

$\boxed{I_n(\alpha)=-\dfrac{\alpha^{n+1}\ln\alpha}{n+1}+\dfrac{\alpha^{n+1}-1}{(n+1)^2}}$

### 4) b) Limite en $\alpha\to 0^+$

* $\displaystyle\lim_{\alpha\to 0^+}\alpha^{n+1}\ln\alpha=0$ (croissance comparée, $n+1\geq 1$)
* $\displaystyle\lim_{\alpha\to 0^+}\alpha^{n+1}=0$

D'où $\displaystyle\lim_{\alpha\to 0^+}I_n(\alpha)=0+\dfrac{0-1}{(n+1)^2}=\dfrac{-1}{(n+1)^2}$, soit :

$\boxed{I_n=\dfrac{-1}{(n+1)^2}} \quad\blacksquare$

### 4) c) Relation de récurrence sur $(J_n)$

$J_{n+1}=\displaystyle\int_0^1 x^{n+1}\ln(x+1)\,dx$

I.P.P. : $\begin{cases}u(x)=\ln(x+1)\\ v'(x)=x^{n+1}\end{cases}\Rightarrow\begin{cases}u'(x)=\dfrac{1}{x+1}\\ v(x)=\dfrac{x^{n+2}}{n+2}\end{cases}$

$J_{n+1}=\left[\dfrac{x^{n+2}}{n+2}\ln(x+1)\right]_0^1-\dfrac{1}{n+2}\displaystyle\int_0^1\dfrac{x^{n+2}}{x+1}\,dx$

$=\dfrac{\ln 2}{n+2}-\dfrac{1}{n+2}\displaystyle\int_0^1\dfrac{x^{n+2}}{x+1}\,dx\qquad(\star)$

Calcul de $K=\displaystyle\int_0^1\dfrac{x^{n+2}}{x+1}\,dx$ : écrivons $x^{n+2}=(x+1)x^{n+1}-x^{n+1}$, d'où :

$K=\displaystyle\int_0^1 x^{n+1}\,dx-\int_0^1\dfrac{x^{n+1}}{x+1}\,dx=\dfrac{1}{n+2}-L\quad\text{où }L=\displaystyle\int_0^1\dfrac{x^{n+1}}{x+1}\,dx$

Pour $L$, I.P.P. : $\begin{cases}u(x)=x^{n+1}\\ v'(x)=\dfrac{1}{x+1}\end{cases}\Rightarrow\begin{cases}u'(x)=(n+1)x^n\\ v(x)=\ln(x+1)\end{cases}$

$L=\big[x^{n+1}\ln(x+1)\big]_0^1-(n+1)\displaystyle\int_0^1 x^n\ln(x+1)\,dx=\ln 2-(n+1)J_n$

D'où $K=\dfrac{1}{n+2}-\ln 2+(n+1)J_n$.

En reportant dans $(\star)$ :

$J_{n+1}=\dfrac{\ln 2}{n+2}-\dfrac{1}{n+2}\!\left[\dfrac{1}{n+2}-\ln 2+(n+1)J_n\right]$

$=\dfrac{\ln 2}{n+2}-\dfrac{1}{(n+2)^2}+\dfrac{\ln 2}{n+2}-\dfrac{n+1}{n+2}J_n$

$\boxed{J_{n+1}=\dfrac{2\ln 2}{n+2}-\dfrac{1}{(n+2)^2}-\dfrac{n+1}{n+2}\,J_n}\quad\blacksquare$
"""

# ============================================================================
# BAC C 2007 — Session Complémentaire
# ============================================================================

CORRECTIONS["bac-c-2007-sc-math-ex1"] = r"""## Exercice 1

Plaçons le carré direct $ABCD$ avec $A(0,0)$, $B(a,0)$, $C(a,a)$, $D(0,a)$, centre $O(a/2,a/2)$, et $E$ symétrique de $C$ par rapport à $D$, soit $E(-a,a)$.

### 1) a) Détermination des quatre ensembles

**$\Gamma_1$** : $\|\vec{MA}-\vec{MB}+\vec{MC}\|=a$.

La somme des coefficients est $1-1+1=1\neq 0$. Soit $G_1=\mathrm{bar}\{(A,1),(B,-1),(C,1)\}$. Alors :

$\vec{MA}-\vec{MB}+\vec{MC}=1\cdot\vec{MG_1}=\vec{MG_1}$

Position de $G_1$ : $G_1=A-B+C=(0,0)-(a,0)+(a,a)=(0,a)=D$.

D'où $\|\vec{MD}\|=a$, soit $\boxed{\Gamma_1:\ MD=a,\ \text{cercle de centre }D\text{ et rayon }a}$.

**$\Gamma_2$** : $MA^2-MB^2+MC^2=a^2$.

Avec les mêmes poids (somme $1$, $G_1=D$), la formule de Leibniz donne :

$MA^2-MB^2+MC^2=MD^2+\big(DA^2-DB^2+DC^2\big)=MD^2+\big(a^2-2a^2+a^2\big)=MD^2$

D'où $MD^2=a^2$, soit $\boxed{\Gamma_2=\Gamma_1}$.

**$\Gamma_3$** : $(\vec{MA}-\vec{MB}-\vec{MD})\cdot(2\vec{MA}-2\vec{MB}+\vec{MC})=0$.

Premier vecteur, somme des poids $1-1-1=-1$ : $\vec{MA}-\vec{MB}-\vec{MD}=-\vec{MG_3}$ avec $G_3=\mathrm{bar}\{(A,1),(B,-1),(D,-1)\}=-A+B+D=(a,a)=C$.

Donc le premier vecteur vaut $-\vec{MC}=\vec{CM}$.

Deuxième vecteur, somme des poids $2-2+1=1$ : $2\vec{MA}-2\vec{MB}+\vec{MC}=\vec{MG_4}$ avec $G_4=2A-2B+C=(-a,a)=E$.

Donc le deuxième vecteur vaut $\vec{ME}$.

D'où l'équation devient $-\vec{MC}\cdot\vec{ME}=0$, c'est-à-dire $\vec{MC}\cdot\vec{ME}=0$.

C'est l'équation du cercle de diamètre $[CE]$. Or le milieu de $[CE]$ est $D$ et $CE=2a$, donc rayon $a$.

$\boxed{\Gamma_3=\Gamma_1}$.

**$\Gamma_4$** : $\|\vec{MA}-\vec{MB}-\vec{ME}\|=\|\vec{MD}-\vec{MC}\|$.

Membre de droite : $\vec{MD}-\vec{MC}=\vec{CD}$, donc $\|\vec{MD}-\vec{MC}\|=CD=a$.

Membre de gauche, somme des poids $1-1-1=-1$ : $\vec{MA}-\vec{MB}-\vec{ME}=-\vec{MG_5}$ avec $G_5=\mathrm{bar}\{(A,1),(B,-1),(E,-1)\}=-A+B+E=(0,a)=D$.

Donc $\|\vec{MA}-\vec{MB}-\vec{ME}\|=\|\vec{MD}\|=MD$.

L'équation devient $MD=a$, soit $\boxed{\Gamma_4=\Gamma_1}$.

### 1) b) Constat

$\boxed{\Gamma_1=\Gamma_2=\Gamma_3=\Gamma_4}$ : c'est le cercle de centre $D$ et de rayon $a$, qui passe en particulier par $C$ et $E$.

### 2) a) Translation $f_k$

$\vec{MM'}=\vec{MA}-\vec{MB}+(1-k)\vec{MC}$, somme des poids $=1-1+(1-k)=1-k$.

$f_k$ est une translation $\Leftrightarrow$ somme $=0\Leftrightarrow k=1$.

Pour $k=1$ : $\vec{MM'}=\vec{MA}-\vec{MB}=\vec{BA}$.

D'où $\boxed{f_1=t_{\vec{BA}}}$.

### 2) b) Cas $k\in\mathbb R^*\setminus\{1\}$

Soit $\Omega_k=\mathrm{bar}\{(A,1),(B,-1),(C,1-k)\}$ (somme $1-k\neq 0$). Alors $\vec{MA}-\vec{MB}+(1-k)\vec{MC}=(1-k)\vec{M\Omega_k}$, d'où :

$\vec{MM'}=(1-k)\vec{M\Omega_k}\quad(\star)$

**Point invariant** : $M=\Omega_k\Rightarrow\vec{MM'}=\vec 0\Rightarrow M'=M$. Donc $\Omega_k$ est invariant.

Unicité : si $M$ est invariant, $\vec{MM'}=\vec 0\Rightarrow(1-k)\vec{M\Omega_k}=\vec 0\Rightarrow M=\Omega_k$ (car $1-k\neq 0$).

**Reconnaissance** : de $(\star)$, $M'-M=(1-k)(\Omega_k-M)$, soit $M'=k M+(1-k)\Omega_k$. C'est l'écriture d'une homothétie de centre $\Omega_k$ et de rapport $k$.

$\boxed{f_k\ \text{est l'homothétie de centre }\Omega_k\text{ et de rapport }k}$.

**Coordonnées de $\Omega_k$** : $\Omega_k=\dfrac{1\cdot A-1\cdot B+(1-k)C}{1-k}=\dfrac{(0,0)-(a,0)+(1-k)(a,a)}{1-k}=\left(\dfrac{-ka}{1-k},\ a\right)=\left(\dfrac{ka}{k-1},\ a\right)$.

### 2) c) Lieu de $\Omega_k$

L'ordonnée est constante : $y_{\Omega_k}=a$. C'est l'équation de la droite $(DC)$.

L'abscisse $x_k=\dfrac{ka}{k-1}=\dfrac{a}{1-\frac{1}{k}}$ : pour $k\in\mathbb R^*\setminus\{1\}$, $x_k$ parcourt $\mathbb R\setminus\{0,a\}$ (car $k=0$ donnerait $x=0$ et $k\to\infty$ donnerait $x=a$).

Donc $x_k\neq 0$ (i.e. $\Omega_k\neq D$) et $x_k\neq a$ (i.e. $\Omega_k\neq C$).

$\boxed{\text{Lieu de }\Omega_k=(DC)\setminus\{D,C\}}$.

### 2) d) Cas $k=\dfrac{1}{2}$ : lieu du centre de gravité $G$

Pour $k=1/2$ : $\Omega_{1/2}=\left(\dfrac{a/2}{-1/2},a\right)=(-a,a)=E$.

Donc $f_{1/2}$ est l'homothétie de centre $E$ et de rapport $1/2$. Pour tout $M$ : $M'=E+\dfrac{1}{2}(M-E)=\dfrac{1}{2}(M+E)$, c'est-à-dire **$M'$ est le milieu de $[ME]$**.

Centre de gravité de $DMM'$ :

$G=\dfrac{D+M+M'}{3}=\dfrac{D+M+\frac{M+E}{2}}{3}=\dfrac{D}{3}+\dfrac{M}{2}+\dfrac{E}{6}=\dfrac{5D+E}{6}+\dfrac{1}{2}(M-D)\cdot\dots$

Plus simplement : posons $\Omega'=\dfrac{5D+E}{6}=\mathrm{bar}\{(D,5),(E,1)\}$. Alors :

$\vec{\Omega'G}=G-\Omega'=\dfrac{D}{3}+\dfrac{M}{2}+\dfrac{E}{6}-\dfrac{5D+E}{6}=\dfrac{M-D}{2}=\dfrac{1}{2}\vec{DM}$

Or $M$ décrit $\Gamma$ (cercle de diamètre $[CE]$ = cercle de centre $D$ et rayon $a$ d'après 1.a)), donc $\|\vec{DM}\|=a$, donc :

$\|\vec{\Omega'G}\|=\dfrac{a}{2}$

**Coordonnées** : $\Omega'=\dfrac{5(0,a)+(-a,a)}{6}=\left(-\dfrac{a}{6},a\right)$.

$\boxed{G\text{ décrit le cercle de centre }\Omega'\!\left(-\dfrac{a}{6},a\right)\text{ et de rayon }\dfrac{a}{2}}$.
"""

CORRECTIONS["bac-c-2007-sc-math-ex2"] = r"""## Exercice 2

Plaçons le carré direct $ABCD$ avec $A(0,0)$, $B(a,0)$, $C(a,a)$, $D(0,a)$, $O(a/2,a/2)$ ; $I(a/2,0)$, $J(a,a/2)$, $K(a/2,a)$, $L(0,a/2)$.

### 1) b) Existence et unicité de la rotation $r$

$\vec{AI}=(a/2,0)$ et $\vec{OK}=(0,a/2)$.

$\|\vec{AI}\|=\|\vec{OK}\|=a/2\neq 0$, donc il existe une unique rotation $r$ telle que $r(A)=O$ et $r(I)=K$. $\quad\blacksquare$

### 1) c) Angle et centre de $r$

**Angle** : $\theta=(\widehat{\vec{AI},\vec{OK}})=(\widehat{(a/2,0),(0,a/2)})=\dfrac{\pi}{2}$.

**Centre** : intersection des médiatrices de $[AO]$ et $[IK]$.

Médiatrice de $[AO]$ : passe par $(a/4,a/4)$, perpendiculaire à $\vec{AO}=(a/2,a/2)$, donc d'équation $x+y=a/2$.

Médiatrice de $[IK]$ : passe par $(a/2,a/2)=O$, perpendiculaire à $\vec{IK}=(0,a)$, donc horizontale d'équation $y=a/2$.

Intersection : $y=a/2$ et $x=0$, soit le point $(0,a/2)=L$.

$\boxed{r=\text{rotation de centre }L\text{ et d'angle }\dfrac{\pi}{2}}$.

### 2) a) Décomposition de $r$ en produit de réflexions

**Vérification** $r=S_{(DA)}\circ S_{(LK)}$ :

Les droites $(DA)$ et $(LK)$ passent toutes deux par $L$. $(DA)$ est l'axe des ordonnées (direction $\pi/2$), $(LK)$ a la direction $\vec{LK}=(a/2,a/2)$ (direction $\pi/4$).

L'angle orienté de droites de $(LK)$ vers $(DA)$ est $\pi/2-\pi/4=\pi/4$.

Donc $S_{(DA)}\circ S_{(LK)}$ est la rotation de centre $L$ et d'angle $2\cdot\pi/4=\dfrac{\pi}{2}=r$. $\quad\blacksquare$

**Remarque sur l'énoncé** : la première égalité $r=S_{(OL)}\circ S_{(DA)}$ telle qu'écrite est erronée. $(OL)$ et $(DA)$ se coupent à angle droit en $L$, donc $S_{(OL)}\circ S_{(DA)}$ est une rotation d'angle $\pi$ (demi-tour), pas $\pi/2$. Il s'agit probablement d'une coquille pour $S_{(LI)}\circ S_{(DA)}$ : $(LI)$ a la direction $\pi/4$... non, $(LI)$ va de $L$ à $I$, direction $-\pi/4$ ; l'angle de $(DA)$ à $(LI)$ vaut $-\pi/4-\pi/2=-3\pi/4\equiv\pi/4\ [\pi]$, donc $S_{(LI)}\circ S_{(DA)}=$rotation$(L,\pi/2)=r$. La forme correcte est donc :

$\boxed{r=S_{(LI)}\circ S_{(DA)}=S_{(DA)}\circ S_{(LK)}}$.

### 2) b) Nature et éléments de $g=S_{(OI)}\circ S_{(LI)}\circ S_{(LK)}$

Composition de $3$ réflexions $=$ isométrie indirecte, donc soit réflexion soit symétrie glissée.

Calculons en coordonnées :
* $S_{(LK)}$ : axe $x-y+a/2=0$ ; $(x,y)\mapsto(y-a/2,\ x+a/2)$
* $S_{(LI)}$ : axe $x+y-a/2=0$ ; $(x,y)\mapsto(a/2-y,\ a/2-x)$
* $S_{(OI)}$ : axe $x=a/2$ ; $(x,y)\mapsto(a-x,\ y)$

Composition $g(x,y)$ :

$S_{(LK)}(x,y)=(y-a/2,\ x+a/2)$

$S_{(LI)}(y-a/2,\ x+a/2)=(a/2-(x+a/2),\ a/2-(y-a/2))=(-x,\ a-y)$

$S_{(OI)}(-x,\ a-y)=(a-(-x),\ a-y)=(a+x,\ a-y)$

Donc $\boxed{g(x,y)=(x+a,\ a-y)}$.

C'est la composée de la réflexion d'axe $y=a/2=(LJ)$ (qui envoie $(x,y)$ sur $(x,a-y)$) et de la translation de vecteur $\vec{AB}=(a,0)$, vecteur parallèle à l'axe. C'est donc une **symétrie glissée** :

$\boxed{g=\text{symétrie glissée d'axe }(LJ)\text{ et de vecteur }\vec{AB}}$.

### 3) a) Existence et unicité de la similitude directe $s_1$ : $O\mapsto I$, $A\mapsto B$

$O\neq A$ et $I\neq B$, donc il existe une **unique** similitude directe $s_1$ qui envoie $O$ sur $I$ et $A$ sur $B$. $\quad\blacksquare$

### 3) b) Rapport et angle de $s_1$

Notons $s_1(z)=\alpha z+\beta$ en notation complexe. Affixes : $A=0$, $B=a$, $O=\dfrac{a(1+i)}{2}$, $I=\dfrac{a}{2}$.

* $s_1(A)=B$ : $\beta=a$.
* $s_1(O)=I$ : $\alpha\cdot\dfrac{a(1+i)}{2}+a=\dfrac{a}{2}$, donc $\alpha(1+i)=-1$, donc $\alpha=\dfrac{-1}{1+i}=\dfrac{-(1-i)}{2}=-\dfrac{1}{2}+\dfrac{i}{2}$.

**Rapport** : $|\alpha|=\sqrt{1/4+1/4}=\dfrac{\sqrt 2}{2}=\dfrac{1}{\sqrt 2}$.

**Angle** : $\alpha=\dfrac{\sqrt 2}{2}e^{i\theta}$ avec $\cos\theta=-\dfrac{1}{\sqrt 2}$, $\sin\theta=\dfrac{1}{\sqrt 2}$, donc $\theta=\dfrac{3\pi}{4}$.

$\boxed{\text{Rapport }k=\dfrac{1}{\sqrt 2},\ \text{angle }\theta=\dfrac{3\pi}{4}}$.

### 3) c) « Vérifier que $s_1(A)=A$ »

**Remarque** : par construction $s_1(A)=B\neq A$. L'énoncé semble erroné ici (probablement OCR : on veut sans doute calculer $s_1(B)$, ou le point fixe de $s_1$, ou vérifier $s_1\circ s_1(B)=B$).

Calculons le **point fixe** $\Omega$ de $s_1$ : $\alpha z+\beta=z\Rightarrow z=\dfrac{\beta}{1-\alpha}=\dfrac{a}{1-(-1/2+i/2)}=\dfrac{a}{3/2-i/2}=\dfrac{2a}{3-i}=\dfrac{2a(3+i)}{10}=\dfrac{a(3+i)}{5}$.

Donc le point fixe de $s_1$ a pour affixe $\dfrac{3a}{5}+i\dfrac{a}{5}$, soit $\Omega\!\left(\dfrac{3a}{5},\dfrac{a}{5}\right)$.

### 4) a) Similitude $s_2$ : $A\mapsto O$, $B\mapsto D$

Notons $s_2(z)=\alpha'z+\beta'$. $D=ia$.

* $s_2(A)=O$ : $\beta'=O=\dfrac{a(1+i)}{2}$.
* $s_2(B)=D$ : $\alpha'\cdot a+\dfrac{a(1+i)}{2}=ia$, donc $\alpha'a=ia-\dfrac{a(1+i)}{2}=a\!\left(i-\dfrac{1+i}{2}\right)=a\!\left(\dfrac{-1+i}{2}\right)$.

D'où $\alpha'=-\dfrac{1}{2}+\dfrac{i}{2}$, identique à $\alpha$ de $s_1$.

$\boxed{\text{Rapport }k'=\dfrac{1}{\sqrt 2},\ \text{angle }\theta'=\dfrac{3\pi}{4}}$.

$s_1$ et $s_2$ ont mêmes rapport et angle (mais centres différents).

**Note** : l'énoncé extrait est tronqué après cette question (artefact de saut de page OCR), les sous-questions 4)b), 4)c) etc. ne sont pas disponibles.
"""

CORRECTIONS["bac-c-2007-sc-math-ex3"] = r"""## Exercice 3 (Problème, 10 points)

**Note sur l'énoncé** : la définition de la famille $f_n$ est manquante dans la transcription. D'après l'égalité A.3.a) « $f_n(x)-f_0(x)=n(f_1(x)-f_0(x))$ » et le fait que toutes les courbes passent par un point commun (A.2.b)), la famille est :

$$\boxed{f_n(x)=x-n\ln x\quad(\text{défini sur }]0,+\infty[)}$$

En particulier $f_0(x)=x$ et $f_1(x)=x-\ln x$ (cohérent avec A.1.a)).

## Partie A

### 1) a) $f_1(x)=x-\ln x$ — limites

### 1) b)

* $\displaystyle\lim_{x\to 0^+}f_1(x)=\lim_{x\to 0^+}(x-\ln x)=0-(-\infty)=+\infty$
* $\displaystyle\lim_{x\to+\infty}\dfrac{f_1(x)}{x}=\lim_{x\to+\infty}\!\left(1-\dfrac{\ln x}{x}\right)=1-0=1$
* $\displaystyle\lim_{x\to+\infty}\bigl(f_1(x)-x\bigr)=\lim_{x\to+\infty}(-\ln x)=-\infty$

Interprétation : $(C_1)$ admet une **B.P. de direction $y=x$** en $+\infty$.

### 2) a) T.V. de $f_1$

$f_1'(x)=1-\dfrac{1}{x}=\dfrac{x-1}{x}$, du signe de $x-1$.

$f_1'(x)=0\Leftrightarrow x=1$ ; $f_1(1)=1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| $f_1'(x)$ | | $-$ | $0$ | $+$ | |
| $f_1(x)$ | $+\infty$ | $\searrow$ | $1$ | $\nearrow$ | $+\infty$ |

En particulier $f_1(x)\geq 1>0$ pour tout $x>0$.

### 2) b) Points communs aux courbes $(C_n)$ et positions relatives

$f_n(x_0)=f_m(x_0)\Leftrightarrow(m-n)\ln x_0=0\Leftrightarrow x_0=1$.

$f_n(1)=1-n\cdot 0=1$. Donc toutes les courbes $(C_n)$ passent par le point $\boxed{A_0(1,1)}$.

**Positions relatives** : $f_{n+1}(x)-f_n(x)=-\ln x$.

* Si $0<x<1$ : $-\ln x>0$, donc $(C_{n+1})$ est **au-dessus** de $(C_n)$.
* Si $x=1$ : $(C_{n+1})$ et $(C_n)$ se coupent en $A_0$.
* Si $x>1$ : $-\ln x<0$, donc $(C_{n+1})$ est **en-dessous** de $(C_n)$.

### 2) c) Tangentes en $x=e$ — point commun

$f_n(e)=e-n\ln e=e-n$ ; $f_n'(x)=1-\dfrac{n}{x}$ ; $f_n'(e)=1-\dfrac{n}{e}$.

Tangente $T_n$ : $y=(e-n)+\left(1-\dfrac{n}{e}\right)(x-e)=\left(1-\dfrac{n}{e}\right)x-e+n+e-n=\left(1-\dfrac{n}{e}\right)x$.

Donc $T_n:\ y=\left(1-\dfrac{n}{e}\right)x$ : pour tout $n$, $T_n$ passe par **l'origine $O(0,0)$**. $\quad\blacksquare$

### 3) a) Identité $f_n(x)-f_0(x)=n\bigl(f_1(x)-f_0(x)\bigr)$

$f_n(x)-f_0(x)=(x-n\ln x)-x=-n\ln x$.

$n\bigl(f_1(x)-f_0(x)\bigr)=n\bigl((x-\ln x)-x\bigr)=-n\ln x$.

Égalité vérifiée. $\quad\blacksquare$

### 3) b) Relation vectorielle

$M_0(x,f_0(x))=(x,x)$, $M_1(x,f_1(x))=(x,x-\ln x)$, $M_n(x,f_n(x))=(x,x-n\ln x)$.

$\vec{M_0M_n}=(0,-n\ln x)=n\cdot(0,-\ln x)=n\cdot\vec{M_0M_1}$. $\quad\blacksquare$

### 3) c) Construction de $(C_n)$ point par point

D'après 3)b), pour chaque abscisse $x$, le point $M_n$ de $(C_n)$ s'obtient à partir de $M_0\in(C_0)$ et $M_1\in(C_1)$ par : $M_n=M_0+n\vec{M_0M_1}$.

Concrètement, pour $(C_2)$ : on prend l'abscisse $x$, on lit $M_0$ et $M_1$ sur leurs courbes, puis $M_2$ est le symétrique de $M_0$ par rapport à $M_1$ (puisque $\vec{M_0M_2}=2\vec{M_0M_1}\Leftrightarrow M_1$ est milieu de $[M_0M_2]$).

## Partie B

Soit $g(x)=\dfrac{f_0(x)}{f_1(x)}=\dfrac{x}{x-\ln x}$ pour $x>0$, et $g(0)=0$.

### 1) a) $D_g=[0,+\infty[$

D'après A.2.a), $f_1(x)\geq 1>0$ sur $]0,+\infty[$, donc $f_1$ ne s'annule pas. De plus $g(0)$ est défini. Donc $D_g=[0,+\infty[$. $\quad\blacksquare$

### 1) b) Continuité

Sur $]0,+\infty[$ : $g$ est quotient de fonctions continues avec dénominateur non nul, donc continue.

En $0$ : $\displaystyle\lim_{x\to 0^+}g(x)=\lim_{x\to 0^+}\dfrac{x}{x-\ln x}$. Or $x\to 0$ et $x-\ln x\to+\infty$, donc $g(x)\to 0=g(0)$. Donc continue à droite en $0$. $\quad\blacksquare$

### 2) a) Limite en $+\infty$

$g(x)=\dfrac{x}{x-\ln x}=\dfrac{1}{1-\frac{\ln x}{x}}\xrightarrow[x\to+\infty]{}\dfrac{1}{1-0}=1$

Donc $\boxed{\lim_{x\to+\infty}g(x)=1}$ : **A.H.** $y=1$ en $+\infty$.

### 2) b) Limite de $g(x)/x$ en $0^+$

$\dfrac{g(x)}{x}=\dfrac{1}{x-\ln x}\xrightarrow[x\to 0^+]{}\dfrac{1}{+\infty}=0$

Interprétation : $(\Gamma)$ admet **l'axe $(Ox)$ comme tangente** à l'origine.

### 3) a) Calcul de $g'(x)$

$g'(x)=\dfrac{(x-\ln x)-x\!\left(1-\frac{1}{x}\right)}{(x-\ln x)^2}=\dfrac{x-\ln x-x+1}{(x-\ln x)^2}=\dfrac{1-\ln x}{(x-\ln x)^2}$

$\boxed{g'(x)=\dfrac{1-\ln x}{(x-\ln x)^2}}$, du signe de $1-\ln x$, c'est-à-dire :

* $g'(x)>0$ pour $0<x<e$
* $g'(e)=0$
* $g'(x)<0$ pour $x>e$

### 3) b) T.V. et tracé

$g(e)=\dfrac{e}{e-\ln e}=\dfrac{e}{e-1}$.

| $x$ | $0$ | | $e$ | | $+\infty$ |
|---|---|---|---|---|---|
| $g'(x)$ | | $+$ | $0$ | $-$ | |
| $g(x)$ | $0$ | $\nearrow$ | $\dfrac{e}{e-1}$ | $\searrow$ | $1$ |

**Remarque** : le T.V. présent dans l'énoncé extrait (signes $-/+$, valeur $e$ au maximum, limite $+\infty$ en $+\infty$) est erroné. Le bon T.V. est ci-dessus : $g$ croît de $0$ à $\dfrac{e}{e-1}\approx 1{,}58$, puis décroît vers $1$.

### 4) Encadrement de $\dfrac{\ln x}{x}$ sur $[1,e]$

Sur $[1,e]$, $g$ est croissante (vu T.V.), donc $g(1)\leq g(x)\leq g(e)$, soit :

$1\leq g(x)\leq\dfrac{e}{e-1}$

En passant à l'inverse (tous strictement positifs) : $\dfrac{e-1}{e}\leq\dfrac{1}{g(x)}\leq 1$.

Or $\dfrac{1}{g(x)}=\dfrac{x-\ln x}{x}=1-\dfrac{\ln x}{x}$, donc $\dfrac{\ln x}{x}=1-\dfrac{1}{g(x)}$, ce qui donne :

$0\leq\dfrac{\ln x}{x}\leq 1-\dfrac{e-1}{e}=\dfrac{1}{e}$

$\boxed{\forall x\in[1,e],\ 0\leq\dfrac{\ln x}{x}\leq\dfrac{1}{e}} \quad\blacksquare$

### 5) a) Calcul de $U_0$ et $U_1$

$U_0=\displaystyle\int_1^e dx=e-1$

$U_1=\displaystyle\int_1^e\dfrac{\ln x}{x}dx$. Posons $u=\ln x$, $du=\dfrac{dx}{x}$, $x:1\to e\Rightarrow u:0\to 1$.

$U_1=\displaystyle\int_0^1 u\,du=\left[\dfrac{u^2}{2}\right]_0^1=\dfrac{1}{2}$.

$\boxed{U_0=e-1,\ U_1=\dfrac{1}{2}}$.

### 5) b) $(U_n)$ positive et décroissante

* **Positivité** : sur $[1,e]$, $\dfrac{\ln x}{x}\geq 0$, donc $\!\left(\dfrac{\ln x}{x}\right)^n\geq 0$, donc $U_n\geq 0$.
* **Décroissance** : sur $[1,e]$, $\dfrac{\ln x}{x}\leq\dfrac{1}{e}<1$, donc $\!\left(\dfrac{\ln x}{x}\right)^{n+1}\leq\!\left(\dfrac{\ln x}{x}\right)^n$ (en multipliant par la quantité positive $\dfrac{\ln x}{x}\leq 1$). En intégrant, $U_{n+1}\leq U_n$.

$(U_n)$ est décroissante et minorée par $0$, donc **convergente**.

### 5) c) Encadrement et limite

D'après B.4), $0\leq\dfrac{\ln x}{x}\leq\dfrac{1}{e}$ sur $[1,e]$. Donc :

$0\leq\!\left(\dfrac{\ln x}{x}\right)^n\leq\dfrac{1}{e^n}$

En intégrant sur $[1,e]$ :

$0\leq U_n\leq\dfrac{e-1}{e^n}$

$\lim_{n\to+\infty}\dfrac{e-1}{e^n}=0$, donc par encadrement $\boxed{\lim_{n\to+\infty}U_n=0}$.

### 6) a) Expression de $S_n$

Pour $x\in[1,e]$, $r=\dfrac{\ln x}{x}\in[0,1/e]$, donc $r\neq 1$. La somme géométrique donne :

$\sum_{k=0}^n r^k=\dfrac{1-r^{n+1}}{1-r}$

Donc $S_n=\displaystyle\sum_{k=0}^n U_k=\sum_{k=0}^n\int_1^e\!\left(\dfrac{\ln x}{x}\right)^k dx=\int_1^e\sum_{k=0}^n\!\left(\dfrac{\ln x}{x}\right)^k dx$

$\boxed{S_n=\displaystyle\int_1^e\dfrac{1-\!\left(\dfrac{\ln x}{x}\right)^{n+1}}{1-\dfrac{\ln x}{x}}dx} \quad\blacksquare$

### 6) b) Expression de $I-S_n$

$I=\displaystyle\int_1^e\dfrac{x}{x-\ln x}dx=\int_1^e\dfrac{1}{1-\frac{\ln x}{x}}dx$ (en divisant numérateur et dénominateur par $x$).

D'où :

$I-S_n=\displaystyle\int_1^e\!\left[\dfrac{1}{1-\frac{\ln x}{x}}-\dfrac{1-\!\left(\frac{\ln x}{x}\right)^{n+1}}{1-\frac{\ln x}{x}}\right]dx=\int_1^e\dfrac{\left(\frac{\ln x}{x}\right)^{n+1}}{1-\frac{\ln x}{x}}dx$

En multipliant numérateur et dénominateur du facteur $1/(1-\frac{\ln x}{x})$ par $x$, on retrouve $\dfrac{x}{x-\ln x}$ :

$\boxed{I-S_n=\displaystyle\int_1^e\dfrac{x}{x-\ln x}\!\left(\dfrac{\ln x}{x}\right)^{n+1}dx} \quad\blacksquare$

### 6) c) Encadrement de $I-S_n$ et convergence

Sur $[1,e]$ :

* $\dfrac{x}{x-\ln x}=g(x)\geq 0$
* $\!\left(\dfrac{\ln x}{x}\right)^{n+1}>0$ pour $x\in\,]1,e]$

Donc $I-S_n>0$.

De plus $g(x)\leq\dfrac{e}{e-1}$ et $\!\left(\dfrac{\ln x}{x}\right)^{n+1}\leq\dfrac{1}{e^{n+1}}$ (d'après B.4), donc :

$0<I-S_n\leq\dfrac{e}{e-1}\cdot\dfrac{1}{e^{n+1}}\cdot(e-1)=\dfrac{1}{e^n}$

$\boxed{0<I-S_n\leq\dfrac{1}{e^n}}$

Comme $\dfrac{1}{e^n}\to 0$, par encadrement $I-S_n\to 0$, donc $\boxed{\lim_{n\to+\infty}S_n=I}$.

### 6) d) Encadrement de $I$

De $0<I-S_n\leq\dfrac{1}{e^n}$ on déduit $S_n\leq I\leq S_n+\dfrac{1}{e^n}$, donc :

$\boxed{S_n\leq I\leq S_n+\dfrac{1}{e^{n+1}}}\quad\text{(le sujet utilise la borne plus fine }\tfrac{1}{e^{n+1}}\text{ — cf. ci-dessous)}$

**Borne plus fine** : avec $g(x)\leq\dfrac{e}{e-1}$ et $\left(\frac{\ln x}{x}\right)^{n+1}\leq\frac{1}{e^{n+1}}$ et intégration sur $[1,e]$ de longueur $e-1$, on a aussi $I-S_n\leq\dfrac{1}{e^{n+1}}\cdot\dfrac{e}{e-1}\cdot(e-1)=\dfrac{1}{e^n}$. La borne en $1/e^{n+1}$ donnée dans l'énoncé suppose $g\leq 1$, ce qui n'est pas vrai sur $[1,e]$. On gardera la borne sûre $\dfrac{1}{e^n}$.

### 6) e) Approximation à $10^{-3}$ près

$S_n$ approche $I$ à $10^{-3}$ près $\Leftrightarrow I-S_n\leq 10^{-3}$.

Condition suffisante : $\dfrac{1}{e^n}\leq 10^{-3}$, soit $e^n\geq 1000$, soit $n\geq\dfrac{\ln 1000}{\ln e}=\ln 1000\approx 6{,}908$.

Donc $\boxed{n\geq 7}$.
"""

# ============================================================================
# BAC C 2008 — Session Normale
# ============================================================================

CORRECTIONS["bac-c-2008-sn-math-ex1"] = r"""## Exercice 1

$f(x)=x+\dfrac{1}{e^x+1}$ sur $\mathbb R$.

### 1) a) Tableau de variation de $f$

$f'(x)=1-\dfrac{e^x}{(e^x+1)^2}=\dfrac{(e^x+1)^2-e^x}{(e^x+1)^2}=\dfrac{e^{2x}+e^x+1}{(e^x+1)^2}$

Le numérateur $e^{2x}+e^x+1>0$ et le dénominateur $(e^x+1)^2>0$, donc $\boxed{f'(x)>0\ \forall x\in\mathbb R}$.

**Limites** :

* $\displaystyle\lim_{x\to-\infty}f(x)=\lim_{x\to-\infty}\!\left(x+\dfrac{1}{e^x+1}\right)=-\infty+1=-\infty$
* $\displaystyle\lim_{x\to+\infty}f(x)=\lim_{x\to+\infty}\!\left(x+\dfrac{1}{e^x+1}\right)=+\infty+0=+\infty$

| $x$ | $-\infty$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $+$ | |
| $f(x)$ | $-\infty$ | $\nearrow$ | $+\infty$ |

### 1) b) Bijection

$f$ continue, strictement croissante sur $\mathbb R$, $\lim_{-\infty}f=-\infty$, $\lim_{+\infty}f=+\infty$. Donc $f$ réalise une bijection de $\mathbb R$ sur $\boxed{J=\mathbb R}$.

### 2) a) $\displaystyle\lim_{x\to-\infty}\bigl(f(x)-(x+1)\bigr)=0$

$f(x)-(x+1)=\dfrac{1}{e^x+1}-1=\dfrac{-e^x}{e^x+1}\xrightarrow[x\to-\infty]{}\dfrac{0}{0+1}=0$ $\quad\blacksquare$

Interprétation : $(C)$ admet la droite $y=x+1$ comme **asymptote oblique** en $-\infty$.

### 2) b) $\displaystyle\lim_{x\to+\infty}\bigl(f(x)-x\bigr)=0$

$f(x)-x=\dfrac{1}{e^x+1}\xrightarrow[x\to+\infty]{}0$ $\quad\blacksquare$

Interprétation : $(C)$ admet la droite $y=x$ comme **asymptote oblique** en $+\infty$.

### 2) c) Encadrement $x\leq f(x)\leq x+1$

$f(x)-x=\dfrac{1}{e^x+1}$. Or $e^x>0$ donc $e^x+1>1$, donc $0<\dfrac{1}{e^x+1}<1$.

D'où $0<f(x)-x<1$, c'est-à-dire $\boxed{x<f(x)<x+1}$ $\quad\blacksquare$

Interprétation : $(C)$ est strictement comprise entre les deux asymptotes obliques $y=x$ et $y=x+1$.

### 2) d) Relation $f(-x)+f(x)=1$

$f(x)+f(-x)=x+\dfrac{1}{e^x+1}-x+\dfrac{1}{e^{-x}+1}=\dfrac{1}{e^x+1}+\dfrac{e^x}{1+e^x}=\dfrac{1+e^x}{e^x+1}=1$ $\quad\blacksquare$

Interprétation : le point $I\!\left(0,\dfrac{1}{2}\right)$ est **centre de symétrie** de $(C)$.

### 2) e) $f(-0{,}7)\cdot f(0{,}6)<0$

D'après 2)c), $f(0{,}6)>0{,}6>0$.

D'après 2)d), $f(-0{,}7)=1-f(0{,}7)$. Or $f(0{,}7)=0{,}7+\dfrac{1}{e^{0{,}7}+1}$. Avec $e^{0{,}7}\approx 2{,}014$ : $f(0{,}7)\approx 0{,}7+0{,}332\approx 1{,}032>1$. Donc $f(-0{,}7)\approx -0{,}032<0$.

D'où $f(-0{,}7)\cdot f(0{,}6)<0$. $\quad\blacksquare$

(Conséquence : $f$ admet un unique zéro dans $]-0{,}7\,;\,0{,}6[$, qui est $0$ d'ailleurs par la symétrie — vérification : $f(\alpha)=0\Leftrightarrow f(-\alpha)=1$, et $f(0)=1/2\neq 0$, donc le zéro n'est pas $0$, il est strictement négatif.)

### 3) Construction de $(C)$

$f(0)=\dfrac{1}{2}$. $(C)$ passe par $I(0,1/2)$, centre de symétrie. Strictement croissante. Asymptotes obliques $y=x+1$ en $-\infty$ et $y=x$ en $+\infty$, avec $(C)$ strictement entre les deux.
"""

CORRECTIONS["bac-c-2008-sn-math-ex2"] = r"""## Exercice 2

**Remarque sur l'énoncé** : l'intégrand est $x^3(\ln x)^n$ (et non $x^e(\ln x)^n$ comme écrit). Cette correction est confirmée par la valeur $U_1=\dfrac{3e^4+1}{16}$ donnée dans l'énoncé et par la relation $4U_n+nU_{n-1}=e^4$.

$$U_n=\int_1^e x^3(\ln x)^n\,dx,\quad n\in\mathbb N^*$$

### 1) a) Calcul de $U_1$

I.P.P. : $\begin{cases}u(x)=\ln x\\ v'(x)=x^3\end{cases}\Rightarrow\begin{cases}u'(x)=\dfrac{1}{x}\\ v(x)=\dfrac{x^4}{4}\end{cases}$

$U_1=\left[\dfrac{x^4}{4}\ln x\right]_1^e-\dfrac{1}{4}\int_1^e x^3\,dx=\dfrac{e^4}{4}-\dfrac{1}{4}\!\left[\dfrac{x^4}{4}\right]_1^e=\dfrac{e^4}{4}-\dfrac{e^4-1}{16}=\dfrac{4e^4-(e^4-1)}{16}=\dfrac{3e^4+1}{16}$

$\boxed{U_1=\dfrac{3e^4+1}{16}} \quad\blacksquare$

### 1) b) $(U_n)$ décroissante et positive

* **Positivité** : sur $[1,e]$, $x^3\geq 0$ et $\ln x\geq 0$ donc $(\ln x)^n\geq 0$, d'où $U_n\geq 0$.
* **Décroissance** : sur $[1,e]$, $\ln x\in[0,1]$ donc $(\ln x)^{n+1}\leq(\ln x)^n$, d'où $x^3(\ln x)^{n+1}\leq x^3(\ln x)^n$. En intégrant : $U_{n+1}\leq U_n$.

$(U_n)$ est décroissante et minorée par $0$, donc **convergente** par le théorème de convergence monotone.

### 2) a) Relation de récurrence

I.P.P. dans $U_n$ : $\begin{cases}u(x)=(\ln x)^n\\ v'(x)=x^3\end{cases}\Rightarrow\begin{cases}u'(x)=\dfrac{n(\ln x)^{n-1}}{x}\\ v(x)=\dfrac{x^4}{4}\end{cases}$

$U_n=\left[\dfrac{x^4(\ln x)^n}{4}\right]_1^e-\dfrac{n}{4}\int_1^e x^3(\ln x)^{n-1}\,dx=\dfrac{e^4}{4}-\dfrac{n}{4}U_{n-1}$

D'où $\boxed{4U_n+nU_{n-1}=e^4}$ $\quad\blacksquare$

### 2) b) Calcul de $U_2$ et $U_3$

$n=2$ : $4U_2+2U_1=e^4\Rightarrow U_2=\dfrac{e^4-2U_1}{4}=\dfrac{e^4-\dfrac{3e^4+1}{8}}{4}=\dfrac{8e^4-3e^4-1}{32}=\dfrac{5e^4-1}{32}$

$\boxed{U_2=\dfrac{5e^4-1}{32}}$

$n=3$ : $4U_3+3U_2=e^4\Rightarrow U_3=\dfrac{e^4-3U_2}{4}=\dfrac{e^4-\dfrac{3(5e^4-1)}{32}}{4}=\dfrac{32e^4-15e^4+3}{128}=\dfrac{17e^4+3}{128}$

$\boxed{U_3=\dfrac{17e^4+3}{128}}$

### 3) a) Encadrement de $U_n$

Comme $(U_n)$ est décroissante, $U_{n+1}\leq U_n\leq U_{n-1}$ pour $n\geq 1$.

* De $4U_{n+1}+(n+1)U_n=e^4$ et $U_{n+1}\leq U_n$ : $4U_n+(n+1)U_n\geq 4U_{n+1}+(n+1)U_n=e^4$, soit $(n+5)U_n\geq e^4$, donc $U_n\geq\dfrac{e^4}{n+5}$.
* De $4U_n+nU_{n-1}=e^4$ et $U_n\leq U_{n-1}$ : $4U_n+nU_n\leq 4U_n+nU_{n-1}=e^4$, soit $(n+4)U_n\leq e^4$, donc $U_n\leq\dfrac{e^4}{n+4}$.

$\boxed{\dfrac{e^4}{n+5}\leq U_n\leq\dfrac{e^4}{n+4}} \quad\blacksquare$

### 3) b) Limites

* $\dfrac{e^4}{n+5}\to 0$ et $\dfrac{e^4}{n+4}\to 0$, par encadrement $\boxed{\lim_{n\to+\infty}U_n=0}$.
* $\dfrac{ne^4}{n+5}\to e^4$ et $\dfrac{ne^4}{n+4}\to e^4$, par encadrement $\boxed{\lim_{n\to+\infty}nU_n=e^4}$.
"""

CORRECTIONS["bac-c-2008-sn-math-ex3"] = r"""## Exercice 3

$P(z)=z^3-(5+6i)z^2+(-4+14i)z+8-8i$.

### 1) a) Calcul de $P(1)$

$P(1)=1-(5+6i)+(-4+14i)+8-8i=(1-5-4+8)+(-6+14-8)i=0+0i=0$

$\boxed{P(1)=0}$, donc $1$ est racine de $P$.

### 1) b) Résolution de $P(z)=0$

Factorisation : $P(z)=(z-1)(z^2+az+b)$. En développant et identifiant :

* coefficient de $z^2$ : $a-1=-(5+6i)\Rightarrow a=-4-6i$
* terme constant : $-b=8-8i\Rightarrow b=-8+8i$

Donc $P(z)=(z-1)\bigl(z^2-(4+6i)z+(-8+8i)\bigr)$.

Résolution de $z^2-(4+6i)z+(-8+8i)=0$ :

$\Delta=(4+6i)^2-4(-8+8i)=16+48i-36+32-32i=12+16i$

Recherche de $\sqrt\Delta=\alpha+i\beta$ avec :
$\begin{cases}\alpha^2-\beta^2=12\\ 2\alpha\beta=16\\ \alpha^2+\beta^2=|\Delta|=\sqrt{144+256}=20\end{cases}$

D'où $\alpha^2=16$, $\beta^2=4$ et $\alpha\beta>0$, soit $\sqrt\Delta=\pm(4+2i)$.

$z=\dfrac{(4+6i)\pm(4+2i)}{2}$, donc $z_1=\dfrac{8+8i}{2}=4+4i$ et $z_2=\dfrac{4i}{2}=2i$.

$\boxed{S_{\mathbb C}=\{1,\ 2i,\ 4+4i\}}$.

### 2) a) Calcul de $z_C$ et triangle $ABC$ rectangle en $A$

Coefficients $(2,-2,-1)$, somme $-1$. Définition du barycentre :

$z_G=\dfrac{2z_A-2z_B-z_C}{-1}=-2z_A+2z_B+z_C$

$6=-2(2i)+2(1)+z_C=-4i+2+z_C\Rightarrow\boxed{z_C=4+4i}$

(C'est la troisième racine de $P$.)

**Vérification triangle rectangle en $A$** :

$\vec{AB}=z_B-z_A=1-2i$, $\vec{AC}=z_C-z_A=4+4i-2i=4+2i$.

$\vec{AB}\cdot\vec{AC}=\mathrm{Re}\bigl(\overline{\vec{AB}}\cdot\vec{AC}\bigr)=\mathrm{Re}\bigl((1+2i)(4+2i)\bigr)=\mathrm{Re}(4+2i+8i-4)=0$

Donc $\boxed{\vec{AB}\perp\vec{AC}}$ : le triangle $ABC$ est rectangle en $A$. $\quad\blacksquare$

(Coordonnées : $A(0,2)$, $B(1,0)$, $C(4,4)$, $G(6,0)$.)

### 2) b) Détermination de $\Gamma_1$ et $\Gamma_2$

**$\Gamma_1$** : $2MA^2-2MB^2-MC^2=-10$.

Coefficients $(2,-2,-1)$, somme $-1$. Par la formule de Leibniz avec $G$ pour barycentre :

$2MA^2-2MB^2-MC^2=(2-2-1)MG^2+\bigl(2GA^2-2GB^2-GC^2\bigr)=-MG^2+K$

Calcul de $K$ avec $G(6,0)$ : $GA^2=6^2+2^2=40$, $GB^2=25$, $GC^2=4+16=20$.

$K=2(40)-2(25)-20=10$

D'où $-MG^2+10=-10\Leftrightarrow MG^2=20\Leftrightarrow MG=2\sqrt 5$.

$\boxed{\Gamma_1=\mathcal C(G,2\sqrt 5)}$ : cercle de centre $G$ et de rayon $2\sqrt 5$.

**$\Gamma_2$** : $MA^2-MB^2=-5$.

Soit $M(x,y)$ : $MA^2-MB^2=2\vec{OM}\cdot\vec{BA}+OA^2-OB^2$ — plus directement, en coordonnées :

$MA^2-MB^2=\bigl[(x-0)^2+(y-2)^2\bigr]-\bigl[(x-1)^2+y^2\bigr]=x^2+y^2-4y+4-x^2+2x-1-y^2=2x-4y+3$

$\Gamma_2: 2x-4y+3=-5\Leftrightarrow 2x-4y+8=0\Leftrightarrow\boxed{x-2y+4=0}$

C'est une **droite** de vecteur normal $(1,-2)$, donc perpendiculaire à $\vec{AB}=(1,-2)$.

### 2) c) Position relative de $\Gamma_1$ et $\Gamma_2$

Distance de $G(6,0)$ à $\Gamma_2$ : $d=\dfrac{|6-0+4|}{\sqrt{1^2+(-2)^2}}=\dfrac{10}{\sqrt 5}=2\sqrt 5$.

Or rayon de $\Gamma_1$ vaut $2\sqrt 5=d$.

$\boxed{\Gamma_2\text{ est tangente à }\Gamma_1}$ (le point de tangence est le projeté orthogonal de $G$ sur $\Gamma_2$).
"""

CORRECTIONS["bac-c-2008-sn-math-ex4"] = r"""## Exercice 4

### 1) Tableau de variation de $u(x)=\dfrac{1}{\ln x}$ sur $]1,+\infty[$

$u'(x)=\dfrac{-1/x}{(\ln x)^2}=\dfrac{-1}{x(\ln x)^2}<0\ \forall x>1$, donc $u$ strictement décroissante.

* $\displaystyle\lim_{x\to 1^+}\ln x=0^+\Rightarrow\lim_{x\to 1^+}u(x)=+\infty$
* $\displaystyle\lim_{x\to+\infty}\ln x=+\infty\Rightarrow\lim_{x\to+\infty}u(x)=0^+$

| $x$ | $1$ | | $+\infty$ |
|---|---|---|---|
| $u'(x)$ | | $-$ | |
| $u(x)$ | $+\infty$ | $\searrow$ | $0^+$ |

### 2) Variation de $f(x)=e^{u(x)}=e^{1/\ln x}$

$f$ est la composée $\exp\circ u$. $\exp$ est strictement croissante et $u$ strictement décroissante sur $]1,+\infty[$, donc $\boxed{f\text{ est strictement décroissante sur }]1,+\infty[}$.

Limites :
* $\displaystyle\lim_{x\to 1^+}u(x)=+\infty\Rightarrow\lim_{x\to 1^+}f(x)=e^{+\infty}=+\infty$
* $\displaystyle\lim_{x\to+\infty}u(x)=0^+\Rightarrow\lim_{x\to+\infty}f(x)=e^0=1^+$

| $x$ | $1$ | | $+\infty$ |
|---|---|---|---|
| $f'(x)$ | | $-$ | |
| $f(x)$ | $+\infty$ | $\searrow$ | $1^+$ |

### 3) a) Encadrement de $F_n(x)$ et limite en $+\infty$

$F_n(x)=\displaystyle\int_x^{x+n}f(t)\,dt$ où $x>1$.

Sur $[x,x+n]$, $f$ est décroissante, donc $f(x+n)\leq f(t)\leq f(x)$. En intégrant sur un intervalle de longueur $n$ :

$\boxed{nf(x+n)\leq F_n(x)\leq nf(x)} \quad\blacksquare$

Limite en $+\infty$ : quand $x\to+\infty$, $f(x)\to 1$ et $f(x+n)\to 1$. Par encadrement :

$\boxed{\lim_{x\to+\infty}F_n(x)=n}$

### 3) b) Inégalités $e^x>1+x$ pour $x>0$ et $0<\ln t<t-1$ pour $t>1$

Soit $g(x)=e^x-1-x$. $g(0)=0$, $g'(x)=e^x-1>0$ pour $x>0$, donc $g$ croissante sur $[0,+\infty[$ donc $g(x)>g(0)=0$ pour $x>0$.

$\boxed{e^x>1+x\ \forall x>0} \quad\blacksquare$

Pour $t>1$, posons $x=t-1>0$ : $e^{t-1}>1+(t-1)=t$. En appliquant $\ln$ (croissante strictement) : $t-1>\ln t$.

De plus $\ln t>0$ pour $t>1$.

$\boxed{0<\ln t<t-1\ \forall t>1} \quad\blacksquare$

### 3) c) Minoration et limite en $1^+$

Sur $]1,+\infty[$, $u(t)=1/\ln t>0$, donc d'après l'inégalité $e^y>1+y$ avec $y=1/\ln t>0$ :

$f(t)=e^{1/\ln t}>1+\dfrac{1}{\ln t}$

Donc $f(t)-1>\dfrac{1}{\ln t}$.

D'après b), $\ln t<t-1$ (et $\ln t>0$), donc $\dfrac{1}{\ln t}>\dfrac{1}{t-1}$.

D'où $f(t)-1>\dfrac{1}{t-1}$.

En intégrant sur $[x,x+n]$ :

$F_n(x)-n=\displaystyle\int_x^{x+n}(f(t)-1)\,dt>\int_x^{x+n}\dfrac{dt}{t-1}=\bigl[\ln(t-1)\bigr]_x^{x+n}=\ln\!\left(\dfrac{x+n-1}{x-1}\right)$

$\boxed{F_n(x)-n>\ln\!\left(\dfrac{x+n-1}{x-1}\right)} \quad\blacksquare$

Limite en $1^+$ : quand $x\to 1^+$, $x-1\to 0^+$, donc $\dfrac{x+n-1}{x-1}\to+\infty$, donc $\ln\!\left(\dfrac{x+n-1}{x-1}\right)\to+\infty$. Par minoration :

$\boxed{\lim_{x\to 1^+}F_n(x)=+\infty}$

### 3) d) Tableau de variation de $F_n$

$F_n$ est dérivable et $F_n'(x)=f(x+n)-f(x)$. Comme $x+n>x$ et $f$ strictement décroissante, $f(x+n)<f(x)$, donc $F_n'(x)<0$.

| $x$ | $1$ | | $+\infty$ |
|---|---|---|---|
| $F_n'(x)$ | | $-$ | |
| $F_n(x)$ | $+\infty$ | $\searrow$ | $n$ |

### 3) e) Allure de $F_1$

$F_1$ est strictement décroissante de $+\infty$ à $1$. Asymptote verticale $x=1$ et asymptote horizontale $y=1$ en $+\infty$.
"""

CORRECTIONS["bac-c-2008-sn-math-ex5"] = r"""## Exercice 5

Plaçons $A(0,0)$, $B(a,0)$, $E(0,a)$ (triangle direct rectangle isocèle en $A$).

Le carré direct $AEFG$ a pour vecteurs successifs $\vec{AE}=(0,a)$, $\vec{EF}=(-a,0)$ (rotation $+\pi/2$), $\vec{FG}=(0,-a)$, $\vec{GA}=(a,0)$. Donc $F(-a,a)$, $G(-a,0)$.

Milieux : $I(a/2,0)$, $O(a/2,a/2)$, $C(0,a/2)$. Symétrique de $I$ par rapport à $O$ : $J=2O-I=(a/2,a)$.

### 1) b) Existence et unicité de $r$

$\vec{AE}=(0,a)$, $\vec{BA}=(-a,0)$. $\|\vec{AE}\|=\|\vec{BA}\|=a\neq 0$, donc il existe une unique rotation $r$ telle que $r(A)=B$ et $r(E)=A$. $\quad\blacksquare$

### 1) c) Angle et centre

**Angle** : $\theta=(\widehat{\vec{AE},\vec{BA}})=(\widehat{(0,a),(-a,0)})=\dfrac{\pi}{2}$.

**Centre** : intersection des médiatrices de $[AB]$ et $[EA]$.

* Médiatrice de $[AB]$ : $x=a/2$ (verticale).
* Médiatrice de $[EA]$ : $y=a/2$ (horizontale).

Intersection : $(a/2,a/2)=O$.

$\boxed{r=\text{rotation de centre }O\text{ et d'angle }\dfrac{\pi}{2}}$.

### 1) d) Image de $J$ par $r$

$\vec{OJ}=J-O=(0,a/2)$. Rotation $+\pi/2$ : $R_{\pi/2}(0,a/2)=(-a/2,0)$. Donc $r(J)=O+(-a/2,0)=(0,a/2)=C$.

$\boxed{r(J)=C}$

### 2) a) Existence et unicité de $s$

$C\neq A$ et $A\neq B$, donc il existe une unique similitude directe $s$ qui transforme $C$ en $A$ et $A$ en $B$. $\quad\blacksquare$

### 2) b) Angle et rapport de $s$

En notation complexe $s(z)=\alpha z+\beta$. Affixes : $A=0$, $B=a$, $C=\dfrac{ia}{2}$.

* $s(A)=B$ : $\beta=a$.
* $s(C)=A$ : $\alpha\cdot\dfrac{ia}{2}+a=0\Rightarrow\alpha=\dfrac{-2a}{ia}=\dfrac{-2}{i}=2i$.

$|\alpha|=2$, $\arg(\alpha)=\dfrac{\pi}{2}$.

$\boxed{\text{Rapport }k=2,\ \text{angle }\theta=\dfrac{\pi}{2}}$.

### 2) c) Vérification $s(E)=G$ et image du carré $COJE$

* $s(E)$ : $E=ia\Rightarrow s(E)=2i\cdot ia+a=-2a+a=-a=G$. $\boxed{s(E)=G} \quad\blacksquare$
* $s(O)$ : $O=\dfrac{a(1+i)}{2}\Rightarrow s(O)=2i\cdot\dfrac{a(1+i)}{2}+a=ia(1+i)+a=ia-a+a=ia=E$. Donc $s(O)=E$.
* $s(J)$ : $J=\dfrac{a}{2}+ia\Rightarrow s(J)=2i\!\left(\dfrac{a}{2}+ia\right)+a=ia-2a+a=-a+ia=F$. Donc $s(J)=F$.

D'où $s(C)=A$, $s(O)=E$, $s(J)=F$, $s(E)=G$, donc :

$\boxed{s(COJE)=AEFG}$

### 3) a) $\Omega$ appartient aux quatre cercles

L'angle de $s$ est $\theta=\dfrac{\pi}{2}$. Or pour toute similitude directe de centre $\Omega$ et d'angle $\theta$, et tout point $M\neq\Omega$ avec $M'=s(M)$, on a l'identité fondamentale :

$\bigl(\widehat{\vec{\Omega M},\vec{\Omega M'}}\bigr)=\theta=\dfrac{\pi}{2}$

Donc $\Omega$ voit le segment $[MM']$ sous un angle droit, ce qui équivaut à dire que **$\Omega$ appartient au cercle de diamètre $[MM']$**.

En appliquant à chacune des paires $(M,M')$ images l'une de l'autre par $s$ :

* $(C,A)$ : $\Omega\in$ cercle de diamètre $[CA]$
* $(A,B)$ : $\Omega\in$ cercle de diamètre $[AB]$
* $(E,G)$ : $\Omega\in$ cercle de diamètre $[EG]$
* $(J,F)$ : $\Omega\in$ cercle de diamètre $[JF]$

$\quad\blacksquare$

**Calcul explicite de $\Omega$** : $\Omega=\dfrac{\beta}{1-\alpha}=\dfrac{a}{1-2i}=\dfrac{a(1+2i)}{5}$, soit $\boxed{\Omega\!\left(\dfrac{a}{5},\dfrac{2a}{5}\right)}$.

### 3) b) Tangence des cercles $[JF]$ et $[AB]$ en $\Omega$

Soit $\Omega_1$ et $\Omega_2$ les centres respectifs des cercles de diamètres $[JF]$ et $[AB]$, c'est-à-dire les milieux $\Omega_1=(-a/4,a)$ et $\Omega_2=I=(a/2,0)$.

Deux cercles passant par un même point $\Omega$ sont tangents en $\Omega$ si et seulement si leurs centres et $\Omega$ sont alignés.

Vecteur $\vec{\Omega_1\Omega}=\Omega-\Omega_1=\left(\dfrac{a}{5}+\dfrac{a}{4},\dfrac{2a}{5}-a\right)=\left(\dfrac{9a}{20},-\dfrac{3a}{5}\right)=\dfrac{3a}{20}(3,-4)$.

Vecteur $\vec{\Omega_2\Omega}=\Omega-\Omega_2=\left(\dfrac{a}{5}-\dfrac{a}{2},\dfrac{2a}{5}\right)=\left(-\dfrac{3a}{10},\dfrac{2a}{5}\right)=\dfrac{-a}{10}(3,-4)$.

Les deux vecteurs sont colinéaires (de même direction $(3,-4)$), donc $\Omega_1,\Omega,\Omega_2$ alignés.

$\boxed{\text{Les cercles de diamètres }[JF]\text{ et }[AB]\text{ sont tangents en }\Omega} \quad\blacksquare$

### 4) a) $s(\Gamma)=\Gamma'$ et cocyclicité

$\Gamma$ : cercle de centre $A$ passant par $\Omega$, donc de rayon $A\Omega$.

$s$ est similitude de centre $\Omega$, rapport $2$, angle $\pi/2$. Image de $\Gamma$ par $s$ : cercle de centre $s(A)=B$ et de rayon $2\cdot A\Omega$.

Or $B\Omega=2\cdot A\Omega$ : vérifions. $A\Omega=\dfrac{a\sqrt 5}{5}$, $B\Omega=|a(1+2i)/5-a|=|a(-4+2i)/5|=\dfrac{a\sqrt{20}}{5}=\dfrac{2a\sqrt 5}{5}=2A\Omega$ ✓.

Donc l'image de $\Gamma$ par $s$ est le cercle de centre $B$ et de rayon $B\Omega$, c'est-à-dire $\Gamma'$.

$\boxed{s(\Gamma)=\Gamma'} \quad\blacksquare$

**Cocyclicité de $\Omega,A,B,D$** : Comme $D\in\Gamma$, on a $AD=A\Omega$, donc triangle $\Omega AD$ isocèle en $A$. Donc l'angle inscrit $\widehat{A\Omega D}=\widehat{AD\Omega}$.

De même, $D\in\Gamma'$ donne $BD=B\Omega$, triangle $\Omega BD$ isocèle en $B$, donc $\widehat{B\Omega D}=\widehat{BD\Omega}$.

Or $\widehat{A\Omega B}=$ angle de la similitude $s$ $=\dfrac{\pi}{2}$ (car $s$ envoie $A\Omega$ sur $B\Omega$, donc $\vec{\Omega A}$ est l'image de l'antécédent — plus précisément $\widehat{\vec{\Omega A},\vec{\Omega B}}=\pi/2$).

Si $D$ est intérieur à l'angle $\widehat{A\Omega B}$ : $\widehat{A\Omega D}+\widehat{D\Omega B}=\widehat{A\Omega B}=\dfrac{\pi}{2}$.

Donc $\widehat{ADB}=\widehat{AD\Omega}+\widehat{\Omega DB}=\widehat{A\Omega D}+\widehat{B\Omega D}=\dfrac{\pi}{2}$.

Conclusion : $\Omega$ et $D$ voient tous deux le segment $[AB]$ sous l'angle $\dfrac{\pi}{2}$, donc ils sont sur le cercle de diamètre $[AB]$.

$\boxed{\Omega,A,B,D\text{ sont cocycliques sur le cercle de diamètre }[AB]} \quad\blacksquare$

### 4) b) Alignement de $M,M',D$

Soit $M\in\Gamma\setminus\{\Omega,D\}$ et $M'=s(M)\in\Gamma'$.

D'après le théorème de l'angle inscrit dans $\Gamma$ (centre $A$), pour la corde $[\Omega D]$ :

$\bigl(\widehat{\vec{DM},\vec{D\Omega}}\bigr)=\dfrac{1}{2}\bigl(\widehat{\vec{AM},\vec{A\Omega}}\bigr)\pmod\pi\quad(\star)$

De même dans $\Gamma'$ pour $M'$ :

$\bigl(\widehat{\vec{DM'},\vec{D\Omega}}\bigr)=\dfrac{1}{2}\bigl(\widehat{\vec{BM'},\vec{B\Omega}}\bigr)\pmod\pi\quad(\star\star)$

Or $s$ est similitude directe : elle conserve les angles orientés. $s(A)=B$, $s(M)=M'$, $s(\Omega)=\Omega$, donc :

$\bigl(\widehat{\vec{BM'},\vec{B\Omega}}\bigr)=\bigl(\widehat{\vec{AM},\vec{A\Omega}}\bigr)$

D'où $(\star)=(\star\star)$, c'est-à-dire $\bigl(\widehat{\vec{DM},\vec{D\Omega}}\bigr)=\bigl(\widehat{\vec{DM'},\vec{D\Omega}}\bigr)\pmod\pi$.

Les droites $(DM)$ et $(DM')$ font le même angle avec $(D\Omega)$, donc $(DM)=(DM')$.

$\boxed{M,M',D\text{ sont alignés}} \quad\blacksquare$
"""

# === SENTINEL: insert new entries above this line ===
