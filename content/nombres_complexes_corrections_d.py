"""Nombres complexes — série D, 2015-2024 : énoncés vérifiés + corrections.

Énoncés retranscrits depuis les sujets originaux (PDF du dossier
drive_archive/annals/Sujets corrigés math/bac d), en remplacement du texte OCR.
Toutes les valeurs numériques des corrections ont été vérifiées par calcul formel.

Chargé par ``scripts/load_chapter_content.py nombres_complexes --corrections
nombres_complexes_corrections_d`` : un exercice déjà validé par l'admin n'est
jamais modifié ; l'énoncé OCR remplacé est conservé dans ``ennonce_ocr``.
"""

CORRECTIONS = {
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2015-sc-math-ex2": {
        "enonce": r"""**1)** On considère, dans $\mathbb{C}$, les équations $E_1 : z^2 - 6z + 25 = 0$ et $E_2 : z^2 - 8z + 25 = 0$.

a) Résoudre $E_1$. On note $z_1$ et $z_2$ ses solutions avec $\operatorname{Im}(z_1) > 0$.

b) Résoudre $E_2$. On note $z_3$ et $z_4$ ses solutions avec $\operatorname{Im}(z_3) > 0$.

c) Écrire sous forme trigonométrique les nombres $z_1 + z_3$ et $z_1 \times z_3$.

**2)** Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$. Pour tout nombre complexe $z \neq 3 + 4i$, on pose $f(z) = \dfrac{z - 4 - 3i}{z - 3 - 4i}$. On considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 3 + 4i$, $z_B = 4 + 3i$ et $z_C = 4 + 4i$.

a) Placer les points $A$, $B$ et $C$ dans le repère.

b) Calculer et mettre sous forme algébrique le nombre complexe $f(4 + 4i)$. Interpréter graphiquement.

c) Déterminer et représenter les ensembles de points $M$ du plan d'affixe $z$ :
- $\Gamma_1$ tel que $|f(z)| = 1$ ;
- $\Gamma_2$ tel que $f(z)$ soit imaginaire pur.
""",
        "correction": r"""**1) a)** $\Delta' = (-3)^2 - 25 = -16 = (4i)^2$, donc $z_1 = 3 + 4i$ et $z_2 = 3 - 4i$.

**b)** $\Delta' = (-4)^2 - 25 = -9 = (3i)^2$, donc $z_3 = 4 + 3i$ et $z_4 = 4 - 3i$.

**c)** $z_1 + z_3 = 7 + 7i = 7\sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right) = 7\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$.

$z_1 z_3 = (3 + 4i)(4 + 3i) = 12 + 9i + 16i - 12 = 25i = 25\left(\cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}\right)$.

**2) a)** $A(3 ; 4)$, $B(4 ; 3)$, $C(4 ; 4)$.

**b)** $f(4 + 4i) = \dfrac{4 + 4i - 4 - 3i}{4 + 4i - 3 - 4i} = \dfrac{i}{1} = i$.

Pour $z \neq z_A$ : $f(z) = \dfrac{z - z_B}{z - z_A}$, donc $|f(z)| = \dfrac{MB}{MA}$ et $\arg f(z) \equiv (\overrightarrow{MA}, \overrightarrow{MB}) \ [2\pi]$.

$f(z_C) = i$ donne $\dfrac{CB}{CA} = 1$ et $(\overrightarrow{CA}, \overrightarrow{CB}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $ABC$ est **rectangle isocèle en $C$**.

**c)** $M \in \Gamma_1 \iff MB = MA$ : $\Gamma_1$ est la **médiatrice de $[AB]$**. Elle passe par le milieu $\left(\frac{7}{2} ; \frac{7}{2}\right)$ et est perpendiculaire à $\overrightarrow{AB}(1 ; -1)$ : c'est la droite d'équation $y = x$.

$f(z)$ imaginaire pur $\iff f(z) = 0$ (soit $M = B$) ou $(\overrightarrow{MA}, \overrightarrow{MB}) \equiv \dfrac{\pi}{2} \ [\pi]$. Donc $\Gamma_2$ est le **cercle de diamètre $[AB]$ privé de $A$**, de centre $\left(\frac{7}{2} ; \frac{7}{2}\right)$ et de rayon $\dfrac{AB}{2} = \dfrac{\sqrt{2}}{2}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2015-sn-math-ex2": {
        "enonce": r"""**1)** Pour tout nombre complexe $z$, on pose $P(z) = z^3 - 10z^2 + 33z - 34$.

a) Calculer $P(2)$.

b) Déterminer les réels $a$ et $b$ tels que, pour tout $z$, $P(z) = (z - 2)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$. On note $z_0$, $z_1$ et $z_2$ les solutions telles que $\operatorname{Im}(z_2) < \operatorname{Im}(z_0) < \operatorname{Im}(z_1)$.

**2)** Le plan complexe est rapporté à un repère orthonormé direct $(O;\vec{u},\vec{v})$. Soient les points $A$, $B$ et $C$ d'affixes respectives $z_A = z_1 + 3i$, $z_B = z_2 + i$ et $z_C = 6 + 2i$.

a) Vérifier que $z_A = 4 + 4i$ et $z_B = 4$.

b) Écrire les nombres $z_A$ et $z_B$ sous forme trigonométrique.

c) Placer les points $A$, $B$ et $C$ dans le repère.

**3)** Pour tout nombre $z \neq 4 + 4i$, on pose $f(z) = \dfrac{z - 4}{z - 4 - 4i}$.

a) Vérifier que $f(z_C) = i$ et interpréter graphiquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $f(z)$ soit imaginaire pur.

**4)** Pour tout entier naturel $n$, on pose $z_n = (z_A)^n$ et on note $M_n$ le point d'affixe $z_n$.

a) Déterminer l'ensemble des entiers $n$ pour lesquels le point $M_n$ appartient à l'axe des abscisses.

b) Déterminer l'ensemble des entiers $n$ pour lesquels $OM_n > 2015$.
""",
        "correction": r"""**1) a)** $P(2) = 8 - 40 + 66 - 34 = 0$.

**b)** $(z - 2)(z^2 + az + b) = z^3 + (a - 2)z^2 + (b - 2a)z - 2b$. Par identification : $a - 2 = -10$ et $-2b = -34$, donc $a = -8$ et $b = 17$ (et on vérifie $b - 2a = 33$). Ainsi $P(z) = (z - 2)(z^2 - 8z + 17)$.

**c)** Pour $z^2 - 8z + 17 = 0$ : $\Delta' = 16 - 17 = -1 = i^2$, d'où $z = 4 \pm i$. Les solutions sont $2$, $4 + i$ et $4 - i$. Avec l'ordre imposé : $z_2 = 4 - i$, $z_0 = 2$, $z_1 = 4 + i$.

**2) a)** $z_A = 4 + i + 3i = 4 + 4i$ et $z_B = 4 - i + i = 4$.

**b)** $|z_A| = 4\sqrt{2}$, donc $z_A = 4\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$ ; $z_B = 4(\cos 0 + i\sin 0)$.

**c)** $A(4 ; 4)$, $B(4 ; 0)$, $C(6 ; 2)$.

**3) a)** $f(z_C) = \dfrac{2 + 2i}{2 - 2i} = \dfrac{(1 + i)^2}{(1 - i)(1 + i)} = \dfrac{2i}{2} = i$.

Comme $f(z) = \dfrac{z - z_B}{z - z_A}$, on a $\dfrac{CB}{CA} = |i| = 1$ et $(\overrightarrow{CA}, \overrightarrow{CB}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $ABC$ est **rectangle isocèle en $C$**.

**b)** $|f(z)| = 1 \iff MB = MA$ : $\Gamma_1$ est la **médiatrice de $[AB]$**, c'est-à-dire la droite d'équation $y = 2$.

**c)** $f(z)$ imaginaire pur $\iff M = B$ ou $(\overrightarrow{MA}, \overrightarrow{MB}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AB]$ privé de $A$**, de centre $(4 ; 2)$ et de rayon $2$.

**4)** $z_n = (4\sqrt{2})^n\left(\cos\dfrac{n\pi}{4} + i\sin\dfrac{n\pi}{4}\right)$.

**a)** $M_n$ est sur l'axe des abscisses $\iff \sin\dfrac{n\pi}{4} = 0 \iff \dfrac{n\pi}{4} = k\pi \iff n = 4k$, $k \in \mathbb{N}$ : les multiples de 4.

**b)** $OM_n = |z_n| = (4\sqrt{2})^n$, suite croissante. $(4\sqrt{2})^4 = 1024 < 2015$ et $(4\sqrt{2})^5 = 4096\sqrt{2} \approx 5793 > 2015$. Donc $OM_n > 2015 \iff n \geq 5$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2016-sc-math-ex2": {
        "enonce": r"""**1)** On pose $P(z) = z^3 - 7z^2 + 18z - 12$ où $z$ est un nombre complexe.

a) Calculer $P(1)$.

b) Déterminer deux réels $a$ et $b$ tels que $P(z) = (z - 1)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormal direct $(O;\vec{u},\vec{v})$. Soient les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1$, $z_B = 3 - i\sqrt{3}$ et $z_C = 3 + i\sqrt{3}$.

a) Calculer le module et un argument de chacun des nombres $z_A$, $z_B$ et $z_C$.

b) Placer les points $A$, $B$ et $C$ dans le repère.

**3)** a) Calculer le module du complexe $\dfrac{z_C - z_A}{z_B - z_A}$.

b) En déduire la nature du triangle $ABC$.

**4)** a) Déterminer $z_D$, affixe du point $D$ tel que $ABCD$ soit un parallélogramme. Placer $D$.

b) Déterminer et construire l'ensemble $\Gamma$ des points $M$ d'affixe $z$ tels que $\left|\dfrac{z - 1 - 2i\sqrt{3}}{z - 1}\right| = 1$.

c) Déterminer $z_I$, affixe du point $I$ milieu de $[AD]$. Déterminer la nature du triangle $IBC$.
""",
        "correction": r"""**1) a)** $P(1) = 1 - 7 + 18 - 12 = 0$.

**b)** $(z - 1)(z^2 + az + b) = z^3 + (a - 1)z^2 + (b - a)z - b$, donc $a - 1 = -7$ et $-b = -12$ : $a = -6$, $b = 12$ (on vérifie $b - a = 18$).

**c)** $z^2 - 6z + 12 = 0$ : $\Delta' = 9 - 12 = -3 = (i\sqrt{3})^2$, d'où $z = 3 \pm i\sqrt{3}$. Solutions : $1$, $3 - i\sqrt{3}$ et $3 + i\sqrt{3}$.

**2) a)** $|z_A| = 1$ et $\arg z_A \equiv 0$.

$|z_B| = \sqrt{9 + 3} = 2\sqrt{3}$, $\cos\theta = \dfrac{3}{2\sqrt{3}} = \dfrac{\sqrt{3}}{2}$, $\sin\theta = -\dfrac{1}{2}$ : $\arg z_B \equiv -\dfrac{\pi}{6} \ [2\pi]$.

$z_C = \overline{z_B}$ : $|z_C| = 2\sqrt{3}$ et $\arg z_C \equiv \dfrac{\pi}{6} \ [2\pi]$.

**b)** $A(1 ; 0)$, $B(3 ; -\sqrt{3})$, $C(3 ; \sqrt{3})$.

**3) a)** $\left|\dfrac{z_C - z_A}{z_B - z_A}\right| = \dfrac{|2 + i\sqrt{3}|}{|2 - i\sqrt{3}|} = \dfrac{\sqrt{7}}{\sqrt{7}} = 1$.

**b)** Donc $AC = AB$ : le triangle $ABC$ est **isocèle en $A$** (il n'est pas équilatéral car $BC = 2\sqrt{3} \neq \sqrt{7}$).

**4) a)** $ABCD$ parallélogramme $\iff \overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = 1 + 2i\sqrt{3}$.

**b)** $\left|\dfrac{z - z_D}{z - z_A}\right| = 1 \iff MD = MA$ : $\Gamma$ est la **médiatrice de $[AD]$**. Comme $A(1 ; 0)$ et $D(1 ; 2\sqrt{3})$, c'est la droite d'équation $y = \sqrt{3}$.

**c)** $z_I = \dfrac{z_A + z_D}{2} = 1 + i\sqrt{3}$.

$\dfrac{z_B - z_C}{z_I - z_C} = \dfrac{-2i\sqrt{3}}{-2} = i\sqrt{3}$ est imaginaire pur, donc $(\overrightarrow{CI}, \overrightarrow{CB}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $IBC$ est **rectangle en $C$** (avec $CB = \sqrt{3}\,CI$).
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2016-sn-math-ex2": {
        "enonce": r"""**1)** Pour tout nombre complexe $z$, on pose $P(z) = z^3 - 7z^2 + 19z - 13$.

a) Calculer $P(1)$.

b) Déterminer les réels $a$ et $b$ tels que, pour tout $z$, $P(z) = (z - 1)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$. On note $z_0$, $z_1$ et $z_2$ les solutions telles que $\operatorname{Im}(z_1) < \operatorname{Im}(z_0) < \operatorname{Im}(z_2)$.

**2)** Le plan complexe est rapporté à un repère orthonormé direct $(O;\vec{u},\vec{v})$. Soient les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1$, $z_B = z_1 - i$ et $z_C = z_2 + 1$.

a) Vérifier que $z_B = 3 - 3i$ et que $z_C = 4 + 2i$, puis placer les points $A$, $B$ et $C$.

b) Déterminer la nature du triangle $ABC$.

c) Déterminer l'affixe $z_D$ du point $D$ tel que $ABDC$ soit un parallélogramme.

**3)** Pour tout nombre $z \neq 3 - 3i$, on pose $f(z) = \dfrac{z - 4 - 2i}{z - 3 + 3i}$.

a) Vérifier que $f(z_D) = -i$ et interpréter graphiquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $f(z)$ soit imaginaire pur.

d) Déterminer et construire l'ensemble $\Gamma_3$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{2}$.

e) Vérifier que les trois ensembles $\Gamma_1$, $\Gamma_2$ et $\Gamma_3$ passent par les points $A$ et $D$.
""",
        "correction": r"""**1) a)** $P(1) = 1 - 7 + 19 - 13 = 0$.

**b)** Par identification de $z^3 + (a - 1)z^2 + (b - a)z - b$ avec $P$ : $a = -6$ et $b = 13$ (on vérifie $b - a = 19$).

**c)** $z^2 - 6z + 13 = 0$ : $\Delta' = 9 - 13 = -4 = (2i)^2$, d'où $z = 3 \pm 2i$. Avec l'ordre imposé : $z_1 = 3 - 2i$, $z_0 = 1$, $z_2 = 3 + 2i$.

**2) a)** $z_B = 3 - 2i - i = 3 - 3i$ et $z_C = 3 + 2i + 1 = 4 + 2i$.

**b)** $\dfrac{z_C - z_A}{z_B - z_A} = \dfrac{3 + 2i}{2 - 3i} = \dfrac{i(2 - 3i)}{2 - 3i} = i$. Donc $AC = AB$ et $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : $ABC$ est **rectangle isocèle en $A$**.

**c)** $ABDC$ parallélogramme $\iff \overrightarrow{AB} = \overrightarrow{CD} \iff z_D = z_B + z_C - z_A = 6 - i$.

**3) a)** $f(z_D) = \dfrac{2 - 3i}{3 + 2i} = \dfrac{(2 - 3i)(3 - 2i)}{13} = \dfrac{-13i}{13} = -i$.

Comme $f(z) = \dfrac{z - z_C}{z - z_B}$ : $DC = DB$ et $(\overrightarrow{DB}, \overrightarrow{DC}) \equiv -\dfrac{\pi}{2} \ [2\pi]$. Le triangle $BDC$ est rectangle isocèle en $D$ ; avec 2) b), $ABDC$ est un **carré**.

**b)** $|f(z)| = 1 \iff MC = MB$ : $\Gamma_1$ est la **médiatrice de $[BC]$**.

**c)** $f(z)$ imaginaire pur $\iff M = C$ ou $(\overrightarrow{MB}, \overrightarrow{MC}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[BC]$ privé de $B$**.

**d)** $f(z) - 1 = \dfrac{(z - z_C) - (z - z_B)}{z - z_B} = \dfrac{z_B - z_C}{z - z_B} = \dfrac{-1 - 5i}{z - z_B}$, donc $|f(z) - 1| = \dfrac{\sqrt{26}}{MB}$.

$|f(z) - 1| = \sqrt{2} \iff MB = \sqrt{13}$ : $\Gamma_3$ est le **cercle de centre $B$ et de rayon $\sqrt{13}$**.

**e)** $AB = AC = DB = DC = \sqrt{13}$ ($ABDC$ est un carré de côté $\sqrt{13}$) :
- $A$ et $D$ sont équidistants de $B$ et $C$, donc sur $\Gamma_1$ ;
- les angles en $A$ et en $D$ sont droits, donc $A, D \in \Gamma_2$ ;
- $AB = DB = \sqrt{13}$, donc $A, D \in \Gamma_3$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2017-sc-math-ex2": {
        "enonce": r"""**1)** Pour tout nombre complexe $z$, on pose $P(z) = z^3 - 4\sqrt{2}\,z^2 + 12z - 8\sqrt{2}$.

a) Calculer $P(2\sqrt{2})$.

b) Déterminer les réels $a$ et $b$ tels que, pour tout $z$, $P(z) = (z - 2\sqrt{2})(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormé direct $(O;\vec{u},\vec{v})$. Soient les points $A$, $B$ et $C$ d'affixes respectives $z_A = \sqrt{2} - i\sqrt{2}$, $z_B = 2\sqrt{2}$ et $z_C = \sqrt{2} + i\sqrt{2}$.

a) Placer les points $A$, $B$ et $C$ dans le repère.

b) Déterminer la nature du triangle $ABC$ et celle du quadrilatère $OABC$.

**3)** Pour tout nombre $z \neq \sqrt{2} - i\sqrt{2}$, on pose $f(z) = \dfrac{z - \sqrt{2} - i\sqrt{2}}{z - \sqrt{2} + i\sqrt{2}}$.

a) Vérifier que $f(z_B) = -i$ et interpréter graphiquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $f(z)$ soit imaginaire pur.

d) Déterminer et construire l'ensemble $\Gamma_3$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{2}$.

e) Vérifier que les trois ensembles $\Gamma_1$, $\Gamma_2$ et $\Gamma_3$ passent par les points $O$ et $B$.
""",
        "note": "Sur le scan, le 3) d) semble porter « = 2 » ; seul √2 est compatible avec la question e) (O et B sur Γ3). À confirmer avec le sujet papier.",
        "correction": r"""**1) a)** $P(2\sqrt{2}) = 16\sqrt{2} - 4\sqrt{2} \times 8 + 24\sqrt{2} - 8\sqrt{2} = (16 - 32 + 24 - 8)\sqrt{2} = 0$.

**b)** $(z - 2\sqrt{2})(z^2 + az + b) = z^3 + (a - 2\sqrt{2})z^2 + (b - 2\sqrt{2}\,a)z - 2\sqrt{2}\,b$. Par identification : $a = -2\sqrt{2}$ et $b = 4$ (on vérifie $b - 2\sqrt{2}\,a = 4 + 8 = 12$).

**c)** $z^2 - 2\sqrt{2}\,z + 4 = 0$ : $\Delta' = 2 - 4 = -2 = (i\sqrt{2})^2$, d'où $z = \sqrt{2} \pm i\sqrt{2}$. Solutions : $2\sqrt{2}$, $\sqrt{2} + i\sqrt{2}$ et $\sqrt{2} - i\sqrt{2}$.

**2) b)** $\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{-\sqrt{2} + i\sqrt{2}}{-\sqrt{2} - i\sqrt{2}} = \dfrac{-1 + i}{-1 - i} = -i$. Donc $BC = BA$ et $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv -\dfrac{\pi}{2} \ [2\pi]$ : $ABC$ est **rectangle isocèle en $B$**.

$z_A + z_C = 2\sqrt{2} = z_O + z_B$ : les diagonales $[AC]$ et $[OB]$ ont le même milieu, donc $OABC$ est un parallélogramme. Il a un angle droit en $B$ et deux côtés consécutifs égaux ($BA = BC = 2$) : $OABC$ est un **carré**.

**3) a)** $f(z_B) = \dfrac{\sqrt{2} - i\sqrt{2}}{\sqrt{2} + i\sqrt{2}} = \dfrac{1 - i}{1 + i} = \dfrac{(1 - i)^2}{2} = -i$.

Comme $f(z) = \dfrac{z - z_C}{z - z_A}$ : $BC = BA$ et $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv -\dfrac{\pi}{2}$ ; on retrouve que $ABC$ est rectangle isocèle en $B$.

**b)** $|f(z)| = 1 \iff MC = MA$ : $\Gamma_1$ est la **médiatrice de $[AC]$**, c'est-à-dire l'axe des abscisses ($A$ et $C$ sont symétriques par rapport à cet axe).

**c)** $f(z)$ imaginaire pur $\iff M = C$ ou $(\overrightarrow{MA}, \overrightarrow{MC}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AC]$ privé de $A$**, de centre le point d'affixe $\sqrt{2}$ et de rayon $\sqrt{2}$.

**d)** $f(z) - 1 = \dfrac{z_A - z_C}{z - z_A} = \dfrac{-2i\sqrt{2}}{z - z_A}$, donc $|f(z) - 1| = \dfrac{2\sqrt{2}}{MA}$. Ainsi $|f(z) - 1| = \sqrt{2} \iff MA = 2$ : $\Gamma_3$ est le **cercle de centre $A$ et de rayon $2$**.

**e)** $O$ et $B$ sont sur l'axe des abscisses : ils sont sur $\Gamma_1$. Ils sont à la distance $\sqrt{2}$ du point d'affixe $\sqrt{2}$, donc sur $\Gamma_2$. Enfin $OA = |z_A| = 2$ et $BA = 2$, donc $O, B \in \Gamma_3$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2017-sn-math-ex2": {
        "enonce": r"""**1)** Pour tout complexe $z$, on pose $P(z) = z^3 - 10z^2 + 36z - 40$.

a) Calculer $P(2)$.

b) Déterminer les réels $a$ et $b$ tels que, pour tout $z$, $P(z) = (z - 2)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Dans le plan complexe muni d'un repère orthonormé direct $(O;\vec{u},\vec{v})$, on considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 4 - 2i$, $z_B = 2$ et $z_C = 4 + 2i$.

a) Placer les points $A$, $B$ et $C$ dans le repère.

b) Déterminer la nature du triangle $ABC$.

c) Déterminer l'affixe $z_D$ du point $D$ tel que $ABCD$ soit un parallélogramme.

**3)** Pour tout nombre $z \neq 4 + 2i$, on pose $f(z) = \dfrac{z - 4 + 2i}{z - 4 - 2i}$.

a) Vérifier que $f(z_D) = i$ et interpréter graphiquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{2}$.

**4)** On pose $z_0 = f(2i)$. Pour tout entier naturel $n$, on note $z_n = z_0^{\,n}$.

a) Écrire $z_0$ sous forme algébrique, puis vérifier que $z_0 = \sqrt{2}\,e^{-i\frac{\pi}{4}}$.

b) Déterminer la plus petite valeur de l'entier $n$ telle que $|z_n| \geq 2017$.
""",
        "note": "Sur le sujet original, la question 4) c) est barrée : elle n'est pas reprise.",
        "correction": r"""**1) a)** $P(2) = 8 - 40 + 72 - 40 = 0$.

**b)** Par identification de $z^3 + (a - 2)z^2 + (b - 2a)z - 2b$ avec $P$ : $a = -8$ et $b = 20$ (on vérifie $b - 2a = 36$).

**c)** $z^2 - 8z + 20 = 0$ : $\Delta' = 16 - 20 = -4 = (2i)^2$, d'où $z = 4 \pm 2i$. Solutions : $2$, $4 - 2i$ et $4 + 2i$.

**2) b)** $\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{2 + 2i}{2 - 2i} = \dfrac{(1 + i)^2}{2} = i$ : $BC = BA$ et $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv \dfrac{\pi}{2} \ [2\pi]$. $ABC$ est **rectangle isocèle en $B$**.

**c)** $\overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = 6$. ($ABCD$ est même un carré.)

**3) a)** $f(6) = \dfrac{2 + 2i}{2 - 2i} = i$.

Comme $f(z) = \dfrac{z - z_A}{z - z_C}$ : $DA = DC$ et $(\overrightarrow{DC}, \overrightarrow{DA}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : le triangle $ADC$ est rectangle isocèle en $D$.

**b)** $|f(z)| = 1 \iff MA = MC$ : $\Gamma_1$ est la **médiatrice de $[AC]$**, c'est-à-dire l'axe des abscisses ($A$ et $C$ sont symétriques par rapport à cet axe).

**c)** $f(z) - 1 = \dfrac{z_C - z_A}{z - z_C} = \dfrac{4i}{z - z_C}$, donc $|f(z) - 1| = \dfrac{4}{MC}$. Ainsi $|f(z) - 1| = \sqrt{2} \iff MC = 2\sqrt{2}$ : $\Gamma_2$ est le **cercle de centre $C$ et de rayon $2\sqrt{2}$** (il passe par $B$ et $D$).

**4) a)** $z_0 = f(2i) = \dfrac{-4 + 4i}{-4} = 1 - i$. $|z_0| = \sqrt{2}$ et $\arg z_0 \equiv -\dfrac{\pi}{4}$, donc $z_0 = \sqrt{2}\,e^{-i\frac{\pi}{4}}$.

**b)** $|z_n| = (\sqrt{2})^n$, suite croissante. $(\sqrt{2})^{21} = 2^{10}\sqrt{2} \approx 1448 < 2017$ et $(\sqrt{2})^{22} = 2^{11} = 2048 \geq 2017$. La plus petite valeur est $n = 22$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2018-sc-math-ex2": {
        "enonce": r"""**1)** a) Calculer $(4 - 2i)^2$.

b) Résoudre, dans $\mathbb{C}$, l'équation $z^2 + (2 - 4i)z - 6 = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormé direct $(O;\vec{u},\vec{v})$. On considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1 + i$, $z_B = -3 + 3i$ et $z_C = \dfrac{(z_B)^3}{(z_A)^5}$.

a) Écrire sous forme trigonométrique chacun des nombres $z_A$, $z_B$, puis en déduire celle de $z_C$.

b) Placer les points $A$ et $B$ dans le repère.

c) Écrire sous forme algébrique le nombre $\dfrac{z_B}{z_A}$, puis interpréter géométriquement.

**3)** Pour tout nombre complexe $z \neq 1 + i$, on pose $f(z) = \dfrac{z + 3 - 3i}{z - 1 - i}$.

a) Résoudre, dans $\mathbb{C}$, l'équation $f(z) = i$. Interpréter géométriquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $f(z)$ soit imaginaire pur ou nul.

d) Déterminer et construire l'ensemble $\Gamma_3$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{5}$.
""",
        "correction": r"""**1) a)** $(4 - 2i)^2 = 16 - 16i + 4i^2 = 12 - 16i$.

**b)** $\Delta = (2 - 4i)^2 + 24 = 4 - 16i - 16 + 24 = 12 - 16i = (4 - 2i)^2$. Donc $z = \dfrac{-2 + 4i \pm (4 - 2i)}{2}$ : $z = 1 + i$ ou $z = -3 + 3i$.

**2) a)** $z_A = \sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$ et $z_B = 3\sqrt{2}\left(\cos\dfrac{3\pi}{4} + i\sin\dfrac{3\pi}{4}\right)$.

$|z_C| = \dfrac{(3\sqrt{2})^3}{(\sqrt{2})^5} = \dfrac{54\sqrt{2}}{4\sqrt{2}} = \dfrac{27}{2}$ et $\arg z_C \equiv 3 \times \dfrac{3\pi}{4} - 5 \times \dfrac{\pi}{4} = \pi \ [2\pi]$.

Donc $z_C = \dfrac{27}{2}(\cos\pi + i\sin\pi)$, c'est-à-dire $z_C = -\dfrac{27}{2}$.

**c)** $\dfrac{z_B}{z_A} = \dfrac{(-3 + 3i)(1 - i)}{2} = \dfrac{-3 + 3i + 3i + 3}{2} = 3i$.

Donc $\dfrac{OB}{OA} = 3$ et $(\overrightarrow{OA}, \overrightarrow{OB}) \equiv \dfrac{\pi}{2} \ [2\pi]$ : les droites $(OA)$ et $(OB)$ sont perpendiculaires et $OB = 3\,OA$.

**3) a)** $f(z) = i \iff z + 3 - 3i = i(z - 1 - i) \iff z(1 - i) = -2 + 2i \iff z = \dfrac{-2 + 2i}{1 - i} = -2$.

Comme $f(z) = \dfrac{z - z_B}{z - z_A}$, le point $E(-2)$ vérifie $EB = EA$ et $(\overrightarrow{EA}, \overrightarrow{EB}) \equiv \dfrac{\pi}{2}$ : $AEB$ est rectangle isocèle en $E$.

**b)** $|f(z)| = 1 \iff MB = MA$ : $\Gamma_1$ est la **médiatrice de $[AB]$**.

**c)** $f(z)$ imaginaire pur ou nul $\iff M = B$ ou $(\overrightarrow{MA}, \overrightarrow{MB}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AB]$ privé de $A$**.

**d)** $f(z) - 1 = \dfrac{z_A - z_B}{z - z_A} = \dfrac{4 - 2i}{z - z_A}$ et $|4 - 2i| = 2\sqrt{5}$, donc $|f(z) - 1| = \dfrac{2\sqrt{5}}{MA}$.

$|f(z) - 1| = \sqrt{5} \iff MA = 2$ : $\Gamma_3$ est le **cercle de centre $A$ et de rayon $2$**.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2018-sn-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$. Pour tout nombre complexe $z$, on pose $P(z) = z^3 - (3 + 2i)z^2 + (3 + 3i)z - 4i$.

**1)** a) Déterminer les racines carrées du nombre complexe $-8 + 6i$.

b) Calculer $P(i)$.

c) Déterminer les nombres $a$ et $b$ tels que, pour tout nombre complexe $z$, $P(z) = (z - i)(z^2 + az + b)$.

d) En déduire l'ensemble des solutions de l'équation $P(z) = 0$.

**2)** Soient $A$, $B$ et $C$ les points d'affixes respectives $z_A = i$, $z_B = 1 - i$ et $z_C = 2 + 2i$.

a) Placer les points $A$, $B$ et $C$.

b) Déterminer la nature du triangle $ABC$.

c) Déterminer l'affixe du point $D$ tel que $ABDC$ soit un parallélogramme.

d) Déterminer et construire l'ensemble $\Gamma$ des points $M$ d'affixe $z$ tels que $\left|\dfrac{z - 2 - 2i}{z - 1 + i}\right| = 1$.

**3)** Pour tout entier naturel $n$, on pose $z_n = (z_C)^n$ et $v_n = |z_n|$.

a) Vérifier que $z_C = 2\sqrt{2}\,e^{i\frac{\pi}{4}}$, puis en déduire l'écriture trigonométrique de $z_n$.

b) Montrer que $(v_n)$ est une suite géométrique dont on donnera la raison et le premier terme.

c) Calculer la limite de $(v_n)$ et exprimer en fonction de $n$ la somme $S_n = v_0 + v_1 + \cdots + v_n$.
""",
        "correction": r"""**1) a)** On cherche $\delta = x + iy$ avec $\delta^2 = -8 + 6i$ : $x^2 - y^2 = -8$, $x^2 + y^2 = |-8 + 6i| = 10$ et $2xy = 6 > 0$. Donc $x^2 = 1$, $y^2 = 9$, $x$ et $y$ de même signe : les racines carrées sont $1 + 3i$ et $-1 - 3i$.

**b)** $P(i) = -i - (3 + 2i)(-1) + (3 + 3i)i - 4i = -i + 3 + 2i + 3i - 3 - 4i = 0$.

**c)** $(z - i)(z^2 + az + b) = z^3 + (a - i)z^2 + (b - ia)z - ib$. Par identification : $a - i = -3 - 2i$ donc $a = -3 - i$, et $-ib = -4i$ donc $b = 4$. On vérifie $b - ia = 4 + 3i + i^2 = 3 + 3i$.

**d)** $z^2 - (3 + i)z + 4 = 0$ : $\Delta = (3 + i)^2 - 16 = -8 + 6i = (1 + 3i)^2$. Donc $z = \dfrac{3 + i \pm (1 + 3i)}{2}$, soit $2 + 2i$ ou $1 - i$. Solutions : $i$, $1 - i$ et $2 + 2i$.

**2) b)** $\dfrac{z_C - z_A}{z_B - z_A} = \dfrac{2 + i}{1 - 2i} = \dfrac{i(1 - 2i)}{1 - 2i} = i$ : $AC = AB$ et $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $A$**.

**c)** $\overrightarrow{AB} = \overrightarrow{CD} \iff z_D = z_B + z_C - z_A = 3$. ($ABDC$ est même un carré.)

**d)** $\left|\dfrac{z - z_C}{z - z_B}\right| = 1 \iff MC = MB$ : $\Gamma$ est la **médiatrice de $[BC]$** (elle passe par $A$ et $D$).

**3) a)** $|z_C| = 2\sqrt{2}$ et $z_C = 2\sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right) = 2\sqrt{2}\,e^{i\frac{\pi}{4}}$. Donc $z_n = (2\sqrt{2})^n\left(\cos\dfrac{n\pi}{4} + i\sin\dfrac{n\pi}{4}\right)$.

**b)** $v_n = (2\sqrt{2})^n$, donc $v_{n+1} = 2\sqrt{2}\,v_n$ : $(v_n)$ est géométrique de raison $2\sqrt{2}$ et de premier terme $v_0 = 1$.

**c)** $2\sqrt{2} > 1$, donc $\lim\limits_{n \to +\infty} v_n = +\infty$. Et $S_n = \dfrac{(2\sqrt{2})^{n+1} - 1}{2\sqrt{2} - 1}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2019-sc-math-ex2": {
        "enonce": r"""**1)** Pour tout nombre complexe $z$, on pose $P(z) = z^3 - (4 - i)z^2 + 7z - 4 + 7i$.

a) Déterminer les racines carrées du nombre complexe $-12 - 16i$.

b) Calculer $P(-i)$.

c) Déterminer les nombres $a$ et $b$ tels que, $\forall z \in \mathbb{C}$, $P(z) = (z + i)(z^2 + az + b)$.

d) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Dans le plan complexe muni d'un repère orthonormé $(O;\vec{u},\vec{v})$, on considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1 + 2i$, $z_B = -i$ et $z_C = 3 - 2i$.

a) Placer les points $A$, $B$ et $C$.

b) Soit $D$ le point tel que $ABCD$ soit un parallélogramme. Justifier que $z_D = 4 + i$.

c) Écrire sous forme algébrique $\dfrac{z_D - z_C}{z_D - z_A}$ et en déduire la nature du triangle $ACD$.

**3)** Pour tout nombre complexe $z \neq 1 + 2i$, on pose $f(z) = \dfrac{z - 3 + 2i}{z - 1 - 2i}$.

a) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

b) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{20}$.

**4)** On pose $\alpha = \dfrac{z_A + z_B}{2\sqrt{2}}$ et, pour tout entier naturel $n$, $u_n = |\alpha^n|$.

a) Écrire $\alpha$ sous forme algébrique et vérifier que $u_n = \dfrac{1}{2^n}$.

b) En déduire que $(u_n)$ est une suite géométrique et montrer que $u_0 + u_1 + \cdots + u_{2019} = 2 - \dfrac{1}{2^{2019}}$.
""",
        "note": "Le sujet original dit « les réels a et b » au 1) c), mais b = 7 + 4i n'est pas réel : l'énoncé corrigé dit « les nombres a et b ».",
        "correction": r"""**1) a)** $\delta = x + iy$ avec $\delta^2 = -12 - 16i$ : $x^2 - y^2 = -12$, $x^2 + y^2 = |-12 - 16i| = 20$ et $2xy = -16 < 0$. Donc $x^2 = 4$, $y^2 = 16$, $x$ et $y$ de signes contraires : les racines carrées sont $2 - 4i$ et $-2 + 4i$.

**b)** $P(-i) = i - (4 - i)(-1) - 7i - 4 + 7i = i + 4 - i - 7i - 4 + 7i = 0$.

**c)** $(z + i)(z^2 + az + b) = z^3 + (a + i)z^2 + (b + ia)z + ib$. Par identification : $a + i = -4 + i$ donc $a = -4$ ; $ib = -4 + 7i$ donc $b = \dfrac{-4 + 7i}{i} = 7 + 4i$. On vérifie $b + ia = 7 + 4i - 4i = 7$.

**d)** $z^2 - 4z + 7 + 4i = 0$ : $\Delta = 16 - 28 - 16i = -12 - 16i = (2 - 4i)^2$. Donc $z = \dfrac{4 \pm (2 - 4i)}{2}$, soit $3 - 2i$ ou $1 + 2i$. Solutions : $-i$, $1 + 2i$ et $3 - 2i$.

**2) b)** $ABCD$ parallélogramme $\iff \overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = 1 + 2i + 3 - 2i + i = 4 + i$.

**c)** $\dfrac{z_D - z_C}{z_D - z_A} = \dfrac{1 + 3i}{3 - i} = \dfrac{(1 + 3i)(3 + i)}{10} = \dfrac{10i}{10} = i$.

Donc $DC = DA$ et $(\overrightarrow{DA}, \overrightarrow{DC}) \equiv \dfrac{\pi}{2}$ : le triangle $ACD$ est **rectangle isocèle en $D$** (et $ABCD$ est un carré).

**3) a)** $f(z) = \dfrac{z - z_C}{z - z_A}$, donc $|f(z)| = 1 \iff MC = MA$ : $\Gamma_1$ est la **médiatrice de $[AC]$** (droite d'équation $x - 2y - 2 = 0$).

**b)** $f(z) - 1 = \dfrac{z_A - z_C}{z - z_A} = \dfrac{-2 + 4i}{z - z_A}$ et $|-2 + 4i| = \sqrt{20}$, donc $|f(z) - 1| = \dfrac{\sqrt{20}}{MA}$.

$|f(z) - 1| = \sqrt{20} \iff MA = 1$ : $\Gamma_2$ est le **cercle de centre $A$ et de rayon $1$**.

**4) a)** $\alpha = \dfrac{1 + 2i - i}{2\sqrt{2}} = \dfrac{1 + i}{2\sqrt{2}} = \dfrac{\sqrt{2}}{4} + i\dfrac{\sqrt{2}}{4}$. $|\alpha| = \dfrac{\sqrt{2}}{2\sqrt{2}} = \dfrac{1}{2}$, donc $u_n = |\alpha|^n = \dfrac{1}{2^n}$.

**b)** $u_{n+1} = \dfrac{1}{2}u_n$ : $(u_n)$ est géométrique de raison $\dfrac{1}{2}$ et de premier terme $u_0 = 1$. Donc

$u_0 + u_1 + \cdots + u_{2019} = \dfrac{1 - \left(\frac{1}{2}\right)^{2020}}{1 - \frac{1}{2}} = 2\left(1 - \dfrac{1}{2^{2020}}\right) = 2 - \dfrac{1}{2^{2019}}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2019-sn-math-ex2": {
        "enonce": r"""**1)** a) Déterminer les racines carrées du nombre complexe $-3 + 4i$.

b) En déduire les solutions, dans $\mathbb{C}$, de l'équation $z^2 + (3 - 6i)z - 6 - 10i = 0$.

**2)** Dans le plan complexe muni d'un repère orthonormé $(O;\vec{u},\vec{v})$, on considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = -2 + 2i$, $z_B = i$ et $z_C = -1 + 4i$.

a) Placer les points $A$, $B$ et $C$.

b) Déterminer la nature du triangle $ABC$.

c) Déterminer l'affixe du point $D$ tel que $ABDC$ soit un parallélogramme.

**3)** Pour tout nombre complexe $z \neq i$, on pose $f(z) = \dfrac{z + 1 - 4i}{z - i}$.

a) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

b) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $f(z)$ soit imaginaire pur.

c) Déterminer et construire l'ensemble $\Gamma_3$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{2}$.

**4)** On pose, pour tout entier $n \geq 1$, $z_n = (z_A)^n$.

a) Écrire $z_n$ sous forme trigonométrique.

b) Déterminer la longueur du segment $[OM_{2019}]$, où $M_{2019}$ est le point d'affixe $z_{2019}$.
""",
        "correction": r"""**1) a)** $\delta = x + iy$ avec $\delta^2 = -3 + 4i$ : $x^2 - y^2 = -3$, $x^2 + y^2 = 5$, $2xy = 4 > 0$. Donc $x^2 = 1$, $y^2 = 4$, même signe : les racines carrées sont $1 + 2i$ et $-1 - 2i$.

**b)** $\Delta = (3 - 6i)^2 + 4(6 + 10i) = 9 - 36i - 36 + 24 + 40i = -3 + 4i = (1 + 2i)^2$. Donc $z = \dfrac{-3 + 6i \pm (1 + 2i)}{2}$ : $z = -1 + 4i$ ou $z = -2 + 2i$.

**2) b)** $\dfrac{z_C - z_A}{z_B - z_A} = \dfrac{1 + 2i}{2 - i} = \dfrac{i(2 - i)}{2 - i} = i$ : $AC = AB$ et $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv \dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $A$**.

**c)** $\overrightarrow{AB} = \overrightarrow{CD} \iff z_D = z_B + z_C - z_A = 1 + 3i$.

**3)** $f(z) = \dfrac{z - z_C}{z - z_B}$.

**a)** $|f(z)| = 1 \iff MC = MB$ : $\Gamma_1$ est la **médiatrice de $[BC]$**.

**b)** $f(z)$ imaginaire pur $\iff M = C$ ou $(\overrightarrow{MB}, \overrightarrow{MC}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[BC]$ privé de $B$**.

**c)** $f(z) - 1 = \dfrac{z_B - z_C}{z - z_B} = \dfrac{1 - 3i}{z - z_B}$, donc $|f(z) - 1| = \dfrac{\sqrt{10}}{MB}$. Ainsi $|f(z) - 1| = \sqrt{2} \iff MB = \sqrt{5}$ : $\Gamma_3$ est le **cercle de centre $B$ et de rayon $\sqrt{5}$** (il passe par $A$).

**4) a)** $|z_A| = 2\sqrt{2}$ et $z_A = 2\sqrt{2}\left(-\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right)$, donc $\arg z_A \equiv \dfrac{3\pi}{4}$ et

$z_n = (2\sqrt{2})^n\left(\cos\dfrac{3n\pi}{4} + i\sin\dfrac{3n\pi}{4}\right)$.

**b)** $OM_{2019} = |z_{2019}| = (2\sqrt{2})^{2019}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2020-sc-math-ex2": {
        "enonce": r"""Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$.

**1)** a) Calculer $(2 + 3i)^2$.

b) Résoudre, dans $\mathbb{C}$, l'équation $z^2 - (4 - i)z + 5 - 5i = 0$.

**2)** On pose $P(z) = z^3 - (4 + 2i)z^2 + (8 + 7i)z - 15 - 15i$, où $z$ est un nombre complexe.

a) Calculer $P(3i)$ et déterminer les complexes $a$ et $b$ tels que, pour tout $z \in \mathbb{C}$, $P(z) = (z - 3i)(z^2 + az + b)$.

b) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**3)** Soient $A$, $B$ et $C$ les points d'affixes respectives $3i$, $3 + i$ et $1 - 2i$.

a) Placer les points $A$, $B$ et $C$ et déterminer la nature du triangle $ABC$.

b) Calculer l'affixe du point $D$ pour que le quadrilatère $ABCD$ soit un parallélogramme. Placer le point $D$.

c) Vérifier que le point $I$ d'affixe $z_I = \dfrac{1}{2} + \dfrac{1}{2}i$ est le centre du parallélogramme $ABCD$.

**4)** Soit $\alpha = 2z_I = 1 + i$. Pour tout entier naturel $n$, on pose $z_n = \alpha^n$ et $V_n = |z_n|$.

a) Écrire $\alpha$ sous forme exponentielle.

b) Montrer que $(V_n)$ est une suite géométrique. Préciser sa raison et son premier terme.

c) Déterminer le plus petit entier naturel $p$ vérifiant $V_p \geq 2020$ et vérifier que $z_p$ est imaginaire pur.
""",
        "correction": r"""**1) a)** $(2 + 3i)^2 = 4 + 12i - 9 = -5 + 12i$.

**b)** $\Delta = (4 - i)^2 - 4(5 - 5i) = 16 - 8i - 1 - 20 + 20i = -5 + 12i = (2 + 3i)^2$. Donc $z = \dfrac{4 - i \pm (2 + 3i)}{2}$ : $z = 3 + i$ ou $z = 1 - 2i$.

**2) a)** $P(3i) = -27i - (4 + 2i)(-9) + (8 + 7i)(3i) - 15 - 15i = -27i + 36 + 18i + 24i - 21 - 15 - 15i = 0$.

$(z - 3i)(z^2 + az + b) = z^3 + (a - 3i)z^2 + (b - 3ia)z - 3ib$. Par identification : $a = -4 + i$ et $-3ib = -15 - 15i$, donc $b = 5 - 5i$. On vérifie $b - 3ia = 5 - 5i + 12i + 3 = 8 + 7i$.

**b)** $z^2 + az + b = z^2 - (4 - i)z + 5 - 5i$ : c'est l'équation du 1) b). Solutions de $P(z) = 0$ : $3i$, $3 + i$ et $1 - 2i$.

**3) a)** $\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{-2 - 3i}{-3 + 2i} = \dfrac{(-2 - 3i)(-3 - 2i)}{13} = \dfrac{13i}{13} = i$ : $BC = BA$ et $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv \dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $B$**.

**b)** $\overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = 3i + 1 - 2i - 3 - i = -2$.

**c)** Le milieu de $[AC]$ a pour affixe $\dfrac{3i + 1 - 2i}{2} = \dfrac{1}{2} + \dfrac{1}{2}i = z_I$ (et c'est aussi le milieu de $[BD]$ : $\frac{3 + i - 2}{2}$). $I$ est donc le centre du parallélogramme $ABCD$ (qui est même un carré).

**4) a)** $|\alpha| = \sqrt{2}$ et $\alpha = \sqrt{2}\left(\dfrac{\sqrt{2}}{2} + i\dfrac{\sqrt{2}}{2}\right) = \sqrt{2}\,e^{i\frac{\pi}{4}}$.

**b)** $V_n = |\alpha|^n = (\sqrt{2})^n$, donc $V_{n+1} = \sqrt{2}\,V_n$ : suite géométrique de raison $\sqrt{2}$ et de premier terme $V_0 = 1$.

**c)** $(V_n)$ est croissante, $V_{21} = 2^{10}\sqrt{2} \approx 1448 < 2020$ et $V_{22} = 2^{11} = 2048 \geq 2020$ : $p = 22$.

$z_{22} = 2^{11}e^{i\frac{22\pi}{4}} = 2^{11}e^{i\frac{11\pi}{2}} = 2^{11}e^{-i\frac{\pi}{2}} = -2048i$ : $z_{22}$ est imaginaire pur.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2020-sn-math-ex2": {
        "enonce": r"""**1)** Pour tout complexe $z$, on pose $P(z) = z^3 - (7 + 7i)z^2 + (-2 + 30i)z + 32 - 16i$.

a) Calculer $P(2i)$.

b) Déterminer les nombres complexes $a$ et $b$ tels que, pour tout $z$, $P(z) = (z - 2i)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Dans le plan complexe muni d'un repère orthonormé direct $(O;\vec{u},\vec{v})$, on considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 3 + i$, $z_B = 2i$ et $z_C = 4 + 4i$.

a) Placer les points $A$, $B$ et $C$ dans le repère.

b) Déterminer la nature du triangle $ABC$.

c) Déterminer l'affixe $z_D$ du point $D$ tel que $ABDC$ soit un parallélogramme. Placer $D$.

**3)** Pour tout nombre complexe $z \neq 4 + 4i$, on pose $f(z) = \dfrac{z - 2i}{z - 4 - 4i}$.

a) Vérifier que $f(z_D) = -i$ et interpréter graphiquement.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $|f(z) - 1| = \sqrt{2}$.

**4)** On pose $z_0 = f(6)$ et, pour tout entier naturel $n$, on note $z_n = z_0^{\,n}$.

a) Écrire $z_0$ sous forme algébrique, puis vérifier que $z_0 = \sqrt{2}\,e^{i\frac{\pi}{4}}$.

b) Déterminer la plus petite valeur de l'entier naturel $n$ telle que $|z_n| \geq 2020$.

c) Vérifier que le point d'affixe $z_{2020}$ appartient à l'axe des abscisses.
""",
        "note": "Le sujet original écrit « z ≠ 3 + i » au 3) ; la valeur interdite de f est 4 + 4i (corrigé dans l'énoncé).",
        "correction": r"""**1) a)** $P(2i) = -8i + 4(7 + 7i) + (-2 + 30i)(2i) + 32 - 16i = -8i + 28 + 28i - 4i - 60 + 32 - 16i = 0$.

**b)** $(z - 2i)(z^2 + az + b) = z^3 + (a - 2i)z^2 + (b - 2ia)z - 2ib$. Par identification : $a = -7 - 5i$ et $-2ib = 32 - 16i$, donc $b = 8 + 16i$. On vérifie $b - 2ia = 8 + 16i + 14i - 10 = -2 + 30i$.

**c)** $z^2 - (7 + 5i)z + 8 + 16i = 0$ : $\Delta = (7 + 5i)^2 - 4(8 + 16i) = 24 + 70i - 32 - 64i = -8 + 6i = (1 + 3i)^2$. Donc $z = \dfrac{7 + 5i \pm (1 + 3i)}{2}$, soit $4 + 4i$ ou $3 + i$. Solutions : $2i$, $3 + i$ et $4 + 4i$.

**2) b)** $\dfrac{z_C - z_A}{z_B - z_A} = \dfrac{1 + 3i}{-3 + i} = \dfrac{(1 + 3i)(-3 - i)}{10} = \dfrac{-10i}{10} = -i$ : $AC = AB$ et $(\overrightarrow{AB}, \overrightarrow{AC}) \equiv -\dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $A$**.

**c)** $\overrightarrow{AB} = \overrightarrow{CD} \iff z_D = z_B + z_C - z_A = 1 + 5i$.

**3) a)** $f(1 + 5i) = \dfrac{1 + 3i}{-3 + i} = -i$ (même calcul qu'au 2) b)).

Comme $f(z) = \dfrac{z - z_B}{z - z_C}$ : $DB = DC$ et $(\overrightarrow{DC}, \overrightarrow{DB}) \equiv -\dfrac{\pi}{2}$. Le triangle $BDC$ est rectangle isocèle en $D$ : $ABDC$ est un **carré**.

**b)** $|f(z)| = 1 \iff MB = MC$ : $\Gamma_1$ est la **médiatrice de $[BC]$** (elle passe par $A$ et $D$).

**c)** $f(z) - 1 = \dfrac{z_C - z_B}{z - z_C} = \dfrac{4 + 2i}{z - z_C}$ et $|4 + 2i| = 2\sqrt{5}$, donc $|f(z) - 1| = \dfrac{2\sqrt{5}}{MC}$. Ainsi $|f(z) - 1| = \sqrt{2} \iff MC = \sqrt{10}$ : $\Gamma_2$ est le **cercle de centre $C$ et de rayon $\sqrt{10}$** (il passe par $A$ et $D$).

**4) a)** $z_0 = f(6) = \dfrac{6 - 2i}{2 - 4i} = \dfrac{(6 - 2i)(2 + 4i)}{20} = \dfrac{20 + 20i}{20} = 1 + i = \sqrt{2}\,e^{i\frac{\pi}{4}}$.

**b)** $|z_n| = (\sqrt{2})^n$ est croissante ; $(\sqrt{2})^{21} \approx 1448 < 2020$ et $(\sqrt{2})^{22} = 2048 \geq 2020$ : $n = 22$.

**c)** $z_{2020} = (\sqrt{2})^{2020}e^{i\frac{2020\pi}{4}} = 2^{1010}e^{505i\pi} = -2^{1010}$ : c'est un réel, le point est sur l'axe des abscisses.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2021-sc-math-ex2": {
        "enonce": r"""Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$. On considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = 3i$, $z_B = 2 + 2i$ et $z_C = -3 - 3i$.

**1)** a) Calculer $(2 - i)^2$.

b) Résoudre, dans $\mathbb{C}$, l'équation $z^2 - (2 + 5i)z - 6 + 6i = 0$.

**2)** a) Écrire sous forme trigonométrique chacun des nombres $z_B$ et $z_C$.

b) Déterminer l'ensemble des points $M$ du plan d'affixe $z$ tels que $|z - 3i| = |z - 2 - 2i|$.

**3)** On pose $z_0 = z_C$ et, $\forall n \in \mathbb{N}$, $z_{n+1} = \dfrac{1}{3}i\,z_n + 1 + 3i$ et $d_n = |z_n - z_A|$.

a) Montrer que $z_1 = z_B$.

b) Pour tout entier naturel $n$, on note $M_n$ le point d'affixe $z_n$. Montrer que $\forall n \in \mathbb{N}$, $\dfrac{z_{n+1} - z_A}{z_n - z_A} = \dfrac{1}{3}i$, puis en déduire la nature du triangle $AM_nM_{n+1}$.

c) En déduire que $(d_n)$ est une suite géométrique dont on donnera la raison.

d) Exprimer en fonction de $n$ la somme $S_n = d_0 + d_1 + d_2 + \cdots + d_n$.
""",
        "correction": r"""**1) a)** $(2 - i)^2 = 4 - 4i - 1 = 3 - 4i$.

**b)** $\Delta = (2 + 5i)^2 - 4(-6 + 6i) = 4 + 20i - 25 + 24 - 24i = 3 - 4i = (2 - i)^2$. Donc $z = \dfrac{2 + 5i \pm (2 - i)}{2}$ : $z = 2 + 2i$ ou $z = 3i$.

**2) a)** $z_B = 2\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$ et $z_C = 3\sqrt{2}\left(\cos\left(-\dfrac{3\pi}{4}\right) + i\sin\left(-\dfrac{3\pi}{4}\right)\right)$.

**b)** $|z - z_A| = |z - z_B| \iff MA = MB$ : c'est la **médiatrice de $[AB]$**.

**3) a)** $z_1 = \dfrac{1}{3}i(-3 - 3i) + 1 + 3i = -i + 1 + 1 + 3i = 2 + 2i = z_B$.

**b)** On remarque que $\dfrac{1}{3}i \times 3i + 1 + 3i = -1 + 1 + 3i = 3i = z_A$. En soustrayant les deux égalités :

$z_{n+1} - z_A = \dfrac{1}{3}i(z_n - z_A)$, donc $\dfrac{z_{n+1} - z_A}{z_n - z_A} = \dfrac{1}{3}i$ (car $z_n \neq z_A$).

Cet imaginaire pur a pour argument $\dfrac{\pi}{2}$ : $(\overrightarrow{AM_n}, \overrightarrow{AM_{n+1}}) \equiv \dfrac{\pi}{2}$. Le triangle $AM_nM_{n+1}$ est **rectangle en $A$**, avec $AM_{n+1} = \dfrac{1}{3}AM_n$.

**c)** En prenant les modules : $d_{n+1} = \dfrac{1}{3}d_n$. $(d_n)$ est géométrique de raison $\dfrac{1}{3}$ et de premier terme $d_0 = |z_C - z_A| = |-3 - 6i| = 3\sqrt{5}$.

**d)** $S_n = 3\sqrt{5} \times \dfrac{1 - \left(\frac{1}{3}\right)^{n+1}}{1 - \frac{1}{3}} = \dfrac{9\sqrt{5}}{2}\left(1 - \dfrac{1}{3^{n+1}}\right)$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2021-sn-math-ex2": {
        "enonce": r"""Pour tout nombre complexe $z$, on pose $P(z) = z^3 - (1 + 4i)z^2 - 3z - 1 - 8i$.

**1)** a) Calculer $P(-i)$.

b) Déterminer les complexes $a$ et $b$ tels que $\forall z \in \mathbb{C}$, $P(z) = (z + i)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Dans le plan complexe muni d'un repère orthonormé $(O;\vec{u},\vec{v})$, on considère les points $A$, $B$ et $C$ d'affixes respectives $z_A = -i$, $z_B = -1 + 2i$ et $z_C = 2 + 3i$.

a) Placer les points $A$, $B$ et $C$ dans le repère. Déterminer la nature du triangle $ABC$.

b) Placer le point $D$ d'affixe $z_D = 3$ et préciser la nature du quadrilatère $ABCD$.

**3)** Pour tout nombre complexe $z \neq 2 + 3i$, on pose $f(z) = \dfrac{z + i}{z - 2 - 3i}$.

a) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

b) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $\arg[f(z)] \equiv \dfrac{\pi}{2} \ [\pi]$.

c) Justifier que les ensembles $\Gamma_1$ et $\Gamma_2$ passent par les points $B$ et $D$.

**4)** Pour tout $n \in \mathbb{N}$, on pose $z_n = (z_B - i)^n$. Soit $M_n$ le point d'affixe $z_n$ et $d_n = |z_n|$.

a) Déterminer les valeurs de $n$ pour lesquelles $M_n$ appartient à l'axe des abscisses.

b) Montrer que $(d_n)$ est une suite géométrique et en déduire que $OM_n = (\sqrt{2})^n$.

c) Exprimer en fonction de $n$ la somme $L_n = OM_1 + OM_2 + \cdots + OM_n$, où $n \in \mathbb{N}^*$.
""",
        "correction": r"""**1) a)** $P(-i) = i - (1 + 4i)(-1) + 3i - 1 - 8i = i + 1 + 4i + 3i - 1 - 8i = 0$.

**b)** $(z + i)(z^2 + az + b) = z^3 + (a + i)z^2 + (b + ia)z + ib$. Par identification : $a = -1 - 5i$ et $ib = -1 - 8i$, donc $b = -8 + i$. On vérifie $b + ia = -8 + i - i + 5 = -3$.

**c)** $z^2 - (1 + 5i)z - 8 + i = 0$ : $\Delta = (1 + 5i)^2 + 4(8 - i) = -24 + 10i + 32 - 4i = 8 + 6i = (3 + i)^2$. Donc $z = \dfrac{1 + 5i \pm (3 + i)}{2}$, soit $2 + 3i$ ou $-1 + 2i$. Solutions : $-i$, $-1 + 2i$ et $2 + 3i$.

**2) a)** $\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{3 + i}{1 - 3i} = \dfrac{i(1 - 3i)}{1 - 3i} = i$ : $BC = BA$ et $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv \dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $B$**.

**b)** $z_A + z_C = 2 + 2i = z_B + z_D$ : les diagonales ont le même milieu, $ABCD$ est un parallélogramme. Avec un angle droit en $B$ et $BA = BC$, $ABCD$ est un **carré**.

**3)** $f(z) = \dfrac{z - z_A}{z - z_C}$.

**a)** $|f(z)| = 1 \iff MA = MC$ : $\Gamma_1$ est la **médiatrice de $[AC]$**.

**b)** $\arg f(z) \equiv (\overrightarrow{MC}, \overrightarrow{MA}) \equiv \dfrac{\pi}{2} \ [\pi]$ ($M \neq A$, $M \neq C$) : $\Gamma_2$ est le **cercle de diamètre $[AC]$ privé de $A$ et $C$**.

**c)** $ABCD$ est un carré : $BA = BC$ et $DA = DC$, donc $B, D \in \Gamma_1$ ; les angles en $B$ et $D$ sont droits, donc $B, D \in \Gamma_2$.

**4)** $z_B - i = -1 + i = \sqrt{2}\,e^{i\frac{3\pi}{4}}$, donc $z_n = (\sqrt{2})^n e^{i\frac{3n\pi}{4}}$.

**a)** $M_n$ est sur l'axe des abscisses $\iff \sin\dfrac{3n\pi}{4} = 0 \iff \dfrac{3n}{4} \in \mathbb{Z} \iff n$ est un multiple de 4.

**b)** $d_n = (\sqrt{2})^n$ donc $d_{n+1} = \sqrt{2}\,d_n$ : suite géométrique de raison $\sqrt{2}$, de premier terme $d_0 = 1$, et $OM_n = d_n = (\sqrt{2})^n$.

**c)** $L_n = \sqrt{2} + (\sqrt{2})^2 + \cdots + (\sqrt{2})^n = \sqrt{2} \times \dfrac{(\sqrt{2})^n - 1}{\sqrt{2} - 1}$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2022-sc-math-ex2": {
        "enonce": r"""On considère le polynôme $P$ défini pour tout nombre complexe $z$ par $P(z) = z^3 - (5 + 4i)z^2 + (1 + 16i)z + 3 - 12i$.

**1)** a) Vérifier que $(4 - 2i)^2 = 12 - 16i$.

b) Calculer $P(1)$ et déterminer les nombres complexes $a$ et $b$ tels que $\forall z \in \mathbb{C}$, $P(z) = (z - 1)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$.

a) Placer les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1$, $z_B = 3i$ et $z_C = 4 + i$.

b) Déterminer l'affixe du point $D$ tel que $ABDC$ soit un parallélogramme.

**3)** Pour tout nombre complexe $z \neq 4 + i$, on pose $f(z) = \dfrac{z - 3i}{z - 4 - i}$.

a) Calculer $f(1)$, puis en déduire la nature du triangle $ABC$.

b) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.

c) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $f(z)$ soit imaginaire pur.

d) Montrer que le point $A$ appartient aux ensembles $\Gamma_1$ et $\Gamma_2$.
""",
        "correction": r"""**1) a)** $(4 - 2i)^2 = 16 - 16i - 4 = 12 - 16i$.

**b)** $P(1) = 1 - 5 - 4i + 1 + 16i + 3 - 12i = 0$.

$(z - 1)(z^2 + az + b) = z^3 + (a - 1)z^2 + (b - a)z - b$. Par identification : $a = -4 - 4i$ et $b = -3 + 12i$. On vérifie $b - a = 1 + 16i$.

**c)** $z^2 - (4 + 4i)z - 3 + 12i = 0$ : $\Delta = (4 + 4i)^2 - 4(-3 + 12i) = 32i + 12 - 48i = 12 - 16i = (4 - 2i)^2$. Donc $z = \dfrac{4 + 4i \pm (4 - 2i)}{2}$, soit $4 + i$ ou $3i$. Solutions : $1$, $3i$ et $4 + i$.

**2) b)** $\overrightarrow{AB} = \overrightarrow{CD} \iff z_D = z_B + z_C - z_A = 3 + 4i$.

**3) a)** $f(1) = \dfrac{1 - 3i}{-3 - i} = \dfrac{(1 - 3i)(-3 + i)}{10} = \dfrac{10i}{10} = i$.

Comme $f(z) = \dfrac{z - z_B}{z - z_C}$ : $AB = AC$ et $(\overrightarrow{AC}, \overrightarrow{AB}) \equiv \dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $A$**.

**b)** $|f(z)| = 1 \iff MB = MC$ : $\Gamma_1$ est la **médiatrice de $[BC]$**.

**c)** $f(z)$ imaginaire pur $\iff M = B$ ou $(\overrightarrow{MC}, \overrightarrow{MB}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[BC]$ privé de $C$**.

**d)** $f(1) = i$ : $|f(1)| = 1$, donc $A \in \Gamma_1$ ; $i$ est imaginaire pur, donc $A \in \Gamma_2$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2022-sn-math-ex2": {
        "enonce": r"""On considère le polynôme $P$ défini pour tout nombre complexe $z$ par $P(z) = z^3 - (2 + 2i)z^2 - (2 - 8i)z + 8 + 4i$.

**1)** a) Écrire sous forme algébrique le nombre complexe $(4 - 2i)^2$.

b) Calculer $P(2i)$ et déterminer les complexes $a$ et $b$ tels que $\forall z \in \mathbb{C}$, $P(z) = (z - 2i)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$.

a) Placer les points $A$, $B$ et $C$ d'affixes respectives $z_A = -1 + i$, $z_B = 2i$ et $z_C = 3 - i$.

b) Déterminer l'affixe du point $D$ tel que $ABCD$ soit un parallélogramme.

c) Écrire sous forme exponentielle les nombres $z_A$ et $z_B$.

d) Écrire sous forme trigonométrique le nombre $\dfrac{z_C - 2i}{z_A - 2i}$, et en déduire la nature de $ABC$.

**3)** a) Déterminer et construire l'ensemble $E$ des points $M$ d'affixe $z$ tels que $|z - 3 + i| = |z + 1 - i|$.

b) Déterminer l'ensemble $F$ des points $M$ d'affixe $z$ tels que $\arg(z - 3 + i) - \arg(z + 1 - i) \equiv \dfrac{\pi}{2} \ [\pi]$.
""",
        "correction": r"""**1) a)** $(4 - 2i)^2 = 16 - 16i - 4 = 12 - 16i$.

**b)** $P(2i) = -8i + 4(2 + 2i) - (2 - 8i)(2i) + 8 + 4i = -8i + 8 + 8i - 4i - 16 + 8 + 4i = 0$.

$(z - 2i)(z^2 + az + b) = z^3 + (a - 2i)z^2 + (b - 2ia)z - 2ib$. Par identification : $a = -2$ et $-2ib = 8 + 4i$, donc $b = -2 + 4i$. On vérifie $b - 2ia = -2 + 4i + 4i = -2 + 8i$.

**c)** $z^2 - 2z - 2 + 4i = 0$ : $\Delta = 4 + 8 - 16i = 12 - 16i = (4 - 2i)^2$. Donc $z = \dfrac{2 \pm (4 - 2i)}{2}$, soit $3 - i$ ou $-1 + i$. Solutions : $2i$, $3 - i$ et $-1 + i$.

**2) b)** $\overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = -1 + i + 3 - i - 2i = 2 - 2i$.

**c)** $z_A = \sqrt{2}\,e^{i\frac{3\pi}{4}}$ et $z_B = 2e^{i\frac{\pi}{2}}$.

**d)** $\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{3 - 3i}{-1 - i} = \dfrac{(3 - 3i)(-1 + i)}{2} = \dfrac{6i}{2} = 3i = 3\left(\cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}\right)$.

Donc $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv \dfrac{\pi}{2}$ et $BC = 3BA$ : $ABC$ est **rectangle en $B$**.

**3) a)** $|z - z_C| = |z - z_A| \iff MC = MA$ : $E$ est la **médiatrice de $[AC]$**.

**b)** $\arg(z - z_C) - \arg(z - z_A) \equiv \arg\dfrac{z - z_C}{z - z_A} \equiv (\overrightarrow{MA}, \overrightarrow{MC}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $F$ est le **cercle de diamètre $[AC]$ privé de $A$ et $C$** (il passe par $B$).
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2023-sn-math-ex4": {
        "enonce": r"""**1)** On considère le polynôme $P$ défini pour tout nombre complexe $z$ par $P(z) = z^3 - (4 + i)z^2 + 7z - 4 - 7i$.

a) Écrire sous forme algébrique le nombre complexe $(2 + 4i)^2$.

b) Calculer $P(i)$ et déterminer les nombres $a$ et $b$ tels que $\forall z \in \mathbb{C}$, $P(z) = (z - i)(z^2 + az + b)$.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$.

a) Placer les points $A$, $B$ et $C$ d'affixes respectives $z_A = 1 - 2i$, $z_B = i$ et $z_C = 3 + 2i$.

b) Déterminer l'affixe du point $D$ tel que $ABCD$ soit un parallélogramme.

c) Écrire sous forme trigonométrique le nombre $\dfrac{z_C - i}{z_A - i}$. En déduire la nature de $ABC$.

**3)** a) Calculer l'affixe $z_I$ du point $I$ milieu de $[AB]$ et l'écrire sous forme exponentielle.

b) Déterminer le plus petit entier $n$ tel que $2023 \times |z_I|^n \leq 1$.

**4)** a) Déterminer et construire l'ensemble $\Gamma_1$ des points $M$ d'affixe $z$ tels que $|z - 1 + 2i| = |z - 3 - 2i|$.

b) Déterminer et construire l'ensemble $\Gamma_2$ des points $M$ d'affixe $z$ tels que $\arg\left(\dfrac{z - 3 - 2i}{z - 1 + 2i}\right) \equiv \dfrac{\pi}{2} \ [\pi]$.

c) Vérifier que le point $D$ appartient à chacun des deux ensembles $\Gamma_1$ et $\Gamma_2$.
""",
        "correction": r"""**1) a)** $(2 + 4i)^2 = 4 + 16i - 16 = -12 + 16i$.

**b)** $P(i) = -i - (4 + i)(-1) + 7i - 4 - 7i = -i + 4 + i - 4 = 0$.

$(z - i)(z^2 + az + b) = z^3 + (a - i)z^2 + (b - ia)z - ib$. Par identification : $a = -4$ et $-ib = -4 - 7i$, donc $b = 7 - 4i$. On vérifie $b - ia = 7 - 4i + 4i = 7$.

**c)** $z^2 - 4z + 7 - 4i = 0$ : $\Delta = 16 - 28 + 16i = -12 + 16i = (2 + 4i)^2$. Donc $z = \dfrac{4 \pm (2 + 4i)}{2}$, soit $3 + 2i$ ou $1 - 2i$. Solutions : $i$, $1 - 2i$ et $3 + 2i$.

**2) b)** $\overrightarrow{AB} = \overrightarrow{DC} \iff z_D = z_A + z_C - z_B = 1 - 2i + 3 + 2i - i = 4 - i$.

**c)** $\dfrac{z_C - z_B}{z_A - z_B} = \dfrac{3 + i}{1 - 3i} = \dfrac{(3 + i)(1 + 3i)}{10} = \dfrac{10i}{10} = i = \cos\dfrac{\pi}{2} + i\sin\dfrac{\pi}{2}$.

Donc $BC = BA$ et $(\overrightarrow{BA}, \overrightarrow{BC}) \equiv \dfrac{\pi}{2}$ : $ABC$ est **rectangle isocèle en $B$** (et $ABCD$ est un carré).

**3) a)** $z_I = \dfrac{z_A + z_B}{2} = \dfrac{1 - i}{2} = \dfrac{\sqrt{2}}{2}e^{-i\frac{\pi}{4}}$.

**b)** $|z_I|^n = \left(\dfrac{\sqrt{2}}{2}\right)^n = 2^{-n/2}$. On veut $2^{n/2} \geq 2023$ : $2^{10.5} \approx 1448 < 2023$ et $2^{11} = 2048 \geq 2023$. Le plus petit entier est $n = 22$.

**4) a)** $|z - z_A| = |z - z_C| \iff MA = MC$ : $\Gamma_1$ est la **médiatrice de $[AC]$**.

**b)** $\arg\dfrac{z - z_C}{z - z_A} \equiv (\overrightarrow{MA}, \overrightarrow{MC}) \equiv \dfrac{\pi}{2} \ [\pi]$ : $\Gamma_2$ est le **cercle de diamètre $[AC]$ privé de $A$ et $C$**.

**c)** $DA = |3 + i| = \sqrt{10}$ et $DC = |1 - 3i| = \sqrt{10}$, donc $D \in \Gamma_1$. Et $\dfrac{z_D - z_C}{z_D - z_A} = \dfrac{1 - 3i}{3 + i} = -i$, d'argument $-\dfrac{\pi}{2} \equiv \dfrac{\pi}{2} \ [\pi]$, donc $D \in \Gamma_2$.
""",
    },
    # ─────────────────────────────────────────────────────────────────────────
    "bac-d-2024-sn-math-ex4": {
        "enonce": r"""**1)** On considère le polynôme $P$ défini pour tout nombre complexe $z$ par $P(z) = z^3 - (5 + 4i)z^2 + (1 + 16i)z + 3 - 12i$.

a) Calculer $P(1)$ et déterminer les nombres $a$ et $b$ tels que $\forall z \in \mathbb{C}$, $P(z) = (z - 1)(z^2 + az + b)$.

b) Écrire le nombre complexe $(4 - 2i)^2$ sous forme algébrique.

c) Résoudre, dans $\mathbb{C}$, l'équation $P(z) = 0$.

**2)** Le plan complexe est rapporté à un repère orthonormé $(O;\vec{u},\vec{v})$.

a) Placer les points $A$, $B$ et $C$ d'affixes respectives $z_A = 3i$, $z_B = 1$ et $z_C = 4 + i$.

b) Soit $I$ le milieu du segment $[AC]$. Placer $I$ et donner son affixe $z_I$ sous forme algébrique et trigonométrique.

c) Déterminer le plus petit entier naturel $n$ tel que $|z_I|^n \geq 2024$.

**3)** Pour tout nombre complexe $z \neq 4 + i$, on pose $f(z) = \dfrac{z - 3i}{z - 4 - i}$.

a) Vérifier que $f(z_B) = i$ et en déduire la nature du triangle $ABC$.

b) Déterminer et construire l'ensemble $\Gamma$ des points $M$ d'affixe $z$ tels que $|f(z)| = 1$.
""",
        "correction": r"""**1) a)** $P(1) = 1 - 5 - 4i + 1 + 16i + 3 - 12i = 0$. Par identification de $z^3 + (a - 1)z^2 + (b - a)z - b$ avec $P$ : $a = -4 - 4i$ et $b = -3 + 12i$ (on vérifie $b - a = 1 + 16i$).

**b)** $(4 - 2i)^2 = 16 - 16i - 4 = 12 - 16i$.

**c)** $z^2 - (4 + 4i)z - 3 + 12i = 0$ : $\Delta = (4 + 4i)^2 + 12 - 48i = 12 - 16i = (4 - 2i)^2$. Donc $z = \dfrac{4 + 4i \pm (4 - 2i)}{2}$, soit $4 + i$ ou $3i$. Solutions : $1$, $3i$ et $4 + i$.

**2) b)** $z_I = \dfrac{z_A + z_C}{2} = \dfrac{4 + 4i}{2} = 2 + 2i = 2\sqrt{2}\left(\cos\dfrac{\pi}{4} + i\sin\dfrac{\pi}{4}\right)$.

**c)** $|z_I|^n = (2\sqrt{2})^n = 2^{3n/2}$. $(2\sqrt{2})^7 = 2^{10.5} \approx 1448 < 2024$ et $(2\sqrt{2})^8 = 2^{12} = 4096 \geq 2024$ : $n = 8$.

**3) a)** $f(1) = \dfrac{1 - 3i}{-3 - i} = \dfrac{(1 - 3i)(-3 + i)}{10} = \dfrac{10i}{10} = i$.

Comme $f(z) = \dfrac{z - z_A}{z - z_C}$ : $BA = BC$ et $(\overrightarrow{BC}, \overrightarrow{BA}) \equiv \dfrac{\pi}{2}$. $ABC$ est **rectangle isocèle en $B$**.

**b)** $|f(z)| = 1 \iff MA = MC$ : $\Gamma$ est la **médiatrice de $[AC]$** (elle passe par $B$ et $I$).
""",
    },
}
