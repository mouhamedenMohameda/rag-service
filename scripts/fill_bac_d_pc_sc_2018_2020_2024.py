"""Remplit 12 énoncés Bac D · PC · Session Complémentaire (2018, 2020, 2024).

Source : transcription manuelle des sujets officiels (qualité ~60 %).
NE TOUCHE PAS `validated_by_admin`. Backup auto avant écriture.

Usage :
    .venv/bin/python scripts/fill_bac_d_pc_sc_2018_2020_2024.py --dry-run
    .venv/bin/python scripts/fill_bac_d_pc_sc_2018_2020_2024.py
    .venv/bin/python scripts/fill_bac_d_pc_sc_2018_2020_2024.py --force
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

    # ═══════════════ BAC D · PC · 2018 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2018, "sc", 1): r"""Exercice 1 (5pts)
À une température constante, on réalise la réduction d'un volume $V_1$ d'une solution $(S_1)$ de peroxodisulfate de potassium $K_2S_2O_8$ de concentration molaire $C_1$ par un volume $V_2$ d'une solution $(S_2)$ d'iodure de potassium KI de concentration molaire $C_2$, avec $C_2=2C_1$. On donne $E^0_{I_2/I^-}=0{,}55$ V et $E^0_{S_2O_8^{2-}/SO_4^{2-}}=2{,}1$ V.
1. Écrire les équations des deux demi-réactions et déduire l'équation bilan.
2. À l'instant $t=0$ on mélange $n_{01}=10$ mmol d'ions peroxodisulfate et $n_{02}=20$ mmol d'ions iodure pour obtenir un volume total $V=1$ L.
2.1 Dresser le tableau d'avancement de la réaction.
2.2 Déterminer les concentrations molaires initiales $[S_2O_8^{2-}]_0$ et $[I^-]_0$ respectives des ions peroxodisulfate et des ions iodures dans le mélange. Déduire $C_1$ et $C_2$.
3. À la date $t=0$, on divise le mélange précédent en 10 prélèvements identiques. Pour déterminer la quantité de matière de diiode formé à une date $t>0$, on refroidit à chaque fois l'un des prélèvements en y versant de l'eau glacée puis on dose le diiode formé par une solution de thiosulfate de sodium $Na_2S_2O_3$ de concentration molaire $C_3=4.10^{-1}$ mol/L. La réaction de dosage, rapide et totale, est $2S_2O_3^{2-}+I_2\rightarrow S_4O_6^{2-}+2I^-$. Ce dosage a permis de tracer la courbe de variation de la quantité de matière du diiode en fonction du temps (voir fig 1).
3.1 Pourquoi refroidit-on chaque prélèvement ? Quel(s) facteur(s) cinétique(s) met-on en évidence ?
3.2 Calculer le volume $V_3$ de la solution de thiosulfate de sodium nécessaire pour doser la quantité de diiode $I_2$ formé dans un prélèvement à la date $t=40$ min.
4. Calculer la concentration molaire théorique de diiode à la fin de la réaction. Ce résultat est-il en accord avec le résultat expérimental ?
5. Définir la vitesse de la réaction, la calculer à la date $t=40$ min. Déduire sa vitesse volumique $V_{vol}$.""",

    ("D", "pc", 2018, "sc", 2): r"""Exercice 2 (4pts)
Deux solutions aqueuses de monoacides $(A_1H)$ et $(A_2H)$, de même concentration molaire $C_1=C_2=C=10^{-2}$ mol/L, ont respectivement pour pH : $pH_1=3{,}4$ et $pH_2=2$.
1. Montrer que l'un des acides, que l'on précisera, est fort et l'autre est faible.
2. Écrire les équations de leur dissociation dans l'eau.
3. La solution de l'acide faible est l'acide éthanoïque de $pKa=4{,}8$. L'expression de son pH en fonction de C et du pKa du couple acide-base est $pH=\dfrac{1}{2}(pKa-\log C)$. À un volume $V=5$ mL de la solution de cet acide, on ajoute un volume $V_e$ d'eau pour obtenir une nouvelle solution de $pH'=3{,}9$.
3.1 Calculer le volume d'eau $V_e$.
3.2 Quel est l'effet d'une dilution sur l'ionisation d'un acide faible.
4. On fait réagir l'acide éthanoïque précédent avec une amine $RNH_2$ pour obtenir un composé organique A.
4.1 Écrire l'équation bilan de la réaction.
4.2 La masse molaire moléculaire du composé organique A obtenu est $M=73$ g/mol. Donner les formules semi-développées du composé organique A et de l'amine ainsi que leurs noms.""",

    ("D", "pc", 2018, "sc", 3): r"""Exercice 3 (6pts)
Sur un tremplin de surface parfaitement lisse incliné d'un angle $\alpha=30^\circ$ par rapport à l'horizontale, un jouet S d'enfant constitué d'une petite voiture initialement au repos au point A, est tiré par une force constante $\vec{F}$, inclinée d'un angle $\theta$ par rapport au plan du tremplin. Ce jouet S a une masse $m=100$ g. On donne $\cos\theta=0{,}8$ ; $AB=2$ m ; $AC=2{,}7$ m.
1. La vitesse atteinte par S au point B après le parcours rectiligne AB est égale à $V_B=4$ m/s.
1.1 Calculer la valeur de F.
1.2 Déterminer la nature du mouvement de S sur le trajet AB.
1.3 Au point B, l'action de la force cesse, le solide poursuit son mouvement rectiligne jusqu'au sommet C du tremplin. Déterminer la nature du mouvement de S sur le trajet BC. Calculer la vitesse de S au point C.
2. Le solide quitte le tremplin au point C, origine du repère $(C,\vec{i},\vec{j})$.
2.1 Déterminer l'équation cartésienne de la trajectoire de S dans le repère $(C,\vec{i},\vec{j})$. L'instant de passage de S en C est considéré comme origine des dates.
2.2 S atteint le sol au point d'impact D.
2.2.1 Calculer les coordonnées du point D.
2.2.2 Sachant que le solide est brisé s'il touche le sol avec une vitesse supérieure à 5 m/s, dans quel état se trouve S après la chute.""",

    ("D", "pc", 2018, "sc", 4): r"""Exercice 4 (5pts)
On considère le système constitué d'une barre MN de cuivre de longueur $l=20$ cm qui peut se déplacer sur deux rails horizontaux et parallèles $AA'$ et $BB'$, d'un générateur de f.e.m. $E=4$ V, de deux interrupteurs $K_1$ et $K_2$. L'ensemble du système plonge dans un champ magnétique uniforme $\vec{B}$ de valeur $B=1$ T qui reste vertical. On néglige toutes les résistances devant celle de la barre qui est $r=5\,\Omega$.
1. On ferme l'interrupteur $K_1$ et on laisse $K_2$ ouvert.
1.1 Calculer l'intensité I du courant qui traverse la barre ainsi que l'intensité de la force électromagnétique exercée sur la barre.
1.2 Déterminer le sens du champ $\vec{B}$ pour que la barre se déplace vers la gauche. Déduire les positions des pôles de l'aimant en U.
1.3 On relie le milieu de la barre à l'extrémité isolée d'un ressort à spires non jointives de masse négligeable et de raideur K ; l'autre extrémité est fixée à un support fixe. La barre s'immobilise alors que le ressort est allongé de 2 cm. Représenter les forces agissant sur la barre et calculer la valeur de K.
2. On ferme l'interrupteur $K_2$, on ouvre $K_1$ et on supprime le ressort. On déplace la tige avec une vitesse constante $V=4$ m/s de la gauche vers la droite.
2.1 Donner l'expression du flux à un instant t quelconque et calculer la force électromotrice (f.e.m.) induite e.
2.2 Déterminer l'intensité du courant induit et préciser son sens.
2.3 Préciser les caractéristiques de la force électromagnétique $\vec{f}$ créée lors du déplacement.""",

    # ═══════════════ BAC D · PC · 2020 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2020, "sc", 1): r"""Exercice 1 (4,5pts)
Pour réaliser la réaction entre l'eau oxygénée $H_2O_2$ et les ions iodures $I^-$, on dispose : d'une solution d'iodure de potassium ($C_1=0{,}1$ mol/L), d'acide sulfurique concentré, et d'eau oxygénée ($C_2=0{,}1$ mol/L). L'équation bilan est : $H_2O_2+2I^-+2H^+ \rightarrow I_2+2H_2O$. On réalise deux expériences :
- Exp 1 : 90 mL d'iodure de potassium + 10 mL d'eau oxygénée.
- Exp 2 : 50 mL d'iodure de potassium + 10 mL d'eau oxygénée + 40 mL d'eau distillée.
Les mesures de l'avancement x ont permis de tracer les courbes $C_1$ et $C_2$.
1.1 L'ion $H^+$ joue-t-il le rôle d'un réactif ou d'un catalyseur ? Justifier.
1.2 Calculer la quantité de matière initiale de $H_2O_2$ et d'ions $I^-$ dans chaque mélange. Quel est le réactif limitant ?
2.1 Déterminer graphiquement la vitesse instantanée de la réaction à $t=20$ min pour $C_1$ et $C_2$.
2.2 Déduire la vitesse de disparition de $I^-$ à cette date pour chaque expérience.
2.3 Préciser le facteur cinétique justifiant la disposition des courbes. Associer chaque expérience à sa courbe.
3. Peut-on à l'aide d'une seule courbe, mettre en évidence l'influence de ce facteur ? Comment ?
4. Déterminer le temps $t_{1/2}$ de la demi-réaction pour l'expérience 1.""",

    ("D", "pc", 2020, "sc", 2): r"""Exercice 2 (4,5pts)
On veut déterminer le degré d'acidité d'un vinaigre (masse d'acide acétique $CH_3-COOH$ dans 100 g de vinaigre). Densité = 1,01. On dilue 10 fois le vinaigre pour obtenir une solution S. On dose 20 mL de S par de la soude à $C_b=0{,}1$ mol/L.
1. Citer le matériel nécessaire pour cette dilution.
2. L'équivalence est obtenue pour 20,8 mL de soude.
2.1 Quelle est la concentration $C_1$ de S ?
2.2 Quelle est la concentration C en acide du vinaigre ?
2.3 Quel est le degré d'acidité du vinaigre ?
3.1 Quel volume de soude à $0{,}1$ mol/L doit-on verser dans 20 mL d'acide acétique à $0{,}1$ mol/L pour obtenir une solution de $pH=4{,}8$ ?
3.2 Quelles sont les caractéristiques de cette solution obtenue.
Données : C : 12 g/mol ; H : 1 g/mol ; O : 16 g/mol ; $pKa=4{,}8$.""",

    ("D", "pc", 2020, "sc", 3): r"""Exercice 3 (6pts)
Un ressort de raideur $K=10$ N/m est fixé en A sur un plan horizontal AB. Un solide S ($m=100$ g) y est accroché. À l'équilibre, G est en O.
1. On déplace S de 4 cm de sa position d'équilibre et on l'abandonne sans vitesse initiale à $t=0$.
1.1 Établir l'équation différentielle du mouvement de G.
1.2 Déterminer l'équation horaire du mouvement de S.
2. Exprimer à la date t, l'énergie mécanique totale E du système (ressort + solide + terre) en fonction de K et de l'élongation maximale $x_m$.
3. Au passage par O dans le sens positif, S se détache du ressort, parcourt AB et le quitte en B pour tomber en C au sol ($h=2$ m).
3.1 Déterminer l'équation de la trajectoire du mouvement après B dans le repère $(B;\vec{i};\vec{j})$. Conclure.
3.2 Trouver l'abscisse du point de chute C.
3.3 Calculer la vitesse du solide S à son arrivée en C.""",

    ("D", "pc", 2020, "sc", 4): r"""Exercice 4 (5pts)
Étude d'un satellite en orbite circulaire autour de la terre à l'altitude $h_0=400$ km. Données : $G=6{,}67.10^{-11}$ S.I., $M_T=6.10^{24}$ kg, $R_T=6400$ km.
1.1 Déterminer la nature de son mouvement (soumis uniquement au champ gravitationnel).
1.2 Exprimer la vitesse $V_0$ en fonction de G, M, R et $h_0$ et calculer sa valeur.
1.3 Établir l'expression de sa période $T_0$ en fonction de R, $h_0$, $V_0$ et la calculer.
2. Étude énergétique ($E_p=-GmM/r$).
2.1 Exprimer l'énergie mécanique $E_{m0}$ en fonction de M, m et $r_0$.
2.2 Exprimer $E_{m0}$ et l'énergie cinétique $E_{c0}$ en fonction de $E_{p0}$.
2.3 Exprimer l'énergie W fournie par les moteurs pour passer de l'orbite $r_0$ à une orbite r plus haute.""",

    # ═══════════════ BAC D · PC · 2024 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "pc", 2024, "sc", 1): r"""Exercice 1 (4,25pts)
1.1 Donner les noms systématiques de : $CH_3-CH(OH)-CH_3$ ; $HCOOH$ ; $CH_3-CO-CH_2-CH_3$.
1.2 On fait réagir $CH_3-CH(OH)-CH_3$ avec $HCOOH$. Écrire l'équation et nommer le produit organique.
2. L'hydrolyse d'un ester E fournit un acide A ($M=60$ g/mol) et un alcool B ($C_4H_{10}O$).
2.1 Déterminer la formule brute, semi-développée et le nom de A.
2.2.1 L'oxydation ménagée de B par $KMnO_4$ donne $B'$. $B'$ réagit avec la DNPH et le réactif de Schiff. Préciser la classe de B. Donner les formules semi-développées et noms de B et $B'$ (sachant qu'elles sont ramifiées).
2.2.2 Donner les formules semi-développées d'un isomère de position et d'un isomère de chaîne de B.
2.3 En déduire la formule semi-développée et le nom de l'ester E.""",

    ("D", "pc", 2024, "sc", 2): r"""Exercice 2 (3,5pts)
Cinq solutions (A : $NaCl$, B : $NaOH$, C : $HNO_3$, D : $C_6H_5COOH$, E : $CH_3-NH_2$) ont la même concentration $C=10^{-2}$ mol/L.
1. Identifier les solutions correspondant aux pH mesurés : 3 ; 10,8 ; 11 ; 7 ; 3,65.
2. Calculer les concentrations des espèces dans la solution D. En déduire le pKa du couple correspondant.
3. Trouver la relation entre $V_B$ et $V_C$ pour obtenir un mélange de $pH=7$.
4. On mélange 10 mL de C avec 10 mL de A. Calculer le pH.
5. On veut préparer une solution tampon à partir de B et D. Quel volume de B ajouter à 10 cm³ de D ? Quel sera le pH ?""",

    ("D", "pc", 2024, "sc", 3): r"""Exercice 3 (5pts)
Une piste comporte une partie horizontale AB, une partie BC inclinée d'angle $\alpha$ ($\sin\alpha=0{,}42$, $\cos\alpha=0{,}9$, $BC=45$ m) et un fossé de largeur d. Un motard ($m=200$ kg) passe en A à $t=0$ et atteint B à $t=5$ s.
1.1 D'après le graphe $v=f(t)$, écrire l'équation de la droite et déduire l'accélération a.
1.2 Calculer la distance AB.
2. Sur BC, le motard exerce une force motrice $F=1660$ N et subit $f=500$ N. Calculer l'accélération sur BC et la vitesse $v_C$.
3.1 Étudier le mouvement après C dans le repère $(C;x;y)$ et calculer l'équation de la trajectoire.
3.2 Calculer la largeur maximale d du fossé pour ne pas y tomber.""",

    ("D", "pc", 2024, "sc", 4): r"""Exercice 4 (4,5pts)
Expérience des fentes d'Young ($a=1$ mm, $D=1$ m) avec différents filtres.
1. Définir l'interfrange i et donner son expression.
2. Compléter le tableau des longueurs d'onde $\lambda$ et couleurs pour les interfranges mesurées ($4{,}7$ ; $5{,}2$ ; $6$ ; $6{,}5 \times 10^{-4}$ m).
3. Calculer l'abscisse du milieu de la 2ème frange brillante pour le filtre n°2.
4. Filtre supprimé (lumière blanche) :
4.1 Décrire l'observation sur l'écran.
4.2 Un spectroscope est placé en $x=3$ mm. Préciser le nombre de franges brillantes et leurs longueurs d'onde.""",
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
    shutil.copy2(p, BACKUP_DIR / f"json_bac-pre-fill-d-pc-sc-{stamp}.json")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"\n→ {p} mis à jour ({len(updated)} entrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
