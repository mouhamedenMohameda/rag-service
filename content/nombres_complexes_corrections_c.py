"""Nombres complexes — série C, 2015-2025 : énoncés vérifiés + corrections.

Énoncés retranscrits depuis les sujets originaux (PDF texte décodé, ou scan
lu à l'image pour 2016 SC, 2019 SC, 2023 SC/SN, 2024 SC, 2025 SN), en
remplacement du texte OCR. Toutes les valeurs numériques ont été vérifiées
par calcul formel (sympy).

Chargé par ``scripts/load_chapter_content.py nombres_complexes --corrections
nombres_complexes_corrections_c`` : un exercice déjà validé par l'admin n'est
jamais modifié ; l'énoncé OCR remplacé est conservé dans ``ennonce_ocr``.
"""

CORRECTIONS = {
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2015-sc-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1)** On pose $P(z) = z^3 - (6+5i)z^2 + (1+20i)z + 14 - 5i$ où $z$ est un nombre complexe.

a) Calculer $P(i)$ et déterminer les nombres $a$ et $b$ tels que pour tout $z$ de $\mathbb{C}$ : $P(z) = (z - i)(z^2 + az + b)$.

b) Résoudre, dans l'ensemble des nombres complexes, l'équation $P(z) = 0$.

**2)** On considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = i$, $z_B = 4 + i$ et $z_C = 2 + 3i$. Soit $s$ la similitude directe de centre $A$ qui transforme $B$ en $C$.

a) Donner l'expression complexe de $s$.

b) Déterminer le rapport et un angle de $s$.

**3) a)** Déterminer puis construire les ensembles $\Gamma_1$ et $\Gamma_2$ des points $M$ du plan d'affixe $z$ définis par :

$M \in \Gamma_1 \iff \dfrac{z - i}{z - 4 - i}$ est imaginaire pur ;

$M \in \Gamma_2 \iff \dfrac{z - i}{z - 2 - 3i}$ est imaginaire pur.

b) Justifier que $s(\Gamma_1) = \Gamma_2$.
""",
        "correction": r"""**1) a)** $P(i) = -i - (6+5i)(-1) + (1+20i)i + 14 - 5i = -i + 6 + 5i + i - 20 + 14 - 5i = 0$.

En identifiant les coefficients de $(z - i)(z^2 + az + b) = z^3 + (a - i)z^2 + (b - ia)z - ib$ :
$a - i = -6 - 5i$ donne $a = -6 - 4i$, et $-ib = 14 - 5i$ donne $b = 5 + 14i$.

$P(z) = (z - i)\big(z^2 - (6+4i)z + 5 + 14i\big)$.

**b)** Pour $z^2 - (6+4i)z + 5 + 14i = 0$ : $\Delta = (6+4i)^2 - 4(5+14i) = 20 + 48i - 20 - 56i = -8i = (2 - 2i)^2$.

$z' = \dfrac{6 + 4i + 2 - 2i}{2} = 4 + i$ et $z'' = \dfrac{6 + 4i - 2 + 2i}{2} = 2 + 3i$.

$S = \{\,i \ ;\ 4 + i \ ;\ 2 + 3i\,\}$.

**2) a)** $s : z' = a(z - z_A) + z_A$ avec $a = \dfrac{z_C - z_A}{z_B - z_A} = \dfrac{2 + 2i}{4} = \dfrac{1+i}{2}$.

$z' = \dfrac{1+i}{2}(z - i) + i$, soit $\boxed{z' = \dfrac{1+i}{2}\,z + \dfrac{1+i}{2}}$.

**b)** $\dfrac{1+i}{2} = \dfrac{\sqrt{2}}{2}e^{i\pi/4}$ : rapport $\dfrac{\sqrt{2}}{2}$, angle $\dfrac{\pi}{4}$.

**3) a)** Pour $M \neq B$ : $\dfrac{z - z_A}{z - z_B}$ est imaginaire pur $\iff M = A$ (quotient nul) ou $(\overrightarrow{MB}, \overrightarrow{MA}) \equiv \dfrac{\pi}{2}\ [\pi]$.

$\Gamma_1$ est le **cercle de diamètre $[AB]$ privé de $B$** : centre $2 + i$, rayon $2$.

De même, $\Gamma_2$ est le **cercle de diamètre $[AC]$ privé de $C$** : centre $1 + 2i$, rayon $\sqrt{2}$.

**b)** $s(A) = A$ et $s(B) = C$. Une similitude conserve les angles orientés et transforme un cercle en cercle : l'image du cercle de diamètre $[AB]$ est le cercle de diamètre $[s(A)s(B)] = [AC]$, et le point exclu $B$ a pour image le point exclu $C$. Donc $s(\Gamma_1) = \Gamma_2$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2015-sn-math-ex1": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1)** On pose $P(z) = z^3 - (11+6i)z^2 + (28+38i)z - 12 - 60i$ où $z$ est un nombre complexe.

a) Calculer $P(3)$ et déterminer les nombres $a$ et $b$ tels que pour tout $z$ de $\mathbb{C}$ : $P(z) = (z - 3)(z^2 + az + b)$.

b) Résoudre, dans l'ensemble des nombres complexes, l'équation $P(z) = 0$.

c) Soient $A$, $B$ et $C$ les points images des solutions de l'équation $P(z) = 0$ avec $\operatorname{Im}(z_A) < \operatorname{Im}(z_B) < \operatorname{Im}(z_C)$. Calculer l'affixe du point $G$ barycentre du système $\{(A;2),(B;-2),(C;2)\}$ et placer les points $A$, $B$, $C$ et $G$.

**2)** Pour tout réel $k$ différent de $2$, on définit l'application $f_k$ du plan dans lui-même qui à tout point $M$ associe le point $M'$ tel que :
$$\overrightarrow{MM'} = 2\overrightarrow{MA} - 2\overrightarrow{MB} + (3 - k)\overrightarrow{MC}.$$

a) Pour quelles valeurs de $k$ l'application $f_k$ est-elle une translation ? Déterminer alors son vecteur.

b) On suppose que $k \in \mathbb{R} \setminus \{2;3\}$. Montrer que $f_k$ admet un unique point invariant $\Omega_k$. Reconnaître alors $f_k$ et donner ses éléments caractéristiques en fonction de $k$.

c) Déterminer et construire le lieu géométrique des points $\Omega_k$ lorsque $k$ décrit $\mathbb{R} \setminus \{2;3\}$. Reconnaître $\Omega_1$.

d) Pour $k = 1$, déterminer et construire le lieu géométrique du point $R$, centre de gravité du triangle $AMM'$, lorsque $M$ décrit le cercle $\Gamma$ de centre $G$ passant par $C$.

**3)** Pour tout point $M$ du plan on pose $\varphi(M) = 2MA^2 - 2MB^2 + 2MC^2$ et $\Gamma_m$ l'ensemble des points $M$ tels que $\varphi(M) = m$, où $m$ est un réel.

a) Discuter, suivant les valeurs de $m$, la nature de $\Gamma_m$.

b) Déterminer et construire $\Gamma_m$ pour $m = 10$.
""",
        "correction": r"""**1) a)** $P(3) = 27 - 9(11+6i) + 3(28+38i) - 12 - 60i = 27 - 99 - 54i + 84 + 114i - 12 - 60i = 0$.

Par identification : $a = -8 - 6i$ et $b = 4 + 20i$, donc $P(z) = (z - 3)\big(z^2 - (8+6i)z + 4 + 20i\big)$.

**b)** $\Delta = (8+6i)^2 - 4(4+20i) = 28 + 96i - 16 - 80i = 12 + 16i = (4 + 2i)^2$.

$z' = \dfrac{8 + 6i + 4 + 2i}{2} = 6 + 4i$, $z'' = \dfrac{8 + 6i - 4 - 2i}{2} = 2 + 2i$.

$S = \{\,3 \ ;\ 2 + 2i \ ;\ 6 + 4i\,\}$.

**c)** Ordre des parties imaginaires : $z_A = 3$, $z_B = 2 + 2i$, $z_C = 6 + 4i$.

$z_G = \dfrac{2z_A - 2z_B + 2z_C}{2} = z_A - z_B + z_C = 7 + 2i$. ($ABCG$ est un parallélogramme.)

**2) a)** La somme des coefficients vaut $2 - 2 + (3 - k) = 3 - k$.

Si $k = 3$ : $\overrightarrow{MM'} = 2(\overrightarrow{MA} - \overrightarrow{MB}) = 2\overrightarrow{BA}$, vecteur constant. $f_3$ est la **translation de vecteur $2\overrightarrow{BA}$**, d'affixe $2(z_A - z_B) = 2 - 4i$.

Si $k \neq 3$, $f_k$ n'est pas une translation (voir b).

**b)** Pour $k \neq 3$, soit $\Omega_k = \operatorname{bar}\{(A;2),(B;-2),(C;3-k)\}$. Alors $\overrightarrow{MM'} = (3-k)\overrightarrow{M\Omega_k}$, d'où
$$z' - \omega_k = (k - 2)(z - \omega_k).$$
$M$ est invariant $\iff (k - 3)(z - \omega_k) = 0 \iff M = \Omega_k$ : point invariant unique.

$f_k$ est l'**homothétie de centre $\Omega_k$ et de rapport $k - 2$**, avec
$$\omega_k = \frac{2z_A - 2z_B + (3-k)z_C}{3 - k} = z_C + \frac{2 - 4i}{3 - k}.$$

**c)** $\overrightarrow{C\Omega_k} = \dfrac{1}{3-k}\,\overrightarrow{u}$ où $\overrightarrow{u}(2;-4)$. Quand $k$ décrit $\mathbb{R}\setminus\{2;3\}$, $t = \dfrac{1}{3-k}$ décrit $\mathbb{R}\setminus\{0;1\}$.

Le lieu de $\Omega_k$ est la **droite passant par $C$ de vecteur directeur $(1;-2)$**, d'équation $2x + y = 16$, **privée de $C$** ($t = 0$) **et du point d'affixe $8$** ($t = 1$).

$\omega_1 = 6 + 4i + \dfrac{2 - 4i}{2} = 7 + 2i$ : $\Omega_1 = G$.

**d)** Pour $k = 1$, $f_1$ est l'homothétie de centre $G$ et de rapport $-1$, c'est-à-dire la **symétrie centrale de centre $G$** : $z_{M'} = 2z_G - z$.

$z_R = \dfrac{z_A + z + z_{M'}}{3} = \dfrac{z_A + 2z_G}{3} = \dfrac{17}{3} + \dfrac{4}{3}i$.

$R$ ne dépend pas de $M$ : le lieu de $R$ est **le seul point $R\left(\frac{17}{3};\frac{4}{3}\right)$**.

**3) a)** $G$ est le barycentre de $\{(A;2),(B;-2),(C;2)\}$ (somme $2$), donc
$$\varphi(M) = 2MG^2 + 2GA^2 - 2GB^2 + 2GC^2.$$
$GA^2 = |{-4-2i}|^2 = 20$, $GB^2 = |{-5}|^2 = 25$, $GC^2 = |{-1+2i}|^2 = 5$, donc $2(20 - 25 + 5) = 0$ et $\varphi(M) = 2MG^2$.

- $m < 0$ : $\Gamma_m = \varnothing$ ;
- $m = 0$ : $\Gamma_m = \{G\}$ ;
- $m > 0$ : $\Gamma_m$ est le cercle de centre $G$ et de rayon $\sqrt{m/2}$.

**b)** $m = 10$ : cercle de centre $G(7;2)$ et de rayon $\sqrt{5}$. Il passe par $C$ car $GC = \sqrt{5}$ : c'est le cercle $\Gamma$ de la question 2d.
""",
        "note": "Énoncé corrigé depuis le PDF : la relation est MM' = … (et non OM'), "
                "et φ(M) porte sur les carrés MA², MB², MC². Au 2d le lieu de R est réduit à un point.",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2016-sc-math-ex1": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$. Pour tout nombre complexe $z$ on pose : $P(z) = z^3 - (1+3i)z^2 + 2iz + 6 - 2i$.

**1) a)** Calculer $P(1 - i)$.

b) Déterminer deux nombres $a$ et $b$ tels que pour tout $z \in \mathbb{C}$ on a : $P(z) = (z - 1 + i)(z^2 + az + b)$.

c) En déduire l'ensemble des solutions de l'équation $P(z) = 0$.

**2)** Soit $A$, $B$ et $C$ les points d'affixes respectives $z_A = -1 + i$, $z_B = 1 - i$ et $z_C = 1 + 3i$.

a) Placer les points $A$, $B$ et $C$ et déterminer la nature du triangle $ABC$.

b) Déterminer l'affixe du point $G$ barycentre du système $\{(A,2);(B,1);(C,1)\}$.

c) Déterminer et construire l'ensemble $\Gamma$ des points $M$ du plan tels que $2MA^2 + MB^2 + MC^2 = 16$.

d) Déterminer et construire l'ensemble $\Delta$ des points $M$ du plan tels que $-2MA^2 + MB^2 + MC^2 = 16$.

**3)** Soit $s$ la similitude directe de centre $C$ qui transforme $A$ en $B$.

a) Déterminer l'écriture complexe de $s$.

b) Déterminer le rapport et un angle de $s$.

**4)** On considère la parabole $P$ de foyer $A$ et de directrice $(BC)$.

a) Déterminer l'axe focal et le sommet de $P$.

b) Tracer $P$ et $P'$ dans le repère précédent, où $P' = s(P)$.

c) Donner des équations cartésiennes de $P$ et $P'$ dans le repère précédent.
""",
        "correction": r"""**1) a)** $(1-i)^2 = -2i$, $(1-i)^3 = -2 - 2i$.
$P(1-i) = -2 - 2i - (1+3i)(-2i) + 2i(1-i) + 6 - 2i = -2 - 2i + 2i - 6 + 2i + 2 + 6 - 2i = 0$.

**b)** Par identification : $a = -4i$ et $b = -4 - 2i$, donc $P(z) = (z - 1 + i)(z^2 - 4iz - 4 - 2i)$.

**c)** $\Delta = (4i)^2 + 4(4 + 2i) = 8i = (2 + 2i)^2$, d'où $z = \dfrac{4i \pm (2 + 2i)}{2}$, soit $1 + 3i$ et $-1 + i$.

$S = \{\,1 - i \ ;\ -1 + i \ ;\ 1 + 3i\,\}$.

**2) a)** $\overrightarrow{AB}$ a pour affixe $2 - 2i$ et $\overrightarrow{AC}$ a pour affixe $2 + 2i = i(2 - 2i)$.

Donc $AB = AC = 2\sqrt{2}$ et $(\overrightarrow{AB}, \overrightarrow{AC}) = \dfrac{\pi}{2}$ : $ABC$ est **rectangle isocèle en $A$** ($BC = 4$).

**b)** $z_G = \dfrac{2(-1+i) + (1-i) + (1+3i)}{4} = \dfrac{4i}{4} = i$.

**c)** $2MA^2 + MB^2 + MC^2 = 4MG^2 + 2GA^2 + GB^2 + GC^2$, avec $GA^2 = 1$, $GB^2 = |1 - 2i|^2 = 5$, $GC^2 = |1 + 2i|^2 = 5$.

$4MG^2 + 12 = 16 \iff MG = 1$ : $\Gamma$ est le **cercle de centre $G(0;1)$ et de rayon $1$**.

**d)** La somme des coefficients est nulle. Avec $M(x;y)$ :
$-2\big[(x+1)^2 + (y-1)^2\big] + (x-1)^2 + (y+1)^2 + (x-1)^2 + (y-3)^2 = -8x + 8$.

$-8x + 8 = 16 \iff x = -1$ : $\Delta$ est la **droite d'équation $x = -1$** (elle passe par $A$, parallèle à $(BC)$).

**3) a)** $s : z' = a(z - z_C) + z_C$ avec $a = \dfrac{z_B - z_C}{z_A - z_C} = \dfrac{-4i}{-2 - 2i} = 1 + i$.

$z' = (1+i)(z - 1 - 3i) + 1 + 3i$, soit $\boxed{z' = (1+i)z + 3 - i}$.

**b)** $1 + i = \sqrt{2}\,e^{i\pi/4}$ : rapport $\sqrt{2}$, angle $\dfrac{\pi}{4}$.

**4) a)** La directrice $(BC)$ est la droite $x = 1$. L'axe focal est la perpendiculaire à $(BC)$ passant par $A$ : la **droite $y = 1$**. Le sommet est le milieu de $A$ et de son projeté $(1;1)$ sur la directrice : $S(0;1)$.

**c)** (traitée avant b), car le tracé s'appuie sur les équations.) $M \in P \iff MA^2 = d(M,(BC))^2 \iff (x+1)^2 + (y-1)^2 = (x-1)^2$, soit
$$P : (y - 1)^2 = -4x.$$

$P' = s(P)$ est la parabole de foyer $s(A) = B$ et de directrice $s\big((BC)\big)$. Comme $s(C) = C$ et $s(B) = (1+i)(1-i) + 3 - i = 5 - i$, la directrice est la droite passant par $(1;3)$ et $(5;-1)$ : $x + y - 4 = 0$.

$M \in P' \iff (x-1)^2 + (y+1)^2 = \dfrac{(x + y - 4)^2}{2}$, soit
$$P' : x^2 + y^2 - 2xy + 4x + 12y - 12 = 0.$$

**b)** Le sommet de $P'$ est $s(S) = (1+i)i + 3 - i = 2$, soit $(2;0)$, et son axe est $s\big((y = 1)\big)$, la droite $(BS')$ d'équation $y = x - 2$. On trace $P$ (sommet $(0;1)$, ouverte vers les $x$ négatifs) puis $P'$ (sommet $(2;0)$, foyer $B$).
""",
        "note": "Énoncé corrigé depuis le scan : z_B = 1 − i (et non i − 1), facteur (z − 1 + i).",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2016-sn-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$. Pour tout nombre complexe $z$ on pose : $P(z) = z^3 - (4+8i)z^2 + (-14+24i)z + 32 + 4i$.

**1) a)** Calculer $P(2i)$ et déterminer deux nombres $a$ et $b$ tels que pour tout nombre complexe $z$ on a : $P(z) = (z - 2i)(z^2 + az + b)$.

b) En déduire l'ensemble des solutions de l'équation $P(z) = 0$. On note $z_1$, $z_2$ et $z_3$ ses solutions avec $|z_1| < |z_2| < |z_3|$.

c) Soit $A$, $B$ et $C$ les points d'affixes respectives $z_1$, $z_2$ et $z_3$. Déterminer l'affixe du point $G$ barycentre du système $\{(O,5);(A,-7);(C,4)\}$. Placer $A$, $B$, $C$ et $G$ sur la figure.

**2)** Pour tout nombre complexe $z$ on pose : $Q(z) = z^2 - (4+6i)z - 2 + 16i$. On note $\Gamma$ l'ensemble des points $M$ d'affixe $z$ tels que $Q(z)$ soit imaginaire pur (ou nul).

a) En posant $z = x + iy$, donner une équation cartésienne de $\Gamma$ et montrer que $\Gamma$ est une conique de centre $G$.

b) Préciser les sommets et l'excentricité de $\Gamma$ puis la construire dans le repère précédent.
""",
        "correction": r"""**1) a)** $P(2i) = -8i + 4(4+8i) + 2i(-14+24i) + 32 + 4i = -8i + 16 + 32i - 28i - 48 + 32 + 4i = 0$.

Par identification : $a = -4 - 6i$, $b = -2 + 16i$, donc $P(z) = (z - 2i)\big(z^2 - (4+6i)z - 2 + 16i\big)$.

**b)** $\Delta = (4+6i)^2 - 4(-2+16i) = -20 + 48i + 8 - 64i = -12 - 16i = (2 - 4i)^2$.

Racines : $\dfrac{4 + 6i \pm (2 - 4i)}{2}$, soit $3 + i$ et $1 + 5i$.

$|2i| = 2 < |3 + i| = \sqrt{10} < |1 + 5i| = \sqrt{26}$ : $z_1 = 2i$, $z_2 = 3 + i$, $z_3 = 1 + 5i$.

**c)** $z_G = \dfrac{5\cdot 0 - 7(2i) + 4(1 + 5i)}{5 - 7 + 4} = \dfrac{4 + 6i}{2} = 2 + 3i$.

**2) a)** Avec $z = x + iy$ : $\operatorname{Re} Q(z) = x^2 - y^2 - 4x + 6y - 2$.

$M \in \Gamma \iff x^2 - y^2 - 4x + 6y - 2 = 0 \iff (x - 2)^2 - (y - 3)^2 = -3$, soit
$$\Gamma : \frac{(y-3)^2}{3} - \frac{(x-2)^2}{3} = 1.$$

C'est une **hyperbole équilatère de centre $(2;3) = G$**, d'axe focal la droite $x = 2$.

**b)** $a = b = \sqrt{3}$, $c = \sqrt{a^2 + b^2} = \sqrt{6}$.

Sommets : $(2 ; 3 + \sqrt{3})$ et $(2 ; 3 - \sqrt{3})$. Foyers : $(2 ; 3 \pm \sqrt{6})$. Excentricité : $e = \dfrac{c}{a} = \sqrt{2}$. Asymptotes : $y - 3 = \pm(x - 2)$.

(Remarque : les racines de $Q$, $B$ et $C$, appartiennent à $\Gamma$ puisque $Q$ s'y annule.)
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2017-sc-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1)** On considère l'équation $(E) : iz^3 - (1+i)z^2 - (2+2i)z + 8i = 0$.

a) Vérifier que l'équation $(E)$ admet une solution réelle à déterminer.

b) Déterminer les deux autres solutions de l'équation $(E)$.

c) Placer les points $A$, $B$ et $C$ d'affixes respectives $-2$ ; $2 - 2i$ et $1 + i$. Déterminer la nature du triangle $ABC$.

**2)** Soit $s$ l'application du plan dans lui-même qui à tout point $M(x;y)$ associe le point $M'(x';y')$ tel que $x' = x + y$ et $y' = -x + y - 2$.

a) Donner l'expression complexe de $s$.

b) En déduire la nature et les éléments caractéristiques de $s$. Déterminer $s(C)$.

**3)** On désigne par $z_G$ l'affixe du point $G$, centre de gravité du triangle $ABC$, et pour tout nombre complexe $z$ on pose :
$$f(z) = |z + 2|^2 + |z - 2 + 2i|^2 + |z - 1 - i|^2.$$

a) Justifier que $z_G = \dfrac{1}{3} - \dfrac{1}{3}i$ et que $f(z) = 3\left|z - \dfrac{1}{3} + \dfrac{1}{3}i\right|^2 + \dfrac{40}{3}$.

b) Déterminer, suivant les valeurs du réel $k$, l'ensemble $\Gamma_k$ des points $M$ du plan d'affixe $z$ tels que $f(z) = k$. Déterminer l'ensemble $\Gamma_{20}$.
""",
        "correction": r"""**1) a)** Pour $z = x$ réel : $ix^3 - (1+i)x^2 - (2+2i)x + 8i = 0 \iff \begin{cases} -x^2 - 2x = 0 \\ x^3 - x^2 - 2x + 8 = 0 \end{cases}$.

La première donne $x = 0$ ou $x = -2$ ; seul $x = -2$ vérifie la seconde ($-8 - 4 + 4 + 8 = 0$). La solution réelle est $\boxed{-2}$.

**b)** $iz^3 - (1+i)z^2 - (2+2i)z + 8i = (z + 2)\big(iz^2 - (1+3i)z + 4i\big)$.

$iz^2 - (1+3i)z + 4i = 0 \iff z^2 - (3 - i)z + 4 = 0$ (en divisant par $i$).

$\Delta = (3 - i)^2 - 16 = -8 - 6i = (1 - 3i)^2$, d'où $z = \dfrac{3 - i \pm (1 - 3i)}{2}$ : $2 - 2i$ et $1 + i$.

$S = \{\,-2 \ ;\ 2 - 2i \ ;\ 1 + i\,\}$.

**c)** $CA = |{-3 - i}| = \sqrt{10}$, $CB = |1 - 3i| = \sqrt{10}$, $AB = |4 - 2i| = 2\sqrt{5}$, et $CA^2 + CB^2 = 20 = AB^2$.

$ABC$ est **rectangle isocèle en $C$**.

**2) a)** $z' = x' + iy' = (x + y) + i(-x + y - 2) = (1 - i)x + (1 + i)y - 2i = (1 - i)(x + iy) - 2i$.

$\boxed{z' = (1 - i)z - 2i}$.

**b)** $1 - i = \sqrt{2}\,e^{-i\pi/4} \neq 1$ : $s$ est une **similitude directe** de rapport $\sqrt{2}$ et d'angle $-\dfrac{\pi}{4}$. Son centre vérifie $\omega = (1 - i)\omega - 2i \iff i\omega = -2i \iff \omega = -2$ : c'est le point $A$.

$s(C) = (1 - i)(1 + i) - 2i = 2 - 2i$, donc $s(C) = B$.

**3) a)** $z_G = \dfrac{-2 + 2 - 2i + 1 + i}{3} = \dfrac{1}{3} - \dfrac{1}{3}i$.

$f(z) = MA^2 + MB^2 + MC^2 = 3MG^2 + GA^2 + GB^2 + GC^2$, avec
$GA^2 = \left|-\tfrac{7}{3} + \tfrac{1}{3}i\right|^2 = \tfrac{50}{9}$, $GB^2 = \left|\tfrac{5}{3} - \tfrac{5}{3}i\right|^2 = \tfrac{50}{9}$, $GC^2 = \left|\tfrac{2}{3} + \tfrac{4}{3}i\right|^2 = \tfrac{20}{9}$.

Leur somme vaut $\dfrac{120}{9} = \dfrac{40}{3}$, d'où $f(z) = 3|z - z_G|^2 + \dfrac{40}{3}$.

**b)** $f(z) = k \iff MG^2 = \dfrac{3k - 40}{9}$.

- $k < \dfrac{40}{3}$ : $\Gamma_k = \varnothing$ ;
- $k = \dfrac{40}{3}$ : $\Gamma_k = \{G\}$ ;
- $k > \dfrac{40}{3}$ : $\Gamma_k$ est le cercle de centre $G$ et de rayon $\dfrac{\sqrt{3k - 40}}{3}$.

$\Gamma_{20}$ : cercle de centre $G\left(\frac{1}{3};-\frac{1}{3}\right)$ et de rayon $\dfrac{\sqrt{20}}{3} = \dfrac{2\sqrt{5}}{3}$.
""",
        "note": "Énoncé corrigé depuis le PDF : l'équation (E), l'application s et la fonction f "
                "étaient mal retranscrites par l'OCR.",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2017-sn-math-ex1": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1) a)** Soit $a$ un nombre réel. Résoudre dans l'ensemble des nombres complexes l'équation d'inconnue $z$ :
$$(1+i)z^2 - 2(a+1)z - (-1+i)(a^2+1) = 0.$$

b) Soient $f$ et $g$ les transformations données par leurs expressions complexes $f : z \mapsto z' = 1 - iz$ et $g : z \mapsto z'' = z - i$. Déterminer la nature et les éléments caractéristiques de chacune des transformations $f$ et $g$.

Dans le reste de l'exercice on considère les points $I$, $M_1$ et $M_2$ d'affixes respectives $z_0 = 1 - i$, $z_1 = 1 - ia$ et $z_2 = a - i$, où $a = e^{i\alpha}$, $\alpha \in \,]0;2\pi[$.

**2) a)** Montrer que le triangle $IM_1M_2$ est rectangle en $I$, isocèle et direct.

b) Préciser les lieux géométriques de chacun des points $M_1$ et $M_2$ lorsque $\alpha$ décrit l'intervalle $]0;\pi[$.

c) Écrire $z_1$ et $z_2$ sous forme exponentielle pour $\alpha$ appartenant à l'intervalle $\left]0;\dfrac{\pi}{2}\right[$.

**3)** Soit $M_3$ le point d'affixe $z_3 = i\sin\alpha + ia$ et soit $G$ l'isobarycentre des points $M_1$, $M_2$ et $M_3$.

a) Vérifier que $z_G = \dfrac{1 + \cos\alpha}{3} + i\,\dfrac{-1 + 2\sin\alpha}{3}$ puis montrer que, pour $\alpha \in \,]0;\pi[$, le point $G$ appartient à une ellipse $\Gamma$ dont on donnera une équation.

b) Préciser les sommets et l'excentricité de $\Gamma$ puis la construire dans le repère précédent.
""",
        "correction": r"""**1) a)** On vérifie que $z' = a - i$ et $z'' = 1 - ia$ conviennent :

somme $z' + z'' = (a + 1) - i(a + 1) = (a+1)(1 - i) = \dfrac{2(a+1)}{1+i}$ ;

produit $z'z'' = (a - i)(1 - ia) = a - ia^2 - i - a = -i(a^2 + 1) = \dfrac{(1 - i)(a^2+1)}{1+i}$.

Ce sont bien la somme $\dfrac{2(a+1)}{1+i}$ et le produit $\dfrac{-(-1+i)(a^2+1)}{1+i}$ des racines. $S = \{\,a - i \ ;\ 1 - ia\,\}$.

**b)** $f : z' = -iz + 1$ avec $-i = e^{-i\pi/2}$ : **rotation d'angle $-\dfrac{\pi}{2}$**, de centre $\omega$ tel que $\omega = 1 - i\omega$, soit $\omega = \dfrac{1}{1+i} = \dfrac{1 - i}{2}$.

$g : z'' = z - i$ : **translation de vecteur $-\vec{v}$** (affixe $-i$).

**2) a)** $z_1 - z_0 = i(1 - a)$ et $z_2 - z_0 = a - 1$, donc $z_2 - z_0 = i(z_1 - z_0)$.

Ainsi $IM_2 = IM_1$ et $(\overrightarrow{IM_1}, \overrightarrow{IM_2}) = \dfrac{\pi}{2}$ : $IM_1M_2$ est rectangle isocèle direct en $I$.

**b)** Soit $N$ le point d'affixe $a = e^{i\alpha}$. Pour $\alpha \in \,]0;\pi[$, $N$ décrit le demi-cercle unité supérieur (privé de $\pm 1$).

$M_1 = f(N)$ : $z_1 = 1 + e^{i(\alpha - \pi/2)}$ avec $\alpha - \dfrac{\pi}{2} \in \left]-\dfrac{\pi}{2};\dfrac{\pi}{2}\right[$. $M_1$ décrit le **demi-cercle de centre $(1;0)$ et de rayon $1$ situé dans le demi-plan $x > 1$** (extrémités exclues).

$M_2 = g(N)$ : $M_2$ décrit le **demi-cercle de centre $(0;-1)$ et de rayon $1$ situé dans le demi-plan $y > -1$** (extrémités exclues).

**c)** $z_1 = 1 + e^{i(\alpha - \pi/2)} = 2\cos\left(\dfrac{\alpha}{2} - \dfrac{\pi}{4}\right) e^{i\left(\frac{\alpha}{2} - \frac{\pi}{4}\right)}$ ;

$z_2 = e^{i\alpha} + e^{-i\pi/2} = 2\cos\left(\dfrac{\alpha}{2} + \dfrac{\pi}{4}\right) e^{i\left(\frac{\alpha}{2} - \frac{\pi}{4}\right)}$.

Pour $\alpha \in \left]0;\frac{\pi}{2}\right[$, $\frac{\alpha}{2} - \frac{\pi}{4} \in \left]-\frac{\pi}{4};0\right[$ et $\frac{\alpha}{2} + \frac{\pi}{4} \in \left]\frac{\pi}{4};\frac{\pi}{2}\right[$ : les deux cosinus sont strictement positifs, ce sont donc les formes exponentielles (modules $2\cos(\cdot)$, argument $\frac{\alpha}{2} - \frac{\pi}{4}$).

**3) a)** $z_1 + z_2 + z_3 = 1 - ia + a - i + i\sin\alpha + ia = 1 + \cos\alpha + i(2\sin\alpha - 1)$, d'où la formule de $z_G$.

Avec $x = \dfrac{1 + \cos\alpha}{3}$ et $y = \dfrac{-1 + 2\sin\alpha}{3}$ : $\cos\alpha = 3x - 1$, $\sin\alpha = \dfrac{3y + 1}{2}$. Comme $\cos^2\alpha + \sin^2\alpha = 1$ :
$$\Gamma : \frac{\left(x - \frac{1}{3}\right)^2}{\frac{1}{9}} + \frac{\left(y + \frac{1}{3}\right)^2}{\frac{4}{9}} = 1.$$

(Pour $\alpha \in \,]0;\pi[$, $\sin\alpha > 0$ : $G$ décrit la partie de $\Gamma$ où $y > -\frac{1}{3}$.)

**b)** Centre $\Omega\left(\frac{1}{3};-\frac{1}{3}\right)$, grand axe vertical : $a = \dfrac{2}{3}$, $b = \dfrac{1}{3}$, $c = \sqrt{a^2 - b^2} = \dfrac{\sqrt{3}}{3}$.

Sommets : $\left(\frac{1}{3};\frac{1}{3}\right)$, $\left(\frac{1}{3};-1\right)$, $\left(0;-\frac{1}{3}\right)$, $\left(\frac{2}{3};-\frac{1}{3}\right)$. Excentricité $e = \dfrac{c}{a} = \dfrac{\sqrt{3}}{2}$.
""",
        "note": "Énoncé corrigé depuis le PDF : g(z) = z − i (translation), z₂ = a − i, z₃ = i sin α + ia.",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2018-sc-math-ex1": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{i},\vec{j})$. Pour tout nombre complexe $z$ on pose : $P(z) = z^3 - (7+3i)z^2 + (12+15i)z - 4 - 18i$.

**1) a)** Calculer $P(2)$ et déterminer les nombres $a$ et $b$ tels que $\forall z \in \mathbb{C}$ : $P(z) = (z - 2)(z^2 + az + b)$.

b) En déduire l'ensemble des solutions de l'équation $P(z) = 0$.

c) On considère les points $A$, $B$ et $D$ images des solutions de l'équation $P(z) = 0$ tels que $\operatorname{Im}(z_A) \le \operatorname{Im}(z_B) \le \operatorname{Im}(z_D)$. Placer les points $A$, $B$ et $D$ et déterminer la nature du triangle $ABD$.

**2) a)** Déterminer le barycentre du système $\{(A;9),(B;-6),(C;2)\}$, où $C$ est le symétrique de $A$ par rapport à $(BD)$.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ du plan tels que $9MA^2 - 6MB^2 + 2MC^2 = -10$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ du plan tels que $4MA^2 - 6MB^2 + 2MC^2 = -10$.

d) Déterminer et construire l'ensemble $\Gamma_3$ des points $M$ du plan tels que
$$\left(9\overrightarrow{MA} - 6\overrightarrow{MB} + 2\overrightarrow{MC}\right)\cdot\left(\overrightarrow{MA} - \overrightarrow{MB} + \overrightarrow{MC}\right) = 10.$$

**3)** Soit $S_0 = \mathrm{id}$ et $\forall n \in \mathbb{N}$, $S_{n+1} = S \circ S_n$, où $S$ est la similitude directe qui transforme $A$ en $B$ et $B$ en $D$.

a) Déterminer la nature et les éléments caractéristiques de $S_{2018}$.

b) Justifier que $S_{2020^{2020}}$ est une homothétie de rapport positif.
""",
        "correction": r"""**1) a)** $P(2) = 8 - 4(7+3i) + 2(12+15i) - 4 - 18i = 8 - 28 - 12i + 24 + 30i - 4 - 18i = 0$.

Par identification : $a = -5 - 3i$, $b = 2 + 9i$, donc $P(z) = (z - 2)\big(z^2 - (5+3i)z + 2 + 9i\big)$.

**b)** $\Delta = (5+3i)^2 - 4(2+9i) = 16 + 30i - 8 - 36i = 8 - 6i = (3 - i)^2$.

Racines : $\dfrac{5 + 3i \pm (3 - i)}{2}$, soit $4 + i$ et $1 + 2i$. $S = \{\,2 \ ;\ 4 + i \ ;\ 1 + 2i\,\}$.

**c)** $z_A = 2$, $z_B = 4 + i$, $z_D = 1 + 2i$.

$z_D - z_A = -1 + 2i = i(2 + i) = i(z_B - z_A)$ : $AB = AD = \sqrt{5}$ et $(\overrightarrow{AB}, \overrightarrow{AD}) = \dfrac{\pi}{2}$. $ABD$ est **rectangle isocèle direct en $A$**.

**2) a)** $ABD$ étant rectangle isocèle en $A$, le symétrique $C$ de $A$ par rapport à $(BD)$ fait de $ABCD$ un carré : $z_C = z_B + z_D - z_A = 3 + 3i$.

Barycentre : $\dfrac{9\cdot 2 - 6(4+i) + 2(3+3i)}{5} = \dfrac{0}{5} = 0$. C'est le **point $O$**.

**b)** $9MA^2 - 6MB^2 + 2MC^2 = 5MO^2 + 9OA^2 - 6OB^2 + 2OC^2 = 5MO^2 + 36 - 102 + 36 = 5MO^2 - 30$.

$5MO^2 - 30 = -10 \iff MO = 2$ : $\Gamma_1$ est le **cercle de centre $O$ et de rayon $2$**.

**c)** La somme des coefficients est nulle. Avec $M(x;y)$ :
$4\big[(x-2)^2 + y^2\big] - 6\big[(x-4)^2 + (y-1)^2\big] + 2\big[(x-3)^2 + (y-3)^2\big] = 20x - 50$.

$20x - 50 = -10 \iff x = 2$ : $\Gamma_2$ est la **droite d'équation $x = 2$** (perpendiculaire à $(OA)$ en $A$).

**d)** $9\overrightarrow{MA} - 6\overrightarrow{MB} + 2\overrightarrow{MC} = 5\overrightarrow{MO}$, et $\overrightarrow{MA} - \overrightarrow{MB} + \overrightarrow{MC} = \overrightarrow{MD'}$ où $D'$ a pour affixe $z_A - z_B + z_C = 1 + 2i$ : $D' = D$.

$5\,\overrightarrow{MO}\cdot\overrightarrow{MD} = 10 \iff \overrightarrow{MO}\cdot\overrightarrow{MD} = 2$. Avec $K$ milieu de $[OD]$, $K\left(\frac{1}{2};1\right)$ :
$\overrightarrow{MO}\cdot\overrightarrow{MD} = MK^2 - \dfrac{OD^2}{4} = MK^2 - \dfrac{5}{4}$.

$MK^2 = \dfrac{13}{4}$ : $\Gamma_3$ est le **cercle de centre $K\left(\frac{1}{2};1\right)$ et de rayon $\dfrac{\sqrt{13}}{2}$**.

**3)** $S : z' = \alpha z + \beta$ avec $\alpha = \dfrac{z_D - z_B}{z_B - z_A} = \dfrac{-3 + i}{2 + i} = -1 + i$ et $\beta = z_B - \alpha z_A = 6 - i$.

$S$ : rapport $\sqrt{2}$, angle $\dfrac{3\pi}{4}$, centre $\Omega$ d'affixe $\dfrac{\beta}{1 - \alpha} = \dfrac{6 - i}{2 - i} = \dfrac{13 + 4i}{5}$.

$S_n = S^n$ est la similitude de centre $\Omega$, de rapport $(\sqrt{2})^n$ et d'angle $\dfrac{3n\pi}{4}$.

**a)** $n = 2018$ : rapport $2^{1009}$, angle $\dfrac{3 \times 2018\,\pi}{4} = 1513\pi + \dfrac{\pi}{2} \equiv -\dfrac{\pi}{2}\ [2\pi]$.

$S_{2018}$ est la similitude directe de centre $\Omega\left(\frac{13}{5};\frac{4}{5}\right)$, de rapport $2^{1009}$ et d'angle $-\dfrac{\pi}{2}$.

**b)** $N = 2020^{2020} = 4^{2020}\times 505^{2020}$ est multiple de $8$, donc $\dfrac{3N\pi}{4}$ est un multiple de $2\pi$ : l'angle est nul. $S_N$ est l'**homothétie de centre $\Omega$ et de rapport $(\sqrt{2})^N > 0$**.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2018-sn-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{i},\vec{j})$. Pour tout nombre complexe $z$ on pose : $P(z) = z^3 - (1+4i)z^2 - (9-i)z - 6 + 18i$.

**1) a)** Calculer $P(3i)$ et déterminer les nombres $a$ et $b$ tels que $\forall z \in \mathbb{C}$ : $P(z) = (z - 3i)(z^2 + az + b)$.

b) En déduire l'ensemble des solutions de l'équation $P(z) = 0$.

c) On considère les points $A$, $B$ et $C$ images des solutions de l'équation $P(z) = 0$ tels que $|z_C| \le |z_B| \le |z_A|$. Placer les points $A$, $B$ et $C$ et déterminer la nature du triangle $ABC$.

d) Soit $A' = \operatorname{bar}\{(A;-5),(B;6),(C;12)\}$. Vérifier que l'affixe de $A'$ est $z_{A'} = -3 + i$. Placer $A'$.

**2)** On considère l'ellipse $\Gamma$ de sommets $A$, $A'$ et $B$.

a) Déterminer le centre $I$ et l'excentricité de $\Gamma$.

b) Écrire une équation cartésienne de $\Gamma$ dans le repère $(O;\vec{i},\vec{j})$.

c) Préciser les points d'intersection de $\Gamma$ avec l'axe $(Ox)$.

d) Déterminer les foyers et les directrices de $\Gamma$ puis construire $\Gamma$.
""",
        "correction": r"""**1) a)** $P(3i) = -27i + 9(1+4i) - 3i(9 - i) - 6 + 18i = -27i + 9 + 36i - 27i - 3 - 6 + 18i = 0$.

Par identification : $a = -1 - i$, $b = -6 - 2i$, donc $P(z) = (z - 3i)\big(z^2 - (1+i)z - 6 - 2i\big)$.

**b)** $\Delta = (1+i)^2 + 4(6+2i) = 24 + 10i = (5 + i)^2$, d'où $z = \dfrac{1 + i \pm (5 + i)}{2}$ : $3 + i$ et $-2$.

$S = \{\,3i \ ;\ 3 + i \ ;\ -2\,\}$.

**c)** $|{-2}| = 2 \le |3i| = 3 \le |3 + i| = \sqrt{10}$ : $z_C = -2$, $z_B = 3i$, $z_A = 3 + i$.

$BA = |3 - 2i| = \sqrt{13}$, $BC = |{-2 - 3i}| = \sqrt{13}$, $AC = |{-5 - i}| = \sqrt{26}$ et $BA^2 + BC^2 = AC^2$ : $ABC$ est **rectangle isocèle en $B$**.

**d)** $z_{A'} = \dfrac{-5(3 + i) + 6(3i) + 12(-2)}{-5 + 6 + 12} = \dfrac{-39 + 13i}{13} = -3 + i$.

**2) a)** $A(3;1)$ et $A'(-3;1)$ sont deux sommets symétriques : le centre est leur milieu $I(0;1)$, d'affixe $i$.

$a = IA = 3$ (axe focal horizontal $y = 1$) et $b = IB = 2$ ; $c = \sqrt{a^2 - b^2} = \sqrt{5}$ et $e = \dfrac{c}{a} = \dfrac{\sqrt{5}}{3}$.

**b)** $\Gamma : \dfrac{x^2}{9} + \dfrac{(y - 1)^2}{4} = 1$.

**c)** $y = 0$ : $\dfrac{x^2}{9} = \dfrac{3}{4}$, soit $x = \pm\dfrac{3\sqrt{3}}{2}$. Points $\left(\pm\dfrac{3\sqrt{3}}{2};0\right)$.

**d)** Foyers $F(\sqrt{5};1)$ et $F'(-\sqrt{5};1)$. Directrices $x = \pm\dfrac{a^2}{c} = \pm\dfrac{9\sqrt{5}}{5}$. Quatrième sommet $(0;-1)$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2019-sc-math-ex1": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé direct $(O;\vec{i},\vec{j})$. Pour tout nombre complexe $z$ on pose :
$$P(z) = z^3 - (12+5i)z^2 + (45+42i)z - (54+97i).$$

**1) a)** Déterminer les nombres $m$ et $p$ tels que $\forall z \in \mathbb{C}$, $P(z) = (z - 3 - 4i)(z^2 + mz + p)$ puis résoudre dans $\mathbb{C}$ l'équation $P(z) = 0$.

b) On considère les points $A$, $B$ et $C$ images respectives des solutions de l'équation $P(z) = 0$, avec $\operatorname{Re}(z_A) \ge \operatorname{Re}(z_B) \ge \operatorname{Re}(z_C)$. Placer les points $A$, $B$ et $C$.

**2) a)** Déterminer l'affixe du point $I$, barycentre du système $\{(A;-3);(B;2);(C;3)\}$.

b) Donner l'écriture complexe de la similitude directe $S$ de centre $I$, de rapport $\dfrac{1}{\sqrt{2}}$ et d'angle $\dfrac{\pi}{4}$.

c) Montrer que l'image de $C$ par $S$ est le point $D$ d'affixe $1 + 4i$.

**3)** On considère l'ellipse $\Gamma$ de centre $I$ dont $D$ et $A$ sont des sommets.

a) Donner l'équation réduite de $\Gamma$ dans le repère $(O;\vec{i},\vec{j})$.

b) Déterminer l'excentricité, les foyers et les autres sommets de $\Gamma$. Construire $\Gamma$.

**4)** On considère la suite $(M_n)$ des points du plan définis par $M_0 = C$ et $\forall n \in \mathbb{N}$, $M_{n+1} = S(M_n)$.

a) Déterminer les affixes respectives $z_1$, $z_2$ et $z_3$ des points $M_1$, $M_2$ et $M_3$.

b) Montrer que tous les points $M_n$ appartiennent à l'une des quatre droites $(IA)$, $(IB)$, $(IC)$ et $(ID)$. Laquelle passe par $M_{2019}$ ?
""",
        "correction": r"""**1) a)** En développant $(z - 3 - 4i)(z^2 + mz + p)$ et en identifiant : $m - 3 - 4i = -12 - 5i$ donne $m = -9 - i$, et $-(3 + 4i)p = -(54 + 97i)$ donne $p = \dfrac{54 + 97i}{3 + 4i} = 22 + 3i$.

$z^2 - (9 + i)z + 22 + 3i = 0$ : $\Delta = (9+i)^2 - 4(22+3i) = -8 + 6i = (1 + 3i)^2$, d'où $z = \dfrac{9 + i \pm (1 + 3i)}{2}$ : $5 + 2i$ et $4 - i$.

$S = \{\,3 + 4i \ ;\ 5 + 2i \ ;\ 4 - i\,\}$.

**b)** $z_A = 5 + 2i$, $z_B = 4 - i$, $z_C = 3 + 4i$.

**2) a)** $z_I = \dfrac{-3(5 + 2i) + 2(4 - i) + 3(3 + 4i)}{2} = \dfrac{2 + 4i}{2} = 1 + 2i$.

**b)** $\dfrac{1}{\sqrt{2}}e^{i\pi/4} = \dfrac{1 + i}{2}$, donc $z' - z_I = \dfrac{1+i}{2}(z - z_I)$, soit
$$S : z' = \frac{1+i}{2}\,z + \frac{3 + i}{2}.$$

**c)** $S(C) : \dfrac{(1+i)(3+4i)}{2} + \dfrac{3+i}{2} = \dfrac{-1 + 7i + 3 + i}{2} = 1 + 4i = z_D$.

**3) a)** $\overrightarrow{ID}(0;2)$ et $\overrightarrow{IA}(4;0)$ sont orthogonaux : $D$ est un sommet du petit axe ($b = 2$, vertical) et $A$ un sommet du grand axe ($a = 4$, horizontal).
$$\Gamma : \frac{(x - 1)^2}{16} + \frac{(y - 2)^2}{4} = 1.$$

**b)** $c = \sqrt{16 - 4} = 2\sqrt{3}$, $e = \dfrac{c}{a} = \dfrac{\sqrt{3}}{2}$.
Foyers $(1 + 2\sqrt{3};2)$ et $(1 - 2\sqrt{3};2)$. Autres sommets : $(-3;2)$ et $(1;0)$.

**4) a)** $z_1 = z_D = 1 + 4i$ ; $z_2 = \dfrac{(1+i)(1+4i)}{2} + \dfrac{3+i}{2} = 3i$ ; $z_3 = \dfrac{(1+i)(3i)}{2} + \dfrac{3+i}{2} = 2i$.

**b)** $z_n - z_I = \left(\dfrac{1+i}{2}\right)^n (z_C - z_I)$, donc $\arg(z_n - z_I) \equiv \dfrac{\pi}{4} + \dfrac{n\pi}{4}\ [2\pi]$.

Directions depuis $I$ : $(IC)$ : $\frac{\pi}{4}$ ($z_C - z_I = 2 + 2i$) ; $(ID)$ : $\frac{\pi}{2}$ ($2i$) ; $(IB)$ : $-\frac{\pi}{4} \equiv \frac{3\pi}{4}\ [\pi]$ ($3 - 3i$) ; $(IA)$ : $0$ ($4$).

Modulo $\pi$, la direction de $\overrightarrow{IM_n}$ ne dépend que du reste de $n$ modulo $4$ :
$n \equiv 0 \to (IC)$, $n \equiv 1 \to (ID)$, $n \equiv 2 \to (IB)$, $n \equiv 3 \to (IA)$.

$2019 = 4 \times 504 + 3$ : $M_{2019} \in (IA)$.
""",
        "note": "Énoncé corrigé depuis le scan : l'angle de S est π/4 (et non −π/4).",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2019-sn-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1)** Pour tout nombre complexe $z$ on pose $P(z) = z^3 - (5+4i)z^2 + (7+10i)z + 5 - 10i$. Calculer $P(i)$ puis déterminer les solutions $z_0$, $z_1$ et $z_2$ de l'équation $P(z) = 0$ avec $\operatorname{Re}(z_0) < \operatorname{Re}(z_1) < \operatorname{Re}(z_2)$.

**2)** On considère les points $A$, $B$ et $C$ d'affixes respectives $z_0$, $z_1$ et $z_2$.

a) Déterminer la nature du triangle $ABC$.

b) Soit $G$ le barycentre du système $\{(A,13);(B,-3);(C,2)\}$. Déterminer l'affixe de $G$.

c) Déterminer et construire l'ensemble $\Gamma$ des points $M$ du plan tels que $13MA^2 - 3MB^2 + 2MC^2 = 12$.

**3)** On considère l'hyperbole $H$ de centre $G$ qui passe par $C$ et dont $A$ est un sommet.

a) Déterminer le 2ème sommet de $H$.

b) Vérifier que l'équation de $H$ peut s'écrire sous la forme $x^2 - 3(y - 2)^2 = -3$.

c) Donner l'équation réduite de $H$ puis déterminer ses foyers, ses asymptotes et son excentricité et la construire.
""",
        "correction": r"""**1)** $P(i) = -i + (5 + 4i) + i(7 + 10i) + 5 - 10i = -i + 5 + 4i + 7i - 10 + 5 - 10i = 0$.

$P(z) = (z - i)\big(z^2 - (5 + 3i)z + 10 + 5i\big)$ ; $\Delta = (5+3i)^2 - 4(10+5i) = -24 + 10i = (1 + 5i)^2$.

Racines $\dfrac{5 + 3i \pm (1 + 5i)}{2}$ : $3 + 4i$ et $2 - i$.

$z_0 = i$, $z_1 = 2 - i$, $z_2 = 3 + 4i$.

**2) a)** $\dfrac{z_C - z_A}{z_B - z_A} = \dfrac{3 + 3i}{2 - 2i} = \dfrac{3}{2}i$ : imaginaire pur, donc $(\overrightarrow{AB}, \overrightarrow{AC}) = \dfrac{\pi}{2}$. $ABC$ est **rectangle en $A$** (non isocèle : $AC = \frac{3}{2}AB$).

**b)** $z_G = \dfrac{13i - 3(2 - i) + 2(3 + 4i)}{12} = \dfrac{24i}{12} = 2i$.

**c)** $13MA^2 - 3MB^2 + 2MC^2 = 12MG^2 + 13GA^2 - 3GB^2 + 2GC^2$ avec $GA^2 = 1$, $GB^2 = |2 - 3i|^2 = 13$, $GC^2 = |3 + 2i|^2 = 13$ : $13 - 39 + 26 = 0$.

$12MG^2 = 12 \iff MG = 1$ : $\Gamma$ est le **cercle de centre $G(0;2)$ et de rayon $1$** (il passe par $A$).

**3) a)** Le 2ème sommet est le symétrique de $A(0;1)$ par rapport à $G(0;2)$ : $A_2(0;3)$.

**b)** Axe focal $x = 0$, $a = GA = 1$ : $H : (y - 2)^2 - \dfrac{x^2}{b^2} = 1$. $C(3;4) \in H$ : $4 - \dfrac{9}{b^2} = 1$, donc $b^2 = 3$.

$(y-2)^2 - \dfrac{x^2}{3} = 1 \iff x^2 - 3(y - 2)^2 = -3$.

**c)** Équation réduite : $\dfrac{(y - 2)^2}{1} - \dfrac{x^2}{3} = 1$.

$c = \sqrt{1 + 3} = 2$ : foyers $(0;0)$ et $(0;4)$. Excentricité $e = \dfrac{c}{a} = 2$. Asymptotes $y - 2 = \pm\dfrac{x}{\sqrt{3}}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2020-sn-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{i},\vec{j})$. Pour tout nombre complexe $z$ on pose : $P(z) = z^3 + (1-2i)z^2 - (5+3i)z + 4 - 8i$.

**1)** Calculer $P(-i)$ et en déduire l'ensemble des solutions de l'équation $P(z) = 0$.

**2)** On note $A$, $B$ et $C$ les images des solutions de l'équation $P(z) = 0$ telles que $|z_B| < |z_A| < |z_C|$.

a) Placer les points $A$, $B$ et $C$ puis déterminer la nature du triangle $ABC$.

b) Soit $G$ le barycentre du système $\{(A;9),(B;-2),(C;6)\}$. Vérifier que $z_G = 2i$ puis placer $G$.

c) Déterminer et construire l'ensemble $E$ des points $M$ du plan tels que $9MA^2 - 2MB^2 + 6MC^2 = 195$.

d) Déterminer et construire l'ensemble $F$ des points $M$ du plan tels que $3MA^2 - 5MB^2 + 2MC^2 = 65$.

e) Préciser la position relative des deux ensembles $E$ et $F$.

**3)** Soit $f$ la transformation d'écriture complexe $z' = mz + (2 - 2m)i$ où $m$ est un nombre complexe.

a) Résoudre l'équation $z' = z$ (discuter suivant les valeurs de $m$).

b) Déterminer la valeur de $m$ pour que $f(B) = A$, puis caractériser $f$ dans ce cas.
""",
        "correction": r"""**1)** $P(-i) = i + (1 - 2i)(-1) + i(5 + 3i) + 4 - 8i = i - 1 + 2i + 5i - 3 + 4 - 8i = 0$.

$P(z) = (z + i)\big(z^2 + (1 - 3i)z - 8 - 4i\big)$ ; $\Delta = (1 - 3i)^2 + 4(8 + 4i) = 24 + 10i = (5 + i)^2$.

Racines $\dfrac{-1 + 3i \pm (5 + i)}{2}$ : $2 + 2i$ et $-3 + i$.

$S = \{\,-i \ ;\ 2 + 2i \ ;\ -3 + i\,\}$.

**2) a)** $|{-i}| = 1 < |2 + 2i| = 2\sqrt{2} < |{-3 + i}| = \sqrt{10}$ : $z_B = -i$, $z_A = 2 + 2i$, $z_C = -3 + i$.

$BA = |2 + 3i| = \sqrt{13}$, $BC = |{-3 + 2i}| = \sqrt{13}$, $AC = |{-5 - i}| = \sqrt{26}$ et $BA^2 + BC^2 = AC^2$ : $ABC$ est **rectangle isocèle en $B$**.

**b)** $z_G = \dfrac{9(2 + 2i) - 2(-i) + 6(-3 + i)}{13} = \dfrac{26i}{13} = 2i$.

**c)** $9MA^2 - 2MB^2 + 6MC^2 = 13MG^2 + 9GA^2 - 2GB^2 + 6GC^2$ avec $GA^2 = 4$, $GB^2 = 9$, $GC^2 = 10$ : $36 - 18 + 60 = 78$.

$13MG^2 + 78 = 195 \iff MG^2 = 9$ : $E$ est le **cercle de centre $G(0;2)$ et de rayon $3$**.

**d)** Somme des coefficients nulle. Avec $M(x;y)$, le calcul donne $3MA^2 - 5MB^2 + 2MC^2 = 39 - 26y$.

$39 - 26y = 65 \iff y = -1$ : $F$ est la **droite d'équation $y = -1$**.

**e)** La distance de $G(0;2)$ à $F$ vaut $3$, égale au rayon de $E$ : la droite $F$ est **tangente** au cercle $E$, au point $(0;-1)$, c'est-à-dire en $B$.

**3) a)** $z' = z \iff (m - 1)z = -(2 - 2m)i = 2(m - 1)i$.

- Si $m \neq 1$ : une seule solution $z = 2i$ (le point $G$) ;
- Si $m = 1$ : tout $z$ est solution ($f$ est l'identité).

**b)** $f(B) = A \iff -mi + (2 - 2m)i = 2 + 2i \iff -3mi = 2 \iff m = \dfrac{2i}{3}$.

$f : z' = \dfrac{2}{3}i\,z + \left(2 - \dfrac{4i}{3}\right)i$, et $\dfrac{2}{3}i = \dfrac{2}{3}e^{i\pi/2}$ : $f$ est la **similitude directe de centre $G(2i)$, de rapport $\dfrac{2}{3}$ et d'angle $\dfrac{\pi}{2}$**.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2021-sn-math-ex3": {
        "enonce": r"""Dans le plan complexe, muni d'un repère orthonormal direct $(O;\vec{u},\vec{v})$, on considère les points $A$ et $B$ d'affixes respectives $z_A = -2 - i$ et $z_B = -1 - 3i$.

**1) a)** Montrer que $\forall z \in \mathbb{C}$, on a : $-4z^2 - (12 + 16i)z + 7 - 24i = (2iz - 4 + 3i)^2$.

b) En déduire les solutions dans $\mathbb{C}$ de l'équation
$$(E) : z^2 - (2m + 2 + i)z + 2m^2 + (5 + 5i)m - 1 + 7i = 0,$$
où $m$ est un paramètre complexe.

**2)** Soit $S_1$ la similitude directe qui, à tout point $M$ d'affixe $m$, associe le point $M_1$ d'affixe $z_1 = (1 + i)m - 1 + 2i$ et soit $S_2$ la similitude directe qui, à tout point $M$ d'affixe $m$, associe le point $M_2$ d'affixe $z_2 = (1 - i)m + 3 - i$.

a) Donner les éléments caractéristiques de $S_1$ et $S_2$.

b) Montrer que $S_1 \circ S_2$ est une homothétie dont on donnera le rapport et le centre $C$.

c) Soit $R$ la transformation qui au point $M_1$ associe le point $M_2$, pour tout point $M$ du plan. Justifier que $R$ est une rotation dont on donnera une mesure de l'angle et l'affixe du centre $D$.

d) Placer les points $A$, $B$, $C$ et $D$ et déterminer la nature du triangle $ABD$.

**3)** Soit $\mathcal{E}$ l'ellipse de foyers $A$ et $B$ et dont $D$ est un sommet.

a) Déterminer le centre $I$ de $\mathcal{E}$ et justifier que la longueur du grand axe de $\mathcal{E}$ est $\sqrt{10}$.

b) Donner l'équation de $\mathcal{E}$.

c) Construire $\mathcal{E}$ après avoir placé ses sommets.
""",
        "correction": r"""**1) a)** $(2iz - 4 + 3i)^2 = -4z^2 + 2\cdot 2iz(-4 + 3i) + (-4 + 3i)^2 = -4z^2 - (12 + 16i)z + 7 - 24i$.

**b)** $\Delta = (2m + 2 + i)^2 - 4\big(2m^2 + (5+5i)m - 1 + 7i\big) = -4m^2 - (12 + 16i)m + 7 - 24i = (2im - 4 + 3i)^2$.

$z = \dfrac{2m + 2 + i \pm (2im - 4 + 3i)}{2}$, d'où les deux solutions
$$z_1 = (1 + i)m - 1 + 2i \quad\text{et}\quad z_2 = (1 - i)m + 3 - i.$$

**2) a)** $S_1$ : $1 + i = \sqrt{2}e^{i\pi/4}$, rapport $\sqrt{2}$, angle $\dfrac{\pi}{4}$ ; centre : $\omega = (1+i)\omega - 1 + 2i \iff i\omega = 1 - 2i \iff \omega = -2 - i$ : **centre $A$**.

$S_2$ : $1 - i = \sqrt{2}e^{-i\pi/4}$, rapport $\sqrt{2}$, angle $-\dfrac{\pi}{4}$ ; centre : $-i\omega = -3 + i \iff \omega = -1 - 3i$ : **centre $B$**.

**b)** $S_1 \circ S_2(m) = (1 + i)\big((1 - i)m + 3 - i\big) - 1 + 2i = 2m + 3 + 4i$.

C'est l'**homothétie de rapport $2$** et de centre $C$ tel que $c = 2c + 3 + 4i$, soit $z_C = -3 - 4i$.

**c)** $m = \dfrac{z_1 + 1 - 2i}{1 + i}$, donc $z_2 = \dfrac{1 - i}{1 + i}(z_1 + 1 - 2i) + 3 - i = -i(z_1 + 1 - 2i) + 3 - i$, soit
$$R : z_2 = -iz_1 + 1 - 2i.$$
$-i = e^{-i\pi/2}$ : **rotation d'angle $-\dfrac{\pi}{2}$**, de centre $D$ tel que $(1 + i)d = 1 - 2i$, soit $z_D = -\dfrac{1}{2} - \dfrac{3}{2}i$.

**d)** $\dfrac{z_A - z_D}{z_B - z_D} = \dfrac{-\frac{3}{2} + \frac{1}{2}i}{-\frac{1}{2} - \frac{3}{2}i} = -i$ : $DA = DB$ et $(\overrightarrow{DB}, \overrightarrow{DA}) = -\dfrac{\pi}{2}$. $ABD$ est **rectangle isocèle en $D$**.

**3) a)** Le centre est le milieu des foyers : $z_I = \dfrac{z_A + z_B}{2} = -\dfrac{3}{2} - 2i$.

$DA = DB$ : $D$ est sur la médiatrice de $[AB]$, c'est donc un sommet du petit axe. Pour tout point de $\mathcal{E}$, $MA + MB = 2a$ ; en $D$ : $2a = DA + DB = 2\left|-\tfrac{3}{2} + \tfrac{1}{2}i\right| = 2\cdot\dfrac{\sqrt{10}}{2} = \sqrt{10}$.

(On a $c = \dfrac{AB}{2} = \dfrac{\sqrt{5}}{2}$, $b = ID = \dfrac{\sqrt{5}}{2}$, $a = \dfrac{\sqrt{10}}{2}$, $e = \dfrac{\sqrt{2}}{2}$.)

**b)** $M \in \mathcal{E} \iff MA + MB = \sqrt{10}$. En élevant au carré deux fois :
$$36x^2 + 16xy + 24y^2 + 140x + 120y + 175 = 0.$$

(Dans le repère centré en $I$ porté par les axes de l'ellipse : $\dfrac{X^2}{5/2} + \dfrac{Y^2}{5/4} = 1$.)

**c)** Sommets du grand axe : $I \pm \dfrac{\sqrt{2}}{2}(1 - 2i)$, soit $\left(-\frac{3}{2} \pm \frac{\sqrt{2}}{2} ; -2 \mp \sqrt{2}\right)$ ; sommets du petit axe : $D\left(-\frac{1}{2};-\frac{3}{2}\right)$ et $D'\left(-\frac{5}{2};-\frac{5}{2}\right)$.
""",
        "note": "Le texte OCR indiquait « grand axe 10 » : il s'agit de √10 (racine perdue à la conversion).",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2022-sn-math-ex2": {
        "enonce": r"""**1)** Soit $P(z) = z^3 - (5 + 6i)z^2 + (-6 + 16i)z + 20 + 10i$, $z \in \mathbb{C}$.

a) Calculer $P(-1 + i)$ puis déterminer les complexes $a$ et $b$ tels que $P(z) = (z + 1 - i)(z^2 + az + b)$.

b) En déduire les solutions de l'équation $P(z) = 0$. On notera $z_1$, $z_2$ et $z_3$ les solutions de cette équation avec $|z_1| < |z_2| < |z_3|$.

**2)** Dans le plan complexe, muni d'un repère orthonormal direct $(O;\vec{u},\vec{v})$, on considère les points $A$, $B$ et $C$ d'affixes respectives $z_1$, $z_2$ et $z_3$.

a) Placer les points $A$, $B$, $C$ et $I$, où $I$ est le milieu du segment $[AB]$.

b) Soit $D$ le barycentre du système $\{(A;3),(B;1)\}$. Vérifier que $z_D = i$ et placer $D$.

**3)** Soit $H$ l'hyperbole de foyers $A$ et $B$ dont $D$ est un sommet.

a) Déterminer le centre et l'excentricité de $H$.

b) Vérifier que l'équation réduite de $H$ dans le repère $(O;\vec{u},\vec{v})$ s'écrit $(x - 1)^2 - \dfrac{(y - 1)^2}{3} = 1$.

c) Déterminer le 2e sommet, les directrices et les asymptotes de l'hyperbole $H$ et la construire.
""",
        "correction": r"""**1) a)** $(-1 + i)^2 = -2i$, $(-1 + i)^3 = 2 + 2i$.
$P(-1 + i) = 2 + 2i + 2i(5 + 6i) + (-6 + 16i)(-1 + i) + 20 + 10i = 2 + 2i + 10i - 12 + 6 - 22i - 16 + 20 + 10i = 0$.

Par identification : $a = -6 - 5i$, $b = 5 + 15i$.

**b)** $z^2 - (6 + 5i)z + 5 + 15i = 0$ : $\Delta = (6 + 5i)^2 - 4(5 + 15i) = -9 = (3i)^2$, d'où $z = \dfrac{6 + 5i \pm 3i}{2}$ : $3 + 4i$ et $3 + i$.

$|{-1 + i}| = \sqrt{2} < |3 + i| = \sqrt{10} < |3 + 4i| = 5$ : $z_1 = -1 + i$, $z_2 = 3 + i$, $z_3 = 3 + 4i$.

**2) a)** $A(-1;1)$, $B(3;1)$, $C(3;4)$, $I(1;1)$.

**b)** $z_D = \dfrac{3(-1 + i) + (3 + i)}{4} = \dfrac{4i}{4} = i$.

**3) a)** Le centre est le milieu des foyers : $I(1;1)$. $c = IA = 2$ ; $D(0;1)$ est sur l'axe focal $y = 1$, donc $a = ID = 1$. $e = \dfrac{c}{a} = 2$.

**b)** $b^2 = c^2 - a^2 = 3$, axe focal horizontal : $(x - 1)^2 - \dfrac{(y - 1)^2}{3} = 1$.

**c)** 2e sommet : symétrique de $D$ par rapport à $I$, soit $(2;1)$.
Directrices : $x = 1 \pm \dfrac{a^2}{c} = 1 \pm \dfrac{1}{2}$, soit $x = \dfrac{1}{2}$ et $x = \dfrac{3}{2}$.
Asymptotes : $y - 1 = \pm\sqrt{3}(x - 1)$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2023-sc-math-ex4": {
        "enonce": r"""**1)** Soit $P(z) = z^3 - 4iz^2 - 6z + 4i$ où $z$ est un nombre complexe.

a) Calculer $P(2i)$ puis résoudre dans $\mathbb{C}$ l'équation $P(z) = 0$. On notera $z_0$, $z_1$ et $z_2$ les solutions de cette équation avec $\operatorname{Re}(z_1) > \operatorname{Re}(z_0) > \operatorname{Re}(z_2)$.

b) Écrire sous forme exponentielle chacun des trois complexes $z_0$, $z_1$ et $z_2$.

c) En déduire les solutions de l'équation $\left(\dfrac{z - i}{z + i}\right)^3 - 4i\left(\dfrac{z - i}{z + i}\right)^2 - 6\,\dfrac{z - i}{z + i} + 4i = 0$.

**2)** Dans le plan complexe muni d'un repère orthonormé direct $(O;\vec{u},\vec{v})$, on note $A$, $B$, $C$ et $D$ les points d'affixes respectives $z_A = z_1$, $z_B = z_0$, $z_C = z_2$ et $z_D = 1$ ($z_0$, $z_1$ et $z_2$ sont ceux définis au-dessus).

a) Préciser les affixes des points $A$, $B$ et $C$ puis déterminer la nature du triangle $ABC$.

b) Déterminer l'écriture complexe de la similitude directe $S$ de centre $A$ telle que $S(B) = C$.

**3)** Soit $(M_n)$ la suite des points définie par $M_0 = B$ et $\forall n \in \mathbb{N}$, $M_{n+1} = S(M_n)$.

a) Montrer que $\forall n \in \mathbb{N}$, le triangle $AM_nM_{n+1}$ est rectangle isocèle direct en $M_n$.

b) Montrer que $\forall n \in \mathbb{N}$, les points $A$, $M_n$ et $M_{n+4}$ sont alignés et que $M_{2023} \in (AD)$.
""",
        "correction": r"""**1) a)** $P(2i) = -8i + 16i - 12i + 4i = 0$.

$P(z) = (z - 2i)(z^2 - 2iz - 2)$ ; $\Delta' = (-i)^2 + 2 = 1$, d'où $z = i \pm 1$.

$S = \{\,2i \ ;\ 1 + i \ ;\ -1 + i\,\}$, et avec l'ordre imposé : $z_1 = 1 + i$, $z_0 = 2i$, $z_2 = -1 + i$.

**b)** $z_0 = 2e^{i\pi/2}$, $z_1 = \sqrt{2}e^{i\pi/4}$, $z_2 = \sqrt{2}e^{3i\pi/4}$.

**c)** Pour $z \neq -i$, posons $Z = \dfrac{z - i}{z + i}$ : l'équation s'écrit $P(Z) = 0$, donc $Z \in \{2i ; 1 + i ; -1 + i\}$. Comme $Z \neq 1$, on inverse : $z = \dfrac{i(1 + Z)}{1 - Z}$.

- $Z = 2i$ : $z = \dfrac{i(1 + 2i)}{1 - 2i} = -\dfrac{4}{5} - \dfrac{3}{5}i$ ;
- $Z = 1 + i$ : $z = \dfrac{i(2 + i)}{-i} = -2 - i$ ;
- $Z = -1 + i$ : $z = \dfrac{i\cdot i}{2 - i} = -\dfrac{2}{5} - \dfrac{1}{5}i$.

$S = \left\{-\dfrac{4}{5} - \dfrac{3}{5}i \ ;\ -2 - i \ ;\ -\dfrac{2}{5} - \dfrac{1}{5}i\right\}$.

**2) a)** $z_A = 1 + i$, $z_B = 2i$, $z_C = -1 + i$.

$\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{-1 - i}{1 - i} = -i$ : $BA = BC$ et $(\overrightarrow{BA}, \overrightarrow{BC}) = -\dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $B$**.

**b)** $S : z' - z_A = a(z - z_A)$ avec $a = \dfrac{z_C - z_A}{z_B - z_A} = \dfrac{-2}{-1 + i} = 1 + i$.

$z' = (1 + i)(z - 1 - i) + 1 + i$, soit $\boxed{z' = (1 + i)z + 1 - i}$ (rapport $\sqrt{2}$, angle $\frac{\pi}{4}$).

**3) a)** Posons $u = z_n - z_A$. Alors $z_{n+1} - z_A = (1 + i)u$, donc $z_{n+1} - z_n = iu$ et $z_A - z_n = -u$.

$\dfrac{z_A - z_n}{z_{n+1} - z_n} = \dfrac{-u}{iu} = i$ : $M_nA = M_nM_{n+1}$ et $(\overrightarrow{M_nM_{n+1}}, \overrightarrow{M_nA}) = \dfrac{\pi}{2}$. Le triangle $AM_nM_{n+1}$ est rectangle isocèle direct en $M_n$.

**b)** $z_{n+4} - z_A = (1 + i)^4(z_n - z_A) = -4(z_n - z_A)$ : réel, donc $A$, $M_n$, $M_{n+4}$ sont alignés.

Par récurrence, $M_{4k+3} \in (AM_3)$. $z_3 - z_A = (1 + i)^3(z_B - z_A) = (-2 + 2i)(-1 + i) = -4i$, d'où $z_3 = 1 - 3i$.

$z_D - z_A = -i$ et $z_3 - z_A = -4i$ sont colinéaires : $M_3 \in (AD)$. Comme $2023 = 4 \times 505 + 3$, $M_{2023} \in (AM_3) = (AD)$.
""",
        "note": "Énoncé corrigé depuis le scan : P(z) = z³ − 4iz² − 6z + 4i, ordre Re(z₁) > Re(z₀) > Re(z₂), "
                "équation du 1c, z_B = z₀, z_C = z₂, z_D = 1 et M_{n+4} au 3b.",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2023-sn-math-ex3": {
        "enonce": r"""**I.** Soit $m$ un nombre complexe non nul. Pour tout nombre complexe $z$, on note
$$P(z) = 2z^3 - (4 - 2i + 2m)z^2 + \big(m^2 + (3 - i)m + 2 - 3i\big)z - (m + 1)(m - i).$$

**1)** Résoudre, dans $\mathbb{C}$, l'équation $2z^2 - 2(1 - i + m)z + (m + 1)(m - i) = 0$.

**2)** Calculer $P(1)$ et en déduire les solutions, dans $\mathbb{C}$, de l'équation $P(z) = 0$.

**II.** Le plan complexe est muni d'un repère orthonormal direct $(O;\vec{u},\vec{v})$. On considère les points $A$, $B$, $C$, $M$, $M_1$ et $M_2$ d'affixes respectives
$z_A = 1$, $z_B = -i$, $z_C = 1 - i$, $z_M = m$, $z_{M_1} = z_1 = \dfrac{(1 - i)(1 + m)}{2}$ et $z_{M_2} = z_2 = \dfrac{(1 - i)(1 + im)}{2}$.

**1)** Préciser les transformations $f$ et $g$ telles que, pour tout $m \in \mathbb{C}^*$, $f(M) = M_1$ et $g(M) = M_2$.

**2)** Montrer que $z_2 = iz_1 - i$ et en déduire que $M_2 = R(M_1)$ où $R$ est une rotation à préciser.

**3)** On suppose, dans cette question, que $M$ décrit le cercle de diamètre $[AB]$ privé de $O$.

a) Déterminer le lieu géométrique du point $M_1$.

b) Justifier que, si $m \neq -i$, alors $\dfrac{z_2 - m}{z_1 - m} = -i\,\dfrac{m - 1}{i + m}$ puis en déduire que les points $M$, $M_1$ et $M_2$ sont alignés.

**4)** On considère la parabole $\mathcal{P}$ de directrice $(OB)$ et de foyer $A$.

a) Déterminer le paramètre $p$ et le sommet $S$ de $\mathcal{P}$.

b) Justifier que l'équation réduite de $\mathcal{P}$ s'écrit $y^2 = 2x - 1$ puis construire $\mathcal{P}$.

c) Donner une équation de la tangente à $\mathcal{P}$ au point $C$.
""",
        "correction": r"""**I. 1)** $\Delta' = (1 - i + m)^2 - 2(m + 1)(m - i) = -m^2 = (im)^2$.

$z = \dfrac{(1 - i + m) \pm im}{2}$ : $z_1 = \dfrac{1 - i + (1 - i)m}{2} = \dfrac{(1 - i)(1 + m)}{2}$ et $z_2 = \dfrac{1 - i + (1 + i)m}{2} = \dfrac{(1 - i)(1 + im)}{2}$.

**2)** $P(1) = 2 - 4 + 2i - 2m + m^2 + 3m - im + 2 - 3i - (m^2 - im + m - i) = 0$.

On vérifie que $P(z) = (z - 1)\big(2z^2 - 2(1 - i + m)z + (m + 1)(m - i)\big)$, donc les solutions de $P(z) = 0$ sont $1$, $z_1$ et $z_2$.

**II. 1)** $f : z' = \dfrac{1 - i}{2}z + \dfrac{1 - i}{2}$, avec $\dfrac{1 - i}{2} = \dfrac{\sqrt{2}}{2}e^{-i\pi/4}$. Centre : $\omega = \dfrac{(1-i)/2}{(1+i)/2} = -i$.
$f$ est la **similitude directe de centre $B$, de rapport $\dfrac{\sqrt{2}}{2}$ et d'angle $-\dfrac{\pi}{4}$**.

$g : z' = \dfrac{1 + i}{2}z + \dfrac{1 - i}{2}$, avec $\dfrac{1 + i}{2} = \dfrac{\sqrt{2}}{2}e^{i\pi/4}$. Centre : $\omega\,\dfrac{1 - i}{2} = \dfrac{1 - i}{2}$, soit $\omega = 1$.
$g$ est la **similitude directe de centre $A$, de rapport $\dfrac{\sqrt{2}}{2}$ et d'angle $\dfrac{\pi}{4}$**.

**2)** $iz_1 - i = \dfrac{(1 + i)(1 + m)}{2} - i = \dfrac{1 - i + (1 + i)m}{2} = z_2$.

$R : z' = iz - i$ est la **rotation d'angle $\dfrac{\pi}{2}$** et de centre $\omega$ tel que $(1 - i)\omega = -i$, soit $\omega = \dfrac{1 - i}{2}$ (milieu de $[AB]$).

**3) a)** Le cercle de diamètre $[AB]$ a pour centre $K\left(\frac{1}{2};-\frac{1}{2}\right)$ et pour rayon $\frac{\sqrt{2}}{2}$ ; il passe par $O$.
Son image par $f$ est le cercle de centre $f(K)$, $z_{f(K)} = \dfrac{1-i}{2}\cdot\dfrac{1-i}{2} + \dfrac{1-i}{2} = \dfrac{1}{2} - i$, et de rayon $\dfrac{\sqrt{2}}{2}\times\dfrac{\sqrt{2}}{2} = \dfrac{1}{2}$.

Le lieu de $M_1$ est le **cercle de centre $\left(\frac{1}{2};-1\right)$ et de rayon $\frac{1}{2}$, privé du point $f(O)$ d'affixe $\frac{1 - i}{2}$**.

**b)** $z_1 - m = \dfrac{(1 - i) - (1 + i)m}{2} = \dfrac{-(1 + i)(m + i)}{2}$ et $z_2 - m = \dfrac{(1 - i)(1 - m)}{2}$.

$\dfrac{z_2 - m}{z_1 - m} = -\dfrac{1 - i}{1 + i}\cdot\dfrac{1 - m}{m + i} = -(-i)\cdot\dfrac{-(m - 1)}{m + i} = -i\,\dfrac{m - 1}{i + m}$.

Si $M$ est sur le cercle de diamètre $[AB]$ ($M \neq B$), $\dfrac{m - 1}{m + i} = \dfrac{z_M - z_A}{z_M - z_B}$ est imaginaire pur (ou nul si $M = A$). Donc $-i\,\dfrac{m - 1}{m + i}$ est réel : $M$, $M_1$ et $M_2$ sont **alignés**.

**4) a)** La directrice $(OB)$ est l'axe des ordonnées $x = 0$ et le foyer est $A(1;0)$ : $p = d(A, (OB)) = 1$ et le sommet est le milieu de $A$ et de $O$ : $S\left(\frac{1}{2};0\right)$.

**b)** $M \in \mathcal{P} \iff MA^2 = x^2 \iff (x - 1)^2 + y^2 = x^2 \iff y^2 = 2x - 1$.

**c)** $C(1;-1)$ : $(-1)^2 = 2 - 1$, donc $C \in \mathcal{P}$. En dérivant $y^2 = 2x - 1$ : $2yy' = 2$, pente $\dfrac{1}{y_C} = -1$.

Tangente en $C$ : $y + 1 = -(x - 1)$, soit $y = -x$.
""",
        "note": "Énoncé corrigé depuis le scan : g(M) = M₂, z₂ = iz₁ − i, rapport −i(m − 1)/(i + m) "
                "et alignement de M, M₁, M₂.",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2024-sc-math-ex4": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$. On considère l'équation $(E) : z^2 - 4z + 4(1 + \cos^2\alpha) = 0$, avec $\alpha \in \left]0;\dfrac{\pi}{2}\right[$.

**1)** Résoudre, dans $\mathbb{C}$, l'équation $(E)$ (on note $z_1$ et $z_2$ les solutions de cette équation avec $\operatorname{Im}(z_1) > \operatorname{Im}(z_2)$).

**2)** Dans la suite de l'exercice, on suppose que $\alpha = \dfrac{\pi}{3}$ et on considère les points $A$, $B$, $C$ et $D$ d'affixes respectives $z_A = z_1$, $z_B = z_2$, $z_C = 5 + 2i$ et $z_D = -1 - 2i$.

a) Déterminer, suivant les valeurs du réel $k$, l'ensemble $\Gamma_k$ des points $M$ du plan tels que $2MO^2 + MA^2 - MB^2 = k$.

b) Déterminer l'ensemble $\Delta$ des points $M$ du plan tels que $2MO^2 - MA^2 - MB^2 = -10$.

**3)** Soient $a$, $b$ et $c$ trois réels et $H$ l'hyperbole d'équation $x^2 + ay^2 + bx + c = 0$ qui passe par les points $A$, $C$ et $D$.

a) Montrer que le triplet $(a,b,c)$ vérifie le système $\begin{cases} a + 2b + c = -4 \\ 4a + 5b + c = -25 \\ 4a - b + c = -1 \end{cases}$

b) Résoudre le système et donner l'équation réduite de $H$.

c) Déterminer le centre, les sommets, l'excentricité et les asymptotes de $H$.
""",
        "correction": r"""**1)** $\Delta' = 4 - 4(1 + \cos^2\alpha) = -4\cos^2\alpha = (2i\cos\alpha)^2$.

$z_1 = 2 + 2i\cos\alpha$ et $z_2 = 2 - 2i\cos\alpha$ (avec $\cos\alpha > 0$ sur $\left]0;\frac{\pi}{2}\right[$).

**2)** Pour $\alpha = \dfrac{\pi}{3}$ : $z_A = 2 + i$, $z_B = 2 - i$.

**a)** Les coefficients $2$, $1$, $-1$ ont pour somme $2$. Le barycentre $G$ de $\{(O;2),(A;1),(B;-1)\}$ a pour affixe $\dfrac{(2 + i) - (2 - i)}{2} = i$.

$2MO^2 + MA^2 - MB^2 = 2MG^2 + 2GO^2 + GA^2 - GB^2 = 2MG^2 + 2 + 4 - 8 = 2MG^2 - 2$.

$\Gamma_k$ : $MG^2 = \dfrac{k + 2}{2}$.
- $k < -2$ : $\Gamma_k = \varnothing$ ;
- $k = -2$ : $\Gamma_k = \{G\}$ ;
- $k > -2$ : $\Gamma_k$ est le cercle de centre $G(0;1)$ et de rayon $\sqrt{\dfrac{k + 2}{2}}$.

**b)** Somme des coefficients nulle. Avec $M(x;y)$ :
$2(x^2 + y^2) - \big[(x - 2)^2 + (y - 1)^2\big] - \big[(x - 2)^2 + (y + 1)^2\big] = 8x - 10$.

$8x - 10 = -10 \iff x = 0$ : $\Delta$ est l'**axe des ordonnées** (droite $x = 0$).

**3) a)** $A(2;1) \in H$ : $4 + a + 2b + c = 0$ ; $C(5;2) \in H$ : $25 + 4a + 5b + c = 0$ ; $D(-1;-2) \in H$ : $1 + 4a - b + c = 0$. D'où le système.

**b)** (2) − (3) : $6b = -24$, $b = -4$. (1) : $a + c = 4$ ; (3) : $4a + c = -5$, d'où $3a = -9$, $a = -3$ et $c = 7$.

$H : x^2 - 3y^2 - 4x + 7 = 0 \iff (x - 2)^2 - 3y^2 = -3 \iff \dfrac{y^2}{1} - \dfrac{(x - 2)^2}{3} = 1$.

**c)** Centre $\Omega(2;0)$, axe focal vertical $x = 2$, $a = 1$, $b = \sqrt{3}$, $c = 2$.
Sommets : $(2;1) = A$ et $(2;-1) = B$. Foyers $(2;\pm 2)$. Excentricité $e = \dfrac{c}{a} = 2$.
Asymptotes : $y = \pm\dfrac{x - 2}{\sqrt{3}}$.
""",
        "note": "Énoncé corrigé depuis le scan : α ∈ ]0 ; π/2[ (intervalle ouvert).",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2024-sn-math-ex3": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{i},\vec{j})$. Pour tout nombre complexe $z$ on pose $P(z) = z^3 - (2 + 2i)z^2 + 11z + 38 + 8i$.

**1) a)** Calculer $P(-2)$ puis déterminer les complexes $a$ et $b$ tels que $P(z) = (z + 2)(z^2 + az + b)$.

b) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$. On note $z_1$, $z_2$ et $z_3$ les solutions de cette équation avec $\operatorname{Im}(z_1) > \operatorname{Im}(z_2) > \operatorname{Im}(z_3)$.

**2)** On considère les points $A$, $B$ et $C$ d'affixes respectives $z_1$, $z_2$ et $z_3$.

a) Placer les points $A$, $B$ et $C$.

b) Montrer que le point $D$ d'affixe $6$ est le barycentre de $\{(A,3);(B,-4);(C,5)\}$.

**3)** On définit l'ellipse $\mathcal{E}$ dont $A$ et $B$ sont deux sommets et dont $C$ est un foyer.

a) Reconnaître l'axe focal de $\mathcal{E}$ et en déduire que $D$ est un 3e sommet de $\mathcal{E}$.

b) Préciser le centre et le 4e sommet de $\mathcal{E}$.

c) Justifier que $\dfrac{(x - 2)^2}{16} + \dfrac{y^2}{25} = 1$ est une équation de $\mathcal{E}$, puis construire $\mathcal{E}$.
""",
        "correction": r"""**1) a)** $P(-2) = -8 - 4(2 + 2i) - 22 + 38 + 8i = -8 - 8 - 8i - 22 + 38 + 8i = 0$.

Par identification : $a = -4 - 2i$ et $b = 19 + 4i$, donc $P(z) = (z + 2)\big(z^2 - (4 + 2i)z + 19 + 4i\big)$.

**b)** $\Delta = (4 + 2i)^2 - 4(19 + 4i) = 12 + 16i - 76 - 16i = -64 = (8i)^2$, d'où $z = \dfrac{4 + 2i \pm 8i}{2}$ : $2 + 5i$ et $2 - 3i$.

$z_1 = 2 + 5i$, $z_2 = -2$, $z_3 = 2 - 3i$.

**2) a)** $A(2;5)$, $B(-2;0)$, $C(2;-3)$.

**b)** $\dfrac{3(2 + 5i) - 4(-2) + 5(2 - 3i)}{3 - 4 + 5} = \dfrac{6 + 15i + 8 + 10 - 15i}{4} = \dfrac{24}{4} = 6$.

**3) a)** Le foyer $C$ et le sommet $A$ ont même abscisse $2$. Le sommet $B$ n'est pas sur la droite $x = 2$ ; le foyer est sur l'axe focal, et si $B$ était sur l'axe focal, celui-ci serait $(BC)$ qui ne contient pas $A$. Donc l'axe focal est la droite $(AC)$ : $x = 2$, et $A$ est un sommet du grand axe, $B$ un sommet du petit axe.

Le centre est le projeté de $B$ sur l'axe focal : $\Omega(2;0)$. Le symétrique de $B(-2;0)$ par rapport à $\Omega$ est $(6;0) = D$ : $D$ est le 3e sommet.

**b)** Centre $\Omega(2;0)$ ; 4e sommet : symétrique de $A$ par rapport à $\Omega$, soit $(2;-5)$.

**c)** $a = \Omega A = 5$ (vertical), $b = \Omega B = 4$, donc $\mathcal{E} : \dfrac{(x - 2)^2}{16} + \dfrac{y^2}{25} = 1$.

Vérification : $c = \sqrt{25 - 16} = 3$, foyers $(2;\pm 3)$ : $C(2;-3)$ est bien un foyer. Excentricité $e = \dfrac{3}{5}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-c-2025-sn-math-ex2": {
        "enonce": r"""On considère dans $\mathbb{C}$ le polynôme $P$ défini pour tout $\alpha \in \left]-\dfrac{\pi}{2};\dfrac{\pi}{2}\right[$ par
$$P(z) = z^3 - (6 + 4i\sin\alpha)z^2 + (8 + 16i\sin\alpha)z - 16i\sin\alpha.$$

**1)** Résoudre dans $\mathbb{C}$ l'équation $P(z) = 0$, sachant qu'elle admet une solution réelle $z_0$.

**2)** Dans le plan complexe muni du repère orthonormé direct $(O;\vec{u},\vec{v})$, on considère les points $A$, $M_1$ et $M_2$ d'affixes respectives $z_0$, $z_1 = 2 + 2e^{i\alpha}$ et $z_2 = 2 - 2e^{-i\alpha}$. On note $G = \operatorname{bar}\{(A;-12),(M_1;21),(M_2;3)\}$.

a) Justifier que $z_2 = 2 - e^{-2i\alpha}(z_1 - 2)$ puis caractériser la rotation $R$ qui transforme $M_1$ en $M_2$ pour tout $\alpha \in \left]-\dfrac{\pi}{2};\dfrac{\pi}{2}\right[$.

b) Déterminer $\alpha$ pour que le triangle $AM_1M_2$ soit équilatéral.

c) Montrer que, si $\alpha$ varie, les points $M_1$ et $M_2$ restent sur un même cercle à préciser.

d) Montrer que, si $\alpha$ varie, la droite $(M_1M_2)$ conserve une direction fixe.

e) Vérifier que l'affixe du point $G$ est $z_G = 2 + 3\cos\alpha + 4i\sin\alpha$. Justifier que $G$ reste sur une ellipse dont on donnera l'équation réduite et l'excentricité.
""",
        "correction": r"""**1)** Notons $s = \sin\alpha$. Pour $z = x$ réel, la partie imaginaire de $P(x)$ vaut $s(-4x^2 + 16x - 16) = -4s(x - 2)^2$ et la partie réelle $x^3 - 6x^2 + 8x = x(x - 2)(x - 4)$ : $x = 2$ annule les deux, donc $z_0 = 2$.

$P(z) = (z - 2)\big(z^2 - (4 + 4is)z + 8is\big)$.

Les nombres $2 + 2e^{i\alpha}$ et $2 - 2e^{-i\alpha}$ ont pour somme $4 + 2(e^{i\alpha} - e^{-i\alpha}) = 4 + 4is$ et pour produit $4 + 4e^{i\alpha} - 4e^{-i\alpha} - 4 = 8is$ : ce sont les racines du trinôme.

$S = \{\,2 \ ;\ 2 + 2e^{i\alpha} \ ;\ 2 - 2e^{-i\alpha}\,\}$.

**2) a)** $z_1 - 2 = 2e^{i\alpha}$, donc $-e^{-2i\alpha}(z_1 - 2) = -2e^{-i\alpha} = z_2 - 2$.

$z_2 - 2 = e^{i(\pi - 2\alpha)}(z_1 - 2)$ : $R$ est la **rotation de centre $A(2)$ et d'angle $\pi - 2\alpha$**.

**b)** $AM_1 = AM_2 = 2$ ; le triangle est équilatéral si et seulement si $\pi - 2\alpha \equiv \pm\dfrac{\pi}{3}\ [2\pi]$. Avec $\alpha \in \left]-\frac{\pi}{2};\frac{\pi}{2}\right[$ (donc $\pi - 2\alpha \in \,]0;2\pi[$) : $\pi - 2\alpha = \dfrac{\pi}{3}$ ou $\dfrac{5\pi}{3}$, soit $\alpha = \dfrac{\pi}{3}$ ou $\alpha = -\dfrac{\pi}{3}$.

**c)** $|z_1 - 2| = |z_2 - 2| = 2$ : $M_1$ et $M_2$ restent sur le **cercle de centre $A(2;0)$ et de rayon $2$**.

**d)** $z_1 - z_2 = 2(e^{i\alpha} + e^{-i\alpha}) = 4\cos\alpha$, réel non nul : $(M_1M_2)$ est toujours **parallèle à l'axe des abscisses**.

**e)** $z_G = \dfrac{-12\cdot 2 + 21(2 + 2e^{i\alpha}) + 3(2 - 2e^{-i\alpha})}{12} = \dfrac{24 + 42e^{i\alpha} - 6e^{-i\alpha}}{12} = 2 + 3\cos\alpha + 4i\sin\alpha$.

$x - 2 = 3\cos\alpha$, $y = 4\sin\alpha$, donc
$$\frac{(x - 2)^2}{9} + \frac{y^2}{16} = 1.$$

$G$ est sur l'ellipse de centre $(2;0)$, grand axe vertical : $a = 4$, $b = 3$, $c = \sqrt{7}$, $e = \dfrac{\sqrt{7}}{4}$. (Comme $\cos\alpha > 0$, $G$ décrit la demi-ellipse $x > 2$.)
""",
    },
}


# Avertissements du contrôle (scripts/check_content.py) relus à la main et acceptés.
ACCEPTED: dict[str, list[str]] = {
    # 4 c) est traitée avant 4 b) : le tracé de P et P' utilise leurs équations (dit dans la correction).
    "bac-c-2016-sc-math-ex1": ["sous-questions ['a', 'c', 'b']"],
}
