"""SVT — chapitre « Reproduction humaine et endocrinologie » (séries C et D) :
énoncés retranscrits des PDF officiels, avec les documents (figures) découpés dans
le sujet, + corrections croisées avec les corrigés officiels quand ils existent.

Les figures sont servies par l'app web : app/public/static/figures/svt/<id>-docN.jpg
(chemin public /static/figures/svt/…, accessible sans session).

- ENONCES : ``scripts/load_enonces.py svt_reproduction --apply``
- CORRECTIONS : ``scripts/load_corrections.py svt_reproduction --apply``
Règle : une réponse qui dépend d'un détail illisible sur le scan n'est pas affirmée ;
la correction dit ce que le document permet d'établir.
"""

CH = "Reproduction humaine et endocrinologie"
FIG = "/static/figures/svt/"

ENONCES: dict[str, dict] = {}
CORRECTIONS: dict[str, dict] = {}


def fig(eid: str, n: int | str, legende: str) -> str:
    return f"![{legende}]({FIG}{eid}-doc{n}.jpg)"


def _add(eid: str, enonce: str, correction: str, chapitres=None, note: str = "") -> None:
    ENONCES[eid] = {"chapitre": CH, "chapitres": list(chapitres or []), "enonce": enonce.strip() + "\n",
                    "note": note, "replace_ocr": True}
    CORRECTIONS[eid] = {"enonce": enonce.strip() + "\n", "correction": correction.strip() + "\n", "note": note}


# ═══════════════════════════════ D 2015 — session normale ═════════════════════

E = "bac-d-2015-sn-svt-ex1"
_add(E, rf"""
**Reproduction (7 points)**

On se propose d'étudier quelques aspects de l'activité sexuelle chez l'espèce humaine.

**A.** Les figures du document 1 représentent des cellules germinales en division au cours de la gamétogenèse. Pour la simplification, on a représenté 3 paires de chromosomes.

{fig(E, 1, "Document 1 : cellules germinales en division (figures a, b, c, d)")}

**1.** Identifiez pour chaque figure, en justifiant votre réponse, le type de gamétogenèse.

**2.** Complétez le tableau 1.

| | Figure a | Figure b | Figure c | Figure d |
|---|---|---|---|---|
| Nom de la cellule | | | | |
| Quantité d'ADN (exprimée en X) | | | | |
| Lieu d'existence | | | | |

*Tableau 1*

**3.** Un autre type de division cellulaire intervient lors de la gamétogenèse. Nommez ce type de division, et précisez son moment de la vie.

**B.** La figure a du document 2 représente une structure ovarienne observée au microscope optique.

{fig(E, 2, "Document 2 : structures observées au microscope (figures a, b, c, d)")}

**1.** Légendez cette structure.

Une coupe d'ovaire réalisée des jours plus tard montre la structure illustrée par la figure b du document 2.

**2.** Donnez un nom à cette structure et décrivez l'évolution qui s'est produite dans l'intervalle de temps qui sépare les figures a et b.

**3.** Les figures c et d du document 2 représentent deux aspects différents d'un même organe sexuel.

a) De quel organe s'agit-il ?

b) Dans quelle phase du cycle cet organe présente :
- l'aspect représenté par la figure c ;
- l'aspect représenté par la figure d.

**C.** Le tableau 2 exprime le résultat de dosage de deux hormones (X et Y) chez une femme :

| | 1 mai | 3 mai | 5 mai | 7 mai | 9 mai | 11 mai | 13 mai | 15 mai | 17 mai | 19 mai | 21 mai | 23 mai | 25 mai | 27 mai | 29 mai | 31 mai |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hormone X | 0,3 | 4 | 11 | 18 | 19 | 17 | 10 | 3 | 0,3 | 0,3 | 0,2 | 0,3 | 0,3 | 0,2 | 0,3 | 0,3 |
| Hormone Y | 25 | 12 | 15 | 17 | 18 | 16,5 | 6 | 3,2 | 3,2 | 3,7 | 4 | 5 | 6 | 8 | 12 | 18 |

*Tableau 2*

**1.** Identifiez les hormones X et Y.

**2.** À quelle date approximative :

a) l'ovulation s'est-elle produite ? Justifiez la réponse.

b) la menstruation est-elle apparue ? Justifiez la réponse.

**3.** Mettez en relation les deux hormones dosées et les figures du document 2.
""", r"""
**A. 1.** Les figures a et c sont des étapes de l'**ovogenèse** : la division est inégale (cytoplasme partagé de façon très inégale, chromosomes en position excentrique, globule polaire visible sur la figure a). Les figures b et d sont des étapes de la **spermatogenèse** : la cellule se divise par un étranglement équatorial en deux cellules de même taille.

**A. 2.** (En prenant X = quantité d'ADN d'une cellule haploïde à chromosomes dupliqués.)

| | Figure a | Figure b | Figure c | Figure d |
|---|---|---|---|---|
| Nom de la cellule | ovocyte II au moment de la fécondation (spermatozoïde à son contact, globule polaire visible) | spermatocyte I en division | ovocyte I en division (métaphase I) | spermatocyte II en division |
| Quantité d'ADN | $\dfrac{3X}{2}$ (ovocyte II : $X$ + noyau du spermatozoïde : $\dfrac{X}{2}$) | $2X$ | $2X$ | $X$ |
| Lieu d'existence | trompe (oviducte) | testicule (tube séminifère) | ovaire | testicule (tube séminifère) |

**A. 3.** La **mitose** (phase de multiplication). Elle a lieu à partir de la puberté et pendant toute la vie pour la spermatogenèse, et pendant la vie fœtale pour l'ovogenèse.

**B. 1.** La figure a est un follicule : 1 = ovocyte I ; 2 = granulosa (cellules folliculaires) ; 3 = thèque interne.

**B. 2.** La figure b est un **corps jaune**. Entre a et b, le follicule mûr a libéré l'ovocyte (ovulation) ; les cellules folliculaires restées dans l'ovaire se sont transformées en cellules lutéales qui forment le corps jaune.

**B. 3. a)** Il s'agit de l'**utérus** (sa muqueuse, l'endomètre).

**b)** Figure c : **phase folliculaire** (muqueuse en développement). Figure d : **phase lutéale** (muqueuse épaisse et très vascularisée, « dentelle utérine »).

**C. 1.** L'hormone X n'est sécrétée qu'entre le 3 et le 15 mai, après le pic de Y : c'est la **progestérone**, produite par le corps jaune. L'hormone Y présente un pic (25 le 1er mai), puis un second plateau pendant que X est élevée, et remonte à partir du 19 mai : c'est l'**œstradiol** (œstrogène).

**C. 2. a)** L'ovulation a eu lieu vers le **2 mai** : juste après le pic d'œstradiol et au moment où la progestérone commence à être sécrétée (formation du corps jaune).

**b)** La menstruation est apparue vers le **15-16 mai** : la progestérone (et l'œstradiol) chutent à leur minimum (régression du corps jaune), ce qui entraîne la destruction de la muqueuse utérine.

**C. 3.**
- L'œstradiol (Y) est sécrété par le follicule (figure a) pendant la phase folliculaire et fait proliférer la muqueuse utérine (figure c).
- Pendant la phase lutéale, le corps jaune (figure b) sécrète la progestérone (X) et de l'œstradiol ; la progestérone, avec l'œstradiol, fait apparaître la dentelle utérine (figure d).
""", note="Correction conforme au corrigé officiel (figure a : le corrigé la nomme « zygote », 3X/2 ; c'est l'ovocyte II en cours de fécondation). Le texte OCR en base avait un tableau 2 faux, remplacé par les valeurs du sujet.")

# ═══════════════════════════════ D 2016 — session normale ═════════════════════

E = "bac-d-2016-sn-svt-ex1"
_add(E, rf"""
**Reproduction (6,5 points)**

Le document 1 représente deux structures (A et B) observables chez une femme pubère.

{fig(E, 1, "Document 1 : structures A et B")}

**1.** Donnez un titre et une légende à chacune de ces structures.

**2.** Précisez le lieu d'observation de ces structures.

**3.** Pour des raisons médicales, Madame A a subi une ovariectomie bilatérale. En justifiant votre réponse, donnez une des conséquences de cette opération :

a) au niveau de son utérus ;

b) au niveau de son hypophyse.

**4.** Madame B présente un retard des règles de 3 semaines. Le test de grossesse positif qu'elle a effectué révèle la présence d'une hormone X dans l'urine.

a) Identifiez l'hormone X.

b) Donnez son origine et son rôle.

**5.** Au cours de la gestation les règles ne réapparaissent pas et le placenta sécrète des hormones qui provoquent le développement des glandes mammaires.

**5.1.** Quelles sont ces hormones ?

**5.2.** Quelle est l'hormone qui manque et qui intervient normalement au cours de la formation du lait ?

**5.3.** Expliquez la non-réapparition des règles pendant la grossesse.

Les femmes paysannes ne suivent pas généralement le « planning familial », pourtant l'écart d'âge de leurs enfants est important. Par contre, les femmes des villes ont souvent recours à des méthodes modernes pour espacer l'âge de leurs enfants.

**6.** À l'aide de vos connaissances, expliquez ces constats.

**7.** Parmi les méthodes principales utilisées par les femmes des villes, on peut citer :
- les pilules combinées ;
- le RU-486.

Donnez les effets de chacune de ces méthodes.
""", r"""
**1.**

| Structure A : follicule mûr (follicule de De Graaf) | Structure B : ovocyte fécondé |
|---|---|
| 1 : paroi du follicule (granulosa, entourée des thèques) | 1 : globules polaires |
| 2 : cavité folliculaire (antrum) | 2 : pronucléus femelle |
| 3 : ovocyte I (bloqué en prophase I) | 3 : pronucléus mâle |

**2.** Structure A : dans l'**ovaire**. Structure B : dans la **trompe** (oviducte).

**3. a)** Atrophie de l'utérus (muqueuse non développée, plus de règles) : les ovaires ne sécrètent plus d'œstrogènes ni de progestérone, qui stimulaient la muqueuse utérine.

**b)** Hypersécrétion de FSH et de LH par l'hypophyse (qui peut s'hypertrophier) : il n'y a plus de rétrocontrôle négatif exercé par les hormones ovariennes.

**4. a)** L'hormone X est l'**HCG** (hormone chorionique gonadotrope).

**b)** Origine : le trophoblaste de l'embryon (futur placenta). Rôle : maintenir le corps jaune, qui continue à sécréter œstrogènes et progestérone au début de la grossesse.

**5.1.** Les œstrogènes, la progestérone et l'hormone lactogène placentaire (HPL).

**5.2.** La **prolactine** (hormone hypophysaire).

**5.3.** Le taux élevé et constant d'œstrogènes et de progestérone (corps jaune puis placenta) maintient la muqueuse utérine développée (pas de règles) et bloque par rétrocontrôle négatif la sécrétion de FSH et LH : pas de nouveau cycle.

**6.** Les femmes paysannes allaitent longtemps et souvent. La tétée stimule la sécrétion de prolactine, qui freine la sécrétion de GnRH, donc de FSH et LH : il n'y a pas d'ovulation pendant cette période, ce qui espace naturellement les naissances.

**7.**
- **Pilule combinée** (œstrogène + progestatif de synthèse) : rétrocontrôle négatif sur l'hypothalamus et l'hypophyse, donc pas de pic de LH et pas d'ovulation ; elle rend aussi la muqueuse utérine impropre à la nidation et la glaire cervicale imperméable aux spermatozoïdes.
- **RU-486** (mifépristone, anti-progestérone) : il bloque l'action de la progestérone sur l'utérus, ce qui empêche la nidation ou interrompt une grossesse débutante.
""", note="Correction conforme au corrigé officiel. Légende 1 de la structure A : le corrigé indique « granulosa » ; sur le scan la flèche pointe la paroi du follicule (granulosa et thèques), la correction le dit ainsi. 3 b) : le corrigé écrit « hypertrophie de l'hypophyse » ; la conséquence établie est l'hypersécrétion de FSH et LH.")


# ═══════════════════════════════ D 2017 — session normale ═════════════════════

E = "bac-d-2017-sn-svt-ex1"
_add(E, rf"""
**Reproduction (7 points)**

**A.** Le document 1 montre trois événements $A$, $B$ et $C$ pouvant se produire chez une femme $F_1$.

{fig(E, 1, "Document 1 : appareil génital féminin, structures 1, 2, 3, X, Y et événements A, B, C")}

**1.** Donnez la légende qui correspond aux numéros et nommez les événements $A$, $B$ et $C$.

**2.** La structure $X$ sécrète une hormone $H_1$ qui stimule la structure $Y$ à sécréter deux hormones $H_2$ et $H_3$ indispensables à l'événement $A$. Identifiez l'hormone $H_1$ et précisez son rôle.

**3.** L'hormone $H_3$ est à l'origine du déclenchement de l'événement $B$. Après avoir identifié l'hormone $H_3$, expliquez son rôle dans le déterminisme de cet événement.

**4.** Précisez le(s) effet(s) exercé(s) par $H_2$ et $H_3$ pendant la période qui débute par l'événement $A$.

**5.** Chez une autre femme $F_2$, l'événement $A$ ne peut se dérouler : son médecin lui annonce sa stérilité. Citez deux causes probables de cette stérilité.

**6.** Afin de tester l'une des deux causes précitées, le médecin injecte à cette femme ($F_2$) un liquide opaque au niveau du col utérin et constate que ce liquide ne se répand pas au niveau de ses ovaires.

a) Qu'apporte ce résultat ?

b) À votre avis, comment la stérilité de cette femme peut-elle être remédiée ?

**B.** Chez deux femmes $F_3$ et $F_4$ stériles, le taux plasmatique maximal d'œstradiol ne dépasse jamais $190\ \text{{pg·mL}}^{{-1}}$, alors qu'il est de $480\ \text{{pg·mL}}^{{-1}}$ au $12^{{\text{{e}}}}$ jour du cycle chez une femme normale.

**1.** Proposez la ou les cause(s) probable(s) du taux faible d'œstradiol chez $F_3$ et $F_4$.

**2.** Quelle conséquence aura-t-elle sur l'événement $B$ ? Justifiez.

Le dosage d'œstradiol chez ces deux femmes suite à un traitement par l'injection d'une substance $S$ permet d'obtenir le document 2.

{{fig(E, 2, "Document 2 : taux d'œstradiol (pg/mL) chez F3 et F4, injection de S au jour 3")}}

**3.** Analysez ce document. Déduisez l'effet de la substance $S$.

**4.** Quelle est la cause confirmée de la stérilité de chacune des deux femmes ?

**5.** Proposez un remède pour la stérilité de $F_3$ et $F_4$.
""", r"""
**A. 1.** Légendes : 1 = corps jaune ; 2 = follicule (avec son ovocyte) ; 3 = endomètre (muqueuse utérine).

Événements : $A$ = **nidation** (implantation de l'embryon $X$ dans l'endomètre) ; $B$ = **ovulation** (expulsion de l'ovocyte hors du follicule) ; $C$ = **fécondation** (dans la trompe).

**A. 2.** $H_1$ est l'**HCG** (hormone chorionique gonadotrope), sécrétée par le trophoblaste de l'embryon. Rôle : elle maintient le corps jaune ($Y$) et le transforme en corps jaune gestatif, qui continue à sécréter œstrogènes et progestérone ($H_2$, $H_3$) : la muqueuse utérine est conservée et la nidation possible.

**A. 3.** $H_3$ est l'**œstradiol**. En fin de phase folliculaire, le follicule mûr en sécrète une quantité élevée ; ce taux élevé exerce un **rétrocontrôle positif** sur le complexe hypothalamo-hypophysaire, qui libère un **pic de LH** (et de FSH). Ce pic de LH déclenche l'ovulation environ 36 heures plus tard.

**A. 4.** Pendant la grossesse (période qui débute par la nidation), la progestérone ($H_2$) et les œstrogènes ($H_3$) :
- maintiennent la muqueuse utérine développée et favorable à la gestation (pas de règles ; la progestérone réduit les contractions utérines) ;
- exercent un rétrocontrôle négatif sur l'hypothalamus et l'hypophyse : pas de pic de LH, donc pas de nouveau cycle ni d'ovulation ;
- préparent le développement des glandes mammaires.

**A. 5.** Causes probables : une cause **anatomique** (obstruction des trompes, qui empêche la rencontre des gamètes ; malformation de l'utérus) ou une cause **hormonale** (sécrétion insuffisante de progestérone, muqueuse non préparée à la nidation).

**A. 6. a)** Le liquide injecté dans l'utérus n'atteint pas les ovaires : les trompes sont **obstruées**. Les spermatozoïdes ne peuvent pas rejoindre l'ovocyte : la stérilité est d'origine anatomique.

**b)** Par la **FIVETE** (fécondation in vitro et transfert d'embryon) : les ovocytes prélevés sont fécondés au laboratoire et l'embryon est placé directement dans l'utérus, sans passer par les trompes.

**B. 1.** Un taux faible d'œstradiol traduit une croissance folliculaire incomplète. Causes probables : un **déficit hormonal** (sécrétion insuffisante de GnRH ou de FSH) ou une **insensibilité de l'ovaire** à la FSH (absence de récepteurs à la FSH sur les follicules).

**B. 2.** Sans taux élevé d'œstradiol, il n'y a pas de rétrocontrôle positif sur l'hypothalamus et l'hypophyse, donc **pas de pic de LH** et **pas d'ovulation** (l'événement $B$ ne se produit pas).

**B. 3.** Avant l'injection de $S$ (jours 1 à 3), le taux d'œstradiol est faible et identique chez les deux femmes (environ $100$ à $200\ \text{pg/mL}$).

Après l'injection :
- chez $F_3$, il augmente fortement (plus de $500\ \text{pg/mL}$ au jour 5) puis se maintient vers $450\ \text{pg/mL}$, une valeur proche de la normale ;
- chez $F_4$, il ne varie presque pas et redescend même vers $120\ \text{pg/mL}$.

$S$ stimule la croissance des follicules et leur sécrétion d'œstradiol quand l'ovaire est capable d'y répondre : $S$ a une action de type **FSH**.

**B. 4.**
- $F_3$ : ses ovaires répondent à $S$ ; sa stérilité est due à un **manque de FSH** (déficit hypothalamo-hypophysaire).
- $F_4$ : ses ovaires ne répondent pas à $S$ ; sa stérilité est due à une **insensibilité ovarienne** (absence de récepteurs à la FSH).

**B. 5.**
- $F_3$ : traitement hormonal par injections de FSH (puis LH ou HCG pour déclencher l'ovulation).
- $F_4$ : aucun traitement hormonal n'est efficace ; seule une procréation médicalement assistée avec don d'ovocytes est envisageable.
""", note="Correction conforme au corrigé officiel (1 = corps jaune, 2 = follicule mûr, 3 = endomètre ; H1 = HCG ; H3 = œstradiol ; F3 : manque de FSH, F4 : absence de récepteurs). Le corrigé appelle 2 « follicule mûr » ; sur le schéma c'est un follicule contenant son ovocyte, la correction écrit « follicule ».")

# ═══════════════════════════════ D 2018 — session normale ═════════════════════

E = "bac-d-2018-sn-svt-ex3"
_add(E, rf"""
**Exercice 2 (8 points)**

La stérilité chez la femme est liée à plusieurs causes dont certaines peuvent être corrigées.

**A.** Mme A consulte son médecin pour un problème de stérilité. Il lui demande de prendre sa température corporelle quotidienne durant 30 jours. Les résultats obtenus sont représentés par la courbe du document 1.

{{fig(E, 1, "Document 1 : température corporelle (°C) de Mme A pendant 30 jours")}}

**1.** À partir de l'analyse de ce document, déterminer l'événement manquant chez Mme A.

Le gynécologue suppose que la stérilité de Madame A est liée soit à un manque de stimulation des ovaires par l'hypophyse (hypothèse 1), soit à une insensibilité des ovaires aux sécrétions hypophysaires (hypothèse 2).

**2.** Justifier les deux hypothèses formulées par le médecin.

Le médecin demande à Mme A de réaliser une échographie avec biopsie de ses ovaires ainsi que des dosages hormonaux. L'échographie révèle deux ovaires de taille normale alors que la biopsie réalisée à diverses reprises ne présente que des follicules primaires.

Les résultats des dosages hormonaux chez Mme A concernant les hormones hypophysaires (LH et FSH) et les hormones ovariennes montrent des concentrations nettement plus faibles que celles d'une femme à cycle normal.

**3.** Ces résultats permettent-ils de valider l'hypothèse 2 ? Justifiez.

Le médecin est conduit à pratiquer un traitement qui consiste à injecter de la FSH. Les dosages d'œstradiol sont réalisés durant la période 1 (sans traitement) et durant la période 2 (sous traitement). Les résultats obtenus sont consignés dans le tableau (le traitement débute au jour 7 de la période 2) :

| Temps (jours) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Période 1 : œstradiol (pg/mL) | 200 | 200 | 200 | 200 | 200 | 200 | 220 | 240 | 240 | 240 | 240 |
| Période 2 : œstradiol (pg/mL) | 200 | 200 | 200 | 200 | 200 | 200 | 220 | 400 | 600 | 700 | 950 |

**4.** Qu'apportent ces résultats à propos de la cause de stérilité chez Mme A ?

**5.** Suite à ce traitement, le contrôle régulier de la croissance des follicules ovariens par échographie a donné le résultat présenté par le document 2.

{{fig(E, 2, "Document 2 : ovaire de Mme A sous traitement (structures A, B, C)")}}

a) Identifiez les structures $A$, $B$ et $C$.

b) Ce traitement a-t-il résolu la stérilité de Mme A ? Justifier.

c) À partir de ces données, proposer une explication aux taux de FSH et LH constatés chez Madame A avant son traitement.

d) Comparez l'aspect de cet ovaire avec celui d'une femme à cycle normal.

e) Donnez une explication aux différences constatées.

**B.** Madame B présente une autre forme de stérilité ; après des analyses, son médecin lui propose un remède basé sur un protocole simplifié par le schéma du document 3.

{{fig(E, 3, "Document 3 : protocole sur les jours du cycle (opérations 1 à 5)")}}

*Légende du document 3 :* 1 = injection d'un analogue de GnRH ; 2 = injection de FSH ; 3 = dosages d'œstradiol ; 4 = injection de HCG ; 5 = ponction d'ovocytes. *D'après le schéma :* l'opération 1 couvre les jours 2 à 12, l'opération 2 les jours 3 à 11, l'opération 3 les jours 7 à 14 ; l'opération 4 a lieu au jour 14 et l'opération 5 au jour 15.

**1.** Nommez cette assistance médicale.

**2.** Quelle est la cause de stérilité la plus probable chez madame B ?

**3.** Dans quel but est réalisée chacune des opérations 1, 2, 3, 4 et 5 ?
""", r"""
**A. 1.** La température reste comprise entre $36$ et $36{,}5\ °\text{C}$ pendant les 30 jours, avec de petites oscillations, sans plateau élevé. Il n'y a pas de décalage thermique (élévation d'environ $0{,}5\ °\text{C}$ due à la progestérone après l'ovulation) : l'événement manquant est l'**ovulation**.

**A. 2.** L'ovulation nécessite une croissance folliculaire, stimulée par la FSH, puis un pic de LH, tous deux d'origine hypophysaire.
- Hypothèse 1 : si l'hypophyse ne sécrète pas (ou pas assez) de FSH et de LH, les follicules ne se développent pas et il n'y a pas d'ovulation.
- Hypothèse 2 : si les ovaires ne répondent pas à la FSH et à la LH (absence de récepteurs), même avec une hypophyse normale il n'y a ni croissance folliculaire ni ovulation.

**A. 3.** Non. Si les ovaires étaient insensibles (hypothèse 2), ils ne sécréteraient presque pas d'hormones ovariennes et, en l'absence de rétrocontrôle négatif, l'hypophyse sécréterait **beaucoup** de FSH et de LH. Or les taux de FSH et de LH sont **faibles** : l'hypothèse 2 n'est pas validée ; les résultats sont compatibles avec l'hypothèse 1 (manque de stimulation hypophysaire).

**A. 4.** Sans traitement, l'œstradiol reste faible (200 à 240 pg/mL). Avec la FSH, il augmente fortement à partir du jour 8 (de 220 à 950 pg/mL) : les follicules se développent et sécrètent de l'œstradiol. Les ovaires de Mme A **répondent à la FSH** : ils sont normaux, l'hypothèse 2 est rejetée. La stérilité est due à un **manque de FSH** (hypothèse 1).

**A. 5. a)** $B$ : **follicule mûr** (de De Graaf), le plus gros, avec une grande cavité. $A$ : follicule tertiaire (cavitaire) ; $C$ : follicule secondaire (plein), plus petits et en croissance.

**b)** Oui, la cause de la stérilité est corrigée : sous FSH, les follicules primaires reprennent leur croissance jusqu'au stade de follicules mûrs, capables d'ovuler. La fécondation redevient possible.

**c)** Avant le traitement, les follicules restaient au stade primaire et sécrétaient très peu d'œstradiol. Les faibles taux de FSH et de LH viennent d'un **défaut de sécrétion de l'hypophyse** (ou de l'hypothalamus) : c'est la cause primitive de la stérilité, et non une conséquence des faibles taux d'hormones ovariennes.

**d)** Chez une femme à cycle normal, un seul follicule (le follicule dominant) arrive à maturité à chaque cycle. L'ovaire de Mme A traitée présente **plusieurs follicules mûrs** en même temps.

**e)** Dans un cycle normal, la FSH sécrétée diminue en cours de phase folliculaire (rétrocontrôle négatif exercé par l'œstradiol) : seul le follicule le plus sensible continue sa croissance. Ici, la FSH est injectée à dose élevée et n'est pas soumise à ce rétrocontrôle : plusieurs follicules sont stimulés en même temps.

**B. 1.** C'est la **FIVETE** (fécondation in vitro et transfert d'embryon).

**B. 2.** La cause la plus probable est une **obstruction des trompes** : les ovaires fonctionnent (on les stimule et on ponctionne les ovocytes), mais la fécondation est réalisée hors de l'organisme, ce qui contourne les trompes.

**B. 3.**
- **1** (analogue de GnRH) : bloquer le fonctionnement de l'hypophyse et le cycle naturel de la femme, pour contrôler entièrement le cycle (cycle artificiel, pas d'ovulation spontanée).
- **2** (FSH) : stimuler la croissance de plusieurs follicules à la fois.
- **3** (dosages d'œstradiol) : suivre la croissance et la maturité des follicules (l'œstradiol est sécrété par les follicules en croissance).
- **4** (HCG, à action de type LH) : déclencher la maturation finale et l'ovulation de plusieurs follicules mûrs.
- **5** (ponction) : recueillir les ovocytes juste avant l'ovulation pour les féconder in vitro avec les spermatozoïdes.
""", note="Correction croisée avec le corrigé officiel (ovulation absente ; FSH : ovaires normaux ; A tertiaire, B mûr, C secondaire ; FIVETE, trompes obstruées ; buts des opérations 1 à 5). Différences : en 3, le corrigé dit que les résultats « ne confirment aucune hypothèse » ; des FSH et LH faibles excluent en fait l'hypothèse 2 (une insensibilité ovarienne donnerait des FSH/LH élevées) — c'est ce qu'écrit la correction. En 5 b, le corrigé parle de « follicules rompus » ; le document montre des follicules mûrs, la correction s'en tient à ce que montre le document. En 5 c, le corrigé attribue les faibles FSH/LH à un rétrocontrôle négatif des faibles œstrogènes ; un taux faible d'œstrogènes lève au contraire ce rétrocontrôle, la correction attribue donc ces taux à un défaut de sécrétion hypophysaire.")


# ═══════════════════════════════ D 2019 — session normale ═════════════════════

E = "bac-d-2019-sn-svt-ex3"
_add(E, rf"""
**Exercice 3 (5,25 points)**

**A.** Les figures 1, 2 et 3 illustrent des étapes d'un phénomène qui se déroule dans les voies génitales d'une femelle de mammifères.

{fig(E, 1, "Figures 1, 2 et 3 : étapes du phénomène (éléments A, B, C, D, E)")}

**1.** De quel phénomène s'agit-il ?

**2.** Donnez les noms des éléments $A$, $B$, $C$, $D$ et $E$.

**3.** Précisez la quantité d'ADN et la formule chromosomique des éléments $A$, $B$, $C$, $D$ et $E$ en considérant $2n = 4$ (une paire d'autosomes et la paire des gonosomes). Votre réponse doit être sous forme d'un tableau.

**4.** Des ovules de souris sont fécondés in vitro, mais au stade de la figure 3, on aspire l'élément $A$ ou $B$. On fait alors agir la cytochalasine B, qui permet le dédoublement strict des chromosomes. La cellule ainsi obtenue peut se diviser et l'embryon qui en résulte est implanté dans l'utérus d'une souris porteuse. Seuls les embryons à caryotype normal sont viables.

a) Décrivez l'état de l'utérus de la femelle porteuse au moment de l'implantation.

b) Peut-on prévoir le sexe des souriceaux ? Justifier votre réponse en envisageant les divers cas possibles.

**B.** Afin de préciser la relation entre deux hormones $X$ et $Y$, on dose la concentration moyenne de l'hormone $X$ chez une femme ayant des cycles de 28 jours, dans des conditions différentes :
- a : cycle normal ;
- b : cycle fécond ;
- c : cycle normal avec injections de l'hormone $Y$ du $J_{{+6}}$ au $J_{{+9}}$ du cycle.

Le tableau suivant présente les résultats obtenus dans les trois conditions.

| Jours | $J_{{-1}}$ | $J_0$ | $J_{{+1}}$ | $J_{{+3}}$ | $J_{{+6}}$ | $J_{{+8}}$ | $J_{{+11}}$ | $J_{{+13}}$ | $J_{{+14}}$ | $J_{{+17}}$ | $J_{{+20}}$ | $J_{{+22}}$ | $J_{{+30}}$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Normal (a) | trace | 0,5 | 2 | 7 | 17 | 19 | 12 | 2 | trace | trace | trace | trace | trace |
| Fécond (b) | trace | 0,5 | 2 | 7 | 17 | 19,5 | 23 | 27 | 29 | 31 | 33 | 35 | 40 |
| Avec injections de Y (c) | trace | 0,5 | 2 | 7 | 17 | 24 | 27 | 24 | 20 | 10 | 2 | trace | trace |

**1.** Identifiez l'hormone $X$, précisez son origine dans chaque cycle.

**2.** Déduisez le rôle de l'hormone $Y$ et nommez-la.

**3.** Précisez la date des événements constatés dans chaque cycle.

**4.** Précisez les types de rétrocontrôles exercés aux jours $J_{{-1}}$ et $J_{{+20}}$. Citez à chaque fois leurs conséquences.
""", r"""
**A. 1.** Il s'agit de la **fécondation** (rencontre et fusion des gamètes dans la trompe).

**A. 2.** D'après le corrigé officiel (les flèches du scan sont peu lisibles) :

| Élément | A | B | C | D | E |
|---|---|---|---|---|---|
| Nom | pronucléus femelle | pronucléus mâle | 2ᵉ globule polaire | cellule folliculaire | 1ᵉʳ globule polaire |

**A. 3.** On note $Q$ la quantité d'ADN d'une cellule diploïde avant réplication ($2n = 4$ chromosomes à une chromatide). Les pronucléus répliquent leur ADN avant de fusionner.

| Élément | A | B | C | D | E |
|---|---|---|---|---|---|
| Formule chromosomique | $n = 1 + X$ | $n = 1 + X$ ou $n = 1 + Y$ | $n = 1 + X$ | $2n = 2 + XX$ | $n = 1 + X$ |
| Quantité d'ADN | $Q$ | $Q$ | $\dfrac{Q}{2}$ | $Q$ | $Q$ |

($C$, 2ᵉ globule polaire : chromosomes à une chromatide ; $E$, 1ᵉʳ globule polaire : chromosomes à deux chromatides.)

**A. 4. a)** Au moment de l'implantation, la muqueuse utérine de la femelle porteuse doit être en phase lutéale : **épaisse, très vascularisée, avec des glandes développées (dentelle utérine)**, et le muscle utérin au repos (peu de contractions).

**b)** Oui : tous les souriceaux nés seront des **femelles**.
- Si on aspire le pronucléus mâle $B$ : il reste le pronucléus femelle $(1 + X)$ ; après dédoublement, $2 + XX$ : femelle.
- Si on aspire le pronucléus femelle $A$ : il reste le pronucléus mâle, $(1 + X)$ ou $(1 + Y)$. Après dédoublement : $2 + XX$ (femelle) ou $2 + YY$, caryotype anormal non viable.

Seuls les embryons $XX$ se développent.

**B. 1.** $X$ apparaît après $J_0$ (ovulation) et atteint des valeurs élevées : c'est la **progestérone**. Son origine :
- cycle normal (a) : le corps jaune (cyclique) ;
- cycle fécond (b) : le corps jaune gestatif (puis le placenta) ;
- cycle (c) : le corps jaune, maintenu temporairement par les injections.

**B. 2.** Avec les injections de $Y$ ($J_{+6}$ à $J_{+9}$), la progestérone augmente plus que dans le cycle normal ($24$ et $27$ contre $19$ et $12$) et sa chute est retardée : $Y$ **stimule et maintient le corps jaune**. C'est l'**HCG** (hormone chorionique gonadotrope, à action de type LH).

**B. 3.**
- Cycle normal (a) : ovulation à $J_0$ ; menstruation vers $J_{+13}$–$J_{+14}$, quand la progestérone n'est plus qu'à l'état de traces.
- Cycle fécond (b) : ovulation à $J_0$, fécondation dans les 24 h qui suivent ($J_{+1}$), nidation vers $J_{+7}$ ; la progestérone continue d'augmenter (pas de menstruation).
- Cycle (c) : ovulation à $J_0$ ; menstruation retardée, vers $J_{+20}$–$J_{+22}$, quand la progestérone retombe à l'état de traces.

**B. 4.**

| Cycle | Jour | Rétrocontrôle | Conséquence |
|---|---|---|---|
| Normal (a) | $J_{-1}$ | positif (taux élevé d'œstradiol) | pic de LH, ovulation |
| | $J_{+20}$ | négatif (œstradiol sécrété par les follicules en croissance : $J_{+20}$ est le 6ᵉ jour du cycle suivant, en phase folliculaire) | sécrétion de FSH et LH limitée (un seul follicule poursuit sa croissance) |
| Fécond (b) | $J_{-1}$ | positif | pic de LH, ovulation |
| | $J_{+20}$ | négatif (progestérone et œstradiol élevés) | sécrétion de FSH et LH freinée : pas de nouveau cycle |
| Avec Y (c) | $J_{-1}$ | positif | pic de LH, ovulation |
| | $J_{+20}$ | négatif levé (progestérone en chute) | augmentation de la FSH, nouveau cycle |
""", note="Correction croisée avec le corrigé officiel. Les noms A–E viennent du corrigé (flèches du scan peu lisibles), ce que dit la correction. Différences : en B.4 le corrigé écrit « RC⁻ » à J−1 pour le cycle normal tout en citant « pic de LH, ovulation » (coquille : c'est un rétrocontrôle positif) . En B.3, le tableau ne permet qu'une date approchée des menstruations (J+13–J+14 et J+20–J+22).")


# ═══════════════════════════════ D 2023 — session normale ═════════════════════

E = "bac-d-2023-sn-svt-ex4"
_add(E, rf"""
**Exercice 2 (5 points)**

Aïcha, élève de la 7ᵉ SN, essaie d'expliquer à sa sœur, mariée et enceinte, quelques aspects de la reproduction chez l'espèce humaine.

Dans ce but, elle se base sur les figures du document ci-contre observées chez une femme.

{fig(E, 1, "Figure 1 : phénomènes X, Y, Z et W ; figure 2 : schémas 1, 2 et 3")}

**1.** Nommer les phénomènes $X$, $Y$, $Z$ et $W$ en les classant selon l'ordre chronologique.

**2.** Donner un titre pour chaque schéma de la figure 2.

**3.** Nommer l'hormone qui déclenche le phénomène $X$ et celle qui marque le phénomène $Y$.

**4.** Une échographie réalisée chez la sœur d'Aïcha a révélé l'existence de deux embryons et d'un seul corps jaune.

a) Comment expliquer ce phénomène ?

b) Ces embryons peuvent-ils être de sexes différents ? Justifier.

**5.** Au terme de la grossesse de la sœur d'Aïcha, on assiste à la chute d'une hormone $H_1$ suite à l'effet d'une autre hormone $H_2$.

a) Identifier $H_1$ et $H_2$.

b) Rappeler le(s) rôle(s) de l'hormone $H_1$ pendant la gestation et préciser le rôle cité de l'hormone $H_2$.

**6.** Afin d'espacer les naissances, Aïcha conseille à sa sœur de faire recours à une méthode contraceptive à base de $H_1$. Citer trois choix possibles et leur(s) niveau(x) d'action en remplissant le tableau suivant.

| | Choix 1 : … | Choix 2 : … | Choix 3 : … |
|---|---|---|---|
| Niveau a : … | | | ✕ |
| Niveau b : … | | | ✕ |
| Niveau c : … | | ✕ | |

*(✕ : case barrée sur le sujet.)*
""", r"""
**1.** $X$ = **ovulation** (expulsion de l'ovocyte hors du follicule) ; $Y$ = **nidation** (implantation du blastocyste dans l'endomètre) ; $Z$ = **fécondation** (ovocyte entouré de spermatozoïdes, avec les deux pronucléus) ; $W$ = **menstruation** (destruction de la muqueuse utérine).

Ordre chronologique : $W \to X \to Z \to Y$ (menstruation au début du cycle, ovulation, fécondation, puis nidation environ une semaine plus tard).

**2.** Schéma 1 : embryon au stade **2 blastomères** (première division de la cellule-œuf) ; schéma 2 : **blastocyste** ; schéma 3 : **morula**.

**3.** L'ovulation ($X$) est déclenchée par le **pic de LH**. La nidation ($Y$) est marquée par l'apparition de l'**HCG**, sécrétée par le trophoblaste.

**4. a)** Deux embryons pour un seul corps jaune : une seule ovulation, donc une seule cellule-œuf, qui s'est séparée en deux au début du développement. Ce sont de **vrais jumeaux** (jumeaux monozygotes).

**b)** Non : ils proviennent de la même cellule-œuf et ont le même patrimoine génétique, donc les mêmes chromosomes sexuels. Ils sont obligatoirement de **même sexe**.

**5. a)** $H_1$ = **progestérone** ; $H_2$ = **cortisol** (sécrété en fin de grossesse).

**b)** Rôles de la progestérone pendant la gestation :
- maintien de la muqueuse utérine développée (dentelle utérine) ;
- **silence utérin** (elle inhibe les contractions du myomètre) ;
- inhibition des cycles par **rétrocontrôle négatif** sur l'hypothalamus et l'hypophyse.

Rôle du cortisol : il fait chuter la progestérone (en favorisant sa transformation en œstrogènes au niveau du placenta). La levée du silence utérin permet les **contractions utérines** de l'accouchement.

**6.** Niveaux d'action : a = **endomètre**, b = **col de l'utérus** (glaire cervicale), c = **complexe hypothalamo-hypophysaire**.

| | Choix 1 : pilule combinée | Choix 2 : micropilule | Choix 3 : pilule séquentielle |
|---|---|---|---|
| a : endomètre | développement anormal, pas de dentelle : pas de nidation | développement anormal : pas de nidation | ✕ |
| b : col de l'utérus | glaire épaisse, imperméable aux spermatozoïdes : pas de fécondation | glaire imperméable : pas de fécondation | ✕ |
| c : complexe hypothalamo-hypophysaire | rétrocontrôle négatif : pas de pic de LH, pas d'ovulation | ✕ | rétrocontrôle négatif : pas d'ovulation |

(Les niveaux a et b peuvent être inversés.)
""", note="Correction conforme au corrigé officiel (W–X–Z–Y ; 2 blastomères, blastocyste, morula ; LH et HCG ; vrais jumeaux ; H1 progestérone, H2 cortisol ; pilule combinée, micropilule, pilule séquentielle).")

# ═══════════════════════════════ D 2024 — session normale ═════════════════════

E = "bac-d-2024-sn-svt-ex2"
_add(E, rf"""
**Exercice 1 (6 points)**

**A.** Les schémas du document ci-contre représentent des étapes d'un phénomène observé chez l'espèce humaine.

{fig(E, 1, "Document : étapes A, B et C (éléments 1 à 8)")}

**1.** Annotez ce document.

**2.** Classer les étapes $A$, $B$ et $C$ dans leur ordre chronologique.

**3.** On considère volontairement $2n = 4$, dont une paire de gonosomes. Soit un gène $G = B/b$ porté par le chromosome $X$. Sachant que ce phénomène est étudié chez un couple dont la mère est de phénotype $[b]$ et le père de phénotype $[B]$ pour ce gène, complétez le tableau ci-contre :

| Élément | 2 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|
| Formule chromosomique | | | | | |
| Nombre d'allèle(s) de $G$ | | | | | |
| Type d'allèle(s) de $G$ | | | | | |

**B.** On dose à partir du $14^{{\text{{e}}}}$ jour du cycle la concentration plasmatique d'une hormone $H$ (en ng/mL) chez une femme ayant des cycles de 28 jours, dans quatre situations différentes ($A$, $B$, $C$ et $D$) :
- $A$ = cycle fécond ;
- $B$ = cycle normal ;
- $C$ = cycle avec injection d'une substance placentaire $X$ du jour 20 au jour 25 ;
- $D$ = cycle avec injection d'une substance synthétique $Y$ du jour 18 au jour 21.

Des événements $E_1$, $E_2$, $E_3$ et $E_4$ peuvent être constatés pendant cette période :
- $E_3$ est constaté dans les quatre situations ;
- $E_2$ et $E_1$ sont caractéristiques de la situation $A$ ;
- $E_4$ est commun aux situations $B$, $C$ et $D$ mais apparaît à des temps différents selon chaque situation.

| Jours | 14 | 16 | 18 | 21 | 23 | 26 | 28 | 32 | 35 | 38 | 42 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Cycle A | trace | 7 | 11 | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 43 |
| Cycle C | trace | 7 | 11 | 18 | 20 | 23 | 27 | 16 | 3 | trace | trace |
| Cycles B et D | trace | 7 | 11 | 18 | 14 | 5 | trace | trace | trace | trace | trace |

**1.** Représenter la variation de l'hormone $H$ dans la situation $B$ et identifier cette hormone.

**2.** Nommer les événements $E$, sachant que l'événement $E_1$ nécessite un silence utérin.

**3.** L'événement $E_4$ peut être constaté aux jours 22, 28 et 37 selon la situation.

a) Faites une correspondance entre ces temps (jours) et les différentes situations.

b) Déduisez le nom des substances $X$ et $Y$.

**4.** À partir de ces données et de vos connaissances, élaborer un schéma bilan montrant les interactions hormonales survenues au cours du cycle fécond (du $J_{{21}}$ au $J_{{42}}$).
""", r"""
**A. 1.** Le document montre la fécondation et le début du développement :
1 = cellule folliculaire (de la corona radiata) ; 2 = spermatozoïde ; 3 = 1ᵉʳ globule polaire ; 4 = 2ᵉ globule polaire ; 5 = chromosomes de l'ovocyte II en métaphase II ; 6 = chromosomes métaphasiques (première mitose de la cellule-œuf) ; 7 = pronucléus mâle ; 8 = pronucléus femelle.

**A. 2.** $C$ (pénétration du spermatozoïde dans l'ovocyte II) $\to$ $B$ (expulsion du 2ᵉ globule polaire, formation des pronucléus) $\to$ $A$ (première mitose de la cellule-œuf).

**A. 3.** La mère $[b]$ est $X^bX^b$ ; le père $[B]$ est $X^BY$. Chaque chromosome à deux chromatides porte deux exemplaires de l'allèle.

| Élément | 2 (spermatozoïde) | 4 (2ᵉ globule polaire) | 5 (ovocyte II en métaphase II) | 6 (cellule-œuf en mitose) | 7 (pronucléus mâle) |
|---|---|---|---|---|---|
| Formule chromosomique | $n = 1A + X$ ou $n = 1A + Y$ | $n = 1A + X$ | $n = 1A + X$ | $2n = 2A + XX$ ou $2n = 2A + XY$ | $n = 1A + X$ ou $n = 1A + Y$ |
| Nombre d'allèle(s) de $G$ | 1 ou 0 | 1 | 2 | 4 ou 2 | 2 ou 0 |
| Type d'allèle(s) de $G$ | $B$ ou aucun | $b$ | $b$ ($b$, $b$) | $B$, $B$, $b$, $b$ (fille) ou $b$, $b$ (garçon) | $B$, $B$ ou aucun |

(Chromosomes à une chromatide : spermatozoïde et 2ᵉ globule polaire ; à deux chromatides : ovocyte II en métaphase II, chromosomes métaphasiques de la mitose, et pronucléus mâle après la réplication de son ADN.)

**B. 1.** Dans la situation $B$, $H$ est à l'état de traces à $J_{14}$, augmente jusqu'à un maximum de $18\ \text{ng/mL}$ à $J_{21}$, puis diminue (14 à $J_{23}$, 5 à $J_{26}$) jusqu'à l'état de traces à $J_{28}$. Une hormone sécrétée seulement en deuxième partie de cycle (phase lutéale), avec un seul pic, est la **progestérone**, sécrétée par le corps jaune.

**B. 2.** $E_1$ = **nidation** (elle nécessite le silence utérin dû à la progestérone) ; $E_2$ = **fécondation** ; $E_3$ = **ovulation** (à $J_{14}$, dans les quatre situations) ; $E_4$ = **menstruation**.

**B. 3. a)**

| Jour de $E_4$ | 22 | 28 | 37 |
|---|---|---|---|
| Situation | $D$ | $B$ | $C$ |

- $B$ (cycle normal) : la progestérone revient à l'état de traces à $J_{28}$ : menstruation à $J_{28}$.
- $C$ : la progestérone reste élevée jusqu'à $J_{28}$, puis chute (3 à $J_{35}$, traces à $J_{38}$) : menstruation retardée vers $J_{37}$.
- $D$ : la progestérone a la même évolution que dans le cycle normal, mais la menstruation survient plus tôt, à $J_{22}$ : la substance $Y$ empêche la progestérone d'agir sur l'endomètre.

**b)** $X$ (substance placentaire qui prolonge l'activité du corps jaune) = **HCG**. $Y$ (substance de synthèse qui provoque les règles malgré une progestérone normale, en bloquant ses récepteurs) = **RU 486 (mifépristone)**.

**B. 4.** Schéma bilan (cycle fécond, $J_{21}$ à $J_{42}$) :
- le **trophoblaste** de l'embryon sécrète l'**HCG** ;
- l'HCG stimule (+) le **corps jaune**, qui se maintient et continue à sécréter **progestérone et œstradiol** ;
- ces hormones agissent (+) sur l'**endomètre** (maintien de la dentelle utérine, silence utérin : nidation et gestation possibles) ;
- elles exercent un **rétrocontrôle négatif** (−) sur l'hypothalamus et l'hypophyse : la sécrétion de FSH et de LH est freinée, il n'y a pas de nouveau cycle.
""", note="Correction conforme au corrigé officiel (annotations 1 à 8, C → B → A, tableau des allèles, progestérone, E1 nidation / E2 fécondation / E3 ovulation / E4 menstruation, 22 = D, 28 = B, 37 = C, X = HCG, Y = RU 486). Pour l'élément 7, le corrigé compte 2 allèles : c'est vrai après la réplication de l'ADN du pronucléus, ce que précise la correction. Le schéma bilan cite le corps jaune (le corrigé écrit « ovaires »).")


# ═══════════════════════════════ D 2015 — session complémentaire ══════════════

E = "bac-d-2015-sc-svt-ex1"
_add(E, rf"""
**Reproduction (6 points)**

Le testicule produit de la testostérone de façon constante grâce à un système de régulation que l'on se propose de découvrir en réalisant les expériences suivantes.

**Expérience 1**

On injecte des gonadostimulines à un animal mâle impubère ayant des cellules testiculaires inactives. Les conséquences de ces injections sur trois types de cellules testiculaires sont consignées dans le tableau 1.

| Cellules testiculaires | Injection de LH | Injection de FSH |
|---|---|---|
| Spermatogonies | inactives | activées |
| Cellules de Sertoli | non développées | développées |
| Cellules de Leydig | activées | inactives |

**1.** Citer le rôle des cellules de Sertoli et de Leydig.

**2.** Analyser les résultats de l'expérience 1 et en dégager les cellules cibles de chacune des hormones hypophysaires.

**Expérience 2**

Des cellules de Leydig sont cultivées in vitro. On ajoute, au milieu de culture, différentes molécules, LH et/ou TNFα, et on mesure en parallèle la production de testostérone. Le document 1 résume les résultats de cette expérience.

{fig(E, 1, "Document 1 : production de testostérone (UA) sans LH et avec LH, sans TNFα et avec ajout de TNFα")}

**3.** Analyser ces résultats et déduire l'effet de la TNFα.

**4.** Proposer une hypothèse quant au mode d'action de la TNFα.

**Expérience 3**

Afin d'étudier l'action de certains types de cellules testiculaires sur l'activité des cellules hypophysaires, on réalise des cultures dans des milieux appropriés et on mesure le taux de gonadostimulines libérées (tableau 2).

| | Milieu 1 : cellules hypophysaires ($X$) seules | Milieu 2 : cellules ($X$) + cellules $Y$ | Milieu 3 : cellules ($X$) + cellules $Z$ |
|---|---|---|---|
| Libération de FSH | 100 % | 100 % | 40 % |
| Libération de LH | 100 % | 40 % | 100 % |

**5.** Analyser les résultats de l'expérience 3 et identifier les cellules $Y$ et $Z$.

**6.** Représenter les différentes relations entre l'hypophyse et le testicule.
""", r"""
**1.**
- **Cellules de Sertoli** (dans la paroi des tubes séminifères) : elles nourrissent et soutiennent les cellules de la lignée germinale et permettent la spermatogenèse ; elles sécrètent aussi l'inhibine et la protéine qui fixe la testostérone (ABP).
- **Cellules de Leydig** (dans le tissu interstitiel, entre les tubes) : elles sécrètent la **testostérone**.

**2.**
- Avec la LH, seules les cellules de Leydig sont activées ; spermatogonies et cellules de Sertoli restent inactives.
- Avec la FSH, les spermatogonies sont activées et les cellules de Sertoli se développent, mais les cellules de Leydig restent inactives.

Cellules cibles : la **LH** agit sur les **cellules de Leydig** ; la **FSH** agit sur les **cellules de Sertoli** (et, par leur intermédiaire, active les spermatogonies, donc la spermatogenèse).

**3.**
- Sans LH, les cellules de Leydig ne produisent presque pas de testostérone, avec ou sans TNFα.
- Avec LH seule, la production est forte (environ $4{,}8$ UA).
- Avec LH et TNFα, elle reste très faible (environ $0{,}4$ UA).

La LH stimule la sécrétion de testostérone, et la TNFα **inhibe cet effet de la LH** (elle n'a pas d'effet propre sans LH).

**4.** Hypothèse : la TNFα empêche la LH d'agir sur la cellule de Leydig, par exemple en **bloquant les récepteurs membranaires à la LH** (ou en bloquant la chaîne de réactions déclenchée dans la cellule après la fixation de la LH).

**5.**
- Les cellules hypophysaires seules libèrent 100 % de FSH et de LH (témoin).
- Avec les cellules $Y$, la libération de LH tombe à 40 % ; celle de FSH ne change pas : $Y$ freine sélectivement la LH.
- Avec les cellules $Z$, la libération de FSH tombe à 40 % ; celle de LH ne change pas : $Z$ freine sélectivement la FSH.

$Y$ = **cellules de Leydig** : leur testostérone exerce un rétrocontrôle négatif sur la sécrétion de LH. $Z$ = **cellules de Sertoli** : elles sécrètent l'**inhibine**, qui exerce un rétrocontrôle négatif sur la sécrétion de FSH.

**6.** Schéma des relations :
- hypophyse → **LH** → (+) cellules de Leydig → **testostérone** ;
- hypophyse → **FSH** → (+) cellules de Sertoli → spermatogenèse ; la testostérone agit aussi (+) sur la spermatogenèse ;
- testostérone → (−) hypophyse (et hypothalamus) : freine la sécrétion de LH ;
- cellules de Sertoli → **inhibine** → (−) hypophyse : freine la sécrétion de FSH.

Ce double rétrocontrôle négatif maintient constante la production de testostérone.
""", note="Pas de corrigé officiel disponible pour cette session. Les réponses se déduisent directement des tableaux et du document (cellules cibles, Y = Leydig, Z = Sertoli/inhibine). Le mode d'action de la TNFα est demandé sous forme d'hypothèse : la correction en propose une, présentée comme telle.")


# ═══════════════════════════════ D 2016 — session complémentaire ══════════════

E = "bac-d-2016-sc-svt-ex1"
_add(E, rf"""
**Reproduction (7 points)**

**A.** Les dosages des quantités d'ADN contenues dans trois catégories de cellules germinales de testicules de deux sujets adultes $A$ et $B$ ont donné les résultats suivants :

| | | Cellules $X$ | Cellules $Y$ | Cellules $Z$ |
|---|---|---|---|---|
| Sujet $A$ | Nombre de cellules (UA) | 8 | 4 | 2 |
| | Quantité d'ADN | $x$ | $2x$ | $4x$ |
| Sujet $B$ | Nombre de cellules (UA) | 2 | 10 | 2 |
| | Quantité d'ADN | $x$ | $2x$ | $4x$ |

**1.** Comparez le nombre de cellules puis la quantité d'ADN des cellules $X$, $Y$, $Z$ du sujet $A$.

**2.** Expliquez les résultats constatés chez $A$.

**3.** Identifiez les cellules $X$, $Y$ et $Z$.

**4.** Analysez les résultats obtenus chez le sujet $B$. Que peut-on en déduire ?

**5.** Proposez une explication à l'anomalie constatée chez le sujet $B$.

**6.** Quel traitement hormonal pourrait corriger ce dysfonctionnement ?

**B.** Le document 1 représente l'évolution de la quantité d'ADN par noyau depuis la maturation de l'ovocyte jusqu'à l'obtention d'un embryon de deux cellules chez un mammifère.

{fig(E, 1, "Document 1 : quantité d'ADN par noyau (Q/2, Q, 2Q) en fonction du temps ; repères t1 à t5, segments 1, 2, 3 et noyaux a, b, c, d, e")}

**1.** Déterminez les phénomènes qui se sont déroulés :

a) entre $t_1$ et $t_2$ ;

b) entre $t_2$ et $t_3$ ;

c) entre $t_4$ et $t_5$.

**2.** Nommez les phases de la fécondation qui correspondent aux segments 1, 2 et 3.

**3.** Précisez le nombre de chromosomes et le nombre de chromatides par chromosome pour les noyaux $b$, $c$, $d$ et $e$.
""", r"""
**A. 1.** Chez $A$, le nombre de cellules double de $Z$ à $Y$ (2 → 4) puis de $Y$ à $X$ (4 → 8), tandis que la quantité d'ADN par cellule est divisée par deux à chaque fois ($4x$ → $2x$ → $x$).

**A. 2.** Chaque cellule $Z$ donne deux cellules $Y$, et chaque cellule $Y$ donne deux cellules $X$, avec à chaque fois un partage de l'ADN en deux, sans réplication entre les deux divisions : ce sont les **deux divisions successives de la méiose** (spermatogenèse).

**A. 3.**
- $Z$ ($4x$) = **spermatocytes I** : diploïdes, chromosomes à deux chromatides.
- $Y$ ($2x$) = **spermatocytes II** : haploïdes, chromosomes à deux chromatides.
- $X$ ($x$) = **spermatides** : haploïdes, chromosomes à une chromatide ; elles se différencient ensuite en spermatozoïdes.

**A. 4.** Chez $B$, les spermatocytes I sont en nombre normal (2), mais les spermatocytes II s'accumulent (10 au lieu de 4) et les spermatides sont très peu nombreuses (2 au lieu de 8). La première division de méiose se fait, mais la **deuxième division de méiose est bloquée** (ou très ralentie) : la production de spermatides, donc de spermatozoïdes, est fortement réduite (risque de stérilité).

**A. 5.** Explication possible : un **déficit hormonal** des hormones qui contrôlent la spermatogenèse, en particulier un taux insuffisant de **testostérone** (sécrétée par les cellules de Leydig sous l'action de la LH), qui est nécessaire au déroulement complet de la méiose, ou un déficit en FSH (qui agit par les cellules de Sertoli).

**A. 6.** Un traitement par **testostérone**, ou par des gonadostimulines (LH, qui stimule la sécrétion de testostérone, et FSH), pourrait rétablir la spermatogenèse, si l'anomalie est bien d'origine hormonale.

**B. 1.**
- **a)** À $t_1$, la quantité d'ADN passe de $2Q$ à $Q$ : la **première division de méiose** vient de s'achever (expulsion du 1ᵉʳ globule polaire). Entre $t_1$ et $t_2$, le noyau $a$ est celui de l'**ovocyte II**, bloqué en métaphase II ; c'est sous cette forme qu'il est expulsé lors de l'ovulation.
- **b)** Entre $t_2$ et $t_3$, la quantité d'ADN passe de $Q$ à $\dfrac{Q}{2}$ : c'est la **deuxième division de méiose**, déclenchée par la pénétration du spermatozoïde (expulsion du 2ᵉ globule polaire).
- **c)** Entre $t_4$ et $t_5$, la quantité passe de $2Q$ à $Q$ : c'est la **première mitose** de la cellule-œuf, qui donne un embryon de deux cellules.

**B. 2.**
- Segment 1 : **pénétration du spermatozoïde et activation de l'ovocyte** (achèvement de la méiose et expulsion du 2ᵉ globule polaire).
- Segment 2 : **formation des pronucléus et réplication de leur ADN** (de $\dfrac{Q}{2}$ à $Q$).
- Segment 3 : **amphimixie (caryogamie)** : union des pronucléus mâle et femelle ($Q + Q = 2Q$) ; la cellule-œuf est formée.

**B. 3.**

| Noyau | b | c | d | e |
|---|---|---|---|---|
| Quantité d'ADN | $\dfrac{Q}{2}$ | $Q$ | $2Q$ | $Q$ |
| Nombre de chromosomes | $n$ | $n$ | $2n$ | $2n$ |
| Chromatides par chromosome | 1 | 2 | 2 | 1 |

($b$ : noyau haploïde après la méiose ; $c$ : pronucléus après réplication ; $d$ : cellule-œuf avant sa première mitose ; $e$ : noyau de chaque cellule de l'embryon à deux cellules.)
""", note="Pas de corrigé officiel disponible pour cette session. Identification des cellules (8 : 4 : 2 et x, 2x, 4x) et lecture du document B déduites sans ambiguïté des données. Les questions A5–A6 demandent une explication et un traitement : la correction les présente comme hypothèse (déficit en testostérone ou en gonadostimulines).")


# ═══════════════════════════════ D 2022 — session complémentaire ══════════════

E = "bac-d-2022-sc-svt-ex3"
_add(E, rf"""
**Exercice 2 (5 points)**

On se propose d'étudier quelques aspects de la fonction reproductrice à partir des résultats des séries d'expériences suivantes.

**1ʳᵉ série d'expériences**

- La castration d'un animal jeune (mâle ou femelle) supprime la gamétogenèse et l'animal demeure impubère.
- On injecte à des rats mâles impubères des doses croissantes d'une hormone $X$ extraite à partir des testicules d'un rat mâle adulte. Le document 1 montre l'évolution du poids des vésicules séminales et de la prostate chez ces rats suite à ce traitement.
- On injecte à des rattes impubères des doses croissantes d'une hormone $Y$ extraite à partir de l'ovaire d'une ratte pubère. Le document 2 montre l'évolution du poids de leurs utérus suite à ce traitement.

{fig(E, 1, "Document 1 : poids (mg) des vésicules séminales et de la prostate en fonction de la dose d'hormone X (mg)")}

{fig(E, 2, "Document 2 : poids de l'utérus (mg) en fonction de la dose d'hormone Y (µg)")}

Analysez les résultats de ces expériences en vue :

**1.** de préciser le mode d'action des gonades sur certains organes de l'appareil génital (vésicules séminales, prostate et utérus) ;

**2.** d'identifier les hormones $X$ et $Y$.

**2ᵉ série d'expériences**

Afin de préciser certains contrôles du fonctionnement des gonades, on réalise les expériences suivantes :
- L'ablation de l'hypophyse chez des animaux immatures empêche la maturité sexuelle et les gonades demeurent atrophiées.

**3.** Quelle information tirez-vous à partir de l'analyse de cette expérience ?

- La parabiose effectuée entre un rat mâle adulte castré depuis 30 jours avec un rat mâle (ou femelle) impubère entraîne une maturité sexuelle précoce (puberté précoce).

**4.** Proposez une hypothèse expliquant la maturité sexuelle précoce chez le rat (ou la ratte).

**5.** À partir de vos connaissances, réalisez deux schémas qui résument les relations entre les différents organes intervenant dans la régulation de l'activité sexuelle (mâle et femelle).
""", r"""
**1.** La castration supprime la gamétogenèse et la puberté. Chez le rat impubère, l'injection d'un extrait testiculaire ($X$) fait augmenter le poids des vésicules séminales (de 100 à 250 mg) et de la prostate (de 50 à environ 125 mg) d'autant plus que la dose est forte (de 0,1 à 1 mg). Chez la ratte impubère, l'extrait ovarien ($Y$) fait augmenter le poids de l'utérus, d'environ 10 mg à environ 145 mg, en fonction de la dose (à partir de quelques millièmes de µg).

Les gonades agissent donc sur ces organes génitaux par **voie hormonale** : elles sécrètent dans le sang des hormones qui stimulent le développement et l'activité de leurs organes cibles, avec un effet proportionnel à la dose.

**2.** $X$, hormone testiculaire qui stimule les glandes annexes mâles, est la **testostérone**. $Y$, hormone ovarienne qui fait croître l'utérus, est l'**œstradiol** (œstrogènes).

**3.** Sans hypophyse, les gonades restent atrophiées et la maturité sexuelle n'est pas atteinte : le fonctionnement des gonades dépend de l'**hypophyse**, qui les stimule par ses hormones (les gonadostimulines **FSH et LH**).

**4.** Hypothèse : chez le rat castré, l'absence de testostérone lève le **rétrocontrôle négatif** exercé sur l'hypothalamus et l'hypophyse ; ceux-ci sécrètent alors de grandes quantités de gonadostimulines (FSH et LH). Par la circulation sanguine commune établie par la parabiose, ces gonadostimulines passent chez l'animal impubère et stimulent précocement ses gonades, qui se mettent à fonctionner : la puberté est précoce.

**5.** Schéma chez le mâle :
- hypothalamus → **GnRH** → (+) hypophyse ;
- hypophyse → **LH** → (+) cellules de Leydig → **testostérone** → (+) organes cibles (vésicules séminales, prostate, caractères sexuels) ;
- hypophyse → **FSH** → (+) cellules de Sertoli → spermatogenèse (avec la testostérone) ;
- testostérone → (−) hypothalamus et hypophyse ; inhibine (cellules de Sertoli) → (−) hypophyse (FSH).

Schéma chez la femelle :
- hypothalamus → **GnRH** → (+) hypophyse ;
- hypophyse → **FSH** et **LH** → (+) ovaire (follicules, puis corps jaune) ;
- ovaire → **œstradiol** et **progestérone** → (+) utérus (endomètre) et autres organes cibles ;
- œstradiol et progestérone → (−) hypothalamus et hypophyse pendant la plus grande partie du cycle ; un taux élevé d'œstradiol en fin de phase folliculaire exerce un rétrocontrôle **positif**, qui déclenche le pic de LH et l'ovulation.
""", note="Pas de corrigé officiel disponible pour cette session. Les réponses se lisent sans ambiguïté sur les documents (X = testostérone, Y = œstradiol, rôle de l'hypophyse) ; la question 4 demande une hypothèse, présentée comme telle (levée du rétrocontrôle négatif chez le castré).")


# ═══════════════════════════════ C 2015 — session normale ═════════════════════

E = "bac-c-2015-sn-svt-ex1"
_add(E, rf"""
**Reproduction (8 points)**

**A.** Le document 1 correspond à une coupe transversale d'un organe sexuel de mammifère.

{fig(E, 1, "Document 1 : coupe d'un organe sexuel de mammifère (cellules a à f)")}

**1.** Nommez les cellules $a$, $b$ et $c$ et précisez le rôle de chacune.

**2.** Identifiez les stades de division cellulaire correspondant aux cellules $d$, $e$ et $f$. Schématisez les stades $d$ et $e$.

**3.** Précisez les phases de la gamétogenèse illustrées par ce document.

**B.** L'observation des ovaires d'une femelle $A$ de mammifère montre la présence de 7 corps jaunes.

**1.** Ce chiffre peut-il être une indication précise sur le nombre de petits susceptibles d'être rencontrés dans la portée correspondante ? Discutez.

**2.** L'utérus d'une autre femelle $B$ contient deux embryons de même sexe. Combien de corps jaunes peut-on trouver dans ses ovaires ? Justifiez votre réponse.

**3.** L'ablation de l'hypophyse pratiquée sur une femelle $C$ provoque la disparition de quelques caractères sexuels.

a) Quelle relation existe entre l'hypophyse et ces caractères ?

b) Comment peut-on remédier expérimentalement aux symptômes observés chez cette femelle ?
""", r"""
Le document est une coupe de **testicule** : un tube séminifère et le tissu interstitiel voisin.

**A. 1.**
- $a$ = **cellule de Leydig** (tissu interstitiel) : elle sécrète la **testostérone**.
- $b$ = **cellule de Sertoli** : elle soutient et nourrit les cellules germinales ; elle sécrète l'ABP (qui concentre la testostérone dans le tube) et l'inhibine (qui freine la FSH).
- $c$ = **spermatozoïde** : le gamète mâle ; il apporte le lot haploïde de chromosomes du père à l'ovocyte et détermine le sexe de l'embryon (chromosome $X$ ou $Y$).

**A. 2.** D'après le corrigé officiel (le scan ne permet pas de distinguer finement les chromosomes) : $d$ = **anaphase I**, $e$ = **anaphase II**, $f$ = **prophase I** de la méiose.

Schémas attendus (avec $2n = 4$, par exemple) :
- $d$, anaphase I : les chromosomes homologues, chacun à deux chromatides, se séparent et migrent vers les deux pôles (2 chromosomes à deux chromatides vers chaque pôle) ;
- $e$, anaphase II : dans une cellule haploïde, les chromatides de chaque chromosome se séparent (2 chromatides vers chaque pôle).

**A. 3.** Le document montre la **multiplication** (spermatogonies, en périphérie du tube), l'**accroissement** (spermatocytes I), la **maturation** (méiose) et la **différenciation** (spermiogenèse : des spermatides aux spermatozoïdes, vers la lumière du tube).

**B. 1.** Non, pas de façon précise. Chaque corps jaune correspond à une ovulation, donc à un ovocyte libéré : 7 corps jaunes signifient au plus 7 cellules-œufs.
- Le nombre de petits peut être **inférieur** : tous les ovocytes ne sont pas fécondés, et certains embryons ne se nidifient pas ou meurent.
- Il peut être **supérieur** : une cellule-œuf peut donner de vrais jumeaux. Dans le cas extrême où chacune des 7 cellules-œufs donne des jumeaux, il y a 14 petits.

Le nombre de petits est donc compris entre 0 et 14 : les corps jaunes n'en donnent qu'une indication relative.

**B. 2.** **Un ou deux corps jaunes** :
- 1 corps jaune : une seule ovulation, une cellule-œuf qui s'est divisée en deux ; ce sont de **vrais jumeaux** (forcément de même sexe) ;
- 2 corps jaunes : deux ovulations, deux cellules-œufs ; ce sont de **faux jumeaux**, qui peuvent être de même sexe.

**B. 3. a)** La relation est **indirecte** : l'hypophyse sécrète les gonadostimulines (FSH et LH) qui stimulent les ovaires ; les ovaires sécrètent les hormones sexuelles (œstrogènes et progestérone), qui maintiennent les caractères sexuels. Sans hypophyse, les ovaires ne sont plus stimulés et les caractères sexuels régressent.

**b)** Par des **injections de FSH et de LH** (gonadostimulines), qui relancent l'activité ovarienne ; des injections d'hormones ovariennes (œstrogènes, progestérone) rétabliraient aussi directement les caractères sexuels.
""", note="Correction croisée avec le corrigé officiel (a Leydig, b Sertoli, c spermatozoïde ; d anaphase I, e anaphase II, f prophase I ; 0 à 14 petits ; 1 ou 2 corps jaunes ; relation indirecte, injection de FSH et LH). Les stades d, e, f sont repris du corrigé (le scan ne permet pas de les vérifier finement), ce que dit la correction.")


# ─────────────────────────────────────────────────────────────────────────────
CHECKS: dict[str, list[str]] = {}
