"""Remplit 34 énoncés Bac D · PC · 2020-2024 (Gemini, à valider).

Convention pour QCM (présents en 2023 SN et 2024 SN) :
  ex1 = QCM (premier dans le sujet papier)
  ex2 = Exercice 1 du sujet
  ex3 = Exercice 2
  ex4 = Exercice 3
  ex5 = Exercice 4

Pour les autres années sans QCM, ex1-ex4 = Exercice 1-4 (ex5 vide).
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

    # ═══════════════ 2020 SESSION NORMALE ═══════════════
    ("D", "pc", 2020, "sn", 1): r"""Exercice 1 (4,75 pts) – Cinétique chimique
Étude de la décomposition de l'iodure d'hydrogène (HI) en $I_2$ et $H_2$ à $380^\circ$C.
1.1 Pourquoi refroidit-on rapidement l'ampoule avant le dosage ?
1.2 Écrire les demi-équations et l'équation-bilan de la réaction de dosage du diiode par le thiosulfate de sodium ($Na_2S_2O_3$).
1.3 Montrer que la quantité de diiode formé est $n(I_2) = \dfrac{CV}{2}$.
2.1 Définir la vitesse instantanée de formation du diiode.
2.2 Calculer les vitesses de formation à $t=0$ pour les températures $250^\circ$C et $380^\circ$C à partir du graphique.
2.3 Identifier le facteur cinétique mis en évidence.""",

    ("D", "pc", 2020, "sn", 2): r"""Exercice 2 (4,25 pts) – Acide-Base
1.1 Définir un acide fort et un acide faible. L'acide méthanoïque (HCOOH) de $C_A=6.10^{-2}$ mol/L et $pH=2{,}49$ est-il fort ou faible ?
1.2 Écrire l'équation de sa réaction avec l'eau.
1.3 Établir le tableau d'avancement et calculer le taux d'avancement final.
2.1 Écrire l'équation du dosage de cet acide par la soude ($C_B=0{,}05$ mol/L).
2.2 Retrouver la valeur de $C_A$ sachant que l'équivalence est atteinte pour $V_B=6$ mL.
2.3 Choisir l'indicateur coloré adéquat (hélianthine, BBT ou bleu de thymol) pour un pH à l'équivalence de 8,7.
2.4 À quoi correspond le pH du mélange à la demi-équivalence ($V_B=3$ mL) ?""",

    ("D", "pc", 2020, "sn", 3): r"""Exercice 3 (5,5 pts) – Mécanique (chute et projectile)
Un solide S glisse sur un plan incliné AB ($\alpha=30^\circ$) puis quitte la piste en C.
1.1 Établir l'équation horaire du mouvement sur AB.
1.2 Calculer la longueur AB (pour $h=1{,}25$ m) et les vitesses $V_B$ et $V_C$.
2.1 Établir l'équation de la trajectoire du mobile après le point C dans le repère $(Cx, Cy)$.
2.2 Exprimer et calculer la portée CP.
2.3 Exprimer la flèche et déterminer la valeur de $\alpha$ pour laquelle elle est maximale.""",

    ("D", "pc", 2020, "sn", 4): r"""Exercice 4 (5,5 pts) – Physique atomique (électrons et champs)
1.1 Déterminer le signe et la valeur de la tension accélératrice $U_0$ pour un champ $E=6.10^3$ V/m.
1.2 Calculer la vitesse $V_0$ à l'arrivée en O.
2.1 Établir l'équation de la trajectoire entre deux plaques déviatrices sous une tension U.
2.2 Calculer U pour une déviation $\tan(\alpha)=0{,}3$.
3.1 Nature du mouvement dans un champ magnétique B et expression du rayon R.
3.2 Calculer la déviation angulaire magnétique pour $B=2{,}25.10^{-1}$ T.
3.3 Valeur de B pour que l'électron effectue un quart de cercle.""",

    # ═══════════════ 2021 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2021, "sc", 1): r"""Exercice 1 (4 pts) – Estérification / Hydrolyse
Réaction du méthanoate d'éthyle ($C_3H_6O_2$) dans deux ballons (A) et (B) avec des conditions de température et de quantités initiales différentes.
1. Écrire l'équation chimique avec formules semi-développées.
2. Montrer graphiquement que la réaction est lente et limitée.
3.1 Déterminer la composition du système à l'équilibre pour (A) et (B).
3.2 Calculer la constante d'équilibre K.
3.3 Conclusion sur le caractère énergétique de la réaction.
4. Déterminer le sens d'évolution spontanée d'un mélange donné à une date t.""",

    ("D", "pc", 2021, "sc", 2): r"""Exercice 2 (5 pts) – Acide-Base
Comparaison entre $S_1$ (acide chlorhydrique, $pH=2$) et $S_2$ (acide méthanoïque, $pH=2{,}9$) à $C=10^{-2}$ mol/L.
1. Identifier l'acide fort et l'acide faible ; écrire les équations avec l'eau.
2.1 Vérifier que $pK_a(S_2)=3{,}74$.
2.2 Établir l'expression du pH en fonction de C et $pK_a$.
2.3 Calculer le coefficient de dissociation $\alpha$.
2.4 Calculer le pH après une dilution par 10.
3. Calculer le volume d'eau $v_1$ à ajouter à $S_1$ pour passer d'un $pH=2$ à $pH=3{,}4$.""",

    ("D", "pc", 2021, "sc", 3): r"""Exercice 3 (5 pts) – Mécanique (skieur)
1.1 Nature du mouvement d'un skieur sur un plan incliné ($\theta=30^\circ$) sans frottement.
1.2 Exprimer $E_c$ et $E_p$ en fonction de l'abscisse x.
1.3 En déduire l'énergie mécanique E.
2.1 Exprimer la vitesse $V_0$ au point de saut en fonction de h et g.
2.2 Établir l'équation de la trajectoire après le saut (angle $\alpha=60^\circ$).
2.3 Coordonnées du sommet S de la trajectoire.
2.4 Valeur minimale $h_m$ pour franchir un bassin de largeur $d=10$ m.""",

    ("D", "pc", 2021, "sc", 4): r"""Exercice 4 (6 pts) – Optique (interférences)
1.1 Définir l'interfrange.
1.2 Calculer la distance entre fentes $a_1$ et la longueur d'onde $\lambda$ à partir de deux interfranges donnés.
2.1 Représenter et calculer la largeur du champ d'interférences.
2.2 Nombre de franges brillantes et sombres sur l'écran.
3.1 Observation avec deux radiations ($\lambda_1=0{,}48$ µm et $\lambda_2=0{,}54$ µm).
3.2 Distance de la première coïncidence des franges brillantes.
4. Longueurs d'onde du spectre visible formant une frange obscure à $x=2$ mm en lumière blanche.""",

    # ═══════════════ 2021 SESSION NORMALE ═══════════════
    ("D", "pc", 2021, "sn", 1): r"""Exercice 1 (4 pts) – Cinétique chimique
Oxydation de l'ion iodure $I^-$ par l'ion peroxodisulfate $S_2O_8^{2-}$.
1.1 Citer deux facteurs cinétiques et leur influence.
1.2 Pourquoi la vitesse d'une réaction diminue-t-elle généralement au cours du temps ?
2.1 Écrire les demi-équations et l'équation-bilan.
2.2 Calculer la vitesse instantanée de disparition de $S_2O_8^{2-}$ à $t=75$ s et en déduire celle de formation de $SO_4^{2-}$.
2.3 Identifier les courbes correspondant aux températures $20^\circ$C et $30^\circ$C.
2.4 Expliquer l'utilité de l'eau glacée lors des prélèvements.
2.5 Déterminer la composition du mélange à $t=25$ s pour la courbe (a).""",

    ("D", "pc", 2021, "sn", 2): r"""Exercice 2 (5 pts) – Chimie organique
1. Nommer les composés et leurs fonctions : propan-2-ol, butanal, butanone, acide éthanoïque.
2. Donner les isomères de position, de fonction et de chaîne pour certains de ces composés.
3.1 Réaction entre un alcool et un acide : donner le nom et la formule de l'ester E obtenu.
3.2 Citer deux autres réactifs pouvant former le même ester E.
4. Équation de l'oxydation ménagée d'un alcool par le permanganate de potassium.
5. Réaction entre un acide et une amine A pour former un amide de formule brute $C_4H_9ON$.""",

    ("D", "pc", 2021, "sn", 3): r"""Exercice 3 (6 pts) – Mécanique (oscillateur)
1. Calculer la raideur K d'un ressort s'allongeant de 10 cm avec une masse $m=100$ g.
2.1 Établir l'équation différentielle du mouvement sur un plan horizontal.
2.2 Déterminer l'équation horaire $x(t)$ sachant que $V_0=0{,}4$ m/s à $t=0$.
3.1 Exprimer l'énergie mécanique totale E du système.
3.2 Retrouver l'équation différentielle à partir de la conservation de l'énergie mécanique.""",

    ("D", "pc", 2021, "sn", 4): r"""Exercice 4 (5 pts) – Électromagnétisme (force de Laplace et induction)
1.1 Direction et sens de B pour que la barre MN s'éloigne du générateur.
1.2 Calculer l'intensité de la force de Laplace pour $I=5$ A et $B=0{,}5$ T.
2.1 Cas des rails verticaux : sens de B pour que la barre glisse vers le générateur.
2.2 Intensité minimale I pour que la barre commence à monter.
2.3 Équilibre avec un ressort ($K=10$ N/m) : calculer I pour un allongement de 1 cm.
3.1 Phénomène d'induction : exprimer la f.e.m. e et l'intensité i induite en fonction de V.
3.2 Caractéristiques et module de la force électromagnétique de freinage $\vec{f}$.""",

    # ═══════════════ 2022 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2022, "sc", 1): r"""Exercice 1 (4 pts)
À un instant $t=0$, on réalise, dans un bécher, un mélange réactionnel constitué d'un volume $V_1=10$ mL d'une solution aqueuse d'iodure de potassium KI de concentration molaire $C_1=5.10^{-1}$ mol/L et d'un volume $V_2=10$ mL d'une solution aqueuse de peroxodisulfate de potassium $K_2S_2O_8$ de concentration molaire $C_2=5.10^{-3}$ mol/L. Les ions iodure $I^-$ réagissent avec les ions peroxodisulfate $S_2O_8^{2-}$ selon l'équation : $2I^-+S_2O_8^{2-}\rightarrow I_2+2SO_4^{2-}$. Au cours de l'expérience, la température reste constante. On note x l'avancement de la réaction à l'instant t.
1.1 Dresser le tableau d'avancement du système.
1.2 Déterminer le réactif limitant. En déduire l'avancement maximal $x_{max}$ et la quantité de matière maximale de diiode formé.
2. À partir des résultats des mesures, on obtient la courbe $x=f(t)$.
2.1 Déterminer graphiquement l'avancement final $x_f$.
2.2 Comparer $x_{max}$ et $x_f$. La réaction est-elle limitée ?
3.1 Définir la vitesse de la réaction. Déterminer sa valeur à $t=10$ min.
3.2 Déduire la vitesse de disparition de $I^-$ à cet instant.
3.3 Décrire l'évolution de la vitesse au cours du temps.""",

    ("D", "pc", 2022, "sc", 2): r"""Exercice 2 (5 pts)
Un composé organique B a pour formule brute $C_3H_6O$.
1. On ajoute quelques gouttes de 2,4-DNPH ; le test est positif. Quelle est la couleur du précipité ? Déduire les formules semi-développées possibles et leurs noms.
2. Avec le réactif de Schiff, on obtient un précipité rose. En déduire la fonction de B.
3. B est oxydé par le dichromate de potassium acidifié ($Cr_2O_7^{2-}/Cr^{3+}$) pour donner un acide C. Écrire l'équation bilan.
4. B a été obtenu par oxydation d'un alcool A.
4.1 Déduire la classe, la formule et le nom de A.
4.2 A est préparé par hydratation d'un alcène. Établir l'équation bilan (formules brutes) et écrire les formules des alcools obtenus. A est-il majoritaire ?
5. Solution d'acide C à $C_A=0{,}01$ mol/L, $pH=3{,}45$.
5.1 L'acide est-il fort ou faible ? Justifier.
5.2 Calculer le $pK_a$ du couple associé à C.
5.3 Calculer $V_A$ et $V_B$ (soude à 0,01 mol/L) pour obtenir 30 mL de solution tampon.""",

    ("D", "pc", 2022, "sc", 3): r"""Exercice 3 (5,5 pts)
Un point matériel M ($m=50$ g) est lancé de O vers le haut d'un plan incliné de $15^\circ$ avec $V_0=3$ m/s. Longueur $OA=1$ m.
1.1 Sans frottement, calculer la vitesse $V_A$ au sommet.
1.2 En réalité, $V'_A=1$ m/s. Déterminer l'intensité de la force de frottement f supposée constante.
2. Le mobile quitte le plan en A avec $V'_A=1$ m/s.
2.1 Établir l'équation de la trajectoire dans le repère $(A; x, y)$.
2.2 Calculer la distance HD (point de chute).
2.3 Déterminer la vitesse $V_D$ au point D.""",

    ("D", "pc", 2022, "sc", 4): r"""Exercice 4 (5,5 pts)
1. Cellule au césium éclairée par $\lambda=410.10^{-9}$ m.
1.1 Définir et donner la valeur du potentiel d'arrêt $U_0$ (via Fig 1).
1.2 Calculer la vitesse d'émission des électrons.
1.3 Calculer l'énergie d'extraction $W_0$ et la fréquence seuil $\nu_0$.
1.4 Pour $U_{AC}=10$ V, calculer la vitesse $V_A$ à l'anode.
2. Atome d'hydrogène : $E_n=-13{,}6/n^2$ (eV).
2.1 Compléter le diagramme d'énergie (Fig 2).
2.2.1 Calculer l'énergie du photon pour la transition $n=1\rightarrow n=3$.
2.2.2 En déduire la longueur d'onde $\lambda$ correspondante.""",

    # ═══════════════ 2022 SESSION NORMALE ═══════════════
    ("D", "pc", 2022, "sn", 1): r"""Exercice 1 (5 pts)
Mélange de $n_0=0{,}5$ mol d'acide propanoïque et $n_0=0{,}5$ mol de propan-2-ol en présence de $H_3O^+$.
1. Nommer la réaction et citer deux caractéristiques.
2. Écrire l'équation (formules semi-développées) et nommer l'ester E obtenu.
3. Via le graphique $n_E=f(t)$ :
3.1 Donner la composition à l'équilibre et calculer K.
3.2 Calculer le rendement. Conclure.
3.3 Nommer un autre composé dont la réaction totale avec le propan-2-ol donne E.
3.4 Calculer la vitesse à $t=3{,}5$ h.
3.5 Rôle des ions $H_3O^+$ et nom générique de tels composés.""",

    ("D", "pc", 2022, "sn", 2): r"""Exercice 2 (4 pts)
1. Solution $S_A$ d'HCl ($C_A=0{,}015$ mol/L) préparée par dilution d'une solution commerciale ($d=1{,}15$, 37 %). Montrer que $C_0\approx 11{,}66$ mol/L.
2. Base faible B de concentration C.
2.1 Montrer que $\tau=[OH^-]/C$ et $K_A=\dfrac{K_e(1-\tau)}{C\cdot \tau^2}$.
2.2 Pour $C=10^{-2}$ mol/L, on a $pH_1=10{,}6$ ($NH_3$) et $pH_2=9$ ($NH_2OH$). Calculer $\tau_1$ et $\tau_2$.
2.3 Calculer $pK_{A1}$ et $pK_{A2}$.
3. Dosage de 20 mL de solution S ($C'=C_B/1000$) par $S_A$.
3.1 Équation du dosage.
3.2 Avec $V_{AE}=14{,}2$ mL, calculer $C'$ puis $C_B$.""",

    ("D", "pc", 2022, "sn", 3): r"""Exercice 3 (6 pts)
Ressort horizontal ($k=5$ N/m) lié à un solide ($m=0{,}2$ kg). À $t=0$, $x_0=3$ cm et $V_0=-\pi/10$ m/s.
1. Calculer l'énergie mécanique à $t_0$.
2. Établir l'équation différentielle et l'équation horaire.
3. Par conservation d'énergie, déterminer :
3.1 Les vitesses à la position d'équilibre.
3.2 Les positions où la vitesse s'annule.
4. Ressort vertical avec fourche créant des ondes à la surface de l'eau ($a=3$ cm, $y=a\cos(100\pi t+\pi)$).
4.1 Équation horaire d'un point M à $d_1$, $d_2$. Application pour $d_1=2$ cm, $d_2=14$ cm, $C=2$ m/s.
4.2 Nombre de franges d'amplitude maximale pour $O_1O_2=12$ cm.""",

    ("D", "pc", 2022, "sn", 4): r"""Exercice 4 (5 pts)
Ions émis en $F_1$ sans vitesse. Accélération entre $P_1, P_2$ par $|U|=10^3$ V.
1. Signe de U pour que les ions atteignent $P_2$.
2. Expression de V en $F_2$ en fonction de m, q, U.
3. Calculer V pour ${}^{200}Hg^{2+}$ et ${}^{202}Hg^{2+}$.
4. Passage entre $P_2, P_3$ (champs $E_1$ et $B_1$). Montrer que seuls les ions avec $V=E_1/B_1$ atteignent $F_3$. Est-ce le cas ici ? ($E_1=6.10^4$ V/m, $B_1=1$ T).
5. Déviation par $\vec{B}$ après $F_3$.
5.1 Déterminer le sens de $\vec{B}$ et le signe des charges de $X_1$, $X_2$, $X_3$.
5.2 Calculer les masses $m_1$, $m_2$, $m_3$ pour $r_1=2{,}2$ cm, $r_2=1{,}44$ cm, $r_3=1{,}2$ cm.
5.3 Identifier les ions via le tableau fourni.""",

    # ═══════════════ 2023 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2023, "sc", 1): r"""Exercice 1 (3,75 pts)
On dissout 1,11 g d'acide propanoïque dans 150 mL d'eau ($S_0$, $pH=2{,}45$).
1. Montrer que l'acide est faible.
2. Solution S : 100 mL de $S_0$ + $V_e$ d'eau, $pH=3$.
2.1 Concentrations des espèces dans S.
2.2 En déduire C et calculer $V_e$.
3. Dosage de 100 mL de S par soude ($C_b=2.10^{-1}$ mol/L).
3.1 Nature de la solution à l'équivalence et concentration $C'$.
3.2 Calculer le pH à l'équivalence.
3.3 Le bleu de bromothymol est-il approprié ?""",

    ("D", "pc", 2023, "sc", 2): r"""Exercice 2 (4,25 pts)
$H_2O_2+2I^-+2H_3O^+\rightarrow I_2+4H_2O$. Mélange : $V_1=40$ mL de $H_2O_2$ (0,5 mol/L) + $V_2=75$ mL de KI ($C_2$) + excès d'acide.
1. Tableau descriptif d'évolution.
2. À $t_1=6$ min, il reste $1{,}5.10^{-2}$ mol de $I^-$.
2.1 Déterminer $x_1$ et $C_2$.
2.2 Montrer que $I^-$ est limitant.
2.3 Déterminer $x_f$ et la composition finale.
3. Définir et calculer la vitesse à $t=10$ min. Évolution ?
4. À température plus élevée, $x=0{,}015$ mol à $t=10$ min. Vérifier que la réaction est finie et conclure sur le rôle de la température.""",

    ("D", "pc", 2023, "sc", 3): r"""Exercice 3 (5,5 pts)
Piste ABCM : AB rectiligne ($L=l$, $\alpha=30^\circ$), BM circulaire ($r=2{,}5$ m). Solide $m=200$ g lancé de A avec $V_A$.
1. Frottements négligeables.
1.1 Nature du mouvement sur AB, expression de $V_B$. Calculer $V_A$ si $V_B=4{,}56$ m/s.
1.2 Expression de $V_C$ en fonction de g, $V_A$, r.
1.3 Expression de $V_M$ en fonction de g, $V_A$, r, $\theta$.
1.4 Expression et calcul de la réaction R en M.
2. Avec frottement f constant sur ABC. $V'_C=3$ m/s. Expression et calcul de f.
3. Arrivée en M avec $V_M=4$ m/s, mouvement dans le vide. Équation de la trajectoire.""",

    ("D", "pc", 2023, "sc", 4): r"""Exercice 4 (4 pts)
Cellule éclairée par $\lambda_1=0{,}49$ µm et $\lambda_2=0{,}4$ µm. Métaux : Potassium (2,26 eV) ou Strontium (2,06 eV).
1. Calculer en Joules :
1.1 Énergie des photons pour $\lambda_1$ et $\lambda_2$.
1.2 Travail d'extraction pour K et Sr.
2. Justifier :
2.1 Extraction possible sur K avec les deux radiations ?
2.2 $|U_0|$ est-il plus grand pour $\lambda_1$ ou $\lambda_2$ sur Sr ?
3. Calculer la vitesse d'émission sur Sr avec $\lambda_1$.
4. Calculer $U_{AC}$ pour que $V_A=1500$ km/s.""",

    # ═══════════════ 2023 SESSION NORMALE (QCM + 4 exos) ═══════════════
    ("D", "pc", 2023, "sn", 1): r"""QCM (4 pts)
Indiquer pour chaque n° de question la ou les réponse(s) exacte(s).
1. L'expression de la constante d'acidité $K_a$ associée à l'équation $NH_4^+ + H_2O \rightleftharpoons NH_3 + H_3O^+$ est :
A. $K_a=\dfrac{[H_3O^+][NH_4^+]}{[NH_3][H_2O]}$
B. $K_a=\dfrac{[H_3O^+][NH_4^+]}{[NH_3]}$
C. $K_a=\dfrac{[H_3O^+][NH_3]}{[NH_4^+]}$
2. Le réactif de Tollens donne un test positif avec :
A. Les cétones
B. Les aldéhydes
C. Les alcools
3. On dit qu'il y a effet photoélectrique si :
A. Un électron est émis
B. Un photon est émis
C. Un photon et un électron sont absorbés
4. L'expression de l'interfrange i est :
A. $i=\dfrac{ax}{D}$
B. $i=\dfrac{aD}{\lambda}$
C. $i=\dfrac{\lambda D}{a}$""",

    ("D", "pc", 2023, "sn", 2): r"""Exercice 1 (3,5 pts)
Les ions peroxodisulfate $S_2O_8^{2-}$ oxydent lentement les ions iodures $I^-$. Établir l'équation bilan de cette réaction. On donne les couples $S_2O_8^{2-}/SO_4^{2-}$ et $I_2/I^-$.
1. À la date $t=0$, et à une température constante, on réalise un mélange de volume total $V=40$ mL en versant dans un erlenmeyer un volume $V_1$ d'une solution aqueuse de peroxodisulfate d'ammonium $(NH_4)_2S_2O_8$ de concentration molaire $C_1$, un volume $V_2=V_1$ d'une solution aqueuse d'iodure de potassium KI de concentration molaire $C_2=3C_1$ et quelques gouttes d'une solution d'empois d'amidon.
2.1 Exprimer les concentrations molaires initiales $[S_2O_8^{2-}]_0$ et $[I^-]_0$ en fonction de $C_1$ dans le mélange réactionnel. Préciser le réactif limitant.
2.2 Dresser le tableau d'avancement volumique de la réaction.
3. À différentes dates t, on prélève un volume $V_0$ auquel on ajoute de l'eau glacée et on dose le diiode $I_2$ formé par une solution de thiosulfate de sodium $Na_2S_2O_3$. Les résultats ont permis de tracer la courbe d'avancement volumique $y=f(t)$.
3.1 Préciser comment peut-on reconnaître expérimentalement le point d'équivalence.
3.2 Déterminer, à partir de la courbe, la valeur de $[S_2O_8^{2-}]_0$ et déduire les valeurs de $C_1$ et $C_2$.
3.3 Définir la vitesse volumique d'une réaction chimique. Déterminer graphiquement sa valeur à $t=20$ min. Déduire à cette date la vitesse instantanée de la réaction et celle de la disparition de $I^-$.""",

    ("D", "pc", 2023, "sn", 3): r"""Exercice 2 (3,5 pts)
On mélange une mole d'acide éthanoïque et une mole de propan-2-ol en présence d'acide sulfurique pur.
1.1 Écrire l'équation bilan et donner le nom du produit organique obtenu.
1.2 Donner le nom de cette réaction et préciser ses caractéristiques.
1.3 L'acide éthanoïque réagit avec le chlorure de thionyle $SOCl_2$ pour donner un composé organique B. En déduire la formule semi-développée (f.s.d.) et le nom de B.
1.4 On prépare un amide monosubstitué E de formule $C_4H_8ON$ en faisant réagir B avec une amine D. Quelle est la classe de l'amine D ? Donner les noms et f.s.d. de D et E.
2. Solution d'acide éthanoïque de concentration 0,1 mol/L, $pH=2{,}9$.
2.1 Montrer que cet acide est faible et écrire l'équation de sa réaction avec l'eau.
2.2 Calculer le coefficient d'ionisation $\alpha$.
2.3 Déterminer la valeur du $pK_a$ du couple acide éthanoïque-ion éthanoate.""",

    ("D", "pc", 2023, "sn", 4): r"""Exercice 3 (4 pts)
Une particule X ($q=3{,}2.10^{-19}$ C, $m=6{,}68.10^{-27}$ kg) pénètre entre deux plaques A et B ($l=10$ cm, $d=6$ cm). Elle entre en O avec une vitesse $\vec{V_0}$ formant un angle $\alpha$ avec l'horizontale.
1.1 Préciser les signes des armatures et de la tension $U_{BA}$.
1.2 Établir l'équation cartésienne de la trajectoire.
1.3 Déterminer $\alpha$ pour que la particule passe par $O'$.
1.4 Déterminer les coordonnées du point le plus bas de la trajectoire. Données : $E=8350$ V/m ; $V_0=2.10^5$ m/s.
2. La désintégration de ${}_{92}^{232}U$ donne la particule X avec le nucléide ${}_{90}^{228}Th$.
2.1 Écrire l'équation, préciser le type de radioactivité et la nature de X.
2.2 Calculer l'énergie émise en MeV.
2.3 Calculer la constante de désintégration $\lambda$ si la période est 69,8 ans.""",

    ("D", "pc", 2023, "sn", 5): r"""Exercice 4 (5 pts)
Spire carrée ($a=10$ cm) dans une bobine longue.
1.1 Courant constant créant $B=2$ T. Exprimer et calculer le flux magnétique.
1.2 Champ B variant selon la courbe. Quel phénomène apparaît ? Justifier. Exprimer B puis la f.e.m. induite dans les différents intervalles de temps.
2. Vibreur ($N=100$ Hz) avec corde élastique verticale. $a=2$ mm, $C=40$ m/s.
2.1 Équation horaire de O (passe par l'équilibre en sens positif à $t=0$).
2.2 Équation du mouvement d'un point M à $x=30$ cm de O et sa vitesse maximale.
2.3 Comparer les mouvements de M et d'un point N à 50 cm de O.
2.4 Observations avec stroboscope pour $N_e=200$ Hz, 99 Hz et 50 Hz.""",

    # ═══════════════ 2024 SESSION NORMALE (QCM + 4 exos) ═══════════════
    ("D", "pc", 2024, "sn", 1): r"""Q.C.M (2,5 pts)
Indiquer pour chaque numéro de question la ou les réponse(s) exacte(s).
1. L'expression de la vitesse de formation v(P) d'un produit P est :
A. $v(P)=\dfrac{1}{V}\cdot\dfrac{dx}{dt}$
B. $v(P)=\dfrac{dn(P)}{dt}$
C. $v(P)=\dfrac{d[P]}{dt}$
2. La déshydratation intramoléculaire d'un alcool :
A. donne un étheroxyde
B. donne un alcène
C. donne un aldéhyde
3. La valeur du pH d'un acide faiblement ionisé est donnée par :
A. $pH=2(pK_a+\log C)$
B. $pH=\dfrac{1}{2}(pK_a-\log C)$
C. $pH=\dfrac{1}{2}(pK_a+\log C)$
4. Effet photoélectrique possible seulement si :
A. $\nu_{incident}>\nu_{seuil}$
B. $\lambda_{incident}>\lambda_{seuil}$
C. $W_{rayonnement}<W_{extraction}$
5. Valeur de la constante de Rydberg :
A. $R_H=1{,}09.10^7$ m$^{-1}$
B. $R_H=13{,}6$ eV
C. $R_H=1{,}6.10^{-12}$ J""",

    ("D", "pc", 2024, "sn", 2): r"""Exercice 1 (4 pts)
Acide butyrique $CH_3-CH_2-CH_2-COOH$ réagit avec le méthanol ($CH_3OH$) pour donner E.
1.1 Nom systématique de l'acide butyrique.
1.2 Équation bilan (f.s.d.), nom de la fonction de E et nom de E.
1.3 Masse de méthanol pour 330 g d'acide en proportions stœchiométriques.
2. Mélange de volume $V=400$ mL porté à ébullition. Dosage périodique de prélèvements de 1 mL par de la soude à 0,2 mol/L.
2.1 Équation du dosage.
2.2 Volume de soude à $t=0$.
2.3 À 120 h, l'avancement est $x_f=2{,}5$ mol. Calculer le rendement.
3. n mol d'acide dans 500 mL d'eau, $pH=2{,}95$.
3.1 Expressions des concentrations et valeur de n.
3.2 Préparation d'une solution tampon $pH=4{,}9$. Calculer la masse m de soude solide à ajouter. Donnée : $pK_a=4{,}9$.""",

    ("D", "pc", 2024, "sn", 3): r"""Exercice 2 (3,5 pts)
Mélange de $V_1=40$ mL de peroxodisulfate de sodium et $V_2=60$ mL d'iodure de potassium (même concentration $C=2.10^{-1}$ mol/L).
1.1 Équation de la réaction.
1.2 Quantités initiales et réactif limitant.
1.3 Tableau d'avancement molaire.
2. Dosage du diiode formé à diverses dates.
2.1 Vitesse en fonction de la concentration $[I_2]$.
2.2 Déterminer graphiquement la vitesse à $t=45$ s.
2.3 Définir et déterminer graphiquement le temps de demi-réaction.
3. Influence de la température et de la concentration sur la vitesse et $t_{1/2}$.""",

    ("D", "pc", 2024, "sn", 4): r"""Exercice 3 (6 pts)
Rails AB et CD avec tige MN ($m=25$ g, $l=10$ cm) dans $B=0{,}8$ T vertical ascendant.
1.1 Nature du mouvement. Déduire l'intensité si $V=1{,}6$ m/s après 4 cm.
1.2 Tige liée à un ressort ($K=40$ N/m). Allongement x à l'équilibre.
1.3 Générateur remplacé par fil ($R=2\,\Omega$), ressort supprimé. Tige déplacée à $V=6$ m/s. Calculer f.e.m. induite e, intensité et sens du courant ($r_{tige}=1\,\Omega$).
2. Ressort et tige verticaux (Fig 4). Tige écartée de $x_m=5$ cm vers le bas et lâchée sans vitesse.
2.1 Allongement à l'équilibre et équation horaire du mouvement sinusoidal.
2.2 Montrer que le système est conservatif et calculer son énergie mécanique.
3. Onde transversale sur corde ($C=10$ m/s).
3.1 Définir $\lambda$ et la déterminer via le graphe. Déduire N.
3.2 Comparer les mouvements de P et Q distants de 10 cm.
3.3 Calculer l'instant $t_c$ de l'aspect de la corde.""",

    ("D", "pc", 2024, "sn", 5): r"""Exercice 4 (4 pts)
Station ISS ($h=400$ km) autour de la Terre ($M=6.10^{24}$ kg, $R=6400$ km).
1.1 Expression de la force F exercée par la Terre.
1.2 Expression et calcul de la vitesse V.
1.3 Expression et calcul de la période T. Déduire le nombre de tours par jour.
1.4 Expression de l'énergie mécanique du système ($E_p=-\dfrac{mGM}{R+h}$).
2. Injection d'iode ${}_{53}^{131}I$ (émetteur $\beta^-$, $t_{1/2}=8$ jours) de masse $m_0=0{,}8$ g.
2.1 Composition du nucléide.
2.2 Équation de désintégration.
2.3 Nombre de noyaux $N_0$ et activité initiale $A_0$ ($m_{nucl}=2{,}176.10^{-25}$ kg).
2.4 Durée $t_1$ pour que l'activité soit de 20 %. Montrer que $t_1=\dfrac{t_{1/2}}{\ln 2}\cdot\ln\dfrac{A_0}{A(t_1)}$.""",
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
    shutil.copy2(p, BACKUP_DIR / f"json_bac-pre-fill-d-pc-2020-2024-{stamp}.json")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"\n→ {p} mis à jour ({len(updated)} entrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
