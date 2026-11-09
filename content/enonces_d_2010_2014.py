"""Énoncés des sujets de maths série D 2010-2014.

2011-2014 : cases vides en base (ou texte d'un autre sujet). 2010 : texte OCR en
base, remplacé par la transcription vérifiée (``replace_ocr``).

Retranscrits à la main depuis les PDF originaux de
drive_archive/annals/Sujets corrigés math/bac d/ (texte PDF illisible : polices
mal encodées, donc lecture de l'image de chaque page). Chaque exercice reçoit
aussi son chapitre.

Chargé par scripts/load_enonces.py (brouillon : rien n'est validé).
"""

ENONCES: dict[str, dict] = {}


def _add(eid: str, chapitre: str, enonce: str, chapitres: list[str] | None = None, note: str = "",
         replace_ocr: bool = False) -> None:
    assert eid not in ENONCES, eid
    ENONCES[eid] = {"chapitre": chapitre, "chapitres": chapitres or [], "enonce": enonce.strip(), "note": note,
                    "replace_ocr": replace_ocr}


# ═══════════════════════════════════ 2011 — session normale ═══════════════════

_add("bac-d-2011-sn-math-ex1", "Probabilités", r"""
**Exercice 1 (3 points)**

Un groupe d'élèves est composé de 3 garçons et de 4 filles. Les noms de ces sept élèves sont inscrits sur des jetons indiscernables au toucher et placés dans une enveloppe.

À chaque cours de mathématiques, le professeur tire au hasard un jeton et interroge l'élève concerné. Durant une semaine, il y a 6 cours de mathématiques. On appelle $X$ la variable aléatoire définie par « $X$ est égale au nombre de fois où le professeur interroge une fille durant cette semaine ». On considère les événements :

$A$ : « Le professeur interroge exactement cinq garçons. »

$B$ : « Une fille au moins est interrogée durant la semaine. »

Parmi les réponses proposées pour chaque question ci-après, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | La probabilité, à un cours donné, que l'élève interrogé soit un garçon est : | $\dfrac{3}{7}$ | $C_7^3$ | $A_7^3$ |
| 2 | La probabilité, à un cours donné, que l'élève interrogé soit une fille est : | $\dfrac{1}{2}$ | $\dfrac{4}{3}$ | $\dfrac{4}{7}$ |
| 3 | L'ensemble des valeurs de $X$ est : | $\{0,1,2,\dots,7\}$ | $\{0,1,2,\dots,6\}$ | $\{0,1,2,3,4\}$ |
| 4 | La probabilité de l'événement $A$ est : | $\left(\dfrac{3}{7}\right)^5$ | $C_6^5\left(\dfrac{3}{7}\right)^5\left(\dfrac{4}{7}\right)$ | $\left(\dfrac{4}{7}\right)^5\left(\dfrac{3}{7}\right)$ |
| 5 | La probabilité de l'événement $B$ est : | $1 - \left(\dfrac{3}{7}\right)^6$ | $1 - \left(\dfrac{4}{7}\right)^5$ | $\dfrac{4}{7}$ |
| 6 | Le nombre de filles interrogées durant la semaine que l'on peut espérer est : | $2$ | $3$ | $4$ |

Recopie sur la feuille et complète le tableau suivant en choisissant la bonne réponse.

| Question | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""")

_add("bac-d-2011-sn-math-ex2", "Nombres complexes", r"""
**Exercice 2 (5 points)**

**1.** On pose $p(z) = z^3 - 5z^2 + 12z - 8$.

a) Calculer $p(1)$.

b) Déterminer $a$ et $b$ tels que pour tout $z$ on a $p(z) = (z - 1)(z^2 + az + b)$.

c) Résoudre dans $\mathbb{C}$ l'équation $p(z) = 0$.

**2.** On considère le plan complexe rapporté à un repère orthonormal $(O;\vec{u},\vec{v})$. Soient les points $A$, $B$ et $C$ d'affixes respectives $z_1 = 1$, $z_2 = 2 + 2i$ et $z_3 = 2 - 2i$.

a) Calculer le module et un argument de chacun des nombres $z_1$, $z_2$ et $z_3$.

b) Placer les points $A$, $B$ et $C$ dans le repère $(O;\vec{u},\vec{v})$.

**3. a)** Écrire le nombre $\dfrac{z_2}{z_3}$ sous forme algébrique. En déduire la nature du triangle $OBC$.

b) Déterminer et représenter l'ensemble $\Gamma$ des points $M$ d'affixe $z$ tels que $\left|\dfrac{z - 1}{z - 2 - 2i}\right| = 1$.
""")

_add("bac-d-2011-sn-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (x + 2)e^x$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$, unité 1 cm.

**1.** Calculer $\lim\limits_{x \to -\infty} f(x)$, $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

**2.** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

**3.** Déterminer les points d'intersection de $(C)$ avec les axes des coordonnées puis construire $(C)$ dans le repère $(O;\vec{i},\vec{j})$.

**4. a)** Vérifier que pour tout réel $x$ on a : $f'(x) = f(x) + e^x$. En déduire une primitive de $f$ sur $\mathbb{R}$.

b) Calculer l'aire $S$ du domaine plan délimité par la courbe $(C)$ et les axes des coordonnées.

**5.** On définit une suite numérique $(U_n)$ par son terme général : $U_n = f\left(\dfrac{1}{n}\right)$, $n \ge 1$.

a) Calculer $U_1$ et $U_2$. Montrer que $(U_n)$ est décroissante (on pourra utiliser les variations de $f$).

b) Calculer $\lim\limits_{n \to +\infty} U_n$.
""")

_add("bac-d-2011-sn-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = x - 1 + \dfrac{1 + \ln x}{x}$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$, unité 1 cm.

**1. a)** Montrer que $\lim\limits_{x \to 0^+} f(x) = -\infty$ et interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$. Montrer que la droite $\Delta$ d'équation $y = x - 1$ est asymptote à la courbe $(C)$.

c) Étudier la position relative de $(C)$ et $\Delta$.

**2.** On considère la fonction $g$ définie sur $]0;+\infty[$ par $g(x) = x^2 - \ln x$.

a) Vérifier que $g\left(\dfrac{1}{\sqrt{2}}\right) = \dfrac{1 + \ln 2}{2}$.

b) Calculer $g'(x)$.

c) Étudier les variations de $g$ et montrer que pour tout $x$ de $]0;+\infty[$ : $g(x) > 0$.

**3. a)** Calculer $f'(x)$ et vérifier que pour tout $x$ de $]0;+\infty[$ on a : $f'(x) = \dfrac{g(x)}{x^2}$.

b) Dresser le tableau de variation de $f$.

**4. a)** Montrer que $f$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$. Vérifier que $\dfrac{1}{e} < \alpha < \dfrac{1}{2}$.

**5. a)** Préciser les points de la courbe $(C)$ en lesquels la tangente $(T)$ est parallèle à $\Delta$.

b) Représenter la courbe $(C)$ et les droites $\Delta$ et $(T)$ dans $(O;\vec{i},\vec{j})$.

c) Discuter graphiquement, suivant les valeurs du paramètre $m$, le nombre de solutions de l'équation $(m + 1)x - 1 - \ln x = 0$.

**6.** Soit $n$ un entier naturel, $n \ge 1$. On note $U_n$ l'aire du domaine plan délimité par la courbe $(C)$, l'asymptote oblique $\Delta$ et les droites d'équations respectives $x = n$ et $x = n + 1$.

a) Exprimer $U_n$ en fonction de $n$.

b) Calculer et interpréter graphiquement $\lim\limits_{n \to +\infty} U_n$.
""", ["Suites numériques"])


# ══════════════════════════════ 2011 — session complémentaire ═════════════════

_add("bac-d-2011-sc-math-ex1", "Fonctions numériques (Limites et Continuité)", r"""
**Exercice 1 (3 points)**

Parmi les réponses proposées pour chaque question ci-après, une seule réponse est exacte.

**1)** Soit $f$ une fonction définie et continue sur $\mathbb{R}$ vérifiant, pour tout réel $x$, $f(4 - x) + f(x) = 8$ et $\lim\limits_{x \to +\infty} f(x) = 5$. Soit $(C)$ la courbe de $f$ dans un repère orthonormé.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | La courbe $(C)$ admet | un centre de symétrie $\Omega(-2;4)$ | un centre de symétrie $\Omega(2;4)$ | un axe de symétrie d'équation $x = 2$ |
| 2 | La courbe $(C)$ admet une asymptote d'équation | $x = 5$ | $y = 5$ | $y = 5x$ |
| 3 | $\lim\limits_{x \to -\infty} f(x)$ égale | $-5$ | $3$ | $-\infty$ |
| 4 | Si $f$ est strictement croissante sur l'intervalle $[2;+\infty[$, alors elle est | croissante sur $\mathbb{R}$ | décroissante sur $]-\infty;2]$ | non monotone sur $\mathbb{R}$ |

**2)** Une usine produit des bouteilles de 75 cl d'eau minérale. Soit $X$ la variable aléatoire ayant pour valeurs les quantités possibles d'eau dans une bouteille expérimentée, en centilitres. On note $p_i$ la probabilité que la quantité d'eau dans une bouteille soit $x_i$ centilitres. On donne le tableau suivant :

| $x_i$ | $74{,}8$ | $74{,}9$ | $75$ | $75{,}1$ | $75{,}2$ |
|---|---|---|---|---|---|
| $p_i$ | $\frac{1}{20}$ | $\frac{3}{20}$ | $\frac{11}{20}$ | $\frac{4}{20}$ | $\frac{1}{20}$ |

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 5 | Si on choisit au hasard une bouteille, la probabilité qu'elle soit au moins 75 cl est : | $\frac{1}{20}$ | $\frac{1}{5}$ | $\frac{3}{4}$ |
| 6 | L'espérance mathématique de la variable $X$ est égale à | $75{,}001$ | $75$ | $74{,}99$ |

Recopie sur la feuille et complète le tableau suivant en choisissant la bonne réponse.

| Question | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""", ["Probabilités"], note="Le sujet numérote 1 et 2 les questions de la partie 2) ; renumérotées 5 et 6 pour correspondre au tableau réponse.")

_add("bac-d-2011-sc-math-ex2", "Nombres complexes", r"""
**Exercice 2 (4 points)**

Pour tout nombre complexe $z$ on pose $f(z) = z^2 - 2z$. On pose $a = 1 + i$ et $b = 1 + i\sqrt{3}$.

**1. a)** Calculer $f(a)$ et $f(b)$.

b) En déduire les solutions, dans $\mathbb{C}$, des équations $z^2 - 2z + 2 = 0$ et $z^2 - 2z + 4 = 0$.

**2.** On pose $c = ab = (1 + i)(1 + i\sqrt{3})$.

a) Écrire $a$ et $b$ sous forme trigonométrique et exponentielle.

b) Écrire $c$ sous forme algébrique et exponentielle.

c) En déduire les valeurs exactes de $\cos\dfrac{7\pi}{12}$ et $\sin\dfrac{7\pi}{12}$.
""", note="Le sujet original ne définit pas a et b avant la question 1 (on lit a = 1 + i et b = 1 + i√3 à la question 2) "
          "et la question 2b porte « a et b » : il s'agit de c = ab.")

_add("bac-d-2011-sc-math-ex3", "Suites numériques", r"""
**Exercice 3 (4 points)**

On définit une suite $(U_n)$ pour tout entier naturel non nul $n$ par : $U_n = \dfrac{n^2}{2^n}$.

**1. a)** Calculer les termes $U_2$, $U_3$, $U_4$ et $U_5$.

b) Montrer que $(U_n)$ est positive, non monotone et qu'elle n'est ni arithmétique, ni géométrique.

**2. a)** Montrer que pour tout entier naturel non nul $n$ on a : $\dfrac{U_{n+1}}{U_n} = \dfrac{1}{2}\left(\dfrac{n + 1}{n}\right)^2$.

b) Prouver que pour tout entier naturel $n \ge 5$, on a : $0 < \dfrac{U_{n+1}}{U_n} \le \dfrac{3}{4}$.

**3. a)** Déterminer le sens de variation de la suite $(U_n)$ à partir du rang 5.

b) Que peut-on en déduire pour la suite ?

**4. a)** Montrer que pour tout naturel $n \ge 5$, on a : $0 < U_n < \dfrac{25}{32}\left(\dfrac{3}{4}\right)^{n-5}$.

b) En déduire $\lim\limits_{n \to +\infty} U_n$.
""")

_add("bac-d-2011-sc-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (9 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = 2x - 1 + \ln x$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1.** Calculer $\lim\limits_{x \to 0^+} f(x)$, $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

**2. a)** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

b) Démontrer que $f$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

c) Dresser le tableau de variation de $f^{-1}$, réciproque de $f$.

**3.** Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$. Vérifier que $0{,}6 < \alpha < 0{,}7$.

**4. a)** Préciser les points de $(C)$ en lesquels la tangente est parallèle à la droite d'équation $y = 3x$.

b) Construire la courbe $(C)$.

**5. a)** En utilisant une intégration par parties, calculer $\displaystyle\int_\alpha^1 \ln t\,dt$.

b) En déduire, en fonction de $\alpha$, l'aire du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = \alpha$ et $x = 1$.

**6.** On considère la fonction $g$ définie sur $\mathbb{R}$ par $g(x) = x - 1 + 2e^x$. Soit $\Gamma$ sa courbe représentative dans le repère précédent.

a) En utilisant le tableau de variation de $f$, dresser le tableau de variation de $g$.

b) Calculer $\lim\limits_{x \to -\infty} \big(g(x) - (x - 1)\big)$ et interpréter graphiquement.

c) Calculer $\lim\limits_{x \to +\infty} \dfrac{g(x)}{x}$ et interpréter graphiquement.

d) Déterminer en fonction de $\alpha$ l'abscisse du point d'intersection de la courbe $\Gamma$ de $g$ avec l'axe des abscisses.

e) Construire $\Gamma$.
""", note="Le sujet original titre cet exercice « Exercice 3 » (deux fois) : c'est le 4e exercice.")

# ═══════════════════════════════════ 2012 — session normale ═══════════════════

_add("bac-d-2012-sn-math-ex1", "Probabilités", r"""
**Exercice 1 (3 points)**

Pour éclairer une salle, on utilise deux lampes différentes. On note $F$ l'événement « la première lampe est défaillante » et $G$ l'événement « la deuxième lampe est défaillante ». Des études ont montré que : $p(F) = 0{,}2$ ; $p(G) = 0{,}3$ ; $p(F \cap G) = 0{,}1$.

Pour chacune des questions suivantes, une seule des réponses proposées est correcte.

| N° | Question | A | B | C |
|---|---|---|---|---|
| 1 | La probabilité de l'événement « les deux lampes sont défaillantes » est : | $0{,}1$ | $0{,}5$ | $0{,}6$ |
| 2 | La probabilité de l'événement « au moins une des deux lampes est défaillante » est : | $0{,}9$ | $0{,}4$ | $0{,}6$ |
| 3 | La probabilité de l'événement « les deux lampes fonctionnent » est : | $0{,}8$ | $0{,}6$ | $0{,}5$ |
| 4 | La probabilité de l'événement « exactement une des deux lampes est défaillante » est : | $0{,}3$ | $0{,}4$ | $0{,}6$ |
| 5 | Sachant que la deuxième lampe est défaillante, la probabilité que la première lampe fonctionne est : | $\frac{1}{2}$ | $\frac{2}{3}$ | $\frac{1}{3}$ |
| 6 | On définit une variable aléatoire $X$ égale au nombre de lampes défaillantes dans la salle. L'espérance mathématique de $X$ est : | $0{,}8$ | $0{,}6$ | $0{,}5$ |

Recopie sur la feuille de réponse et complète le tableau suivant en choisissant la bonne réponse.

| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""")

_add("bac-d-2012-sn-math-ex2", "Nombres complexes", r"""
**Exercice 2 (4 points)**

**1. a)** Résoudre dans l'ensemble des nombres complexes l'équation $z^2 - 4z + 5 = 0$ et soient $z_1$ et $z_2$ ses solutions telles que $\operatorname{Im}(z_1) > 0$.

b) Écrire le nombre $z_3 = i + z_1$ sous forme trigonométrique.

**2)** Dans le plan complexe muni d'un repère $(O;\vec{u},\vec{v})$, on considère les points $A$ et $B$ d'affixes respectives $z_A = z_1$ et $z_B = -1 - i + z_2$.

a) Placer les points $A$ et $B$. Déterminer la nature du triangle $OAB$.

b) Déterminer l'affixe du point $C$ tel que le quadrilatère $OACB$ soit un parallélogramme. Placer $C$.

**3)** Pour tout nombre complexe $z$ tel que $z \ne 1 - 2i$ on pose : $f(z) = \dfrac{z - 2 - i}{z - 1 + 2i}$.

a) Écrire sous forme algébrique le nombre $\omega = f(3 - i)$. Interpréter géométriquement.

b) Déterminer puis construire l'ensemble $\Gamma_1$ des points $M$ du plan d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer puis construire l'ensemble $\Gamma_2$ des points $M$ du plan d'affixe $z$ tels que le nombre $f(z)$ soit imaginaire pur.

d) Déterminer puis construire l'ensemble $\Gamma_3$ des points $M$ du plan d'affixe $z$ tels que $|f(z) - 1| = \sqrt{10}$.
""")

_add("bac-d-2012-sn-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (6 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = e^{-2x-1} + 3x - 1$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Calculer $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \big(f(x) - (3x - 1)\big)$ et interpréter graphiquement.

b) Montrer que $\lim\limits_{x \to -\infty} f(x) = +\infty$ et $\lim\limits_{x \to -\infty} \dfrac{f(x)}{x} = -\infty$ ; interpréter graphiquement.

**2. a)** Calculer la dérivée $f'(x)$ et étudier son signe.

b) Dresser le tableau de variation de $f$.

**3. a)** Montrer que l'équation $f(x) = 0$ admet exactement deux solutions $\alpha$ et $\beta$. Vérifier que $-1{,}3 < \alpha < -1{,}2$ et $0{,}2 < \beta < 0{,}3$.

b) Représenter la courbe $(C)$.

**4)** On définit les suites $(U_n)$ et $(V_n)$ pour tout entier naturel $n$ par : $U_n = e^{-2n-1}$, $V_n = 3n - 1$.

a) Démontrer que la suite $(U_n)$ est géométrique décroissante.

b) Démontrer que la suite $(V_n)$ est arithmétique croissante.

c) Les suites $(U_n)$ et $(V_n)$ sont-elles adjacentes ? Justifier.

**5)** Pour tout entier naturel $n$ on pose : $S_n = f(0) + f(1) + f(2) + \dots + f(n)$.

a) Calculer $S_n$ en fonction de $n$.

b) Calculer $\lim\limits_{n \to +\infty} S_n$ et $\lim\limits_{n \to +\infty} \dfrac{S_n}{n^2}$.
""", ["Suites numériques"])

_add("bac-d-2012-sn-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (7 points)**

Soit $f$ la fonction définie sur $]-1;+\infty[$ par $f(x) = \dfrac{2x + 1}{x + 1} - \ln(x + 1)$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Calculer $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et interpréter graphiquement.

b) Montrer que $\lim\limits_{x \to -1^+} f(x) = -\infty$ et interpréter graphiquement.

**2. a)** Calculer $f'(x)$ et vérifier que la courbe $(C)$ admet au point d'abscisse $0$ une tangente horizontale dont on donnera une équation.

b) Dresser le tableau de variation de $f$.

**3. a)** Calculer $f''(x)$ et vérifier que la courbe $(C)$ admet un point d'inflexion $A$ d'abscisse $1$.

b) Écrire une équation de la tangente $(T)$ à la courbe $(C)$ au point $A$.

**4. a)** Montrer que la restriction $g$ de $f$ sur $I = [0;+\infty[$ réalise une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Dresser le tableau de variation de $g^{-1}$.

c) Calculer $\left(g^{-1}\right)'\left(\dfrac{3 - 2\ln 2}{2}\right)$.

**5. a)** Montrer que l'équation $f(x) = 0$ admet exactement deux solutions $\alpha$ et $\beta$. Vérifier que $-0{,}7 < \alpha < -0{,}6$ et $5{,}3 < \beta < 5{,}4$.

b) Placer, sur le repère $(O;\vec{i},\vec{j})$, les points d'intersection de la courbe $(C)$ avec les axes, son point d'inflexion, les tangentes précédentes puis représenter la courbe $(C)$.

c) Représenter la courbe $(C')$ de $g^{-1}$ dans le repère précédent.

**6. a)** Montrer que la fonction $f$ admet des primitives sur $]-1;+\infty[$.

b) Déterminer les réels $a$ et $b$ tels que la fonction $F(x) = ax - (x + b)\ln(x + 1)$ soit une primitive de $f$ sur $]-1;+\infty[$.

c) Calculer, en fonction de $\beta$, l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 0$ et $x = \beta$. Donner une valeur approchée de cette aire à $10^{-2}$ près.
""")

# ══════════════════════════════ 2012 — session complémentaire ═════════════════

_add("bac-d-2012-sc-math-ex1", "Suites numériques", r"""
**Exercice 1 (3 points)**

Soit $(U_n)$ la suite numérique définie pour tout entier naturel $n$ par : $\begin{cases} U_0 = 2 \\ U_{n+1} = 3U_n - 2 \end{cases}$

Pour chacune des questions suivantes, une seule des réponses proposées est correcte.

| N° | Question | A | B | C |
|---|---|---|---|---|
| 1 | La suite $(V_n)$ définie par $V_n = U_n - 1$ est une suite | géométrique | arithmétique | ni géométrique ni arithmétique |
| 2 | La suite $(T_n)$ définie par $T_n = \ln(V_n)$ est une suite | géométrique | arithmétique | bornée |
| 3 | La suite $(W_n)$ définie par $W_n = U_{n+1} - U_n$ est une suite | croissante | décroissante | non monotone |
| 4 | Le terme général de la suite $(U_n)$ est | $U_n = 1 + 3^n$ | $U_n = 2 \times 3^n$ | $U_n = 2n + 1$ |
| 5 | La somme $S_n = U_0 + U_1 + \dots + U_n$ est égale à | $S_n = \dfrac{1 + 3^{n+1}}{2}$ | $S_n = n + \dfrac{1}{2} + \dfrac{3^{n+1}}{2}$ | $S_n = \dfrac{1 - 3^n}{2}$ |
| 6 | La limite de la suite $(U_n)$ est | $-\infty$ | $0$ | $+\infty$ |

Recopie sur la feuille de réponse et complète le tableau suivant en choisissant la bonne réponse.

| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""", note="Énoncé lu sur un scan (CamScanner) qui porte des réponses manuscrites d'un élève : elles n'ont pas été recopiées.")

_add("bac-d-2012-sc-math-ex2", "Nombres complexes", r"""
**Exercice 2 (5 points)**

Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$. Pour tout nombre complexe $z$ tel que $z \ne -3 - 2i$ on pose : $f(z) = \dfrac{z - 2 - i}{z + 3 + 2i}$.

**1)** Résoudre dans $\mathbb{C}$ l'équation $z^2 - 2z + 5 = 0$.

**2)** Calculer le nombre $p = f(1 - 2i)$ puis l'écrire sous forme algébrique.

**3)** On considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 2 + i$, $z_B = -3 - 2i$ et $z_C = 1 + 2i$.

a) Placer les points $A$, $B$ et $C$ dans le repère $(O;\vec{u},\vec{v})$.

b) Écrire le nombre $q = f(z_C)$ sous forme trigonométrique. En déduire la nature du triangle $ABC$.

c) Déterminer et représenter dans le même repère les ensembles des points $M$ du plan d'affixe $z$ dans chacun des cas suivants :

- $\Gamma_1$ tel que $|f(z)| = 1$ ;
- $\Gamma_2$ tel que $f(z)$ soit imaginaire pur ;
- $\Gamma_3$ tel que $|f(z) - 1| = 2\sqrt{34}$.
""")

_add("bac-d-2012-sc-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (6 points)**

Soit $f$ la fonction définie sur $]0;+\infty[$ par $f(x) = x - 2 - 2\ln x$.

**1.** Calculer $\lim\limits_{x \to 0^+} f(x)$, $\lim\limits_{x \to +\infty} f(x)$, $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et $\lim\limits_{x \to +\infty} \big(f(x) - x\big)$ et interpréter graphiquement.

**2.** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

**3.** Donner l'équation de la tangente $T$ à $(C)$ au point $A$ d'abscisse $x_0 = 1$.

**4.** Montrer que l'équation $f(x) = 0$ admet exactement deux solutions $\alpha$ et $\beta$ et que $0{,}4 < \alpha < 0{,}5$ ; $5{,}3 < \beta < 5{,}4$. Démontrer que $\alpha^2 e^\beta = \beta^2 e^\alpha$.

**5.** Soit $g$ la restriction de $f$ sur $I = ]0;2[$.

a) Montrer que $g$ réalise une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Calculer $\left(g^{-1}\right)'(-1)$ (on pourra utiliser la question 3).

**6. a)** Tracer les courbes $(C)$ et $(C')$ respectivement des fonctions $f$ et $g^{-1}$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

b) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $2x - 2 - m - 2\ln x = 0$.

**7. a)** En utilisant une intégration par parties, calculer $\displaystyle\int_1^2 \ln x\,dx$.

b) Calculer l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = 2$.
""")

_add("bac-d-2012-sc-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (6 points)**

Soit $g$ la fonction définie sur $\mathbb{R}$ par $g(x) = xe^x - 1$.

**1. a)** Calculer $\lim\limits_{x \to -\infty} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer $g'(x)$ et dresser le tableau de variation de $g$.

**2. a)** Montrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$. Vérifier que $0{,}5 < \alpha < 0{,}6$.

b) Justifier que : si $x \le \alpha$ alors $g(x) \le 0$ et si $x \ge \alpha$ alors $g(x) \ge 0$.

**3.** Soit $f$ la fonction définie sur $]-\infty;-1[ \cup ]-1;+\infty[$ par $f(x) = \dfrac{e^x - x}{x + 1}$.

a) Justifier et interpréter les limites suivantes : $\lim\limits_{x \to -1^-} f(x) = -\infty$, $\lim\limits_{x \to -1^+} f(x) = +\infty$, $\lim\limits_{x \to -\infty} f(x) = -1$, $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = +\infty$.

b) Calculer $f'(x)$ et montrer que $f'(x) = \dfrac{g(x)}{(x + 1)^2}$.

c) Dresser le tableau de variation de $f$.

d) Vérifier que $f(\alpha) = \dfrac{1 - \alpha^2}{\alpha^2 + \alpha}$ et donner une valeur approchée de $f(\alpha)$ à $10^{-1}$ près.

**4.** Tracer la courbe $(C)$ de la fonction $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.
""")

# ═══════════════════════════════════ 2013 — session normale ═══════════════════

_add("bac-d-2013-sn-math-ex1", "Probabilités", r"""
**Exercice 1 (3 points)**

Une urne contient 4 boules blanches et 2 boules noires indiscernables au toucher. On effectue au hasard un tirage de 2 boules simultanément de l'urne.

On note $A_0$ l'événement « on a obtenu aucune boule noire », $A_1$ l'événement « on a obtenu une seule boule noire » et $A_2$ l'événement « on a obtenu deux boules noires ».

Soit $X$ la variable aléatoire qui associe le nombre de boules noires tirées.

Parmi les réponses proposées pour chaque question ci-après, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | Le nombre de tirages possibles est : | $C_6^2$ | $A_6^2$ | $6^2$ |
| 2 | La probabilité $p(A_0)$ est : | $\frac{4}{6}$ | $\frac{6}{15}$ | $\left(\frac{4}{6}\right)^2$ |
| 3 | La probabilité $p(A_1)$ est : | $\frac{8}{15}$ | $\frac{1}{6}$ | $\frac{2}{6}$ |
| 4 | La probabilité $p(A_2)$ est : | $\frac{4}{6}$ | $\frac{6}{15}$ | $\frac{1}{15}$ |
| 5 | L'espérance mathématique de $X$ est : | $\frac{2}{3}$ | $\frac{16}{15}$ | $4$ |

Recopie et complète le tableau suivant en choisissant la bonne réponse. Aucune justification n'est demandée.

| Question | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Réponse | | | | | |
""")

_add("bac-d-2013-sn-math-ex2", "Nombres complexes", r"""
**Exercice 2 (5 points)**

Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$.

**1. a)** Résoudre dans $\mathbb{C}$ l'équation $(E_1) : z^2 + 2z + 10 = 0$. On note $z_1$ et $z_2$ ses solutions avec $\operatorname{Im}(z_2) \le 0$.

b) Résoudre dans $\mathbb{C}$ l'équation $(E_2) : z^2 - 4z + 20 = 0$. On note $z_3$ et $z_4$ ses solutions avec $\operatorname{Im}(z_4) \le 0$.

**2)** On considère les points $A$, $B$, $K$, $L$ et $E$ d'affixes respectives $z_A = z_1$, $z_B = z_2$, $z_K = z_3$, $z_L = z_4$ et $z_E = z_3 - 2i$.

a) Placer les points $A$, $B$, $K$, $L$ et $E$ dans le repère $(O;\vec{u},\vec{v})$.

b) Écrire $z_E = z_3 - 2i$ sous forme algébrique et trigonométrique.

c) Déterminer la nature du quadrilatère $ABLE$ et du triangle $AKE$.

**3)** Pour tout nombre complexe $z$ tel que $z \ne -1 + 3i$ on pose : $f(z) = \dfrac{z - 2 - 4i}{z + 1 - 3i}$.

Déterminer et représenter dans le même repère les ensembles des points $M$ du plan d'affixe $z$ dans chacun des cas suivants :

- $\Gamma_1$ tel que $|f(z)| = 1$ ;
- $\Gamma_2$ tel que $|f(z) - 1| = \sqrt{10}$.
""")

_add("bac-d-2013-sn-math-ex3", "Suites numériques", r"""
**Exercice 3 (4 points)**

On considère la suite numérique $(U_n)$ définie par $U_0 = 6$ et, pour tout $n \in \mathbb{N}$, $U_{n+1} = 3U_n + 10n - 13$.

**1. a)** Calculer $U_1$, $U_2$ et vérifier que $U_3 = 43$.

b) Justifier que la suite numérique $(U_n)$ n'est ni géométrique ni arithmétique.

**2)** On définit la suite numérique $(V_n)$ par : pour tout entier $n \in \mathbb{N}$, $V_n = U_n + 5n - 4$.

a) Démontrer que la suite $(V_n)$ est une suite géométrique dont on déterminera la raison et le premier terme. Exprimer $V_n$ en fonction de $n$.

b) À partir de quel terme a-t-on $V_n \ge 2013$ ?

c) En déduire que, pour tout $n \in \mathbb{N}$, $U_n = 2 \times 3^n - 5n + 4$.

**3)** Pour tout entier naturel $n$, on pose $S_n = U_0 + U_1 + \dots + U_n$. Déterminer l'expression de $S_n$ en fonction de $n$.
""")

_add("bac-d-2013-sn-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (8 points)**

**Partie A**

On considère la fonction $g$ définie sur $]0;+\infty[$ par $g(x) = x^3 - 3 + 2\ln x$.

**1. a)** Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer la dérivée $g'(x)$ et dresser le tableau de variation de $g$.

**2. a)** Montrer que $g$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $g(x) = 0$ admet une unique solution $\alpha$. Vérifier que $1{,}34 \le \alpha \le 1{,}35$.

c) En déduire le signe de la fonction $g$ sur l'intervalle $]0;+\infty[$.

**Partie B**

On considère la fonction $f$ définie sur $]0;+\infty[$ par $f(x) = x - 2 + \dfrac{1 - \ln x}{x^2}$. On note $\Gamma$ sa courbe représentative dans le plan muni d'un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Démontrer que $\lim\limits_{x \to 0^+} f(x) = +\infty$, $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \big(f(x) - (x - 2)\big) = 0$.

b) Interpréter graphiquement les limites précédentes.

c) Étudier le signe de $d(x) = f(x) - (x - 2)$. Résumer dans un tableau et interpréter graphiquement.

**2. a)** Calculer $f'(x)$ et justifier que $f'(x)$ a même signe que $g(x)$.

b) Montrer que $f(\alpha) = \dfrac{3\alpha^3 - 4\alpha^2 - 1}{2\alpha^2}$ et donner une valeur approchée de $f(\alpha)$ à $10^{-1}$ près.

c) En déduire le tableau de variation de $f$.

**3. a)** Donner l'équation de la tangente $T$ à $\Gamma$ au point $A$ d'abscisse $x_0 = 1$.

b) Montrer que la courbe $\Gamma$ coupe l'axe des abscisses en un deuxième point autre que $A$, d'abscisse $\beta$ telle que $1{,}9 \le \beta \le 2$.

c) Tracer l'allure de la courbe dans le repère $(O;\vec{i},\vec{j})$.

**4)** Soit $n$ un entier naturel, $n \ge 3$. On considère l'aire du domaine $E$ du plan compris entre la courbe et les droites d'équations respectives $y = x - 2$, $x = 3$ et $x = n$.

a) Justifier que cette aire, exprimée en cm², est donnée par $I_n = \displaystyle\int_3^n \dfrac{-1 + \ln x}{x^2}\,dx$.

b) Calculer $J_n = \displaystyle\int_3^n \dfrac{\ln x}{x^2}\,dx$ à l'aide d'une intégration par parties. En déduire $I_n$ en fonction de $n$.

c) Calculer la limite de l'aire $I_n$ du domaine $E$ quand $n$ tend vers $+\infty$.
""", ["Intégration et Primitives"],
     note="Le PDF (version retapée) écrit g(x) = x² − 3 + 2 ln x : c'est une coquille. Seul g(x) = x³ − 3 + 2 ln x "
          "est cohérent avec la suite (f'(x) = g(x)/x³, 1,34 ≤ α ≤ 1,35 et la formule de f(α)) ; vérifié par calcul. "
          "L'intégrale notée J₀ dans le sujet est notée Jₙ ici.")

# ══════════════════════════════ 2013 — session complémentaire ═════════════════

_add("bac-d-2013-sc-math-ex1", "Suites numériques", r"""
**Exercice 1 (3 points)**

On considère la suite arithmétique $(U_n)$ de raison $r = 3$ et de premier terme $U_0 = 15$.

Pour chaque question, parmi les réponses proposées, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | Le terme général de la suite $(U_n)$ est : | $U_n = 3 + 15n$ | $U_n = 15 + 3n$ | $U_n = 3n + 12$ |
| 2 | La valeur de $U_{10}$ est : | $U_{10} = 153$ | $U_{10} = 13$ | $U_{10} = 45$ |
| 3 | Si $U_0 + U_1 + \dots + U_n = 204$ alors : | $n = 204$ | $n = 30$ | $n = 7$ |
| 4 | La suite $(V_n)$ de terme général $V_n = \dfrac{1}{U_n}$ est : | convergente | croissante | géométrique |
| 5 | La suite $(T_n)$ de terme général $T_n = e^{U_n}$ est : | arithmétique | géométrique | majorée |
| 6 | Si $(W_n)$ est une suite numérique telle que pour tout $n$ : $V_n \le W_n \le U_n$, alors $(W_n)$ est : | minorée | décroissante | divergente |

Recopie sur la feuille de réponse et complète le tableau suivant en choisissant la bonne réponse. Aucune justification n'est demandée.

| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""", note="Question 3 : le PDF a un blanc (« Si U₀ + U₁ + ⋯   204 ») ; complété en « + Uₙ = 204 », seule lecture cohérente (n = 7).")

_add("bac-d-2013-sc-math-ex2", "Nombres complexes", r"""
**Exercice 2 (5 points)**

**1)** Résoudre dans l'ensemble des nombres complexes $\mathbb{C}$ l'équation $(E) : z^2 - 6z + 18 = 0$.

**2)** Résoudre dans l'ensemble des nombres complexes $\mathbb{C}$ l'équation $(E') : z^2 - 2\sqrt{3}\,z + 4 = 0$.

**3)** Écrire sous forme trigonométrique et exponentielle chacun des nombres $u = 3 + 3i$ et $v = \sqrt{3} - i$.

**4)** On pose $w = (3 + 3i)(\sqrt{3} - i)$.

a) Écrire $w$ sous forme algébrique.

b) En utilisant 3), écrire $w$ sous forme trigonométrique et exponentielle.

c) En déduire les valeurs exactes de $\cos\dfrac{\pi}{12}$ et $\sin\dfrac{\pi}{12}$.
""")

_add("bac-d-2013-sc-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (6 points)**

On considère la fonction numérique $f$ définie sur l'intervalle $I = ]-1;+\infty[$ par $f(x) = x - 2 + \ln(x + 1)$.

**1. a)** Montrer que $\lim\limits_{x \to -1^+} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

b) Calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$ et $\lim\limits_{x \to +\infty} \big(f(x) - x\big)$. Interpréter graphiquement.

**2.** Calculer $f'(x)$ et dresser le tableau de variation de $f$.

**3. a)** Montrer que la fonction $f$ réalise une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $f(x) = 0$ admet dans $I$ une unique solution $\alpha$. Vérifier que $1{,}2 < \alpha < 1{,}3$.

c) Construire la courbe $(C)$ représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**4)** Pour tout $x > -1$, on pose $u(x) = (x + 1)\ln(x + 1)$.

a) Calculer $u'(x)$ et montrer que pour tout $x > -1$ on a $f(x) = u'(x) + x - 3$.

b) En déduire la primitive $F$ de la fonction $f$ sur $]-1;+\infty[$ qui vérifie $F(0) = 0$.

c) Calculer l'aire du domaine plan limité par la courbe $(C)$ de $f$ et les droites d'équations $x = 0$ et $x = \alpha$.

**5)** Soit $f^{-1}$ la réciproque de $f$ et $(C')$ sa courbe représentative dans le repère précédent.

a) Déduire de ce qui précède les limites $\lim\limits_{x \to -\infty} f^{-1}(x)$, $\lim\limits_{x \to +\infty} f^{-1}(x)$ et $\lim\limits_{x \to +\infty} \dfrac{f^{-1}(x)}{x}$.

b) Calculer $\left(f^{-1}\right)'(-2)$ et donner l'équation de la tangente à la courbe $(C')$ au point d'abscisse $x_0 = -2$.
""")

_add("bac-d-2013-sc-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (6 points)**

**1)** On considère la fonction numérique $g$ définie par $g(x) = (2x + 3)e^{x+1} + 1$.

a) Justifier que $\lim\limits_{x \to +\infty} g(x) = +\infty$ et $\lim\limits_{x \to -\infty} g(x) = 1$.

b) Calculer $g'(x)$ et dresser le tableau de variation de $g$.

c) En déduire que pour tout réel $x$, $g(x) > 0$.

**2)** On considère la fonction numérique $f$ définie par $f(x) = x - 3 + (2x + 1)e^{x+1}$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$.

a) Montrer que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

b) Calculer et interpréter graphiquement $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

c) Montrer que la droite $D$ d'équation $y = x - 3$ est une asymptote oblique à $(C)$ au voisinage de $-\infty$, puis déterminer leurs positions relatives.

**3. a)** Écrire $f'(x)$ en fonction de $g(x)$.

b) Dresser le tableau de variation de $f$.

**4. a)** Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$ puis vérifier que $0 < \alpha < 0{,}1$.

c) Montrer que la solution $\alpha$ vérifie l'égalité $\ln\left(\dfrac{3 - \alpha}{2\alpha + 1}\right) - \alpha = 1$.

**5. a)** Montrer qu'il existe un unique point $A$ auquel la tangente $T$ à $(C)$ est parallèle à l'asymptote oblique d'équation $y = x - 3$. Donner une équation de $T$.

b) Construire la courbe $(C)$, la tangente $T$ et l'asymptote $D$.

c) Discuter graphiquement, suivant les valeurs du paramètre $m$, le nombre de solutions de l'équation $(2x + 1)e^{x+1} - m - 3 = 0$.
""")

# ═══════════════════════════════════ 2014 — session normale ═══════════════════

_add("bac-d-2014-sn-math-ex1", "Probabilités", r"""
**Exercice 1 (3 points)**

Une cage contient six pigeons dont quatre femelles et deux mâles ; parmi ces pigeons, on dispose de deux couples de plumage blanc et de deux femelles de plumage gris. On tire simultanément deux oiseaux de cette cage (les tirages sont équiprobables).

**1)** On considère les probabilités :

- $p_1$ la probabilité de l'événement $A$ : « Les deux oiseaux tirés sont de plumage gris » ;
- $p_2$ la probabilité de l'événement $B$ : « Les deux oiseaux tirés sont de même couleur » ;
- $p_3$ la probabilité de l'événement $C$ : « Les deux oiseaux tirés sont de même sexe ».

**2)** On suppose dans cette question que le tirage a donné deux oiseaux de même couleur. On note $p_4$ la probabilité que ces deux oiseaux soient de même sexe.

Parmi les réponses proposées pour chaque question ci-après, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | Le nombre de tirages possibles est : | $6^2$ | $A_6^2$ | $C_6^2$ |
| 2 | La probabilité $p_1$ est : | $\frac{4}{15}$ | $\frac{1}{15}$ | $\frac{2}{15}$ |
| 3 | La probabilité $p_2$ est : | $\frac{1}{15}$ | $\frac{7}{15}$ | $\frac{8}{15}$ |
| 4 | La probabilité $p_3$ est : | $\frac{2}{15}$ | $\frac{8}{15}$ | $\frac{7}{15}$ |
| 5 | La probabilité $p_4$ est : | $\frac{1}{3}$ | $\frac{3}{7}$ | $\frac{7}{15}$ |

Recopie et complète le tableau suivant en choisissant la bonne réponse. Aucune justification n'est demandée.

| Question n° | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Réponse | | | | | |
""")

_add("bac-d-2014-sn-math-ex2", "Nombres complexes", r"""
**Exercice 2 (5 points)**

On considère le plan complexe muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1.** Résoudre dans l'ensemble des nombres complexes chacune des équations suivantes :
$(E_1) : z^2 - 2z + 17 = 0$ et $(E_2) : z^2 + 8z + 17 = 0$.

**2)** Pour tout nombre complexe $z$ tel que $z \ne -4 - i$, on pose $f(z) = \dfrac{z - 1 + 4i}{z + 4 + i}$. On considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = -4 - i$, $z_B = 1 - 4i$ et $z_C = 4 + i$.

a) Placer dans le repère $(O;\vec{u},\vec{v})$ les points $A$, $B$ et $C$, et déterminer la nature du triangle $ABC$.

b) Calculer $\alpha = f(-1 + 4i)$ puis donner son écriture algébrique et trigonométrique.

c) Déterminer puis construire l'ensemble $\Gamma_1$ des points $M$ du plan d'affixe $z$ tels que $|f(z)| = 1$.

d) Déterminer puis construire l'ensemble $\Gamma_2$ des points $M$ du plan d'affixe $z$ tels que le nombre $f(z)$ soit imaginaire pur.

**3)** On considère la suite de nombres complexes $(z_n)_{n \in \mathbb{N}}$ définie par $z_0 = 4 + i$ et, pour tout entier naturel $n$, $z_{n+1} = \dfrac{\alpha}{2}\,z_n$. On appelle $M_n$ le point d'affixe $z_n$.

a) Calculer $z_1$ et $z_2$.

b) Montrer que la suite de terme général $V_n = |z_n|$ est une suite géométrique.

c) On pose $S_n = OM_0 + OM_1 + \dots + OM_n$. Donner l'expression de $S_n$ en fonction de $n$. Calculer $\lim\limits_{n \to +\infty} S_n$.
""", ["Suites numériques"])

_add("bac-d-2014-sn-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (7 points)**

On considère la fonction numérique $f$ définie par $f(x) = 2x - 1 + 2e^x$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Justifier que $\lim\limits_{x \to -\infty} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} f(x) = +\infty$.

b) Calculer et donner une interprétation graphique de $\lim\limits_{x \to -\infty} \big(f(x) - (2x - 1)\big)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

**2. a)** Dresser le tableau de variation de $f$.

b) Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ que l'on déterminera.

c) Montrer que l'équation $f(x) = 0$ admet dans $\mathbb{R}$ une unique solution $\alpha$ puis vérifier que $-0{,}3 < \alpha < -0{,}2$.

**3)** Construire les courbes $(C)$ et $(C')$ représentant respectivement la fonction $f$ et sa réciproque $f^{-1}$ dans le repère $(O;\vec{i},\vec{j})$.

**4. a)** Déterminer une équation de la tangente $(T)$ à $(C)$ en $x_0 = \alpha$.

b) Vérifier que $\left(f^{-1}\right)'(0) = \dfrac{1}{-2\alpha + 3}$.

**5)** On considère la suite $(U_n)$ définie pour tout entier naturel $n$ par $U_n = f(n)$.

a) Montrer que $(U_n)$ est la somme de deux suites, une arithmétique et une géométrique, dont on déterminera le premier terme et la raison.

b) On pose $S_n = U_0 + U_1 + \dots + U_n$. Donner l'expression de $S_n$ en fonction de $n$. Calculer $\lim\limits_{n \to +\infty} S_n$.
""", ["Suites numériques"])

_add("bac-d-2014-sn-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (7 points)**

**Partie A**

On considère la fonction $g$ définie sur l'intervalle $]0;+\infty[$ par $g(x) = x - 3 + 3\ln x$.

**1. a)** Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer la dérivée $g'(x)$ et dresser le tableau de variation de $g$.

**2. a)** Montrer que l'équation $g(x) = 0$ admet dans $]0;+\infty[$ une unique solution $\alpha$ puis vérifier que $1{,}59 < \alpha < 1{,}60$.

b) En déduire le signe de $g$ sur l'intervalle $]0;+\infty[$.

**Partie B**

Soit $f$ la fonction définie sur l'intervalle $]0;+\infty[$ par $f(x) = \dfrac{(x - 3)\ln x}{x}$.

On peut donc aussi écrire : $f(x) = \dfrac{x - 3}{x}\ln x$ (1) et $f(x) = \ln x - \dfrac{3\ln x}{x}$ (2).

On désigne par $(C)$ la courbe représentative de $f$ dans un repère orthonormé $(O;\vec{i},\vec{j})$.

**1. a)** Démontrer que $\lim\limits_{x \to 0^+} f(x) = +\infty$, $\lim\limits_{x \to +\infty} f(x) = +\infty$ et $\lim\limits_{x \to +\infty} \big(f(x) - \ln x\big) = 0$.

b) Interpréter graphiquement les limites précédentes.

**2. a)** Calculer la dérivée $f'(x)$. Vérifier que $f'(x)$ et $g(x)$ ont le même signe.

b) Montrer que $f(\alpha) = \dfrac{-(\alpha - 3)^2}{3\alpha}$ et donner une valeur approchée de $f(\alpha)$ à $10^{-1}$ près.

c) Dresser le tableau de variation de la fonction $f$.

**3. a)** Déterminer une équation de la tangente $T$ à $(C)$ au point d'abscisse $1$.

b) Déterminer les coordonnées des points d'intersection de $(C)$ avec l'axe des abscisses. Tracer $(C)$ et $T$.

c) Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation $2x^2 - mx + x\ln x - 3\ln x = 0$.

**4. a)** Calculer l'intégrale $J = \displaystyle\int_1^e \dfrac{\ln x}{x}\,dx$.

b) En utilisant une intégration par parties, calculer l'intégrale $I = \displaystyle\int_1^e \ln x\,dx$.

c) Justifier que l'aire $S$ du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$ est donnée par $S = -\displaystyle\int_1^e f(x)\,dx$. Calculer cette aire.
""", ["Intégration et Primitives"],
     note="Partie B 3a : le sujet ne donne pas l'abscisse du point (« au point d'abscisse. ») ; le corrigé officiel "
          "utilise A(1 ; 0), d'où « au point d'abscisse 1 ». Partie A 2a : « dans ℝ » remplacé par « dans ]0 ; +∞[ » (domaine de g).")

# ══════════════════════════════ 2014 — session complémentaire ═════════════════

_add("bac-d-2014-sc-math-ex1", "Probabilités", r"""
**Exercice 1 (3 points)**

Un questionnaire à choix multiples (QCM) comporte 8 questions indépendantes. Pour chacune d'elles, quatre réponses sont proposées dont une seule correcte. Un élève répond au hasard à chaque question du QCM. On note $X$ le nombre de réponses correctes qu'il a données. On considère les événements suivants :

$A$ : « L'élève a toutes les réponses correctes. »

$B$ : « L'élève n'a aucune réponse correcte. »

$C$ : « L'élève a au moins une réponse correcte. »

$D$ : « L'élève a exactement deux réponses correctes. »

Parmi les réponses proposées pour chaque question ci-après, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | L'ensemble des valeurs de $X$ est : | $\{0,1,2,\dots,8\}$ | $\{0,1,\dots,4\}$ | $\{1,2,\dots,8\}$ |
| 2 | La probabilité de l'événement $A$ est : | $\frac{1}{4} \times 8$ | $\left(\frac{1}{4}\right)^8$ | $\left(\frac{1}{8}\right)^8$ |
| 3 | La probabilité de l'événement $B$ est : | $1 - \left(\frac{1}{4}\right)^8$ | $\left(\frac{3}{4}\right)^8$ | $1 - \left(\frac{7}{8}\right)^8$ |
| 4 | La probabilité de l'événement $C$ est : | $1 - \left(\frac{1}{4}\right)^8$ | $\left(\frac{1}{4}\right)\left(\frac{3}{4}\right)^7$ | $1 - \left(\frac{3}{4}\right)^8$ |
| 5 | La probabilité de l'événement $D$ est : | $C_8^2\left(\frac{1}{4}\right)^2\left(\frac{3}{4}\right)^6$ | $\left(\frac{1}{4}\right)^2$ | $1 - \left(\frac{3}{4}\right)^6$ |
| 6 | Le nombre de réponses correctes de l'élève que l'on peut espérer est : | $8$ | $6$ | $2$ |

Recopie sur la feuille de réponse et complète le tableau ci-contre en choisissant la bonne réponse.

| Question n° | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""")

_add("bac-d-2014-sc-math-ex2", "Nombres complexes", r"""
**Exercice 2 (5 points)**

Le plan complexe est muni d'un repère orthonormé direct $(O;\vec{u},\vec{v})$.

**1)** On considère les nombres : $z_1 = \dfrac{-1 + 7i}{3 + 4i}$, $z_2 = (1 + i)^2$ et $z_3 = \dfrac{4 - 8i}{1 + 3i}$.

a) Donner la forme algébrique de chacun des nombres $z_1$, $z_2$ et $z_3$.

b) Donner la forme trigonométrique de chacun des nombres $z_1$, $z_2$ et $z_3$.

**2. a)** Placer dans le repère $(O;\vec{u},\vec{v})$ les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1 + i$, $z_B = 2i$ et $z_C = -2 - 2i$.

b) Montrer que le triangle $ABC$ est rectangle.

c) Déterminer et construire l'ensemble $\Delta$ des points $M$ d'affixe $z$ tels que $\left|\dfrac{z + 2 + 2i}{z - 2i}\right| = 1$.

d) Déterminer l'affixe du point $D$ tel que le quadrilatère $ABCD$ soit un parallélogramme. Placer $D$.

**3)** Résoudre dans $\mathbb{C}$ l'équation $z^2 + 2z + 10 = 0$.
""")

_add("bac-d-2014-sc-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (5 points)**

Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = (x^2 + 2x + 1)e^x$. Soit $(C)$ sa courbe représentative dans le repère orthonormal $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Montrer que $\lim\limits_{x \to -\infty} f(x) = 0$. Interpréter graphiquement.

b) Montrer que $\lim\limits_{x \to +\infty} f(x) = +\infty$ et calculer $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$. Interpréter graphiquement.

**2. a)** Calculer $f'(x)$ et vérifier que la courbe $(C)$ admet deux tangentes horizontales que l'on déterminera.

b) Dresser le tableau de variation de $f$.

**3)** Déterminer l'intersection de $(C)$ avec les axes des coordonnées puis construire $(C)$ dans $(O;\vec{i},\vec{j})$.

**4)** Soit $g$ la restriction de $f$ sur l'intervalle $[0;+\infty[$.

a) Montrer que $g$ réalise une bijection de $[0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

b) Donner une équation de la tangente $T$ à $(C)$ au point d'abscisse $0$ et calculer $\left(g^{-1}\right)'(1)$.

**5. a)** Déterminer les réels $a$, $b$ et $c$ tels que la fonction définie par $F(x) = (ax^2 + bx + c)e^x$ soit une primitive de $f$ sur $\mathbb{R}$.

b) Calculer l'aire du domaine plan délimité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = -1$ et $x = 0$.
""")

_add("bac-d-2014-sc-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (7 points)**

**Partie A**

On considère la fonction $g$ définie sur l'intervalle $]0;+\infty[$ par $g(x) = 2 - x - \ln x$.

**1. a)** Calculer $\lim\limits_{x \to 0^+} g(x)$ et $\lim\limits_{x \to +\infty} g(x)$.

b) Calculer la dérivée $g'(x)$ et dresser le tableau de variation de $g$.

**2. a)** Montrer que $g$ réalise une bijection de $]0;+\infty[$ sur un intervalle $J$ que l'on déterminera.

b) Montrer que l'équation $g(x) = 0$ admet dans $]0;+\infty[$ une unique solution $\alpha$. Vérifier que $1{,}55 \le \alpha \le 1{,}56$.

c) En déduire le signe de la fonction $g$ sur l'intervalle $]0;+\infty[$.

**Partie B**

Soit $f$ la fonction définie sur l'intervalle $]0;+\infty[$ par $f(x) = \left(1 - \dfrac{1}{x}\right)(1 - \ln x)$. On désigne par $(C)$ la courbe représentative de $f$ dans le plan rapporté à un repère orthonormal $(O;\vec{i},\vec{j})$.

**1. a)** Démontrer que $\lim\limits_{x \to 0^+} f(x) = -\infty$, $\lim\limits_{x \to +\infty} f(x) = -\infty$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x} = 0$.

b) Interpréter graphiquement les limites précédentes.

**2. a)** Calculer la dérivée $f'(x)$. Vérifier que pour tout réel $x$ de $]0;+\infty[$, $f'(x) = \dfrac{g(x)}{x^2}$.

b) Montrer que $f(\alpha) = \dfrac{(\alpha - 1)^2}{\alpha}$ et donner une valeur approchée de $f(\alpha)$ à $10^{-1}$ près.

c) Dresser le tableau de variation de la fonction $f$.

**3)** Déterminer les coordonnées des points d'intersection de $(C)$ avec l'axe des abscisses. Tracer $(C)$.

**4. a)** En utilisant une intégration par parties, calculer l'intégrale $I = \displaystyle\int_1^x \ln t\,dt$.

b) En remarquant que $f(x) = 1 - \ln x - \dfrac{1}{x} + \dfrac{1}{x}\ln x$, donner une primitive $F$ de $f$ sur $[1;+\infty[$.

c) Calculer l'aire $S$ du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations $x = 1$ et $x = e$.
""", ["Intégration et Primitives"])


# ═══════════════════════════════════ 2010 — session normale ═══════════════════
# Texte OCR déjà en base (tableaux illisibles) : remplacé par la transcription.

_add("bac-d-2010-sn-math-ex1", "Fonctions numériques (Limites et Continuité)", r"""
**Exercice 1 (3 points)**

On considère une fonction $f$ dérivable sur son domaine de définition $D_f$, de dérivée $f'$. Son tableau de variation est donné ci-dessous. On nomme $(C)$ la courbe représentative de la fonction $f$ dans le plan muni d'un repère orthogonal $(O;\vec{i},\vec{j})$.

| $x$ | $-\infty$ | | $-2$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|---|---|
| $f'(x)$ | | $+$ | ‖ | $-$ | $0$ | $+$ | |
| $f(x)$ | $-3$ | ↗ | $+\infty$ ‖ $+\infty$ | ↘ | $-4$ | ↗ | $+\infty$ |

Pour chaque question, parmi les réponses proposées, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | L'ensemble de définition de $f$ est : | $\mathbb{R}\setminus\{-2\}$ | $\mathbb{R}\setminus\{-2;1\}$ | $\mathbb{R}\setminus\{1\}$ |
| 2 | L'équation $f(x) = 0$ admet dans $D_f$ exactement | 3 solutions | 2 solutions | 1 solution |
| 3 | La courbe $(C)$ admet une asymptote d'équation | $x = 1$ | $x = -2$ | $y = -2$ |
| 4 | La fonction $f$ est une fonction | paire | impaire | ni paire ni impaire |
| 5 | L'équation de la tangente à $(C)$ au point d'abscisse $x_0 = 1$ est | $x = 1$ | $y = 0$ | $y = -4$ |

Recopie sur la feuille de réponse et complète le tableau ci-dessous. Aucune justification n'est demandée.

| N° question | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Réponse exacte | | | | | |
""", replace_ocr=True)

_add("bac-d-2010-sn-math-ex2", "Nombres complexes", r"""
**Exercice 2 (4 points)**

Pour tout nombre $z$ on pose : $p(z) = z^3 - z^2 - 4z - 6$.

**1°) a)** Calculer $p(3)$.

b) Déterminer les réels $a$, $b$ tels que pour tout $z$ on a $p(z) = (z - 3)(z^2 + az + b)$.

c) Résoudre dans l'ensemble des nombres complexes l'équation $p(z) = 0$.

**2°)** On considère dans le plan complexe muni d'un repère orthonormé $(O;\vec{u},\vec{v})$ les points $A$, $B$, $C$ et $D$ d'affixes respectives $z_A = 3 + 2i$, $z_B = -1 + i$, $z_C = -1 - i$ et $z_D = 3$.

a) Placer les points $A$, $B$, $C$ et $D$ dans le repère $(O;\vec{u},\vec{v})$.

b) Comparer l'affixe du milieu de $[AC]$ à celle du milieu de $[BD]$.

c) En déduire la nature du quadrilatère $ABCD$.

d) Déterminer et construire l'ensemble des points $M$ d'affixe $z$ tels que $|z - 3| = |z + 1 - i|$.
""", replace_ocr=True)

_add("bac-d-2010-sn-math-ex3", "Suites numériques", r"""
**Exercice 3 (4 points)**

On considère la suite numérique $(U_n)$ définie pour tout entier $n \ge 1$ par : $U_n = \dfrac{n^2 + n + 1}{n(n + 1)}$.

**1. a)** Calculer $U_1$, $U_2$ et $U_3$.

b) Justifier que la suite $(U_n)$ n'est pas arithmétique, n'est pas géométrique et est convergente.

**2°)** Pour tout entier $n \ge 1$ on pose : $V_n = \dfrac{n^2 - 1}{n}$.

a) Montrer que $U_n = V_{n+1} - V_n$.

b) En déduire l'expression de la somme $S_n = U_1 + U_2 + \dots + U_n$ en fonction de $n$.

**3)** Pour tout entier $n \ge 2$ on pose $W_n = \ln V_n$ et $S'_n = W_2 + W_3 + \dots + W_n$. Démontrer que $S'_n = \ln\left[\dfrac{(n + 1)!}{2n}\right]$.
""", replace_ocr=True)

_add("bac-d-2010-sn-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (9 points)**

On considère la fonction numérique $f$ définie par $f(x) = x + 2 + e^x$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Calculer les limites de $f(x)$ en $-\infty$ et en $+\infty$.

b) Calculer et donner une interprétation graphique de $\lim\limits_{x \to -\infty} \big(f(x) - (x + 2)\big)$ et $\lim\limits_{x \to +\infty} \dfrac{f(x)}{x}$.

**2)** Dresser le tableau de variation de $f$.

**3°)** Montrer que $f$ réalise une bijection de $\mathbb{R}$ sur un intervalle $J$ que l'on déterminera.

**4°)** Montrer que l'équation $f(x) = 0$ admet une unique solution $\alpha$ puis vérifier que $-2{,}5 < \alpha < -2$.

**5°)** Construire $(C)$ et $(C')$ représentant respectivement la fonction $f$ et sa réciproque $f^{-1}$ dans le repère $(O;\vec{i},\vec{j})$.

**6. a)** Déterminer la primitive $F$ de $f$ qui vérifie $F(0) = 0$.

Soit $A(\alpha)$ l'aire du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = \alpha$ et $x = 0$.

b) Calculer $A(\alpha)$ en fonction de $\alpha$. Montrer que $A(\alpha) = \dfrac{6 - 2\alpha - \alpha^2}{2}$.

**7. a)** Déterminer une équation de la tangente $(T)$ à $(C)$ au point d'abscisse $x_0 = \alpha$.

b) Vérifier que $\left(f^{-1}\right)'(0) = \dfrac{-1}{\alpha + 1}$.

**8)** On considère la fonction $g$ définie par $g(x) = \ln(x + 2 + e^x)$.

a) Déterminer l'ensemble de définition de $g$.

b) Dresser le tableau de variation de $g$.

c) Construire la courbe $(\Gamma)$ de $g$ dans un nouveau repère orthonormé $(O;\vec{u},\vec{v})$.
""", replace_ocr=True)

# ══════════════════════════════ 2010 — session complémentaire ═════════════════

_add("bac-d-2010-sc-math-ex1", "Suites numériques", r"""
**Exercice 1 (3 points)**

Pour chaque question ci-après, une seule réponse est exacte.

| N° | Question | Réponse A | Réponse B | Réponse C |
|---|---|---|---|---|
| 1 | $(U_n)$ est une suite arithmétique de raison $r = 3$ et telle que $U_5 = 17$, alors : | $U_{10} = 34$ | $U_{10} = 32$ | $U_{10} = 85$ |
| 2 | $(U_n)$ est une suite arithmétique de raison $r = 10$ et de premier terme $U_0 = \frac{11}{2}$ ; si $U_0 + U_1 + \dots + U_n = 2010$ alors : | $n = 19$ | $n = 20$ | $n = 21$ |
| 3 | Si $S_n = 1 + 2 + 2^2 + \dots + 2^n$ alors : | $S_n = 1 - 2^n$ | $S_n = 2^{n+1} - 1$ | $S_n = 2^n - 1$ |
| 4 | La suite de terme général $U_n = \dfrac{(-1)^n}{(-1)^n + n^2}$ | converge vers 1 | ne converge pas | converge vers 0 |
| 5 | La suite de terme général $U_n = \dfrac{10^n}{n!}$ est | croissante | décroissante | non monotone |
| 6 | Soient $(U_n)$ et $(V_n)$ deux suites numériques telles que $U_n \le V_n$. Si $(U_n)$ est croissante | $(U_n)$ est bornée | $(V_n)$ est bornée | $(V_n)$ est divergente |

Recopie sur la feuille et complète le tableau suivant en choisissant la bonne réponse.

| Question | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Réponse | | | | | | |
""", replace_ocr=True,
     note="Question 6 telle qu'imprimée : aucune des trois réponses n'est vraie en général (avec Uₙ ≤ Vₙ et (Uₙ) croissante, "
          "(Vₙ) est seulement minorée). Probable coquille du sujet (« (Vₙ) décroissante » rendrait la réponse A juste).")

_add("bac-d-2010-sc-math-ex2", "Nombres complexes", r"""
**Exercice 2 (4 points)**

**1.** Résoudre dans $\mathbb{C}$, l'ensemble des nombres complexes, l'équation $z^2 - 4z + 13 = 0$ et soient $z_1$ et $z_2$ ses solutions telles que $\operatorname{Im}(z_1) > 0$.

**2.** On considère dans le plan complexe les points $A$ et $B$ d'affixes respectives $z_A = 1 + z_1$ et $z_B = i + z_2$.

a) Écrire les nombres $z_A$ et $z_B$ sous forme algébrique et trigonométrique.

b) Représenter dans le repère $(O;\vec{i},\vec{j})$ les points $A$ et $B$. Déterminer la nature du triangle $OAB$.

c) Déterminer et placer le point $C$ tel que le quadrilatère $OACB$ soit un parallélogramme.

d) Déterminer et construire l'ensemble $\Gamma$ des points $M$ du plan d'affixe $z$ tels que le complexe $\dfrac{z - 2 + 2i}{z - 3 - 3i}$ soit imaginaire.
""", replace_ocr=True)

_add("bac-d-2010-sc-math-ex3", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 3 (6 points)**

On considère la fonction $f$ définie sur $]0;+\infty[$ par $f(x) = \dfrac{1}{x} + \ln x$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Calculer $\lim\limits_{x \to 0^+} f(x)$ et interpréter graphiquement.

b) Calculer $\lim\limits_{x \to +\infty} f(x)$ et $\lim\limits_{x \to +\infty} \big(f(x) - \ln x\big)$ et interpréter graphiquement.

**2. a)** Calculer $f'(x)$, où $f'$ est la dérivée de la fonction $f$.

b) Dresser le tableau de variation de $f$.

**3. a)** Dresser le tableau de variation de $\ln : x \mapsto \ln x$.

b) Tracer les courbes $(C)$ et $\Gamma$ représentatives de $f$ et de $\ln$ dans le repère $(O;\vec{i},\vec{j})$.

**4.** Soit $h$ la restriction de $f$ sur $I = ]1;+\infty[$.

a) Montrer que $h$ réalise une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Soit $(C')$ la courbe représentative de $h^{-1}$ dans le repère $(O;\vec{i},\vec{j})$. Étudier la position de $(C')$ avec sa tangente au point d'abscisse $x_0 = 1$.

c) Construire $(C')$ dans le repère $(O;\vec{i},\vec{j})$.

**5. a)** Calculer $A = \displaystyle\int_1^e \ln x\,dx$ (on pourra utiliser une intégration par parties).

b) En déduire l'aire $S$ du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = 1$ et $x = e$.
""", replace_ocr=True)

_add("bac-d-2010-sc-math-ex4", "Fonctions Logarithmes et Exponentielles", r"""
**Exercice 4 (7 points)**

On considère la fonction numérique $f$ définie sur $\mathbb{R}^*$ par $f(x) = \dfrac{e^x}{e^x - 1}$. Soit $(C)$ sa courbe représentative dans un repère orthonormé $(O;\vec{i},\vec{j})$ d'unité 1 cm.

**1. a)** Calculer $\lim\limits_{x \to 0^+} f(x)$, $\lim\limits_{x \to 0^-} f(x)$, $\lim\limits_{x \to -\infty} f(x)$ et $\lim\limits_{x \to +\infty} f(x)$.

b) En déduire que la courbe $(C)$ possède trois asymptotes dont on donnera des équations.

**2. a)** Calculer la dérivée de la fonction $f$ et vérifier que pour tout $x$ non nul : $f'(x) = -\dfrac{f(x)}{e^x - 1}$.

b) Dresser le tableau de variation de $f$.

**3. a)** Montrer que la fonction $g$, restriction de $f$ sur $I = ]0;+\infty[$, réalise une bijection de $I$ sur un intervalle $J$ que l'on déterminera.

b) Déterminer l'expression de la réciproque $g^{-1}$ de $g$.

**4. a)** Montrer que la courbe $(C)$ possède le point $\Omega\left(0;\dfrac{1}{2}\right)$ comme centre de symétrie.

b) Construire les courbes $(C)$ et $(C')$ représentatives des fonctions $f$ et $g^{-1}$ dans le repère $(O;\vec{i},\vec{j})$.

**5. a)** Déterminer une primitive $F$ de $f$ sur $I = ]0;+\infty[$.

b) Soit $n$ un entier naturel, $n \ge 1$, et $U_n$ l'aire du domaine plan limité par la courbe $(C)$, l'axe des abscisses et les droites d'équations respectives $x = \dfrac{1}{n}$ et $x = 1$. Calculer $U_n$ en fonction de $n$.

c) Calculer et interpréter graphiquement $\lim\limits_{n \to +\infty} U_n$.
""", ["Suites numériques"], replace_ocr=True)
