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
}
