"""Énoncés vérifiés — chapitre « Fonctions Logarithmes et Exponentielles », série D,
sujets 2015-2025.

Retranscrits depuis les PDF originaux (drive_archive/annals/Sujets corrigés math/
bac d/), lus sur l'image de chaque page, en remplacement du texte OCR en base
(gardé dans ``ennonce_ocr``). Les valeurs numériques (encadrements, racines,
formules à vérifier) ont été contrôlées par calcul ; les erreurs du sujet
original sont signalées en note admin.

Chargé par scripts/load_enonces.py (brouillon : rien n'est validé).
"""

ENONCES: dict[str, dict] = {}
CH = "Fonctions Logarithmes et Exponentielles"


def _add(eid: str, enonce: str, chapitres: list[str] | None = None, note: str = "",
         chapitre: str = CH) -> None:
    assert eid not in ENONCES, eid
    ENONCES[eid] = {"chapitre": chapitre, "chapitres": chapitres or [], "enonce": enonce.strip(),
                    "note": note, "replace_ocr": True}


# ═══════════════════════════════════ 2015 — session normale ═══════════════════

_add("bac-d-2015-sn-math-ex3", r"""
**Exercice 3 (6 points)**

On considère la fonction $f$ définie sur $[0;+\infty[$ par : $\begin{cases} f(x) = 3x - 3 - 2x\ln x, & x > 0 \\ f(0) = -3 \end{cases}$

Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Calculer $\lim\limits_{x \to 0^+} f(x)$. En déduire que $f$ est continue à droite de $x_0 = 0$.

b) Montrer que $\lim\limits_{x \to 0^+} \dfrac{f(x) - f(0)}{x} = -\infty$ et interpréter graphiquement.

c) Montrer que $\lim\limits_{x \to +\infty} f(x) = -\infty$.

**2. a)** Calculer $f'(x)$ pour $x \in\, ]0;+\infty[$ et vérifier que $f'(\sqrt{e}) = 0$.

b) Dresser le tableau de variation de la fonction $f$.

**3. a)** Déterminer une équation de la tangente $(T)$ à $(C)$ au point $A$ d'abscisse $x_0 = 1$.

b) Montrer que $(C)$ coupe l'axe des abscisses $(Ox)$ en un point $B$ autre que $A$ dont l'abscisse $\alpha$ est telle que $2{,}3 \le \alpha \le 2{,}4$.

c) Déduire de ce qui précède le signe de $f(x)$ sur $[0;+\infty[$.

**4)** On considère la fonction $g$ définie par : $\begin{cases} g(x) = \dfrac{1}{2}x^2 - x^2\ln x, & x > 0 \\ g(0) = 0 \end{cases}$

a) Montrer que pour tout $x > 0$, $f(x) = 3x - 3 + g'(x)$.

b) En déduire une primitive $F$ de $f$ sur $]0;+\infty[$.

**5)** Pour tout entier naturel $n \ge 1$ on pose : $U_n = \displaystyle\int_{\frac{1}{n}}^{1} f(x)\,dx$.

a) Montrer que la suite $(U_n)$ est décroissante.

b) Exprimer $U_n$ en fonction de $n$.

c) Calculer $\lim\limits_{n \to +\infty} U_n$.
""", ["Intégration et Primitives", "Suites numériques"])

_add("bac-d-2015-sn-math-ex4", r"""
**Exercice 4 (6 points)**

On considère la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = (x - 2)(1 + e^x)$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Justifier que $\lim\limits_{x \to +\infty} f(x) = +\infty$. Calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

b) Calculer $\lim\limits_{x \to -\infty} \big(f(x) - (x - 2)\big)$ et en donner une interprétation graphique.

**2. a)** Calculer la dérivée $f'(x)$ puis la dérivée seconde $f''(x)$.

b) En déduire que la courbe $(C)$ possède un point d'inflexion $A$ dont on précisera les coordonnées.

c) Dresser le tableau de variation de la dérivée $f'$. En déduire le signe de $f'(x)$ pour tout réel $x$.

**3. a)** À l'aide des questions précédentes, dresser le tableau de variation de $f$.

b) Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ que l'on déterminera. On désigne par $(C')$ la courbe représentative de la réciproque $f^{-1}$ dans le repère $(O;\vec{i},\vec{j})$.

**4. a)** Déterminer les points d'intersection de la courbe $(C)$ avec les axes de coordonnées.

b) Déterminer le point $B$ de $(C)$ où la tangente $T$ à la courbe $(C)$ est parallèle à l'asymptote $(D)$. Donner une équation de $T$.

c) Tracer $(C)$, $T$, $(D)$ et $(C')$.

d) Discuter graphiquement le nombre de solutions de l'équation $x - 2 = (2 + m)e^{-x}$.

**5. a)** Calculer l'intégrale $I = \displaystyle\int_0^2 (x - 2 - 2e^x)\,dx$.

b) En utilisant une intégration par parties, calculer $J = \displaystyle\int_0^2 xe^x\,dx$.

c) Calculer l'aire du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 0$ et $x = 2$.
""", ["Intégration et Primitives"],
     note="L'asymptote (D) de la question 4b est la droite y = x − 2 de la question 1b (le sujet ne la nomme pas avant).")

# ══════════════════════════════ 2015 — session complémentaire ═════════════════

_add("bac-d-2015-sc-math-ex3", r"""
**Exercice 3 (6 points)**

**1)** On considère la fonction numérique $g$ définie par $g(x) = (2x + 1)e^x + 1$.

a) Justifier que $\lim\limits_{x \to +\infty} g(x) = +\infty$ et $\lim\limits_{x \to -\infty} g(x) = 1$.

b) Calculer $g'(x)$ et dresser le tableau de variation de $g$.

c) En déduire que pour tout réel $x$, $g(x) > 0$.

**2)** On considère la fonction numérique $f$ définie par $f(x) = x + 2 + (2x - 1)e^x$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

a) Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

b) Calculer et interpréter graphiquement $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

c) Montrer que la droite $D$ d'équation $y = x + 2$ est une asymptote oblique à $(C)$ au voisinage de $-\infty$ puis déterminer leurs positions relatives.

**3)** Écrire $f'(x)$ en fonction de $g(x)$ et dresser le tableau de variation de $f$.

**4. a)** Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$ puis vérifier que $-0{,}86 < \alpha < -0{,}85$.

**5. a)** Montrer qu'il existe un unique point $A$ en lequel la tangente $T$ à $(C)$ est parallèle à l'asymptote oblique. Préciser les coordonnées de $A$ et donner l'équation de $T$.

b) Construire la courbe $(C)$, la tangente $T$ et l'asymptote $D$.

c) Discuter graphiquement, suivant les valeurs de $m$, le nombre de solutions de l'équation $(2x - 1)e^x - m + 2 = 0$.
""", note="Erreur du sujet original, vérifiée par calcul : α ≈ −0,8443, donc −0,85 < α < −0,84 "
          "(f(−0,86) ≈ −0,011 et f(−0,85) ≈ −0,004 sont tous deux négatifs). L'énoncé est recopié tel quel ; "
          "la correction doit le signaler.")

_add("bac-d-2015-sc-math-ex4", r"""
**Exercice 4 (6 points)**

**Partie A**

Soit $g$ la fonction définie sur $]0;+\infty[$ par $g(x) = 2x^2 + \ln x$.

**1. a)** Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer la dérivée $g'(x)$ et dresser le tableau de variation de $g$.

**2. a)** Montrer que $g$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ à déterminer.

b) Démontrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$ telle que $0{,}54 < \alpha < 0{,}55$.

c) En déduire le signe de $g(x)$ sur $]0;+\infty[$.

**Partie B**

On considère la fonction $f$ définie sur $]0;+\infty[$ par $f(x) = 2x - \dfrac{1 + \ln x}{x}$. On appelle $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 2 cm.

**1. a)** Justifier que $\lim\limits_{x \to 0^+} f(x) = +\infty$ et en donner une interprétation géométrique.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \big(f(x) - 2x\big)$. En déduire que $(C)$ admet une asymptote oblique $(\Delta)$ en $+\infty$.

c) Étudier la position relative de $(C)$ et $(\Delta)$.

**2. a)** Calculer $f'(x)$ puis vérifier que $f'(x) = \dfrac{g(x)}{x^2}$.

b) Dresser le tableau de variation de $f$.

c) Vérifier que $f(\alpha) = \dfrac{4\alpha^2 - 1}{\alpha}$ et en donner une valeur approchée.

**3. a)** Donner une équation de la tangente $(T)$ à $(C)$ au point d'abscisse $x_0 = \dfrac{1}{e}$.

b) Tracer $(C)$, $(\Delta)$ et $(T)$ dans le repère $(O;\vec{i},\vec{j})$ d'unité 2 cm.

**4. a)** Donner une primitive $F$ de $f$ sur $]0;+\infty[$.

b) Calculer l'aire, en unité d'aire, du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = \dfrac{1}{e}$ et $x = 1$.
""", ["Intégration et Primitives"])

# ═══════════════════════════════════ 2016 — session normale ═══════════════════

_add("bac-d-2016-sn-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x - 1 + \dfrac{x}{e^x} = x - 1 + xe^{-x}$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1)** On considère la fonction $g$ définie sur $\mathbb{R}$ par $g(x) = 1 - x + e^x$.

a) Calculer $g'(x)$, où $g'$ est la dérivée de $g$.

b) Étudier les variations de $g$ et en déduire le signe de $g(x)$ sur $\mathbb{R}$.

**2. a)** Calculer les limites suivantes : $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x}$, puis interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$. Montrer que la droite $(\Delta)$ d'équation $y = x - 1$ est une asymptote oblique à $(C)$ et étudier la position relative de $(C)$ et $(\Delta)$.

**3. a)** Calculer la dérivée $f'(x)$ puis vérifier que $f'(x) = \dfrac{g(x)}{e^x}$.

b) Dresser le tableau de variation de $f$ sur $\mathbb{R}$.

**4. a)** Déterminer le point $A$ de $(C)$ où la tangente $T$ à la courbe $(C)$ est parallèle à l'asymptote $(\Delta)$. Donner une équation de $T$.

b) Tracer $T$, $(\Delta)$ et $(C)$.

**5)** Soit $H$ la fonction définie sur $\mathbb{R}$ par $H(x) = -(x + 1)e^{-x}$.

a) Vérifier que $H'(x) = f(x) - x + 1$. En déduire une primitive $F$ de $f$ sur $\mathbb{R}$.

b) Calculer l'aire du domaine plan limité par $(C)$, $(\Delta)$ et les droites d'équations $x = 1$ et $x = 3$.
""", ["Intégration et Primitives"])

_add("bac-d-2016-sn-math-ex4", r"""
**Exercice 4 (7 points)**

**Partie A**

On considère la fonction $g$ définie sur $]0;+\infty[$ par $g(x) = x^3 - 2 + 4\ln x$.

**1. a)** Montrer que $g$ est strictement croissante sur $]0;+\infty[$.

b) Dresser le tableau de variation de $g$.

**2. a)** Montrer que $g$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$. Vérifier que $1{,}1 < \alpha < 1{,}2$.

c) En déduire le signe de $g(x)$ sur $]0;+\infty[$.

**Partie B**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = x - 1 - \dfrac{2\ln x}{x^2}$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = +\infty$ et interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \big(f(x) - (x - 1)\big)$. En déduire que la courbe $(C)$ admet une asymptote oblique $\Delta$ dont on donnera une équation.

c) Étudier la position relative de $(C)$ et $\Delta$.

**2. a)** Calculer $f'(x)$ et vérifier que pour tout $x$ de $]0;+\infty[$ on a : $f'(x) = \dfrac{g(x)}{x^3}$.

b) Montrer que $f(\alpha) = \dfrac{3\alpha^3 - 2\alpha^2 - 2}{2\alpha^2}$.

c) Dresser le tableau de variation de $f$.

**3. a)** Donner l'équation de la tangente $T$ à la courbe $(C)$ au point $A$ d'abscisse $1$. Vérifier que $T$ est perpendiculaire à $\Delta$.

b) Montrer que la courbe $(C)$ coupe $(Ox)$ en un point $B$ autre que $A$ d'abscisse $\beta$ telle que $1{,}3 < \beta < 1{,}4$.

c) Représenter la courbe $(C)$ et les droites $\Delta$ et $(T)$ dans le repère $(O;\vec{i},\vec{j})$.

d) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $2x^3 - (m + 1)x^2 - 2\ln x = 0$.

**4)** Soit $S$ l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = \beta$.

a) Justifier que $S = -\displaystyle\int_1^\beta f(x)\,dx$.

b) En utilisant une intégration par parties, calculer $I = \displaystyle\int_1^\beta \dfrac{\ln x}{x^2}\,dx$. Calculer $S$ en fonction de $\beta$.
""", ["Intégration et Primitives"])

# ══════════════════════════════ 2016 — session complémentaire ═════════════════

_add("bac-d-2016-sc-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = xe^x - e^x + x - 1$. Soit $(C)$ sa courbe représentative dans un repère orthonormal $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Calculer et interpréter $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to -\infty} \big(f(x) - (x - 1)\big)$.

b) En remarquant que $f(x) = (x - 1)(e^x + 1)$, calculer $\lim\limits_{x \to +\infty} f(x)$.

c) Déterminer et interpréter $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

**2. a)** Calculer $f'(x)$ et $f''(x)$, où $f'$ et $f''$ sont respectivement la dérivée et la dérivée seconde de $f$.

b) Calculer $f'(-1)$ et préciser son signe.

c) Étudier les variations de $f'$ et en déduire le signe de $f'(x)$.

**3.** Dresser le tableau de variation de $f$.

**4.** Déterminer les points d'intersection de $(C)$ avec les axes de coordonnées puis la construire.

**5. a)** Vérifier que pour tout $x \in \mathbb{R}$ on a : $f(x) = f'(x) - e^x + x - 2$. En déduire une primitive $F$ de $f$ sur $\mathbb{R}$.

b) Calculer l'aire $S$ du domaine plan délimité par la courbe $(C)$ et les axes de coordonnées.
""", ["Intégration et Primitives"])

_add("bac-d-2016-sc-math-ex4", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = x - 2 - \ln x$.

**1. a)** Calculer $\lim\limits_{x \to 0^+} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$.

b) Calculer et interpréter graphiquement $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et $\lim\limits_{x \to +\infty} \big(f(x) - x\big)$.

**2.** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

**3.** Donner une équation de la tangente $T$ à $(C)$ au point $A$ d'abscisse $x_0 = e$.

**4. a)** Montrer que l'équation $f(x) = 0$ admet exactement deux solutions $\alpha$ et $\beta$ ($\alpha < \beta$) et que $0{,}1 < \alpha < 0{,}2$ ; $3{,}1 < \beta < 3{,}2$. Démontrer que $\dfrac{e^\alpha}{e^\beta} = \dfrac{\alpha}{\beta}$.

b) En déduire le signe de $f(x)$ sur $]0;+\infty[$.

**5.** Soit $g$ la restriction de $f$ sur $I = [1;+\infty[$.

a) Montrer que $g$ réalise une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Calculer $\left(g^{-1}\right)'(e - 3)$ (on pourra utiliser la question 3).

**6.** Tracer $(C)$ et $(C')$, courbes respectives des fonctions $f$ et $g^{-1}$, dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**7. a)** En utilisant une intégration par parties, calculer $\displaystyle\int_1^e \ln x\,dx$.

b) Calculer l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$.
""", ["Intégration et Primitives"])

# ═══════════════════════════════════ 2017 — session normale ═══════════════════

_add("bac-d-2017-sn-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = e^{-x} + 2x - 2$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \big(f(x) - (2x - 2)\big)$. Interpréter graphiquement.

b) Calculer $\lim\limits_{x \to -\infty} f(x)$, $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

**2° a)** Calculer la dérivée $f'(x)$ et vérifier que $f'(-\ln 2) = 0$.

b) Étudier le signe de $f'(x)$ puis dresser le tableau de variation de $f$.

**3° a)** Montrer que l'équation $f(x) = 0$ admet exactement deux solutions $\alpha$ et $\beta$. Vérifier que $-1{,}7 < \alpha < -1{,}6$ et $0{,}7 < \beta < 0{,}8$.

b) Représenter la courbe $(C)$ de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**4°** On définit les suites $(u_n)$ et $(v_n)$ pour tout entier naturel $n$ par : $u_n = e^{-n}$ et $v_n = 2n - 2$.

a) Montrer que $(u_n)$ est une suite géométrique et qu'elle est décroissante.

b) Montrer que $(v_n)$ est une suite arithmétique et qu'elle est croissante.

c) Ces deux suites sont-elles adjacentes ? Justifier.

**5°** Pour tout entier naturel $n$, on pose $S_n = f(0) + f(1) + f(2) + \dots + f(n)$.

a) Exprimer $S_n$ en fonction de $n$.

b) Calculer $\lim\limits_{n \to +\infty} S_n$ et $\lim\limits_{n \to +\infty} \dfrac{S_n}{n^2}$.
""", ["Suites numériques"])

_add("bac-d-2017-sn-math-ex4", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction numérique définie sur $]0;+\infty[$ par $f(x) = (2 - 2x)(\ln x - 2)$ et $\Gamma$ sa courbe dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** On considère la fonction $g$ définie sur $]0;+\infty[$ par $g(x) = \dfrac{1}{x} + 1 - \ln x$.

a) Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer la dérivée $g'(x)$ puis dresser le tableau de variation de $g$.

c) Montrer que $g$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

d) Montrer que l'équation $g(x) = 0$ admet sur $]0;+\infty[$ une unique solution $\alpha$ telle que $3{,}5 < \alpha < 3{,}6$. En déduire le signe de $g(x)$ sur $]0;+\infty[$.

**2° a)** Calculer $\lim\limits_{x \to 0^+} f(x)$, $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

b) Calculer la dérivée $f'(x)$ et montrer que pour tout $x > 0$, $f'(x) = 2g(x)$.

c) Dresser le tableau de variation de $f$.

**3° a)** Montrer que $f(\alpha) = \dfrac{2(1 - \alpha)^2}{\alpha}$, où $\alpha$ est le réel trouvé dans la question 1° d).

b) Donner une équation de la tangente $T$ à la courbe $\Gamma$ au point $A$ d'abscisse $x_0 = 1$.

c) Montrer que $\Gamma$ coupe $(Ox)$ en un deuxième point $B$, autre que $A$, d'abscisse $x_B$ telle que $7{,}38 < x_B < 7{,}39$.

**4° a)** Construire $\Gamma$ et $T$ dans le repère $(O;\vec{i},\vec{j})$ (on prendra $\alpha = 1{,}8$ et $f(\alpha) = 2{,}7$).

b) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $(2 - 2x)\ln x = m$.

**5° a)** À l'aide d'une intégration par parties, montrer que $\displaystyle\int_1^2 (2 - 2x)\ln x\,dx = -\dfrac{1}{2}$.

b) En déduire l'aire du domaine plan délimité par la courbe $\Gamma$ de $f$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = 2$.
""", ["Intégration et Primitives"],
     note="Erreur du sujet original (question 4a) : « on prendra α = 1,8 et f(α) = 2,7 » contredit 1°d (3,5 < α < 3,6). "
          "Vérifié par calcul : α ≈ 3,591 et f(α) ≈ 3,74. Recopié tel quel ; la correction doit utiliser les vraies valeurs.")

# ══════════════════════════════ 2017 — session complémentaire ═════════════════

_add("bac-d-2017-sc-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (x + 2)(1 + e^{-x})$ et soit $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et que $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

b) Montrer que $f(x) = x + 2 + \dfrac{x}{e^x} + \dfrac{2}{e^x}$, puis calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \big(f(x) - (x + 2)\big)$.

c) En déduire que $\Gamma$ admet une asymptote oblique $D$ dont on donnera une équation.

d) Étudier la position relative entre $\Gamma$ et $D$.

**2° a)** Montrer que $f'(x) = 1 - (x + 1)e^{-x}$, où $f'$ est la dérivée première de $f$.

b) Étudier les variations de $f'$ et en déduire le signe de $f'(x)$.

c) Dresser le tableau de variation de $f$.

**3° a)** Déterminer le point $A$ de $\Gamma$ où la tangente $T$ à la courbe $\Gamma$ est parallèle à l'asymptote $D$. Donner une équation de $T$.

b) Déterminer les points d'intersection de $\Gamma$ avec les axes de coordonnées.

c) Tracer $D$, $T$ et $\Gamma$ dans le repère $(O;\vec{i},\vec{j})$.

**4° a)** Calculer l'intégrale $I = \displaystyle\int_{-2}^{0} 2e^{-x}\,dx$.

b) À l'aide d'une intégration par parties, calculer l'intégrale $J = \displaystyle\int_{-2}^{0} xe^{-x}\,dx$.

c) En déduire l'aire du domaine délimité par l'asymptote $D$, la courbe $\Gamma$ et les droites d'équations $x = -2$ et $x = 0$.

**5°** Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $x + 2 = (m - 2)e^x$.
""", ["Intégration et Primitives"])

_add("bac-d-2017-sc-math-ex4", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $D_f = ]0;1[ \cup ]1;+\infty[$ par $f(x) = \dfrac{2x - 1 + \ln x}{x - 1}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** On considère la fonction $u$ définie sur $]0;+\infty[$ par $u(x) = 1 + x\ln x$.

a) Calculer $\lim\limits_{x \to 0^+} u(x)$ et $\lim\limits_{x \to +\infty} u(x)$.

b) Calculer $u'(x)$, où $u'$ est la dérivée de $u$, puis dresser le tableau de variation de $u$.

c) Montrer que $\forall x > 0$ on a $u(x) \ge 1 - \dfrac{1}{e}$. En déduire le signe de $u(x)$.

**2° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = +\infty$ et interpréter graphiquement.

b) Calculer et interpréter les limites $\lim\limits_{x \to 1^-} f(x)$ et $\lim\limits_{x \to 1^+} f(x)$.

**3° a)** Montrer que $f(x)$ peut s'écrire sous la forme $f(x) = 2 + \dfrac{1}{x - 1} + \dfrac{\ln x}{x - 1}$.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et en déduire que la courbe $(C)$ admet une asymptote horizontale $(\Delta)$ dont on donnera une équation.

c) Étudier la position relative de $(C)$ et $(\Delta)$.

**4° a)** Calculer $f'(x)$ et vérifier que pour tout $x$ de $D_f$ on a : $f'(x) = \dfrac{-u(x)}{x(x - 1)^2}$.

b) Dresser le tableau de variation de $f$.

**5°** Soit $g$ la restriction de $f$ sur l'intervalle $]0;1[$.

a) Montrer que $g$ est une bijection de $]0;1[$ sur un intervalle $I$ que l'on précisera.

b) Dresser le tableau de variation de $g^{-1}$, où $g^{-1}$ est la réciproque de $g$.

**6° a)** Montrer que la courbe $(C)$ coupe $(Ox)$ en un unique point $A$ d'abscisse $\alpha$ avec $0{,}6 < \alpha < 0{,}8$.

b) Tracer $(\Delta)$, $(C)$ et $(C')$ dans le repère $(O;\vec{i},\vec{j})$, où $(C')$ est la courbe de $g^{-1}$.
""")

# ═══════════════════════════════════ 2018 — session normale ═══════════════════

_add("bac-d-2018-sn-math-ex4", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = \dfrac{2 + x + x\ln x}{x}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = +\infty$ et interpréter graphiquement.

b) Vérifier que $f(x) = \dfrac{2}{x} + 1 + \ln x$.

c) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$. Interpréter graphiquement.

**2° a)** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

b) Donner une équation de la tangente $T$ à la courbe $(C)$ au point d'abscisse $x_0 = 1$.

**3°** Soit $g$ la restriction de $f$ sur l'intervalle $I = ]0;2]$.

a) Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ que l'on précisera.

b) Dresser le tableau de variation de $g^{-1}$, où $g^{-1}$ est la fonction réciproque de $g$.

c) Calculer $\left(g^{-1}\right)'(3)$ (on pourra utiliser 2° b)).

d) Construire $(C)$, $(C')$ et $T$ dans le repère $(O;\vec{i},\vec{j})$, où $(C')$ est la courbe de $g^{-1}$.

**4°** On considère la fonction $h$ définie sur $]0;+\infty[$ par $h(x) = f(x) - x$.

a) Dresser le tableau de variation de $h$.

b) Montrer que l'équation $h(x) = 0$ admet une unique solution $\alpha$, telle que $2 < \alpha < 3$. Vérifier que $f(\alpha) = \alpha$ et en déduire que $\forall x \ge \alpha$ on a $f(x) - x \le 0$.

**5°** Soit $(u_n)$ la suite définie par $\begin{cases} u_0 = 3 \\ u_{n+1} = f(u_n), \ \forall n \in \mathbb{N} \end{cases}$

a) Montrer par récurrence que $u_n \ge \alpha$, $\forall n \in \mathbb{N}$.

b) Montrer que $(u_n)$ est décroissante (on pourra utiliser 4° b)). En déduire que $(u_n)$ est convergente.

**6° a)** Utiliser une intégration par parties pour calculer l'intégrale $K = \displaystyle\int_1^e \ln x\,dx$.

b) En déduire l'aire du domaine délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$.
""", ["Intégration et Primitives", "Suites numériques"])

_add("bac-d-2018-sn-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction numérique définie sur $\mathbb{R}$ par $f(x) = 2x - 1 + 2xe^{-x}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et que $\lim\limits_{x \to +\infty} f(x) = +\infty$.

b) Montrer que $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

c) Montrer que la droite $D$ d'équation $y = 2x - 1$ est une asymptote oblique à $(C)$ et étudier la position relative entre $(C)$ et $D$.

**2° a)** Calculer la dérivée $f'$ puis montrer que l'expression de la dérivée seconde de $f$ est $f''(x) = (2x - 4)e^{-x}$.

b) Montrer que la courbe $(C)$ admet un point d'inflexion $A$ dont on donnera les coordonnées.

c) Étudier les variations de $f'$ et en déduire que $f'$ est positive.

d) Dresser le tableau de variation de $f$.

**3° a)** Montrer que la courbe $(C)$ coupe $(Ox)$ en un unique point d'abscisse $\alpha$ avec $0{,}2 < \alpha < 0{,}3$.

b) Déterminer le point $B$ de $(C)$ où la tangente $T$ est parallèle à l'asymptote $D$. Donner une équation de $T$.

c) Tracer $D$, $T$ et $(C)$ dans le repère $(O;\vec{i},\vec{j})$.

d) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $-m - 1 + 2xe^{-x} = 0$.
""", ["Fonctions numériques (Limites et Continuité)"],
     note="Exercice rangé jusqu'ici dans « Fonctions numériques » ; c'est l'étude d'une fonction exponentielle : "
          "chapitre principal passé à « Fonctions Logarithmes et Exponentielles » (l'ancien chapitre est gardé en second).")

# ══════════════════════════════ 2018 — session complémentaire ═════════════════

_add("bac-d-2018-sc-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x + 2 - e^x$ et soit $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to +\infty} f(x) = -\infty$ et calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$. Interpréter graphiquement.

b) Calculer $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to -\infty} \big(f(x) - (x + 2)\big)$. En déduire que $\Gamma$ admet une asymptote oblique $D$ dont on donnera une équation.

c) Étudier la position relative entre $\Gamma$ et $D$.

**2° a)** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

b) Montrer que l'équation $f(x) = 0$ admet exactement deux solutions $\alpha$ et $\beta$ ($\alpha < \beta$) et que $-1{,}9 < \alpha < -1{,}8$ ; $1{,}1 < \beta < 1{,}2$.

c) Montrer que : $\alpha + f'(\alpha) = \beta + f'(\beta)$.

**3°** Soit $h$ la restriction de $f$ sur l'intervalle $I = ]-\infty;0]$.

a) Montrer que $h$ admet une réciproque, notée $h^{-1}$.

b) Dresser le tableau de variation de $h^{-1}$.

c) Montrer que $\left(h^{-1}\right)'(0) = \dfrac{-1}{1 + \alpha}$.

**4° a)** Déterminer le point $A$ de la courbe $\Gamma$ auquel la tangente $T$ est perpendiculaire à $D$. Donner une équation de $T$.

b) Tracer $D$, $T$, $\Gamma$ et $\Gamma'$ dans le repère $(O;\vec{i},\vec{j})$, où $\Gamma'$ est la courbe de $h^{-1}$ dans ce repère.
""")

_add("bac-d-2018-sc-math-ex4", r"""
**Exercice 4 (7 points)**

**Partie A**

On considère la fonction $g$ définie sur $]0;+\infty[$ par $g(x) = -x + 3 - 2\ln x$.

**1° a)** Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer $g'(x)$, où $g'$ est la dérivée de $g$, puis dresser le tableau de variation de $g$.

**2° a)** Montrer que $g$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $g(x) = 0$ admet une unique solution $\lambda$ et que $1{,}8 \le \lambda \le 1{,}9$.

c) En déduire le signe de $g$ sur l'intervalle $]0;+\infty[$.

**Partie B**

Soit $f$ la fonction définie sur $I = ]0;+\infty[$ par $f(x) = \dfrac{x - 1 + \ln x}{x^2}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = -\infty$ et interpréter graphiquement.

b) Montrer que $\lim\limits_{x \to +\infty} f(x) = 0$ et interpréter graphiquement.

**2° a)** Calculer $f'(x)$ et vérifier que pour tout $x$ de $I$ on a : $f'(x) = \dfrac{g(x)}{x^3}$.

b) Montrer que $f(\lambda) = \dfrac{\lambda + 1}{2\lambda^2}$ et donner une valeur approchée de $f(\lambda)$ à $10^{-1}$ près.

c) Dresser le tableau de variation de $f$.

**3° a)** Donner une équation de la tangente $T$ à $(C)$ au point d'abscisse $x_0 = 1$.

b) Tracer $(C)$ et $T$ dans le repère $(O;\vec{i},\vec{j})$.

c) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $\ln x = 1 - x + 2x^3 + mx^2$.

**4° a)** À l'aide d'une intégration par parties, calculer l'intégrale $J = \displaystyle\int_1^e \dfrac{\ln x}{x^2}\,dx$.

b) En déduire l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$.
""", ["Intégration et Primitives"])

# ═══════════════════════════════════ 2019 — session normale ═══════════════════

_add("bac-d-2019-sn-math-ex4", r"""
**Exercice 4 (6 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = (x - 1)(1 - \ln x)$ et $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** On considère la fonction $g$ définie sur l'intervalle $]0;+\infty[$ par $g(x) = \dfrac{1}{x} - \ln x$.

a) Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer la dérivée $g'(x)$ puis dresser le tableau de variation de $g$.

c) Montrer que l'équation $g(x) = 0$ admet sur $]0;+\infty[$ une unique solution $\alpha$ telle que $1{,}7 < \alpha < 1{,}8$.

d) En déduire le signe de $g(x)$ sur $]0;+\infty[$.

**2° a)** Calculer $\lim\limits_{x \to 0^+} f(x)$, $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

b) Montrer que pour tout $x > 0$, $f'(x) = g(x)$, où $f'$ est la dérivée de $f$.

c) Dresser le tableau de variation de $f$.

**3° a)** Montrer que $f(\alpha) = \dfrac{(\alpha - 1)^2}{\alpha}$, où $\alpha$ est le réel trouvé dans la question 1° c).

b) Déterminer les points d'intersection de la courbe $\Gamma$ avec l'axe $(Ox)$.

**4°** Soit $h$ la restriction de $f$ sur l'intervalle $I = [\alpha;+\infty[$.

a) Montrer que $h$ réalise une bijection de l'intervalle $I$ sur l'intervalle $J = ]-\infty;f(\alpha)]$.

b) Calculer $\left(h^{-1}\right)'(0)$.

c) Construire $\Gamma$ et $\Gamma'$ dans le repère $(O;\vec{i},\vec{j})$, où $\Gamma'$ est la courbe de $h^{-1}$.

**5° a)** À l'aide d'une intégration par parties, montrer que $\displaystyle\int_1^e (x - 1)\ln x\,dx = \dfrac{e^2 - 3}{4}$.

b) En déduire l'aire du domaine plan délimité par la courbe $\Gamma$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = e$.
""", ["Intégration et Primitives"])

# ══════════════════════════════ 2019 — session complémentaire ═════════════════

_add("bac-d-2019-sc-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $[-1;+\infty[$ par $f(-1) = 0$ et $\forall x > -1$, $f(x) = (x + 1)^2\ln(x + 1) - (x + 1)$. On note $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Vérifier que $\forall x > -1$, $f(x) = (x + 1)\big[(x + 1)\ln(x + 1) - 1\big]$.

b) Montrer que $\lim\limits_{x \to -1^+} f(x) = 0$ et $\lim\limits_{x \to -1^+} \dfrac{f(x)}{x + 1} = -1$ (on donne la limite suivante : $\lim\limits_{x \to -1^+} (x + 1)\ln(x + 1) = 0$).

c) En déduire que $f$ est continue et dérivable à droite de $-1$.

d) Calculer $\lim\limits_{x \to +\infty} f(x)$ et vérifier que $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

**2° a)** Montrer que $\forall x > -1$, $f'(x) = 2(x + 1)\ln(x + 1) + x$ ($f'$ étant la dérivée de $f$).

b) En remarquant que $\forall x > -1$, le signe de $2(x + 1)\ln(x + 1)$ est celui de $x$, montrer que $f'$ est négative sur $]-1;0[$ et positive sur $]0;+\infty[$.

c) Dresser le tableau de variation de $f$.

**3°** Soit $g$ la restriction de $f$ sur l'intervalle $[0;+\infty[$.

a) Montrer que $g$ réalise une bijection de $[0;+\infty[$ sur un intervalle $J$ à déterminer.

b) Montrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$, avec $0{,}7 \le \alpha \le 0{,}8$.

c) Justifier que $g'(\alpha) = \alpha + 2$ et en déduire la valeur de $\left(g^{-1}\right)'(0)$, où $g^{-1}$ est la réciproque de $g$.

**4°** Tracer dans le même repère les courbes $(C)$ et $(C')$ ($(C')$ étant la courbe de $g^{-1}$).
""", note="Scan de mauvaise qualité (taches) : énoncé reconstitué et contrôlé par calcul (factorisation, f', α ≈ 0,763, g'(α) = α + 2).")

_add("bac-d-2019-sc-math-ex4", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (2x - 2)(1 + e^x)$ et soit $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to +\infty} f(x) = +\infty$ et que $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

b) Calculer $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to -\infty} \big(f(x) - (2x - 2)\big)$.

c) En déduire que la droite $D$ d'équation $y = 2x - 2$ est une asymptote oblique pour $\Gamma$. Étudier la position relative entre $\Gamma$ et $D$.

**2° a)** Calculer $f'(x)$ et justifier que $f''(x) = (2x + 2)e^x$.

b) Étudier les variations de $f'$ et en déduire que $\forall x \in \mathbb{R}$, $f'(x) > 0$.

c) Dresser le tableau de variation de $f$.

**3° a)** Déterminer le point d'intersection de $\Gamma$ avec $(Ox)$.

b) Écrire une équation de la tangente $T$ au point d'abscisse $0$ de $\Gamma$.

c) Tracer $D$, $T$ et $\Gamma$ dans le repère $(O;\vec{i},\vec{j})$.

d) Discuter graphiquement, selon les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $(2x - 2)e^x = 2 + m$.

**4° a)** Calculer, à l'aide d'une intégration par parties, l'intégrale $I = \displaystyle\int_0^1 (2x - 2)e^x\,dx$.

b) En déduire l'aire $A$ de la partie du plan délimitée par $\Gamma$, l'axe $(Ox)$ et les droites d'équations $x = 0$ et $x = 1$.
""", ["Intégration et Primitives"], note="Scan de mauvaise qualité : énoncé reconstitué et contrôlé par calcul (f'' et I = 4 − 2e).")

# ═══════════════════════════════════ 2020 — session normale ═══════════════════

_add("bac-d-2020-sn-math-ex3", r"""
**Exercice 3 (4 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x - 2 + e^{-x}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Justifier que $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \big(f(x) - (x - 2)\big) = 0$.

b) En déduire que la droite $(\Delta)$ d'équation $y = x - 2$ est asymptote à la courbe $(C)$ puis étudier leur position relative.

**2° a)** Montrer que $f(x) = \dfrac{xe^x - 2e^x + 1}{e^x}$ et que $\dfrac{f(x)}{x} = 1 - \dfrac{2}{x} + \dfrac{1}{xe^x}$.

b) En déduire que $\lim\limits_{x \to -\infty} f(x) = +\infty$ et que $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = -\infty$. Interpréter graphiquement.

**3°** Justifier que $f'(x) = 1 - e^{-x}$ et dresser le tableau de variation de $f$.

**4° a)** Montrer que l'équation $f(x) = 0$ admet deux solutions $\alpha$ et $\beta$ avec $\beta < \alpha$ puis vérifier que $1{,}8 < \alpha < 1{,}9$.

b) Justifier que $f'(\alpha) = \alpha - 1$.

**5°** Construire la courbe $(C)$ et son asymptote $(\Delta)$ dans le repère $(O;\vec{i},\vec{j})$.
""")

_add("bac-d-2020-sn-math-ex4", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $[0;+\infty[$ par : $\begin{cases} f(x) = x - x\ln x, & \forall x > 0 \\ f(0) = 0 \end{cases}$ et soit $(\Gamma)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Calculer $\lim\limits_{x \to 0^+} f(x)$ et en déduire que $f$ est continue en $0^+$.

b) Calculer $\lim\limits_{x \to 0^+} \dfrac{f(x) - f(0)}{x - 0}$ et interpréter graphiquement.

c) Montrer que $\lim\limits_{x \to +\infty} f(x) = -\infty$ et que $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = -\infty$ puis interpréter graphiquement.

**2°** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

**3° a)** Déterminer les points d'intersection de la courbe $(\Gamma)$ avec l'axe des abscisses.

b) Donner une équation de la tangente $(T)$ à $(\Gamma)$ au point d'abscisse $e$.

**4°** Soit $g$ la restriction de $f$ sur l'intervalle $I = [1;+\infty[$.

a) Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que $\left(g^{-1}\right)'(0) = -1$, où $g^{-1}$ est la réciproque de $g$.

c) Construire $(T)$, $(\Gamma)$ et $(\Gamma')$ dans le repère $(O;\vec{i},\vec{j})$, $(\Gamma')$ étant la courbe représentative de $g^{-1}$.

d) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $2x - x\ln x = m$.

**5° a)** Utiliser une intégration par parties pour calculer l'intégrale $A = \displaystyle\int_1^e x\ln x\,dx$.

b) En déduire l'aire du domaine plan délimité par la courbe $(\Gamma)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$.
""", ["Intégration et Primitives"])

# ══════════════════════════════ 2020 — session complémentaire ═════════════════

_add("bac-d-2020-sc-math-ex3", r"""
**Exercice 3 (4 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = -3x + 2 + e^x$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Calculer $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to -\infty} \big(f(x) - (-3x + 2)\big)$. Interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ puis interpréter graphiquement.

**2° a)** Calculer la dérivée $f'(x)$.

b) Calculer $f'(\ln 3)$ et en déduire le signe de $f'(x)$.

c) Dresser le tableau de variation de $f$.

**3°** On considère les suites $(u_n)$ et $(v_n)$ définies sur $\mathbb{N}$ par : $u_n = 6n - 2$ et $v_n = e^{2n}$.

a) Exprimer $f(2n)$ en fonction de $u_n$ et $v_n$ pour $n \in \mathbb{N}$.

b) Montrer que $(u_n)$ est une suite arithmétique puis calculer sa limite.

c) Déterminer la nature de $(v_n)$ et étudier sa monotonie.

d) Calculer la somme $S = f(0) + f(2) + f(4) + \dots + f(2020)$.
""", ["Suites numériques"])

_add("bac-d-2020-sc-math-ex4", r"""
**Exercice 4 (7 points)**

On considère la fonction numérique $f$ définie sur $]0;2[ \cup ]2;+\infty[$ par $f(x) = \dfrac{\ln x}{(x - 2)^2}$, et on note $(\Gamma)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** Soit $g(x) = x - 2 - 2x\ln x$.

a) Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer $g'(x)$ et vérifier que $g'\left(\dfrac{1}{\sqrt{e}}\right) = 0$.

c) Montrer que $g\left(\dfrac{1}{\sqrt{e}}\right) = \dfrac{2}{\sqrt{e}} - 2$ et dresser le tableau de variation de $g$.

d) En déduire le signe de $g(x)$.

**2° a)** Calculer les limites de $f$ aux bornes de son domaine de définition $D_f$.

b) Justifier que la courbe $(\Gamma)$ admet trois asymptotes que l'on déterminera.

**3° a)** Calculer la dérivée $f'$ de $f$ et vérifier que $\forall x \in D_f$, $f'(x) = \dfrac{g(x)}{x(x - 2)^3}$.

b) Vérifier que $f'$ est positive sur $]0;2[$ et négative sur $]2;+\infty[$ puis dresser le tableau de variation de $f$.

**4° a)** Écrire l'équation réduite de la tangente $T$ à $(\Gamma)$ au point $A$ d'abscisse $1$.

b) Tracer la courbe $(\Gamma)$, la tangente $T$ et les asymptotes.

**5°** Soit $S$ l'aire, en unité d'aire, du domaine délimité par la courbe $(\Gamma)$, l'axe des abscisses et les droites d'équations respectives $x = 3$ et $x = 4$.

a) Vérifier que $S = \displaystyle\int_3^4 f(x)\,dx$.

b) En remarquant que $\forall x \in D_f$, $f(x) = \dfrac{1}{(x - 2)^2}\ln x$ et en utilisant une intégration par parties, montrer que $S = \left[\dfrac{-\ln x}{x - 2}\right]_3^4 + \displaystyle\int_3^4 \dfrac{1}{x(x - 2)}\,dx$.

c) Montrer que $\forall x \in D_f$, $\dfrac{1}{x(x - 2)} = \dfrac{1}{2}\left(\dfrac{1}{x - 2} - \dfrac{1}{x}\right)$ puis vérifier que $\displaystyle\int_3^4 \dfrac{1}{x(x - 2)}\,dx = \dfrac{1}{2}\ln\dfrac{3}{2}$.

d) En déduire la valeur de $S$.
""", ["Intégration et Primitives"])

# ═══════════════════════════════════ 2021 — session normale ═══════════════════

_add("bac-d-2021-sn-math-ex3", r"""
**Exercice 3 (5,5 points)**

Soit $f$ la fonction numérique définie sur $\mathbb{R}$ par $f(x) = 1 + (x + 2)e^{-x}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$, d'unité graphique 1 cm.

**1° a)** Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ puis calculer et interpréter graphiquement $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x}$.

b) Justifier que $f(x) = 1 + \dfrac{x}{e^x} + \dfrac{2}{e^x}$ puis calculer et interpréter graphiquement $\lim\limits_{x \to +\infty} f(x)$.

**2°** Calculer $f'(x)$, où $f'$ est la fonction dérivée de $f$. Dresser le tableau de variation de $f$.

**3°** Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$. Justifier que $-2{,}2 < \alpha < -2$.

**4° a)** Montrer que $I(0;3)$ est un point d'inflexion pour la courbe $(C)$. Écrire une équation de la tangente $T$ à $(C)$ en ce point.

b) Construire la courbe $(C)$ et sa tangente $T$ dans le repère $(O;\vec{i},\vec{j})$.

**5°** Soit $S$ l'aire, en cm², de la partie du plan fermée par la courbe $(C)$ et les axes de coordonnées.

a) Montrer que $S = \displaystyle\int_\alpha^0 f(x)\,dx$.

b) Vérifier que $\forall x \in \mathbb{R}$, $f(x) = 1 + h'(x)$, où $h(x) = -(x + 3)e^{-x}$. En déduire une primitive de $f$ sur $\mathbb{R}$.

c) Justifier que $e^{-\alpha} = \dfrac{-1}{\alpha + 2}$ et en déduire que $S = \dfrac{-(\alpha + 3)^2}{\alpha + 2}$.
""", ["Fonctions numériques (Limites et Continuité)", "Intégration et Primitives"],
     note="Exercice rangé jusqu'ici dans « Fonctions numériques » ; c'est l'étude d'une fonction exponentielle : "
          "chapitre principal passé à « Fonctions Logarithmes et Exponentielles » (les anciens chapitres sont gardés en second).")

_add("bac-d-2021-sn-math-ex4", r"""
**Exercice 4 (6,5 points)**

Soit $f$ la fonction définie sur l'intervalle $I = ]0;+\infty[$ par $f(x) = x - 2 + 2\left(\dfrac{\ln x}{x}\right)$, et soit $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** On considère la fonction $g$ définie sur $I$ par $g(x) = x^2 + 2 - 2\ln x$.

a) Calculer $g'(x)$ pour tout $x \in I$ et étudier son signe sur cet intervalle.

b) Calculer $g(1)$, puis en déduire que $g$ est positive sur $I$.

**2° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$. Interpréter graphiquement.

b) Montrer que la droite $\Delta$ d'équation $y = x - 2$ est asymptote à $\Gamma$ et étudier leur position relative.

**3° a)** Montrer que $\forall x > 0$, $f'(x) = \dfrac{g(x)}{x^2}$ ($g$ étant la fonction définie en 1°).

b) En déduire le signe de $f'$ puis dresser le tableau de variation de la fonction $f$.

c) Montrer que la courbe $\Gamma$ coupe l'axe des abscisses en un seul point $A$ d'abscisse $\beta$. Vérifier que $1{,}47 < \beta < 1{,}48$.

**4° a)** Déterminer une équation de la tangente $T$ à $\Gamma$ au point d'abscisse $e$.

b) Construire la courbe $\Gamma$, l'asymptote $\Delta$ ainsi que la tangente $T$ dans le même repère $(O;\vec{i},\vec{j})$.

c) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $(m + 2)x = 2\ln x$.

**5° a)** Montrer que $f$ réalise une bijection de $I$ dans un intervalle $J$ à déterminer.

b) Vérifier que $f^{-1}(-1) = 1$ et calculer $\left(f^{-1}\right)'(-1)$, où $f^{-1}$ est la réciproque de $f$.

c) Construire la courbe $(\Gamma')$ de $f^{-1}$ dans le même repère $(O;\vec{i},\vec{j})$.
""")

# ══════════════════════════════ 2021 — session complémentaire ═════════════════

_add("bac-d-2021-sc-math-ex3", r"""
**Exercice 3 (6 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = \dfrac{4x^2 + 1 + 2\ln x}{2x^2}$ et $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = -\infty$ puis interpréter graphiquement le résultat.

b) Montrer que $\lim\limits_{x \to +\infty} f(x) = 2$ et déduire que la courbe $(C)$ admet une asymptote $(D)$ à préciser.

**2° a)** Montrer que $f'(x) = \dfrac{-2\ln x}{x^3}$.

b) Dresser le tableau de variation de $f$.

**3°** Soit $g$ la restriction de $f$ sur l'intervalle $I = [1;+\infty[$.

a) Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Dresser le tableau de variation de $g^{-1}$.

**4° a)** Montrer que l'équation $f(x) = 0$ admet une unique solution $x_0$ et que $0{,}4 < x_0 < 0{,}5$.

b) Construire $(D)$, $(C)$ et $(C')$, $(C')$ étant la courbe représentative de $g^{-1}$.

**5° a)** Utiliser une intégration par parties pour calculer $I = \displaystyle\int_1^e \dfrac{\ln x}{x^2}\,dx$.

b) En déduire l'aire $A$ du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = e$.
""", ["Intégration et Primitives"],
     note="Retouches mineures : en 4a le sujet écrit « admet, dans ℝ, une unique solution » (f n'est définie que sur ]0 ; +∞[) "
          "et en 5b « la courbe Γ » pour (C).")

_add("bac-d-2021-sc-math-ex4", r"""
**Exercice 4 (6 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (2x - 4)(e^x - 1)$. On note $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** Soit $h$ la fonction définie sur $\mathbb{R}$ par $h(x) = (2x - 2)e^x - 2$.

a) Montrer que $\lim\limits_{x \to -\infty} h(x) = -2$ et $\lim\limits_{x \to +\infty} h(x) = +\infty$.

b) Calculer $h'(x)$ puis dresser le tableau de variation de $h$.

c) Montrer que l'équation $h(x) = 0$ admet dans $\mathbb{R}$ une unique solution $\alpha$ et justifier que $1{,}2 < \alpha < 1{,}3$.

d) Déterminer le signe de $h$ sur $\mathbb{R}$.

**2° a)** Calculer $\lim\limits_{x \to +\infty} f(x)$ et vérifier que $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

b) Montrer que $\lim\limits_{x \to -\infty} f(x) = +\infty$ et que la droite $(\Delta)$ d'équation $y = -2x + 4$ est une asymptote à $\Gamma$. Étudier la position relative entre $(\Delta)$ et $\Gamma$.

**3° a)** Montrer que $f'(x) = h(x)$, $\forall x \in \mathbb{R}$.

b) Dresser le tableau de variation de $f$.

c) Vérifier que $f(\alpha) = -\dfrac{2(\alpha - 2)^2}{\alpha - 1}$.

**4° a)** Déterminer les points d'intersection de $\Gamma$ avec les axes de coordonnées.

b) Construire $(\Delta)$ et $\Gamma$ dans le repère $(O;\vec{i},\vec{j})$ (on prendra $\alpha = 1{,}3$).
""", note="En 4b le sujet écrit « Construire (D) » : il s'agit de l'asymptote (Δ).")

# ═══════════════════ Exercices d'autres chapitres qui étudient une fonction exp ═══════
ED = "Équations différentielles"
FN = "Fonctions numériques (Limites et Continuité)"
IP = "Intégration et Primitives"

_add("bac-d-2019-sn-math-ex3", r"""
**Exercice 3 (6 points)**

**A. 1°** Déterminer la solution générale de l'équation différentielle $(E) : y'' - 4y' + 4y = 0$.

**2°** Soit $h$ la solution de $(E)$ qui vérifie $h(0) = -1$ et $h'(0) = -1$. Montrer que $h(x) = (x - 1)e^{2x}$.

**B.** On considère la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = h(x) + 2x - 2 = (x - 1)(2 + e^{2x})$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ ; $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

b) Montrer que la droite $D$ d'équation $y = 2x - 2$ est asymptote à $(C)$ et étudier leurs positions relatives.

**2° a)** Montrer que $f'(x) = 2 + (2x - 1)e^{2x}$ et en déduire l'expression de $f''(x)$ ($f'$ et $f''$ étant respectivement la dérivée première et la dérivée seconde de $f$).

b) Montrer que le point $A(0;-3)$ est un point d'inflexion pour la courbe $(C)$.

c) Étudier les variations de $f'$ et en déduire qu'elle est strictement positive sur $\mathbb{R}$.

d) Dresser le tableau de variation de $f$.

**3° a)** Déterminer le point $B$ de $(C)$ où la tangente $T$ est parallèle à la droite $D$. Écrire une équation de $T$.

b) Tracer $D$, $T$ et $(C)$ dans le repère $(O;\vec{i},\vec{j})$.

c) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $x - 1 = me^{-2x}$.
""", [CH, FN], chapitre=ED,
     note="Chapitre principal inchangé (Équations différentielles) ; la partie B est une étude de fonction exponentielle : "
          "« Fonctions Logarithmes et Exponentielles » ajouté en second.")

_add("bac-d-2022-sn-math-ex4", r"""
**Exercice 4 (4 points)**

**I. 1°** Déterminer la solution générale de l'équation différentielle $(E) : y'' + 2y' + y = 0$.

**2°** Déterminer la solution $h$ de l'équation $(E)$ qui vérifie $h(0) = -1$ et $h(-1) = 0$.

**II.** Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = -(x + 1)e^{-x} - 1$. On note $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Calculer $\lim\limits_{x \to -\infty} f(x)$ et vérifier que $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = -\infty$. Interpréter graphiquement.

b) Montrer que la droite $(\Delta)$ d'équation $y = -1$ est une asymptote horizontale à $\Gamma$ et étudier leur position relative.

**2° a)** Montrer que $\forall x \in \mathbb{R}$, $f'(x) = xe^{-x}$ puis en déduire son signe sur $\mathbb{R}$.

b) Dresser le tableau de variations de $f$.

**3° a)** Montrer que la courbe $\Gamma$ coupe $(Ox)$ en un unique point d'abscisse $\alpha$ avec $-1{,}3 < \alpha < -1{,}2$.

b) Montrer que la courbe $\Gamma$ admet un point d'inflexion $A$ et préciser ses coordonnées.

c) Construire $(\Delta)$ et $\Gamma$ dans le repère précédent.
""", [CH, FN], chapitre=ED,
     note="Chapitre principal inchangé (Équations différentielles) ; la partie II est une étude de fonction exponentielle : "
          "« Fonctions Logarithmes et Exponentielles » ajouté en second.")

_add("bac-d-2023-sn-math-ex3", r"""
**Exercice 3 (4 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (x^2 - x - 1)e^{-x} + 1$. On note $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to -\infty} f(x) = +\infty$ et que $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = -\infty$. Interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$. En déduire que $\Gamma$ admet en $+\infty$ une asymptote $(\Delta)$ à préciser.

c) Déterminer le signe de $(x^2 - x - 1)$ sur $\mathbb{R}$. En déduire la position relative de $(\Delta)$ et $\Gamma$.

**2° a)** Montrer que $\forall x \in \mathbb{R}$, $f'(x) = x(3 - x)e^{-x}$ puis dresser le tableau de variations de $f$.

b) Construire $(\Delta)$ et $\Gamma$ dans le repère précédent.

**3° a)** Montrer que la fonction $f$ vérifie l'équation différentielle $E : y'' + 2y' + y = 2e^{-x} + 1$.

b) En déduire une primitive de $f$ puis calculer l'aire $A$ du domaine délimité par la courbe $\Gamma$, l'asymptote $(\Delta)$ et les droites d'équations $x = 0$ et $x = 1$.
""", [FN, ED, IP],
     note="Exercice rangé jusqu'ici dans « Fonctions numériques » ; c'est l'étude d'une fonction exponentielle : "
          "chapitre principal passé à « Fonctions Logarithmes et Exponentielles » (les anciens chapitres sont gardés en second).")

# ═══════════════════════════════════ 2022 — session normale ═══════════════════

_add("bac-d-2022-sn-math-ex5", r"""
**Exercice 5 (6 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = x^2(2\ln x - 1) + 1$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = 1$ puis interpréter le résultat.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$, puis interpréter graphiquement ce résultat.

**2° a)** Montrer que $f'(x) = 4x\ln x$.

b) Dresser le tableau de variation de $f$.

**3°** Soit $g$ la restriction de $f$ sur l'intervalle $I = [1;+\infty[$.

a) Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ à déterminer.

b) Dresser le tableau de variation de $g^{-1}$.

**4°** Construire $(C)$ et $(C')$ dans le repère $(O;\vec{i},\vec{j})$ ($(C')$ étant la courbe de $g^{-1}$).

**5° a)** Utiliser une intégration par parties pour calculer l'intégrale $K = \displaystyle\int_1^e x^2\ln x\,dx$.

b) En déduire l'aire $A$ du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = e$.
""", [IP])

# ══════════════════════════════ 2022 — session complémentaire ═════════════════

_add("bac-d-2022-sc-math-ex3", r"""
**Exercice 3 (6 points)**

On considère la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = (x - 1)e^x + x$. On note $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1°** Soit $h$ la fonction définie sur $\mathbb{R}$ par $h(x) = xe^x + 1$.

a) Montrer que $\lim\limits_{x \to -\infty} h(x) = 1$ et que $\lim\limits_{x \to +\infty} h(x) = +\infty$.

b) Calculer $h'(x)$ puis dresser le tableau de variation de $h$.

c) Montrer que $h(x)$ est positive pour tout réel $x$.

**2. a)** Calculer $\lim\limits_{x \to +\infty} f(x)$ et vérifier que $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$. Interpréter graphiquement.

b) Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et que la droite $(\Delta)$ d'équation $y = x$ est une asymptote oblique à $\Gamma$.

c) Étudier la position relative entre $(\Delta)$ et $\Gamma$.

**3. a)** Montrer que $f'(x) = h(x)$, $\forall x \in \mathbb{R}$.

b) Dresser le tableau de variation de $f$.

c) Construire $(\Delta)$ et $\Gamma$ dans le repère $(O;\vec{i},\vec{j})$.
""")

_add("bac-d-2022-sc-math-ex4", r"""
**Exercice 4 (6 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = \dfrac{x + 1 + \ln x}{x}$, et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = -\infty$ puis interpréter graphiquement le résultat.

b) Montrer que $\lim\limits_{x \to +\infty} f(x) = 1$ et déduire que la courbe $(C)$ admet une asymptote $(D)$ à préciser.

**2. a)** Montrer que $f'(x) = -\dfrac{\ln x}{x^2}$.

b) Dresser le tableau de variation de $f$.

c) Montrer que l'équation $f(x) = 0$ admet, dans $]0;+\infty[$, une unique solution $x_0$ et que $0{,}27 < x_0 < 0{,}28$.

**3°** Soit $g$ la restriction de $f$ sur l'intervalle $I = ]0;1]$.

a) Montrer que $g$ est une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Dresser le tableau de variation de $g^{-1}$.

**4. a)** Construire $(D)$, $(C)$ et $(C')$, où $(C')$ est la courbe représentative de $g^{-1}$.

b) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $E_m : (m - 1)x = 1 + \ln x$.

**5. a)** Montrer que $\displaystyle\int_1^e \dfrac{\ln x}{x}\,dx = \dfrac{1}{2}$.

b) En déduire l'aire $A$ du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = e$.
""", [IP])

# ═══════════════════════════════════ 2023 — session normale ═══════════════════

_add("bac-d-2023-sn-math-ex5", r"""
**Exercice 5 (5 points)**

**I.** Soit $g$ la fonction définie sur $]0;+\infty[$ par $g(x) = x^2 - 4 + 3\ln x$.

**1° a)** Justifier que $\lim\limits_{x \to 0^+} g(x) = -\infty$ et $\lim\limits_{x \to +\infty} g(x) = +\infty$.

b) Calculer la dérivée $g'(x)$ et dresser le tableau de variations de $g$.

**2° a)** Montrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$ et que $1{,}6 < \alpha < 1{,}7$.

b) En déduire le signe de $g(x)$ sur $]0;+\infty[$.

**II.** On considère la fonction $f$ définie sur $]0;+\infty[$ par $f(x) = x - 2 + \dfrac{1 - 3\ln x}{x}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1° a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = +\infty$ puis interpréter le résultat.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \big(f(x) - x + 2\big)$. En déduire que $(C)$ admet une asymptote oblique $(D)$ en $+\infty$.

c) Étudier la position relative de $(C)$ et $(D)$.

**2° a)** Montrer que $f'(x) = \dfrac{g(x)}{x^2}$ où $g$ est la fonction définie dans la partie I.

b) Vérifier que $f(\alpha) = \dfrac{2\alpha^2 - 2\alpha - 3}{\alpha}$ puis dresser le tableau de variation de $f$.

**3°** Soit $h$ la restriction de $f$ sur l'intervalle $I = ]0;\alpha]$.

a) Montrer que $h$ est une bijection de $I$ sur un intervalle $J$ à déterminer.

b) Dresser le tableau de variation de la réciproque $h^{-1}$ de $h$.

**4°** Construire $(C)$, $(C')$ et $(D)$ dans le repère $(O;\vec{i},\vec{j})$ ($(C')$ étant la courbe de $h^{-1}$).
""")

# ═══════════════════════════════════ 2024 — session normale ═══════════════════

_add("bac-d-2024-sn-math-ex3", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x - 3 + \dfrac{1}{2}e^x$. On note $\Gamma$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Justifier que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

b) Calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

c) Calculer $\lim\limits_{x \to -\infty} \big(f(x) - (x - 3)\big)$ et en déduire que la droite $D$ d'équation $y = x - 3$ est une asymptote oblique à $\Gamma$. Déterminer la position relative de $D$ et $\Gamma$.

**2)** Calculer $f'(x)$, $\forall x \in \mathbb{R}$, et dresser le tableau de variations de $f$.

**3. a)** Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$ dans $\mathbb{R}$ et que $1{,}2 < \alpha < 1{,}3$.

b) Construire $D$ et $\Gamma$ dans le repère précédent.
""")

_add("bac-d-2024-sn-math-ex5", r"""
**Exercice 5 (5 points)**

**I.** Soit $u$ la fonction définie sur $]0;+\infty[$ par $u(x) = 2x - 1 - \ln x$.

**1.** Étudier les variations de $u$.

**2.** En déduire que $u(x)$ est positive sur $]0;+\infty[$.

**II.** On considère la fonction $g$ définie sur $[0;+\infty[$ par : $\begin{cases} g(x) = x^2 - 2 - x\ln x, & \text{si } x > 0 \\ g(0) = -2 \end{cases}$ et soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Calculer $\lim\limits_{x \to 0^+} g(x)$. En déduire que $g$ est continue à droite de $x_0 = 0$.

b) Montrer que $\lim\limits_{x \to 0^+} \dfrac{g(x) - g(0)}{x} = +\infty$ et interpréter graphiquement.

c) Calculer $\lim\limits_{x \to +\infty} g(x)$ et $\lim\limits_{x \to +\infty} \dfrac{g(x)}{x}$ et interpréter graphiquement.

**2. a)** Montrer que $g'(x) = u(x)$, $\forall x \in\, ]0;+\infty[$, où $u$ est la fonction définie dans la partie I. Dresser le tableau de variation de $g$.

b) Déterminer une équation de la tangente $(T)$ à $(C)$ au point d'abscisse $x_0 = 1$.

c) Montrer que la courbe $(C)$ coupe l'axe $(Ox)$ en un seul point $A$ dont l'abscisse $\alpha$ est telle que $1{,}7 < \alpha < 1{,}8$.

d) Vérifier que la courbe $(C)$ admet un point d'inflexion $B$ et déterminer ses coordonnées.

**3.** Construire la courbe $(C)$ et la tangente $(T)$ dans le repère $(O;\vec{i},\vec{j})$.
""", note="Retouche : en II.1c le sujet écrit « Calculer lim g(x) = +∞ et lim g(x)/x = +∞ » (valeurs données dans "
          "la consigne) ; reformulé en « Calculer lim g(x) et lim g(x)/x ».")
