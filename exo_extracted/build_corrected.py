"""Génère math_c_2014_corrected.json — corrections refaites par Claude
pour Bac C 2014 SN ex1, ex2, ex3, en gardant la méthodologie/style
des corrigés existants (T.V., A.H., I.P.P., \\Leftrightarrow, etc.).
"""
import json, datetime, pathlib

SRC = pathlib.Path(__file__).parent / "math_c_2014.json"
OUT = pathlib.Path(__file__).parent / "math_c_2014_corrected.json"

src = json.loads(SRC.read_text())

# Helpers
def find(num):
    for e in src:
        if e["exercice_numero"] == num and e["session"] == "Normale":
            return e
    raise KeyError(num)

# =========================================================================
# Exercice 1 — Complexes / Hyperbole
# =========================================================================
corr1 = r"""## Exercice 1

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

# =========================================================================
# Exercice 2 — Fonction xe^x, suite intégrale
# =========================================================================
corr2 = r"""## Exercice 2

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

# =========================================================================
# Exercice 3 — f(x)=x ln(1+1/x), suites intégrales
# =========================================================================
corr3 = r"""## Exercice 3

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

now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

out = []
for num, corr in [(1, corr1), (2, corr2), (3, corr3)]:
    src_ex = find(num)
    e = dict(src_ex)
    e["correction"] = corr
    e["correction_source"] = "claude-opus-4-7 rewrite"
    e["correction_quality"] = "claude_rewritten_v1"
    e["_corrected_at"] = now
    # garder l'ancienne pour comparaison
    e["correction_legacy"] = src_ex["correction"]
    out.append(e)

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(f"Wrote {OUT} with {len(out)} corrected exercices")
print(f"Avg correction length: {sum(len(e['correction']) for e in out)//len(out)} chars")
