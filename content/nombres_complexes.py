"""Chapitre « Nombres complexes » — notions canoniques + cours (format court, 6 sections).

Rédigé à partir du programme officiel (Curricula de mathématiques IGENRSE 2022,
items CN143 à CN180) et des cours IPN « Nombres complexes 1 et 2 ».
Chaque item du programme est couvert par exactement une notion (champ ``programme``).

Séries (d'après le programme) : CN165-167, CN174-175 et CN176-179 sont en série C
uniquement ; tout le reste est commun aux séries C et D.

Chargé sur le serveur par ``scripts/load_chapter_content.py`` : les cours sont
insérés en BROUILLON (validated_by_admin = False) ; l'admin les relit et les
valide dans l'atelier chapitre.
"""

CHAPITRE = "Nombres complexes"
MATIERE = "math"
SOURCE = "Programme IGENRSE 2022 (CN143-CN180) + cours IPN Nombres complexes 1 et 2"

NOTIONS = [
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.forme-algebrique",
        "label": "Forme algébrique et calculs dans ℂ",
        "series": ["C", "D"],
        "programme": ["CN143", "CN144", "CN145", "CN146", "CN147", "CN148",
                      "CN149", "CN150", "CN151", "CN152", "CN153"],
        "keywords": ["forme algébrique", "forme algebrique", "partie réelle", "partie imaginaire",
                     "imaginaire pur"],
        "lesson": r"""## 1. L'idée en une phrase
Un nombre complexe s'écrit $z = x + iy$ avec $x, y$ réels et $i^2 = -1$ : on calcule comme dans $\mathbb{R}$, en remplaçant $i^2$ par $-1$.

## 2. Définitions
- $\mathbb{C} = \{x + iy \,/\, x \in \mathbb{R},\ y \in \mathbb{R}\}$ contient $\mathbb{R}$.
- L'écriture $z = x + iy$ est **unique** : c'est la forme algébrique de $z$.
- $\operatorname{Re}(z) = x$ est la partie réelle, $\operatorname{Im}(z) = y$ la partie imaginaire (ce sont deux **réels**).
- $z$ est **réel** $\iff \operatorname{Im}(z) = 0$ ; $z$ est **imaginaire pur** $\iff \operatorname{Re}(z) = 0$.
- Égalité : $x + iy = x' + iy' \iff x = x'$ et $y = y'$.

## 3. Propriétés à connaître
- Somme : $(x + iy) + (x' + iy') = (x + x') + i(y + y')$.
- Produit : $(x + iy)(x' + iy') = (xx' - yy') + i(xy' + x'y)$.
- Puissances de $i$ : $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, donc $i^n$ ne dépend que du reste de $n$ dans la division par 4.
- Inverse ($z \neq 0$) : $\dfrac{1}{x + iy} = \dfrac{x - iy}{x^2 + y^2}$.
- Identités remarquables valables dans $\mathbb{C}$ : $(a + ib)^2 = a^2 - b^2 + 2iab$ et $(a + ib)(a - ib) = a^2 + b^2$.

## 4. Méthodes
- **Mettre un quotient sous forme algébrique** : multiplier numérateur et dénominateur par le conjugué du dénominateur, qui devient le réel $x^2 + y^2$.
- **Montrer qu'un nombre est réel (ou imaginaire pur)** : l'écrire sous forme algébrique et vérifier que la partie imaginaire (ou réelle) est nulle.
- **Résoudre une égalité entre complexes** : identifier parties réelles et parties imaginaires.

## 5. Exemple corrigé
Écrire $z = \dfrac{5 + 6i}{1 + i}$ sous forme algébrique.

$z = \dfrac{(5 + 6i)(1 - i)}{(1 + i)(1 - i)} = \dfrac{5 - 5i + 6i - 6i^2}{1 + 1} = \dfrac{11 + i}{2}$, donc $z = \dfrac{11}{2} + \dfrac{1}{2}i$.

## 6. Pièges fréquents
- $i^2 = -1$, pas $1$.
- $\operatorname{Im}(3 - 2i) = -2$, pas $-2i$.
- $\dfrac{1}{a + ib} \neq \dfrac{1}{a} + \dfrac{1}{ib}$.
- On ne compare pas deux complexes avec $<$ ou $>$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.representation-geometrique",
        "label": "Représentation géométrique et affixes",
        "series": ["C", "D"],
        "programme": ["CN154", "CN155"],
        "keywords": ["affixe", "plan complexe", "point image"],
        "lesson": r"""## 1. L'idée en une phrase
Dans un repère orthonormé direct $(O ; \vec{u}, \vec{v})$, le point $M(x ; y)$ et le complexe $z = x + iy$ sont la même information : $z$ est l'**affixe** de $M$.

## 2. Définitions
- À tout point $M(x ; y)$ on associe $z_M = x + iy$ ; $M$ est le point image de $z$.
- Le vecteur $\vec{w}(x ; y)$ a pour affixe $x + iy$.
- L'axe des abscisses porte les réels, l'axe des ordonnées les imaginaires purs.

## 3. Propriétés à connaître
- Affixe du vecteur $\overrightarrow{AB}$ : $z_B - z_A$.
- Distance : $AB = |z_B - z_A|$.
- Milieu $I$ de $[AB]$ : $z_I = \dfrac{z_A + z_B}{2}$.
- Barycentre $G$ de $(A, \alpha), (B, \beta)$ avec $\alpha + \beta \neq 0$ : $z_G = \dfrac{\alpha z_A + \beta z_B}{\alpha + \beta}$.
- $\overrightarrow{AB} = \overrightarrow{DC} \iff z_B - z_A = z_C - z_D$.

## 4. Méthodes
- **Placer un point** : lire $\operatorname{Re}$ en abscisse, $\operatorname{Im}$ en ordonnée.
- **Montrer que $ABCD$ est un parallélogramme** : vérifier $z_B - z_A = z_C - z_D$ (ou que $[AC]$ et $[BD]$ ont le même milieu).
- **Trouver un point défini par une égalité vectorielle** : traduire chaque vecteur par sa différence d'affixes.

## 5. Exemple corrigé
$A(1 + 2i)$, $B(3 - i)$, $C(4 + i)$. Trouver $D$ tel que $ABCD$ soit un parallélogramme.

$ABCD$ parallélogramme $\iff \overrightarrow{AB} = \overrightarrow{DC} \iff z_B - z_A = z_C - z_D$, donc $z_D = z_A + z_C - z_B = 1 + 2i + 4 + i - 3 + i = 2 + 4i$.

Vérification : $z_B - z_A = 2 - 3i$ et $z_C - z_D = 2 - 3i$.

## 6. Pièges fréquents
- L'affixe de $\overrightarrow{AB}$ est $z_B - z_A$ (arrivée moins départ), pas $z_A - z_B$.
- Le repère doit être orthonormé **direct** pour parler d'angles et d'arguments.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.conjugue",
        "label": "Conjugué d'un nombre complexe",
        "series": ["C", "D"],
        "programme": ["CN156", "CN157"],
        "keywords": ["conjugu", "\\overline", "\\bar"],
        "lesson": r"""## 1. L'idée en une phrase
Le conjugué de $z = x + iy$ est $\overline{z} = x - iy$ : son point image est le symétrique de celui de $z$ par rapport à l'axe des abscisses.

## 2. Définitions
- $\overline{x + iy} = x - iy$ pour $x, y$ réels.
- Les points $M(z)$ et $M'(\overline{z})$ sont symétriques par rapport à $(O ; \vec{u})$.

## 3. Propriétés à connaître
- $z + \overline{z} = 2\operatorname{Re}(z)$ et $z - \overline{z} = 2i\operatorname{Im}(z)$.
- $z\overline{z} = x^2 + y^2 = |z|^2$ (un réel positif).
- $\overline{\overline{z}} = z$, $\overline{z + z'} = \overline{z} + \overline{z'}$, $\overline{zz'} = \overline{z}\,\overline{z'}$, $\overline{\left(\dfrac{z}{z'}\right)} = \dfrac{\overline{z}}{\overline{z'}}$, $\overline{z^n} = \overline{z}^{\,n}$.
- $z$ réel $\iff \overline{z} = z$ ; $z$ imaginaire pur $\iff \overline{z} = -z$.
- Si $|z| = 1$ alors $\overline{z} = \dfrac{1}{z}$.

## 4. Méthodes
- **Montrer que $Z$ est réel** : calculer $\overline{Z}$ avec les règles ci-dessus et montrer $\overline{Z} = Z$ (souvent plus rapide que la forme algébrique).
- **Montrer que $Z$ est imaginaire pur** : montrer $\overline{Z} = -Z$.
- **Polynôme à coefficients réels** : si $z_0$ est racine, alors $\overline{z_0}$ l'est aussi.

## 5. Exemple corrigé
Soit $z$ tel que $|z| = 1$ et $z \neq 1$. Montrer que $Z = \dfrac{1 + z}{1 - z}$ est imaginaire pur.

Comme $|z| = 1$, $\overline{z} = \dfrac{1}{z}$. Donc $\overline{Z} = \dfrac{1 + \frac{1}{z}}{1 - \frac{1}{z}} = \dfrac{z + 1}{z - 1} = -\dfrac{1 + z}{1 - z} = -Z$ : $Z$ est imaginaire pur.

## 6. Pièges fréquents
- $\overline{iz} = -i\,\overline{z}$ (le conjugué de $i$ est $-i$).
- La règle « $\overline{z_0}$ est aussi racine » ne vaut que pour un polynôme à coefficients **réels**.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.module",
        "label": "Module d'un nombre complexe",
        "series": ["C", "D"],
        "programme": ["CN158", "CN159"],
        "keywords": ["module", "|z"],
        "lesson": r"""## 1. L'idée en une phrase
Le module $|z|$ est la distance $OM$ entre l'origine et le point image de $z$ ; $|z_B - z_A|$ est la distance $AB$.

## 2. Définitions
- Pour $z = x + iy$ : $|z| = \sqrt{x^2 + y^2} = OM$.
- $|z|^2 = z\overline{z}$.

## 3. Propriétés à connaître
- $|z| = 0 \iff z = 0$ ; $|-z| = |\overline{z}| = |z|$.
- $|zz'| = |z|\,|z'|$, $\left|\dfrac{z}{z'}\right| = \dfrac{|z|}{|z'|}$, $|z^n| = |z|^n$.
- Inégalité triangulaire : $|z + z'| \leq |z| + |z'|$.
- $AB = |z_B - z_A|$.

## 4. Méthodes
- **Ensemble des points $M(z)$ tels que $|z - a| = r$** ($r > 0$) : cercle de centre $A(a)$ et de rayon $r$.
- **Ensemble des points tels que $|z - a| = |z - b|$** : médiatrice de $[AB]$.
- **Nature d'un triangle** : calculer les longueurs des côtés avec des modules.
- **Module d'un produit ou d'un quotient** : utiliser les propriétés, sans développer.

## 5. Exemple corrigé
Déterminer l'ensemble $E$ des points $M(z)$ tels que $|z + 1 + 2i| = |z - 4|$.

$|z + 1 + 2i| = |z - (-1 - 2i)| = AM$ avec $A(-1 - 2i)$, et $|z - 4| = BM$ avec $B(4)$. Donc $AM = BM$ : $E$ est la médiatrice de $[AB]$.

## 6. Pièges fréquents
- $|x + iy| = \sqrt{x^2 + y^2}$, jamais $x + y$.
- $|z + z'| \neq |z| + |z'|$ en général.
- Bien écrire $|z - a|$ sous la forme « $z$ moins l'affixe du centre » : $|z + 2i| = |z - (-2i)|$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.argument",
        "label": "Argument d'un nombre complexe non nul",
        "series": ["C", "D"],
        "programme": ["CN160", "CN161"],
        "keywords": ["argument", "arg("],
        "lesson": r"""## 1. L'idée en une phrase
Un argument de $z \neq 0$ est une mesure de l'angle orienté $(\vec{u}, \overrightarrow{OM})$ : il donne la direction du point image, à $2\pi$ près.

## 2. Définitions
- Pour $z \neq 0$ : $\arg z \equiv (\vec{u}, \overrightarrow{OM}) \ [2\pi]$.
- Si $\theta = \arg z$ et $r = |z|$ : $\cos\theta = \dfrac{x}{r}$ et $\sin\theta = \dfrac{y}{r}$.
- $0$ n'a pas d'argument.

## 3. Propriétés à connaître
- $\arg(zz') \equiv \arg z + \arg z' \ [2\pi]$ ; $\arg\left(\dfrac{1}{z}\right) \equiv -\arg z$ ; $\arg\left(\dfrac{z}{z'}\right) \equiv \arg z - \arg z'$ ; $\arg(z^n) \equiv n\arg z$.
- $\arg \overline{z} \equiv -\arg z$ et $\arg(-z) \equiv \arg z + \pi \ [2\pi]$.
- $z$ réel non nul $\iff \arg z \equiv 0 \ [\pi]$ ; $z$ imaginaire pur non nul $\iff \arg z \equiv \dfrac{\pi}{2} \ [\pi]$.
- Angle de deux vecteurs : $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \arg\left(\dfrac{z_C - z_A}{z_B - z_A}\right) \ [2\pi]$.

## 4. Méthodes
- **Trouver un argument** : calculer $r = |z|$, puis $\cos\theta = \dfrac{x}{r}$ et $\sin\theta = \dfrac{y}{r}$, et reconnaître un angle remarquable.
- **Argument d'un produit ou d'un quotient** : additionner ou soustraire les arguments connus.
- **Ensemble des points tels que $\arg z \equiv \theta \ [2\pi]$** : demi-droite d'origine $O$ (privée de $O$) dirigée selon l'angle $\theta$.

## 5. Exemple corrigé
Trouver un argument de $Z = \dfrac{1 + i}{1 - i\sqrt{3}}$.

$|1 + i| = \sqrt{2}$, $\cos\theta = \sin\theta = \dfrac{\sqrt{2}}{2}$, donc $\arg(1 + i) \equiv \dfrac{\pi}{4}$. $|1 - i\sqrt{3}| = 2$, $\cos\theta' = \dfrac{1}{2}$, $\sin\theta' = -\dfrac{\sqrt{3}}{2}$, donc $\arg(1 - i\sqrt{3}) \equiv -\dfrac{\pi}{3}$.

Donc $\arg Z \equiv \dfrac{\pi}{4} - \left(-\dfrac{\pi}{3}\right) = \dfrac{7\pi}{12} \ [2\pi]$.

## 6. Pièges fréquents
- $\theta = \arctan\dfrac{y}{x}$ est faux quand $x < 0$ : utiliser $\cos\theta$ **et** $\sin\theta$.
- $\arg(z + z') \neq \arg z + \arg z'$.
- Toujours préciser « à $2\pi$ près » (ou « à $\pi$ près »).
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.forme-trigo-exponentielle",
        "label": "Formes trigonométrique et exponentielle",
        "series": ["C", "D"],
        "programme": ["CN162", "CN163", "CN164"],
        "keywords": ["forme trigonométrique", "forme trigonometrique", "forme exponentielle",
                     "e^{i"],
        "lesson": r"""## 1. L'idée en une phrase
Tout complexe non nul s'écrit $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$ avec $r = |z| > 0$ et $\theta = \arg z$ : c'est la forme idéale pour multiplier, diviser et calculer des puissances.

## 2. Définitions
- Forme trigonométrique : $z = r(\cos\theta + i\sin\theta)$, $r > 0$.
- Notation : $e^{i\theta} = \cos\theta + i\sin\theta$ ; forme exponentielle : $z = re^{i\theta}$.
- Valeurs à connaître : $e^{i0} = 1$, $e^{i\pi/2} = i$, $e^{i\pi} = -1$, $e^{-i\pi/2} = -i$.

## 3. Propriétés à connaître
- $re^{i\theta} = r'e^{i\theta'} \iff r = r'$ et $\theta \equiv \theta' \ [2\pi]$.
- $e^{i\theta} \times e^{i\theta'} = e^{i(\theta + \theta')}$, $\dfrac{e^{i\theta}}{e^{i\theta'}} = e^{i(\theta - \theta')}$, $(e^{i\theta})^n = e^{in\theta}$.
- $\overline{e^{i\theta}} = e^{-i\theta}$ et $|e^{i\theta}| = 1$.

## 4. Méthodes
- **Algébrique → exponentielle** : calculer $r = \sqrt{x^2 + y^2}$, factoriser $z = r\left(\dfrac{x}{r} + i\dfrac{y}{r}\right)$ et reconnaître $\cos\theta$ et $\sin\theta$.
- **Exponentielle → algébrique** : $x = r\cos\theta$, $y = r\sin\theta$.
- **Puissance** : passer en exponentielle, puis $z^n = r^n e^{in\theta}$.
- **Ramener à $r > 0$** : $-2e^{i\theta} = 2e^{i(\theta + \pi)}$.

## 5. Exemple corrigé
Calculer $(1 + i\sqrt{3})^6$.

$|1 + i\sqrt{3}| = 2$ et $1 + i\sqrt{3} = 2\left(\dfrac{1}{2} + i\dfrac{\sqrt{3}}{2}\right) = 2e^{i\pi/3}$. Donc $(1 + i\sqrt{3})^6 = 2^6 e^{i6\pi/3} = 64e^{2i\pi} = 64$.

## 6. Pièges fréquents
- Dans $re^{i\theta}$, $r$ doit être **strictement positif** : $-3e^{i\pi/4}$ n'est pas une forme exponentielle.
- $\cos\theta - i\sin\theta = e^{-i\theta}$, et $\sin\theta + i\cos\theta = e^{i(\pi/2 - \theta)}$ (ne pas confondre).
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.euler-moivre",
        "label": "Formules d'Euler, de Moivre et linéarisation",
        "series": ["C"],
        "programme": ["CN165", "CN166", "CN167"],
        "keywords": ["moivre", "euler", "linéaris", "linearis"],
        "lesson": r"""## 1. L'idée en une phrase
Les formules d'Euler et de Moivre font passer des puissances de $\cos$ et $\sin$ aux cosinus et sinus d'angles multiples, et inversement.

## 2. Définitions
- Formules d'Euler : $\cos\theta = \dfrac{e^{i\theta} + e^{-i\theta}}{2}$ et $\sin\theta = \dfrac{e^{i\theta} - e^{-i\theta}}{2i}$.
- Formule de Moivre : $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ pour $n \in \mathbb{Z}$.
- Linéariser $\cos^n\theta$ ou $\sin^n\theta$ : l'écrire comme une somme de $\cos k\theta$ et $\sin k\theta$.

## 3. Propriétés à connaître
- $e^{i\theta} + e^{-i\theta} = 2\cos\theta$ et $e^{i\theta} - e^{-i\theta} = 2i\sin\theta$.
- Angle moitié : $1 + e^{i\theta} = e^{i\theta/2}\left(e^{-i\theta/2} + e^{i\theta/2}\right) = 2\cos\dfrac{\theta}{2}\,e^{i\theta/2}$.
- $1 - e^{i\theta} = -2i\sin\dfrac{\theta}{2}\,e^{i\theta/2}$.

## 4. Méthodes
- **Exprimer $\cos n\theta$ en fonction de $\cos\theta$** : développer $(\cos\theta + i\sin\theta)^n$ avec le binôme, puis identifier la partie réelle (et la partie imaginaire pour $\sin n\theta$).
- **Linéariser** : remplacer $\cos\theta$ (ou $\sin\theta$) par la formule d'Euler, développer, regrouper $e^{ik\theta}$ et $e^{-ik\theta}$.
- **Module et argument de $1 + e^{i\theta}$** : factoriser par l'angle moitié, puis discuter le signe de $\cos\dfrac{\theta}{2}$.

## 5. Exemple corrigé
Linéariser $\cos^3\theta$.

$\cos^3\theta = \left(\dfrac{e^{i\theta} + e^{-i\theta}}{2}\right)^3 = \dfrac{e^{3i\theta} + 3e^{i\theta} + 3e^{-i\theta} + e^{-3i\theta}}{8} = \dfrac{2\cos 3\theta + 6\cos\theta}{8}$.

Donc $\cos^3\theta = \dfrac{1}{4}\cos 3\theta + \dfrac{3}{4}\cos\theta$.

## 6. Pièges fréquents
- Le dénominateur de la formule de $\sin\theta$ est $2i$, pas $2$.
- Ne pas oublier le $2^n$ au dénominateur quand on élève la formule d'Euler à la puissance $n$.
- $2\cos\dfrac{\theta}{2}\,e^{i\theta/2}$ n'est une forme exponentielle que si $\cos\dfrac{\theta}{2} > 0$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.equations-premier-degre",
        "label": "Équations du premier degré et équations avec z̄",
        "series": ["C", "D"],
        "programme": ["CN168", "CN169"],
        "keywords": ["premier degré", "premier degre", "\\overline{z}", "\\bar{z}", "\\bar z"],
        "lesson": r"""## 1. L'idée en une phrase
Une équation où $z$ apparaît seul se résout comme dans $\mathbb{R}$ ; dès que $\overline{z}$ apparaît, on pose $z = x + iy$ et on identifie parties réelle et imaginaire.

## 2. Définitions
- $az = b$ avec $a \neq 0$ : solution unique $z = \dfrac{b}{a}$.
- Équation du type $az + b\overline{z} = c$ ($a, b, c$ complexes) : on cherche $z = x + iy$ avec $x, y$ réels.

## 3. Propriétés à connaître
- Deux complexes sont égaux si et seulement si leurs parties réelles **et** leurs parties imaginaires sont égales.
- Si $z = x + iy$ alors $\overline{z} = x - iy$.
- Un système de deux équations à deux inconnues complexes $z$ et $z'$ se résout par substitution ou par combinaison, comme dans $\mathbb{R}$.

## 4. Méthodes
- **Équation en $z$ seulement** : isoler $z$, puis mettre le résultat sous forme algébrique.
- **Équation avec $\overline{z}$** : poser $z = x + iy$, développer, écrire le tout sous la forme $A + iB = c$, puis résoudre le système réel obtenu.

## 5. Exemple corrigé
Résoudre dans $\mathbb{C}$ : $2z + i\overline{z} = 3$.

On pose $z = x + iy$ : $2x + 2iy + i(x - iy) = (2x + y) + i(x + 2y)$. On obtient le système $2x + y = 3$ et $x + 2y = 0$, d'où $x = -2y$, puis $-3y = 3$ : $y = -1$ et $x = 2$.

Solution : $z = 2 - i$. Vérification : $2(2 - i) + i(2 + i) = 4 - 2i + 2i - 1 = 3$.

## 6. Pièges fréquents
- On ne peut pas « diviser par $\overline{z}$ » pour isoler $z$ quand $z$ et $\overline{z}$ apparaissent tous les deux.
- L'identification n'est valable que si $x$ et $y$ sont **réels**.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.racines-carrees",
        "label": "Racines carrées d'un nombre complexe",
        "series": ["C", "D"],
        "programme": ["CN173"],
        "keywords": ["racine carrée", "racines carrées", "racine carree", "racines carrees"],
        "lesson": r"""## 1. L'idée en une phrase
Tout complexe $Z \neq 0$ a exactement deux racines carrées opposées $\delta$ et $-\delta$, qu'on trouve en posant $\delta = x + iy$.

## 2. Définitions
- $\delta$ est une racine carrée de $Z$ si $\delta^2 = Z$.
- Si $Z = a$ est réel : pour $a > 0$, les racines sont $\pm\sqrt{a}$ ; pour $a < 0$, ce sont $\pm i\sqrt{-a}$.

## 3. Propriétés à connaître
Si $\delta = x + iy$ est une racine carrée de $Z$, alors :
- $x^2 - y^2 = \operatorname{Re}(Z)$ (égalité des parties réelles) ;
- $x^2 + y^2 = |Z|$ (égalité des modules) ;
- $2xy = \operatorname{Im}(Z)$, qui donne le **signe** de $xy$.

En forme exponentielle : si $Z = re^{i\theta}$, alors $\delta = \pm\sqrt{r}\,e^{i\theta/2}$.

## 4. Méthodes
- **Méthode algébrique** : écrire les trois équations ci-dessus, en déduire $x^2$ et $y^2$, puis choisir les signes grâce à $xy$.
- **Méthode exponentielle** : à utiliser quand $Z$ a un argument remarquable.

## 5. Exemple corrigé
Racines carrées de $Z = -5 + 12i$.

$|Z| = \sqrt{25 + 144} = 13$. Le système $x^2 - y^2 = -5$, $x^2 + y^2 = 13$ donne $x^2 = 4$ et $y^2 = 9$. Comme $2xy = 12 > 0$, $x$ et $y$ ont le même signe.

Les racines carrées sont $2 + 3i$ et $-2 - 3i$. Vérification : $(2 + 3i)^2 = 4 + 12i - 9 = -5 + 12i$.

## 6. Pièges fréquents
- Ne jamais écrire $\sqrt{-5 + 12i}$ : le symbole $\sqrt{\phantom{x}}$ est réservé aux réels positifs.
- Ne pas oublier l'équation des modules, qui rend le calcul immédiat.
- Bien utiliser le signe de $xy$ pour ne pas garder quatre « racines ».
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.equation-second-degre",
        "label": "Équation du second degré dans ℂ",
        "series": ["C", "D"],
        "programme": ["CN170", "CN171"],
        "keywords": ["second degré", "second degre", "discriminant", "z^2", "z²"],
        "lesson": r"""## 1. L'idée en une phrase
Dans $\mathbb{C}$, toute équation $az^2 + bz + c = 0$ ($a \neq 0$) a deux solutions (éventuellement confondues), données par $\dfrac{-b \pm \delta}{2a}$ où $\delta^2 = \Delta$.

## 2. Définitions
- Discriminant : $\Delta = b^2 - 4ac$ ; $\delta$ est une racine carrée (complexe) de $\Delta$.
- Si $b = 2b'$ : discriminant réduit $\Delta' = b'^2 - ac$ et solutions $\dfrac{-b' \pm \delta'}{a}$.

## 3. Propriétés à connaître
- Solutions : $z_1 = \dfrac{-b + \delta}{2a}$ et $z_2 = \dfrac{-b - \delta}{2a}$ ; si $\Delta = 0$, solution double $-\dfrac{b}{2a}$.
- **Coefficients réels** : si $\Delta < 0$, les solutions sont $\dfrac{-b \pm i\sqrt{-\Delta}}{2a}$, deux complexes **conjugués**.
- Somme et produit : $z_1 + z_2 = -\dfrac{b}{a}$ et $z_1 z_2 = \dfrac{c}{a}$.

## 4. Méthodes
- **Coefficients réels** : calculer $\Delta$ (ou $\Delta'$) et conclure selon son signe.
- **Coefficients complexes** : calculer $\Delta$, chercher une racine carrée $\delta$ par la méthode algébrique, puis appliquer la formule.
- **Vérifier** avec la somme et le produit des racines.

## 5. Exemple corrigé
Résoudre $z^2 - (3 + 4i)z - 1 + 5i = 0$.

$\Delta = (3 + 4i)^2 - 4(-1 + 5i) = (9 + 24i - 16) + 4 - 20i = -3 + 4i$. Pour $\delta = x + iy$ : $x^2 - y^2 = -3$, $x^2 + y^2 = |\Delta| = 5$, $xy > 0$, donc $\delta = 1 + 2i$.

$z_1 = \dfrac{3 + 4i + 1 + 2i}{2} = 2 + 3i$ et $z_2 = \dfrac{3 + 4i - 1 - 2i}{2} = 1 + i$.

Vérification : $z_1 + z_2 = 3 + 4i$ et $z_1 z_2 = (2 + 3i)(1 + i) = -1 + 5i$.

## 6. Pièges fréquents
- Avec des coefficients complexes, les solutions ne sont **pas** conjuguées en général.
- « $\Delta < 0$ » n'a de sens que si $\Delta$ est réel.
- Écrire $\delta$, pas $\sqrt{\Delta}$, quand $\Delta$ n'est pas un réel positif.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.equation-troisieme-degre",
        "label": "Équation du troisième degré et factorisation de polynômes",
        "series": ["C", "D"],
        "programme": ["CN172"],
        "keywords": ["p(z)", "polynôme", "polynome", "z^3", "z³", "troisième degré", "troisieme degre"],
        "lesson": r"""## 1. L'idée en une phrase
Pour résoudre $P(z) = 0$ avec $P$ de degré 3, on trouve une racine $z_0$, on factorise $P(z) = (z - z_0)Q(z)$ avec $Q$ de degré 2, puis on résout $Q(z) = 0$.

## 2. Définitions
- $z_0$ est racine de $P$ si $P(z_0) = 0$.
- Si $z_0$ est racine, il existe $a, b, c$ tels que $P(z) = (z - z_0)(az^2 + bz + c)$.

## 3. Propriétés à connaître
- Le coefficient de $z^3$ de $P$ donne $a$, et le terme constant donne $-z_0 c$.
- Si $P$ est à coefficients **réels** et $z_0$ racine, alors $\overline{z_0}$ est aussi racine.
- Une racine **imaginaire pure** s'écrit $z_0 = iy$ avec $y$ réel ; une racine **réelle** s'écrit $z_0 = x$.

## 4. Méthodes
- **Racine imaginaire pure (ou réelle)** : remplacer $z$ par $iy$ (ou $x$), séparer partie réelle et partie imaginaire ; les deux doivent être nulles **pour le même** $y$.
- **Factoriser** : identifier les coefficients de $(z - z_0)(az^2 + bz + c)$ avec ceux de $P$, ou utiliser le schéma de Horner.
- **Finir** : résoudre $az^2 + bz + c = 0$ (voir l'équation du second degré).

## 5. Exemple corrigé
$P(z) = z^3 - (4 + i)z^2 + (5 + 4i)z - 5i$. Montrer que $P$ a une racine imaginaire pure, puis résoudre $P(z) = 0$.

Avec $z = iy$ : $P(iy) = (4y^2 - 4y) + i(-y^3 + y^2 + 5y - 5)$. La partie réelle est nulle pour $y = 0$ ou $y = 1$ ; la partie imaginaire vaut $-5$ pour $y = 0$ et $0$ pour $y = 1$. Donc $z_0 = i$.

Par identification, $P(z) = (z - i)(z^2 - 4z + 5)$. Pour $z^2 - 4z + 5 = 0$ : $\Delta' = 4 - 5 = -1$, donc $z = 2 \pm i$.

Solutions : $i$, $2 + i$ et $2 - i$.

## 6. Pièges fréquents
- Vérifier que la racine trouvée annule bien $P$ avant de factoriser.
- Pour une racine imaginaire pure, il faut que la partie réelle **et** la partie imaginaire s'annulent pour la même valeur de $y$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.racines-n-iemes",
        "label": "Racines n-ièmes de l'unité et d'un complexe",
        "series": ["C"],
        "programme": ["CN174", "CN175"],
        "keywords": ["racines n", "racine n", "racines cubiques", "racine cubique", "racines de l'unité",
                     "racines de l’unité", "z^n", "1 + j + j"],
        "lesson": r"""## 1. L'idée en une phrase
L'équation $z^n = Z$ ($Z \neq 0$) a exactement $n$ solutions, obtenues en prenant la racine $n$-ième du module et en divisant l'argument par $n$, à $\dfrac{2\pi}{n}$ près.

## 2. Définitions
- Racines $n$-ièmes de l'unité : solutions de $z^n = 1$, soit $\omega_k = e^{2ik\pi/n}$ pour $k = 0, 1, \ldots, n - 1$.
- Racines cubiques de l'unité : $1$, $j = e^{2i\pi/3} = -\dfrac{1}{2} + i\dfrac{\sqrt{3}}{2}$ et $j^2 = \overline{j}$.

## 3. Propriétés à connaître
- $1 + \omega_1 + \cdots + \omega_{n-1} = 0$ pour $n \geq 2$ ; en particulier $1 + j + j^2 = 0$ et $j^3 = 1$.
- Les images des racines $n$-ièmes de l'unité sont les sommets d'un polygone régulier à $n$ côtés inscrit dans le cercle trigonométrique.
- Si $Z = re^{i\theta}$, les racines $n$-ièmes de $Z$ sont $z_k = \sqrt[n]{r}\,e^{i\frac{\theta + 2k\pi}{n}}$, $k = 0, \ldots, n - 1$.

## 4. Méthodes
- **Résoudre $z^n = Z$** : écrire $Z = re^{i\theta}$ et chercher $z = \rho e^{i\alpha}$ : $\rho^n = r$ et $n\alpha \equiv \theta \ [2\pi]$.
- **Utiliser $1 + j + j^2 = 0$** pour simplifier des sommes ou montrer qu'un triangle est équilatéral.

## 5. Exemple corrigé
Résoudre $z^3 = 8i$.

$8i = 8e^{i\pi/2}$. Avec $z = \rho e^{i\alpha}$ : $\rho^3 = 8$ donc $\rho = 2$, et $3\alpha \equiv \dfrac{\pi}{2} \ [2\pi]$ donc $\alpha = \dfrac{\pi}{6} + \dfrac{2k\pi}{3}$.

- $k = 0$ : $2e^{i\pi/6} = \sqrt{3} + i$ ;
- $k = 1$ : $2e^{5i\pi/6} = -\sqrt{3} + i$ ;
- $k = 2$ : $2e^{3i\pi/2} = -2i$.

## 6. Pièges fréquents
- Il y a $n$ solutions : $k$ va de $0$ à $n - 1$ (au-delà, on retrouve les mêmes).
- On divise **tout** l'argument $\theta + 2k\pi$ par $n$, pas seulement $\theta$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.ecriture-complexe-transformations",
        "label": "Écriture complexe des transformations (translation, homothétie, rotation, similitude directe)",
        "series": ["C"],
        "programme": ["CN176", "CN177", "CN178", "CN179"],
        "keywords": ["translation", "homothétie", "homothetie", "rotation", "similitude", "z' =", "z'="],
        "lesson": r"""## 1. L'idée en une phrase
Une transformation du plan qui s'écrit $z' = az + b$ ($a \neq 0$) est une similitude directe ; selon $a$, c'est une translation, une homothétie ou une rotation.

## 2. Définitions
- Translation de vecteur $\vec{w}(b)$ : $z' = z + b$.
- Homothétie de centre $\Omega(\omega)$ et de rapport $k$ réel non nul : $z' - \omega = k(z - \omega)$.
- Rotation de centre $\Omega(\omega)$ et d'angle $\theta$ : $z' - \omega = e^{i\theta}(z - \omega)$.
- Similitude directe : $z' = az + b$ avec $a \in \mathbb{C}^*$.

## 3. Propriétés à connaître
Pour $z' = az + b$ :
- si $a = 1$ : translation de vecteur d'affixe $b$ ;
- si $a \neq 1$ : un seul point fixe, le centre $\omega = \dfrac{b}{1 - a}$ ; le rapport est $|a|$ et l'angle est $\arg a$ ;
- $a$ réel ($\neq 1$) : homothétie de rapport $a$ ; $|a| = 1$ ($a \neq 1$) : rotation d'angle $\arg a$.

Une similitude directe multiplie les distances par $|a|$ et conserve les angles orientés. Si elle transforme $A$ en $A'$ et $B$ en $B'$, alors $a = \dfrac{z_{B'} - z_{A'}}{z_B - z_A}$.

## 4. Méthodes
- **Reconnaître une transformation** : mettre l'écriture sous la forme $z' = az + b$, puis calculer $|a|$, $\arg a$ et le centre.
- **Écrire une transformation donnée** : utiliser la forme « $z' - \omega = \ldots(z - \omega)$ ».
- **Déterminer la similitude envoyant $A$ sur $A'$ et $B$ sur $B'$** : calculer $a$ par la formule, puis $b = z_{A'} - az_A$.

## 5. Exemple corrigé
Nature et éléments de $s : z' = (1 + i)z + 1 - 2i$.

$a = 1 + i = \sqrt{2}e^{i\pi/4}$ : rapport $\sqrt{2}$, angle $\dfrac{\pi}{4}$. Centre : $\omega = \dfrac{1 - 2i}{1 - (1 + i)} = \dfrac{1 - 2i}{-i} = i(1 - 2i) = 2 + i$.

$s$ est la similitude directe de centre $\Omega(2 + i)$, de rapport $\sqrt{2}$ et d'angle $\dfrac{\pi}{4}$. Vérification : $(1 + i)(2 + i) + 1 - 2i = 1 + 3i + 1 - 2i = 2 + i$.

## 6. Pièges fréquents
- Le rapport d'une similitude est $|a|$, pas $a$.
- Pour une homothétie, le rapport $k$ est **réel** (il peut être négatif) ; $z' = -z$ est la symétrie de centre $O$.
- La formule du centre $\omega = \dfrac{b}{1 - a}$ n'existe que pour $a \neq 1$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    {
        "id": "math.complexes.applications-geometriques",
        "label": "Applications géométriques des nombres complexes",
        "series": ["C", "D"],
        "programme": ["CN180"],
        "keywords": ["ensemble des points", "triangle", "cercle", "aligné", "aligne", "carré", "parallélogramme",
                     "losange", "rectangle", "équilatéral", "equilateral", "isocèle", "isocele", "médiatrice"],
        "lesson": r"""## 1. L'idée en une phrase
Le quotient $Z = \dfrac{z_C - z_A}{z_B - z_A}$ contient toute la géométrie de l'angle en $A$ : son module donne $\dfrac{AC}{AB}$ et son argument donne l'angle $(\overrightarrow{AB}, \overrightarrow{AC})$.

## 2. Définitions
- $|Z| = \dfrac{AC}{AB}$ et $\arg Z \equiv (\overrightarrow{AB}, \overrightarrow{AC}) \ [2\pi]$.
- Ensemble de points (lieu géométrique) : ensemble des points $M(z)$ vérifiant une condition sur $z$.

## 3. Propriétés à connaître
- $A$, $B$, $C$ alignés $\iff Z$ réel.
- $(AB) \perp (AC) \iff Z$ imaginaire pur.
- $ABC$ isocèle en $A \iff |Z| = 1$ ; rectangle isocèle en $A \iff Z = \pm i$ ; équilatéral $\iff Z = e^{\pm i\pi/3}$.
- Pour $Z = \dfrac{z - b}{z - a}$ avec $A(a)$, $B(b)$ :
    - $|Z| = 1$ : médiatrice de $[AB]$ ;
    - $Z$ réel : droite $(AB)$ privée de $A$ ;
    - $Z$ imaginaire pur : cercle de diamètre $[AB]$ privé de $A$.
- $A$, $B$, $C$, $D$ sont sur le cercle de centre $\Omega$ et de rayon $r$ si $|z_A - \omega| = \cdots = |z_D - \omega| = r$.

## 4. Méthodes
- **Nature d'un triangle** : calculer $Z = \dfrac{z_C - z_A}{z_B - z_A}$ sous forme algébrique ou exponentielle, puis lire module et argument.
- **Nature d'un quadrilatère** : parallélogramme (mêmes milieux des diagonales), puis losange (côtés égaux), rectangle (angle droit) ou carré (les deux).
- **Lieu géométrique** : interpréter la condition avec des distances (modules) ou des angles (arguments) ; sinon poser $z = x + iy$ et reconnaître une équation de droite ou de cercle.

## 5. Exemple corrigé
$A(1 + i)$, $B(3 + 2i)$, $C(3i)$. Quelle est la nature du triangle $ABC$ ?

$Z = \dfrac{z_C - z_A}{z_B - z_A} = \dfrac{-1 + 2i}{2 + i} = \dfrac{(-1 + 2i)(2 - i)}{5} = \dfrac{-2 + i + 4i + 2}{5} = i$.

$|Z| = 1$ donc $AC = AB$, et $\arg Z \equiv \dfrac{\pi}{2}$ donc $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \dfrac{\pi}{2}$ : $ABC$ est rectangle isocèle en $A$ (direct).

## 6. Pièges fréquents
- L'ordre compte : $\arg\dfrac{z_C - z_A}{z_B - z_A}$ mesure $(\overrightarrow{AB}, \overrightarrow{AC})$, pas $(\overrightarrow{AC}, \overrightarrow{AB})$.
- Exclure les points qui annulent un dénominateur.
- « Imaginaire pur » inclut $0$ : vérifier si le point correspondant appartient à l'ensemble.
""",
    },
]
