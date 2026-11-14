"""SVT — chapitre « Génétique classique et humaine » (séries C et D) :
énoncés retranscrits des PDF officiels, avec les documents (figures) découpés dans
le sujet, + corrections croisées avec les corrigés officiels quand ils existent.
Les proportions et effectifs sont recalculés (CHECKS en fin de fichier).

Figures : app/public/static/figures/svt/<id>-docN.jpg (chemin public /static/figures/svt/…).

- ENONCES : ``scripts/load_enonces.py svt_genetique --apply``
- CORRECTIONS : ``scripts/load_corrections.py svt_genetique --apply``
"""

CH = "Génétique classique et humaine"
FIG = "/static/figures/svt/"

ENONCES: dict[str, dict] = {}
CORRECTIONS: dict[str, dict] = {}


def fig(eid: str, n: int | str, legende: str) -> str:
    return f"![{legende}]({FIG}{eid}-doc{n}.jpg)"


def _add(eid: str, enonce: str, correction: str, chapitres=None, note: str = "") -> None:
    ENONCES[eid] = {"chapitre": CH, "chapitres": list(chapitres or []), "enonce": enonce.strip() + "\n",
                    "note": note, "replace_ocr": True}
    CORRECTIONS[eid] = {"enonce": enonce.strip() + "\n", "correction": correction.strip() + "\n", "note": note}


# ═══════════════════════════════ D 2017 — session normale ═════════════════════

E = "bac-d-2017-sn-svt-ex4"
_add(E, rf"""
**Génétique (6 points)**

On s'intéresse chez la drosophile au comportement de deux gènes $G_1$ et $G_2$, contrôlant deux caractères héréditaires :
- $G_1$ dont les allèles ($vg^+$, $vg$) ;
- $G_2$ dont les allèles ($b^+$, $b$).

Une drosophile femelle hétérozygote de phénotype $[vg^+b^+]$ produit un ovocyte II représenté par le document 5 (seul le chromosome qui porte les gènes étudiés est considéré).

{{fig(E, 1, "Document 5 : chromosome de l'ovocyte II (chromatides vg⁺ b et vg⁺ b⁺)")}}

**1.** Précisez la quantité d'ADN et la garniture chromosomique de cet ovocyte.

**2.** Quels sont les différents types de gamètes produits par cette femelle et dans quelles proportions ?

**3.** On réalise le croisement de cette femelle avec un mâle de même génotype. La descendance issue de ce croisement montre entre autres $4{{,}}5\ \%$ d'individus de phénotype $[vg\,b^+]$.

a) Déduisez le génotype du mâle.

b) Quels sont les différents types de gamètes produits par ce mâle et dans quelles proportions ?

**4.** Expliquez les résultats en dressant l'échiquier de croisement.

**5.** Quels sont les effectifs des différents phénotypes sur 200 drosophiles issues de ce croisement ?

**6.** Précisez la localisation relative des deux gènes.
""", r"""
**1.** L'ovocyte II est **haploïde** et ses chromosomes ont **deux chromatides** : garniture $n = 4$ chromosomes ($3$ autosomes $+ X$) à deux chromatides. Sa quantité d'ADN est égale à celle d'une cellule diploïde avant réplication (notée $Q$).

Le document montre un chromosome dont les deux chromatides portent $vg^+$, l'une avec $b$ et l'autre avec $b^+$ : il y a eu un **crossing-over** entre les deux gènes pendant la méiose I. Les deux gènes sont donc **liés** (sur le même chromosome).

**2.** Les gènes étant liés avec crossing-over, la femelle produit quatre types de gamètes : deux types **parentaux** (majoritaires) et deux types **recombinés** (minoritaires). En notant $p$ le pourcentage de recombinaison, et avec le génotype $\dfrac{vg^+\,b^+}{vg\ \,b}$ établi à la question 3 :
- $vg^+b^+$ et $vg\,b$ : $\dfrac{1 - p}{2}$ chacun (parentaux) ;
- $vg^+b$ et $vg\,b^+$ : $\dfrac{p}{2}$ chacun (recombinés).

**3. a)** Chez la drosophile mâle, il n'y a pas de crossing-over.
- Si le mâle était $\dfrac{vg^+\,b}{vg\ \,b^+}$, il produirait 50 % de gamètes $vg\,b^+$, et la proportion de $[vg\,b^+]$ serait de 25 %, quel que soit $p$.
- Le mâle est donc $\dfrac{vg^+\,b^+}{vg\ \,b}$ (même génotype que la femelle). Dans ce cas, $[vg\,b^+]$ ne s'obtient qu'avec un gamète femelle recombiné $vg\,b^+$ et un gamète mâle $vg\,b$ : $\dfrac{p}{2} \times \dfrac{1}{2} = \dfrac{p}{4} = 4{,}5\ \%$, d'où $p = 18\ \%$.

**b)** Le mâle produit $\dfrac{1}{2}$ $vg^+b^+$ et $\dfrac{1}{2}$ $vg\,b$.

**4.** Gamètes femelles : $vg^+b^+$ (41 %), $vg\,b$ (41 %), $vg^+b$ (9 %), $vg\,b^+$ (9 %).

| ♀ \ ♂ | $vg^+b^+$ ($\frac{1}{2}$) | $vg\,b$ ($\frac{1}{2}$) |
|---|---|---|
| $vg^+b^+$ (41 %) | $[vg^+b^+]$ 20,5 % | $[vg^+b^+]$ 20,5 % |
| $vg\,b$ (41 %) | $[vg^+b^+]$ 20,5 % | $[vg\,b]$ 20,5 % |
| $vg^+b$ (9 %) | $[vg^+b^+]$ 4,5 % | $[vg^+b]$ 4,5 % |
| $vg\,b^+$ (9 %) | $[vg^+b^+]$ 4,5 % | $[vg\,b^+]$ 4,5 % |

Bilan : $[vg^+b^+]$ 70,5 % ; $[vg\,b]$ 20,5 % ; $[vg^+b]$ 4,5 % ; $[vg\,b^+]$ 4,5 %.

**5.** Sur 200 drosophiles : $[vg^+b^+]$ : $0{,}705 \times 200 = 141$ ; $[vg\,b]$ : $41$ ; $[vg^+b]$ : $9$ ; $[vg\,b^+]$ : $9$.

**6.** Les deux gènes sont **liés** (sur le même chromosome) et séparés par une distance de **18 cM** (18 unités de recombinaison).
""", note="Correction conforme au corrigé officiel (n = 3 + X chromosomes à deux chromatides ; mâle vg⁺b⁺/vgb ; p = 18 % ; effectifs 141, 9, 9, 41 ; distance 18 cM).")


# ═══════════════════════════════ D 2019 — session normale ═════════════════════

E = "bac-d-2019-sn-svt-ex2"
_add(E, rf"""
**Exercice 2 (3 points)**

L'arbre généalogique ci-contre est celui d'une famille dont certains membres sont atteints d'une maladie héréditaire.

{fig(E, 1, "Arbre généalogique : individus 1 à 8 (2, 3 et 5 atteints ; 8 = fœtus)")}

**1.** Discutez le mode de transmission de cette maladie :
- Hypothèse 1 : l'allèle de la maladie est dominant, porté par $X$.
- Hypothèse 2 : l'allèle de la maladie est dominant, autosomique.
- Hypothèse 3 : l'allèle de la maladie est récessif, porté par $X$.
- Hypothèse 4 : l'allèle de la maladie est récessif, autosomique.

Des études génétiques et physiologiques précisent que l'absence de l'allèle normal est létale avant la naissance, car le développement du fœtus exige la protéine fonctionnelle que le gène muté ne peut fournir.

**2.** Qu'apporte cette information ?

**3.** D'autres études statistiques ont confirmé que cette maladie affecte seulement les femmes.

a) Que concluez-vous ?

b) Donnez les génotypes des individus 1, 2 et 6.

**4.** Quel est le risque de la maladie chez le fœtus 8 ?

**5.** Le garçon 5, âgé de trois ans, est une exception aux études statistiques. Proposez une hypothèse afin d'expliquer son phénotype.

*NB : notez $N$ ou $n$ pour l'allèle normal et $M$ ou $m$ pour l'allèle responsable de la maladie.*
""", r"""
Lecture de l'arbre : le couple 1 (homme sain) × 2 (femme atteinte) a un fils sain, 4. Le couple 4 × 3 (femme atteinte) a un fils atteint, 5, et une fille saine, 6. Le couple 6 × 7 (homme sain) attend le fœtus 8.

**1.**

| Hypothèse | Validité | Justification |
|---|---|---|
| 1 : dominant, porté par $X$ | possible | aucun père atteint n'a de fille saine ; la mère atteinte 2 peut être hétérozygote $X^MX^n$ et avoir un fils sain |
| 2 : dominant, autosomique | possible | chaque enfant atteint (5) a un parent atteint (3) |
| 3 : récessif, porté par $X$ | **rejetée** | une mère atteinte ($X^mX^m$) aurait tous ses fils atteints ; or la mère 2 a un fils sain (4) |
| 4 : récessif, autosomique | possible | les parents atteints ont des enfants sains, compatibles avec des parents hétérozygotes |

**2.** Comme l'absence de l'allèle normal est létale, tout individu né porte au moins un allèle normal. Les femmes atteintes (2 et 3) possèdent donc l'allèle normal **et** sont malades : l'allèle de la maladie s'exprime chez l'hétérozygote, il est **dominant**. L'hypothèse 4 est rejetée.

**3. a)** Si le gène était autosomique, les deux sexes seraient atteints. La maladie ne touche que les femmes : un homme qui reçoit l'allèle de la maladie ($X^MY$) n'a pas d'allèle normal (il est hémizygote) et meurt avant la naissance. Le gène est donc porté par le chromosome $X$ : l'**hypothèse 1** est retenue (allèle dominant, lié à $X$).

**b)** 1 : $X^nY$ ; 2 : $X^MX^n$ ; 6 : $X^nX^n$.

**4.** 6 ($X^nX^n$) × 7 ($X^nY$) : aucun des parents ne porte l'allèle $M$. Le risque pour le fœtus 8 est **nul** (0).

**5.** Le garçon 5 est atteint et vivant : il porte l'allèle $M$ et aussi un allèle normal, donc deux chromosomes $X$. Hypothèse : il présente une anomalie chromosomique, un **syndrome de Klinefelter** $X^MX^nY$ (avec un chromosome $X$ en trop provenant, par non-disjonction, de sa mère 3, qui est $X^MX^n$).
""", note="Correction conforme au corrigé officiel (hypothèses 1, 2, 4 possibles, 3 rejetée ; allèle dominant ; lié à X ; génotypes 1 XnY, 2 XMXn, 6 XnXn ; risque nul ; Klinefelter XMXnY).")


# ═══════════════════════════════ D 2022 — session normale ═════════════════════

E = "bac-d-2022-sn-svt-ex2"
_add(E, rf"""
**Exercice 1 (4 points)**

Chez une drosophile ($D_1$), de phénotype $[G_1N_2]$, on étudie la transmission de deux caractères héréditaires, contrôlés par deux couples d'allèles distants de 8 centimorgans.
- Le 1ᵉʳ caractère est contrôlé par le couple d'allèles ($G_1$, $G_2$) ;
- le 2ᵉ caractère est contrôlé par le couple d'allèles ($N_1$, $N_2$).

La figure ci-contre est une représentation simplifiée d'une cellule ($C$) issue de la division réductionnelle chez la drosophile ($D_1$) hybride pour les deux couples d'allèles.

{fig(E, 1, "Cellule C : un chromosome à deux chromatides, G2 N2 (segment noir) et G2 N1")}

**1.** Nommez la cellule $C$.

**2.** En se limitant aux allèles seulement, représentez les types de gamètes fournis par la femelle $D_1$ et précisez la proportion de chaque type.

**3.** Le croisement de la drosophile ($D_1$) avec un mâle ($D_2$) de même phénotype donne une descendance où toutes les femelles sont $[G_1N_2]$, alors que les mâles sont répartis en quatre phénotypes.

a) Que concluez-vous ?

b) Écrire le génotype de chacune des drosophiles $D_1$ et $D_2$.

c) Donnez la répartition phénotypique selon le sexe, sur un total de 1000 drosophiles, en complétant le tableau suivant :

| | $[G_1N_2]$ | $[G_1N_1]$ | $[G_2N_2]$ | $[G_2N_1]$ |
|---|---|---|---|---|
| Femelles | ? | ? | ? | ? |
| Mâles | ? | ? | ? | ? |
""", r"""
**1.** La cellule $C$ est issue de la première division de méiose (division réductionnelle) chez une femelle : c'est un **ovocyte II** (haploïde, chromosomes à deux chromatides). Ses deux chromatides portent $G_2N_2$ et $G_2N_1$ : un **crossing-over** a eu lieu entre les deux gènes.

**2.** $D_1$ est hybride et de phénotype $[G_1N_2]$ : $G_1$ domine $G_2$ et $N_2$ domine $N_1$. Les gènes sont liés, distants de 8 cM, donc $p = 8\ \%$ de gamètes recombinés. D'après la cellule $C$, le chromosome d'origine portait $G_2N_1$ (le segment noir $N_2$ vient de l'homologue) : $D_1$ possède les combinaisons parentales $G_1N_2$ et $G_2N_1$.

| Gamète | $G_1N_2$ | $G_2N_1$ | $G_1N_1$ | $G_2N_2$ |
|---|---|---|---|---|
| Type | parental | parental | recombiné | recombiné |
| Proportion | $\dfrac{1 - p}{2} = 46\ \%$ | $46\ \%$ | $\dfrac{p}{2} = 4\ \%$ | $4\ \%$ |

**3. a)** Les femelles ont toutes le phénotype du père, alors que les mâles présentent quatre phénotypes, ceux des gamètes de la mère : la transmission dépend du sexe. Les deux gènes sont **portés par le chromosome $X$** (liés au sexe), sans équivalent sur $Y$.

**b)** $D_1$ (femelle) : $X^{G_1N_2}X^{G_2N_1}$ ; $D_2$ (mâle) : $X^{G_1N_2}Y$.

**c)** Les femelles reçoivent toutes le $X^{G_1N_2}$ de leur père : elles sont toutes $[G_1N_2]$. Les mâles reçoivent le $Y$ du père et un $X$ de la mère : leurs phénotypes reflètent les gamètes de la mère. Sur 1000 drosophiles (500 femelles, 500 mâles) :

| | $[G_1N_2]$ | $[G_1N_1]$ | $[G_2N_2]$ | $[G_2N_1]$ |
|---|---|---|---|---|
| Femelles | 500 | 0 | 0 | 0 |
| Mâles | 230 | 20 | 20 | 230 |

($0{,}46 \times 500 = 230$ et $0{,}04 \times 500 = 20$.)
""", note="Correction conforme au corrigé officiel (ovocyte II ; gamètes 46 %, 4 %, 4 %, 46 % ; gènes portés par X ; D1 = X^G1N2 X^G2N1, D2 = X^G1N2 Y ; 500/0/0/0 et 230/20/20/230).")


# ═══════════════════════════════ D 2023 — session normale ═════════════════════

E = "bac-d-2023-sn-svt-ex3"
_add(E, r"""
**Exercice 1 (4 points)**

Afin de déterminer le mode de transmission de deux gènes, un professeur donne à ses élèves les résultats de deux croisements ($C_1$ et $C_2$) réalisés entre des drosophiles de race pure.

| | Parents | Résultats |
|---|---|---|
| $C_1$ | ♀ sauvage × ♂ à ailes écartées et yeux rugueux | 100 % d'individus sauvages |
| $C_2$ | ♂ sauvage × ♀ à ailes écartées et yeux rugueux | 98 drosophiles ♂ à ailes de type sauvage et yeux rugueux ; 101 drosophiles ♀ toutes sauvages |

*Remarque : ♀ = femelle ; ♂ = mâle.*

**1.** Analyser ces résultats afin de :

a) préciser la relation de dominance ;

b) déterminer si les gènes qui gouvernent ces deux caractères sont liés ou indépendants.

**2.** Donner les génotypes des parents et ceux de la $F_1$ pour les deux croisements.

**3.** Le croisement entre les drosophiles de la $F_1$ issues du deuxième croisement donne une $F_2$ de 224 drosophiles. Donner, en justifiant votre réponse, le nombre d'individus correspondant à chaque phénotype de la $F_2$.

*NB : forme des yeux ($R$, $r$) ; forme des ailes ($E$, $e$).*
""", r"""
**1. a)** Le croisement $C_1$ entre races pures donne une $F_1$ homogène de phénotype sauvage : les allèles sauvages sont **dominants**. On note $R$ (yeux sauvages) > $r$ (yeux rugueux) et $E$ (ailes sauvages) > $e$ (ailes écartées).

**b)**
- **Ailes :** le croisement $C_1$ et son réciproque $C_2$ donnent le même résultat (toute la $F_1$ a des ailes sauvages) : le gène est **autosomique**.
- **Yeux :** les résultats diffèrent selon le sens du croisement. En $C_2$, les fils ont le phénotype de leur mère (yeux rugueux) et les filles celui de leur père : le gène est **porté par le chromosome $X$**.

Les deux gènes sont sur des chromosomes différents : ils sont **indépendants**.

**2.**
- $C_1$ : ♀ $EE\,X^RX^R$ × ♂ $ee\,X^rY$ → $F_1$ : ♀ $Ee\,X^RX^r$ et ♂ $Ee\,X^RY$, 100 % $[ER]$.
- $C_2$ : ♀ $ee\,X^rX^r$ × ♂ $EE\,X^RY$ → $F_1$ : ♀ $Ee\,X^RX^r$ $[ER]$ et ♂ $Ee\,X^rY$ $[Er]$.

**3.** $F_1$ de $C_2$ : ♀ $Ee\,X^RX^r$ × ♂ $Ee\,X^rY$. Les gènes étant indépendants, on combine les deux caractères :
- ailes : $Ee \times Ee$ → $\dfrac{3}{4}\,[E]$ et $\dfrac{1}{4}\,[e]$ ;
- yeux : $X^RX^r \times X^rY$ → $\dfrac{1}{2}\,[R]$ et $\dfrac{1}{2}\,[r]$ (dans chaque sexe).

| ♀ \ ♂ | $E\,X^r$ | $e\,X^r$ | $E\,Y$ | $e\,Y$ |
|---|---|---|---|---|
| $E\,X^R$ | $[ER]$ | $[ER]$ | $[ER]$ | $[ER]$ |
| $E\,X^r$ | $[Er]$ | $[Er]$ | $[Er]$ | $[Er]$ |
| $e\,X^R$ | $[ER]$ | $[eR]$ | $[ER]$ | $[eR]$ |
| $e\,X^r$ | $[Er]$ | $[er]$ | $[Er]$ | $[er]$ |

| Phénotype | $[ER]$ | $[Er]$ | $[eR]$ | $[er]$ |
|---|---|---|---|---|
| Proportion | $\dfrac{6}{16}$ | $\dfrac{6}{16}$ | $\dfrac{2}{16}$ | $\dfrac{2}{16}$ |
| Nombre sur 224 | 84 | 84 | 28 | 28 |
""", note="Correction conforme au corrigé officiel (allèles sauvages dominants ; ailes autosomique, yeux liés à X ; gènes indépendants ; F2 : 84, 84, 28, 28).")

# ═══════════════════════════════ D 2024 — session normale ═════════════════════


# ═══════════════════════════════ D 2018 — session normale ═════════════════════

E = "bac-d-2018-sn-svt-ex2"
_add(E, r"""
**Exercice 1 (5 points)**

On considère chez une espèce animale (lapin) trois gènes ($A/a$), ($B/b$) et ($R/r$) portés par des autosomes.

Afin de tester le degré de compréhension de ses élèves, un professeur propose à sa classe de 7ᵉ D une représentation simplifiée de la carte génétique et les résultats partiels de deux croisements (tableau ci-dessous).

*Carte génétique proposée :* deux segments de chromosome, l'un portant $A,a$ et $B,b$ séparés de $X$ cM, l'autre portant $B,b$ et $R,r$ séparés de $Y$ cM.

| | Croisement 1 (test cross) | Croisement 2 (autocroisement) |
|---|---|---|
| Phénotypes des individus croisés | $[AB] \times [ab]$ | $[BR] \times [BR]$ |
| Parmi les phénotypes obtenus | 42 % $[Ab]$ | 3 % $[bR]$ |

**1.** Déterminez les valeurs $X$ et $Y$.

**2.** Quels sont les gamètes formés par les individus du croisement 1 et dans quelles proportions ?

**3.** Mohamed suggère à son professeur de représenter les gènes sur un même chromosome, au lieu de deux. Justifiez cette suggestion.

**4.** Suite à la suggestion de Mohamed, le professeur demande à ses élèves de représenter ces gènes sur un seul chromosome. Niang et Sidi proposent deux réponses justes mais qui diffèrent l'une de l'autre. Quelles sont ces deux réponses ?

**5.** Camara annonce à son professeur qu'il peut confirmer la réponse de Sidi. Justifiez par un croisement l'annonce de Camara.
""", r"""
**1.**
- **Croisement 1** (test cross) : le parent $[ab]$ est double récessif ($ab/ab$) et ne fournit que des gamètes $ab$, donc les phénotypes reflètent les gamètes du parent $[AB]$ (double hétérozygote). 42 % de $[Ab]$ est une proportion **parentale** : $\dfrac{1 - p}{2} = 42\ \%$, d'où $p = 16\ \%$ et **$X = 16$ cM**. Le parent $[AB]$ est $\dfrac{A\,b}{a\,B}$.
- **Croisement 2** (autocroisement de deux doubles hétérozygotes) : 3 % de $[bR]$ est faible, c'est un phénotype **recombiné**. Les parents sont donc $\dfrac{B\,R}{b\,r}$ ; ils produisent $BR$ et $br$ avec la fréquence $\dfrac{1 - p}{2}$ chacun, $Br$ et $bR$ avec $\dfrac{p}{2}$ chacun. Un individu $[bR]$ est $\dfrac{b\,R}{b\,R}$ ou $\dfrac{b\,R}{b\,r}$ :
$$\left(\dfrac{p}{2}\right)^2 + 2 \times \dfrac{p}{2} \times \dfrac{1 - p}{2} = \dfrac{2p - p^2}{4} = 0{,}03 \iff p^2 - 2p + 0{,}12 = 0,$$
d'où $p = 1 - \sqrt{0{,}88} \approx 0{,}062$ (l'autre racine est supérieure à 1). Donc **$Y \approx 6$ cM**.

(Comme $p$ est petit, $\dfrac{p^2}{4}$ est négligeable et on retrouve directement $\dfrac{p}{2} \approx 3\ \%$.)

**2.**
- Parent $[AB]$, de génotype $\dfrac{A\,b}{a\,B}$ : 4 types de gamètes, $Ab$ 42 %, $aB$ 42 % (parentaux), $AB$ 8 % et $ab$ 8 % (recombinés).
- Parent $[ab]$, de génotype $\dfrac{a\,b}{a\,b}$ : un seul type de gamète, $ab$ (100 %).

**3.** $A/a$ est lié à $B/b$, et $B/b$ est lié à $R/r$ : les trois gènes sont donc portés par le **même chromosome** (le gène $B/b$ ne peut pas être sur deux chromosomes différents).

**4.** On connaît les distances $A$–$B$ = 16 cM et $B$–$R$ = 6 cM, mais pas l'ordre des gènes. Deux cartes sont possibles :
- **Niang** : $R$ est à l'extérieur, de l'autre côté de $B$ : $A$ — 16 cM — $B$ — 6 cM — $R$, soit $A$–$R$ = 22 cM.
- **Sidi** : $R$ est entre $A$ et $B$ : $A$ — 10 cM — $R$ — 6 cM — $B$, soit $A$–$R$ = 10 cM.

**5.** Il suffit de mesurer la distance $A$–$R$ par un **test cross** : $\dfrac{A\,R}{a\,r} \times \dfrac{a\,r}{a\,r}$.

Si la carte de Sidi est juste ($A$–$R$ = 10 cM), on obtient : $[AR]$ 45 %, $[ar]$ 45 %, $[Ar]$ 5 %, $[aR]$ 5 %. (Avec la carte de Niang, 22 cM, on aurait 11 % pour chaque phénotype recombiné.) Obtenir 5 % de chaque recombiné confirme la réponse de Sidi.
""", note="Correction conforme au corrigé officiel (X = 16 cM, Y = 6 cM ; gamètes 42/42/8/8 ; gènes sur un même chromosome ; cartes A–B–R et A–R–B ; test cross AR/ar × ar/ar donnant 45/5/5/45 pour Sidi). Y vaut exactement 1 − √0,88 ≈ 6,2 cM, arrondi à 6 cM comme dans le corrigé. Le NB du corrigé (« hypothèse I celle de Sidi … 11 % ») inverse les noms : 11 % correspond à la carte de Niang (22 cM).")


# ═══════════════════════════════ C 2017 — session normale ═════════════════════

E = "bac-c-2017-sn-svt-ex4"
_add(E, r"""
**Génétique (5 points)**

On croise deux drosophiles, l'une de type sauvage $[a^+b^+]$, l'autre du type mutant $[ab]$. Tous les individus de la $F_1$ ont le phénotype sauvage $[a^+b^+]$.

**1.** Que déduisez-vous ?

Ensuite on croise entre eux les individus de la $F_1$ ; on obtient une $F_2$ composée de :
- 70 % de drosophiles de type $[a^+b^+]$ ;
- 20 % de drosophiles de type $[ab]$ ;
- 5 % de drosophiles de type $[a^+b]$ ;
- 5 % de drosophiles de type $[ab^+]$.

**2.** Donnez le génotype de chacun des deux parents et celui de la $F_1$.

**3.** Interprétez les résultats obtenus en $F_2$.

**4.** Prévoir la répartition de 700 drosophiles issues d'un croisement d'une femelle de $F_1$ avec un mâle de type $[ab]$.

**5.** Il existe un troisième gène $n^+/n$, distant du gène $a^+/a$ de 6 centimorgans. Représentez la carte génétique des trois gènes.
""", r"""
**1.** On étudie deux caractères (dihybridisme). La $F_1$ est homogène : les parents sont de **race pure** (première loi de Mendel). La $F_1$ a le phénotype sauvage : les allèles sauvages sont **dominants**, $a^+ > a$ et $b^+ > b$.

**2.** Parents : $\dfrac{a^+\,b^+}{a^+\,b^+}$ et $\dfrac{a\,b}{a\,b}$ ; $F_1$ : $\dfrac{a^+\,b^+}{a\ \,b}$ (gènes liés, voir 3).

**3.** Si les gènes étaient indépendants, la $F_2$ serait en proportions $\dfrac{9}{16}$, $\dfrac{3}{16}$, $\dfrac{3}{16}$, $\dfrac{1}{16}$ (56,25 %, 18,75 %, 18,75 %, 6,25 %). On obtient 70 %, 20 %, 5 %, 5 % : les gènes sont **liés**, avec des phénotypes recombinés peu nombreux, donc un **crossing-over** partiel.

Chez la drosophile, il n'y a pas de crossing-over chez le mâle : le mâle $F_1$ donne $\dfrac{1}{2}\,a^+b^+$ et $\dfrac{1}{2}\,ab$. La femelle $F_1$ donne $a^+b^+$ et $ab$ (parentaux, $\dfrac{1 - p}{2}$ chacun), $a^+b$ et $ab^+$ (recombinés, $\dfrac{p}{2}$ chacun).

$[ab]$ s'obtient seulement par $ab$ (femelle) × $ab$ (mâle) : $\dfrac{1 - p}{2} \times \dfrac{1}{2} = 20\ \%$, d'où $\dfrac{1 - p}{2} = 40\ \%$ et $p = 20\ \%$.

| ♀ \ ♂ | $a^+b^+$ ($\frac{1}{2}$) | $ab$ ($\frac{1}{2}$) |
|---|---|---|
| $a^+b^+$ (40 %) | $[a^+b^+]$ 20 % | $[a^+b^+]$ 20 % |
| $ab$ (40 %) | $[a^+b^+]$ 20 % | $[ab]$ 20 % |
| $a^+b$ (10 %) | $[a^+b^+]$ 5 % | $[a^+b]$ 5 % |
| $ab^+$ (10 %) | $[a^+b^+]$ 5 % | $[ab^+]$ 5 % |

Bilan : $[a^+b^+]$ 70 %, $[ab]$ 20 %, $[a^+b]$ 5 %, $[ab^+]$ 5 % : c'est bien le résultat observé. Les deux gènes sont distants de **20 cM**.

**4.** Croisement test : ♀ $\dfrac{a^+\,b^+}{a\ \,b}$ × ♂ $\dfrac{a\,b}{a\,b}$. Les phénotypes reflètent les gamètes de la femelle : $[a^+b^+]$ 40 %, $[ab]$ 40 %, $[a^+b]$ 10 %, $[ab^+]$ 10 %.

Sur 700 drosophiles : $[a^+b^+]$ : 280 ; $[ab]$ : 280 ; $[a^+b]$ : 70 ; $[ab^+]$ : 70.

**5.** On connaît $a$–$b$ = 20 cM et $a$–$n$ = 6 cM, mais pas le côté où se trouve $n$. Deux cartes sont possibles :
- $n$ entre $a$ et $b$ : $a$ — 6 cM — $n$ — 14 cM — $b$ ;
- $n$ à l'extérieur, du côté opposé à $b$ : $n$ — 6 cM — $a$ — 20 cM — $b$ (soit $n$–$b$ = 26 cM).

Seul un croisement donnant la distance $n$–$b$ permettrait de choisir entre les deux.
""", note="Correction croisée avec le corrigé officiel, qui ne traite que les questions 1, 2 et le début de 3. Le corrigé écrit « b > b⁺ » : coquille, la F1 sauvage montre que b⁺ domine b. Les questions 3 à 5 sont entièrement recalculées (p = 20 %, 280/280/70/70) ; en 5, les deux positions possibles de n sont données car l'énoncé ne permet pas de trancher.")


# ═══════════════════════════════ C 2020 — session normale ═════════════════════

E = "bac-c-2020-sn-svt-ex1"
_add(E, r"""
**Exercice 1 (4 points)**

On croise deux lignées de drosophiles, l'une à corps gris et ailes longues, l'autre à corps noir et ailes vestigiales. Les hybrides de la $F_1$ ont tous un phénotype corps gris, ailes longues.

**1.** Définissez les mots génotype et phénotype.

**2.** Expliquez le résultat de ce croisement.

**3.** Le croisement de drosophiles femelles hybrides de la $F_1$ avec des mâles doubles récessifs donne 17 % de phénotypes nouveaux.

a) Quels sont les phénotypes nouveaux obtenus ?

b) Quelle est la proportion d'un gamète parental ?

c) Nommez et représentez le phénomène à l'origine de l'apparition des phénotypes nouveaux.

d) Donnez les résultats de la $F_2$. Justifiez par un échiquier de croisement.
""", r"""
On note $G$ (corps gris) et $n$ (corps noir), $L$ (ailes longues) et $v$ (ailes vestigiales).

**1.**
- **Génotype** : ensemble des allèles que possède un individu pour le ou les gènes considérés.
- **Phénotype** : ensemble des caractères observables (l'expression du génotype).

**2.** La $F_1$ est homogène : les parents sont de **race pure** (dihybridisme). Elle a le phénotype gris, ailes longues : $G$ domine $n$ et $L$ domine $v$. Le caractère se transmet de la même façon aux deux sexes (gènes **autosomiques**). Génotypes : parents $\dfrac{G\,L}{G\,L}$ et $\dfrac{n\,v}{n\,v}$ ; $F_1$ $\dfrac{G\,L}{n\,v}$.

**3. a)** Les phénotypes nouveaux (recombinés) sont $[Gv]$ (corps gris, ailes vestigiales) et $[nL]$ (corps noir, ailes longues).

**b)** Croisement test : les phénotypes reflètent les gamètes de la femelle $F_1$. 17 % de recombinés : $p = 17\ \%$, donc chaque gamète parental ($GL$ ou $nv$) représente $\dfrac{1 - p}{2} = 41{,}5\ \%$ (et chaque gamète recombiné $\dfrac{p}{2} = 8{,}5\ \%$).

**c)** C'est le **brassage intrachromosomique** dû au **crossing-over** : pendant la prophase I de méiose, les chromatides de deux chromosomes homologues échangent des segments entre les gènes $G/n$ et $L/v$ ; on obtient des chromatides recombinées $G\,v$ et $n\,L$.

**d)** On entend par $F_2$ le croisement des individus de la $F_1$ entre eux. Chez la drosophile, il n'y a pas de crossing-over chez le mâle : le mâle $F_1$ produit $\dfrac{1}{2}\,GL$ et $\dfrac{1}{2}\,nv$.

| ♂ \ ♀ | $GL$ (41,5 %) | $nv$ (41,5 %) | $Gv$ (8,5 %) | $nL$ (8,5 %) |
|---|---|---|---|---|
| $GL$ ($\frac{1}{2}$) | $[GL]$ | $[GL]$ | $[GL]$ | $[GL]$ |
| $nv$ ($\frac{1}{2}$) | $[GL]$ | $[nv]$ | $[Gv]$ | $[nL]$ |

Résultats : $[GL] = \dfrac{3 - p}{4} = 70{,}75\ \%$ ; $[nv] = \dfrac{1 - p}{4} = 20{,}75\ \%$ ; $[Gv] = [nL] = \dfrac{p}{4} = 4{,}25\ \%$.
""", note="Correction conforme au corrigé officiel (Gv et nL ; gamète parental 41,5 % ; crossing-over ; F2 : (3−p)/4, (1−p)/4, p/4, p/4). L'échiquier du corrigé contient une coquille (case nv × nv notée [GL] au lieu de [nv]) ; son bilan final est juste. La correction précise l'interprétation de « F2 » retenue (F1 × F1, sans crossing-over chez le mâle).")


# ═══════════════════════════════ C 2023 — session normale ═════════════════════

E = "bac-c-2023-sn-svt-ex4"
_add(E, r"""
**Exercice 3 (6 points)**

On se propose d'étudier la transmission de deux couples d'allèles chez la drosophile ($b^+$, $b$) et ($n^+$, $n$).

Le croisement d'un mâle $[b^+n^+]$ avec une femelle $[b\,n]$ donne une génération $F_1$ formée de drosophiles $[b^+n^+]$.

**1.** Que peut-on déduire ?

**2.** Le croisement d'un mâle de la $F_1$ avec une femelle $[b\,n]$ donne les résultats suivants : 101 $[b^+n^+]$ ; 99 $[b\,n]$.

a) Nommez ce type de croisement et précisez son intérêt.

b) Que déduisez-vous des résultats de ce croisement ?

c) Donnez les génotypes des parents et ceux de la $F_1$.

**3.** Le croisement de deux drosophiles de la $F_1$ donne une génération $F_2$ dont 22 % de phénotype $[b\,n]$.

a) Expliquez les résultats de ce croisement en justifiant votre réponse par un échiquier.

b) Calculez le pourcentage d'un gamète parental produit par la femelle de $F_1$. Que déduisez-vous ?

c) Donnez la répartition phénotypique de cette descendance sur un total de 2000 drosophiles.
""", r"""
**1.** La $F_1$ est homogène : les parents sont de **race pure**. Elle a le phénotype $[b^+n^+]$ : les allèles $b^+$ et $n^+$ sont **dominants** ($b^+ > b$, $n^+ > n$).

**2. a)** C'est un **croisement test** (test cross) : on croise l'individu étudié avec un double récessif $[b\,n]$, qui ne fournit que des gamètes $b\,n$. Les phénotypes des descendants reflètent directement les gamètes de l'individu testé (leurs types et leurs proportions).

**b)** On obtient seulement les deux phénotypes parentaux, en proportions égales (101 et 99, soit environ 50 % chacun), sans phénotype recombiné. Le mâle $F_1$ ne produit que deux types de gamètes, $b^+n^+$ et $b\,n$ : les deux gènes sont **liés** (portés par le même chromosome), avec une **liaison totale** chez le mâle (pas de crossing-over chez la drosophile mâle).

**c)** Parents : ♂ $\dfrac{b^+\,n^+}{b^+\,n^+}$ et ♀ $\dfrac{b\,n}{b\,n}$ ; $F_1$ : $\dfrac{b^+\,n^+}{b\ \,n}$.

**3. a)** Mâle $F_1$ : $\dfrac{1}{2}\,b^+n^+$ et $\dfrac{1}{2}\,b\,n$. Femelle $F_1$ (crossing-over possible) : $b^+n^+$ et $b\,n$ à $\dfrac{1 - p}{2}$ chacun, $b^+n$ et $b\,n^+$ à $\dfrac{p}{2}$ chacun.

| ♂ \ ♀ | $b^+n^+$ ($\frac{1 - p}{2}$) | $b^+n$ ($\frac{p}{2}$) | $b\,n^+$ ($\frac{p}{2}$) | $b\,n$ ($\frac{1 - p}{2}$) |
|---|---|---|---|---|
| $b^+n^+$ ($\frac{1}{2}$) | $[b^+n^+]$ | $[b^+n^+]$ | $[b^+n^+]$ | $[b^+n^+]$ |
| $b\,n$ ($\frac{1}{2}$) | $[b^+n^+]$ | $[b^+n]$ | $[b\,n^+]$ | $[b\,n]$ |

D'où $[b^+n^+] = \dfrac{3 - p}{4}$, $[b\,n] = \dfrac{1 - p}{4}$, $[b^+n] = [b\,n^+] = \dfrac{p}{4}$.

**b)** $\dfrac{1 - p}{4} = 22\ \%$, donc $1 - p = 88\ \%$ et $p = 12\ \%$. Un gamète parental de la femelle représente $\dfrac{1 - p}{2} = 44\ \%$.

On en déduit que, chez la femelle, la liaison est **partielle** : un crossing-over se produit entre les deux gènes, distants de **12 cM**.

**c)** Sur 2000 drosophiles :

| Phénotype | $[b^+n^+]$ | $[b\,n]$ | $[b^+n]$ | $[b\,n^+]$ |
|---|---|---|---|---|
| Proportion | $\dfrac{3 - p}{4} = 72\ \%$ | $22\ \%$ | $3\ \%$ | $3\ \%$ |
| Effectif | 1440 | 440 | 60 | 60 |
""", note="Correction conforme au corrigé officiel (test cross, liaison totale chez le mâle ; p = 12 % ; gamète parental 44 % ; 1440, 440, 60, 60).")


# ═══════════════════════════════ C 2018 — session normale ═════════════════════

E = "bac-c-2018-sn-svt-ex3"
_add(E, r"""
**Exercice 3 (6 points)**

Afin d'étudier, chez une plante, le mode de transmission de deux caractères, couleur de la fleur et longueur de la tige, on effectue deux croisements.

- Le croisement d'une plante à fleurs rouges et tige courte avec une plante à fleurs jaunes et tige longue donne une génération $F_1$ formée de plantes à fleurs bicolores et tiges longues.

**1.** Que pouvez-vous en déduire ?

- Le croisement d'une plante de $F_1$ avec une plante à fleurs bicolores et tige courte donne une $F_2$ :
  - 200 plantes à fleurs bicolores et tiges longues ;
  - 200 plantes à fleurs bicolores et tiges courtes ;
  - 160 plantes à fleurs rouges et tiges courtes ;
  - 160 plantes à fleurs jaunes et tiges longues ;
  - 40 plantes à fleurs rouges et tiges longues ;
  - 40 plantes à fleurs jaunes et tiges courtes.

**2.** Analysez ces résultats afin de préciser si les gènes sont liés ou indépendants.

**3.** Écrivez les génotypes des parents et des individus de la $F_1$.

**4.** Expliquez les résultats de la $F_2$ en réalisant l'échiquier de croisement.

**5.** Précisez la position relative des gènes.

*Attention : utilisez les symboles suivants : $R$ = rouge ; $B$ = jaune ; $L$ = longue ; $n$ = courte.*
""", r"""
**1.** La $F_1$ est homogène : les parents sont de **race pure**.
- Tige : la $F_1$ a la tige longue, donc **$L$ domine $n$**.
- Couleur : la $F_1$ a des fleurs bicolores (rouge et jaune), donc **$R$ et $B$ sont codominants**.

**2.** Si les gènes étaient indépendants, le croisement $F_1$ × (bicolore, courte) donnerait 6 phénotypes dans les proportions $\dfrac{1}{8}$, $\dfrac{1}{8}$, $\dfrac{1}{8}$, $\dfrac{1}{8}$, $\dfrac{1}{4}$, $\dfrac{1}{4}$ (soit 100, 100, 100, 100, 200 et 200 sur 800 plantes). Or on obtient 160 rouges-courtes et 160 jaunes-longues (combinaisons des parents de départ) contre seulement 40 rouges-longues et 40 jaunes-courtes (combinaisons nouvelles) : les gènes sont **liés**, avec crossing-over (**liaison partielle**).

**3.** Parents : $\dfrac{R\,n}{R\,n}$ (rouge, courte) et $\dfrac{B\,L}{B\,L}$ (jaune, longue) ; $F_1$ : $\dfrac{R\,n}{B\,L}$ (bicolore, longue).

La plante testeuse (bicolore, courte) est $\dfrac{R\,n}{B\,n}$.

**4.** La $F_1$ produit $Rn$ et $BL$ (parentaux, $\dfrac{1 - p}{2}$ chacun), $RL$ et $Bn$ (recombinés, $\dfrac{p}{2}$ chacun). La plante testeuse produit $\dfrac{1}{2}\,Rn$ et $\dfrac{1}{2}\,Bn$.

| testeuse \ $F_1$ | $Rn$ ($\frac{1 - p}{2}$) | $BL$ ($\frac{1 - p}{2}$) | $RL$ ($\frac{p}{2}$) | $Bn$ ($\frac{p}{2}$) |
|---|---|---|---|---|
| $Rn$ ($\frac{1}{2}$) | $[Rn]$ rouge, courte | $[RBL]$ bicolore, longue | $[RL]$ rouge, longue | $[RBn]$ bicolore, courte |
| $Bn$ ($\frac{1}{2}$) | $[RBn]$ bicolore, courte | $[BL]$ jaune, longue | $[RBL]$ bicolore, longue | $[Bn]$ jaune, courte |

D'où : bicolore-longue $\dfrac{1}{4}$ ; bicolore-courte $\dfrac{1}{4}$ ; rouge-courte et jaune-longue $\dfrac{1 - p}{4}$ chacune ; rouge-longue et jaune-courte $\dfrac{p}{4}$ chacune.

Sur 800 plantes : $\dfrac{1}{4} \times 800 = 200$ ✓ ; $\dfrac{p}{4} = \dfrac{40}{800} = 5\ \%$, d'où $p = 20\ \%$ ; alors $\dfrac{1 - p}{4} \times 800 = 160$ ✓.

**5.** $p = 20\ \%$ : les deux gènes sont portés par le même chromosome, distants de **20 cM**.
""", note="Correction conforme au corrigé officiel (R et B codominants, L > n ; gènes liés ; parents Rn/Rn × BL/BL, F1 Rn/BL ; p/4 = 5 %, p = 20 %, 20 cM).")


# ═══════════════════════════════ C 2019 — session normale ═════════════════════

E = "bac-c-2019-sn-svt-ex1"
_add(E, rf"""
**Exercice 1 (7 points)**

**A.** Le tableau ci-contre est le résultat d'une électrophorèse réalisée sur l'ADN des membres d'une famille dont certains sont atteints par une maladie héréditaire.

{fig(E, 1, "Électrophorèse : allèles A et B chez le père, la mère, la fille (sains) et le fils (malade)")}

*Lecture du document :* le père ne présente que l'allèle $A$ ; la mère présente $A$ et $B$ ; la fille ne présente que $A$ ; le fils, malade, ne présente que $B$.

Écrire les génotypes des membres de cette famille.

**B.** On considère chez une drosophile trois gènes $G_1$ ($B/b$), $G_2$ ($N/n$) et $G_3$ ($R/r$).

Le tableau suivant montre des résultats partiels de quelques croisements tests réalisés chez cette drosophile.

| Gènes | ($B/b$)–($N/n$) | ($N/n$)–($R/r$) | ($B/b$)–($R/r$) |
|---|---|---|---|
| % d'un phénotype recombiné | 7 | 4 | ? |

**1.** Exploitez ces résultats en vue de déterminer :

**1.1.** si les gènes sont liés ou indépendants ;

**1.2.** les génotypes des individus croisés dans chaque colonne, sachant que les phénotypes $[Bn]$ et $[Nr]$ sont recombinés ;

**1.3.** la répartition phénotypique de chaque descendance pour les deux premières colonnes.

**2.** Déduisez la distance entre $G_1$ et $G_3$.

**3.** Dressez les cartes factorielles possibles.
""", r"""
**A.**
- La mère est saine et possède les deux allèles $A$ et $B$ : l'allèle de la maladie est **récessif**. Le fils malade ne possède que $B$, donc $B$ est l'allèle muté (récessif) et $A$ l'allèle normal (dominant).
- Le père ne possède que $A$ et pourtant son fils ne possède que $B$ : le fils n'a reçu aucun allèle de son père, ce qui s'explique si le gène est **porté par le chromosome $X$** (le fils reçoit le $Y$ de son père et le $X^B$ de sa mère).

| Individu | Père | Mère | Fille | Fils |
|---|---|---|---|---|
| Génotype | $X^AY$ | $X^AX^B$ | $X^AX^A$ | $X^BY$ |

**B. 1.1.** Dans un croisement test, deux gènes indépendants donnent 4 phénotypes à 25 % chacun ; un phénotype recombiné à 7 % (ou 4 %) est très inférieur à 25 % : les gènes sont **liés** deux à deux, avec une **liaison partielle** (crossing-over).

**B. 1.2.** $[Bn]$ est recombiné, donc les combinaisons parentales sont $BN$ et $bn$ ; $[Nr]$ est recombiné, donc les combinaisons parentales sont $NR$ et $nr$.
- 1ʳᵉ colonne : $\dfrac{B\,N}{b\,n} \times \dfrac{b\,n}{b\,n}$ ;
- 2ᵉ colonne : $\dfrac{N\,R}{n\,r} \times \dfrac{n\,r}{n\,r}$ ;
- 3ᵉ colonne : $\dfrac{B\,R}{b\,r} \times \dfrac{b\,r}{b\,r}$ (d'après les deux premières, $B$, $N$ et $R$ sont sur le même chromosome).

**B. 1.3.**

| 1ʳᵉ colonne | $[BN]$ | $[bn]$ | $[Bn]$ | $[bN]$ |
|---|---|---|---|---|
| Proportion | 43 % | 43 % | 7 % | 7 % |

| 2ᵉ colonne | $[NR]$ | $[nr]$ | $[Nr]$ | $[nR]$ |
|---|---|---|---|---|
| Proportion | 46 % | 46 % | 4 % | 4 % |

(Chaque phénotype recombiné vaut $\dfrac{p}{2}$ et chaque phénotype parental $\dfrac{1 - p}{2}$.)

**B. 2.** $G_1$–$G_2$ : $p = 2 \times 7 = 14\ \%$, soit **14 cM**. $G_2$–$G_3$ : $p = 2 \times 4 = 8\ \%$, soit **8 cM**.

Selon la position de $G_3$ : $G_1$–$G_3$ = $14 + 8 = $ **22 cM**, ou $14 - 8 = $ **6 cM**.

**B. 3.** Deux cartes factorielles possibles :
- $G_1$ — 14 cM — $G_2$ — 8 cM — $G_3$ (soit $G_1$–$G_3$ = 22 cM) ;
- $G_1$ — 6 cM — $G_3$ — 8 cM — $G_2$ (soit $G_1$–$G_2$ = 14 cM).
""", note="Correction conforme au corrigé officiel (B récessif lié à X ; gènes liés ; 43/43/7/7 et 46/46/4/4 ; 14 cM et 8 cM ; 22 ou 6 cM). Le corrigé note le génotype de la mère « X^A/Y^B » : coquille, c'est X^A X^B (la mère a deux chromosomes X). L'électrophorèse du scan est lisible mais peu nette : sa lecture est écrite dans l'énoncé et concorde avec le corrigé.")


E = "bac-c-2020-sn-svt-ex2"
_add(E, rf"""
**Exercice 2 (6 points)**

Le pedigree ci-contre est celui d'une famille dont certains membres sont atteints par une maladie oculaire.

{fig(E, 1, "Pedigree : I1 × I2 ; II2 atteint, marié à II1 ; II3 marié à II4 ; enfants à naître III1 et III2")}

**1.** L'allèle de cette maladie est-il dominant ou récessif ?

Un examen ophtalmologique est réalisé chez certains membres de cette famille. Le document 1 montre le fond de l'œil de différents sujets :
- $[a]$ s'observe chez les sujets à vision normale ;
- $[b]$ s'observe chez les sujets à vision très diminuée ;
- $[c]$ s'observe chez tous les sujets malades.

{fig(E, 2, "Document 1 : fonds d'œil a, b et c")}

**2.** Qu'apportent ces informations ?

**3.** L'allèle responsable de la maladie est-il porté par $X$, $Y$ ou par un autosome ?

**4.** Des études médicales ont précisé que le fond $[b]$ s'observe chez les hommes.

a) Que déduisez-vous ?

b) Donnez les génotypes des individus suivants : $I_2$, $II_1$, $II_2$ et $II_3$.

Sachant que la fréquence des hybrides dans cette population est de $\dfrac{1}{50}$ :

**5.** Quelle est la probabilité pour que le sujet :

a) $III_1$ soit un garçon atteint ;

b) $III_2$ soit atteint.
""", r"""
On note $S$ l'allèle normal et $M$ l'allèle de la maladie.

**1.** Le couple $I_1$ × $I_2$, sain, a un fils atteint ($II_2$) : l'allèle de la maladie était présent chez les parents sans s'exprimer. Il est **récessif**.

**2.** Il y a **trois phénotypes** de fond d'œil : $[a]$ (normal), $[c]$ (malade) et un phénotype intermédiaire $[b]$ (vision très diminuée), qui correspond aux hétérozygotes $S/M$. Les deux allèles s'expriment chez l'hétérozygote : il y a **codominance** au niveau du fond d'œil, tandis que la maladie elle-même n'apparaît que chez les homozygotes $M/M$.

**3.**
- **Porté par $Y$** : rejeté, car le père $I_1$ n'est pas atteint alors que son fils $II_2$ l'est.
- **Autosomique** : possible, si $I_1$ et $I_2$ sont tous deux hétérozygotes.
- **Porté par $X$** : possible, si la mère $I_2$ est hétérozygote ($X^SX^M$).

**4. a)** Un homme ne possède qu'un seul chromosome $X$ ; si le gène était porté par $X$, un homme ne pourrait pas être hétérozygote, donc pas présenter le fond $[b]$. Puisque des hommes ont le fond $[b]$, le gène est **autosomique**.

**b)** $I_2$ : $S/M$ (mère d'un enfant $M/M$, non atteinte) ; $II_1$ : $S/S$ ou $S/M$ (non atteinte, d'origine extérieure à la famille) ; $II_2$ : $M/M$ (atteint) ; $II_3$ : $S/S$ ou $S/M$ (non atteint, enfant de deux hétérozygotes).

**5. a)** $III_1$ est un garçon atteint ($M/M$) si sa mère $II_1$ est hybride (probabilité $\dfrac{1}{50}$) et lui transmet $M$ ($\dfrac{1}{2}$), le père $II_2$ ($M/M$) transmettant toujours $M$ ($1$), et si l'enfant est un garçon ($\dfrac{1}{2}$) :
$$P = \dfrac{1}{50} \times \dfrac{1}{2} \times 1 \times \dfrac{1}{2} = \dfrac{1}{200}.$$

**b)** $II_3$ est sain, enfant de deux hétérozygotes : il est hybride avec la probabilité $\dfrac{2}{3}$. $II_4$ est hybride avec la probabilité $\dfrac{1}{50}$. Deux hybrides ont un enfant $M/M$ avec la probabilité $\dfrac{1}{4}$ :
$$P = \dfrac{2}{3} \times \dfrac{1}{50} \times \dfrac{1}{4} = \dfrac{1}{300}.$$
""", note="Correction conforme au corrigé officiel (récessif ; codominance au niveau du fond d'œil ; Y rejeté, X et autosome possibles ; [b] chez des hommes → autosomique ; I2 S/M, II1 S/S ou S/M, II2 M/M, II3 S/S ou S/M ; 1/200 et 1/300). La correction précise que la codominance porte sur le fond d'œil, la maladie restant récessive. Comme le corrigé, elle traite II1 et II4 comme non examinés (fréquence des hybrides de la population).")


# ═══════════════════════════════ D 2024 — session normale ═════════════════════

E = "bac-d-2024-sn-svt-ex3"
_add(E, r"""
**Exercice 2 (4 points)**

Koumba décrit les membres de sa famille où sévit une maladie héréditaire :

« Ma mère Pinda est normale comme moi, mais mon père Sidi et mon fils Souley souffrent de cette maladie. Mon frère Ali est sain, contrairement à mon mari Oumar et ma fille Fatma. Raki, l'épouse de mon frère, est malade et ce couple a un garçon, Baba, sain. Habi, l'épouse de mon fils Souley, est saine et attend un enfant dans quelques mois. »

**1.** Établir l'arbre généalogique de cette famille.

**2.** Discuter le mode de transmission de cette maladie.

**3.** La séparation par électrophorèse des fragments d'ADN du gène en question a montré que Fatma ne présente qu'un seul type d'ADN. Qu'apporte cette donnée ?

**4.** Écrire les génotypes de Koumba et de ses parents.

**5.** Donner le génotype de l'enfant de Habi sachant qu'il est de sexe masculin.

*NB : on considère l'allèle normal ($N$ ou $n$) et l'allèle muté ($M$ ou $m$).*
""", r"""
**1.** Arbre généalogique :
- génération I : Sidi (homme **malade**) × Pinda (femme saine) ;
- génération II : leurs enfants Koumba (femme saine) et Ali (homme sain). Koumba est mariée à Oumar (homme **malade**), Ali à Raki (femme **malade**) ;
- génération III : enfants de Koumba et Oumar, Souley (garçon **malade**) et Fatma (fille **malade**) ; enfant d'Ali et Raki, Baba (garçon sain). Souley est marié à Habi (femme saine) ;
- génération IV : le fœtus de Souley et Habi.

**2.**
- **Récessif autosomique** : possible, si les individus sains qui ont un parent ou un enfant malade sont hétérozygotes.
- **Dominant autosomique** : possible, si les malades sont hétérozygotes et les sains homozygotes.
- **Récessif lié à $X$** : rejeté. Raki est malade ($X^mX^m$) et son fils Baba est sain : il aurait reçu $X^m$ de sa mère et serait malade.
- **Dominant lié à $X$** : rejeté. Sidi est malade ($X^MY$) et sa fille Koumba est saine : elle aurait reçu $X^M$ de son père et serait malade.
- **Lié à $Y$** : rejeté, car des femmes sont malades.

**3.** Fatma est malade et ne possède qu'un seul type d'allèle : elle est **homozygote**. Si l'allèle de la maladie était dominant, un malade homozygote $M/M$ aurait deux parents porteurs de $M$, donc deux parents malades ; or sa mère Koumba est saine. L'allèle de la maladie est donc **récessif autosomique** ($N > m$).

**4.** Koumba (saine, fille d'un père $m/m$) : $N/m$ ; Sidi (malade) : $m/m$ ; Pinda (saine) : $N/N$ ou $N/m$.

**5.** Souley est malade ($m/m$) et transmet toujours $m$. Habi est saine : $N/N$ ou $N/m$. L'enfant est donc $N/m$ (sain, porteur) ou $m/m$ (malade, seulement si Habi est $N/m$). Le gène étant autosomique, le sexe de l'enfant ne change rien à ce résultat.
""", note="Le texte en base pour cet identifiant (« Exercice 2 (4,5 pts), drosophiles b, vg, r ») ne correspond pas au sujet officiel D 2024 session normale, dont l'exercice 2 est celui de la famille de Koumba : l'énoncé est remplacé par celui du PDF (l'ancien texte reste dans ennonce_ocr). Correction conforme au corrigé officiel (arbre ; récessif X rejeté par Raki/Baba, dominant X par Sidi/Koumba ; Fatma homozygote → récessif autosomique ; Koumba N/m, Sidi m/m, Pinda N/N ou N/m ; enfant N/m ou m/m).")


# ═══════════════════════════════ D 2015 — session normale ═════════════════════

E = "bac-d-2015-sn-svt-ex4"
_add(E, r"""
**Génétique (6 points)**

Les drosophiles de type sauvage sont notamment $[b^+, vg^+, r^+]$.

**A.** On croise une drosophile femelle de type sauvage $[b^+, vg^+]$ avec un mâle $[b, vg]$. Toutes les drosophiles de la $F_1$ sont $[b^+, vg^+]$.

**1.** Quelles conclusions peut-on tirer de ce croisement ?

On croise ensuite des drosophiles femelles obtenues en $F_1$ avec des mâles $[b, vg]$. On obtient les résultats suivants :
- 51 drosophiles $[b^+, vg^+]$ ;
- 52 drosophiles $[b, vg^+]$ ;
- 48 drosophiles $[b, vg]$ ;
- 49 drosophiles $[b^+, vg]$.

**2.** Comment appelle-t-on ce type de croisement ? Quel renseignement apporte le résultat de ce croisement ?

**3.** Précisez les génotypes des parents et celui de la $F_1$. Vérifiez par des croisements les résultats obtenus.

**B.** On croise une drosophile femelle $[b^+, r]$ avec un mâle $[b, r^+]$, les deux drosophiles étant de race pure. On obtient une première génération ($F'_1$) où toutes les drosophiles sont $[b^+]$, mais tous les mâles sont $[r]$ et toutes les femelles sont $[r^+]$.

**1.** Interprétez ces résultats et écrivez les génotypes des individus croisés et ceux de la $F'_1$.

**2.** Réalisez le croisement entre les individus de la $F'_1$ puis donnez le bilan phénotypique.
""", r"""
**A. 1.** La $F_1$ est homogène : les parents sont de **race pure** (première loi de Mendel). Elle a le phénotype sauvage : $b^+ > b$ et $vg^+ > vg$.

**A. 2.** C'est un **croisement test** (test cross) : le mâle double récessif ne fournit que des gamètes $b\,vg$, donc les phénotypes des descendants reflètent les gamètes de la femelle $F_1$.

On obtient 4 phénotypes en proportions **égales** (51, 52, 48, 49 sur 200, soit environ 25 % chacun) : la femelle $F_1$ produit 4 types de gamètes équiprobables. Les deux gènes sont **indépendants** (portés par des chromosomes différents).

**A. 3.** Parents : $\dfrac{b^+}{b^+}\,\dfrac{vg^+}{vg^+}$ et $\dfrac{b}{b}\,\dfrac{vg}{vg}$ ; $F_1$ : $\dfrac{b^+}{b}\,\dfrac{vg^+}{vg}$.

Vérification (croisement test $F_1$ × $\dfrac{b}{b}\,\dfrac{vg}{vg}$) :

| ♀ $F_1$ \ ♂ | $b\,vg$ (100 %) |
|---|---|
| $b^+vg^+$ ($\frac{1}{4}$) | $[b^+vg^+]$ |
| $b^+vg$ ($\frac{1}{4}$) | $[b^+vg]$ |
| $b\,vg^+$ ($\frac{1}{4}$) | $[b\,vg^+]$ |
| $b\,vg$ ($\frac{1}{4}$) | $[b\,vg]$ |

On attend 4 phénotypes à 25 %, soit 50 de chaque sur 200 : c'est conforme aux résultats observés.

**B. 1.**
- **Gène $b$** : toute la $F'_1$ est $[b^+]$, quel que soit le sexe ; $b^+$ domine $b$ et le gène est **autosomique**.
- **Gène $r$** : les mâles ont le phénotype de leur mère ($[r]$) et les femelles celui de leur père ($[r^+]$). La transmission dépend du sexe : le gène est **porté par le chromosome $X$**. Les femelles $[r^+]$ ont reçu $X^{r^+}$ de leur père et $X^r$ de leur mère : $r^+$ domine $r$.
- Les deux gènes, l'un autosomique et l'autre lié à $X$, sont **indépendants**.

Génotypes : ♀ $\dfrac{b^+}{b^+}\,X^rX^r$ × ♂ $\dfrac{b}{b}\,X^{r^+}Y$.

$F'_1$ : femelles $\dfrac{b^+}{b}\,X^{r^+}X^r$ $[b^+r^+]$ ; mâles $\dfrac{b^+}{b}\,X^rY$ $[b^+r]$.

**B. 2.** Croisement $F'_1$ × $F'_1$ : ♀ $\dfrac{b^+}{b}\,X^{r^+}X^r$ × ♂ $\dfrac{b^+}{b}\,X^rY$.

| ♀ \ ♂ | $b^+X^r$ | $b\,X^r$ | $b^+Y$ | $b\,Y$ |
|---|---|---|---|---|
| $b^+X^{r^+}$ | ♀ $[b^+r^+]$ | ♀ $[b^+r^+]$ | ♂ $[b^+r^+]$ | ♂ $[b^+r^+]$ |
| $b^+X^r$ | ♀ $[b^+r]$ | ♀ $[b^+r]$ | ♂ $[b^+r]$ | ♂ $[b^+r]$ |
| $b\,X^{r^+}$ | ♀ $[b^+r^+]$ | ♀ $[b\,r^+]$ | ♂ $[b^+r^+]$ | ♂ $[b\,r^+]$ |
| $b\,X^r$ | ♀ $[b^+r]$ | ♀ $[b\,r]$ | ♂ $[b^+r]$ | ♂ $[b\,r]$ |

Bilan phénotypique (identique dans les deux sexes) : $[b^+r^+]$ $\dfrac{6}{16}$ ; $[b^+r]$ $\dfrac{6}{16}$ ; $[b\,r^+]$ $\dfrac{2}{16}$ ; $[b\,r]$ $\dfrac{2}{16}$.
""", note="Correction conforme au corrigé officiel (F1 b+/b vg+/vg, gènes indépendants ; gène r porté par X ; ♀ b+/b+ XrXr × ♂ b/b Xr+Y ; bilan 6/16, 6/16, 2/16, 2/16).")


# ═══════════════════════════════ D 2016 — session normale ═════════════════════

E = "bac-d-2016-sn-svt-ex4"
_add(E, rf"""
**Hérédité humaine (6 points)**

On s'intéresse à la transmission d'une maladie héréditaire qui se présente sous deux formes différentes : $X$ et $Y$. Les tableaux 1 et 2 présentent le résultat de l'analyse de l'ADN de certains membres de deux familles A et B présentant chacune l'une des formes $X$ ou $Y$.

Tableau 1 (forme $X$) :

| Famille A | père | mère | Fatma | Mariem |
|---|---|---|---|---|
| Allèle $A_1$ | ? | + | + | + |
| Allèle $A_2$ | ? | − | + | − |

Tableau 2 (forme $Y$) :

| Famille B | père | mère | Amadou | Omar |
|---|---|---|---|---|
| Allèle $A_1$ | − | ? | − | + |
| Allèle $A_2$ | + | ? | + | − |

(+ = présence ; − = absence)

*NB : chaque famille ne présente qu'une seule forme ($X$ ou $Y$) de la maladie. On sait que le père de la famille A est sain, ainsi que la mère de la famille B.*

**1.** Analysez ces résultats afin de déduire :

**a.** si le gène de chaque forme est autosomal ou porté par $X$ ;

**b.** si l'allèle de chaque forme est dominant ou récessif ;

**c.** le génotype du père de la famille A et celui de la mère de la famille B.

**2.** Le pedigree ci-contre est celui d'une autre famille C dont certains membres sont atteints de l'une des formes précitées.

{fig(E, 1, "Pedigree de la famille C : I1 (homme sain) × I2 (femme saine) ; enfants II1 (garçon malade), II2 (fille saine), II3 (fœtus)")}

**a.** Précisez, si possible, la forme de la maladie dans la famille C.

**b.** L'analyse de l'ADN de certains membres de la famille C montre la présence de l'allèle $A_1$ chez les individus $I_1$, $II_1$ et $II_2$. Que pouvez-vous en déduire ?

**3.** Écrivez les génotypes des individus $I_1$, $I_2$, $II_1$ et $II_2$ de la famille C.

**4.** Précisez les individus malades de la famille A.

**5.** Quel est le risque pour que le fœtus ($II_3$) soit une fille malade ?
""", r"""
**1. a.**
- **Forme $X$ (famille A)** : la mère ne possède que $A_1$ (homozygote $A_1A_1$). Fatma possède $A_2$, qu'elle n'a pu recevoir que de son père ; Mariem ne possède que $A_1$, elle a donc reçu $A_1$ de son père. Le père possède donc $A_1$ et $A_2$. Si le gène était porté par $X$, le père transmettrait son unique chromosome $X$, donc le **même** allèle, à toutes ses filles ; or Fatma et Mariem ont reçu de lui deux allèles différents. Le gène de la forme $X$ est donc **autosomal**.
- **Forme $Y$ (famille B)** : Omar ne possède que $A_1$, alors que son père ne possède pas $A_1$. Si le gène était autosomal, Omar aurait reçu un allèle de son père, donc $A_2$. Omar n'a reçu aucun allèle de ce gène de son père : le gène est **porté par $X$** (le père transmet $Y$ à ses fils).

**b.**
- **Forme $X$** : le père de la famille A possède les deux allèles $A_1$ et $A_2$ et il est sain ; l'allèle de la maladie, présent chez lui, est masqué : il est **récessif**.
- **Forme $Y$** : Amadou (qui ne possède que $A_2$) et Omar (qui ne possède que $A_1$) ont reçu leur chromosome $X$ de leur mère, qui possède donc $A_1$ et $A_2$. Elle est saine et porte l'allèle de la maladie : il est **récessif**.

**c.** Père de la famille A : $A_1//A_2$ ; mère de la famille B : $X^{A_1}X^{A_2}$.

**2. a.** Les parents $I_1$ et $I_2$ sont sains et ont un garçon malade $II_1$ : l'allèle de la maladie est récessif. Ce pedigree est compatible avec les deux formes (gène autosomal récessif ou gène récessif porté par $X$) : il ne permet pas, à lui seul, de préciser la forme.

**b.** Si la forme était $Y$ (gène porté par $X$), un homme ne posséderait qu'un seul allèle : $I_1$, sain, porteur de $A_1$, montrerait que $A_1$ est l'allèle normal, et $II_1$, malade, porteur de $A_1$, montrerait que $A_1$ est l'allèle de la maladie : contradiction. La famille C est donc atteinte de la **forme $X$** (autosomale récessive). $II_1$ malade possède $A_1$ : $A_1$ est l'allèle de la maladie (forme $X$), $A_2$ l'allèle normal.

**3.** $II_1$ (malade) : $A_1//A_1$ ; il a reçu $A_1$ de chacun de ses parents, sains : $I_1$ : $A_1//A_2$ et $I_2$ : $A_1//A_2$. $II_2$ (saine, porteuse de $A_1$) : $A_1//A_2$.

**4.** Dans la famille A (forme $X$, allèle de la maladie $A_1$ récessif), les malades sont les homozygotes $A_1//A_1$ : **la mère et Mariem**. Le père et Fatma ($A_1//A_2$) sont sains.

**5.** $I_1$ ($A_1//A_2$) × $I_2$ ($A_1//A_2$) : la probabilité d'un enfant malade $A_1//A_1$ est $\dfrac{1}{4}$, celle d'une fille est $\dfrac{1}{2}$ (indépendante du gène autosomal). Risque que le fœtus soit une fille malade : $\dfrac{1}{4} \times \dfrac{1}{2} = \dfrac{1}{8}$.
""", note="Le texte OCR en base contenait des valeurs fausses dans les tableaux (A2 « + » chez la mère et Mariem de la famille A, colonne « mère » absente de la famille B) et des individus mal numérotés (I3, I4) : l'énoncé est retranscrit du PDF officiel (l'ancien texte reste dans ennonce_ocr). Correction conforme au corrigé officiel (forme X autosomale récessive, forme Y liée à X récessive ; père A A1//A2, mère B XA1XA2 ; famille C forme X, A1 allèle morbide ; I1, I2, II2 A1//A2, II1 A1//A1 ; malades de A : la mère et Mariem ; risque 1/8).")


# ═══════════════════════════════ C 2015 — session normale ═════════════════════

E = "bac-c-2015-sn-svt-ex3"
_add(E, rf"""
**Génétique (6 points)**

Le document 5 représente l'arbre généalogique d'une famille dont certains membres sont atteints d'une maladie héréditaire.

{fig(E, 1, "Document 5 : arbre généalogique. I1 (homme sain) × I2 (femme malade) ; leurs enfants II1 (fille saine), II2 et II3 (garçons malades), II5 (fille saine) ; II3 × II4 (femme saine) → III2 et III3 (filles saines) ; II5 × II6 (homme sain) → III4 (garçon malade), III5 et III6 (jumelles saines), III7 (garçon sain) ; III1 (homme sain) × III2 → IV1 (garçon sain) et IV2 (enfant à naître) ; III7 × III8 (femme saine) → IV3 (garçon sain) et IV4 (enfant à naître)")}

**1.** L'allèle de cette maladie est-il :

**a.** dominant ou récessif ?

**b.** autosomique ou gonosomique ? Discutez.

**2.** On fait, par la technique d'électrophorèse, l'analyse des fragments d'ADN correspondant aux allèles $A$ et $B$ du gène impliqué dans cette maladie. Le document 6 montre les résultats obtenus chez certains membres de cette famille.

Document 6 (électrophorèse) :

| | $I_2$ | $II_2$ | $II_6$ |
|---|---|---|---|
| Fragment $A$ | bande | bande | bande |
| Fragment $B$ | — | — | bande |

**a.** Identifiez, parmi les allèles $A$ et $B$, l'allèle normal et l'allèle responsable de la maladie.

**b.** Vérifiez la validité des hypothèses retenues.

**c.** Écrivez les génotypes des individus $III_1$, $III_2$, $III_4$ et $III_7$.

**3.** Pouvez-vous préciser la nature des jumelles $III_5$ et $III_6$ ?

**4.** Quel est le risque pour que :

**a.** $IV_2$ soit une fille malade ;

**b.** $IV_4$ soit malade ?

*NB : on considère que la fréquence des hybrides dans la population à laquelle appartient cette famille est $\dfrac{{1}}{{40}}$.*
""", r"""
**1. a.** Le couple $II_5 \times II_6$, sain, a un garçon malade $III_4$ : l'allèle de la maladie, présent chez au moins un des parents, y est masqué. Il est **récessif**.

**b.**
- **Gène porté par $Y$** : rejeté, car la maladie touche aussi des femmes ($I_2$).
- **Gène porté par $X$** : possible. La mère malade $I_2$ ($X^mX^m$) a tous ses garçons malades ($II_2$, $II_3$) ; ses filles $II_1$ et $II_5$ sont saines et conductrices ($X^NX^m$) ; $II_5$ transmet $X^m$ à son fils $III_4$ ; le père malade $II_3$ ($X^mY$) a des filles saines conductrices ($III_2$, $III_3$).
- **Gène autosomique** : possible.

**2. a.** $I_2$ et $II_2$ sont malades et ne possèdent que le fragment $A$ : ils sont homozygotes pour l'allèle de la maladie. **$A$ est l'allèle responsable de la maladie, $B$ l'allèle normal** ($B > A$).

**b.** $II_6$ est un homme sain qui possède **deux** allèles, $A$ et $B$ : le gène est présent en deux exemplaires chez l'homme, il n'est donc pas porté par $X$. Il est **autosomique**. $II_6$, hétérozygote $B//A$ et sain, confirme que $A$ est récessif. Hypothèse retenue : **allèle récessif autosomique**.

**c.**
- $III_1$ (homme sain extérieur à la famille) : $B//B$ ou $B//A$ ;
- $III_2$ (saine, fille du père malade $II_3$ qui lui a transmis $A$) : $B//A$ ;
- $III_4$ (malade) : $A//A$ ;
- $III_7$ (sain, fils de $II_5$ et $II_6$ tous deux $B//A$) : $B//B$ ou $B//A$.

**3.** Non. $III_5$ et $III_6$ sont deux filles saines, de génotype $B//B$ ou $B//A$ : elles peuvent être de vraies jumelles (même génotype) comme de fausses jumelles ; les données ne permettent pas de trancher.

**4. a.** $III_2$ est sûrement $B//A$. Pour que $IV_2$ soit malade, il faut que $III_1$ soit hybride (probabilité $\dfrac{1}{40}$), puis que l'enfant reçoive $A$ de chacun ($\dfrac{1}{4}$) ; la probabilité d'une fille est $\dfrac{1}{2}$ :
$$P = \dfrac{1}{40} \times \dfrac{1}{4} \times \dfrac{1}{2} = \dfrac{1}{320}.$$

**b.** $III_7$ est sain, issu de deux parents $B//A$ : la probabilité qu'il soit hybride est $\dfrac{2}{3}$. $III_8$, issue de la population, est hybride avec la probabilité $\dfrac{1}{40}$ :
$$P = \dfrac{2}{3} \times \dfrac{1}{40} \times \dfrac{1}{4} = \dfrac{1}{240}.$$
""", note="Document 6 retranscrit en tableau (scan peu lisible ; lecture confirmée par la version dactylographiée et le corrigé : I2 et II2 n'ont que A, II6 a A et B). Corrections conformes au corrigé officiel pour 1, 2 et 3. Question 4 : le corrigé officiel donne 1/40 × 1/40 × 1/4 × 1/2 et 1/40 × 1/40 × 1/4, ce qui est faux : III2 est sûrement B//A (son père II3 est malade), donc un seul facteur 1/40 pour IV2 (1/320) ; III7, sain et issu de deux hétérozygotes, est hybride avec la probabilité 2/3 et non 1/40 (IV4 : 1/240).")


# ═══════════════════════════════ C 2013 — session normale ═════════════════════

E = "bac-c-2013-sn-svt-ex3"
_add(E, r"""
**Génétique (6 points)**

On se propose d'étudier la transmission de deux caractères chez la drosophile à partir des croisements suivants.

**1er croisement** : entre 2 souches de drosophiles :
- $P_1$ : souche mutante à ailes vestigiales et yeux pourpres ;
- $P_2$ : souche sauvage à ailes normales et yeux rouges.

La génération $F_1$ est constituée de drosophiles de type sauvage.

**1.** Que déduisez-vous ?

**2e croisement** : le croisement entre les individus de $F_1$ donne une génération $F_2$ dans laquelle on dénombre :
- 727 drosophiles de type sauvage ;
- 208 drosophiles de type mutant ;
- 33 drosophiles à ailes normales et yeux pourpres ;
- 32 drosophiles à ailes vestigiales et yeux rouges.

**2.** Interprétez, croisement à l'appui, les résultats obtenus.

**3.** Déduisez la position des gènes étudiés.

**4.** Donnez la répartition attendue sur 1000 drosophiles issues d'un croisement d'une femelle de $F_1$ × mâle mutant.
""", r"""
Notations : $vg^+$ (ailes normales) / $vg$ (ailes vestigiales) ; $pr^+$ (yeux rouges) / $pr$ (yeux pourpres).

**1.** Il s'agit d'un **dihybridisme** (deux caractères). La $F_1$ est homogène : les parents sont de race pure (1re loi de Mendel). La $F_1$ ne présente que les phénotypes sauvages : les allèles sauvages sont **dominants** : $vg^+ > vg$ et $pr^+ > pr$.

**2.** Si les gènes étaient indépendants, la $F_2$ présenterait les proportions $\dfrac{9}{16}$, $\dfrac{3}{16}$, $\dfrac{3}{16}$, $\dfrac{1}{16}$, soit environ 562, 188, 188 et 63 drosophiles sur 1000. Les résultats observés (727, 208, 33, 32) en sont très éloignés : les phénotypes parentaux sont largement majoritaires, les phénotypes recombinés rares. Les deux gènes sont donc **liés** (portés par le même chromosome), avec une **liaison partielle** (crossing-over).

Chez la drosophile, le crossing-over n'a lieu que chez la femelle.

Croisement : $F_1$ ♀ $\dfrac{vg^+\ pr^+}{vg\ \ pr}$ × $F_1$ ♂ $\dfrac{vg^+\ pr^+}{vg\ \ pr}$.

Gamètes, en notant $p$ le taux de recombinaison :
- femelle : $vg^+pr^+$ et $vg\,pr$ (parentaux) : $\dfrac{1-p}{2}$ chacun ; $vg^+pr$ et $vg\,pr^+$ (recombinés) : $\dfrac{p}{2}$ chacun ;
- mâle (liaison totale) : $vg^+pr^+$ : $\dfrac{1}{2}$ ; $vg\,pr$ : $\dfrac{1}{2}$.

| ♀ \ ♂ | $vg^+pr^+$ $\left(\dfrac{1}{2}\right)$ | $vg\,pr$ $\left(\dfrac{1}{2}\right)$ |
|---|---|---|
| $vg^+pr^+$ $\left(\dfrac{1-p}{2}\right)$ | $[vg^+pr^+]$ $\dfrac{1-p}{4}$ | $[vg^+pr^+]$ $\dfrac{1-p}{4}$ |
| $vg\,pr$ $\left(\dfrac{1-p}{2}\right)$ | $[vg^+pr^+]$ $\dfrac{1-p}{4}$ | $[vg\,pr]$ $\dfrac{1-p}{4}$ |
| $vg^+pr$ $\left(\dfrac{p}{2}\right)$ | $[vg^+pr^+]$ $\dfrac{p}{4}$ | $[vg^+pr]$ $\dfrac{p}{4}$ |
| $vg\,pr^+$ $\left(\dfrac{p}{2}\right)$ | $[vg^+pr^+]$ $\dfrac{p}{4}$ | $[vg\,pr^+]$ $\dfrac{p}{4}$ |

Répartition phénotypique théorique : $[vg^+pr^+]$ $\dfrac{3-p}{4}$ ; $[vg\,pr]$ $\dfrac{1-p}{4}$ ; $[vg^+pr]$ $\dfrac{p}{4}$ ; $[vg\,pr^+]$ $\dfrac{p}{4}$. Elle explique bien les deux classes recombinées peu nombreuses et à peu près égales (33 et 32).

**3.** Les deux classes recombinées représentent $\dfrac{p}{4} + \dfrac{p}{4} = \dfrac{p}{2}$ de la $F_2$ :
$$\dfrac{p}{2} = \dfrac{33 + 32}{1000} = 0{,}065 \quad\Rightarrow\quad p = 0{,}13 = 13\ \%.$$
Les deux gènes sont portés par le même chromosome et distants de **13 centimorgans** (13 cM). (Avec $p = 0{,}13$, on attend environ 717, 218, 32 et 32 drosophiles sur 1000, proche des effectifs observés.)

**4.** Croisement test : $F_1$ ♀ $\dfrac{vg^+\ pr^+}{vg\ \ pr}$ × ♂ $\dfrac{vg\ \ pr}{vg\ \ pr}$. Le mâle ne fournit que des gamètes $vg\,pr$ : les phénotypes des descendants reflètent les gamètes de la femelle.
- $[vg^+pr^+]$ : $\dfrac{1-p}{2} = 0{,}435$, soit **435** drosophiles ;
- $[vg\,pr]$ : $0{,}435$, soit **435** drosophiles ;
- $[vg^+pr]$ : $\dfrac{p}{2} = 0{,}065$, soit **65** drosophiles ;
- $[vg\,pr^+]$ : $0{,}065$, soit **65** drosophiles.
""", note="Exercice absent de la base (squelette vide) : énoncé retranscrit du PDF officiel C 2013 session normale. Correction conforme au corrigé officiel (gènes liés, crossing-over chez la femelle seulement ; répartition (3−p)/4, (1−p)/4, p/4, p/4 ; distance 13 cM ; croisement test 435, 435, 65, 65). Le corrigé calcule p à partir de la seule classe de 32 (p = 0,128 ≈ 13 %) ; ici p est calculé à partir des deux classes recombinées (p = 0,13), même conclusion.")


# ═══════════════════════════════ C 2014 — session normale ═════════════════════

E = "bac-c-2014-sn-svt-ex3"
_add(E, r"""
**Génétique (6 points)**

Chez une famille atteinte d'une maladie héréditaire rare, on réalise une électrophorèse des allèles (fragments d'ADN) du gène responsable de cette maladie. Les résultats sont donnés par le tableau suivant ($I_1$ et $I_2$ sont les parents ; $II_1$, $II_2$ et $II_3$ leurs enfants) :

| Individus | $I_1$ | $I_2$ | $II_1$ | $II_2$ | $II_3$ |
|---|---|---|---|---|---|
| Fragment $A_1$ | bande | bande | — | — | bande |
| Fragment $A_2$ | bande | bande | bande | bande | bande |
| Phénotype | ♂ | ♀ saine | ♂ malade | ♀ | ♀ |

**1.** Quel est l'allèle responsable de cette maladie ? Pourquoi ?

**2.** S'agit-il d'une maladie :

**a.** récessive ou dominante ? Pourquoi ?

**b.** liée au sexe ou autosomale ? Pourquoi ?

**3.** Dressez le pedigree de cette famille.

**4.** Précisez les génotypes des individus de cette famille.

**5.** La femme $II_3$ se marie à un homme phénotypiquement normal. Quelle est la probabilité pour que leur premier enfant soit un garçon malade ?
""", r"""
**1.** $II_1$ est malade et ne possède que le fragment $A_2$ : l'allèle responsable de la maladie est **$A_2$** ($A_1$ est l'allèle normal).

**2. a.** La femme $I_2$ possède les deux allèles $A_1$ et $A_2$ (hétérozygote) et elle est saine : l'allèle $A_2$ de la maladie est masqué, il est **récessif** ($A_1 > A_2$).

**b.** L'homme $I_1$ possède deux allèles, $A_1$ et $A_2$. Si le gène était porté par $X$, un homme n'en posséderait qu'un seul exemplaire ; s'il était porté par $Y$, la femme $I_2$ n'en posséderait aucun. Le gène est donc **autosomal**.

**3.** Pedigree :
- génération I : $I_1$ (homme, hétérozygote donc **sain**) × $I_2$ (femme saine) ;
- génération II : $II_1$ (garçon **malade**), $II_2$ (fille ne possédant que $A_2$, donc **malade**), $II_3$ (fille hétérozygote, donc **saine**).

**4.** $I_1$ : $A_1//A_2$ ; $I_2$ : $A_1//A_2$ ; $II_1$ : $A_2//A_2$ ; $II_2$ : $A_2//A_2$ ; $II_3$ : $A_1//A_2$.

**5.** $II_3$ est $A_1//A_2$. L'enfant ne peut être malade ($A_2//A_2$) que si le mari, phénotypiquement normal, est lui aussi hétérozygote $A_1//A_2$.
- La maladie étant **rare**, le mari est très probablement homozygote $A_1//A_1$ : la probabilité d'avoir un enfant malade est alors **nulle**.
- S'il était hétérozygote, la probabilité d'un enfant malade serait $\dfrac{1}{2} \times \dfrac{1}{2} = \dfrac{1}{4}$, et celle d'un garçon malade $\dfrac{1}{4} \times \dfrac{1}{2} = \dfrac{1}{8}$.

L'énoncé ne donnant pas la fréquence des hétérozygotes dans la population, on ne peut pas donner une valeur unique : la probabilité vaut $\dfrac{1}{8} \times f$, où $f$ est la probabilité que le mari soit hétérozygote, très faible pour une maladie rare.
""", note="Exercice absent de la base (squelette vide) : énoncé retranscrit du PDF officiel C 2014 session normale ; le tableau d'électrophorèse est retranscrit (bande A2 de I1 peu visible sur le scan, confirmée par la version dactylographiée et par le corrigé, qui qualifie I1 de « mâle hybride »). Questions 1 et 2 conformes au corrigé officiel (A2 allèle muté, récessif, autosomal). Question 3 : le pedigree du corrigé représente II3 par un carré, alors que le tableau la donne de sexe féminin (♀) ; corrigé ici. Les questions 4 et 5 ne sont pas traitées dans le corrigé : les génotypes découlent directement du tableau ; pour la question 5, l'énoncé ne donne pas la fréquence des hétérozygotes, la réponse est donc donnée en fonction de celle-ci (1/8 si le mari est hétérozygote, quasi nulle sinon).")


# ─────────────────────────────────────────────────────────────────────────────
CHECKS: dict[str, list[str]] = {
    "bac-d-2017-sn-svt-ex4": [
        "close(Rational(18, 100)/4, Rational(45, 1000))",
        "close(Rational(1, 2) + Rational(1, 2)*Rational(41, 100), Rational(705, 1000))",
        "close(Rational(705, 1000)*200, 141) and close(Rational(205, 1000)*200, 41) and close(Rational(45, 1000)*200, 9)",
    ],
    "bac-d-2022-sn-svt-ex2": [
        "close((1 - Rational(8, 100))/2, Rational(46, 100)) and close(Rational(8, 100)/2, Rational(4, 100))",
        "close(Rational(46, 100)*500, 230) and close(Rational(4, 100)*500, 20) and 230 + 20 + 20 + 230 == 500",
    ],
    "bac-d-2023-sn-svt-ex3": [
        "close(Rational(3, 4)*Rational(1, 2), Rational(6, 16)) and close(Rational(1, 4)*Rational(1, 2), Rational(2, 16))",
        "close(Rational(6, 16)*224, 84) and close(Rational(2, 16)*224, 28) and 84 + 84 + 28 + 28 == 224",
    ],
    "bac-d-2018-sn-svt-ex2": [
        "close((1 - Rational(16, 100))/2, Rational(42, 100))",
        "abs(N(1 - sqrt(Rational(88, 100))) - 0.062) < 0.001 and close(((1 - sqrt(Rational(88, 100)))*2 - (1 - sqrt(Rational(88, 100)))**2)/4, Rational(3, 100))",
        "close((1 - Rational(10, 100))/2, Rational(45, 100)) and close(Rational(22, 100)/2, Rational(11, 100))",
    ],
    "bac-c-2017-sn-svt-ex4": [
        "close((1 - Rational(20, 100))/2*Rational(1, 2), Rational(20, 100)) and close(Rational(20, 100)/2*Rational(1, 2), Rational(5, 100))",
        "close(Rational(1, 2)*1 + Rational(1, 2)*Rational(40, 100), Rational(70, 100)) and close(Rational(1, 2)*Rational(40, 100), Rational(20, 100))",
        "close(Rational(40, 100)*700, 280) and close(Rational(10, 100)*700, 70)",
    ],
    "bac-c-2020-sn-svt-ex1": [
        "close((1 - Rational(17, 100))/2, Rational(415, 1000)) and close(Rational(17, 100)/2, Rational(85, 1000))",
        "close(Rational(1, 2) + Rational(1, 2)*Rational(415, 1000), (3 - Rational(17, 100))/4) and close((3 - Rational(17, 100))/4, Rational(7075, 10000))",
        "close((1 - Rational(17, 100))/4, Rational(2075, 10000)) and close(Rational(17, 100)/4, Rational(425, 10000))",
    ],
    "bac-c-2023-sn-svt-ex4": [
        "close((1 - Rational(12, 100))/4, Rational(22, 100)) and close((1 - Rational(12, 100))/2, Rational(44, 100))",
        "close((3 - Rational(12, 100))/4*2000, 1440) and close(Rational(22, 100)*2000, 440) and close(Rational(12, 100)/4*2000, 60)",
    ],
    "bac-c-2018-sn-svt-ex3": [
        "200 + 200 + 160 + 160 + 40 + 40 == 800 and close(Rational(40, 800)*4, Rational(20, 100))",
        "close((1 - Rational(20, 100))/4*800, 160) and close(Rational(1, 4)*800, 200)",
    ],
    "bac-c-2019-sn-svt-ex1": [
        "close((1 - Rational(14, 100))/2, Rational(43, 100)) and close((1 - Rational(8, 100))/2, Rational(46, 100))",
        "14 + 8 == 22 and 14 - 8 == 6",
    ],
    "bac-c-2020-sn-svt-ex2": [
        "close(Rational(1, 50)*Rational(1, 2)*1*Rational(1, 2), Rational(1, 200))",
        "close(Rational(2, 3)*Rational(1, 50)*Rational(1, 4), Rational(1, 300))",
    ],
    "bac-d-2015-sn-svt-ex4": [
        "51 + 52 + 48 + 49 == 200 and all(abs(k - 50) <= 2 for k in (51, 52, 48, 49))",
        "close(Rational(3, 4)*Rational(1, 2), Rational(6, 16)) and close(Rational(1, 4)*Rational(1, 2), Rational(2, 16))",
    ],
    "bac-d-2016-sn-svt-ex4": [
        "close(Rational(1, 4)*Rational(1, 2), Rational(1, 8))",
    ],
    "bac-c-2015-sn-svt-ex3": [
        "close(Rational(1, 40)*Rational(1, 4)*Rational(1, 2), Rational(1, 320))",
        "close(Rational(2, 3)*Rational(1, 40)*Rational(1, 4), Rational(1, 240)) and close((Rational(2, 4))/(Rational(3, 4)), Rational(2, 3))",
    ],
    "bac-c-2013-sn-svt-ex3": [
        "727 + 208 + 33 + 32 == 1000 and close(Rational(33 + 32, 1000)*2, Rational(13, 100))",
        "close((3 - Rational(13, 100))/4*1000, Rational(7175, 10)) and close((1 - Rational(13, 100))/4*1000, Rational(2175, 10)) and close(Rational(13, 100)/4*1000, Rational(325, 10))",
        "close((1 - Rational(13, 100))/2*1000, 435) and close(Rational(13, 100)/2*1000, 65)",
        "abs(Rational(9, 16)*1000 - 562) < 1 and abs(Rational(3, 16)*1000 - 188) < 1 and abs(Rational(1, 16)*1000 - 63) < 1",
    ],
    "bac-c-2014-sn-svt-ex3": [
        "close(Rational(1, 2)*Rational(1, 2)*Rational(1, 2), Rational(1, 8))",
    ],
}
