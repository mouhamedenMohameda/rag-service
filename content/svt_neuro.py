"""SVT — chapitre « Neurophysiologie » (séries C et D) :
énoncés retranscrits des PDF officiels, avec les documents (figures) découpés dans
le sujet, + corrections croisées avec les corrigés officiels quand ils existent.
Les durées et vitesses sont recalculées (CHECKS en fin de fichier).

Figures : app/public/static/figures/svt/<id>-docN.jpg (chemin public /static/figures/svt/…).

- ENONCES : ``scripts/load_enonces.py svt_neuro --apply``
- CORRECTIONS : ``scripts/load_corrections.py svt_neuro --apply``
Règle : une valeur lue sur un graphique est donnée avec la précision que le graphique permet.
"""

CH = "Neurophysiologie"
FIG = "/static/figures/svt/"

ENONCES: dict[str, dict] = {}
CORRECTIONS: dict[str, dict] = {}


def fig(eid: str, n: int | str, legende: str) -> str:
    return f"![{legende}]({FIG}{eid}-doc{n}.jpg)"


def _add(eid: str, enonce: str, correction: str, chapitres=None, note: str = "") -> None:
    ENONCES[eid] = {"chapitre": CH, "chapitres": list(chapitres or []), "enonce": enonce.strip() + "\n",
                    "note": note, "replace_ocr": True}
    CORRECTIONS[eid] = {"enonce": enonce.strip() + "\n", "correction": correction.strip() + "\n", "note": note}


# ═══════════════════════════════ C 2012 — session normale ═════════════════════

E = "bac-c-2012-sn-svt-ex2"
_add(E, rf"""
**Physiologie nerveuse (7 points)**

On isole deux fibres de calmar reliées entre elles par une synapse (document 2). On les fait plonger dans un liquide physiologique approprié. Une stimulation efficace appliquée en $S_1S_2$ donne lieu aux enregistrements du document 3.

{fig(E, 2, "Document 2 : dispositif — électrodes stimulatrices S1 S2 sur l'axone présynaptique, électrodes réceptrices R1 (axone présynaptique) et R2 (axone postsynaptique), oscillographe à deux voies")}

{fig(E, 3, "Document 3 : tracé 1 (R1) et tracé 2 (R2), ddp en mV en fonction du temps en ms")}

**1.** Analysez et comparez les deux enregistrements obtenus en $R_1$ et $R_2$.

**2.** Quelle est la durée de la propagation de l'influx nerveux entre $R_1$ et $R_2$ d'après l'enregistrement ?

**3.** Cette durée est-elle compatible avec la vitesse de l'influx nerveux mesurée sur une fibre pré- ou postsynaptique, qui est de $10\ \text{{m/s}}$ ? (On précise que la distance $R_1R_2 = 1\ \text{{cm}}$.) Que déduisez-vous ?

**4.** Si la stimulation est portée sur la fibre postsynaptique, obtiendra-t-on les mêmes tracés ? Justifiez votre réponse.

**5.** On utilise une eau de mer sans $Ca^{{2+}}$ à la place du liquide physiologique. Une stimulation de même intensité que celle utilisée lors de la première expérience ne donne que le tracé 1 du document 3. Que peut-on conclure ?

**6.** On injecte à l'aide d'une micropipette des ions $Ca^{{2+}}$ dans la terminaison présynaptique. On obtient, en l'absence de toute stimulation, le tracé 2 du document 3. Expliquez.

**7.** En vous basant sur vos connaissances, résumez le mécanisme de la transmission synaptique.
""", r"""
**1.** Les deux tracés partent du potentiel de repos ($-70\ \text{mV}$) et présentent la même forme : une dépolarisation rapide jusqu'à environ $0\ \text{mV}$, une repolarisation, puis une légère hyperpolarisation avant le retour au potentiel de repos. Ce sont deux **potentiels d'action** de même amplitude (environ $70\ \text{mV}$). Ils diffèrent par le moment où ils apparaissent : le tracé 1 ($R_1$, fibre présynaptique) culmine vers $1\ \text{ms}$ après la stimulation, le tracé 2 ($R_2$, fibre postsynaptique) vers $2{,}3\ \text{ms}$ : le potentiel d'action postsynaptique est **retardé**.

**2.** Le décalage entre les deux potentiels d'action (d'un sommet à l'autre) est d'environ
$$\Delta t \approx 2{,}3 - 1 = 1{,}3\ \text{ms}.$$

**3.** À $10\ \text{m/s}$, l'influx parcourt $1\ \text{cm}$ en
$$t = \dfrac{d}{v} = \dfrac{10^{-2}}{10} = 10^{-3}\ \text{s} = 1\ \text{ms}.$$
La durée mesurée (environ $1{,}3\ \text{ms}$) est **plus longue** : elle n'est pas compatible avec une simple propagation le long des fibres. Le retard supplémentaire (environ $0{,}3\ \text{ms}$) correspond au franchissement de la synapse : c'est le **délai synaptique**, qui traduit une transmission **chimique** du message au niveau de la synapse.

**4.** Non. Une stimulation de la fibre postsynaptique fait naître un potentiel d'action enregistré en $R_2$, mais **aucun** potentiel d'action en $R_1$ : la synapse ne transmet le message que dans un seul sens, de l'élément présynaptique vers l'élément postsynaptique (le neurotransmetteur n'est libéré que par la terminaison présynaptique).

**5.** Sans $Ca^{2+}$ dans le milieu extracellulaire, le potentiel d'action naît et se propage dans la fibre présynaptique (tracé 1), mais il n'est pas transmis à la fibre postsynaptique. On conclut que les ions $Ca^{2+}$ du milieu extracellulaire sont **indispensables à la transmission synaptique**.

**6.** Les ions $Ca^{2+}$ injectés dans la terminaison présynaptique déclenchent, même sans potentiel d'action présynaptique, l'**exocytose** des vésicules et la libération du neurotransmetteur dans la fente synaptique. Celui-ci se fixe sur les récepteurs de la membrane postsynaptique, la dépolarise et fait naître un potentiel d'action postsynaptique (tracé 2). L'entrée de $Ca^{2+}$ dans la terminaison est donc l'étape qui couple l'arrivée du message présynaptique à la libération du neurotransmetteur.

**7.** Mécanisme de la transmission synaptique :
1. arrivée du potentiel d'action à la terminaison présynaptique ;
2. ouverture de canaux à $Ca^{2+}$ et entrée de $Ca^{2+}$ dans la terminaison ;
3. exocytose des vésicules : libération du neurotransmetteur dans la fente synaptique ;
4. diffusion du neurotransmetteur et fixation sur des récepteurs spécifiques de la membrane postsynaptique ;
5. ouverture de canaux ioniques (entrée de $Na^+$) : dépolarisation postsynaptique qui, si elle atteint le seuil, fait naître un potentiel d'action postsynaptique ;
6. inactivation du neurotransmetteur (dégradation enzymatique ou recapture), qui met fin à son action.
""", note="Exercice absent de la base (squelette vide) : énoncé retranscrit du PDF officiel C 2012 session normale. Correction conforme au corrigé officiel pour 1, 3 (conclusion : délai synaptique, transmission chimique), 4 et 5 ; les questions 6 et 7, non traitées par le corrigé, sont rédigées. Question 2 : le corrigé donne 1,6 ms, mais sur le document 3 les sommets des deux potentiels d'action sont à environ 1 ms et 2,3 ms, soit un décalage d'environ 1,3 ms (délai synaptique d'environ 0,3 ms et non 0,6 ms) ; la conclusion est la même. Le corrigé attribue aussi au Ca2+ la dépolarisation postsynaptique et les mouvements de Na+ et K+ : c'est inexact, le Ca2+ agit dans la terminaison présynaptique en déclenchant l'exocytose du neurotransmetteur.")


# ═══════════════════════════════ C 2013 — session normale ═════════════════════

E = "bac-c-2013-sn-svt-ex2"
_add(E, rf"""
**Physiologie nerveuse (6 points)**

Le document 3 schématise le contact synaptique entre deux fibres nerveuses géantes de calmar ($N_1$ et $N_2$) et localise les niveaux d'intervention de l'expérimentateur :
- $S$ = stimulation électrique ;
- $R_1$ et $R_2$ = électrodes réceptrices.

{fig(E, 3, "Document 3 : contact synaptique entre les fibres N1 et N2, stimulation S et électrodes réceptrices R1 (sur N1) et R2 (sur N2)")}

Le document 4 présente une série d'expériences réalisées au niveau de ce contact synaptique.

{fig(E, 4, "Document 4 : expériences 1 à 4 (stimulation en S, microgoutte d'acétylcholine entre N1 et N2 puis dans N2, eau de mer privée de Ca2+) et enregistrements obtenus en R1 et R2")}

**1.** Analysez l'enregistrement obtenu en ①.

**2.** Quel enregistrement obtient-on si la stimulation est portée en $N_2$ ? Justifiez votre réponse.

**3.** Interprétez le résultat de chacune des expériences ②, ③ et ④.

**4.** À partir des informations tirées de ces expériences et de vos connaissances, citez les principales étapes du fonctionnement synaptique.
""", r"""
**1.** Expérience ① (eau de mer, stimulation en $S$) : on enregistre en $R_1$ un potentiel d'action monophasique (passage du potentiel de repos $-70\ \text{mV}$ à environ $0\ \text{mV}$, puis retour), puis en $R_2$ un potentiel d'action de même forme, **avec un léger retard**. Le potentiel d'action né dans $N_1$ (présynaptique) est transmis à $N_2$ (postsynaptique) à travers la synapse ; le retard correspond au temps de propagation et au **délai synaptique**.

**2.** Si la stimulation est portée en $N_2$, on enregistre un potentiel d'action en $R_2$ seulement ; **rien en $R_1$**. La transmission synaptique est **unidirectionnelle** : elle se fait toujours du neurone présynaptique ($N_1$) vers le neurone postsynaptique ($N_2$), car seule la terminaison présynaptique libère le neurotransmetteur et seule la membrane postsynaptique porte les récepteurs.

**3.**
- **Expérience ②** : l'acétylcholine déposée dans la fente synaptique, sans stimulation, fait naître un potentiel d'action en $R_2$ (rien en $R_1$). L'acétylcholine reproduit l'effet du potentiel d'action présynaptique : c'est le **neurotransmetteur** de cette synapse ; elle agit sur la membrane postsynaptique.
- **Expérience ③** : l'acétylcholine injectée à l'intérieur de $N_2$ n'a aucun effet. Elle n'agit donc que sur la **face externe** de la membrane postsynaptique, où se trouvent ses **récepteurs membranaires**.
- **Expérience ④** : sans $Ca^{2+}$ dans le milieu, le potentiel d'action naît en $R_1$ mais n'est pas transmis en $R_2$. Les ions $Ca^{2+}$ extracellulaires sont **indispensables à la transmission synaptique** : ils sont nécessaires à la libération de l'acétylcholine par la terminaison présynaptique.

**4.** Principales étapes du fonctionnement synaptique :
1. arrivée du potentiel d'action à la terminaison présynaptique ;
2. entrée d'ions $Ca^{2+}$ dans la terminaison présynaptique ;
3. exocytose des vésicules : libération d'acétylcholine dans la fente synaptique ;
4. fixation de l'acétylcholine sur ses récepteurs de la membrane postsynaptique ;
5. ouverture de canaux ioniques, entrée de $Na^+$ : **dépolarisation** de la membrane postsynaptique, qui fait naître un potentiel d'action postsynaptique ;
6. destruction de l'acétylcholine (par l'acétylcholinestérase), qui met fin à son action.
""", note="Exercice absent de la base (squelette vide) : énoncé retranscrit du PDF officiel C 2013 session normale. Le bord droit du scan est coupé : le dernier caractère de la question 1 (« ① ») et quelques fins de mots des questions 2 à 4 ont été rétablis d'après le contexte ; le document 3 est légèrement rogné à droite (électrode R2). Correction conforme au corrigé officiel (PA en R1 puis R2 avec retard ; unidirectionnalité ; acétylcholine neurotransmetteur, récepteurs membranaires, Ca2+ indispensable à la libération). Le corrigé écrit « du neurone post synaptique vers le neurone post synaptique » et « hypolarisation » : il faut lire « du neurone présynaptique vers le neurone postsynaptique » et « dépolarisation ».")


# ═══════════════════════════════ C 2014 — session normale ═════════════════════

E = "bac-c-2014-sn-svt-ex2"
_add(E, rf"""
**Physiologie nerveuse (6 points)**

À l'aide d'une cathode, on stimule point par point la surface de deux fibres nerveuses ($A$ et $B$). En fixant la durée de l'excitation, on cherche l'intensité minimale déclenchant la naissance d'un influx nerveux. Les résultats sont résumés par le document 3.

{fig(E, 3, "Document 3 : seuil d'intensité (en µA) en fonction de la distance (en mm) le long des fibres A et B")}

**1.** Commentez ces courbes.

**2.** Déduisez le type des fibres $A$ et $B$ étudiées.

**3.** Schématisez ces deux fibres.

**4.** À quelles structures de la fibre $A$ les points en rapport avec l'intensité minimale correspondent-ils ?

**5.** Précisez le mode de conduction de l'influx nerveux au niveau de chaque type de fibre.
""", r"""
**1.**
- **Fibre $B$** : le seuil d'intensité est le même ($5\ \mu\text{A}$) en tout point : la fibre est également excitable sur toute sa longueur.
- **Fibre $A$** : le seuil varie de façon périodique. Il n'atteint la valeur minimale de $5\ \mu\text{A}$ qu'en des points régulièrement espacés de $1\ \text{mm}$ (à $1$, $2$ et $3\ \text{mm}$) ; entre ces points, il augmente fortement (plus de $20\ \mu\text{A}$ à mi-distance). La fibre $A$ n'est facilement excitable qu'en des points précis.

**2.** La fibre $B$, uniformément excitable, est une fibre **sans myéline** (amyélinique). La fibre $A$, excitable seulement en des points régulièrement espacés, est une fibre **myélinisée** : la gaine de myéline, isolante, rend la membrane peu excitable sauf aux endroits où elle est interrompue.

**3.** Schémas (à dessiner) :
- fibre $B$ : un axone entouré seulement de sa membrane, sans gaine de myéline ;
- fibre $A$ : un axone entouré d'une gaine de myéline formée de manchons successifs (cellules de Schwann), interrompue à intervalles réguliers (ici tous les $1\ \text{mm}$) par des étranglements où la membrane de l'axone est à nu : les nœuds de Ranvier.

**4.** Les points où le seuil est minimal ($5\ \mu\text{A}$) correspondent aux **nœuds de Ranvier**, seules zones où la membrane de l'axone n'est pas recouverte de myéline.

**5.**
- Fibre $B$ (amyélinique) : conduction **continue**, de proche en proche ; le potentiel d'action se régénère en chaque point de la membrane (conduction lente).
- Fibre $A$ (myélinisée) : conduction **saltatoire** ; le potentiel d'action ne naît qu'aux nœuds de Ranvier et « saute » d'un nœud au suivant (conduction rapide).
""", note="Exercice absent de la base (squelette vide) : énoncé retranscrit du PDF officiel C 2014 session normale ; le document 3 est repris de la version dactylographiée qui accompagne le corrigé (plus lisible, mêmes données). Correction conforme au corrigé officiel (A fibre myélinisée, B amyélinique ; minima = nœuds de Ranvier ; conduction saltatoire / de proche en proche).")


# ═══════════════════════════════ C 2017 — session normale ═════════════════════

E = "bac-c-2017-sn-svt-ex2"
_add(E, rf"""
**Physiologie nerveuse (5 points)**

Soit trois neurones $N_1$, $N_2$ et $N_3$ ; leur potentiel de repos est de $-70\ \text{{mV}}$ ; leur niveau critique de dépolarisation est de $-50\ \text{{mV}}$. Chaque PPSE ou PPSI a une amplitude de $10\ \text{{mV}}$, en valeur absolue. Le neurone $N_1$ est excitateur ; le neurone $N_2$ est inhibiteur.

{fig(E, 1, "Chaîne de trois neurones N1, N2, N3 : point A sur l'axone de N1, oscilloscope 1 sur l'axone de N1, 2 sur le corps cellulaire de N2, 3 sur l'axone de N2, point B sur l'axone de N2, 4 sur le corps cellulaire de N3, 5 sur l'axone de N3")}

*NB : tous les oscilloscopes ont une électrode interne.*

On applique une stimulation efficace au point $A$.

**1.** Qu'enregistrera-t-on aux points 1, 2 et 3 ? Pourquoi ?

**2.** On applique une stimulation efficace au point $B$. Qu'enregistrera-t-on aux points 1, 3 et 4 ? Pourquoi ?

On applique 2 stimulations rapprochées et efficaces au point $A$.

**3.** Représentez les réponses obtenues en 1, 2 et 3.

**4.** Quelle est la valeur (en mV) du potentiel membranaire enregistré en 4, et pourquoi ?

**5.** Déduisez la propriété du neurone $N_2$.

On applique 2 stimulations rapprochées et efficaces au point $B$.

**6.** Représentez les réponses obtenues en 4 et 5.
""", r"""
**1.** Stimulation efficace en $A$ :
- en **1** : un **potentiel d'action**, né en $A$ et propagé le long de l'axone de $N_1$ ;
- en **2** : un **PPSE** de $10\ \text{mV}$ (le potentiel passe de $-70$ à $-60\ \text{mV}$), car $N_1$ est excitateur ;
- en **3** : le **potentiel de repos** ($-70\ \text{mV}$). Le PPSE ($-60\ \text{mV}$) n'atteint pas le niveau critique ($-50\ \text{mV}$) : aucun potentiel d'action ne naît dans $N_2$. Un PPSE est local, il ne se propage pas le long de l'axone.

**2.** Stimulation efficace en $B$ (axone de $N_2$) :
- en **1** : le **potentiel de repos** : le message ne franchit pas la synapse $N_1$–$N_2$ en sens inverse (transmission synaptique unidirectionnelle) ;
- en **3** : un **potentiel d'action** : né en $B$, il se propage dans l'axone dans les deux sens et atteint le point 3 ;
- en **4** : un **PPSI** de $10\ \text{mV}$ (hyperpolarisation de $-70$ à $-80\ \text{mV}$), car $N_2$ est inhibiteur.

**3.** Deux stimulations rapprochées en $A$ :
- en **1** : **deux potentiels d'action** successifs ;
- en **2** : les deux PPSE se **somment** (sommation temporelle) : le potentiel atteint $-70 + 10 + 10 = -50\ \text{mV}$, le niveau critique, et un **potentiel d'action** naît dans $N_2$ ;
- en **3** : **un seul potentiel d'action**, propagé le long de l'axone de $N_2$.

**4.** Le potentiel d'action de $N_2$ arrive à la synapse $N_2$–$N_3$ ; $N_2$ étant inhibiteur, il provoque en 4 un **PPSI** de $10\ \text{mV}$ : le potentiel membranaire passe de $-70$ à $-80\ \text{mV}$.

**5.** $N_2$ n'a répondu (potentiel d'action) qu'à la somme de deux PPSE : c'est un neurone **intégrateur**, capable de **sommation temporelle**.

**6.** Deux stimulations rapprochées en $B$ : deux potentiels d'action arrivent à la synapse $N_2$–$N_3$ ;
- en **4** : les deux PPSI se somment : **hyperpolarisation** jusqu'à $-70 - 10 - 10 = -90\ \text{mV}$, puis retour à $-70\ \text{mV}$ ;
- en **5** : le **potentiel de repos** ($-70\ \text{mV}$) : $N_3$, hyperpolarisé, ne produit aucun potentiel d'action.
""", note="Correction conforme au corrigé officiel (1 : PA, PPSE, PR ; 2 : PR, PA, PPSI ; 3 : 2 PA, sommation de 2 PPSE → PA, 1 PA ; 4 : −80 mV ; 5 : N2 intégrateur ; 6 : −90 mV en 4, −70 mV en 5). Dans le corrigé, le tableau de la question 2 est intitulé O1, O2, O3 au lieu des points 1, 3 et 4 demandés, et la justification de la question 1 dit que le PPSE est « propageable » : un PPSE est un potentiel local, non propagé ; corrigé ici.")


# ─────────────────────────────────────────────────────────────────────────────
CHECKS: dict[str, list[str]] = {
    "bac-c-2012-sn-svt-ex2": [
        "close(Rational(1, 100)/10, Rational(1, 1000))",
        "close(Rational(23, 10) - 1, Rational(13, 10)) and close(Rational(13, 10) - 1, Rational(3, 10))",
    ],
    "bac-c-2017-sn-svt-ex2": [
        "-70 + 10 == -60 and -70 + 10 + 10 == -50 and -70 - 10 == -80 and -70 - 10 - 10 == -90",
    ],
}
