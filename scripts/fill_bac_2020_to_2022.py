"""Remplit 13 énoncés : Bac C PC 2020/2021 SN + Bac D SVT 2022 SC.

Source : transcription manuelle des sujets officiels (qualité ~60 %,
à revoir dans l'admin UI). NE TOUCHE PAS `validated_by_admin`.

Schéma de la clé EXOS :
    (filiere_id, matiere_id, annee, session_code, ex_num) -> ennonce
    avec session_code ∈ {"sn", "sc"}.

Le script trouve l'entrée par (filiere, annee, session, exercice_numero),
en acceptant `matiere_id ∈ {pc, physique, chimie}` quand on cible "pc"
(ids legacy `chimie-YYYY-sn-exN` / `physique-...`). Pour "svt" et "math"
le match est strict.

Comportement :
  - Met à jour `ennonce_complet`, `is_skeleton=False`, `updated_at`.
  - Skip si déjà rempli (>100 chars) sauf --force.
  - Backup automatique dans json_backups/ avant écriture.

Usage :
    .venv/bin/python scripts/fill_bac_2020_to_2022.py --dry-run
    .venv/bin/python scripts/fill_bac_2020_to_2022.py
    .venv/bin/python scripts/fill_bac_2020_to_2022.py --force
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

EXOS: dict[tuple[str, str, int, str, int], str] = {

    # ═══════════════ BAC C · PC · 2020 SESSION NORMALE ═══════════════
    ("C", "pc", 2020, "sn", 1): r"""Exercice 1 (4pts)
Afin d'étudier la cinétique de décomposition de l'iodure d'hydrogène HI en diiode et dihydrogène, on place à la date $t=0$ dans un thermostat maintenu à $380^\circ$C des ampoules scellées identiques, contenant chacune la même quantité de matière en iodure d'hydrogène. À la date t donnée, une ampoule est refroidie rapidement et ouverte. Le diiode formé à cet instant est mis en solution et dosé par un volume V d'une solution de thiosulfate de sodium $Na_2S_2O_3$ de concentration C.
1.1 Pourquoi refroidit-on rapidement l'ampoule ? (0,5pt)
1.2 Écrire les demi-équations électroniques des couples oxydants/réducteurs et l'équation bilan de la réaction correspondant au dosage. On donne $E^0_{I_2/I^-}=0{,}55$ V et $E^\circ_{S_4O_6^{2-}/S_2O_3^{2-}}=0{,}08$ V. (1pt)
1.3 Montrer que la quantité de matière du diiode formée à la date t est donnée par la relation $n(I_2)=\dfrac{CV}{2}$. (0,5pt)
2. Les courbes représentatives de la fonction $C_0=f(t)$ sont données par la figure pour deux températures, où $C_0$ représente la concentration en diiode.
2.1 Définir la vitesse instantanée de formation du diiode. (0,5pt)
2.2 Calculer les vitesses de formation du diiode à $t=0$. (1pt)
2.3 Quel facteur cinétique ces deux expériences mettent-elles en évidence ? (0,5pt)""",

    ("C", "pc", 2020, "sn", 2): r"""Exercice 2 (3pts)
1. L'acide benzoïque est un corps solide blanc de formule $C_6H_5COOH$, présent dans certaines plantes. On le représente par AH. On dissout une masse $m=122$ mg d'acide benzoïque pour obtenir une solution aqueuse $S_A$ de volume $V=100$ mL. On mesure le pH et on trouve $pH=3{,}1$.
1.1 Calculer la concentration molaire volumique $C_A$ de la solution $S_A$. (0,5pt)
1.2 Écrire l'équation de la réaction entre l'acide et l'eau. (0,5pt)
1.3 Montrer que la constante pKa du couple AH/A$^-$ peut s'écrire $pKa=-\log\dfrac{[H_3O^+]^2}{C_A-[H_3O^+]}$. Calculer pKa. (1pt)
2. On mélange un volume $V_A=40$ mL de la solution $S_A$ d'acide benzoïque avec un volume $V_B=5$ mL d'une solution d'hydroxyde de sodium de concentration $C_B$. On mesure le pH du mélange et on trouve $pH=3{,}8$.
2.1 Écrire l'équation de la réaction réalisée. (0,5pt)
2.2 Calculer la quantité de matière n(OH$^-$) qui se trouve dans ce mélange. On donne : C : 12 g/mol ; H : 1 g/mol ; O : 16 g/mol. (0,5pt)""",

    ("C", "pc", 2020, "sn", 3): r"""Exercice 3 (4,5pts)
On néglige les frottements sauf dans la question 2.
1. Un ouvrier exerce sur un solide de masse m, par l'intermédiaire d'une corde inextensible et de masse négligeable faisant l'angle $\beta$ (figure 2), une force constante F pour le faire monter à partir du repos d'une position A à une position B distante de d, selon la ligne de plus grande pente d'un plan incliné d'un angle $\alpha$ par rapport à l'horizontale. L'origine des abscisses x étant le point A.
1.1 Déterminer la nature du mouvement et établir son équation horaire. Faire les applications numériques. On donne : $\cos\beta=0{,}9$ ; $\sin\beta=0{,}42$ ; $F=152{,}5$ N ; $m=25$ kg ; $\alpha=30^\circ$. (1,5pt)
1.2 Sachant que $d=4$ m, calculer le travail de la tension $\vec{T}$ de la corde, lors de son déplacement de la position A à la position B. Préciser son caractère. (1pt)
1.3 Donner les expressions des travaux des autres forces appliquées au solide pendant ce déplacement, en précisant leurs caractères. (0,5pt)
2. On considère maintenant que le plan incliné exerce sur le solide une force de frottement f constante. On constate que l'ouvrier doit exercer une force $F'=162{,}5$ N pour déplacer le solide de A vers B avec la même accélération. Déduire la valeur de cette force de frottement. (0,5pt)
3. Établir en fonction de x les expressions des énergies potentielle de pesanteur $E_P(x)$, cinétique $E_c(x)$ et mécanique $E_m(x)$ du solide entre A et B. L'origine de l'énergie potentielle de pesanteur est le plan horizontal passant par B. (0,5pt)
4. Lorsque le solide passe en B la force $\vec{F}$ exercée par l'ouvrier est supprimée ; il continue alors son mouvement pour atteindre le point C avec une vitesse nulle. En déduire la distance BC. (0,5pt)""",

    ("C", "pc", 2020, "sn", 4): r"""Exercice 4 (4,5pts)
Le poids de l'électron sera négligeable devant les autres forces appliquées.
1. Un faisceau d'électrons est émis sans vitesse par une cathode C et accéléré par une anode A à l'aide d'une différence de potentiel $U_0=V_A-V_C$.
1.1 Déterminer le signe de $U_0$ appliquée entre C et A et calculer sa valeur si $AC=d_0=3$ cm et $E=6.10^3$ V/m. (0,75pt)
1.2 Calculer la vitesse $V_0$ de l'électron lorsqu'il arrive en $O'$. On donne $e=1{,}6.10^{-19}$ C, $m=9.10^{-31}$ kg. (0,75pt)
2. En O, les électrons pénètrent avec la vitesse $\vec{V}_0$ dans une zone où règne un champ électrique dû à une tension U existant entre deux plaques $P_1$ et $P_2$ de longueur l et distantes de d.
2.1 Établir l'expression de l'équation de la trajectoire de l'électron entre les plaques. Donner cette expression en fonction de $U_0$, U et d. Préciser sa nature. (0,75pt)
2.2 Déterminer la valeur de la tension U si la déviation angulaire électrique est telle que $\tan\alpha=0{,}3$. On donne $l=d=4$ cm. (0,5pt)
3. On remplace le champ électrique $\vec{E}$ par un champ magnétique $\vec{B}$ créé dans une zone carrée MNPQ de côté $a=4$ cm. Les électrons pénètrent dans cette zone au point O avec la vitesse $V_0$.
3.1 Déterminer la nature du mouvement de l'électron dans le champ magnétique $\vec{B}$. Donner l'expression du rayon de la trajectoire en fonction de m, e, B et $U_0$. (0,75pt)
3.2 Déterminer la valeur de la déviation angulaire magnétique $\alpha'$ si les électrons sortent entre P et N. On donne $B=2{,}25.10^{-4}$ T. (0,5pt)
3.3 Quelle est la valeur de B pour que l'électron effectue un quart de cercle ? (0,5pt)""",

    ("C", "pc", 2020, "sn", 5): r"""Exercice 5 (4pts)
On place une tige en cuivre PP' de longueur $l=10$ cm et de masse $m_t=15$ g sur deux rails AB et A'B' conducteurs parallèles séparés par une distance $d=5$ cm. On relie les extrémités B et B' des rails à un générateur. On place le circuit dans un champ magnétique uniforme dont le vecteur $\vec{B}$ reste vertical.
1. Déterminer le sens de $\vec{B}$ pour que la tige soit en équilibre. Exprimer alors l'intensité B du champ magnétique en fonction de l'intensité I du courant, de la masse m, de la distance d et de g. (1pt)
2. On fait varier l'intensité du courant et on accroche chaque fois à l'extrémité du fil une masse marquée pour conserver l'équilibre. L'étude expérimentale a permis d'établir un tableau de valeurs.
2.1 Représenter graphiquement $m=f(I)$ les variations de la masse en fonction de l'intensité I. (0,75pt)
2.2 Trouver l'équation de la courbe. (0,75pt)
2.3 En déduire l'intensité B du champ magnétique. (0,75pt)
3. On décroche le fil de la tige et on donne à l'intensité du courant la valeur $I=15$ A. Pour conserver l'équilibre, on incline les rails d'un angle $\alpha$ par rapport à l'horizontale. Calculer $\alpha$. (0,75pt)""",

    # ═══════════════ BAC C · PC · 2021 SESSION NORMALE ═══════════════
    ("C", "pc", 2021, "sn", 1): r"""Exercice 1 (4pts)
1.1 Citer deux facteurs cinétiques et préciser leur influence sur l'évolution d'une réaction chimique. (0,5pt)
1.2 Généralement la vitesse d'une réaction chimique diminue au cours du temps. Dire pourquoi. (0,25pt)
2. On étudie expérimentalement la cinétique de la réaction d'oxydation de l'ion iodure $I^-$ par l'ion peroxodisulfate $S_2O_8^{2-}$. On donne $E_{S_2O_8^{2-}/SO_4^{2-}}=2{,}1$ V et $E_{I_2/I^-}=0{,}6$ V.
2.1 Écrire les demi-équations et l'équation bilan de cette réaction. (1pt)
2.2 Le dosage du diiode formé lors de deux expériences a permis de tracer les courbes de la figure. En utilisant la courbe (b), calculer la vitesse instantanée de disparition de l'ion peroxodisulfate à $t=75$ s. Déduire la vitesse de formation de l'ion $SO_4^{2-}$ à cet instant. (0,5pt)
2.3 Identifier la courbe correspondante à chaque expérience. (0,5pt)
2.4 Les mesures nécessaires à l'établissement de ces courbes ont été effectuées après avoir plongé l'échantillon à doser dans de l'eau glacée. Expliquer. (0,25pt)
2.5 Déterminer la composition du mélange à $t=25$ s pour la courbe (a). (1pt)""",

    ("C", "pc", 2021, "sn", 2): r"""Exercice 2 (3pts)
Les résultats du dosage de 3 solutions basiques A, B et C par une solution d'acide chlorhydrique de concentration molaire $C_A=10^{-2}$ mol/L sont consignés dans un tableau. A, B et C sont respectivement des solutions de soude, d'ammoniac et de méthylamine de même concentration $C_B=10^{-2}$ mol/L. Le volume dosé pour chacune est de 10 cm³.
1. La comparaison des valeurs initiales des pH des solutions basiques permet-elle de comparer la force relative des bases étudiées ? Justifier la réponse. (0,75pt)
2.1 Définir l'équivalence acido-basique. Préciser le volume d'acide chlorhydrique versé dans chacune des 3 solutions basiques à l'équivalence. (0,75pt)
2.2 La comparaison des valeurs des pH aux points d'équivalence dans les 3 dosages confirme-t-elle la réponse à la 1ʳᵉ question ? Justifier. (0,5pt)
2.3 Comparer les valeurs des pH des 3 mélanges après l'équivalence et à volume égal versé. Expliquer ce résultat. (0,5pt)
2.4 Déterminer à partir du tableau les valeurs des pKa des couples acide/base $NH_4^+/NH_3$ et $CH_3NH_3^+/CH_3NH_2$. (0,5pt)""",

    ("C", "pc", 2021, "sn", 3): r"""Exercice 3 (4pts)
On donne $g=10$ m/s². On suspend à l'extrémité inférieure d'un ressort un solide S de masse $m=100$ g. À l'équilibre, le ressort est allongé de 10 cm.
1. Calculer la raideur K du ressort. (0,5pt)
2. Le pendule est placé sur un plan horizontal. À la date $t=0$, le solide S étant en position d'équilibre, on lui communique une vitesse $V_0=0{,}4$ m/s.
2.1 Établir l'équation différentielle du mouvement du centre d'inertie G du solide S. (0,5pt)
2.2 Déterminer l'équation horaire du mouvement de G. (1pt)
3. Exprimer, à la date t, l'énergie mécanique totale E du système en fonction de K, m, x et V puis en fonction de K et de l'élongation maximale $x_m$. (1pt)
4. La figure 3 représente les courbes $C_1$ et $C_2$ des variations des énergies cinétique $E_c$ et potentielle $E_P$ en fonction du temps.
4.1 Identifier la courbe représentative de chaque énergie. (0,5pt)
4.2 Retrouver les valeurs de la constante de raideur K et de la masse m. (0,5pt)""",

    ("C", "pc", 2021, "sn", 4): r"""Exercice 4 (4,5pts)
1. On considère une bobine (B) de rayon $r=20$ cm, longueur $l=53$ cm et $N=200$ spires. Établir la formule donnant l'inductance L de cette bobine en fonction de $\mu_0$, r, l et N puis calculer sa valeur. (1pt)
2. On réalise un circuit comportant en série la bobine (B), un conducteur ohmique $R=110\,\Omega$, un générateur idéal $E=6$ V et un interrupteur K.
2.1 Donner les expressions des tensions $u_R(t)$ et $u_B(t)$ en fonction de R, r, L et $i(t)$. (0,5pt)
2.2 Montrer que l'équation différentielle régissant l'évolution de l'intensité $i(t)$ s'écrit $\dfrac{di(t)}{dt}+\dfrac{\alpha}{L}i(t)=\dfrac{E}{L}$ et exprimer $\alpha$ en fonction de R et r. (0,5pt)
2.3 Sachant que l'équation admet une solution de la forme $i(t)=I_o(1-e^{-t/\tau})$, montrer que $I_o=\dfrac{E}{R+r}$ et $\tau=\dfrac{L}{R+r}$. (1pt)
3. Exploitation de la courbe :
3.1 Préciser, en le justifiant, si l'établissement du courant électrique est instantané. (0,5pt)
3.2 Déterminer graphiquement les valeurs de $I_o$ et de $\tau$. En déduire les valeurs de r et L. (1pt)""",

    ("C", "pc", 2021, "sn", 5): r"""Exercice 5 (4,5pts)
On monte en série un résistor $R_1=10\,\Omega$, une bobine d'inductance $L=0{,}6$ H et de résistance R, et un condensateur de capacité C. On applique une tension alternative sinusoïdale $u(t)=U_m\sin(2\pi N t)$.
1. À partir des courbes de l'oscilloscope :
1.1 Déduire la fréquence $N_1$ de la tension d'alimentation. (0,75pt)
1.2 Déduire les valeurs maximales $U_m$ et $U_{BMm}$ des tensions d'alimentation et aux bornes du résistor. (0,75pt)
1.3 Déduire le déphasage $\phi$ de la tension instantanée $u_{BM}(t)$ par rapport à la tension d'alimentation. (0,5pt)
2. Déterminer l'intensité instantanée $i(t)$ du courant (valeur maximale, fréquence et phase). (0,75pt)
3. Déterminer les valeurs de la résistance R et de la capacité C. (0,5pt)
4. On ajuste la fréquence à une nouvelle valeur $N_2$.
4.1 Montrer que dans ces conditions le circuit est en résonance d'intensité. Calculer alors l'intensité efficace $I_o$ du courant. (0,5pt)
4.2 Déterminer la fréquence $N_2$ de la tension excitatrice. (0,5pt)
4.3 Calculer le coefficient de surtension du circuit. (0,25pt)""",

    # ═══════════════ BAC D · SVT · 2022 SESSION COMPLÉMENTAIRE ═══════════════
    ("D", "svt", 2022, "sc", 1): r"""Exercice 1 (5pts)
L'arbre généalogique est celui d'une famille dont certains individus sont atteints d'une maladie héréditaire.
1. En exploitant ce pédigrée, discutez les deux hypothèses suivantes :
a. l'allèle de la maladie est récessif (0,5pt) ;
b. l'allèle de la maladie est dominant (0,5pt).
Quelle précision apporte cette information ? (0,5pt)
2. Le résultat de l'électrophorèse de l'ADN de la femme $I_1$ montre un seul type d'ADN.
3. Discutez si le gène en question est porté par un autosome ou par un chromosome sexuel X. (1pt)
4. Une biopsie des villosités placentaires a été exigée chez la femme $II_1$ enceinte et ayant un enfant malade.
a. Quelle(s) précision(s) apportent ces documents (caryotype et analyse ADN) ? (0,5pt)
b. Écrivez les génotypes des individus $I_1$, $I_2$, $II_3$ et $II_4$. (1pt)
5. Schématisez la phase de la méiose que vous jugez anormale et qui a conduit à l'anomalie observable chez le fœtus. (1pt)""",

    ("D", "svt", 2022, "sc", 2): r"""Exercice 2 (6 points)
A. Depuis la puberté jusqu'à la ménopause, les organes de l'appareil génital de la femme sont le siège de modifications cycliques et synchronisées.
1. Schématiser l'évolution des structures ovariennes que vous nommez au cours d'un cycle de 28 jours. (1pt)
2. Représenter graphiquement l'évolution parallèle du taux des hormones sécrétées par ces structures. (1pt)
3. Préciser l'effet des hormones ovariennes sur l'utérus (myomètre et endomètre) au cours du même cycle. (1pt)
B. Le document ci-contre est un schéma de l'une des structures observées dans une coupe d'ovaire vers le 21ème jour du cycle sexuel.
1. Nommez cette structure et annotez-la. (1pt)
2. Expliquez le déterminisme hormonal de la formation de cette structure. (1pt)
3. Expliquez le devenir de cette structure. (1pt)""",

    ("D", "svt", 2022, "sc", 3): r"""Exercice 3 (9 points)
A. On pratique sur une fibre nerveuse une stimulation S efficace et à l'aide d'un oscilloscope on enregistre les phénomènes électriques obtenus avant et après la stimulation.
1.a. Légendez le document 1 (dispositif oscilloscope). (1pt)
1.b. Identifiez le phénomène enregistré suite à la stimulation S. (0,5pt)
1.c. Nommez les phases de l'enregistrement désignées par les lettres A, B, C et D. (1pt)
2. Expliquez le mécanisme ionique à l'origine de chaque phase. (1,5pt)
3. Expliquez, schéma à l'appui, le mécanisme de la propagation de ce phénomène. (1pt)
4. Calculez la vitesse de propagation de l'influx nerveux le long de cette fibre (distance = 12 mm). (1pt)
B. Le document 3 présente le schéma d'un dispositif expérimental au niveau d'un récepteur : le fuseau neuromusculaire.
1. Nommez les sites 1 et 2. (0,5pt)
2. Nommez les phénomènes électriques enregistrés au niveau des oscilloscopes $O_1$ et $O_2$ suite à un étirement du muscle M. (1pt)
3. Précisez le rôle du fuseau neuromusculaire. (0,5pt)
4. Représentez l'arc réflexe en ne considérant que la réponse du muscle M.""",
}


_SESSION_MATCH = {"sn": "normal", "sc": "compl"}


def find_entry(data: list[dict], filiere: str, matiere: str,
               annee: int, sess_code: str, ex_num: int) -> dict | None:
    """Trouve (filiere, matiere, annee, session, ex_num) — gère ids legacy."""
    sess_substr = _SESSION_MATCH[sess_code]
    # Si matiere == "pc", accepte aussi les ids legacy chimie/physique.
    if matiere == "pc":
        mat_accept = {"pc", "physique", "chimie"}
    else:
        mat_accept = {matiere}
    candidates: list[dict] = []
    for e in data:
        if e.get("filiere_id") != filiere:
            continue
        if e.get("matiere_id") not in mat_accept:
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
    # Plusieurs : préfère l'entrée déjà non-squelette.
    for c in candidates:
        if not c.get("is_skeleton") and (c.get("ennonce_complet") or "").strip():
            return c
    return candidates[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="Écrase même si ennonce_complet est déjà rempli (>100 chars).")
    ap.add_argument("--json", default=str(JSON_PATH))
    args = ap.parse_args()

    p = Path(args.json)
    data: list[dict] = json.loads(p.read_text(encoding="utf-8"))

    now = datetime.now().isoformat(timespec="seconds")
    updated: list[tuple[str, str, int, int]] = []
    skipped_missing: list[str] = []
    skipped_filled: list[tuple[str, str, int]] = []

    for (fil, mat, annee, sess_code, ex_num), ennonce in EXOS.items():
        label = f"{fil}/{mat}/{annee}/{sess_code}/ex{ex_num}"
        e = find_entry(data, fil, mat, annee, sess_code, ex_num)
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
        # /!\ Ne touche pas validated_by_admin.
        updated.append((label, eid, old_len, len(new_text)))

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
        print("\nDéjà remplis (>100 chars) — skippés sans --force :")
        for label, eid, ln in skipped_filled:
            print(f"  {label:25}  → {eid:45}  ({ln} chars existants)")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not updated:
        print("\nRien à écrire.")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = BACKUP_DIR / f"json_bac-pre-fill-2020-2022-{stamp}.json"
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
