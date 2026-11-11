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
}
