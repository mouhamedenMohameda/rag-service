"""Chapitre « Fonctions Logarithmes et Exponentielles » — notions canoniques + cours
(format court, 6 sections).

Rédigé à partir du programme officiel (Curricula de mathématiques IGENRSE 2022
v0.3.1, items An53 à An79 — 7e année, séries C et D : tous ces items sont au
programme des deux séries) et du cours IPN « Fonctions ln et exp » (chapitre 8).
Chaque item du programme est couvert par exactement une notion (champ ``programme``).

Chargé sur le serveur par ``scripts/load_chapter_content.py`` : les cours sont
insérés en BROUILLON (validated_by_admin = False) ; l'admin les relit et les
valide dans l'atelier chapitre.
"""

CHAPITRE = "Fonctions Logarithmes et Exponentielles"
MATIERE = "math"
SOURCE = "Programme IGENRSE 2022 (An53-An79) + cours IPN « Fonctions ln et exp »"

_CD = ["C", "D"]

NOTIONS = [
    # ═══════════════════════════════ LOGARITHME ═══════════════════════════════
    {
        "id": "math.logexp.ln-definition-proprietes",
        "label": "Fonction ln : définition et propriétés algébriques",
        "series": _CD,
        "programme": ["An53", "An54"],
        "keywords": ["logarithme népérien", "logarithme neperien", "ln(ab)", "ln a + ln b"],
        "lesson": r"""## 1. L'idée en une phrase
$\ln$ est la primitive de $x \mapsto \dfrac{1}{x}$ sur $]0;+\infty[$ qui s'annule en $1$ : elle transforme les produits en sommes.

## 2. Définitions
- $\ln$ est définie sur $]0;+\infty[$, dérivable, et $\ln'(x) = \dfrac{1}{x}$ ; $\ln 1 = 0$.
- $\ln$ est strictement croissante sur $]0;+\infty[$ : $\ln x < 0$ si $0 < x < 1$, $\ln x > 0$ si $x > 1$.
- $\ln$ est une bijection de $]0;+\infty[$ sur $\mathbb{R}$ ; le réel $e \approx 2{,}718$ est l'unique solution de $\ln x = 1$.

## 3. Propriétés à connaître
Pour $a > 0$, $b > 0$ et $n \in \mathbb{Z}$ :
- $\ln(ab) = \ln a + \ln b$ ; $\ln\dfrac{a}{b} = \ln a - \ln b$ ; $\ln\dfrac{1}{b} = -\ln b$.
- $\ln(a^n) = n\ln a$ ; $\ln\sqrt{a} = \dfrac{1}{2}\ln a$ ; $\ln(e^n) = n$.
- $\ln a = \ln b \iff a = b$ ; $\ln a < \ln b \iff a < b$.

## 4. Méthodes
- **Simplifier une expression** : décomposer les produits, quotients et puissances avec les règles ci-dessus, puis regrouper.
- **Trouver le domaine d'une fonction avec $\ln u(x)$** : résoudre $u(x) > 0$.
- **Étudier le signe de $\ln u(x)$** : $\ln u(x) > 0 \iff u(x) > 1$ (avec $u(x) > 0$).

## 5. Exemple corrigé
Simplifier $A = \ln(\sqrt{5} + 1) + \ln(\sqrt{5} - 1)$.

$A = \ln\big[(\sqrt{5} + 1)(\sqrt{5} - 1)\big] = \ln(5 - 1) = \ln 4 = 2\ln 2$.

## 6. Pièges fréquents
- $\ln(a + b) \neq \ln a + \ln b$.
- $\ln(x^2) = 2\ln|x|$ pour $x \neq 0$, et non $2\ln x$ (qui n'existe que si $x > 0$).
- $\ln(-3)$ n'existe pas : vérifier le domaine avant tout calcul.
""",
    },
    {
        "id": "math.logexp.ln-equations",
        "label": "Équations, inéquations et systèmes avec ln",
        "series": _CD,
        "programme": ["An55", "An56", "An57"],
        "keywords": ["ln x =", "résoudre l'équation ln", "inéquation", "ln(x"],
        "lesson": r"""## 1. L'idée en une phrase
On résout une équation avec $\ln$ en fixant d'abord le domaine, puis en utilisant que $\ln$ est une bijection croissante.

## 2. Définitions
- $\ln x = m \iff x = e^m$ (pour tout réel $m$, solution unique dans $]0;+\infty[$).
- $\ln u(x) = \ln v(x) \iff u(x) = v(x)$ avec $u(x) > 0$ et $v(x) > 0$.
- $\ln u(x) < \ln v(x) \iff 0 < u(x) < v(x)$.

## 3. Propriétés à connaître
- $\ln x = 0 \iff x = 1$ ; $\ln x = 1 \iff x = e$.
- $\ln x \le m \iff 0 < x \le e^m$ ; $\ln x \ge m \iff x \ge e^m$.
- Pour une équation du second degré en $\ln x$ : poser $X = \ln x$ ($X$ décrit tout $\mathbb{R}$).

## 4. Méthodes
- **Étape 1 :** écrire les conditions d'existence et en déduire l'ensemble $E$ de résolution.
- **Étape 2 :** regrouper avec $\ln a + \ln b = \ln(ab)$ pour obtenir $\ln(\ldots) = \ln(\ldots)$ ou $\ln(\ldots) = m$.
- **Étape 3 :** résoudre l'équation algébrique, puis **garder seulement les solutions de $E$**.
- **Système** en $\ln x$ et $\ln y$ : poser $X = \ln x$, $Y = \ln y$, résoudre le système linéaire, puis $x = e^X$, $y = e^Y$.

## 5. Exemple corrigé
Résoudre $\ln(x - 2) + \ln(x - 1) = \ln 2$.

Domaine : $x > 2$. L'équation devient $\ln\big[(x - 2)(x - 1)\big] = \ln 2$, soit $x^2 - 3x + 2 = 2$, d'où $x(x - 3) = 0$. Seul $x = 3$ est dans $]2;+\infty[$ : $S = \{3\}$.

## 6. Pièges fréquents
- Oublier le domaine : ici $x = 0$ vérifie l'équation regroupée mais pas l'équation de départ.
- $\ln(x-2) + \ln(x-1)$ et $\ln\big[(x-2)(x-1)\big]$ n'ont pas le même domaine.
- Pour $(\ln x)^2 - \ln x - 2 = 0$, on trouve $X = -1$ ou $X = 2$ : il faut revenir à $x = e^{-1}$ ou $x = e^2$.
""",
    },
    {
        "id": "math.logexp.ln-limites",
        "label": "Limites usuelles de la fonction ln",
        "series": _CD,
        "programme": ["An58"],
        "keywords": ["lim ln", "ln x / x", "x ln x", "ln(1+x)"],
        "lesson": r"""## 1. L'idée en une phrase
$\ln x$ tend vers $+\infty$ quand $x \to +\infty$, mais beaucoup plus lentement que $x$ ; et vers $-\infty$ quand $x \to 0^+$.

## 2. Définitions
- $\lim\limits_{x \to +\infty} \ln x = +\infty$ ; $\lim\limits_{x \to 0^+} \ln x = -\infty$ (la droite $x = 0$ est asymptote verticale).
- Nombre dérivé en $1$ : $\lim\limits_{x \to 1} \dfrac{\ln x}{x - 1} = 1$ et $\lim\limits_{h \to 0} \dfrac{\ln(1 + h)}{h} = 1$.

## 3. Propriétés à connaître
- $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x} = 0$ : la courbe de $\ln$ a une branche parabolique de direction $(Ox)$.
- $\lim\limits_{x \to 0^+} x\ln x = 0$.
- Plus généralement, pour $n \ge 1$ : $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^n} = 0$ et $\lim\limits_{x \to 0^+} x^n\ln x = 0$.

## 4. Méthodes
- **Forme indéterminée $\infty - \infty$** (ex. $x - \ln x$) : factoriser par le terme dominant, $x - \ln x = x\left(1 - \dfrac{\ln x}{x}\right) \to +\infty$.
- **Forme $0 \times \infty$ en $0^+$** : se ramener à $x\ln x$.
- **Limite avec $\ln(1 + u)$** quand $u \to 0$ : écrire $\dfrac{\ln(1 + u)}{u} \to 1$.

## 5. Exemple corrigé
Calculer $\lim\limits_{x \to +\infty} \big(x - 2 - 2\ln x\big)$.

$x - 2 - 2\ln x = x\left(1 - \dfrac{2}{x} - 2\dfrac{\ln x}{x}\right)$. Comme $\dfrac{2}{x} \to 0$ et $\dfrac{\ln x}{x} \to 0$, la parenthèse tend vers $1$ et la limite vaut $+\infty$.

## 6. Pièges fréquents
- $\lim\limits_{x \to 0^+} \ln x = -\infty$, pas $0$.
- « $+\infty - \infty$ » n'est pas une limite : c'est une forme indéterminée à lever.
- $\dfrac{\ln x}{x} \to 0$ en $+\infty$, mais $\dfrac{\ln x}{x} \to -\infty$ en $0^+$.
""",
    },
    {
        "id": "math.logexp.ln-derivees",
        "label": "Dérivée de ln et de ln u",
        "series": _CD,
        "programme": ["An59", "An60"],
        "keywords": ["dérivée de ln", "u'/u", "(ln u)'"],
        "lesson": r"""## 1. L'idée en une phrase
$(\ln x)' = \dfrac{1}{x}$ et, plus généralement, $\big(\ln u\big)' = \dfrac{u'}{u}$ là où $u > 0$.

## 2. Définitions
- $\ln$ est dérivable sur $]0;+\infty[$ et $\ln'(x) = \dfrac{1}{x}$.
- Si $u$ est dérivable et strictement positive sur $I$, $\ln u$ est dérivable sur $I$ et $\big(\ln u(x)\big)' = \dfrac{u'(x)}{u(x)}$.
- Si $u$ ne s'annule pas sur $I$ : $\big(\ln|u(x)|\big)' = \dfrac{u'(x)}{u(x)}$.

## 3. Propriétés à connaître
- $\big(x\ln x\big)' = \ln x + 1$ ; $\left(\dfrac{\ln x}{x}\right)' = \dfrac{1 - \ln x}{x^2}$ ; $\big((\ln x)^2\big)' = \dfrac{2\ln x}{x}$.
- $\big(\ln(x + 1)\big)' = \dfrac{1}{x + 1}$ ; $\big(\ln(x^2 + 1)\big)' = \dfrac{2x}{x^2 + 1}$.
- Le signe de $\dfrac{u'}{u}$ est celui de $u'$ (car $u > 0$).

## 4. Méthodes
- **Dériver** un produit ou quotient contenant $\ln$ : appliquer $(uv)' = u'v + uv'$ et $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$, puis réduire au même dénominateur.
- **Étudier le signe de $f'$** : écrire $f'(x) = \dfrac{g(x)}{x^2}$ (ou $\dfrac{g(x)}{x}$) avec $x^2 > 0$ ; le signe de $f'$ est celui de $g$, souvent étudiée dans une partie A.

## 5. Exemple corrigé
$f(x) = x - 1 + \dfrac{1 + \ln x}{x}$ sur $]0;+\infty[$.

$\left(\dfrac{1 + \ln x}{x}\right)' = \dfrac{\frac{1}{x}\cdot x - (1 + \ln x)}{x^2} = \dfrac{-\ln x}{x^2}$, donc $f'(x) = 1 - \dfrac{\ln x}{x^2} = \dfrac{x^2 - \ln x}{x^2}$.

## 6. Pièges fréquents
- $\big(\ln(x + 1)\big)' = \dfrac{1}{x + 1}$, pas $\dfrac{1}{x}$.
- $(\ln x)^2 \neq \ln(x^2)$ : leurs dérivées sont $\dfrac{2\ln x}{x}$ et $\dfrac{2}{x}$.
- $\ln u$ n'est dérivable que là où $u > 0$.
""",
    },
    {
        "id": "math.logexp.ln-primitives",
        "label": "Primitives et intégrales avec ln (u'/u, ln x)",
        "series": _CD,
        "programme": ["An61"],
        "keywords": ["primitive", "u'/u", "∫ ln", "intégration par parties", "ln x dx"],
        "lesson": r"""## 1. L'idée en une phrase
Une fonction de la forme $\dfrac{u'}{u}$ a pour primitive $\ln|u|$ ; et $\ln x$ s'intègre par parties.

## 2. Définitions
- Sur un intervalle où $u$ ne s'annule pas : une primitive de $\dfrac{u'}{u}$ est $\ln|u|$ (donc $\ln u$ si $u > 0$).
- Une primitive de $\dfrac{1}{x}$ sur $]0;+\infty[$ est $\ln x$ ; de $\dfrac{1}{ax + b}$ est $\dfrac{1}{a}\ln|ax + b|$.
- Une primitive de $\ln x$ sur $]0;+\infty[$ est $x\ln x - x$.

## 3. Propriétés à connaître
- Primitive de $\dfrac{\ln x}{x}$ : $\dfrac{1}{2}(\ln x)^2$ (forme $u'u$).
- Primitive de $\dfrac{1}{x\ln x}$ sur $]1;+\infty[$ : $\ln(\ln x)$ (forme $\dfrac{u'}{u}$).
- Intégration par parties : $\displaystyle\int_a^b u'v = \big[uv\big]_a^b - \int_a^b uv'$.

## 4. Méthodes
- **Reconnaître $\dfrac{u'}{u}$** : chercher si le numérateur est (à une constante près) la dérivée du dénominateur.
- **Intégrer $\ln x$, $x\ln x$, $\dfrac{\ln x}{x^2}$** : par parties avec $v = \ln x$ (qu'on dérive) et $u'$ = le reste (qu'on intègre).
- **Calculer une aire** entre $C_f$ et l'axe des abscisses : $\displaystyle\int_a^b |f(x)|\,dx$ en unités d'aire, puis convertir en cm².

## 5. Exemple corrigé
Calculer $I = \displaystyle\int_1^e \ln x\,dx$.

On pose $v(x) = \ln x$, $v'(x) = \dfrac{1}{x}$, $u'(x) = 1$, $u(x) = x$ : $I = \big[x\ln x\big]_1^e - \displaystyle\int_1^e 1\,dx = e - (e - 1) = 1$.

## 6. Pièges fréquents
- Primitive de $\ln x$ : $x\ln x - x$, et non $\dfrac{1}{x}$ (c'est sa dérivée).
- $\displaystyle\int \dfrac{2x}{x^2 + 1}\,dx = \ln(x^2 + 1)$, sans valeur absolue car $x^2 + 1 > 0$.
- Une aire est positive : si $f \le 0$ sur $[a;b]$, l'aire vaut $-\displaystyle\int_a^b f$.
""",
    },
    {
        "id": "math.logexp.ln-etude",
        "label": "Étude et courbe d'une fonction comportant ln",
        "series": _CD,
        "programme": ["An62"],
        "keywords": ["ln x", "ln(x", "lnx"],
        "lesson": r"""## 1. L'idée en une phrase
Étudier une fonction avec $\ln$ suit toujours le même plan : domaine, limites, dérivée et signe, tableau de variation, éléments de la courbe.

## 2. Définitions
- Courbe de $\ln$ : passe par $(1;0)$ et $(e;1)$, asymptote verticale $x = 0$, branche parabolique de direction $(Ox)$ en $+\infty$.
- Tangente à la courbe de $\ln$ en $1$ : $y = x - 1$ ; la courbe est en dessous : $\ln x \le x - 1$.
- Asymptote oblique $y = ax + b$ en $+\infty$ : $\lim\limits_{x \to +\infty} \big(f(x) - (ax + b)\big) = 0$.

## 3. Propriétés à connaître
- Position de $C_f$ par rapport à la droite $\Delta : y = ax + b$ : signe de $d(x) = f(x) - (ax + b)$, qui contient souvent $\ln x$ (signe connu : négatif sur $]0;1[$, positif sur $]1;+\infty[$).
- Tangente en $x_0$ : $y = f'(x_0)(x - x_0) + f(x_0)$.
- Si $f$ est continue et strictement monotone sur $I$, elle réalise une bijection de $I$ sur $f(I)$.

## 4. Méthodes
- **Fonction auxiliaire** (partie A) : on étudie $g$ (souvent $g(x) = x^2 - 3 + 2\ln x$, $x - 3 + 3\ln x$…) pour obtenir le signe de $f'$.
- **Équation $f(x) = 0$ avec solution $\alpha$** : théorème des valeurs intermédiaires sur un intervalle où $f$ est strictement monotone, puis encadrement par calcul de $f(a)$ et $f(b)$.
- **Utiliser $g(\alpha) = 0$** pour simplifier $f(\alpha)$ : remplacer $\ln\alpha$ par son expression tirée de $g(\alpha) = 0$.

## 5. Exemple corrigé
$f(x) = 2x - 1 + \ln x$ sur $]0;+\infty[$.

$\lim\limits_{x \to 0^+} f(x) = -\infty$, $\lim\limits_{x \to +\infty} f(x) = +\infty$ ; $f'(x) = 2 + \dfrac{1}{x} > 0$ : $f$ est strictement croissante, donc bijection de $]0;+\infty[$ sur $\mathbb{R}$. Comme $f(0{,}6) \approx -0{,}31 < 0$ et $f(0{,}7) \approx 0{,}04 > 0$, l'équation $f(x) = 0$ a une unique solution $\alpha \in\, ]0{,}6;0{,}7[$.

## 6. Pièges fréquents
- Oublier de justifier la stricte monotonie avant d'appliquer le théorème de la bijection.
- Confondre $\dfrac{f(x)}{x} \to 0$ (branche de direction $(Ox)$) et $f(x) \to 0$ (asymptote horizontale).
- Écrire $f(\alpha)$ avec une valeur approchée de $\alpha$ alors qu'on demande une expression exacte.
""",
    },
    {
        "id": "math.logexp.log-base-a",
        "label": "Logarithme de base a, logarithme décimal et changement de base",
        "series": _CD,
        "programme": ["An63", "An64", "An65"],
        "keywords": ["log_a", "logarithme décimal", "logarithme de base", "log x", "ln 10"],
        "lesson": r"""## 1. L'idée en une phrase
Le logarithme de base $a$ est $\ln$ divisé par la constante $\ln a$ : $\log_a x = \dfrac{\ln x}{\ln a}$.

## 2. Définitions
- Pour $a > 0$, $a \ne 1$ : $\log_a(x) = \dfrac{\ln x}{\ln a}$ sur $]0;+\infty[$ ; $\log_a(a) = 1$, $\log_a(1) = 0$.
- Logarithme décimal : $\log x = \log_{10} x = \dfrac{\ln x}{\ln 10}$ ; $\log(10^n) = n$.
- $\log_e = \ln$.

## 3. Propriétés à connaître
- $\log_a$ a les mêmes règles algébriques que $\ln$ : $\log_a(xy) = \log_a x + \log_a y$, $\log_a(x^n) = n\log_a x$.
- $(\log_a x)' = \dfrac{1}{x\ln a}$ : $\log_a$ est croissante si $a > 1$, décroissante si $0 < a < 1$.
- Changement de base : $\log_a(x) = \dfrac{\ln b}{\ln a}\,\log_b(x)$.

## 4. Méthodes
- **Résoudre $a^x = b$** : $x = \log_a b = \dfrac{\ln b}{\ln a}$.
- **Nombre de chiffres** d'un entier $N \ge 1$ : c'est $p + 1$ où $p$ est la partie entière de $\log N$.
- **Calcul de pH** : $\text{pH} = -\log[\text{H}_3\text{O}^+]$.

## 5. Exemple corrigé
Résoudre $2^x = 5$.

$2^x = 5 \iff x\ln 2 = \ln 5 \iff x = \dfrac{\ln 5}{\ln 2} = \log_2 5 \approx 2{,}32$.

## 6. Pièges fréquents
- $\log_a$ n'est défini que pour $a > 0$ et $a \ne 1$.
- $\log(x + y) \neq \log x + \log y$.
- Pour $0 < a < 1$, $\ln a < 0$ : les inégalités changent de sens quand on divise par $\ln a$.
""",
    },
    # ═══════════════════════════════ EXPONENTIELLE ════════════════════════════
    {
        "id": "math.logexp.exp-definition-proprietes",
        "label": "Fonction exponentielle : définition et propriétés algébriques",
        "series": _CD,
        "programme": ["An66", "An67"],
        "keywords": ["exponentielle", "e^x", "exp(", "e^{x"],
        "lesson": r"""## 1. L'idée en une phrase
$\exp$ est la réciproque de $\ln$ : $y = e^x \iff x = \ln y$ ; elle transforme les sommes en produits.

## 2. Définitions
- $\exp$ est définie sur $\mathbb{R}$, à valeurs dans $]0;+\infty[$ : $e^x > 0$ pour tout réel $x$.
- Pour $x$ réel et $y > 0$ : $y = e^x \iff x = \ln y$.
- $e^0 = 1$ ; $e^1 = e$ ; $\ln(e^x) = x$ pour tout $x$ ; $e^{\ln y} = y$ pour tout $y > 0$.

## 3. Propriétés à connaître
- $e^{a + b} = e^a e^b$ ; $e^{a - b} = \dfrac{e^a}{e^b}$ ; $e^{-b} = \dfrac{1}{e^b}$.
- $(e^a)^n = e^{na}$ ; $\sqrt{e^a} = e^{a/2}$.
- $e^a = e^b \iff a = b$ ; $e^a < e^b \iff a < b$ (exp est strictement croissante).

## 4. Méthodes
- **Simplifier** : regrouper les exponentielles avec les règles ci-dessus, en écrivant $\sqrt[3]{e} = e^{1/3}$.
- **Signe d'une expression** $u(x)e^{v(x)}$ : c'est le signe de $u(x)$, car $e^{v(x)} > 0$.
- **Passer de $\ln$ à $\exp$** : $\ln\alpha = 2 - \alpha \iff \alpha = e^{2 - \alpha}$.

## 5. Exemple corrigé
Simplifier $A = \dfrac{e^{2x + 1}\,e^{-x}}{e^{x - 1}}$.

$A = e^{(2x + 1) + (-x) - (x - 1)} = e^{2}$.

## 6. Pièges fréquents
- $e^{a + b} \neq e^a + e^b$.
- $e^x$ n'est jamais nul ni négatif : une équation $e^x = 0$ ou $e^x = -2$ n'a pas de solution.
- $(e^x)^2 = e^{2x}$, pas $e^{x^2}$.
""",
    },
    {
        "id": "math.logexp.exp-equations",
        "label": "Équations, inéquations et systèmes avec exp",
        "series": _CD,
        "programme": ["An68", "An69", "An70"],
        "keywords": ["e^x =", "e^{2x}", "résoudre", "inéquation"],
        "lesson": r"""## 1. L'idée en une phrase
Pour résoudre une équation avec $e^x$, on applique $\ln$ (car $e^x = a \iff x = \ln a$ si $a > 0$), ou on pose $X = e^x$.

## 2. Définitions
- $e^x = a$ : si $a > 0$, une seule solution $x = \ln a$ ; si $a \le 0$, aucune solution.
- $e^{u(x)} = e^{v(x)} \iff u(x) = v(x)$ ; $e^{u(x)} < e^{v(x)} \iff u(x) < v(x)$.
- $e^x > a$ : si $a \le 0$, toujours vrai ; si $a > 0$, $x > \ln a$.

## 3. Propriétés à connaître
- $e^{2x} = (e^x)^2$ : une équation $ae^{2x} + be^x + c = 0$ devient $aX^2 + bX + c = 0$ avec $X = e^x > 0$.
- Un produit $(e^x - 1)(e^x - 2) = 0$ se traite facteur par facteur.
- Système en $e^x$ et $e^y$ : poser $X = e^x > 0$, $Y = e^y > 0$.

## 4. Méthodes
- **Second degré en $e^x$** : poser $X = e^x$, résoudre, **rejeter les solutions $X \le 0$**, puis $x = \ln X$.
- **Inéquation** : se ramener à $e^{u} < e^{v}$ ou à un signe de trinôme en $X = e^x$.
- **Égalité caractérisant $\alpha$** : de $f(\alpha) = 0$ tirer $e^\alpha = \ldots$ puis, si besoin, $\alpha = \ln(\ldots)$.

## 5. Exemple corrigé
Résoudre $e^{2x} + e^x - 42 = 0$.

On pose $X = e^x > 0$ : $X^2 + X - 42 = 0$, $\Delta = 169$, $X = 6$ ou $X = -7$. On rejette $-7$ ; $e^x = 6$ donne $x = \ln 6$.

## 6. Pièges fréquents
- Garder une solution $X = e^x$ négative.
- $e^{x^2 + 12x + 35} = 1 \iff x^2 + 12x + 35 = 0$ (car $1 = e^0$), et non $= 1$.
- Appliquer $\ln$ à une quantité qui peut être négative.
""",
    },
    {
        "id": "math.logexp.exp-limites",
        "label": "Limites usuelles de la fonction exponentielle",
        "series": _CD,
        "programme": ["An71"],
        "keywords": ["lim e^x", "e^x / x", "x e^x", "(e^x - 1)/x"],
        "lesson": r"""## 1. L'idée en une phrase
$e^x$ tend vers $+\infty$ en $+\infty$ (plus vite que toute puissance de $x$) et vers $0$ en $-\infty$.

## 2. Définitions
- $\lim\limits_{x \to +\infty} e^x = +\infty$ ; $\lim\limits_{x \to -\infty} e^x = 0$ (la droite $y = 0$ est asymptote en $-\infty$).
- Nombre dérivé en $0$ : $\lim\limits_{h \to 0} \dfrac{e^h - 1}{h} = 1$.

## 3. Propriétés à connaître
- $\lim\limits_{x \to +\infty} \dfrac{e^x}{x} = +\infty$ : branche parabolique de direction $(Oy)$.
- $\lim\limits_{x \to -\infty} xe^x = 0$.
- $\lim\limits_{x \to +\infty} e^{-x} = 0$ et $\lim\limits_{x \to -\infty} e^{-x} = +\infty$.

## 4. Méthodes
- **Forme $\infty \times 0$** (ex. $(x + 2)e^x$ en $-\infty$) : développer, $xe^x + 2e^x \to 0 + 0$.
- **Forme $\infty - \infty$** (ex. $e^x - x$ en $+\infty$) : factoriser par $e^x$ ou par $x$, $e^x - x = x\left(\dfrac{e^x}{x} - 1\right) \to +\infty$.
- **Asymptote oblique** en $-\infty$ pour $f(x) = ax + b + (\ldots)e^x$ : montrer que $(\ldots)e^x \to 0$.

## 5. Exemple corrigé
$f(x) = x + 2 + e^x$. Calculer $\lim\limits_{x \to -\infty} \big(f(x) - (x + 2)\big)$.

$f(x) - (x + 2) = e^x \to 0$ : la droite $y = x + 2$ est asymptote oblique à $C_f$ en $-\infty$, et $C_f$ est au-dessus car $e^x > 0$.

## 6. Pièges fréquents
- $\lim\limits_{x \to -\infty} e^x = 0$, pas $-\infty$.
- $\lim\limits_{x \to -\infty} xe^x$ est une forme indéterminée qui vaut $0$ (croissance comparée), à citer comme résultat de cours.
- $e^{-x} \to +\infty$ en $-\infty$ : attention au signe de l'exposant.
""",
    },
    {
        "id": "math.logexp.exp-derivees-primitives",
        "label": "Dérivées et primitives avec exp (e^u)",
        "series": _CD,
        "programme": ["An72", "An73", "An74"],
        "keywords": ["dérivée", "e^u", "u'e^u", "primitive", "(ax+b)e^x"],
        "lesson": r"""## 1. L'idée en une phrase
$\exp' = \exp$ ; plus généralement $\big(e^{u}\big)' = u'e^{u}$, et une primitive de $u'e^{u}$ est $e^{u}$.

## 2. Définitions
- $\exp$ est dérivable sur $\mathbb{R}$ et $(e^x)' = e^x$.
- Si $u$ est dérivable sur $I$ : $\big(e^{u(x)}\big)' = u'(x)e^{u(x)}$ ; par exemple $(e^{ax + b})' = ae^{ax + b}$.
- Une primitive de $e^{ax + b}$ ($a \ne 0$) est $\dfrac{1}{a}e^{ax + b}$.

## 3. Propriétés à connaître
- $\big((ax + b)e^x\big)' = (ax + a + b)e^x$ ; $\big(xe^{-x}\big)' = (1 - x)e^{-x}$.
- Une primitive de $P(x)e^x$ ($P$ polynôme) est de la forme $Q(x)e^x$ avec $Q$ de même degré.
- Une primitive de $\dfrac{e^x}{e^x + 1}$ est $\ln(e^x + 1)$ (forme $\dfrac{u'}{u}$).

## 4. Méthodes
- **Primitive de $(x + 1)^2e^x$** : chercher $F(x) = (ax^2 + bx + c)e^x$, dériver, identifier les coefficients avec $f$.
- **Relation du type $f' = f + e^x$** : en déduire une primitive ($F = f - e^x$).
- **Intégration par parties** pour $\displaystyle\int xe^{x}dx$ : dériver $x$, intégrer $e^x$.

## 5. Exemple corrigé
Trouver une primitive de $f(x) = (x^2 + 2x + 1)e^x$.

On cherche $F(x) = (ax^2 + bx + c)e^x$ : $F'(x) = \big(ax^2 + (2a + b)x + b + c\big)e^x$. Identification : $a = 1$, $2a + b = 2$, $b + c = 1$, donc $a = 1$, $b = 0$, $c = 1$ et $F(x) = (x^2 + 1)e^x$.

## 6. Pièges fréquents
- $(e^{-x})' = -e^{-x}$ : ne pas oublier le facteur $-1$.
- $(e^{x^2})' = 2xe^{x^2}$, et une primitive de $e^{x^2}$ ne s'exprime pas avec les fonctions usuelles.
- Primitive de $e^{2x}$ : $\dfrac{1}{2}e^{2x}$, pas $2e^{2x}$.
""",
    },
    {
        "id": "math.logexp.exp-etude",
        "label": "Étude et courbe d'une fonction comportant exp",
        "series": _CD,
        "programme": ["An75"],
        "keywords": ["e^x", "e^{x", "e^{-x", "exp"],
        "lesson": r"""## 1. L'idée en une phrase
Pour une fonction avec $e^x$, le signe de la dérivée vient presque toujours d'un facteur polynôme, car $e^{u} > 0$.

## 2. Définitions
- Courbe de $\exp$ : passe par $(0;1)$ et $(1;e)$, asymptote horizontale $y = 0$ en $-\infty$, branche parabolique de direction $(Oy)$ en $+\infty$.
- Tangente en $0$ : $y = x + 1$ ; la courbe est au-dessus : $e^x \ge x + 1$.
- Les courbes de $\ln$ et $\exp$ sont symétriques par rapport à la droite $y = x$.

## 3. Propriétés à connaître
- $f(x) = P(x)e^x \Rightarrow f'(x) = \big(P(x) + P'(x)\big)e^x$ : signe de $P + P'$.
- Courbe de la réciproque $f^{-1}$ : symétrique de $C_f$ par rapport à $y = x$ ; $(f^{-1})'(b) = \dfrac{1}{f'(a)}$ si $b = f(a)$.
- Asymptote oblique $y = ax + b$ en $-\infty$ si le terme avec $e^x$ tend vers $0$.

## 4. Méthodes
- **Plan d'étude** : limites aux bornes (avec croissances comparées), dérivée et signe, tableau, asymptotes et position, tangentes, points d'intersection avec les axes, tracé.
- **Équation $f(x) = 0$** : bijection puis encadrement de $\alpha$ ; utiliser $e^\alpha = \ldots$ pour exprimer $f(\alpha)$ ou $(f^{-1})'(0)$.
- **Tangente parallèle à une droite de pente $m$** : résoudre $f'(x) = m$.

## 5. Exemple corrigé
$f(x) = (x + 2)e^x$ sur $\mathbb{R}$.

$f'(x) = e^x + (x + 2)e^x = (x + 3)e^x$, du signe de $x + 3$ : $f$ décroît sur $]-\infty;-3]$ et croît sur $[-3;+\infty[$, minimum $f(-3) = -e^{-3}$. En $-\infty$ : $f(x) = xe^x + 2e^x \to 0$ (asymptote $y = 0$) ; en $+\infty$ : $f(x) \to +\infty$ et $\dfrac{f(x)}{x} \to +\infty$ (branche de direction $(Oy)$).

## 6. Pièges fréquents
- Oublier $e^x > 0$ quand on étudie le signe de $f'$.
- Placer l'asymptote $y = 0$ du mauvais côté : pour $e^{x}$ elle est en $-\infty$, pour $e^{-x}$ elle est en $+\infty$.
- Confondre la courbe de $f^{-1}$ avec celle de $\dfrac{1}{f}$.
""",
    },
    {
        "id": "math.logexp.exp-base-a-puissance",
        "label": "Exponentielle de base a et fonctions puissances",
        "series": _CD,
        "programme": ["An76", "An77", "An78"],
        "keywords": ["a^x", "2^x", "10^x", "x^a", "puissance", "x^x"],
        "lesson": r"""## 1. L'idée en une phrase
Pour $a > 0$ et $b$ réel, on définit $a^b = e^{b\ln a}$ : toutes les puissances se ramènent à $\exp$ et $\ln$.

## 2. Définitions
- Exponentielle de base $a$ ($a > 0$) : $x \mapsto a^x = e^{x\ln a}$, définie sur $\mathbb{R}$, à valeurs dans $]0;+\infty[$.
- Fonction puissance ($\alpha$ réel) : $x \mapsto x^\alpha = e^{\alpha\ln x}$ sur $]0;+\infty[$.
- $10^x = e^{x\ln 10}$ est la réciproque du logarithme décimal.

## 3. Propriétés à connaître
- $a^{x + y} = a^xa^y$ ; $a^{-x} = \dfrac{1}{a^x}$ ; $(a^x)^y = a^{xy}$ ; $(ab)^x = a^xb^x$ ; $\ln(a^x) = x\ln a$.
- $(a^x)' = (\ln a)\,a^x$ : croissante si $a > 1$, décroissante si $0 < a < 1$.
- $(x^\alpha)' = \alpha x^{\alpha - 1}$ sur $]0;+\infty[$.

## 4. Méthodes
- **Étudier $f(x) = u(x)^{v(x)}$** (ex. $x^x$) : écrire $f(x) = e^{v(x)\ln u(x)}$, puis dériver $e^{w}$.
- **Limite de $x^x$ en $0^+$** : $x\ln x \to 0$ donc $x^x \to e^0 = 1$.
- **Comparer $a^x$ et $b^x$** : comparer $x\ln a$ et $x\ln b$.

## 5. Exemple corrigé
Dériver $f(x) = x^x$ sur $]0;+\infty[$.

$f(x) = e^{x\ln x}$ et $(x\ln x)' = \ln x + 1$, donc $f'(x) = (\ln x + 1)x^x$, du signe de $\ln x + 1$ : $f$ décroît sur $\left]0;\frac{1}{e}\right]$ et croît sur $\left[\frac{1}{e};+\infty\right[$.

## 6. Pièges fréquents
- $(2^x)' \neq x\,2^{x - 1}$ : c'est $(\ln 2)\,2^x$.
- $x^\alpha$ avec $\alpha$ non entier n'est défini que pour $x > 0$.
- $a^x$ n'a de sens que pour $a > 0$.
""",
    },
    {
        "id": "math.logexp.croissances-comparees",
        "label": "Croissances comparées (ln, puissances, exp)",
        "series": _CD,
        "programme": ["An79"],
        "keywords": ["croissance comparée", "croissances comparées", "x^n e^", "ln x / x^n"],
        "lesson": r"""## 1. L'idée en une phrase
En $+\infty$, l'exponentielle l'emporte sur toute puissance de $x$, qui l'emporte elle-même sur le logarithme.

## 2. Définitions
Pour tout entier $n \ge 1$ :
- $\lim\limits_{x \to +\infty} \dfrac{e^x}{x^n} = +\infty$ ; $\lim\limits_{x \to -\infty} x^ne^x = 0$.
- $\lim\limits_{x \to +\infty} \dfrac{\ln x}{x^n} = 0$ ; $\lim\limits_{x \to 0^+} x^n\ln x = 0$.

## 3. Propriétés à connaître
- Cas les plus utilisés : $\dfrac{e^x}{x} \to +\infty$, $xe^{-x} \to 0$ en $+\infty$, $\dfrac{\ln x}{x} \to 0$ en $+\infty$, $x\ln x \to 0$ en $0^+$.
- Avec des puissances de $\ln$ : $\dfrac{(\ln x)^2}{x} \to 0$ en $+\infty$ (se démontre en posant $x = t^2$, non à citer comme limite usuelle).

## 4. Méthodes
- **Repérer le terme dominant** et factoriser par lui pour lever l'indétermination.
- **Changer de variable** : $\lim\limits_{x \to +\infty} \dfrac{e^{2x}}{x} = \lim\limits_{X \to +\infty} \dfrac{2e^{X}}{X}$ avec $X = 2x$.
- **Citer explicitement** « par croissance comparée » dans la rédaction.

## 5. Exemple corrigé
Calculer $\lim\limits_{x \to +\infty} \dfrac{e^x - x}{x^2}$.

$\dfrac{e^x - x}{x^2} = \dfrac{e^x}{x^2} - \dfrac{1}{x}$. Par croissance comparée $\dfrac{e^x}{x^2} \to +\infty$ et $\dfrac{1}{x} \to 0$, donc la limite vaut $+\infty$.

## 6. Pièges fréquents
- Croire que $\dfrac{x^{10}}{e^x}$ tend vers $+\infty$ : il tend vers $0$.
- Utiliser $x\ln x \to 0$ en $+\infty$ (faux : c'est en $0^+$).
- Oublier de mentionner le résultat de cours utilisé.
""",
    },
]

# ═══════════════════════ Notions de chaque exercice (vérifiées) ═══════════════════
# Lues dans chaque énoncé. Série D : énoncés vérifiés sur les PDF (enonces_d_2010_2014,
# enonces_logexp_d). Série C : à revoir quand les énoncés C auront été vérifiés. Clés courtes :
_K = {
    "LD": "math.logexp.ln-definition-proprietes",
    "LE": "math.logexp.ln-equations",
    "LL": "math.logexp.ln-limites",
    "LV": "math.logexp.ln-derivees",
    "LP": "math.logexp.ln-primitives",
    "LS": "math.logexp.ln-etude",
    "LB": "math.logexp.log-base-a",
    "XD": "math.logexp.exp-definition-proprietes",
    "XE": "math.logexp.exp-equations",
    "XL": "math.logexp.exp-limites",
    "XV": "math.logexp.exp-derivees-primitives",
    "XS": "math.logexp.exp-etude",
    "XB": "math.logexp.exp-base-a-puissance",
    "CC": "math.logexp.croissances-comparees",
}

_TAGS: dict[str, str] = {
    # Série C
    "bac-c-2015-sc-math-ex4": "XS XL XV CC",
    "bac-c-2015-sc-math-ex5": "LS LL LV LP",
    "bac-c-2015-sn-math-ex3": "XS XL XV XE LP",
    "bac-c-2015-sn-math-ex4": "LS LL LV LP LD",
    "bac-c-2016-sc-math-ex2": "XS XL XV CC",
    "bac-c-2016-sc-math-ex3": "XS XL XV XE LD",
    "bac-c-2016-sn-math-ex3": "XS XL XV CC",
    "bac-c-2016-sn-math-ex4": "LS LL LV LP",
    "bac-c-2017-sc-math-ex4": "LS LL LV LP",
    "bac-c-2017-sn-math-ex3": "XS XL XV LP",
    "bac-c-2017-sn-math-ex4": "LS LL LV LP CC",
    "bac-c-2018-sc-math-ex2": "XS XL XV CC",
    "bac-c-2018-sc-math-ex4": "LS LL LV LD XL",
    "bac-c-2018-sn-math-ex4": "XS XL XV XE",
    "bac-c-2018-sn-math-ex5": "LS LL LV LP",
    "bac-c-2019-sc-math-ex4": "LS LL LV CC",
    "bac-c-2019-sn-math-ex5": "XS XL XV LP",
    "bac-c-2020-sn-math-ex4": "LS LL LV LD LP CC",
    "bac-c-2020-sn-math-ex5": "XS XL XV CC",
    "bac-c-2021-sn-math-ex4": "LS LL LV CC",
    "bac-c-2022-sc-math-ex4": "XS XL XV CC",
    "bac-c-2022-sc-math-ex5": "LS LL LV LP",
    "bac-c-2022-sn-math-ex4": "LS LL LV LP CC",
    "bac-c-2023-sn-math-ex4": "LS LL LV LP LD CC",
    "bac-c-2023-sn-math-ex5": "XS XL XV LP",
    "bac-c-2024-sc-math-ex2": "XB LS LL LV CC",
    "bac-c-2024-sc-math-ex5": "XS XL XV",
    "bac-c-2025-sn-math-ex4": "LS LL LV LP",
    "bac-c-2025-sn-math-ex5": "XS XL XV XE LP",
    # Série D — 2010-2014 (énoncés retranscrits, content/enonces_d_2010_2014.py)
    "bac-d-2010-sn-math-ex4": "XS XL XV LS LD",
    "bac-d-2010-sc-math-ex3": "LS LL LV LP",
    "bac-d-2010-sc-math-ex4": "XS XL XV XE LP",
    "bac-d-2011-sn-math-ex3": "XS XL XV CC",
    "bac-d-2011-sn-math-ex4": "LS LL LV LP CC",
    "bac-d-2011-sc-math-ex4": "LS LL LV LP XS XL",
    "bac-d-2012-sn-math-ex3": "XS XL XV XD",
    "bac-d-2012-sn-math-ex4": "LS LL LV LP",
    "bac-d-2012-sc-math-ex3": "LS LL LV LP LE XD",
    "bac-d-2012-sc-math-ex4": "XS XL XV CC",
    "bac-d-2013-sn-math-ex4": "LS LL LV LP CC",
    "bac-d-2013-sc-math-ex3": "LS LL LV LP",
    "bac-d-2013-sc-math-ex4": "XS XL XV XE CC",
    "bac-d-2014-sn-math-ex3": "XS XL XV XE",
    "bac-d-2014-sn-math-ex4": "LS LL LV LP CC",
    "bac-d-2014-sc-math-ex3": "XS XL XV CC",
    "bac-d-2014-sc-math-ex4": "LS LL LV LP",
    # Série D — 2015-2025
    "bac-d-2015-sc-math-ex3": "XS XL XV CC",
    "bac-d-2015-sc-math-ex4": "LS LL LV LP CC",
    "bac-d-2015-sn-math-ex3": "LS LL LV LP CC",
    "bac-d-2015-sn-math-ex4": "XS XL XV CC",
    "bac-d-2016-sc-math-ex3": "XS XL XV CC",
    "bac-d-2016-sc-math-ex4": "LS LL LV LP XD",
    "bac-d-2016-sn-math-ex3": "XS XL XV CC",
    "bac-d-2016-sn-math-ex4": "LS LL LV LP CC",
    "bac-d-2017-sc-math-ex3": "XS XL XV CC",
    "bac-d-2017-sc-math-ex4": "LS LL LV CC",
    "bac-d-2017-sn-math-ex3": "XS XL XV XE XD",
    "bac-d-2017-sn-math-ex4": "LS LL LV LP",
    "bac-d-2018-sc-math-ex3": "XS XL XV",
    "bac-d-2018-sc-math-ex4": "LS LL LV LP CC",
    "bac-d-2018-sn-math-ex4": "LS LL LV LP CC",
    "bac-d-2019-sc-math-ex3": "LS LL LV CC",
    "bac-d-2019-sc-math-ex4": "XS XL XV CC",
    "bac-d-2019-sn-math-ex4": "LS LL LV LP",
    "bac-d-2020-sc-math-ex3": "XS XL XV XE XD",
    "bac-d-2020-sc-math-ex4": "LS LL LV LP CC",
    "bac-d-2020-sn-math-ex3": "XS XL XV",
    "bac-d-2020-sn-math-ex4": "LS LL LV LP CC",
    "bac-d-2021-sc-math-ex3": "LS LL LV LP CC",
    "bac-d-2021-sc-math-ex4": "XS XL XV CC",
    "bac-d-2021-sn-math-ex4": "LS LL LV CC",
    "bac-d-2022-sc-math-ex3": "XS XL XV CC",
    "bac-d-2022-sc-math-ex4": "LS LL LV LP CC",
    "bac-d-2022-sn-math-ex5": "LS LL LV LP CC",
    "bac-d-2023-sn-math-ex5": "LS LL LV CC",
    "bac-d-2024-sn-math-ex3": "XS XL XV",
    "bac-d-2024-sn-math-ex5": "LS LL LV CC",
    # Études de fonctions exponentielles rangées dans d'autres chapitres (log/exp en principal ou en second)
    "bac-d-2018-sn-math-ex3": "XS XL XV CC",
    "bac-d-2019-sn-math-ex3": "XS XL XV CC",
    "bac-d-2021-sn-math-ex3": "XS XL XV CC",
    "bac-d-2022-sn-math-ex4": "XS XL XV CC",
    "bac-d-2023-sn-math-ex3": "XS XL XV CC",
}

EXERCISE_TAGS = {eid: [_K[k] for k in keys.split()] for eid, keys in _TAGS.items()}
