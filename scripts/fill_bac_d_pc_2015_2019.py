"""Remplit 36 énoncés Bac D · PC · 2015-2019 (SN + SC).

Source : extraction Gemini fournie par l'admin, qualité à valider.
NE TOUCHE PAS `validated_by_admin`. Backup auto avant écriture.

Permet la comparaison côte-à-côte avec les Bac C correspondants (qui
contiennent la version "livres" déjà validée). L'admin peut ainsi
fusionner les deux versions au cas par cas.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"


EXOS: dict[tuple[str, str, int, str, int], str] = {

    # ═══════════════ 2015 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2015, "sc", 1): r"""Exercice 1 (5pt)
Soit un composé organique A de formule brute $C_nH_{2n}O_2$.
1.1 Quelles sont les fonctions chimiques possibles de A ? Donner dans chaque cas la formule semi-développée générale.
1.2 Le composé A renferme 36,36 % en masse d'élément oxygène, déterminer sa formule brute.
2. La réaction de A avec un composé C de formule brute $C_3H_8O$ donne un composé F et de l'eau.
2.1 Préciser les fonctions chimiques de A, C et F.
2.2 De quel type de réaction s'agit-il ? Cette réaction est-elle totale ?
3. Sachant que A est ramifié et que l'oxydation ménagée de C donne $C'$ qui rosit le réactif de Schiff, écrire l'équation de la réaction de A avec C. Préciser les noms de A, C, F et $C'$.
4. On verse une solution de soude (1 mol/L) sur une solution de A renfermant 2,2 g de A dissous.
4.1 Écrire l'équation de la réaction.
4.2 Quel doit être le volume de la solution de soude versé à l'équivalence ?""",

    ("D", "pc", 2015, "sc", 2): r"""Exercice 2 (4pt)
1. Le pH d'une solution d'ammoniac $NH_3$ ($10^{-2}$ mol/L) est 10,6.
1.1 Écrire l'équation avec l'eau et calculer les concentrations des espèces chimiques présentes.
1.2 En déduire le pKa du couple mis en jeu.
2. Le pH d'une solution d'éthylamine $C_2H_5NH_2$ ($10^{-2}$ mol/L) est 11,4.
2.1 Répondre aux mêmes questions que la question 1.
2.2 Quelle est la base la plus forte entre l'ammoniac et l'éthylamine ?
3. On prélève 20 cm³ d'éthylamine ; on y verse de l'acide chlorhydrique (obtenu par dissolution de 1,83 g de gaz HCl dans 1 L d'eau). Quel sera le volume d'acide versé à l'équivalence ? Rappeler la définition de l'équivalence.""",

    ("D", "pc", 2015, "sc", 3): r"""Exercice 3 (5pt)
Un canon à ressort vertical lance des projectiles ($m=25$ g). Raideur K : 1 N provoque 5 mm de raccourcissement. Comprimé de $l_0/2$ ($l_0=10$ cm).
1.1 Calculer l'énergie potentielle élastique au maximum de compression.
1.2 Déterminer la vitesse V à la sortie du canon.
1.3 Déterminer l'altitude maximale h atteinte.
2. Au ressort précédent on suspend 100 g ; tiré de 4 cm vers le bas puis abandonné à $t=0$.
2.1 Trouver l'équation différentielle du mouvement.
2.2 Déterminer l'équation horaire.
2.3 Calculer la période et la fréquence.""",

    ("D", "pc", 2015, "sc", 4): r"""Exercice 4 (6pt)
Corde élastique SC ($L=1$ m). Extrémité S reliée à une lame vibrant à fréquence N ($a=3$ mm).
1.1 Rôle de la pelote de coton en C.
1.2 Pourquoi l'onde est-elle transversale ?
2.1 Déterminer graphiquement la longueur d'onde $\lambda$ (à $t=0{,}06$ s).
2.2 Montrer que la célérité est $V=10$ m/s. En déduire N.
3.1 Établir l'équation horaire d'un point M ($SM=x$).
3.2 Déterminer la phase $\varphi_s$.
3.3 Déterminer l'instant $t_1$ où l'onde atteint C.
3.4 Déterminer le nombre et positions des points vibrant en quadrature retard de phase par rapport à S à $t_1$.""",

    # ═══════════════ 2015 SESSION NORMALE ═══════════════
    ("D", "pc", 2015, "sn", 1): r"""Exercice 1 (5pt)
Acide propanoïque ($C=10^{-2}$ mol/L, $pH=3{,}45$).
1.1 Calculer les molarités et le pKa.
1.2 Calculer le coefficient d'ionisation $\alpha$. Conclure.
1.3 On dilue 10 mL à 1 L ($pH=4{,}45$). Calculer le nouveau $\alpha'$.
1.4 Pour $C''=10^{-6}$ mol/L et $pH=6$, calculer $\alpha''$. Comportement de l'acide très dilué ?
2. Transformation de l'acide A en chlorure d'acyle B ($SOCl_2$), puis action sur amine E ($C_2H_7N$) pour donner un amide C.
2.1 Équation pour B et son nom.
2.2 Formules et classes des amines $C_2H_7N$.
2.3 E est une amine secondaire : donner la formule et nom de l'amide C.
3. A obtenu par oxydation ménagée en deux étapes de D. Nom de D et équation de la 2ème étape avec $Cr_2O_7^{2-}$.""",

    ("D", "pc", 2015, "sn", 2): r"""Exercice 2 (4pt)
Mélange de 0,5 mol de pentan-1-ol et 0,5 mol d'acide méthanoïque.
1.1 Équation et nom de l'ester.
1.2 Dosage de l'acide restant ($V_0=2$ cm³) par la soude ($C_B=1$ mol/L).
1.2.1 But du refroidissement ?
1.2.3 Expression de $n_A$ en fonction de $V_B$ et $C_B$.
1.3 Calculer $n_0$ à $t=0$. Expression de $n_E$ (ester formé).
2. Définir et calculer la vitesse instantanée de formation de l'ester à $t=30$ min et la vitesse moyenne entre 10 et 30 min.""",

    ("D", "pc", 2015, "sn", 3): r"""Exercice 3 (5pt)
Particule ($m$, $q>0$) lancée à $\vec{v}_0$ dans un champ magnétique uniforme $\vec{B}$ perpendiculaire.
1.2 Montrer que le mouvement est uniforme et circulaire.
1.3 Expression de la période T et fréquence N. Calculer T ($B=1$ T, $q/m=10^8$ C/Kg).
2. Ajout d'un champ électrique $\vec{E}$.
2.1 Direction de $\vec{E}$ pour un mouvement rectiligne uniforme ?
2.2 Calculer E ($V_0=5.10^7$ m/s).
2.3 On supprime B : équation de la trajectoire dans E, et déviation angulaire $\alpha$.""",

    ("D", "pc", 2015, "sn", 4): r"""Exercice 4 (6pt)
1. Solénoïde ($l=0{,}5$ m, $N=5000$) parcouru par $I=8.10^{-2}$ A. Caractéristiques de $\vec{B}$.
2. Bobine interne $S'$ ($N'=400$, $d'=4$ cm). Calculer le flux magnétique.
3. Courant i variable (selon graphe). Expressions de i et de la f.e.m. induite e dans les intervalles [0 ; 4s], [4 ; 6s] et [6 ; 8s].
4. Rotation de la bobine $S'$ ($\theta=100\pi t$). Calculer le flux $\Phi_0$ à $t=0$ et l'expression de $\Phi(t)$.""",

    # ═══════════════ 2016 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2016, "sc", 1): r"""Exercice 1 (4pt)
1. Oxydation des ions iodure par l'eau oxygénée en milieu acide. Écrire les demi-équations et l'équation bilan.
2. Dosage de $I_2$ par le thiosulfate $S_2O_3^{2-}$. Équation bilan.
3. Utilisation de la courbe $n(H_2O_2) = f(t)$ (avec $n_0=0{,}2$ mol et $C_{thiosulfate}=2{,}5$ mol/L) :
- Vitesse moyenne de disparition entre 0 et 24 min.
- Vitesse instantanée à $t=10$ min (et déduire celle de $I^-$).
- Volume de thiosulfate pour doser $I_2$ à $t=24$ min.
- Temps de demi-réaction.""",

    ("D", "pc", 2016, "sc", 2): r"""Exercice 2 (5pt)
Solution $S_1$ d'ammoniac ($C_1=6{,}3.10^{-4}$ mol/L, $pH=10$).
1. Couleur avec le vert de malachite (virage 11,5 – 13,2) ?
2. Calculer $n_0$ et $V_0$ (volume de gaz dissous).
3. Équation avec l'eau et concentrations effectives des espèces.
4. Valeur de la constante Ka.
5. Mélange de $V_1=20$ mL de $S_1$ avec $V_2=20$ mL de HCl ($C_2=2.10^{-4}$ mol/L) : équation et calcul du volume $V'_2$ pour obtenir une solution tampon ($pH=pKa$).""",

    ("D", "pc", 2016, "sc", 3): r"""Exercice 3 (5pt)
Terre autour du Soleil (trajectoire circulaire, $r=1{,}5.10^{11}$ m).
1. Caractéristiques et représentation de la force subie.
2. Montrer que le mouvement est uniforme via la RFD.
3. Expression de l'accélération en fonction de G, $M_s$ et r.
4. Expression et calcul de la vitesse V.
5. Expression et calcul de la période T.""",

    ("D", "pc", 2016, "sc", 4): r"""Exercice 4 (6pt)
1. Corde élastique : source A ($N=80$ Hz, $a=2$ mm). $t=0$ à la position d'équilibre.
1.1 Expression de l'élongation de A.
1.2 Élongation d'un point B (5 cm de A). État vibratoire et élongation à $t=31{,}25$ ms ($C=8$ m/s).
1.4 Observation stroboscopique (160 Hz, 40 Hz, 82 Hz, 79 Hz).
2. Deux sources $O_1$, $O_2$ ($d=8$ cm, 80 Hz, $V=3{,}2$ m/s) en opposition de phase.
2.1 Établir l'équation de $y_M$ d'un point M situé à $d_1$ et $d_2$.
2.2 Lieu et nombre des points d'amplitude maximale sur $[O_1, O_2]$.""",

    # ═══════════════ 2016 SESSION NORMALE ═══════════════
    ("D", "pc", 2016, "sn", 1): r"""Exercice 1 (4,5pt)
1. On considère une solution S d'une amine notée B. Écrire l'équation bilan de la réaction de cette amine B avec l'eau.
2. On dose $V_b=20$ mL de S par une solution $S'$ d'acide nitrique ($C_a=5.10^{-2}$ mol/L).
2.1 Écrire l'équation bilan du dosage.
2.2 L'équivalence est obtenue pour $V_a=40$ mL. Calculer $C_b$.
2.3 Le pH de S vaut 11,8. Déterminer le pKa du couple acide-base.
3. On obtient 0,4 L de S en dissolvant 1,8 g de B. Quelle est la masse molaire de B ? Donner les formules semi-développées possibles, leurs classes et leurs noms.
4. Calculer les volumes $V_a$ et $V_b$ nécessaires pour préparer 40 mL d'une solution tampon $S''$.
5. $S'$ est préparée à partir d'un flacon d'acide nitrique ($d=1{,}4$ ; 65 % en masse). Quelle est la concentration C de ce flacon ?""",

    ("D", "pc", 2016, "sn", 2): r"""Exercice 2 (4,5pt)
1. L'hydrolyse d'un ester E ($C_5H_{10}O_2$) donne de l'acide éthanoïque et un composé A. Famille de A ?
2. A est oxydé par $KMnO_4$ en un composé B. B réagit avec la 2,4-DNPH mais est sans action sur la liqueur de Fehling.
2.1 Famille de B ?
2.2 Formules semi-développées et noms de B et A.
3.1 Formule semi-développée et nom de l'ester E.
3.2 Équation d'hydrolyse de E et caractéristiques.
4. Équations pour passer de l'acide éthanoïque au chlorure d'éthanoyle et à l'anhydride éthanoïque.
5. Équation du chlorure d'éthanoyle avec l'éthylamine. Nom et fonction du produit.""",

    ("D", "pc", 2016, "sn", 3): r"""Exercice 3 (5,5pt)
Une bobine rectangulaire ($a=4$ cm, $b=10$ cm, $N=1000$, $m=120$ g) est suspendue à un ressort ($k=40$ N/m).
1.1 Allongement initial $\Delta l_0=3$ cm. Dans un champ B, avec $I=2$ A, l'allongement devient $\Delta l=5$ cm.
1.1.1 Représenter le sens du courant et les forces de Laplace $\vec{F}_{CD}$, $\vec{F}_{AC}$, $\vec{F}_{DE}$.
1.2 Condition d'équilibre et calcul de B.
2. On détache la bobine et on la fait entrer à vitesse constante V dans le champ B.
2.1 Exprimer la surface immergée en fonction de V, t et b.
2.2 Expressions du flux $\Phi$ et de la f.é.m. induite e.
2.3 Immobilisée et en rotation ($\omega=40$ rad/s), donner les expressions de $\Phi$ et e. Calculer leurs valeurs maximales.""",

    ("D", "pc", 2016, "sn", 4): r"""Exercice 4 (5,5pt)
Un skieur ($m=80$ kg) sur une piste ABCDE.
1. Sans vitesse en A, poussé par une force $\vec{F}$ sur AB ($l=20$ m), arrive en B avec une vitesse $\vec{V}_B$ pour atteindre C ($l'=40$ m, $\alpha=60^\circ$, $h=5$ m).
1.1 Calculer $V_B$ pour arriver en C avec une vitesse nulle.
1.2 Calculer la force F.
1.3 Nature du mouvement entre B et C.
2. Repart de C vers CD (horizontal). En D, $V_D=10$ m/s, puis entame le tronçon circulaire DE ($r=2{,}2$ m).
2.1.1 Vitesse $V_M$ au point M (angle $\theta$) et valeur en E.
2.1.2 Réaction R de la piste en M.
2.2.1 Équation de la trajectoire après E.
2.2.2 Abscisse du point de chute P.""",

    # ═══════════════ 2017 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2017, "sc", 1): r"""Exercice 1 (5pts)
1. Compléter un tableau avec les noms et fonctions pour :
- (A) Propanoate de 1-méthyl-propyle
- (B) $CH_3CH_2CH_2CH(CH_3)OH$
- (C) $(CH_3)_2CH-CO-Cl$
- (D) amide
2. Noms et fonctions des composés ayant permis d'obtenir B et C.
3. Écrire les équations pour obtenir A, B et C.
4. Identifier la molécule chirale parmi les réactifs de C et D et donner ses énantiomères.""",

    ("D", "pc", 2017, "sc", 2): r"""Exercice 2 (4pts)
1. Dosage de trois acides $A_1H$, $A_2H$, $A_3H$ ($V_a=20$ mL) par la soude ($C_B$). Équation bilan AH + NaOH.
2.1 Trouver les relations entre $C_1$, $C_2$ et $C_3$ à partir des volumes à l'équivalence ($V_{BE}$).
2.2 Déduire que $A_3H$ est le plus fort.
3. Dilution au dixième. La variation de pH est de 1 pour $A_3H$.
3.1 En déduire que $A_3H$ est un acide fort.
3.2 Justifier que $A_1H$ et $A_2H$ sont faibles.
3.3 Calculer $C_3$, $C_B$, $C_1$ et $C_2$.""",

    ("D", "pc", 2017, "sc", 3): r"""Exercice 3 (6pts)
Particules ($q$, $m$) entrant en O à vitesse $\vec{V}_0$.
1. Champ électrique $\vec{E}=E\vec{j}$.
1.1 Équation de la trajectoire.
1.2 Coordonnées de $\vec{V}_1$ à la sortie et expression de $\tan\alpha_1$.
1.3 Exprimer $q/(mV_0^2)$ en fonction de E, $l$ et $\alpha_1$.
2. Champ magnétique $\vec{B}=B\vec{K}$.
2.1 Montrer le mouvement circulaire uniforme.
2.2 Exprimer $q/(mV_0)$ en fonction de $\alpha_2$, B et $l$.
3. Calculer $V_0$ et la charge massique $q/m$.""",

    ("D", "pc", 2017, "sc", 4): r"""Exercice 4 (5pts)
Solénoïde S ($N=500$, $l=40$ cm) contenant une bobine b (50 spires, $r=4$ cm).
1. Caractéristiques de $\vec{B}$ pour $I=0{,}6$ A.
2. Le courant s'annule en 0,04 s. Variation du flux et valeur moyenne de la f.é.m. induite.
3. Courant i variable (selon graphe). Déterminer et représenter graphiquement la f.é.m. induite dans les intervalles [0 ; 4], [4 ; 8], [8 ; 12] et [12 ; 18] ms.""",

    # ═══════════════ 2017 SESSION NORMALE ═══════════════
    ("D", "pc", 2017, "sn", 1): r"""Exercice 1 (4pts)
1. Mélange de 100 cm³ de KI (0,1 mol/L) et 100 cm³ de $K_2S_2O_8$ (0,05 mol/L).
1.1 Demi-équations et équation-bilan.
1.2 Concentrations initiales dans le mélange.
2. Étude cinétique par dosage du diiode par le thiosulfate (0,01 mol/L).
2.1 Équation du dosage.
2.2 Calculer $[I_2]$ quand $V'_{thiosulfate}=40$ cm³.
2.3 Déterminer graphiquement la vitesse de formation à $t=20$ min.
2.4 Vitesse moyenne entre 25 et 40 min.
2.5 Réactif limitant et concentration finale de $[I_2]$.""",

    ("D", "pc", 2017, "sn", 2): r"""Exercice 2 (5pts)
Composés A et B de même masse molaire.
1. Oxydation de A en C. C réagit avec la DNPH mais pas avec la liqueur de Fehling.
1.1 Observation DNPH ?
1.2 Renseignements sur C et A.
2. A + B donne un ester D ($M=130$ g/mol) + eau.
2.1 Fonction de B ?
2.2 Montrer que A a 4 carbones et B en a 3.
2.3 Formules semi-développées et noms de A, B, C et D.
3. A obtenu par hydratation de l'alcène $A'$. Nom et formule de $A'$.
4. Dosage de B par la soude ($C_2=0{,}25$ mol/L). L'équivalence pour $V_1=10$ mL de B est atteinte à 20 mL de soude. Calculer la concentration $C_1$ et la masse de B.""",

    ("D", "pc", 2017, "sn", 3): r"""Exercice 3 (6pts)
Ressort horizontal ($K=20$ N/m) attaché à une masse m.
1. Équation différentielle du mouvement.
2. Équation horaire $x=f(t)$ (segment de 4 cm, $T=0{,}05$ s, passe en O à $t=0$ dans le sens positif).
3. Montrer que l'énergie mécanique $E=4.10^{-3}$ J.
4. Énergie cinétique à $t=0{,}25$ s.
5. S se détache à $t=5$ s et parcourt OA puis ABC (demi-cercle, $r=10$ cm).
5.1 Vitesse en A.
5.2 Vitesse en M (angle $\theta$) et valeur en C.""",

    ("D", "pc", 2017, "sn", 4): r"""Exercice 4 (5pts)
1. Dispositif de Young ($a=2{,}5$ mm, $D=1{,}5$ m).
1.1 Observation sur l'écran ?
1.2 Expression de la différence de marche $\delta$.
1.3 Expression de l'interfrange i. Calculer $\lambda$ pour $i=0{,}3$ mm.
1.4 Nature des franges à $x_1=1{,}05$ mm et $x_2=1{,}2$ mm.
2. Deux radiations ($\lambda_1=0{,}5$ µm et $\lambda_2=0{,}75$ µm).
2.1 Distance de la première coïncidence de franges brillantes.
2.2 Nature des franges qui coïncident à $OM_1=1{,}8$ mm.""",

    # ═══════════════ 2018 SESSION NORMALE ═══════════════
    ("D", "pc", 2018, "sn", 1): r"""Exercice 1 (4,25pts)
Un ester E a pour formule $C_4H_8O_2$.
1. Écrire la formule semi-développée de chacun des esters isomères de E.
2. L'hydrolyse de chacun de ces esters donne un acide et un alcool. Donner à chaque fois le nom et la formule semi-développée de l'acide et de l'alcool ainsi formés.
3. On fait agir 1,8 g d'eau sur 8,8 g de cet ester. Lorsque l'équilibre chimique est atteint, on constate que 5,28 g d'ester n'ont pas été hydrolysés.
3.1 Quelle est alors parmi les formules semi-développées écrites au 1ᵉʳ celle qui correspond à l'ester utilisé ?
3.2 Écrire l'équation chimique de cette réaction.
3.3 Calculer les masses des différents corps présents à l'équilibre.
3.4 Rappeler les caractéristiques de cette réaction.""",

    ("D", "pc", 2018, "sn", 2): r"""Exercice 2 (4,75pts)
1. On dissout une certaine masse d'un acide carboxylique noté RCOOH dans de l'eau distillée pour obtenir une solution $S_A$ de volume $V_A=20$ mL que l'on dose à l'aide d'une solution d'hydroxyde de sodium $S_B$ à $2.10^{-1}$ mol/L.
1.1 Déterminer les coordonnées du point d'équivalence.
1.2 Écrire l'équation-bilan de la réaction du dosage.
1.3 Déterminer la concentration molaire volumique de la solution $S_A$.
1.4 On veut déterminer le $pK_A$ du couple RCOOH/RCOO$^-$ de deux manières différentes.
1.4.1.1 Établir la relation entre le $pK_A$ et le pH de la solution à la demi-équivalence.
1.4.1.2 Trouver la valeur du $pK_A$.
1.4.2.1 Écrire l'équation de la réaction entre l'ion carboxylate et l'eau.
1.4.2.2 Établir l'expression de $K_A = \dfrac{C_A V_A Ke}{[OH^-]^2 (V_A+V_E)}$. En déduire la valeur du $pK_A$.
2. Dans une deuxième expérience, on répète le dosage après avoir ajouté un volume d'eau pure au volume $V_A$. Y a-t-il variation du pH initial, du pH à la demi-équivalence et du volume $V_E$ ?""",

    ("D", "pc", 2018, "sn", 3): r"""Exercice 3 (6pts)
Un satellite artificiel S de masse m tourne autour de la terre sur une orbite circulaire à l'altitude Z.
1.1 Donner les caractéristiques de la force gravitationnelle F. Exprimer son intensité en fonction de Z, m, G, R et M.
1.2 Montrer que le mouvement du satellite est uniforme. Exprimer sa vitesse V.
1.3 Donner l'expression de la période T. Montrer que $T^2/r^3$ est une constante.
2. La lune tourne autour de la terre ($r=385\,000$ km, période 27,3 jours). Calculer la masse de la terre.
3. Satellite géostationnaire :
3.1 Quelle est sa particularité ?
3.2 Exprimer puis calculer son altitude.""",

    ("D", "pc", 2018, "sn", 4): r"""Exercice 4 (5pts)
L'extrémité d'une lame vibrante est animée d'un mouvement vertical sinusoïdal ($a=2$ mm, $f=50$ Hz).
1.1 Établir l'équation horaire $y=f(t)$ du point O (début du mouvement vers le haut à $t=0$).
1.2 Établir l'équation horaire d'un point M à la distance x de O. Que dire du mouvement de M pour $x=2{,}25$ cm ?
1.3 Représenter la coupe de la surface de l'eau à $t=5.10^{-2}$ s.
2. On utilise une fourche à deux pointes $S_1$ et $S_2$ ($d=3{,}5$ cm) vibrant en phase.
2.1 Établir l'équation horaire du mouvement d'un point M situé à $d_1$ et $d_2$ des deux points.
2.2 Déterminer le nombre de points sur le segment $[O_1 O_2]$ vibrant avec une amplitude maximale.""",

    # ═══════════════ 2019 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2019, "sc", 1): r"""Exercice 1 (4,5pts)
1. Donner les formules semi-développées et fonctions de : 3-méthyl-butanal, chlorure de propanoyle, acide 2-méthyl-butanoïque, anhydride éthanoïque, butan-2-ol.
2. Identifier les molécules chirales et donner les deux énantiomères de l'une d'elles.
3. Oxydation ménagée du composé A par le dichromate de potassium. Écrire les équations et nommer le produit.
4. Réaction du composé B avec un alcool R-OH.
4.1 Écrire l'équation.
4.2 La réaction est-elle limitée ?
4.3 Identifier F et l'alcool si $m_F=102$ g.""",

    ("D", "pc", 2019, "sc", 2): r"""Exercice 2 (4,5pts)
1. Identifier les éléments du dispositif de dosage de la figure 1.
2.1 Justifier que B est une base faible et déterminer son $pK_b$.
2.2 Montrer que $C_B = 10^{-1}$ mol/L.
2.3 Déterminer la valeur de $C_A$.
3. Écrire l'équation de la réaction du dosage.
4. Calculer le pH à l'équivalence.
5. Déterminer la formule semi-développée et le nom de la base B (amine primaire) si $m=0{,}135$ g pour $V_B=30$ mL.""",

    ("D", "pc", 2019, "sc", 3): r"""Exercice 3 (5,5pts)
Une tige MN se déplace sur deux rails horizontaux à la vitesse $V=5$ m/s dans un champ B perpendiculaire.
1. Exprimer le flux magnétique à travers le circuit.
2. Déterminer la valeur de la f.e.m. induite.
3. Sens et intensité du courant induit.
4. Étude dynamique : caractéristiques de la force F appliquée.
5. Angle d'inclinaison $\alpha$ pour garder la même vitesse sans force F.""",

    ("D", "pc", 2019, "sc", 4): r"""Exercice 4 (5,5pts)
1. Aspect ondulatoire : fentes de Young ($a=2$ mm, $D=2$ m).
1.1 Observation sur l'écran ?
1.2 Définir l'interfrange i. Calculer i si $3i = 1{,}5$ mm. Nature des franges à $x=1$ mm et $x=1{,}75$ mm.
1.3 Calculer la longueur d'onde $\lambda$.
2. Aspect corpusculaire : cellule photoélectrique ($W_0=1{,}875$ eV, $\lambda=0{,}4$ µm).
2.1 Définir l'effet photoélectrique.
2.2 Définir et calculer la longueur d'onde seuil $\lambda_0$. Comparer avec $\lambda$.
2.3 Énergie cinétique maximale et vitesse de l'électron.
2.4 Définir et calculer le potentiel d'arrêt.""",

    # ═══════════════ 2019 SESSION NORMALE ═══════════════
    ("D", "pc", 2019, "sn", 1): r"""Exercice 1 (4,25pts)
Oxydation des ions iodures par l'ion peroxodisulfate : $2I^- + S_2O_8^{2-} \rightarrow I_2 + 2SO_4^{2-}$.
1.1 Calculer la concentration initiale $[I^-]_0$.
1.2 Montrer que $S_2O_8^{2-}$ est le réactif limitant. En déduire $[S_2O_8^{2-}]_0$ et $C_1$.
1.3 Compléter le tableau d'évolution.
2. Exprimer la vitesse volumique $V(t) = -d[I^-]/(2 dt)$ et déterminer sa valeur initiale.
3.1 Équation du dosage du diiode par le thiosulfate.
3.2 Calculer le volume d'équivalence à $t=10$ min.
4. Effet de l'ajout d'eau : évolution de l'avancement maximal et du temps de demi-réaction.""",

    ("D", "pc", 2019, "sn", 2): r"""Exercice 2 (4,75pts)
1.1 Calculer la concentration d'une solution d'acide RCOOH (0,6 g/L) dosée par NaOH.
1.2 Masse molaire et formule semi-développée de l'acide.
2. Acide $C_2H_5COOH$ ($pH=2{,}6$ pour 11,1 g dans 30 mL).
2.1 Calculer le coefficient d'ionisation $\alpha$.
2.2 Calculer le $pK_a$.
2.3 Mélange avec NaOH : nom du mélange et pH.
3. Propanoate d'éthyle (15,3 g) + eau (2,7 g).
3.1 Écrire l'équation.
3.2 Composition à l'équilibre et constante K.
3.3 Calculer la quantité d'eau x à ajouter pour obtenir 0,12 mol d'acide.""",

    ("D", "pc", 2019, "sn", 3): r"""Exercice 3 (6pts)
Mouvement d'ions ${}_3^6Li^+$ dans des champs E et B.
1. Accélération par $U_0=1252{,}5$ V. Montrer $V_0=2.10^5$ m/s.
2. Entrée dans un champ B ($2{,}5.10^{-1}$ T). Déterminer le sens de B pour une sortie en S.
3. Montrer que le mouvement est uniforme et calculer le rayon r.
4. Calculer la déviation angulaire $\alpha$.
5. Caractéristiques de la vitesse en S.
6. Champ électrique entre plaques C et D. Déterminer le sens de la force électrique.
7. Établir l'équation de la trajectoire.
8. Calculer $V_0$ ($E=2{,}5.10^4$ V/m, $l'=20$ cm).
9. Déterminer la distance d entre les armatures.""",

    ("D", "pc", 2019, "sn", 4): r"""Exercice 4 (5pts)
Oscillateur horizontal ($k=50$ N/m, $m=500$ g).
1. Établir l'équation différentielle du mouvement.
2. Déterminer l'équation horaire ($x_0=2$ cm, $v_o=\sqrt{3}/5$ m/s). Vitesse à la position d'équilibre ?
3. Exprimer l'énergie mécanique. Trouver la vitesse maximale.
4. Chute du solide : équation cartésienne de la trajectoire après avoir quitté la table en $O'$.
5. Coordonnées du point A au sol (5 cm plus bas).
6. Composantes et module de la vitesse en A ; angle $\beta$ avec la verticale.""",
}


_SESSION_MATCH = {"sn": "normal", "sc": "compl"}


def find_entry(data, filiere, matiere, annee, sess_code, ex_num):
    sess_substr = _SESSION_MATCH[sess_code]
    mat_accept = {"pc", "physique", "chimie"} if matiere == "pc" else {matiere}
    candidates = []
    for e in data:
        if e.get("filiere_id") != filiere:
            continue
        if e.get("matiere_id") not in mat_accept:
            continue
        if e.get("annee") != annee:
            continue
        if sess_substr not in str(e.get("session", "")).lower():
            continue
        try:
            num = int(e.get("exercice_numero"))
        except (TypeError, ValueError):
            continue
        if num != ex_num:
            continue
        candidates.append(e)
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    for c in candidates:
        if not c.get("is_skeleton") and (c.get("ennonce_complet") or "").strip():
            return c
    return candidates[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    data = json.loads(p.read_text(encoding="utf-8"))
    now = datetime.now().isoformat(timespec="seconds")

    updated, skipped_missing, skipped_filled = [], [], []
    for (fil, mat, annee, sess, ex_num), ennonce in EXOS.items():
        label = f"{fil}/{mat}/{annee}/{sess}/ex{ex_num}"
        e = find_entry(data, fil, mat, annee, sess, ex_num)
        if e is None:
            skipped_missing.append(label)
            continue
        eid = e.get("id", "?")
        old = (e.get("ennonce_complet") or "").strip()
        if old and len(old) > 100 and not args.force:
            skipped_filled.append((label, eid, len(old)))
            continue
        e["ennonce_complet"] = ennonce.strip()
        e["is_skeleton"] = False
        e["updated_at"] = now
        updated.append((label, eid, len(old), len(ennonce.strip())))

    print(f"Cible : {len(EXOS)} énoncés.")
    print(f"  → mis à jour    : {len(updated)}")
    print(f"  → introuvables  : {len(skipped_missing)}")
    print(f"  → déjà remplis  : {len(skipped_filled)} (--force pour écraser)")
    if updated:
        print("\nMises à jour :")
        for label, eid, ol, nl in updated:
            print(f"  {label:25}  → {eid:45}  {ol} → {nl} chars")
    if skipped_missing:
        print("\nIntrouvables :")
        for label in skipped_missing:
            print(f"  {label}")
    if skipped_filled:
        print("\nDéjà remplis :")
        for label, eid, ln in skipped_filled:
            print(f"  {label:25}  → {eid:45}  ({ln} chars)")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not updated:
        print("\nRien à écrire.")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(p, BACKUP_DIR / f"json_bac-pre-fill-d-pc-2015-2019-{stamp}.json")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"\n→ {p} mis à jour ({len(updated)} entrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
