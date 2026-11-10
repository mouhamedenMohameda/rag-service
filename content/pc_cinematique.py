"""Physique — chapitre « Cinématique et lois de Newton » (séries C et D) :
énoncés retranscrits des PDF officiels + corrections vérifiées.

- ENONCES : texte retranscrit depuis les sujets (drive_archive/annals/phisique et
  chimie), en remplacement du texte OCR ; ``scripts/load_enonces.py pc_cinematique --apply``.
- CORRECTIONS : chaque application numérique refaite par calcul (CHECKS en fin de
  fichier) et, quand le corrigé officiel existe (D 2021 sc, D 2023 sc), comparée à lui ;
  ``scripts/load_corrections.py pc_cinematique --apply``.
Les figures ne sont pas reproduites : quand une donnée n'est lisible que sur la figure,
elle est écrite dans l'énoncé (« D'après la figure : … »).
"""

CH = "Cinématique et lois de Newton"
MCU = "Mouvements dans des champs uniformes"
GRAV = "Gravitation et Satellites"
NUC = "Radioactivité et réactions nucléaires"

ENONCES: dict[str, dict] = {}
CORRECTIONS: dict[str, dict] = {}


def _add(eid: str, enonce: str, correction: str, chapitres=None, note: str = "", chapitre: str = CH) -> None:
    ENONCES[eid] = {"chapitre": chapitre, "chapitres": list(chapitres or []), "enonce": enonce.strip() + "\n",
                    "note": note, "replace_ocr": True}
    CORRECTIONS[eid] = {"enonce": enonce.strip() + "\n", "correction": correction.strip() + "\n", "note": note}


# ═══════════════════════════════ D 2015 — session complémentaire ══════════════

_add("bac-d-2015-sc-pc-ex3", r"""
**Exercice 3 (5 points)**

*Les questions 1 et 2 sont indépendantes.*

**1.** Un jouet d'enfant est constitué par un canon à ressort dirigé verticalement. Ce canon lance de petits projectiles de masse $m = 25\ \text{g}$ chacun. La longueur du ressort à vide est $l_0 = 10\ \text{cm}$. Le ressort a une raideur $K$ telle qu'une force de $1\ \text{N}$ provoque un raccourcissement de $5\ \text{mm}$. Pour lancer le projectile, on comprime le ressort de $\dfrac{l_0}{2}$ et on l'abandonne à lui-même (fig. 1). La position pour laquelle le ressort est au maximum de compression est prise comme état de référence pour l'énergie potentielle de pesanteur $E_{pp}$.

On négligera toutes les forces de frottement et on prendra $g = 10\ \text{m/s}^2$.

**1.1.** Calculer l'énergie potentielle élastique $E_{pe}$ du système (projectile + ressort) lorsque le ressort est au maximum de sa compression.

**1.2.** Déterminer la vitesse $V$ du projectile à la sortie du canon.

**1.3.** Déterminer, en utilisant la conservation de l'énergie mécanique, l'altitude maximale $h$ atteinte par le projectile.

**2.** Au ressort précédent on suspend une masse de $100\ \text{g}$ (voir fig. 2) ; on tire la masse de $4\ \text{cm}$ vers le bas puis on l'abandonne sans vitesse initiale à $t = 0$.

**2.1.** Trouver l'équation différentielle du mouvement.

**2.2.** Déterminer l'équation horaire du mouvement.

**2.3.** Calculer la période du mouvement et en déduire sa fréquence.
""", r"""
**1.1.** Raideur : $K = \dfrac{F}{\Delta l} = \dfrac{1}{5 \times 10^{-3}} = 200\ \text{N/m}$.

Compression maximale : $x = \dfrac{l_0}{2} = 5\ \text{cm} = 0{,}05\ \text{m}$.
$$E_{pe} = \dfrac{1}{2}Kx^2 = \dfrac{1}{2} \times 200 \times 0{,}05^2 = 0{,}25\ \text{J}.$$

**1.2.** Le projectile quitte le ressort (sortie du canon) quand le ressort a retrouvé sa longueur à vide : il est alors monté de $x = 0{,}05\ \text{m}$ depuis la position de référence. Sans frottement, l'énergie mécanique se conserve :
$$E_{pe} = \dfrac{1}{2}mV^2 + mgx \iff V = \sqrt{\dfrac{2(E_{pe} - mgx)}{m}} = \sqrt{\dfrac{2(0{,}25 - 0{,}025 \times 10 \times 0{,}05)}{0{,}025}} = \sqrt{19} \approx 4{,}4\ \text{m/s}.$$

**1.3.** Au point le plus haut, la vitesse est nulle et le ressort ne stocke plus d'énergie :
$$E_{pe} = mgh \iff h = \dfrac{E_{pe}}{mg} = \dfrac{0{,}25}{0{,}025 \times 10} = 1\ \text{m}$$
(mesurée à partir de la position de compression maximale).

**2.1.** Axe vertical orienté vers le bas, origine à la position d'équilibre (où $mg = K\Delta l_0$). Forces : poids $m\vec{g}$ et tension $\vec{T}$, avec $T = K(\Delta l_0 + x)$. La deuxième loi de Newton projetée sur l'axe donne
$$mg - K(\Delta l_0 + x) = m\ddot{x} \iff \ddot{x} + \dfrac{K}{m}x = 0.$$

**2.2.** Solution : $x(t) = X_m\cos(\omega_0 t + \varphi)$ avec $\omega_0 = \sqrt{\dfrac{K}{m}} = \sqrt{\dfrac{200}{0{,}1}} = \sqrt{2000} \approx 44{,}7\ \text{rad/s}$.

À $t = 0$ : $x = +4\ \text{cm}$ (masse tirée vers le bas) et $\dot{x} = 0$, donc $X_m = 0{,}04\ \text{m}$ et $\varphi = 0$ :
$$x(t) = 0{,}04\cos(44{,}7\,t) \quad (x \text{ en m}, t \text{ en s}).$$

**2.3.** $T_0 = \dfrac{2\pi}{\omega_0} = 2\pi\sqrt{\dfrac{m}{K}} \approx 0{,}14\ \text{s}$ et $N_0 = \dfrac{1}{T_0} \approx 7{,}1\ \text{Hz}$.
""")

# ═══════════════════════════════ D 2016 — session normale ═════════════════════

_add("bac-d-2016-sn-pc-ex4", r"""
**Exercice 4 (5,5 points)**

*On néglige les frottements et on prendra $g = 10\ \text{m/s}^2$.*

Un skieur de masse totale $m = 80\ \text{kg}$ aborde une piste verglacée $A$, $B$, $C$, $D$ et $E$ (voir figure). Dans cet exercice, le skieur sera assimilé à un point matériel confondu avec son centre d'inertie $G$.

*D'après la figure :* $AB$ est horizontale ; $BC$ monte jusqu'à $C$ en faisant l'angle $\alpha$ avec la verticale passant par $C$ ; $CD$ est horizontale ; l'arc $DE$ est un quart de cercle de centre $O$ ($O$ à la hauteur de $D$, $E$ à la verticale de $O$), et $\theta$ est l'angle $(\overrightarrow{OD}, \overrightarrow{OM})$ repérant un point $M$ de l'arc ; $E$ est à $h = 5\ \text{m}$ au-dessus du sol ; le repère $(E, x, y)$ a l'axe $Ex$ horizontal et l'axe $Ey$ vertical vers le bas.

**1.** Partant sans vitesse du point $A$, il est poussé sur le parcours $AB$ par une force $\vec{F}$ parallèle à la piste pour arriver en $B$ avec une vitesse $\vec{V}_B$. Cette vitesse $\vec{V}_B$ lui permet d'atteindre le point $C$.

On donne : $AB = l = 20\ \text{m}$ ; $BC = l' = 40\ \text{m}$ ; $g = 10\ \text{m/s}^2$ et $\alpha = 60^\circ$.

**1.1.** Calculer la valeur de la vitesse $\vec{V}_B$ pour laquelle le skieur arrive en $C$ avec une vitesse nulle.

**1.2.** Calculer alors la valeur supposée constante de la force $\vec{F}$.

**1.3.** Déterminer la nature du mouvement du skieur entre $B$ et $C$ sachant que $\vec{F}$ ne s'exerce qu'entre $A$ et $B$.

**2.** En arrivant en $C$, le skieur s'aide de ses bâtons pour repartir sur $CD$, horizontale, et acquérir au point $D$ une vitesse de valeur $V_D = 10\ \text{m/s}$ avec laquelle il entame le tronçon circulaire $DE$ de rayon $r = OD = OE = 2{,}2\ \text{m}$.

**2.1.** En supposant que sur $CD$ le skieur n'utilise plus ses bâtons, exprimer :

**2.1.1.** La valeur $V_M$ de la vitesse du skieur au point $M$ en fonction de $V_D$, $r$, $g$ et de l'angle $\theta$, et en déduire sa valeur au point $E$.

**2.1.2.** La valeur $R$ de la réaction exercée par la piste sur le skieur au point $M$ en fonction de $m$, $V_D$, $r$, $g$ et de l'angle $\theta$.

**2.2.** Le skieur quitte la piste au point $E$ pour arriver au point $P$ situé sur le sol.

**2.2.1.** Calculer l'équation de la trajectoire dans le repère $(E, x, y)$.

**2.2.2.** Calculer l'abscisse du point $P$ de chute.
""", r"""
**1.1.** Sur $BC$, seuls le poids et la réaction (perpendiculaire à la piste, travail nul) agissent. La dénivellation entre $B$ et $C$ vaut $h_C = l'\cos\alpha = 40 \times 0{,}5 = 20\ \text{m}$ (l'angle $\alpha$ est pris par rapport à la verticale).

Théorème de l'énergie cinétique entre $B$ et $C$ ($V_C = 0$) :
$$0 - \dfrac{1}{2}mV_B^2 = -mgh_C \iff V_B = \sqrt{2gl'\cos\alpha} = \sqrt{2 \times 10 \times 20} = 20\ \text{m/s}.$$

**1.2.** Sur $AB$ (horizontale), seule $\vec{F}$ travaille :
$$\dfrac{1}{2}mV_B^2 - 0 = F \times l \iff F = \dfrac{mV_B^2}{2l} = \dfrac{80 \times 400}{40} = 800\ \text{N}.$$

**1.3.** Entre $B$ et $C$, la deuxième loi de Newton projetée sur la ligne de pente (orientée vers $C$) donne $a = -g\cos\alpha = -5\ \text{m/s}^2$ : l'accélération est constante et opposée à la vitesse, le mouvement est **rectiligne uniformément décéléré** (vérification : $V_B^2 = 2 \times 5 \times 40 = 400$).

**2.1.1.** Entre $D$ et $M$, le skieur descend de $r\sin\theta$ ; la réaction ne travaille pas. Théorème de l'énergie cinétique :
$$\dfrac{1}{2}mV_M^2 - \dfrac{1}{2}mV_D^2 = mgr\sin\theta \iff V_M = \sqrt{V_D^2 + 2gr\sin\theta}.$$

En $E$ ($\theta = 90^\circ$) : $V_E = \sqrt{100 + 2 \times 10 \times 2{,}2} = \sqrt{144} = 12\ \text{m/s}$.

**2.1.2.** En $M$, le skieur est à l'intérieur de l'arc ; la réaction $\vec{R}$ est dirigée vers le centre $O$. Sur la normale orientée de $M$ vers $O$, la composante du poids vaut $-mg\sin\theta$ et l'accélération normale vaut $\dfrac{V_M^2}{r}$ :
$$R - mg\sin\theta = m\dfrac{V_M^2}{r} \iff R = m\left(\dfrac{V_D^2}{r} + 3g\sin\theta\right).$$

**2.2.1.** En $E$, la vitesse est horizontale ($V_E = 12\ \text{m/s}$) ; dans l'air, seul le poids agit : $a_x = 0$, $a_y = g$ (axe $Ey$ vers le bas). Donc $x = V_Et$ et $y = \dfrac{1}{2}gt^2$, d'où
$$y = \dfrac{g}{2V_E^2}x^2 = \dfrac{10}{288}x^2 = \dfrac{5}{144}x^2.$$

**2.2.2.** Le sol est à $y = h = 5\ \text{m}$ : $\dfrac{5}{144}x_P^2 = 5 \iff x_P = 12\ \text{m}$.
""", note="Lecture de la figure : l'angle α = 60° est pris entre la piste BC et la verticale passant par C (dénivellation BC·cos α = 20 m, ce qui donne des valeurs exactes V_B = 20 m/s, F = 800 N, V_E = 12 m/s).")

# ═══════════════════════════════ D 2017 — session normale ═════════════════════

_add("bac-d-2017-sn-pc-ex3", r"""
**Exercice 3 (6 points)**

*Les frottements sont négligeables.*

Soit un ressort $R$ élastique de masse négligeable, de constante de raideur $K = 20\ \text{N/m}$, guidé par une tige horizontale. Une des extrémités est fixée en un point $A$, l'autre est attachée à un solide ponctuel $S$ de masse $m$, qui coulisse sur la tige. Dans la position d'équilibre, le centre d'inertie $G$ du solide est en $O$.

**1.** Établir l'équation différentielle du mouvement de $S$.

**2.** Écrire l'équation horaire du mouvement $x = f(t)$ sachant qu'à l'instant $t = 0$ le centre d'inertie $G$ du solide passe en $O$ dans le sens positif et qu'il décrit un segment de $4\ \text{cm}$ au cours des oscillations dont la période est $T = 0{,}05\ \text{s}$.

**3.** Montrer que l'énergie mécanique $E$ du système est égale à $4 \times 10^{-3}\ \text{J}$, sachant que l'énergie potentielle de pesanteur au niveau de la tige est nulle.

**4.** Calculer l'énergie cinétique du système à l'instant $t = 0{,}25\ \text{s}$.

**5.** À la date $t = 5\ \text{s}$, la masse se détache du ressort et se déplace suivant une piste $OABC$ constituée de deux parties :
- $OA$ rectiligne ;
- $ABC$ en forme de demi-cercle de centre $O''$ et de rayon $r = 10\ \text{cm}$.

*D'après la figure :* $OA$ est horizontale ; $A$ est le point bas du demi-cercle et $C$ son point haut, à la verticale de $A$.

**5.1.** Calculer la vitesse du solide $S$ à l'arrivée en $A$.

**5.2.** Trouver l'expression de la vitesse de $S$ en $M$ tel que $\widehat{AO''M} = \theta$ et calculer sa valeur au point $C$. On donne $g = 10\ \text{m/s}^2$.
""", r"""
**1.** Forces sur $S$ : poids et réaction de la tige (verticales, qui se compensent), tension du ressort $\vec{T} = -Kx\,\vec{i}$. Deuxième loi de Newton sur l'axe horizontal :
$$-Kx = m\ddot{x} \iff \ddot{x} + \dfrac{K}{m}x = 0.$$

**2.** $x(t) = X_m\sin(\omega_0 t + \varphi)$ avec $X_m = \dfrac{4}{2} = 2\ \text{cm}$ et $\omega_0 = \dfrac{2\pi}{T} = \dfrac{2\pi}{0{,}05} = 40\pi\ \text{rad/s}$.

À $t = 0$ : $x = 0$ et $\dot{x} > 0$, donc $\varphi = 0$ :
$$x(t) = 0{,}02\sin(40\pi t) \quad (x \text{ en m}).$$

(La masse vaut alors $m = \dfrac{K}{\omega_0^2} = \dfrac{20}{(40\pi)^2} \approx 1{,}27 \times 10^{-3}\ \text{kg}$.)

**3.** $E = E_c + E_{pe} = \dfrac{1}{2}m\dot{x}^2 + \dfrac{1}{2}Kx^2$. Sans frottement, $E$ est constante ; en une position extrême ($x = X_m$, $\dot{x} = 0$) :
$$E = \dfrac{1}{2}KX_m^2 = \dfrac{1}{2} \times 20 \times 0{,}02^2 = 4 \times 10^{-3}\ \text{J}.$$

**4.** $\dfrac{0{,}25}{0{,}05} = 5$ : à $t = 0{,}25\ \text{s}$, cinq périodes se sont écoulées et $S$ repasse en $O$ ($x = 0$). Donc $E_c = E = 4 \times 10^{-3}\ \text{J}$.

**5.1.** $t = 5\ \text{s} = 100\,T$ : $S$ est en $O$ et se déplace dans le sens positif avec la vitesse maximale $V_0 = X_m\omega_0 = 0{,}02 \times 40\pi = 0{,}8\pi \approx 2{,}51\ \text{m/s}$.

Sur $OA$ horizontale sans frottement, la vitesse se conserve : $V_A = 0{,}8\pi \approx 2{,}51\ \text{m/s}$.

**5.2.** Entre $A$ et $M$, $S$ s'élève de $r(1 - \cos\theta)$ ; la réaction ne travaille pas. Théorème de l'énergie cinétique :
$$V_M = \sqrt{V_A^2 - 2gr(1 - \cos\theta)}.$$

En $C$ ($\theta = \pi$) : $V_C = \sqrt{V_A^2 - 4gr} = \sqrt{6{,}32 - 4} \approx 1{,}52\ \text{m/s}$.
""")

# ═══════════════════════════════ D 2018 — session complémentaire ══════════════

_add("bac-d-2018-sc-pc-ex3", r"""
**Exercice 3 (6 points)**

Sur un tremplin de surface parfaitement lisse incliné d'un angle $\alpha = 30^\circ$ par rapport à l'horizontale, un jouet $S$ d'enfant constitué d'une petite voiture en partie cassable, initialement au repos au point $A$, est tiré par une force constante $\vec{F}$, inclinée d'un angle $\theta$ par rapport au plan du tremplin.

Ce jouet $S$ a une masse $m = 100\ \text{g}$ (voir fig. 2). On donne $\cos\theta = 0{,}8$ ; $AB = 2\ \text{m}$ ; $AC = 2{,}7\ \text{m}$ ; $g = 10\ \text{m/s}^2$.

*D'après la figure :* $A$ est au niveau du sol ; $B$ et $C$ sont sur le tremplin ; le repère $(C, \vec{i}, \vec{j})$ a l'axe $Cx$ horizontal et l'axe $Cy$ vertical vers le haut.

**1.** La vitesse atteinte par $S$ au point $B$ après le parcours rectiligne $AB$ est égale à $V_B = 4\ \text{m/s}$.

**1.1.** Calculer la valeur de $F$.

**1.2.** Déterminer la nature du mouvement de $S$ sur le trajet $AB$.

**1.3.** Au point $B$, l'action de la force $\vec{F}$ cesse ; le solide poursuit son mouvement rectiligne jusqu'au sommet $C$ du tremplin. Déterminer la nature du mouvement de $S$ sur le trajet $BC$. Calculer la vitesse de $S$ au point $C$.

**2.** Le solide quitte le tremplin au point $C$, origine du repère $(C, \vec{i}, \vec{j})$.

**2.1.** Déterminer l'équation cartésienne de la trajectoire de $S$ dans le repère $(C, \vec{i}, \vec{j})$. L'instant de passage de $S$ en $C$ est considéré comme origine des dates.

**2.2.** $S$ atteint le sol au point d'impact $D$.

**2.2.1.** Calculer les coordonnées du point $D$.

**2.2.2.** Sachant que le solide est brisé s'il touche le sol avec une vitesse supérieure à $5\ \text{m/s}$, dans quel état se trouve $S$ après la chute ?
""", r"""
**1.1.** Sur $AB$, $S$ part du repos et atteint $V_B = 4\ \text{m/s}$ sur $2\ \text{m}$ : $a = \dfrac{V_B^2}{2\,AB} = \dfrac{16}{4} = 4\ \text{m/s}^2$ (la force étant constante, l'accélération l'est aussi).

Deuxième loi de Newton projetée sur la ligne de pente (la réaction du plan lisse est perpendiculaire) :
$$F\cos\theta - mg\sin\alpha = ma \iff F = \dfrac{m(a + g\sin\alpha)}{\cos\theta} = \dfrac{0{,}1 \times (4 + 5)}{0{,}8} = 1{,}125\ \text{N}.$$

**1.2.** L'accélération est constante ($a = 4\ \text{m/s}^2$) et de même sens que la vitesse : mouvement **rectiligne uniformément accéléré**.

**1.3.** Sans $\vec{F}$ : $a' = -g\sin\alpha = -5\ \text{m/s}^2$, constante et opposée à la vitesse : mouvement **rectiligne uniformément décéléré**.

$BC = AC - AB = 0{,}7\ \text{m}$, donc $V_C^2 = V_B^2 + 2a'\,BC = 16 - 7 = 9$ : $V_C = 3\ \text{m/s}$.

**2.1.** En $C$, $\vec{V}_C$ fait l'angle $\alpha = 30^\circ$ avec l'horizontale. Dans l'air, seul le poids agit : $a_x = 0$, $a_y = -g$.
$$x = V_C\cos\alpha\,t, \qquad y = -\dfrac{1}{2}gt^2 + V_C\sin\alpha\,t,$$
$$y = -\dfrac{g}{2V_C^2\cos^2\alpha}x^2 + x\tan\alpha = -\dfrac{20}{27}x^2 + \dfrac{\sqrt{3}}{3}x \approx -0{,}74x^2 + 0{,}58x.$$

**2.2.1.** $C$ est à la hauteur $AC\sin\alpha = 2{,}7 \times 0{,}5 = 1{,}35\ \text{m}$ au-dessus du sol. Au point $D$ : $y_D = -1{,}35\ \text{m}$, soit
$$-\dfrac{20}{27}x^2 + \dfrac{\sqrt{3}}{3}x + 1{,}35 = 0,$$
dont la racine positive est $x_D \approx 1{,}79\ \text{m}$. Donc $D(1{,}79\ \text{m}\,;\,-1{,}35\ \text{m})$.

**2.2.2.** Entre $C$ et $D$, seul le poids travaille :
$$V_D = \sqrt{V_C^2 + 2g \times 1{,}35} = \sqrt{9 + 27} = 6\ \text{m/s} > 5\ \text{m/s} :$$
le jouet est **brisé**.
""", note="Le texte OCR nommait l'angle de la force β ; le sujet écrit θ (cos θ = 0,8).")

# ═══════════════════════════════ D 2019 — session normale ═════════════════════

_add("bac-d-2019-sn-pc-ex4", r"""
**Exercice 4 (5 points)**

*Les frottements sont négligeables.*

On considère un ressort à spires non jointives de masse négligeable et de raideur $K = 50\ \text{N/m}$. Le ressort est placé sur une table horizontale. On fixe l'une des extrémités du ressort et on accroche à son autre extrémité un solide ponctuel $S$ de masse $m = 500\ \text{g}$.

À l'instant $t = 0$, on déplace le solide de sa position d'équilibre d'une distance $x_0 = 2\ \text{cm}$ et on lui communique une vitesse $v_0 = \dfrac{\sqrt{3}}{5}\ \text{m/s}$.

**1.** Établir l'équation différentielle qui régit le mouvement du centre d'inertie du solide.

**2.** Déterminer l'équation horaire du mouvement. Quelle est la vitesse au passage par la position d'équilibre dans le sens positif ?

**3.** Exprimer l'énergie mécanique de cet oscillateur et montrer qu'elle est constante. Retrouver la valeur maximale de la vitesse du mobile en utilisant le principe de la conservation de l'énergie mécanique.

**4.** Le solide se détache du ressort au passage par la position d'équilibre $O$ dans le sens positif et continue son mouvement sur la table pour la quitter au point $O'$ et atteindre le point $A$ au sol situé $5\ \text{cm}$ plus bas (voir figure : axe $O'x$ horizontal, axe $O'y$ vertical vers le bas). L'instant de passage de $S$ en $O'$ est considéré comme origine des dates.

**4.1.** Déterminer l'équation cartésienne de la trajectoire de $S$ dans le repère $(O', x, y)$.

**4.2.** Trouver les coordonnées du point $A$.

**4.3.** Calculer les composantes du vecteur vitesse $\vec{V}_A$ au point $A$ ; en déduire son module, puis préciser l'angle $\beta$ qu'il fait avec la verticale passant par $A$.
""", r"""
**1.** Sur l'axe horizontal $Ox$ (origine à l'équilibre), seule la tension du ressort $-Kx\,\vec{i}$ a une composante (poids et réaction se compensent) :
$$m\ddot{x} = -Kx \iff \ddot{x} + \dfrac{K}{m}x = 0, \qquad \omega_0 = \sqrt{\dfrac{K}{m}} = \sqrt{\dfrac{50}{0{,}5}} = 10\ \text{rad/s}.$$

**2.** $x(t) = X_m\cos(10t + \varphi)$. Le sujet ne précise pas les sens ; on prend $x_0 = +2\ \text{cm}$ et $v_0$ dans le sens positif.

Amplitude : $X_m = \sqrt{x_0^2 + \left(\dfrac{v_0}{\omega_0}\right)^2} = \sqrt{4 \times 10^{-4} + 12 \times 10^{-4}} = 0{,}04\ \text{m}$.

Phase : $\cos\varphi = \dfrac{x_0}{X_m} = \dfrac{1}{2}$ et $\dot{x}(0) = -X_m\omega_0\sin\varphi > 0$, donc $\sin\varphi < 0$ : $\varphi = -\dfrac{\pi}{3}$.
$$x(t) = 0{,}04\cos\left(10t - \dfrac{\pi}{3}\right) \quad (x \text{ en m}).$$

(Avec d'autres sens, seule la phase change : $\varphi = +\frac{\pi}{3}$ si $v_0$ est dans le sens négatif ; $\varphi = \pm\frac{2\pi}{3}$ si $x_0 = -2\ \text{cm}$.)

Au passage par l'équilibre dans le sens positif : $v = X_m\omega_0 = 0{,}04 \times 10 = 0{,}4\ \text{m/s}$.

**3.** $E = \dfrac{1}{2}m\dot{x}^2 + \dfrac{1}{2}Kx^2$ (énergie potentielle de pesanteur constante, prise nulle). $\dfrac{dE}{dt} = \dot{x}(m\ddot{x} + Kx) = 0$ d'après l'équation différentielle : $E$ est **constante**.

$E = \dfrac{1}{2}Kx_0^2 + \dfrac{1}{2}mv_0^2 = \dfrac{1}{2} \times 50 \times 4 \times 10^{-4} + \dfrac{1}{2} \times 0{,}5 \times 0{,}12 = 0{,}01 + 0{,}03 = 0{,}04\ \text{J}$.

La vitesse est maximale en $x = 0$ : $\dfrac{1}{2}mV_{\max}^2 = E \iff V_{\max} = \sqrt{\dfrac{2E}{m}} = \sqrt{0{,}16} = 0{,}4\ \text{m/s}$.

**4.1.** Sur la table (sans frottement), la vitesse reste $V = 0{,}4\ \text{m/s}$ ; en $O'$ elle est horizontale. Dans l'air : $a_x = 0$, $a_y = g$ (axe vers le bas), donc $x = Vt$, $y = \dfrac{1}{2}gt^2$ :
$$y = \dfrac{g}{2V^2}x^2 = \dfrac{10}{2 \times 0{,}16}x^2 = 31{,}25\,x^2.$$

**4.2.** $y_A = 0{,}05\ \text{m}$ : $x_A^2 = \dfrac{0{,}05}{31{,}25} = 1{,}6 \times 10^{-3}$, $x_A = 0{,}04\ \text{m}$. Donc $A(4\ \text{cm}\,;\,5\ \text{cm})$.

**4.3.** $t_A = \dfrac{x_A}{V} = 0{,}1\ \text{s}$ ; $V_{Ax} = 0{,}4\ \text{m/s}$ et $V_{Ay} = gt_A = 1\ \text{m/s}$.

$V_A = \sqrt{0{,}4^2 + 1^2} = \sqrt{1{,}16} \approx 1{,}08\ \text{m/s}$ ; $\tan\beta = \dfrac{V_{Ax}}{V_{Ay}} = 0{,}4$, d'où $\beta \approx 21{,}8^\circ$.
""", note="Le scan est coupé à gauche (numéros 4.1 à 4.3 et début de lignes restitués). Le sujet ne précise pas les sens de x0 et v0 : la correction prend les deux positifs et indique la phase dans les autres cas. Le sujet nomme l'angle final β.")

# ═══════════════════════════════ D 2020 — session complémentaire ══════════════

_add("bac-d-2020-sc-pc-ex3", r"""
**Exercice 3 (6 points)**

*On néglige les frottements dans tout l'exercice.*

Un ressort $R$ de masse négligeable, à spires non jointives, de raideur $K = 10\ \text{N/m}$, peut se déplacer suivant l'axe horizontal $Ox$ sur le plan horizontal $AB$. On fixe l'une des extrémités en $A$ et on accroche à l'autre extrémité un solide $S$ de masse $m = 100\ \text{g}$. Lorsque $S$ est en équilibre, son centre d'inertie $G$ coïncide avec l'origine $O$ des abscisses (voir figure).

**1.** On déplace le solide $S$ de sa position d'équilibre suivant $X'X$ de $4\ \text{cm}$ et on l'abandonne sans vitesse initiale à $t = 0$.

**1.1.** Établir l'équation différentielle du mouvement de $G$.

**1.2.** Déterminer l'équation horaire du mouvement de $S$.

**2.** Exprimer, à la date $t$, l'énergie mécanique totale $E$ du système (ressort + solide + terre) en fonction de $K$ et de l'élongation maximale $x_m$. L'énergie potentielle de pesanteur est nulle dans le plan horizontal passant par $G$.

**3.** Au passage par $O$ dans le sens positif, le solide $S$ se détache du ressort et continue son mouvement sur le plan $AB$ avant de le quitter en $B$ pour tomber en $C$ sur le sol situé à $h = 2\ \text{m}$ plus bas (voir figure : repère $(B; \vec{i}, \vec{j})$, $\vec{i}$ horizontal, $\vec{j}$ vertical vers le haut).

**3.1.** Déterminer l'équation de la trajectoire du mouvement du solide $S$ après passage par $B$ dans le repère $(B; \vec{i}, \vec{j})$. Conclure.

**3.2.** Trouver l'abscisse du point de chute $C$.

**3.3.** Calculer la vitesse du solide $S$ à son arrivée en $C$.
""", r"""
**1.1.** Sur l'axe $Ox$ : $m\ddot{x} = -Kx$, soit $\ddot{x} + \dfrac{K}{m}x = 0$, avec $\omega_0 = \sqrt{\dfrac{10}{0{,}1}} = 10\ \text{rad/s}$.

**1.2.** $x(t) = x_m\cos(10t + \varphi)$ avec $x_m = 0{,}04\ \text{m}$ (abandon sans vitesse). En prenant le déplacement initial dans le sens positif ($x(0) = +4\ \text{cm}$) : $\varphi = 0$ et
$$x(t) = 0{,}04\cos(10t) \quad (x \text{ en m}).$$
(Si le solide est écarté dans le sens négatif : $x(t) = 0{,}04\cos(10t + \pi)$.)

**2.** $E = \dfrac{1}{2}m\dot{x}^2 + \dfrac{1}{2}Kx^2$. Avec $x = x_m\cos(\omega_0t + \varphi)$ et $m\omega_0^2 = K$ :
$$E = \dfrac{1}{2}Kx_m^2\sin^2(\omega_0t + \varphi) + \dfrac{1}{2}Kx_m^2\cos^2(\omega_0t + \varphi) = \dfrac{1}{2}Kx_m^2 = 8 \times 10^{-3}\ \text{J}.$$

**3.1.** En $O$, la vitesse est maximale : $V_0 = x_m\omega_0 = 0{,}4\ \text{m/s}$ ; sur $AB$ sans frottement, elle se conserve : en $B$, $\vec{V}_B$ est horizontale, $V_B = 0{,}4\ \text{m/s}$.

Après $B$, seul le poids agit : $a_x = 0$, $a_y = -g$. Donc $x = V_Bt$ et $y = -\dfrac{1}{2}gt^2$ :
$$y = -\dfrac{g}{2V_B^2}x^2 = -31{,}25\,x^2.$$

La trajectoire est un **arc de parabole**.

**3.2.** En $C$ : $y_C = -h = -2\ \text{m}$, donc $x_C = \sqrt{\dfrac{2}{31{,}25}} = \sqrt{0{,}064} \approx 0{,}25\ \text{m}$.

**3.3.** Théorème de l'énergie cinétique entre $B$ et $C$ :
$$V_C = \sqrt{V_B^2 + 2gh} = \sqrt{0{,}16 + 40} \approx 6{,}34\ \text{m/s}.$$
""", note="Le sujet ne précise pas le sens de l'écart initial : la correction prend le sens positif et donne aussi l'autre cas.")

# ═══════════════════════════════ D 2020 — session normale ═════════════════════

_add("bac-d-2020-sn-pc-ex3", r"""
**Exercice 3 (5,5 points)**

*Dans tout l'exercice les frottements sont négligeables.*

Un solide $S$ assimilable à un point matériel de masse $m$ est abandonné au point $A$ de la ligne de plus grande pente d'un plan incliné d'un angle $\alpha$ par rapport à l'horizontale (voir fig. 2). Il glisse sur $AB$ et arrive en $B$ avec la vitesse $V_B$.

On donne $\alpha = 30^\circ$ et $g = 10\ \text{m/s}^2$.

*D'après la figure :* $A$ est à la hauteur $h = 1{,}25\ \text{m}$ au-dessus de la droite horizontale $BC$ ; entre $B$ et $C$ la piste est un creux circulaire ; en $C$ la vitesse $\vec{V}_C$ fait l'angle $\alpha$ avec l'horizontale ; le repère $(C; x, y)$ a l'axe $Cx$ horizontal et l'axe $Cy$ vertical vers le haut ; $P$ est sur l'axe $Cx$.

**1.1.** Établir l'équation horaire du mouvement du solide $S$ sur $AB$.

**1.2.** Calculer la longueur $l = AB$, en déduire les valeurs de la vitesse en $B$ et en $C$.

**2.** Le solide quitte la piste au point $C$ pour tomber au point $P$ sur l'axe $Cx$.

**2.1.** Établir l'équation de la trajectoire du mobile entre $C$ et $P$ dans le repère $(Cx; Cy)$ en fonction de $V_B$, $\alpha$ et $g$.

**2.2.** Donner l'expression de la portée $CP$ en fonction de $V_B$, $\alpha$ et $g$ puis en fonction de $l$ et $\alpha$. Calculer $CP$.

**2.3.** Donner l'expression de la flèche en fonction de $V_B$, $\alpha$ et $g$. Pour quelle valeur de $\alpha$ cette flèche est-elle maximale ?
""", r"""
**1.1.** Axe $Ax$ le long de la pente, orienté vers $B$, origine en $A$. Deuxième loi de Newton projetée (la réaction est perpendiculaire) : $a = g\sin\alpha = 5\ \text{m/s}^2$. Départ sans vitesse en $x = 0$ :
$$x(t) = \dfrac{1}{2}g\sin\alpha\,t^2 = 2{,}5\,t^2 \quad (x \text{ en m}, t \text{ en s}).$$

**1.2.** $l = AB = \dfrac{h}{\sin\alpha} = \dfrac{1{,}25}{0{,}5} = 2{,}5\ \text{m}$.

$V_B = \sqrt{2al} = \sqrt{2 \times 5 \times 2{,}5} = 5\ \text{m/s}$.

$B$ et $C$ sont à la même hauteur et la piste $BC$ est sans frottement : $V_C = V_B = 5\ \text{m/s}$.

**2.1.** En $C$ : $V_{Cx} = V_B\cos\alpha$ et $V_{Cy} = V_B\sin\alpha$ ; seul le poids agit ($a_x = 0$, $a_y = -g$) :
$$x = V_B\cos\alpha\,t, \qquad y = -\dfrac{1}{2}gt^2 + V_B\sin\alpha\,t,$$
$$y = -\dfrac{g}{2V_B^2\cos^2\alpha}x^2 + x\tan\alpha \quad \left(\text{ici } y = -\dfrac{4}{15}x^2 + \dfrac{\sqrt{3}}{3}x\right).$$

**2.2.** $y = 0$ pour $x \neq 0$ : $CP = \dfrac{2V_B^2\sin\alpha\cos\alpha}{g} = \dfrac{V_B^2\sin 2\alpha}{g}$.

Avec $V_B^2 = 2gl\sin\alpha$ : $CP = 2l\sin\alpha\sin 2\alpha$.
$$CP = \dfrac{25 \times \sin 60^\circ}{10} \approx 2{,}17\ \text{m}.$$

**2.3.** Au sommet, $V_y = 0$ : la flèche vaut $H = \dfrac{V_B^2\sin^2\alpha}{2g}$ ($= 0{,}3125\ \text{m}$ ici).

À $V_B$ donnée, $H$ croît avec $\sin^2\alpha$ : elle est maximale pour $\alpha = 90^\circ$ (lancement vertical, $H_{\max} = \dfrac{V_B^2}{2g}$). C'est aussi vrai avec $V_B^2 = 2gl\sin\alpha$, puisque $H = l\sin^3\alpha$.
""")

# ═══════════════════════════════ D 2021 — session complémentaire ══════════════

_add("bac-d-2021-sc-pc-ex3", r"""
**Exercice 3 (5 points)**

*On prendra $g = 10\ \text{m/s}^2$.*

Un skieur de masse $m = 60\ \text{kg}$ peut glisser à partir du sommet $O'$ d'un mont couvert de neige au versant duquel se trouve un bassin d'eau de largeur $d = BC = 10\ \text{m}$.

**1.** Dans cette question, on suppose que le skieur glisse sans frottement le long de la ligne de plus grande pente d'un plan incliné d'un angle $\theta = 30^\circ$ par rapport à la verticale. Le skieur quitte le point $O'$, origine de l'axe orienté $x'x$, sans vitesse initiale.

**1.1.** Déterminer la nature du mouvement sur la ligne de plus grande pente du plan incliné.

**1.2.** Donner en fonction de $x$ l'expression de l'énergie cinétique $E_c$ et de l'énergie potentielle $E_p$ du solide lorsque ce dernier occupe une position d'abscisse $x$ comptée à partir de $O'$. *On prendra pour référence de l'énergie potentielle le plan horizontal passant par un point $A$ situé en dessous du point $O'$ tel que $O'A = L$.*

**1.3.** En déduire l'expression de l'énergie mécanique $E$.

**2.** Dans cette question on suppose que le skieur débute son mouvement au point $D$ situé à la hauteur $h$ au-dessus de l'horizontale passant par $O$ (voir la figure). Arrivé au point $O$, le skieur quitte le mont avec une vitesse $\vec{V}_0$ faisant l'angle $\alpha = 60^\circ$ avec l'axe $Ox$, situé à une hauteur $H = 0{,}5\ \text{m}$ au-dessus de la surface du bassin d'eau de largeur $BC$.

*D'après la figure :* $A$ et $O$ sont sur la même horizontale, $A$ au bas de la pente ; $B$ est à la verticale de $O$ ; le repère $(O; x, y)$ a $Ox$ horizontal vers le bassin et $Oy$ vertical vers le haut.

On veut déterminer la valeur minimale $h_m$ de la hauteur $h$ pour que le skieur ne tombe pas dans le bassin d'eau.

**2.1.** Exprimer la vitesse $V_A$ en fonction de $h$ et $g$.

**2.2.** Établir dans le repère $(O; x; y)$ l'équation de la trajectoire du mouvement du skieur à partir de l'instant $t = 0$ où il quitte le point $O$.

**2.3.** Donner les expressions des coordonnées du sommet $S$ de la trajectoire.

**2.4.** Déterminer la valeur minimale $h_m$ de la hauteur $h$ pour que le skieur ne tombe pas dans le bassin d'eau.
""", r"""
**1.1.** Forces : poids et réaction (perpendiculaire à la piste). Sur l'axe $x'x$ (ligne de pente, vers le bas), la composante du poids vaut $mg\cos\theta$ (le plan fait $\theta$ avec la verticale) :
$$a = g\cos\theta = 10 \times \dfrac{\sqrt{3}}{2} \approx 8{,}66\ \text{m/s}^2,$$
constante et de même sens que la vitesse : mouvement **rectiligne uniformément accéléré**.

**1.2.** Théorème de l'énergie cinétique entre $O'$ ($V = 0$) et la position $x$ (le skieur est descendu de $x\cos\theta$) :
$$E_c = mgx\cos\theta \approx 519{,}6\,x\ \text{(J)}.$$

L'altitude au-dessus du plan de référence est $L - x\cos\theta$ :
$$E_p = mg(L - x\cos\theta).$$

**1.3.** $E = E_c + E_p = mgL$ : l'énergie mécanique est constante ($= 600\,L$ en joules).

**2.1.** Théorème de l'énergie cinétique entre $D$ (vitesse nulle) et $A$, situé $h$ plus bas : $V_A = \sqrt{2gh}$. Comme $A$ et $O$ sont sur la même horizontale (piste sans frottement), $V_0 = V_A = \sqrt{2gh}$.

**2.2.** Seul le poids agit : $a_x = 0$, $a_y = -g$ ; $V_{0x} = V_0\cos\alpha$, $V_{0y} = V_0\sin\alpha$ :
$$x = V_0\cos\alpha\,t, \qquad y = -\dfrac{1}{2}gt^2 + V_0\sin\alpha\,t,$$
$$y = -\dfrac{g}{2V_0^2\cos^2\alpha}x^2 + x\tan\alpha = -\dfrac{1}{4h\cos^2\alpha}x^2 + x\tan\alpha = -\dfrac{x^2}{h} + \sqrt{3}\,x.$$

**2.3.** Au sommet, $\dfrac{dy}{dx} = 0$ :
$$x_S = 2h\sin\alpha\cos\alpha = h\sin 2\alpha = \dfrac{\sqrt{3}}{2}h, \qquad y_S = h\sin^2\alpha = \dfrac{3}{4}h.$$

**2.4.** Le skieur ne tombe pas dans le bassin s'il atteint le niveau de l'eau ($y = -H = -0{,}5\ \text{m}$) au-delà de $C$, c'est-à-dire si $y(d) \ge -H$ avec $d = 10\ \text{m}$ :
$$-\dfrac{100}{h} + 10\sqrt{3} \ge -0{,}5 \iff h \ge \dfrac{100}{10\sqrt{3} + 0{,}5}.$$

$$h_m = \dfrac{100}{10\sqrt{3} + 0{,}5} \approx 5{,}61\ \text{m}.$$
""")

# ═══════════════════════════════ D 2021 — session normale ═════════════════════

_add("bac-d-2021-sn-pc-ex3", r"""
**Exercice 3 (6 points)**

*On donne $g = 10\ \text{m/s}^2$.*

On suspend à l'extrémité inférieure d'un ressort de masse négligeable à spires non jointives et de coefficient de raideur $K$ un solide $S$ de masse $m = 100\ \text{g}$ (voir fig. 1). À l'équilibre, le ressort est allongé de $10\ \text{cm}$.

**1.** Calculer la raideur $K$ du ressort.

**2.** Le ressort est maintenant placé sur un plan horizontal et la masse peut se déplacer sans frottement le long de l'axe horizontal $X'X$ (fig. 2). À la date $t = 0$, le solide $S$ étant en position d'équilibre, on lui communique une vitesse $\vec{V}_0$ de valeur $V_0 = 0{,}4\ \text{m/s}$ dirigée suivant l'axe $X'X$ du ressort comme l'indique la figure.

*D'après la figure :* $\vec{V}_0$ est dans le sens positif de l'axe.

**2.1.** Établir l'équation différentielle du mouvement du centre d'inertie $G$ du solide $S$.

**2.2.** Déterminer l'équation horaire du mouvement de $G$.

**3.1.** On prendra l'énergie potentielle de pesanteur du système nulle sur le plan horizontal passant par $G$. Exprimer, à la date $t$, l'énergie mécanique totale $E$ du système (ressort − solide − terre) en fonction de $K$, $m$, $x$ et $V$, puis en fonction de $K$ et de l'élongation maximale $x_m$.

**3.2.** Retrouver l'équation différentielle établie en 2.1. à partir de l'expression de l'énergie mécanique $E$.
""", r"""
**1.** À l'équilibre : $K\Delta l_0 = mg \iff K = \dfrac{mg}{\Delta l_0} = \dfrac{0{,}1 \times 10}{0{,}1} = 10\ \text{N/m}$.

**2.1.** Sur l'axe horizontal (origine $O$ à l'équilibre) : $m\ddot{x} = -Kx$, soit $\ddot{x} + \dfrac{K}{m}x = 0$, avec $\omega_0 = \sqrt{\dfrac{10}{0{,}1}} = 10\ \text{rad/s}$.

**2.2.** $x(t) = x_m\sin(\omega_0t + \varphi)$. À $t = 0$ : $x = 0$ et $\dot{x} = V_0 > 0$, donc $\varphi = 0$ et $x_m = \dfrac{V_0}{\omega_0} = \dfrac{0{,}4}{10} = 0{,}04\ \text{m}$ :
$$x(t) = 0{,}04\sin(10t) \quad (x \text{ en m}).$$

**3.1.** $E = \dfrac{1}{2}mV^2 + \dfrac{1}{2}Kx^2$. Avec $x = x_m\sin(\omega_0t)$, $V = x_m\omega_0\cos(\omega_0t)$ et $m\omega_0^2 = K$ :
$$E = \dfrac{1}{2}Kx_m^2\left(\cos^2(\omega_0t) + \sin^2(\omega_0t)\right) = \dfrac{1}{2}Kx_m^2 = 8 \times 10^{-3}\ \text{J}.$$

**3.2.** $E$ est constante : $\dfrac{dE}{dt} = mV\dot{V} + Kx\dot{x} = \dot{x}(m\ddot{x} + Kx) = 0$. Comme $\dot{x}$ n'est pas identiquement nulle, $m\ddot{x} + Kx = 0$ : on retrouve $\ddot{x} + \dfrac{K}{m}x = 0$.
""")

# ═══════════════════════════════ D 2022 — session complémentaire ══════════════

_add("bac-d-2022-sc-pc-ex3", r"""
**Exercice 3 (5,5 points)**

*On donne $g = 10\ \text{m/s}^2$.*

**1.** Un point matériel $M$ de masse $m = 50\ \text{g}$ est lancé à partir du point $O$ vers le haut d'un plan incliné de $15^\circ$ par rapport à l'horizontale avec une vitesse de valeur $V_0 = 3\ \text{m/s}$. La longueur de ce plan est $OA = 1\ \text{m}$.

**1.1.** Si l'on suppose que les frottements sont négligeables, avec quelle vitesse $V_A$ le point matériel arrive-t-il au sommet du plan incliné ?

**1.2.** En réalité il y a frottement et la vitesse atteinte au point $A$ par le point matériel vaut $V'_A = 1\ \text{m/s}$. Déterminer l'intensité de la force de frottement $\vec{f}$ supposée constante et parallèle à $OA$ appliquée par le plan sur le solide entre $O$ et $A$.

**2.** Arrivé en $A$, le mobile quitte le plan incliné avec la vitesse $V'_A = 1\ \text{m/s}$.

*D'après la figure :* $O$ et $H$ sont au niveau du sol, $H$ étant à la verticale de $A$ ; le repère $(A; x, y)$ a l'axe $Ax$ horizontal et l'axe $Ay$ vertical vers le haut ; $D$ est le point de chute sur le sol.

**2.1.** Dans le repère $(A; x, y)$, établir l'équation de la trajectoire suivie par le mobile.

**2.2.** Quelle distance sépare le point $H$ du point de chute $D$ (voir figure) ?

**2.3.** Déterminer la valeur de la vitesse $V_D$ au point $D$.
""", r"""
**1.1.** Sans frottement, seul le poids travaille ; $A$ est à la hauteur $OA\sin 15^\circ \approx 0{,}259\ \text{m}$ au-dessus de $O$ :
$$V_A = \sqrt{V_0^2 - 2g\,OA\sin 15^\circ} = \sqrt{9 - 5{,}18} \approx 1{,}96\ \text{m/s}.$$

**1.2.** Théorème de l'énergie cinétique avec frottement :
$$\dfrac{1}{2}m\left(V_A'^2 - V_0^2\right) = -mg\,OA\sin 15^\circ - f \times OA,$$
$$f = \dfrac{m\left(V_0^2 - V_A'^2\right)}{2\,OA} - mg\sin 15^\circ = \dfrac{0{,}05 \times 8}{2} - 0{,}05 \times 10 \times 0{,}259 \approx 0{,}071\ \text{N}.$$

**2.1.** En $A$, $\vec{V}'_A$ fait $15^\circ$ avec l'horizontale ; seul le poids agit :
$$x = V'_A\cos 15^\circ\,t, \qquad y = -\dfrac{1}{2}gt^2 + V'_A\sin 15^\circ\,t,$$
$$y = -\dfrac{g}{2V_A'^2\cos^2 15^\circ}x^2 + x\tan 15^\circ \approx -5{,}36\,x^2 + 0{,}268\,x.$$

**2.2.** Le sol est à $y = -AH = -OA\sin 15^\circ \approx -0{,}259\ \text{m}$ :
$$-5{,}36\,x^2 + 0{,}268\,x + 0{,}259 = 0,$$
de racine positive $x_D \approx 0{,}246\ \text{m}$. Comme $H$ est à la verticale de $A$ : $HD \approx 0{,}25\ \text{m}$.

**2.3.** Entre $A$ et $D$, seul le poids travaille :
$$V_D = \sqrt{V_A'^2 + 2g\,AH} = \sqrt{1 + 20 \times 0{,}259} \approx 2{,}49\ \text{m/s}.$$
""", [MCU])

# ═══════════════════════════════ D 2023 — session complémentaire ══════════════

_add("bac-d-2023-sc-pc-ex3", r"""
**Exercice 3 (5,5 points)**

Une piste $ABCM$ est formée de deux parties $AB$ et $BM$.
- $AB$ est une partie rectiligne de longueur $AB = l$. Elle fait un angle $\alpha = 30^\circ$ avec l'horizontale $ADx$.
- $BM$ est une portion de cercle de centre $D$ et de rayon $r = 2{,}5\ \text{m}$.
- $(CD)$ est perpendiculaire à $(AD)$.
- On prendra $g = 10\ \text{m/s}^2$ et $\theta = 80^\circ$.

*D'après la figure :* $(DB)$ est perpendiculaire à $(AB)$ ; $\theta$ est l'angle entre l'horizontale $Dx$ et $(DM)$ ; $M$ est à la verticale du point $O$ de l'axe $Dx$ ; le repère $(O; \vec{i}, \vec{j})$ a $\vec{i}$ horizontal et $\vec{j}$ vertical vers le haut.

Un solide ponctuel de masse $m = 200\ \text{g}$ est propulsé du point $A$ avec une vitesse $V_A$.

**1.** *On suppose que les frottements sont négligeables sur la piste $ABCM$.*

**1.1.** Déterminer la nature du mouvement sur la partie $AB$ ; en déduire l'expression de la vitesse $V_B$ du solide en $B$. Calculer $V_A$ si $V_B = 4{,}56\ \text{m/s}$.

**1.2.** Exprimer la vitesse $V_C$ en $C$ en fonction de $g$, $V_A$ et $r$.

**1.3.** Déterminer l'expression de la vitesse $V_M$ du solide en $M$ en fonction de $g$, $V_A$, $r$ et $\theta$.

**1.4.** Déterminer l'expression de la réaction $R$ de la piste sur le solide en $M$ en fonction de $g$, $V_A$, $r$, $m$ et $\theta$. Calculer la valeur de $R$.

**2.** En réalité, sur le tronçon $ABC$ existent des forces de frottement qui équivalent à une force unique d'intensité $f$ constante. Le solide arrive en $C$ avec une vitesse $V'_C = 3\ \text{m/s}$. Déterminer l'expression de $f$ en fonction de $V_A$, $V'_C$, $g$, $r$, $m$, $l$ et $\alpha$. Calculer la valeur de $f$.

**3.** Le solide arrive en $M$ avec une vitesse $V_M = 4\ \text{m/s}$ et continue son mouvement dans le vide. Déterminer l'équation de sa trajectoire dans le repère $(O; \vec{i}, \vec{j})$ indiqué sur la figure.
""", r"""
**Géométrie.** $(DB) \perp (AB)$ : l'angle $\widehat{BDC}$ vaut $\alpha$. Donc $B$ est à la hauteur $r\cos\alpha$, et $l = AB = \dfrac{r\cos\alpha}{\sin\alpha} = r\sqrt{3} \approx 4{,}33\ \text{m}$ ; $C$ est à la hauteur $r$ et $M$ à la hauteur $r\sin\theta$.

**1.1.** Sur $AB$, deuxième loi de Newton projetée sur la piste : $a = -g\sin\alpha = -5\ \text{m/s}^2$, constante et opposée à la vitesse : mouvement **rectiligne uniformément décéléré**.
$$V_B^2 - V_A^2 = 2a\,l \iff V_B = \sqrt{V_A^2 - 2gr\cos\alpha}.$$
$$V_A = \sqrt{V_B^2 + 2gr\cos\alpha} = \sqrt{4{,}56^2 + 2 \times 10 \times 2{,}5 \times 0{,}866} \approx 8{,}0\ \text{m/s}.$$

**1.2.** Théorème de l'énergie cinétique de $A$ à $C$ (la réaction ne travaille pas, $C$ est à la hauteur $r$) :
$$V_C = \sqrt{V_A^2 - 2gr} \quad (\approx 3{,}75\ \text{m/s}).$$

**1.3.** De même, $M$ étant à la hauteur $r\sin\theta$ :
$$V_M = \sqrt{V_A^2 - 2gr\sin\theta} \quad (\approx 3{,}85\ \text{m/s}).$$

**1.4.** En $M$, le solide est sur l'extérieur de l'arc. Sur la normale orientée de $M$ vers $D$ (la composante du poids vaut $mg\sin\theta$) :
$$mg\sin\theta - R = m\dfrac{V_M^2}{r} \iff R = 3mg\sin\theta - \dfrac{m}{r}V_A^2.$$

$R = 3 \times 0{,}2 \times 10 \times 0{,}985 - \dfrac{0{,}2 \times 64}{2{,}5} \approx 0{,}79\ \text{N}$ (avec $V_A \approx 8\ \text{m/s}$).

**2.** Le trajet $ABC$ a pour longueur $l + r\alpha$ ($\alpha$ en radians, arc $BC$). Théorème de l'énergie cinétique de $A$ à $C$ :
$$\dfrac{1}{2}m\left(V_C'^2 - V_A^2\right) = -mgr - f(l + r\alpha) \iff f = \dfrac{m\left(V_A^2 - V_C'^2 - 2gr\right)}{2(l + r\alpha)}.$$

Avec $l = 4{,}33\ \text{m}$ et $r\alpha = 2{,}5 \times \dfrac{\pi}{6} \approx 1{,}31\ \text{m}$ : $f \approx \dfrac{0{,}2 \times (64 - 9 - 50)}{2 \times 5{,}64} \approx 0{,}09\ \text{N}$.

**3.** En $M$, $\vec{V}_M$ est tangente au cercle, donc perpendiculaire à $(DM)$ : elle fait l'angle $90^\circ - \theta = 10^\circ$ sous l'horizontale. Conditions initiales : $x_M = 0$, $y_M = r\sin\theta$ ; $V_x = V_M\sin\theta$, $V_y = -V_M\cos\theta$. Seul le poids agit :
$$x = V_M\sin\theta\,t, \qquad y = -\dfrac{1}{2}gt^2 - V_M\cos\theta\,t + r\sin\theta,$$
$$y = -\dfrac{g}{2V_M^2\sin^2\theta}x^2 - \dfrac{x}{\tan\theta} + r\sin\theta \approx -0{,}32\,x^2 - 0{,}18\,x + 2{,}46.$$
""", note="Correction conforme au corrigé officiel (V_A = 8 m/s, R ≈ 0,79 N, trajectoire y = −0,32x² − 0,18x + 2,46).")

# ═══════════════════════════════ D 2024 — session complémentaire ══════════════

_add("bac-d-2024-sc-pc-ex3", r"""
**Exercice 3 (5 points)**

*On donne $m = 200\ \text{kg}$ ; $\sin\alpha = 0{,}42$ ; $\cos\alpha = 0{,}9$ ; $BC = 45\ \text{m}$ ; $g = 10\ \text{m/s}^2$.*

Une piste est constituée d'une partie horizontale $AB$, d'une partie $BC$ inclinée d'un angle $\alpha$ par rapport à l'horizontale et d'un fossé de largeur $d$ (voir la figure 1).

Sur cette piste un motard cascadeur passe par le point $A$ à la date $t = 0$ avec la vitesse $V_A$ et atteint le point $B$ à $t = 5\ \text{s}$ avec la vitesse $V_B$. Le graphe représente les variations de la vitesse du centre d'inertie du motard entre $A$ et $B$.

*D'après le graphe :* $V$ varie linéairement de $8\ \text{m/s}$ à $t = 0$ à $16\ \text{m/s}$ à $t = 5\ \text{s}$. *D'après la figure :* le bord gauche du fossé est à la verticale de $C$, au niveau de $AB$, et le bord droit est au même niveau ; le repère $(C; x, y)$ a $Cx$ horizontal et $Cy$ vertical vers le haut.

**1.** En se basant sur le graphe :

**1.1.** Écrire l'équation de la droite $V = f(t)$ et déduire la valeur de l'accélération $a$ du mouvement.

**1.2.** Calculer la distance $AB$.

**2.** Sur la partie $BC$ le motard exerce une force motrice $F = 1660\ \text{N}$ et subit une force de frottement $f = 500\ \text{N}$. Ces deux forces sont constantes et parallèles à $BC$. Calculer la valeur de l'accélération sur cette partie de la piste ainsi que celle de la vitesse $V_C$.

**3.** Le motard arrive au point $C$ avec la vitesse $V_C$.

**3.1.** En considérant l'instant d'arrivée en $C$ comme instant initial, étudier le mouvement du centre d'inertie dans le repère $(C; x; y)$ et calculer l'équation de la trajectoire.

**3.2.** Calculer la valeur maximale de la largeur $d$ du fossé pour que le motard ne tombe pas dans ce fossé.
""", r"""
**1.1.** La droite passe par $(0\,;\,8)$ et $(5\,;\,16)$ : $V = 1{,}6\,t + 8$ ($V$ en m/s, $t$ en s). L'accélération est le coefficient directeur : $a = 1{,}6\ \text{m/s}^2$.

**1.2.** Mouvement rectiligne uniformément accéléré :
$$AB = \dfrac{1}{2}at^2 + V_At = 0{,}8 \times 25 + 8 \times 5 = 60\ \text{m}.$$

**2.** Deuxième loi de Newton projetée sur $BC$ (vers le haut) :
$$F - f - mg\sin\alpha = ma' \iff a' = \dfrac{1660 - 500 - 200 \times 10 \times 0{,}42}{200} = \dfrac{320}{200} = 1{,}6\ \text{m/s}^2.$$

$V_C^2 = V_B^2 + 2a'\,BC = 256 + 144 = 400$ : $V_C = 20\ \text{m/s}$.

**3.1.** En $C$, $\vec{V}_C$ fait l'angle $\alpha$ avec l'horizontale. Dans l'air (frottements négligés), seul le poids agit : $a_x = 0$ (mouvement uniforme sur $Cx$), $a_y = -g$ (mouvement uniformément varié sur $Cy$) :
$$x = V_C\cos\alpha\,t = 18\,t, \qquad y = -5t^2 + V_C\sin\alpha\,t = -5t^2 + 8{,}4\,t,$$
$$y = -\dfrac{g}{2V_C^2\cos^2\alpha}x^2 + x\tan\alpha \approx -0{,}0154\,x^2 + 0{,}467\,x.$$

**3.2.** $C$ est à la hauteur $BC\sin\alpha = 18{,}9\ \text{m}$ au-dessus de $AB$ ; le motard retombe au niveau des bords du fossé en $y = -18{,}9\ \text{m}$ :
$$-0{,}0154\,x^2 + 0{,}467\,x + 18{,}9 = 0 \implies x \approx 53\ \text{m}.$$

Le motard ne tombe pas dans le fossé si $d \le 53\ \text{m}$ : $d_{\max} \approx 53\ \text{m}$.
""", [MCU], note="Les valeurs du graphe (8 m/s à t = 0, 16 m/s à t = 5 s) et la position du fossé (bord gauche à la verticale de C, bords au niveau de AB) sont lues sur la figure ; elles donnent des valeurs exactes (a = 1,6 m/s², V_C = 20 m/s). Le texte OCR portait sin α = 0,3 et BC = 5 m : le sujet donne sin α = 0,42 et BC = 45 m.")

# ═══════════════════════════════ C 2022 — session complémentaire ══════════════

_add("bac-c-2022-sc-pc-ex3", r"""
**Exercice 3 (4 points)**

*On donne $g = 10\ \text{m/s}^2$ ; $\sin 60^\circ = 0{,}87$ ; $\cos 60^\circ = 0{,}5$ ; $\sin 52^\circ = 0{,}79$ ; $\cos 52^\circ = 0{,}6$.*

Un solide ponctuel $S$ de masse $m = 200\ \text{g}$ gravit un plan $OA$ incliné d'un angle $\alpha$ par rapport à la verticale. Il part du point $O$, origine de l'axe orienté $X'X$, avec une vitesse initiale de valeur $V_0$. Au cours de son mouvement, $S$ subit une force de frottement de valeur $f = 0{,}55\ \text{N}$. Un dispositif approprié permet de mesurer la vitesse $V$ instantanée du solide pour différentes positions $x$. La courbe représentative de $V^2 = f(x)$ est donnée par la fig. 2.

*D'après la figure :* le repère $(A; x, y)$ a l'axe $Ax$ horizontal et l'axe $Ay$ vertical vers le haut. *D'après la fig. 2 :* $V^2$ décroît linéairement de $30{,}25\ \text{m}^2/\text{s}^2$ en $x = 0$ à $4\ \text{m}^2/\text{s}^2$ en $x = 1{,}5\ \text{m}$ (point $A$).

**1.** Déterminer l'équation $V^2 = f(x)$ à partir du graphe.

**2.** En appliquant le théorème de l'énergie cinétique entre le point $O$ et un point $M$ quelconque du plan incliné, établir l'expression de $V^2$ en fonction de $x$.

**3.** En déduire les valeurs de la vitesse $V_0$ et de l'angle $\alpha$.

**4.** Donner les expressions de l'énergie cinétique $E_c$ et de l'énergie potentielle $E_p$ du système {solide-terre} en fonction de $x$ ; en prenant pour origine de l'énergie potentielle le plan horizontal passant par le point $O$. En déduire l'expression de l'énergie mécanique $E$ en fonction de $x$.

**5.** Le solide $S$ quitte le plan incliné en $A$ tel que $OA = 1{,}5\ \text{m}$.

**5.1.** Donner les caractéristiques du vecteur vitesse du solide en $A$.

**5.2.** Déterminer les équations paramétriques du mouvement du solide $S$ après avoir quitté le plan incliné dans le repère $(A; x, y)$ et en déduire l'équation de sa trajectoire.
""", r"""
**1.** Droite de coefficient directeur $\dfrac{4 - 30{,}25}{1{,}5} = -17{,}5$ et d'ordonnée à l'origine $30{,}25$ :
$$V^2 = -17{,}5\,x + 30{,}25 \quad (V \text{ en m/s}, x \text{ en m}).$$

**2.** Entre $O$ et $M$ ($OM = x$), $S$ s'élève de $x\cos\alpha$ (le plan fait $\alpha$ avec la verticale) ; la réaction normale ne travaille pas :
$$\dfrac{1}{2}mV^2 - \dfrac{1}{2}mV_0^2 = -mgx\cos\alpha - fx \iff V^2 = -2\left(g\cos\alpha + \dfrac{f}{m}\right)x + V_0^2.$$

**3.** Par identification : $V_0^2 = 30{,}25$, donc $V_0 = 5{,}5\ \text{m/s}$ ; et $2\left(10\cos\alpha + \dfrac{0{,}55}{0{,}2}\right) = 17{,}5 \iff \cos\alpha = 0{,}6$, donc $\alpha = 52^\circ$.

**4.** $E_c = \dfrac{1}{2}mV^2 = 0{,}1 \times (30{,}25 - 17{,}5\,x) = 3{,}025 - 1{,}75\,x$ (J).

$E_p = mgx\cos\alpha = 0{,}2 \times 10 \times 0{,}6\,x = 1{,}2\,x$ (J).

$E = E_c + E_p = 3{,}025 - 0{,}55\,x$ (J) : elle diminue de $f\,x$, le travail des frottements.

**5.1.** En $A$ ($x = 1{,}5\ \text{m}$) : $V_A^2 = 4$, $V_A = 2\ \text{m/s}$. Le vecteur $\vec{V}_A$ a pour origine $A$, pour direction la droite $(OA)$ (à $52^\circ$ de la verticale, soit $38^\circ$ au-dessus de l'horizontale), pour sens de $O$ vers $A$ (vers le haut) et pour valeur $2\ \text{m/s}$.

**5.2.** Composantes initiales : $V_{Ax} = V_A\sin\alpha = 1{,}58\ \text{m/s}$ et $V_{Ay} = V_A\cos\alpha = 1{,}2\ \text{m/s}$. Seul le poids agit ($a_x = 0$, $a_y = -g$) :
$$x = 1{,}58\,t, \qquad y = -5t^2 + 1{,}2\,t.$$

Trajectoire : $y = -\dfrac{g}{2V_A^2\sin^2\alpha}x^2 + \dfrac{\cos\alpha}{\sin\alpha}x \approx -2{,}0\,x^2 + 0{,}76\,x$.
""", note="Données lues sur le graphe : V² = 30,25 m²/s² en x = 0 et 4 m²/s² en x = OA = 1,5 m ; elles donnent cos α = 0,6, c'est-à-dire l'angle 52° dont le sujet fournit les lignes trigonométriques.")


# ═══════════════════════════════ D 2016 — session complémentaire ══════════════

_add("bac-d-2016-sc-pc-ex3", r"""
**Exercice 3 (5 points)**

On considère le mouvement de la Terre autour du Soleil dans le référentiel héliocentrique considéré comme galiléen. On suppose que ce mouvement se fait sur une trajectoire circulaire, de rayon $r = 1{,}5 \times 10^{11}\ \text{m}$. On néglige l'action de tout autre astre et on s'aidera du schéma suivant.

*D'après le schéma :* le vecteur unitaire $\vec{u}$, placé au centre de la Terre, est dirigé de la Terre vers le Soleil.

**1.** Donner les caractéristiques de la force subie par la Terre et la représenter.

**2.** Appliquer la R.F.D. à la Terre et montrer que son mouvement est uniforme.

**3.** En déduire l'expression du vecteur accélération de la Terre en fonction de la constante de gravitation universelle $G$, de la masse du Soleil $M_S$, du rayon $r$ de la trajectoire et du vecteur unitaire $\vec{u}$ ; le représenter sans considération d'échelle sur le schéma.

**4.** Quelle relation peut-on alors écrire entre l'accélération $a$ et la vitesse $V$ du centre d'inertie de la Terre ?

**5.** Donner l'expression de la vitesse $V$ en fonction de la constante de gravitation universelle $G$, la masse du Soleil $M_S$ et le rayon $r$ de la trajectoire. Calculer la valeur de cette vitesse.

**6.** Donner l'expression de la période de rotation $T$ de la Terre autour du Soleil en fonction de la vitesse $V$ et du rayon $r$ de sa trajectoire. Montrer alors qu'on peut écrire que $T = 2\pi r\sqrt{\dfrac{r}{GM_S}}$, puis calculer sa valeur.

On donne : $G = 6{,}67 \times 10^{-11}\ \text{S.I.}$ ; $M_S = 2 \times 10^{30}\ \text{kg}$.
""", r"""
**1.** La Terre (masse $m$) subit la force de gravitation exercée par le Soleil :
- point d'application : le centre $T$ de la Terre ;
- direction : la droite joignant les centres du Soleil et de la Terre ;
- sens : de la Terre vers le Soleil (force attractive) ;
- intensité : $F = \dfrac{GM_Sm}{r^2}$.

Vectoriellement : $\vec{F} = \dfrac{GM_Sm}{r^2}\vec{u}$ (on la représente par une flèche partant de la Terre, dirigée vers le Soleil).

**2.** R.F.D. : $\vec{F} = m\vec{a}$, donc $\vec{a} = \dfrac{\vec{F}}{m}$ est dirigée vers le centre de la trajectoire : l'accélération est **centripète**, sans composante tangentielle. Or $a_t = \dfrac{dV}{dt}$ ; donc $\dfrac{dV}{dt} = 0$ et $V$ est constante : le mouvement circulaire est **uniforme**.

**3.** $\vec{a} = \dfrac{GM_S}{r^2}\vec{u}$ : vecteur partant du centre de la Terre, dirigé vers le Soleil (même direction et même sens que $\vec{F}$).

**4.** Pour un mouvement circulaire uniforme, l'accélération est normale : $a = \dfrac{V^2}{r}$.

**5.** $\dfrac{V^2}{r} = \dfrac{GM_S}{r^2} \iff V = \sqrt{\dfrac{GM_S}{r}} = \sqrt{\dfrac{6{,}67 \times 10^{-11} \times 2 \times 10^{30}}{1{,}5 \times 10^{11}}} \approx 2{,}98 \times 10^{4}\ \text{m/s}$ (environ $30\ \text{km/s}$).

**6.** En une période, la Terre parcourt le périmètre $2\pi r$ à vitesse constante : $T = \dfrac{2\pi r}{V}$. Avec $V = \sqrt{\dfrac{GM_S}{r}}$ :
$$T = 2\pi r\sqrt{\dfrac{r}{GM_S}} = \dfrac{2\pi \times 1{,}5 \times 10^{11}}{2{,}98 \times 10^{4}} \approx 3{,}16 \times 10^{7}\ \text{s},$$
soit environ $366$ jours (cohérent avec une année).
""", [CH], chapitre=GRAV, note="Exercice classé à tort dans « Mouvements dans des champs uniformes » : il porte sur la gravitation (mouvement de la Terre autour du Soleil).")

# ═══════════════════════════════ D 2018 — session normale ═════════════════════

_add("bac-d-2018-sn-pc-ex3", r"""
**Exercice 3 (6 points)**

On donne : $G = 6{,}67 \times 10^{-11}\ \text{S.I.}$ ; la période de révolution de la Terre autour d'elle-même $T = 86\,400\ \text{s}$ ; rayon de la Terre $R = 6380\ \text{km}$.

**1.** Un satellite artificiel $S$ de masse $m$ tourne autour de la Terre sur une orbite circulaire à l'altitude $Z$.

**1.1.** Donner les caractéristiques de la force gravitationnelle $\vec{F}$ exercée par la Terre sur $S$. Exprimer l'intensité $F$ de la force $\vec{F}$ en fonction de $Z$, $m$, $G$, $R$ et $M$ (masse de la Terre).

**1.2.** Montrer que le mouvement du satellite est uniforme. Exprimer sa vitesse $V$ sur son orbite.

**1.3.** Donner l'expression de la période $T$ de révolution de $S$ autour de la Terre en fonction de $G$, $M$ et $r$ (rayon de l'orbite du satellite). Montrer que $\dfrac{T^2}{r^3}$ est une constante pour tous les satellites de la Terre.

**2.** La Lune tourne autour de la Terre sur une orbite circulaire de rayon $r = 385\,000\ \text{km}$ ; sa période est de $27{,}3$ jours. Calculer la masse de la Terre.

**3.** On considère maintenant un satellite géostationnaire.

**3.1.** Quelle est la particularité de ce satellite ?

**3.2.** Exprimer l'altitude $Z$ à laquelle évolue un tel satellite puis la calculer.
""", r"""
**1.1.** Force exercée par la Terre sur $S$ :
- point d'application : le centre d'inertie de $S$ ;
- direction : la droite joignant le centre $O$ de la Terre et $S$ ;
- sens : de $S$ vers $O$ (attractive) ;
- intensité : $F = \dfrac{GMm}{(R + Z)^2}$.

**1.2.** Dans le référentiel géocentrique (galiléen), $\vec{F} = m\vec{a}$ : l'accélération est dirigée vers le centre $O$ de la trajectoire, donc sa composante tangentielle $\dfrac{dV}{dt}$ est nulle et $V$ est constante : le mouvement est **uniforme**.

Accélération normale : $\dfrac{V^2}{R + Z} = \dfrac{GM}{(R + Z)^2} \iff V = \sqrt{\dfrac{GM}{R + Z}}$.

**1.3.** Avec $r = R + Z$ : $T = \dfrac{2\pi r}{V} = 2\pi\sqrt{\dfrac{r^3}{GM}}$, donc
$$\dfrac{T^2}{r^3} = \dfrac{4\pi^2}{GM},$$
qui ne dépend que de la masse de la Terre : c'est la même constante pour tous ses satellites (troisième loi de Kepler).

**2.** Pour la Lune : $M = \dfrac{4\pi^2r^3}{GT^2}$ avec $r = 3{,}85 \times 10^{8}\ \text{m}$ et $T = 27{,}3 \times 86\,400 \approx 2{,}36 \times 10^{6}\ \text{s}$ :
$$M = \dfrac{4\pi^2 \times (3{,}85 \times 10^{8})^3}{6{,}67 \times 10^{-11} \times (2{,}36 \times 10^{6})^2} \approx 6{,}07 \times 10^{24}\ \text{kg}.$$

**3.1.** Un satellite géostationnaire paraît **immobile** pour un observateur terrestre : il tourne dans le plan de l'équateur, dans le même sens que la Terre, avec une période égale à la période de rotation de la Terre sur elle-même ($T = 86\,400\ \text{s}$).

**3.2.** D'après 1.3 : $(R + Z)^3 = \dfrac{GMT^2}{4\pi^2}$, donc
$$Z = \sqrt[3]{\dfrac{GMT^2}{4\pi^2}} - R.$$

Avec $M \approx 6{,}07 \times 10^{24}\ \text{kg}$ : $R + Z \approx 4{,}25 \times 10^{7}\ \text{m}$, d'où $Z \approx 3{,}61 \times 10^{7}\ \text{m} \approx 36\,100\ \text{km}$.
""", [CH], chapitre=GRAV, note="Exercice classé à tort dans « Mouvements dans des champs uniformes » : il porte sur les satellites (gravitation). Question 1.1 : le sujet demande F en fonction de Z, m, G, R et M (le texte OCR avait perdu R).")

# ═══════════════════════════════ D 2020 — session complémentaire ══════════════

_add("bac-d-2020-sc-pc-ex4", r"""
**Exercice 4 (5 points)**

Pour étudier le passage d'une comète au voisinage de notre planète, un satellite est mis en orbite autour de la Terre.

Données : $G = 6{,}67 \times 10^{-11}\ \text{N·m}^2\text{·kg}^{-2}$ ; masse de la Terre $M = 6 \times 10^{24}\ \text{kg}$ ; rayon de la Terre $R = 6400\ \text{km}$.

**1. Étude du mouvement circulaire du satellite dans le référentiel géocentrique.**

Le satellite est supposé mis en orbite circulaire de rayon $r_0$. Il évolue avec une vitesse de valeur $V_0$ à l'altitude $h_0 = 400\ \text{km}$.

**1.1.** En supposant ce satellite uniquement soumis au champ gravitationnel terrestre, déterminer la nature de son mouvement.

**1.2.** Exprimer la vitesse $V_0$ en fonction de $G$, $M$, $R$ et $h_0$ et calculer sa valeur.

**1.3.** Établir l'expression de sa période $T_0$ en fonction de $R$, $h_0$, $V_0$ et la calculer.

**2. Étude énergétique.**

L'énergie potentielle de gravitation s'écrit $E_p = -\dfrac{GmM}{r}$, $r$ étant le rayon de l'orbite et $m$ la masse du satellite.

**2.1.** Exprimer l'énergie mécanique $E_{m0}$ du satellite sur l'orbite circulaire de rayon $r_0$ en fonction de $M$, $m$ et $r_0$.

**2.2.** Exprimer successivement l'énergie mécanique $E_{m0}$ et l'énergie cinétique $E_{c0}$ en fonction de l'énergie potentielle $E_{p0}$ sur cette même orbite.

**2.3.** Exprimer l'énergie $W$ fournie par les moteurs pour que le satellite passe de l'orbite de rayon $r_0$ à une orbite plus haute de rayon $r$ en fonction de $G$, $M$, $m$, $r_0$ et $r$.
""", r"""
**1.1.** Seule force : $\vec{F} = m\vec{\mathcal{G}}$, dirigée vers le centre $O$ de la Terre. D'après la R.F.D., $\vec{a} = \vec{\mathcal{G}}$ est centripète : la composante tangentielle $\dfrac{dV}{dt}$ est nulle. Le mouvement est **circulaire uniforme**.

**1.2.** $\dfrac{V_0^2}{R + h_0} = \dfrac{GM}{(R + h_0)^2} \iff V_0 = \sqrt{\dfrac{GM}{R + h_0}}$.
$$V_0 = \sqrt{\dfrac{6{,}67 \times 10^{-11} \times 6 \times 10^{24}}{6{,}8 \times 10^{6}}} \approx 7{,}67 \times 10^{3}\ \text{m/s}.$$

**1.3.** $T_0 = \dfrac{2\pi(R + h_0)}{V_0} = \dfrac{2\pi \times 6{,}8 \times 10^{6}}{7{,}67 \times 10^{3}} \approx 5{,}57 \times 10^{3}\ \text{s}$ (environ $1\ \text{h}\ 33\ \text{min}$).

**2.1.** $E_{c0} = \dfrac{1}{2}mV_0^2 = \dfrac{GMm}{2r_0}$ et $E_{p0} = -\dfrac{GMm}{r_0}$, donc
$$E_{m0} = E_{c0} + E_{p0} = -\dfrac{GMm}{2r_0}.$$

**2.2.** $E_{m0} = \dfrac{E_{p0}}{2}$ et $E_{c0} = -\dfrac{E_{p0}}{2}$.

**2.3.** L'énergie fournie par les moteurs est la variation de l'énergie mécanique :
$$W = E_m(r) - E_{m0} = -\dfrac{GMm}{2r} + \dfrac{GMm}{2r_0} = \dfrac{GMm}{2}\left(\dfrac{1}{r_0} - \dfrac{1}{r}\right) > 0 \quad (r > r_0).$$
""", [CH], chapitre=GRAV, note="Exercice classé à tort dans « Mouvements dans des champs uniformes » : il porte sur les satellites (gravitation).")

# ═══════════════════════════════ D 2023 — session normale ═════════════════════

_add("bac-d-2023-sn-pc-ex4", r"""
**Exercice 3 (4 points)**

*Les deux questions 1 et 2 de l'exercice sont indépendantes.*

**1.** Une particule $X$ de charge $q = 3{,}2 \times 10^{-19}\ \text{C}$ et de masse $m = 6{,}68 \times 10^{-27}\ \text{kg}$ pénètre entre les armatures d'un condensateur constitué de 2 plaques parallèles métalliques rectangulaires horizontales $A$ et $B$ de longueur $l = 10\ \text{cm}$, séparées par une distance $d = 6\ \text{cm}$ comme le montre la figure. Le point $O$ est équidistant des deux plaques. La particule entre au point $O$ avec une vitesse $\vec{V}_0$ formant un angle $\alpha$ avec l'axe horizontal.

*D'après la figure :* $A$ est la plaque du haut et $B$ celle du bas ; le champ $\vec{E}$ est vertical, dirigé vers le haut ; $\vec{V}_0$ est dirigée vers le bas (sous l'axe $Ox$) ; l'axe $Ox$ est horizontal, l'axe $Oy$ vertical vers le haut ; $O'$ est le point de l'axe $Ox$ situé à la sortie des plaques ($OO' = l$).

**1.1.** Préciser les signes des armatures et de la tension $U_{BA}$.

**1.2.** Établir l'équation cartésienne de la trajectoire de la particule.

**1.3.** Déterminer la valeur de l'angle $\alpha$ pour que la particule passe par le point $O'$.

**1.4.** Déterminer les coordonnées du point le plus bas de la trajectoire.

Données : $E = 8350\ \text{V/m}$ ; $V_0 = 2 \times 10^{5}\ \text{m/s}$.

**2.** La désintégration du nucléide $^{232}_{92}\text{U}$ donne la particule $X$ précédente avec le nucléide $^{228}_{90}\text{Th}$.

**2.1.** Écrire l'équation de la réaction de désintégration, préciser le type de radioactivité et la nature de la particule $X$.

**2.2.** Calculer, en MeV, l'énergie émise lors de cette désintégration.

**2.3.** Calculer la valeur de la constante de désintégration $\lambda$ de l'uranium 232 si sa période est $69{,}8$ ans.

Données : $m_U = 232{,}0371548\ \text{u}$ ; $m_{Th} = 228{,}0287411\ \text{u}$ ; $m_X = 4{,}0026\ \text{u}$ ; $1\ \text{u} = 931{,}5\ \text{MeV}/c^2$.
""", r"""
**1.1.** La particule est positive ($q > 0$) et $\vec{E}$ est dirigé vers le haut, de $B$ vers $A$. Le champ va de l'armature positive vers l'armature négative : $B$ est **positive**, $A$ est **négative**, et $U_{BA} = V_B - V_A > 0$ (avec $U_{BA} = E\,d = 8350 \times 0{,}06 = 501\ \text{V}$).

**1.2.** Le poids est négligeable devant la force électrique ($mg \approx 6{,}5 \times 10^{-26}\ \text{N}$, $qE \approx 2{,}7 \times 10^{-15}\ \text{N}$). R.F.D. : $\vec{a} = \dfrac{q\vec{E}}{m}$, soit $a_x = 0$ et $a_y = \dfrac{qE}{m} = 4 \times 10^{11}\ \text{m/s}^2$.

Conditions initiales en $O$ : $V_{0x} = V_0\cos\alpha$, $V_{0y} = -V_0\sin\alpha$. Donc
$$x = V_0\cos\alpha\,t, \qquad y = \dfrac{qE}{2m}t^2 - V_0\sin\alpha\,t,$$
$$y = \dfrac{qE}{2mV_0^2\cos^2\alpha}x^2 - x\tan\alpha.$$

**1.3.** $O'(l\,;\,0)$ est sur la trajectoire :
$$\dfrac{qEl}{2mV_0^2\cos^2\alpha} = \tan\alpha \iff \sin 2\alpha = \dfrac{qEl}{mV_0^2} = \dfrac{4 \times 10^{11} \times 0{,}1}{4 \times 10^{10}} = 1,$$
donc $2\alpha = 90^\circ$ : $\alpha = 45^\circ$.

**1.4.** Avec $\alpha = 45^\circ$ : $y = 10x^2 - x$ ($x$, $y$ en m), car $\dfrac{qE}{2mV_0^2\cos^2\alpha} = \dfrac{4 \times 10^{11}}{2 \times 4 \times 10^{10} \times 0{,}5} = 10\ \text{m}^{-1}$.

Au point le plus bas, $\dfrac{dy}{dx} = 20x - 1 = 0$ : $x = 0{,}05\ \text{m}$ et $y = 0{,}025 - 0{,}05 = -0{,}025\ \text{m}$.

Point le plus bas : $(5\ \text{cm}\,;\,-2{,}5\ \text{cm})$. Comme $2{,}5\ \text{cm} < \dfrac{d}{2} = 3\ \text{cm}$, la particule ne touche pas la plaque $B$.

**2.1.** Conservation du nombre de masse et du nombre de charge : $232 = 228 + A$ et $92 = 90 + Z$, donc $A = 4$, $Z = 2$ :
$$^{232}_{92}\text{U} \longrightarrow\ ^{228}_{90}\text{Th} +\ ^{4}_{2}\text{He}.$$

C'est une radioactivité **$\alpha$** ; la particule $X$ est un noyau d'hélium $^{4}_{2}\text{He}$ (particule $\alpha$), ce qui est cohérent avec $q = 2e$ et $m \approx 4\ \text{u}$.

**2.2.** $\Delta m = m_U - m_{Th} - m_X = 232{,}0371548 - 228{,}0287411 - 4{,}0026 = 0{,}0058137\ \text{u}$.
$$E = \Delta m\,c^2 = 0{,}0058137 \times 931{,}5 \approx 5{,}42\ \text{MeV}.$$

**2.3.** $\lambda = \dfrac{\ln 2}{T} = \dfrac{0{,}693}{69{,}8} \approx 9{,}93 \times 10^{-3}\ \text{an}^{-1}$, soit $\lambda = \dfrac{0{,}693}{69{,}8 \times 365{,}25 \times 86\,400} \approx 3{,}15 \times 10^{-10}\ \text{s}^{-1}$.
""", [NUC], chapitre=MCU, note="Dans la base cet exercice porte le numéro 4 (le QCM compte comme exercice 1) ; sur le sujet c'est l'« Exercice 3 ». Les orientations (E vers le haut, V0 sous l'axe) sont lues sur la figure.")

# ═══════════════════════════════ D 2024 — session normale ═════════════════════

_add("bac-d-2024-sn-pc-ex5", r"""
**Exercice 4 (4 points)**

*Les questions 1 et 2 de l'exercice sont indépendantes. On donne la constante de gravitation $G = 6{,}67 \times 10^{-11}\ \text{S.I.}$*

**1.** La station spatiale internationale connue sous le nom d'ISS tourne autour de la Terre de masse $M = 6 \times 10^{24}\ \text{kg}$ et de rayon $R = 6400\ \text{km}$ d'un mouvement supposé circulaire uniforme à une altitude $h = 400\ \text{km}$. Cette station est habitée par des astronautes qui restent dans l'espace de longues durées pendant lesquelles ils procèdent à des expériences scientifiques.

**1.1.** Donner l'expression de la force $F$ qu'exerce la Terre sur la station en fonction de $G$, $R$, $m$, $M$ et $h$.

**1.2.** Exprimer la vitesse $V$ de la station en fonction de $m$, $F$, $R$ et $h$. Calculer sa valeur.

**1.3.** Exprimer la période $T$ de la station en fonction de $V$, $R$ et $h$. Calculer la valeur de $T$ et en déduire le nombre de tours effectués par la station en une journée.

**1.4.** L'énergie potentielle de gravitation du système {ISS-Terre} s'écrit $E_p = -\dfrac{mGM}{R + h}$. Donner l'expression de l'énergie mécanique du système {ISS-Terre} en fonction de $M$, $G$, $m$, $R$ et $h$.

**2.** Les astronautes qui habitent la station subissent à leur retour sur terre plusieurs examens médicaux. L'un de ces examens consiste à injecter à l'astronaute un échantillon d'une substance radioactive de masse $m_0 = 0{,}8\ \text{g}$ contenant l'isotope $^{131}_{53}\text{I}$ de l'iode, émetteur du rayonnement $\beta^-$ de demi-vie $t_{1/2} = 8$ jours.

**2.1.** Déterminer la composition du nucléide $^{131}_{53}\text{I}$.

**2.2.** Écrire l'équation de désintégration de ce nucléide. On donne : $_{51}\text{Sb}$, $_{52}\text{Te}$, $_{54}\text{Xe}$, $_{55}\text{Cs}$.

**2.3.** Calculer le nombre $N_0$ de noyaux dans l'échantillon radioactif initial si la masse d'un nucléide $^{131}_{53}\text{I}$ est $2{,}176 \times 10^{-25}\ \text{kg}$, et en déduire son activité initiale $A_0$.

**2.4.** Après une durée $t_1$, l'activité de l'échantillon se réduit à $20\,\%$ de son activité initiale $A_0$. Montrer que $t_1 = \dfrac{t_{1/2}}{\ln 2} \times \ln\dfrac{A_0}{A(t_1)}$, avec $A(t_1)$ l'activité à l'instant $t_1$. Calculer $t_1$.
""", r"""
**1.1.** $F = \dfrac{GMm}{(R + h)^2}$ ($m$ : masse de la station).

**1.2.** Mouvement circulaire uniforme : la R.F.D. donne $F = m\dfrac{V^2}{R + h}$, donc
$$V = \sqrt{\dfrac{F(R + h)}{m}} = \sqrt{\dfrac{GM}{R + h}} = \sqrt{\dfrac{6{,}67 \times 10^{-11} \times 6 \times 10^{24}}{6{,}8 \times 10^{6}}} \approx 7{,}67 \times 10^{3}\ \text{m/s}.$$

**1.3.** $T = \dfrac{2\pi(R + h)}{V} = \dfrac{2\pi \times 6{,}8 \times 10^{6}}{7{,}67 \times 10^{3}} \approx 5{,}57 \times 10^{3}\ \text{s}$.

En une journée : $\dfrac{86\,400}{5{,}57 \times 10^{3}} \approx 15{,}5$ : la station effectue environ $15{,}5$ tours, soit $15$ tours complets.

**1.4.** $E_c = \dfrac{1}{2}mV^2 = \dfrac{GMm}{2(R + h)}$, donc
$$E_m = E_c + E_p = -\dfrac{GMm}{2(R + h)}.$$

**2.1.** $^{131}_{53}\text{I}$ : $Z = 53$ protons et $A - Z = 131 - 53 = 78$ neutrons ($131$ nucléons).

**2.2.** Désintégration $\beta^-$ : émission d'un électron $^{0}_{-1}e$ (et d'un antineutrino). Le noyau fils a $Z = 54$ : c'est le xénon.
$$^{131}_{53}\text{I} \longrightarrow\ ^{131}_{54}\text{Xe} +\ ^{0}_{-1}e\ (+\ \bar{\nu}).$$

**2.3.** $N_0 = \dfrac{m_0}{m(\text{I})} = \dfrac{0{,}8 \times 10^{-3}}{2{,}176 \times 10^{-25}} \approx 3{,}68 \times 10^{21}$ noyaux.

$\lambda = \dfrac{\ln 2}{t_{1/2}} = \dfrac{0{,}693}{8 \times 86\,400} \approx 1{,}00 \times 10^{-6}\ \text{s}^{-1}$, donc $A_0 = \lambda N_0 \approx 3{,}69 \times 10^{15}\ \text{Bq}$.

**2.4.** $A(t) = A_0e^{-\lambda t}$, donc $\ln\dfrac{A_0}{A(t_1)} = \lambda t_1 = \dfrac{\ln 2}{t_{1/2}}t_1$, d'où $t_1 = \dfrac{t_{1/2}}{\ln 2} \times \ln\dfrac{A_0}{A(t_1)}$.

Avec $\dfrac{A_0}{A(t_1)} = \dfrac{1}{0{,}2} = 5$ : $t_1 = \dfrac{8 \times \ln 5}{\ln 2} \approx 18{,}6$ jours.
""", [CH, NUC], chapitre=GRAV, note="Exercice classé à tort dans « Mouvements dans des champs uniformes » : il porte sur la gravitation (ISS) et la radioactivité. Dans la base il porte le numéro 5 ; sur le sujet c'est l'« Exercice 4 ».")

# ═══════════════════════════════ C 2024 — session normale ═════════════════════

_add("bac-c-2024-sn-pc-ex5", r"""
**Exercice 4 (3 points)**

Un solide $S$ ponctuel de masse $m = 200\ \text{g}$ glisse sur un plan $AB$ incliné d'un angle $\alpha = 60^\circ$ par rapport à la verticale suivant l'axe $X'X$.

Le solide a été photographié par une caméra Webcam à différents instants. Par une analyse convenable de la vidéo on a obtenu les résultats du tableau suivant :

| $t\ (\text{s})$ | $0$ | $0{,}2$ | $0{,}4$ | $0{,}6$ | $0{,}8$ | $1$ |
|---|---|---|---|---|---|---|
| $V\ (\text{m/s})$ | $V_0$ | $2{,}4$ | $2{,}8$ | $3{,}2$ | $3{,}6$ | $4$ |

*D'après la figure :* $S$ descend le plan de $A$ vers $B$ ; $B$ est à la verticale d'un point $C$ du sol, à la hauteur $h$ ; le repère $(B; \vec{i}, \vec{j})$ a $\vec{i}$ horizontal, dirigé du côté où le solide se déplace, et $\vec{j}$ vertical vers le haut ; $D$ est sur le sol.

**1.** Représenter le graphe de la fonction $V = f(t)$.

**2.** À partir du graphe, déterminer la nature du mouvement du solide et en déduire les valeurs de l'accélération expérimentale $a$ du mouvement et de la vitesse initiale $V_0$.

**3.** En négligeant les frottements, calculer la valeur $a_0$ de l'accélération théorique. Comparer $a$ et $a_0$ et trouver l'intensité de la force de frottement si elle existe.

**4.** Le solide arrive en $B$ à $t = 1\ \text{s}$. Après $B$, situé sur la verticale d'un point $C$ à une hauteur $h = 2\ \text{m}$, le mobile effectue un mouvement aérien pour tomber en un point $D$ du sol (voir la figure).

**4.1.** Trouver dans le repère $(B, \vec{i}, \vec{j})$ l'équation de la trajectoire en fonction de $\alpha$, $g$ et $V_B$. *On choisira de nouveau pour instant initial l'instant où commence le mouvement à partir de $B$ et on négligera la résistance de l'air.*

**4.2.** Déterminer les coordonnées du point de chute $D$ dans le repère $(B, \vec{i}, \vec{j})$.

*On prendra $g = 10\ \text{m/s}^2$.*
""", r"""
**1.** Les points $(0{,}2\,;\,2{,}4)$, $(0{,}4\,;\,2{,}8)$, …, $(1\,;\,4)$ sont alignés : le graphe $V = f(t)$ est une **droite**.

**2.** $V$ est une fonction affine du temps et le mouvement est rectiligne : mouvement **rectiligne uniformément accéléré**. L'accélération est le coefficient directeur :
$$a = \dfrac{4 - 2{,}4}{1 - 0{,}2} = 2\ \text{m/s}^2.$$

L'ordonnée à l'origine donne $V_0$ : $V = 2t + V_0$ et $2{,}4 = 2 \times 0{,}2 + V_0$, donc $V_0 = 2\ \text{m/s}$.

**3.** Sans frottement, la R.F.D. projetée sur la ligne de pente (la réaction est perpendiculaire au plan) donne, le plan faisant $\alpha = 60^\circ$ avec la verticale :
$$a_0 = g\cos\alpha = 10 \times 0{,}5 = 5\ \text{m/s}^2.$$

$a = 2\ \text{m/s}^2 < a_0$ : il existe une force de frottement $\vec{f}$, opposée au mouvement. R.F.D. : $mg\cos\alpha - f = ma$, donc
$$f = m(a_0 - a) = 0{,}2 \times (5 - 2) = 0{,}6\ \text{N}.$$

**4.1.** En $B$ ($t = 1\ \text{s}$), $V_B = 4\ \text{m/s}$, dirigée suivant la pente vers le bas : elle fait l'angle $\alpha$ avec la verticale. Composantes : $V_{Bx} = V_B\sin\alpha$, $V_{By} = -V_B\cos\alpha$.

Dans l'air, seul le poids agit : $a_x = 0$, $a_y = -g$. Donc
$$x = V_B\sin\alpha\,t, \qquad y = -\dfrac{1}{2}gt^2 - V_B\cos\alpha\,t,$$
$$y = -\dfrac{g}{2V_B^2\sin^2\alpha}x^2 - \dfrac{x}{\tan\alpha}.$$

Numériquement : $y = -\dfrac{5}{12}x^2 - \dfrac{\sqrt{3}}{3}x \approx -0{,}417\,x^2 - 0{,}577\,x$.

**4.2.** Le sol est à $y_D = -h = -2\ \text{m}$ :
$$\dfrac{5}{12}x^2 + \dfrac{\sqrt{3}}{3}x - 2 = 0,$$
dont la racine positive est $x_D \approx 1{,}61\ \text{m}$. Donc $D(1{,}61\ \text{m}\,;\,-2\ \text{m})$.
""", [MCU], note="Le tableau du sujet porte « V₀ » (inconnue) à t = 0, et non 2 m/s comme dans le texte OCR : V₀ = 2 m/s se déduit du graphe (question 2). Dans la base l'exercice porte le numéro 5 ; sur le sujet c'est l'« Exercice 4 ».")


# ─────────────────────────────────────────────────────────────────────────────
# Contrôles numériques, rejoués par scripts/check_content.py.
CHECKS: dict[str, list[str]] = {
    "bac-d-2015-sc-pc-ex3": [
        "close(1/Rational(5, 1000), 200)",
        "close(Rational(1, 2)*200*Rational(5, 100)**2, Rational(1, 4))",
        "close(sqrt(2*(Rational(1, 4) - Rational(25, 1000)*10*Rational(5, 100))/Rational(25, 1000)), sqrt(19))",
        "close(Rational(1, 4)/(Rational(25, 1000)*10), 1)",
        "abs(N(2*pi*sqrt(Rational(1, 10)/200)) - 0.14) < 0.005 and abs(N(sqrt(2000)/(2*pi)) - 7.1) < 0.05",
    ],
    "bac-d-2016-sn-pc-ex4": [
        "close(sqrt(2*10*40*cos(pi/3)), 20) and close(80*400/(2*20), 800)",
        "close(sqrt(10**2 + 2*10*Rational(22, 10)), 12)",
        "close(sqrt(2*12**2*5/10), 12)",
    ],
    "bac-d-2017-sn-pc-ex3": [
        "close(Rational(1, 2)*20*Rational(2, 100)**2, Rational(4, 1000))",
        "close(Rational(2, 100)*2*pi/Rational(5, 100), 8*pi/10)",
        "abs(N(sqrt((8*pi/10)**2 - 4*10*Rational(1, 10))) - 1.52) < 0.005",
        "abs(N(20/(40*pi)**2) - 1.27e-3) < 1e-5",
    ],
    "bac-d-2018-sc-pc-ex3": [
        "close(Rational(1, 10)*(4 + 10*Rational(1, 2))/Rational(8, 10), Rational(9, 8))",
        "close(sqrt(16 - 2*5*Rational(7, 10)), 3) and close(sqrt(9 + 2*10*Rational(135, 100)), 6)",
        "close(10/(2*9*cos(pi/6)**2), Rational(20, 27))",
        "abs(N(max(solve(-Rational(20, 27)*x**2 + sqrt(3)/3*x + Rational(135, 100), x))) - 1.79) < 0.005",
    ],
    "bac-d-2019-sn-pc-ex4": [
        "close(sqrt(Rational(4, 10000) + (sqrt(3)/5/10)**2), Rational(4, 100))",
        "close(Rational(4, 100)*cos(10*0 - pi/3), Rational(2, 100)) and N(-Rational(4, 100)*10*sin(-pi/3)) > 0 and close(-Rational(4, 100)*10*sin(-pi/3), sqrt(3)/5)",
        "close(Rational(1, 2)*50*Rational(4, 10000) + Rational(1, 2)*Rational(1, 2)*Rational(3, 25), Rational(4, 100)) and close(sqrt(2*Rational(4, 100)/Rational(1, 2)), Rational(4, 10))",
        "close(sqrt(Rational(5, 100)/(10/(2*Rational(16, 100)))), Rational(4, 100)) and close(sqrt(Rational(16, 100) + 1), sqrt(Rational(116, 100)))",
        "abs(N(atan(Rational(4, 10))*180/pi) - 21.8) < 0.05",
    ],
    "bac-d-2020-sc-pc-ex3": [
        "close(Rational(1, 2)*10*Rational(4, 100)**2, Rational(8, 1000)) and close(Rational(4, 100)*10, Rational(4, 10))",
        "close(10/(2*Rational(16, 100)), Rational(3125, 100)) and abs(N(sqrt(2/Rational(3125, 100))) - 0.25) < 0.005",
        "abs(N(sqrt(Rational(16, 100) + 40)) - 6.34) < 0.005",
    ],
    "bac-d-2020-sn-pc-ex3": [
        "close(Rational(125, 100)/sin(pi/6), Rational(5, 2)) and close(sqrt(2*5*Rational(5, 2)), 5)",
        "close(10/(2*25*cos(pi/6)**2), Rational(4, 15))",
        "abs(N(25*sin(pi/3)/10) - 2.17) < 0.005 and close(2*Rational(5, 2)*sin(pi/6)*sin(pi/3), 25*sin(pi/3)/10)",
        "close(25*sin(pi/6)**2/20, Rational(3125, 10000))",
    ],
    "bac-d-2021-sc-pc-ex3": [
        "abs(N(10*cos(pi/6)) - 8.66) < 0.005 and abs(N(60*10*cos(pi/6)) - 519.6) < 0.05",
        "all(same(-10*x**2/(2*2*10*hh*cos(pi/3)**2) + x*tan(pi/3), -x**2/hh + sqrt(3)*x) for hh in (1, 3, Rational(56, 10)))",
        "close(2*sin(pi/3)*cos(pi/3), sqrt(3)/2) and close(sin(pi/3)**2, Rational(3, 4))",
        "abs(N(100/(10*sqrt(3) + Rational(1, 2))) - 5.61) < 0.005",
    ],
    "bac-d-2021-sn-pc-ex3": [
        "close(Rational(1, 10)*10/Rational(1, 10), 10) and close(Rational(4, 10)/10, Rational(4, 100))",
        "close(Rational(1, 2)*10*Rational(4, 100)**2, Rational(8, 1000))",
    ],
    "bac-d-2022-sc-pc-ex3": [
        "abs(N(sqrt(9 - 20*sin(pi/12))) - 1.96) < 0.005",
        "abs(N(Rational(5, 100)*8/2 - Rational(5, 100)*10*sin(pi/12)) - 0.071) < 0.0005",
        "abs(N(10/(2*cos(pi/12)**2)) - 5.36) < 0.005 and abs(N(tan(pi/12)) - 0.268) < 0.0005",
        "abs(N(max(solve(-10/(2*cos(pi/12)**2)*x**2 + tan(pi/12)*x + sin(pi/12), x))) - 0.246) < 0.0005",
        "abs(N(sqrt(1 + 20*sin(pi/12))) - 2.49) < 0.005",
    ],
    "bac-d-2023-sc-pc-ex3": [
        "abs(N(sqrt(Rational(456, 100)**2 + 2*10*Rational(5, 2)*cos(pi/6))) - 8.0) < 0.01",
        "abs(N(sqrt(Rational(456, 100)**2 + 50*cos(pi/6) - 50)) - 3.75) < 0.005 and abs(N(sqrt(Rational(456, 100)**2 + 50*cos(pi/6) - 50*sin(4*pi/9))) - 3.85) < 0.005",
        "abs(N(3*Rational(2, 10)*10*sin(4*pi/9) - Rational(2, 10)*64/Rational(5, 2)) - 0.79) < 0.005",
        "abs(N(Rational(2, 10)*(64 - 9 - 50)/(2*(Rational(5, 2)*sqrt(3) + Rational(5, 2)*pi/6))) - 0.09) < 0.005",
        "abs(N(10/(2*16*sin(4*pi/9)**2)) - 0.32) < 0.005 and abs(N(1/tan(4*pi/9)) - 0.18) < 0.005 and abs(N(Rational(5, 2)*sin(4*pi/9)) - 2.46) < 0.005",
    ],
    "bac-d-2024-sc-pc-ex3": [
        "close(Rational(8, 10)*25 + 8*5, 60) and close(8 + Rational(16, 10)*5, 16)",
        "close((1660 - 500 - 200*10*Rational(42, 100))/200, Rational(16, 10)) and close(sqrt(256 + 2*Rational(16, 10)*45), 20)",
        "close(10/(2*400*Rational(81, 100)), Rational(5, 324)) and close(20*Rational(42, 100), Rational(84, 10))",
        "abs(N(max(solve(-Rational(5, 324)*x**2 + Rational(42, 90)*x + Rational(189, 10), x))) - 53.2) < 0.1",
    ],
    "bac-c-2022-sc-pc-ex3": [
        "close((4 - Rational(3025, 100))/Rational(3, 2), -Rational(35, 2))",
        "close(2*(10*Rational(6, 10) + Rational(55, 100)/Rational(2, 10)), Rational(35, 2))",
        "close(Rational(1, 10)*Rational(3025, 100), Rational(3025, 1000)) and close(Rational(2, 10)*10*Rational(6, 10), Rational(12, 10))",
        "close(sqrt(Rational(3025, 100) - Rational(35, 2)*Rational(3, 2)), 2)",
        "abs(N(10/(2*4*Rational(79, 100)**2)) - 2.0) < 0.005 and abs(N(Rational(6, 10)/Rational(79, 100)) - 0.76) < 0.005",
    ],
    "bac-d-2016-sc-pc-ex3": [
        "abs(N(sqrt(Rational(667, 100)*10**-11*2*10**30/(Rational(15, 10)*10**11))) - 2.98e4) < 50",
        "abs(N(2*pi*Rational(15, 10)*10**11*sqrt(Rational(15, 10)*10**11/(Rational(667, 100)*10**-11*2*10**30))) - 3.16e7) < 5e4",
        "abs(N(2*pi*Rational(15, 10)*10**11*sqrt(Rational(15, 10)*10**11/(Rational(667, 100)*10**-11*2*10**30))/86400) - 366) < 1",
    ],
    "bac-d-2018-sn-pc-ex3": [
        "abs(N(4*pi**2*(Rational(385, 1000)*10**9)**3/(Rational(667, 100)*10**-11*(Rational(273, 10)*86400)**2)) - 6.07e24) < 0.01e24",
        "abs(N((Rational(667, 100)*10**-11*Rational(607, 100)*10**24*86400**2/(4*pi**2))**Rational(1, 3)) - 4.25e7) < 0.01e7",
        "abs(N((Rational(667, 100)*10**-11*Rational(607, 100)*10**24*86400**2/(4*pi**2))**Rational(1, 3) - Rational(638, 100)*10**6) - 3.61e7) < 0.01e7",
    ],
    "bac-d-2020-sc-pc-ex4": [
        "abs(N(sqrt(Rational(667, 100)*10**-11*6*10**24/(Rational(68, 10)*10**6))) - 7.67e3) < 5",
        "abs(N(2*pi*Rational(68, 10)*10**6/sqrt(Rational(667, 100)*10**-11*6*10**24/(Rational(68, 10)*10**6))) - 5.57e3) < 5",
    ],
    "bac-d-2023-sn-pc-ex4": [
        "close(Rational(32, 10)*10**-19*8350/(Rational(668, 100)*10**-27), 4*10**11)",
        "close(4*10**11*Rational(1, 10)/(2*10**5)**2, 1) and close(4*10**11/(2*(2*10**5)**2*cos(pi/4)**2), 10)",
        "close((10*x**2 - x).subs(x, Rational(1, 20)), -Rational(1, 40)) and close(8350*Rational(6, 100), 501)",
        "abs(N((Rational(2320371548, 10**7) - Rational(2280287411, 10**7) - Rational(40026, 10**4))*Rational(9315, 10)) - 5.42) < 0.005",
        "abs(N(log(2)/Rational(698, 10)) - 9.93e-3) < 5e-6 and abs(N(log(2)/(Rational(698, 10)*Rational(36525, 100)*86400)) - 3.15e-10) < 0.005e-10",
    ],
    "bac-d-2024-sn-pc-ex5": [
        "abs(N(86400/(2*pi*Rational(68, 10)*10**6/sqrt(Rational(667, 100)*10**-11*6*10**24/(Rational(68, 10)*10**6)))) - 15.5) < 0.05",
        "abs(N(Rational(8, 10)*10**-3/(Rational(2176, 1000)*10**-25)) - 3.68e21) < 0.005e21",
        "abs(N(log(2)/(8*86400)*Rational(8, 10)*10**-3/(Rational(2176, 1000)*10**-25)) - 3.69e15) < 0.005e15",
        "abs(N(8*log(5)/log(2)) - 18.6) < 0.05",
    ],
    "bac-c-2024-sn-pc-ex5": [
        "close((4 - Rational(24, 10))/(1 - Rational(2, 10)), 2) and close(Rational(24, 10) - 2*Rational(2, 10), 2)",
        "close(10*cos(pi/3), 5) and close(Rational(2, 10)*(5 - 2), Rational(6, 10))",
        "close(10/(2*16*sin(pi/3)**2), Rational(5, 12)) and close(1/tan(pi/3), sqrt(3)/3)",
        "abs(N(max(solve(Rational(5, 12)*x**2 + sqrt(3)/3*x - 2, x))) - 1.61) < 0.005",
    ],
}
