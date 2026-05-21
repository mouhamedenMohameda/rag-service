"""Remplit 24 énoncés Bac C PC normale/compl 2015-2019 dans json_bac.json.

Source : transcription manuelle des sujets officiels (qualité estimée 60 %,
à revoir dans l'admin UI). NE TOUCHE PAS `validated_by_admin` — chaque exo
reste "à valider" dans l'UI.

Stratégie de mapping :
  Pour chaque cible (annee, session, ex_num), on cherche dans json_bac.json
  l'entrée correspondant à (filiere_id='C', matiere_id ∈ {pc, physique,
  chimie}, annee, session, exercice_numero). On gère ainsi les deux conventions
  d'ids présentes dans le JSON :
    - id canonique   : bac-c-YYYY-sn|sc-pc-exN
    - id legacy      : chimie-YYYY-sn-exN  ou  physique-YYYY-sn-exN
                       (préservés après migrate_pc.py — matiere_id="pc")

Comportement :
  - Met à jour `ennonce_complet`, `is_skeleton=False`, `updated_at`.
  - Si l'énoncé existant fait >100 chars, on skip sauf --force (les énoncés
    legacy chimie/physique font ~400-700 chars et sont remplacés par les
    versions plus longues + corrigées du user).
  - Backup automatique dans json_backups/ avant écriture.
  - Pas besoin de restart : le rag-service relit le JSON à chaque requête.

Usage :
    .venv/bin/python scripts/fill_pc_c_2015_2019.py --dry-run
    .venv/bin/python scripts/fill_pc_c_2015_2019.py
    .venv/bin/python scripts/fill_pc_c_2015_2019.py --force  # écrase même
                                                              # si déjà rempli
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


# ─── Énoncés à insérer ──────────────────────────────────────────────────────
# Clé logique : (annee, session_code, ex_num) où session_code ∈ {"sn","sc"}.
# Le script trouve dans le JSON l'entrée correspondante (id legacy ou canonique)
# en filtrant sur filiere_id='C' et matiere_id ∈ {pc,physique,chimie}.

EXOS: dict[tuple[int, str, int], str] = {
    # ─────────────────── 2015 SESSION NORMALE ───────────────────
    (2015, "sn", 1): r"""Exercice 1 (5pt)
1. On considère une solution d'acide propanoïque de concentration molaire $C=10^{-2}$ mol/L et de pH égal à 3,45.
1.1 Calculer les molarités des espèces chimiques présentes en solution. Déterminer le pKa du couple acide propanoïque/ion propanoate.
1.2 Calculer le coefficient d'ionisation $\alpha$ de l'acide propanoïque. Conclure.
1.3 On dispose de 10 mL de la solution précédente. On la dilue à un litre. Le pH prend la valeur 4,45. Calculer la nouvelle valeur $\alpha'$ du coefficient d'ionisation.
1.4 On considère une solution d'acide propanoïque de concentration molaire $C''=10^{-6}$ mol/L et de pH égal à 6. Calculer la nouvelle valeur du coefficient d'ionisation. Que dire du comportement de l'acide propanoïque très dilué.
2. En présence du chlorure de thionyle $SOCl_2$, on peut transformer l'acide propanoïque A en chlorure d'acyle B. L'action de B sur une amine E de formule brute $C_2H_7N$ donne naissance à un amide C.
2.1 Écrire à l'aide des formules semi-développées l'équation de la réaction qui donne B. Préciser le nom de B.
2.2 Donner toutes les formules semi-développées des amines de formule brute $C_2H_7N$ et préciser leurs classes.
2.3 Sachant que l'amine E est une amine secondaire, donner la formule semi-développée de l'amide C et son nom.
3. Le composé A a été obtenu par l'oxydation ménagée en deux étapes d'un composé D. Quelle est la formule semi-développée et le nom de D ?
4. Écrire les demi-équations et l'équation bilan de la deuxième étape d'oxydation si l'oxydant est le dichromate de potassium ($2K^+ + Cr_2O_7^{2-}$) en milieu acide.""",

    (2015, "sn", 2): r"""Exercice 2 (4pt)
1. On mélange 0,5 mol de pentan-1-ol $C_5H_{12}O$ et 0,5 mol d'acide méthanoïque $H_2CO_2$ dans un ballon. Le mélange est maintenu à température constante. En utilisant les formules semi-développées, écrire l'équation de la réaction qui se produit dans le ballon. Donner le nom de l'ester formé.
2. On prélève un volume $V_0=2$ cm³ du mélange toutes les 5 minutes, et après refroidissement, on dose l'acide restant avec une solution de soude de concentration $C_B=1$ mol/L en présence de phénolphtaléine.
- Quel est le but du refroidissement ?
- Écrire l'équation bilan de la réaction au cours du dosage.
3. Donner l'expression littérale de la quantité de matière d'acide restant $n_A$ dans le volume $V_0$ de prélèvement à l'instant t en fonction du volume $V_B$ de base versé à l'équivalence et de la concentration $C_B$ de la soude.
4. Calculer la quantité de matière d'acide $n_0$ contenue dans le volume $V_0$ à l'instant t=0 départ de la réaction d'estérification.
5. En déduire l'expression littérale de la quantité de matière d'ester formé $n_E$ dans le volume $V_0=2$ cm³ de mélange, à l'instant t, en fonction de $n_0$, $C_B$ et $V_B$.
Données : $\rho_{\text{pentan-1-ol}}=0{,}8$ g/cm³ ; $\rho'_{\text{acide méthanoïque}}=1{,}2$ g/cm³.""",

    (2015, "sn", 3): r"""Exercice 3
1. Une particule de masse m et de charge q positive est lancée dans le vide à la vitesse $V_0$ dans un plan P carré de côté $L=10$ cm où règne un champ magnétique uniforme perpendiculaire à $\vec{V}_0$.
1.1 Faire un schéma sur lequel il faut représenter la force F.
1.2 Montrer que le mouvement de la particule est uniforme et circulaire puis représenter sur la figure précédente la trajectoire.
1.3 Donner l'expression de la période T de rotation ainsi que celle de la fréquence N en fonction de m, q et B. Calculer T, si $B=1$ T et $q/m=10^8$ C/Kg.
2. On applique simultanément au champ magnétique B de la première question un champ électrique $\vec{E}$.
2.1 Indiquer sur une figure comment doit être dirigé E si l'on veut que le mouvement de la particule soit rectiligne uniforme.
2.2 Calculer E. On donne $V_0=5{,}10^7$ m/s.
2.3 On supprime B, la particule se déplace alors dans le champ électrique $\vec{E}$ précédent.
2.3.1 Trouver l'expression de l'équation de la trajectoire de la particule dans ce champ. Conclure.
2.3.2 Sachant que la particule sort entre B et C, calculer la déviation angulaire $\alpha$ de la particule dans le champ électrique.""",

    (2015, "sn", 4): r"""Exercice 4 (6pt)
1. Un solénoïde S de longueur $l=0{,}5$ m, de diamètre d et comportant $N=5000$ spires est parcouru par un courant d'intensité $I=8.10^{-2}$ A. Donner les caractéristiques du vecteur-champ magnétique $\vec{B}$ du solénoïde S. ($\mu_0=4\pi.10^{-7}$ S.I.)
2. À l'intérieur du solénoïde S, est placée une petite bobine S' de diamètre d' comportant N' spires. Les deux bobines ont le même axe horizontal x'x. Calculer la valeur du flux du champ magnétique $\vec{B}$ à travers la bobine S'. (AN : $N'=400$ ; $d'=4$ cm.)
3. Le solénoïde S est parcouru maintenant par un courant dont l'intensité i varie comme l'indique la courbe.
3.1 Déterminer l'expression de l'intensité i en fonction du temps dans les intervalles [0 ; 4s], [4s ; 6s] et [6s ; 8s].
3.2 Montrer que l'expression de la force électromotrice (f.e.m.) d'induction e qui apparaît dans la bobine peut s'écrire sous la forme $e=10^{-6}NN' \frac{d'^2}{l} \cdot \frac{di}{dt}$.
3.3 Calculer la force électromotrice induite dans les différents intervalles de temps.""",

    # ─────────────────── 2016 SESSION NORMALE ───────────────────
    (2016, "sn", 1): r"""Exercice 1 (4,5pt)
1. On considère une solution S d'une amine notée B. Écrire l'équation bilan de la réaction de cette amine B avec l'eau.
2. On dose un volume $V_b=20$ mL de la solution S à l'aide d'une solution S' d'acide nitrique de concentration molaire volumique $C_a=5.10^{-2}$ mol/L.
2.1 Écrire l'équation bilan de la réaction du dosage.
2.2 L'équivalence acido-basique est obtenue lorsqu'on verse $V_a=40$ mL de la solution S' d'acide nitrique. Calculer la concentration molaire volumique $C_b$ de la solution S.
2.3 Sachant que le pH de la solution S vaut 11,8, déterminer le pKa du couple acide-base.
3. On obtient 0,4 L de la solution S en dissolvant 1,8 g de cette amine. Quelle est la masse molaire de l'amine B. Donner les formules semi-développées possibles de B. Préciser leurs classes et leurs noms.
4. Pour préparer un volume V=40 mL d'une solution tampon S'' on mélange un volume $V_a$ de la solution S' d'acide nitrique et un volume $V_b$ de la solution basique S de l'amine B. Calculer les volumes $V_a$ et $V_b$.
5. La solution S' est préparée à partir d'un flacon commercial de 1 L d'acide nitrique de densité 1,4 contenant 65 % en masse de $HNO_3$. Quelle est la concentration C de cet acide nitrique ?""",

    (2016, "sn", 2): r"""Exercice 2 (4,5pt)
1. L'hydrolyse d'un ester E de formule $C_5H_{10}O_2$ conduit à la formation de l'acide éthanoïque et d'un composé A. À quelle famille appartient le composé A ?
2. Le composé A est oxydé par le permanganate de potassium en milieu acide. Il se forme un composé B. B réagit avec la 2,4-DNPH et il est sans action sur la liqueur de Fehling.
2.1 À quelle famille appartient le composé B ?
2.2 Donner les formules semi-développées et les noms des composés B et A.
3.1 Donner la formule semi-développée et le nom de l'ester E.
3.2 Écrire l'équation-bilan de la réaction d'hydrolyse de l'ester E. Préciser les caractéristiques de cette réaction.
4. Écrire une équation bilan de la réaction permettant de passer de l'acide éthanoïque :
4.1 au chlorure d'éthanoyle.
4.2 à l'anhydride éthanoïque.
5. Écrire l'équation-bilan de la réaction du chlorure d'éthanoyle avec l'éthylamine. Donner la fonction et le nom du produit organique obtenu.""",

    (2016, "sn", 3): r"""Exercice 3 (5,5pt)
1. On considère une bobine rectangulaire AEDC suspendue à un ressort.
1.1 Faire une figure où on représente, sur l'une des spires, le sens du courant parcourant la bobine AEDC. Justifier. Représenter les forces électromagnétiques $\vec{F}_{CD}$, $\vec{F}_{AC}$ et $\vec{F}_{DE}$ exercées à l'équilibre.
1.2 Écrire la condition d'équilibre de la bobine et établir l'expression de la valeur B du champ magnétique en fonction de k, $\Delta l$, m, g, a, I et N. Calculer la valeur B.
2. Après avoir coupé le courant, on détache la bobine du ressort et on la fait entrer avec une vitesse constante $\vec{v}$ dans le champ $\vec{B}$.
2.1 Exprimer à un instant t la surface de la partie immergée de l'une des spires dans le champ en fonction de V, t et b.
2.2 Tenant compte de l'orientation choisie, donner l'expression du flux magnétique en fonction de V, t, b, B et N et celle de la f.é.m. induite e en fonction de V, b, B et N.
3. Lorsque la bobine est totalement immergée, on la fait tourner autour d'un axe vertical avec une vitesse angulaire $\omega = 40$ rad/s.
3.1 Donner les expressions du flux et de la f.é.m. induite e en fonction de a, b, B, N, $\omega$ et t.
3.2 Calculer les valeurs maximales de flux et de e.""",

    (2016, "sn", 4): r"""Exercice 4 (5,5pt)
1. Un skieur de masse totale m=80 kg part sans vitesse du point A. Il est poussé sur AB par une force $\vec{F}$ parallèle à la piste pour arriver en B avec une vitesse $\vec{V}_B$ qui permet d'atteindre le point C. (AN : $AB=20$ m, $BC=40$ m, $g=10$ m/s², $\alpha=60°$.)
1.1 Calculer la valeur de la vitesse $V_B$ pour laquelle le skieur arrive en C avec une vitesse nulle.
1.2 Calculer alors la valeur supposée constante de la force F.
1.3 Déterminer la nature du mouvement du skieur entre B et C sachant que F ne s'exerce qu'entre A et B.
2. En arrivant en C le skieur repart sur CD, horizontale, et acquiert en D une vitesse $V_D = 10$ m/s avec laquelle il entame le tronçon circulaire DE de rayon $r=2{,}2$ m.
2.1.1 Exprimer la valeur $V_M$ de la vitesse au point M en fonction de $V_D$, r, g et de l'angle $\theta$ et en déduire sa valeur au point E.
2.1.2 Exprimer la valeur R de la réaction de la piste au point M en fonction de m, $V_D$, r, g et de l'angle $\theta$.
2.2 Le skieur quitte la piste au point E pour arriver au point P situé sur le sol.
2.2.1 Calculer l'équation de la trajectoire dans le repère $(E,x,y)$.
2.2.2 Calculer l'abscisse du point P de chute.""",

    # ─────────────────── 2017 SESSION NORMALE ───────────────────
    (2017, "sn", 1): r"""Exercice 1 (4pts)
1. On mélange dans un bécher 100 cm³ d'une solution 0,1 mol/L d'iodure de potassium (KI) et 100 cm³ d'une solution 0,05 mol/L de peroxodisulfate de potassium ($K_2S_2O_8$). Écrire les demi-équations d'oxydoréduction et l'équation-bilan.
2. Calculer les concentrations initiales $[I^-]_0$ et $[S_2O_8^{2-}]_0$ dans le mélange réactionnel.
3. On dose le diiode présent dans des prélèvements de 10 cm³ au moyen d'une solution titrée de thiosulfate de sodium $Na_2S_2O_3$ de concentration 0,01 mol/L. Écrire les demi-équations et l'équation-bilan de la réaction de dosage.
4. Calculer la concentration du diiode à l'instant t où le volume versé de thiosulfate est $V' = 40$ cm³.
5. Déterminer graphiquement la vitesse de formation du diiode à la date t = 20 min.
6. Calculer la vitesse moyenne de formation du diiode entre $t_1 = 25$ min et $t_2 = 40$ min.
7. Y a-t-il un réactif limitant ? Si oui lequel ? Calculer la concentration molaire du diiode obtenu au bout d'un temps infini.""",

    (2017, "sn", 2): r"""Exercice 2 (5pts)
1. L'oxydation ménagée de A conduit à un nouveau composé organique C. C réagit positivement avec DNPH et négativement avec la liqueur de Fehling. Qu'observe-t-on lors de la réaction entre C et la DNPH ? Quels renseignements sur C et A peut-on déduire ?
2. Le composé A réagit avec le composé B en donnant un ester D de masse molaire 130 g/mol et de l'eau. Quelle est la fonction du composé B ?
3. Montrer que la molécule de A contient 4 carbones et que celle de B en contient 3. Déterminer la formule semi-développée et le nom de chacun des composés A, B et C. En déduire la formule de D.
4. Le composé A est obtenu par hydratation d'un alcène A'. Donner la formule semi-développée et le nom de A'.
5. On dose un volume $V_1 = 10$ mL d'une solution de B par une solution d'hydroxyde de sodium de concentration $C_2 = 2{,}5.10^{-1}$ mol/L. Le rouge de crésol change de couleur pour un volume versé de 20 mL. Écrire l'équation du dosage et déterminer la concentration $C_1$ de B.""",

    (2017, "sn", 3): r"""Exercice 3 (6pts)
1. Soit un ressort de raideur $K = 20$ N/m guidé par une tige horizontale. Établir l'équation différentielle du mouvement de S.
2. Écrire l'équation horaire $x = f(t)$ sachant qu'à t=0 le centre d'inertie passe en O dans le sens positif et qu'il décrit un segment de 4 cm. Période $T = 0{,}05$ s.
3. Montrer que l'énergie mécanique E est égale à $4.10^{-3}$ J. Calculer l'énergie cinétique à t = 0,25 s.
4. À t = 5 s, la masse se détache du ressort et se déplace suivant une piste ABC en forme de demi-cercle de rayon r = 10 cm. Calculer la vitesse du solide S à l'arrivée en A.
5. Trouver l'expression de la vitesse de S en M tel que $(\vec{O''A},\vec{O''M}) = \theta$ et calculer sa valeur au point C.""",

    (2017, "sn", 4): r"""Exercice 4 (5pts)
1. Soit le dispositif de Young ($a = 2{,}5$ mm, $D = 1{,}5$ m). Décrire ce que l'on observe sur l'écran dans la zone d'interférence.
2. Établir en fonction de a, x et D, l'expression de la différence de marche $\delta$ au point M.
3. Donner l'expression de l'interfrange i. Calculer la longueur d'onde $\lambda$ sachant que $i = 0{,}3$ mm.
4. Quelle est la nature des franges dont les milieux sont situés à $x_1 = 1{,}05$ mm et $x_2 = 1{,}2$ mm du milieu O.""",

    # ─────────────────── 2017 SESSION COMPLÉMENTAIRE ───────────────────
    (2017, "sc", 1): r"""Exercice 1 (5pts)
1. Reproduire sur votre copie le tableau suivant et le compléter (composés : propanoate de 1-méthyl-propyle, anhydride propanoïque, chlorure de 3-méthylbutanoyle, N-méthyléthanamide).
2. Donner les noms et les fonctions des composés organiques qui ont permis d'obtenir les composés B et C.
3. Écrire les équations des réactions permettant d'obtenir les composés A, B et C.
4. L'une des molécules ayant permis d'obtenir A, B, C et D est chirale. Laquelle ? Donner ses deux énantiomères.""",

    (2017, "sc", 2): r"""Exercice 2 (4pts)
1. On considère les acides $A_1H$, $A_2H$ et $A_3H$ dont les solutions aqueuses sont respectivement $S_1$, $S_2$ et $S_3$. On dose $V_a = 20$ mL de chacune avec une solution de soude $C_B$. Écrire l'équation bilan.
2. Trouver la relation entre les concentrations ($C_1, C_2$ et $C_1, C_3$) et les volumes à l'équivalence. Déduire que $A_3H$ est l'acide le plus fort.
3. On procède à la dilution au dixième. Montrer que la variation du pH d'un acide fort dilué au dixième est égale à 1. En déduire que $A_3H$ est un acide fort.
4. Justifier que $A_1H$ et $A_2H$ sont des acides faibles. Déterminer $C_3$, $C_B$, $C_1$ et $C_2$.""",

    (2017, "sc", 3): r"""Exercice 3 (6pts)
1. Des particules ($q>0$, m) pénètrent avec $V_0$ dans un champ électrique E uniforme. Établir l'équation de la trajectoire. Déterminer les coordonnées de la vitesse de sortie $V_1$. Exprimer $\tan\alpha_1$ et le quotient $q/(mV_0^2)$.
2. Dans un champ magnétique uniforme B : montrer que la particule décrit un arc de cercle. Exprimer le quotient $q/(mV_0)$ en fonction de $\alpha_2$, B et l.
3. Calculer $V_0$ puis la charge massique $q/m$ ($E=10^4$ V/m, $B=2.10^{-2}$ T, $\alpha_1=\alpha_2=0{,}096$ rad, $l=0{,}2$ m).""",

    (2017, "sc", 4): r"""Exercice 4 (5pts)
1. Solénoïde S ($N=500$, $l=40$ cm) avec $I=0{,}6$ A. Donner les caractéristiques du champ magnétique B créé à l'intérieur.
2. L'intensité devient nulle en 0,04 s. Quelle est la variation du flux à travers une bobine interne (50 spires, rayon 4 cm) ? Quelle est la valeur moyenne de la f.e.m. induite ?
3. Déterminer les diverses valeurs de la f.e.m. induite dans les intervalles [0 ; 4], [4 ; 8], [8 ; 12] et [12 ; 18] ms selon le graphe i(t).""",

    # ─────────────────── 2018 SESSION NORMALE ───────────────────
    (2018, "sn", 1): r"""Exercice 1 (4,25pts)
1. Ester E de formule $C_4H_8O_2$. Écrire la formule semi-développée de chacun des esters isomères de E. Donner le nom et la formule de l'acide et de l'alcool formés par hydrolyse.
2. On fait agir 1,8 g d'eau sur 8,8 g d'ester. À l'équilibre, 5,28 g d'ester n'ont pas été hydrolysés.
- Quelle est la formule correspondant à l'ester utilisé ?
- Écrire l'équation chimique. Calculer les masses des différents corps à l'équilibre. Rappeler les caractéristiques de cette réaction.""",

    (2018, "sn", 2): r"""Exercice 2 (4,75pts)
1. Dosage de $V_A = 20$ mL d'un acide RCOOH par la soude $C_B = 10^{-2}$ mol/L. Déterminer les coordonnées du point d'équivalence.
2. Écrire l'équation-bilan et déterminer la concentration $C_A$.
3. Déterminer le $pK_A$ : établir la relation entre $pK_A$ et le pH à la demi-équivalence et trouver la valeur du $pK_A$.
4. Expliquer le caractère basique à l'équivalence (réaction ion carboxylate et eau).
5. Si on ajoute de l'eau (dilution), y a-t-il variation du pH initial, du pH à la demi-équivalence et du volume $V_E$ ?""",

    (2018, "sn", 3): r"""Exercice 3 (6pts)
1. Satellite artificiel S à l'altitude Z. Donner les caractéristiques de la force gravitationnelle. Exprimer son intensité.
2. Montrer que le mouvement est uniforme. Exprimer sa vitesse V. Donner l'expression de la période T et montrer que $T^2/r^3$ est une constante.
3. Lune ($r=385\,000$ km, $T=27{,}3$ jours). Calculer la masse de la terre.
4. Satellite géostationnaire : quelle est sa particularité ? Calculer l'altitude Z.""",

    (2018, "sn", 4): r"""Exercice 4 (5pts)
1. Lame vibrante ($a=2$ mm, $f=50$ Hz, $C=50$ cm/s). Établir l'équation horaire du mouvement de la source O et d'un point M à distance x.
2. Que peut-on dire du mouvement de M par rapport à O pour $x = 2{,}25$ cm ?
3. On utilise une fourche à deux pointes $S_1$, $S_2$ ($d = 3{,}5$ cm). Établir l'équation horaire d'un point M au voisinage de O. Trouver les positions des maxima d'amplitude.""",

    # ─────────────────── 2019 SESSION NORMALE ───────────────────
    (2019, "sn", 1): r"""Exercice 1 (4,25pts)
1. Oxydation des ions $I^-$ par $S_2O_8^{2-}$ (réaction totale). Calculer la concentration initiale $[I^-]_0$ dans le mélange ($V_1=50$ mL, $V_2=50$ mL, $C_2=0{,}1$ mol/L).
2. Montrer par la courbe $[I_2]=f(t)$ que $S_2O_8^{2-}$ est le réactif limitant. En déduire $[S_2O_8^{2-}]_0$ et $C_1$.
3. Compléter le tableau descriptif d'évolution du système.
4. Montrer que la vitesse volumique s'exprime par $v(t) = -d[I^-]/(2 dt)$. Déterminer sa valeur initiale.
5. Calculer à t = 10 min le volume V de thiosulfate nécessaire à l'équivalence ($V_0=10$ mL, $C=0{,}02$ mol/L).
6. On ajoute 25 mL d'eau distillée. Justifier sans calcul si l'avancement maximal et le temps de demi-réaction changent.""",

    (2019, "sn", 2): r"""Exercice 2 (4,75pts)
1. 0,6 g d'acide RCOOH dans 1 L d'eau. Dosage de 20 mL par soude 0,02 mol/L : équivalence à 10 mL. Calculer la concentration de l'acide et sa masse molaire. Formule semi-développée ?
2. Acide $C_2H_5COOH$ (11,1 g dans 30 mL d'eau, $pH=2{,}6$). Calculer le coefficient d'ionisation $\alpha$ et le pKa.
3. On mélange 15,3 g de propanoate d'éthyle et 2,7 g d'eau. Écrire l'équation. Déterminer la composition à l'équilibre s'il se forme 3,7 g d'acide. En déduire K.
4. On veut obtenir 0,12 mol d'acide. Calculer la quantité x d'eau à ajouter au mélange précédent.""",

    (2019, "sn", 3): r"""Exercice 3 (6pts)
1. Ions ${}_3^6Li^+$ accélérés par $U_0 = 1252{,}5$ V. Montrer que $V_0 = 2.10^5$ m/s.
2. Zone de largeur $l=1$ cm avec $B = 2{,}5.10^{-1}$ T. Déterminer le sens de B pour une sortie en S. Montrer que le mouvement est uniforme. Calculer le rayon r et la déviation $\alpha$.
3. Champ électrique E entre armatures C et D ($l'=20$ cm, $E=2{,}5.10^4$ V/m). Sens de la force électrique. Établir l'équation de la trajectoire. Calculer $V_0$.
4. Déterminer la distance d entre armatures si la distance minimale séparant l'ion de la plaque inférieure est 0,8 cm.""",

    (2019, "sn", 4): r"""Exercice 4 (5pts)
1. Ressort ($K = 50$ N/m) et solide S ($m = 500$ g). Établir l'équation différentielle et horaire ($x_0=2$ cm, $V_0=\sqrt{3}/5$ m/s). Calculer la vitesse à l'équilibre.
2. Exprimer l'énergie mécanique. Montrer qu'elle est constante. Retrouver $V_{max}$.
3. S se détache à O et quitte la table en O' pour atteindre le sol situé 5 cm plus bas. Déterminer l'équation cartésienne de la trajectoire et les coordonnées de l'impact A. Module et angle de la vitesse en A.""",
}


_SESSION_NAME = {"sn": "Normale", "sc": "Complémentaire"}
_SESSION_MATCH = {"sn": "normal", "sc": "compl"}  # substring de session.lower()


def find_entry(data: list[dict], annee: int, sess_code: str, ex_num: int) -> dict | None:
    """Trouve l'entrée pour (filiere C, PC, annee, session, exercice_numero).

    Gère :
      - matiere_id ∈ {pc, physique, chimie}  (legacy + canonique post-migrate_pc)
      - exercice_numero stocké en int OU en string ("1", "BAC-2010-...")
      - session écrit "Normale" / "normale" / "Complémentaire" etc.
    """
    sess_substr = _SESSION_MATCH[sess_code]
    candidates: list[dict] = []
    for e in data:
        if e.get("filiere_id") != "C":
            continue
        if e.get("matiere_id") not in ("pc", "physique", "chimie"):
            continue
        if e.get("annee") != annee:
            continue
        if sess_substr not in str(e.get("session", "")).lower():
            continue
        raw = e.get("exercice_numero")
        try:
            num = int(raw)
        except (TypeError, ValueError):
            continue
        if num != ex_num:
            continue
        candidates.append(e)
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
    # Tie-break : préfère l'entrée déjà non-squelette (legacy filled) plutôt
    # qu'un squelette dupliqué. Sinon, premier trouvé.
    for c in candidates:
        if not c.get("is_skeleton") and (c.get("ennonce_complet") or "").strip():
            return c
    return candidates[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="Affiche ce qui serait fait, sans écrire.")
    ap.add_argument("--force", action="store_true",
                    help="Écrase même si ennonce_complet est déjà rempli (>100 chars).")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    data: list[dict] = json.loads(p.read_text(encoding="utf-8"))

    now = datetime.now().isoformat(timespec="seconds")
    updated: list[tuple[str, str, int, int]] = []  # (label, id_used, old_len, new_len)
    skipped_missing: list[str] = []
    skipped_filled: list[tuple[str, str, int]] = []

    for (annee, sess_code, ex_num), ennonce in EXOS.items():
        label = f"{annee}-{sess_code}-ex{ex_num}"
        e = find_entry(data, annee, sess_code, ex_num)
        if e is None:
            skipped_missing.append(label)
            continue
        eid = e.get("id", "?")
        old = (e.get("ennonce_complet") or "").strip()
        if old and len(old) > 100 and not args.force:
            skipped_filled.append((label, eid, len(old)))
            continue
        old_len = len(old)
        new_text = ennonce.strip()
        e["ennonce_complet"] = new_text
        e["is_skeleton"] = False
        e["updated_at"] = now
        # /!\ On NE TOUCHE PAS validated_by_admin — l'admin doit relire.
        updated.append((label, eid, old_len, len(new_text)))

    # ─── Rapport ────────────────────────────────────────────────────────────
    print(f"Cible : {len(EXOS)} énoncés à insérer.")
    print(f"  → mis à jour    : {len(updated)}")
    print(f"  → introuvables  : {len(skipped_missing)}")
    print(f"  → déjà remplis  : {len(skipped_filled)} (utiliser --force pour écraser)")

    if updated:
        print("\nMises à jour :")
        for label, eid, ol, nl in updated:
            print(f"  {label:18}  → {eid:45}  {ol} → {nl} chars")
    if skipped_missing:
        print("\nIntrouvables (cas où aucune entrée n'existe — créer via admin UI):")
        for label in skipped_missing:
            print(f"  {label}")
    if skipped_filled:
        print("\nDéjà remplis (>100 chars) — skippés sans --force :")
        for label, eid, ln in skipped_filled:
            print(f"  {label:18}  → {eid:45}  ({ln} chars existants)")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not updated:
        print("\nRien à écrire.")
        return 0

    # ─── Backup défensif puis écriture atomique ──────────────────────────────
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-fill-2015-2019-{stamp}.json"
    shutil.copy2(p, backup)
    print(f"\nBackup : {backup}")

    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"→ {p} mis à jour ({len(updated)} entrées).")
    print("Pas besoin de restart : rag-service relit le JSON à chaque requête.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
