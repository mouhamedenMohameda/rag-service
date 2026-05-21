"""Remplit 70 énoncés Bac C · Math · 2001-2010 (toutes sessions, Gemini).

Convention de mapping :
  Années 2001-2007 (sauf 2001 SC) : 3 items → ex1=Exo1, ex2=Exo2, ex3=Problème
  2001 SC (4 items) : ex1=Exo1(SérieC), ex2=Exo1(TMGM), ex3=Exo2, ex4=Problème
  2008 (5 exos) : ex1-ex5
  2009 et 2010 (4 exos) : ex1-ex4

Source : extraction Gemini, qualité ~60%. Ne touche PAS validated_by_admin.
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

    # ═══════════════ 2001 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2001, "sc", 1): r"""Exercice 1 (Série C uniquement)
Pour tout nombre complexe z on pose : $P(z)=z^4-(2+6i)z^3+(-12+9i)z^2+(13+9i)z+2-6i$.
1.a) Calculer $P(i)$ et $P(2i)$.
1.b) Déterminer les nombres complexes a et b tels que pour tout nombre complexe z on a : $P(z)=(z^2-3iz-2)(z^2+az+b)$.
1.c) Déterminer les nombres complexes $z_1, z_2, z_3, z_4$ solutions de l'équation $P(z)=0$ tels que $|z_1|<|z_2|<|z_3|<|z_4|$.
2. On écrit chacun des nombres $z_1, z_2, z_3, z_4$ sur l'une des quatre faces d'un dé tétraédrique truqué. On lance ce dé et on admet que la probabilité pour que l'une de ces faces soit cachée est proportionnelle au carré du module du nombre complexe $z_k$ inscrit sur cette face, c'est-à-dire $p_k=t|z_k|^2$ pour $k\in\{1,2,3,4\}$ où $t\in\mathbb{R}^*$.
2.a) Démontrer que $p_1=\dfrac{1}{12}$.
2.b) Calculer $p_2, p_3$ et $p_4$.
2.c) Soit X la variable aléatoire réelle qui à chaque jet du tétraèdre associe la somme des parties imaginaires des nombres inscrits sur les faces latérales du dé. Vérifier que X prend exactement deux valeurs puis déterminer sa loi de probabilité.""",

    ("C", "math", 2001, "sc", 2): r"""Exercice 1 (Série TMGM uniquement)
1. Résoudre l'équation différentielle (E) : $y''-4y'+5y=0$.
2. On considère l'équation différentielle (E') : $y''-4y'+5y=(-x+1)e^x$.
2.a) Déterminer les réels a et b tels que la fonction g définie par $g(x)=(ax+b)e^x$ soit une solution de (E').
2.b) h désignant une solution quelconque de l'équation différentielle (E), montrer que la fonction f telle que $f(x)=g(x)+h(x)$ est une solution de l'équation (E').
3. Déterminer, parmi les fonctions f définies au 2.b), celle dont la courbe représentative dans un repère orthonormé passe par le point $A(0;1)$ et admet en ce point une tangente parallèle à la droite d'équation $y+x=0$.""",

    ("C", "math", 2001, "sc", 3): r"""Exercice 2 (Commun aux séries C et TMGM)
Soit la fonction $f_n$ définie par $f_n(x)=x^n e^{1-x}$ pour tout $x\in\mathbb{R}$, où n est un entier naturel non nul.
1. Dresser le tableau de variations de la fonction $f_1$ (cas $n=1$).
2. Pour tout entier naturel non nul n on pose $U_n=\displaystyle\int_0^1 f_n(x)\,dx$.
2.a) En utilisant une intégration par parties, prouver que $U_1=e-2$.
2.b) Démontrer que $\forall n\in\mathbb{N}^* : \dfrac{1}{n+1}\le U_n\le\dfrac{e}{n+1}$.
2.c) Démontrer, en utilisant une intégration par parties, la relation de récurrence $U_{n+1}=(n+1)U_n-1$.
3. Pour tout entier naturel non nul n on pose $V_n=n!\,e-U_n$.
3.a) Démontrer que $V_{n+1}=(n+1)V_n+1$.
3.b) Démontrer par récurrence que $V_n\in\mathbb{N}$.
3.c) Montrer que pour tout entier $n\ge 2$, le nombre $n!\,e=V_n+U_n$ n'est pas un entier naturel.
4. Soient p et q deux entiers naturels strictement positifs.
4.a) Prouver que pour tout entier naturel $n\ge q$, le nombre $\dfrac{n!\,p}{q}$ est un entier naturel.
4.b) Prouver, en utilisant une démonstration par l'absurde, que le nombre e n'est pas rationnel.""",

    ("C", "math", 2001, "sc", 4): r"""Problème (Commun) — Configurations géométriques avec carrés extérieurs
Partie A — Dans le plan orienté, on considère le triangle direct $ABB'$ dont tous les angles sont aigus et on pose $(\vec{AB};\vec{AB'})=\theta\ [2\pi]$. On construit à l'extérieur de ce triangle deux carrés ABCD et $AB'C'D'$ de centres respectifs O et $O'$, et soient P, Q les milieux de $[BB']$ et $[DD']$.
1.a) Faire une figure.
1.b) Prouver que $B'D=BD'$ et $(B'D)\perp(BD')$ ; en déduire la nature du quadrilatère $OPO'Q$.
2. Soit I le point de concours des segments $[B'D]$ et $[BD']$.
2.a) Prouver que A et I sont symétriques par rapport à la droite $(OO')$.
2.b) En déduire $AQ=IP=\tfrac{BB'}{2}$ et $AP=IQ=\tfrac{DD'}{2}$.
3. Les droites (AQ) et (BB') se coupent en H, (AP) et (DD') en K.
3.a) Calculer $\vec{AQ}\cdot\vec{BB'}$ et $\vec{AP}\cdot\vec{DD'}$ ; en déduire que (AQ) et (AP) sont des hauteurs dans $ABB'$ et $ADD'$.
3.b) Prouver que les six points O, O', P, Q, H, K sont cocycliques.

Partie B — On suppose $\theta\in]0;\tfrac{\pi}{2}[\setminus\{\tfrac{\pi}{4}\}$. Soient $\Gamma, \Gamma'$ les cercles circonscrits aux carrés. s la similitude directe de centre I qui transforme O en O'.
1.a) Faire une nouvelle figure ($\theta=50^\circ$, $AB'=7$ cm, $AB=5$ cm) puis déterminer l'intersection des cercles.
1.b) Construire $A_1=s(A)$ et justifier.
2. Soit $M\in\Gamma\setminus\{A,I\}$ et $s(M)=M_1$.
2.a) Comparer $(\vec{OI};\vec{OM})$ et $(\vec{O'I};\vec{O'M_1})$ ; démontrer que A, M, $M_1$ sont alignés.
2.b) Construction simple de $M_1$.
3. Soient $A_1, B_1, C_1, D_1$ les images de A, B, C, D par s. On pose $E=[AB')\cap[A_1B_1]$, $F=[B'C')\cap[A_1D_1]$, $G=[C'D')\cap[D_1C_1]$, $J=[D'A)\cap[C_1B_1]$.
3.a) Construire $B_1, C_1, D_1$ et déduire une 2e méthode pour $A_1$.
3.b) Montrer que $A_1B_1C_1D_1$ est un carré de centre $O'$.
4. Soit r la rotation de centre $O'$ et d'angle $\tfrac{\pi}{2}$. Démontrer $r(E)=F$, $r(F)=G$ ; en déduire que EFGJ est un carré de centre $O'$.

Partie C — Soit $\alpha$ l'angle de s et $\beta=(\vec{B_1A_1};\vec{AB'})\ [2\pi]$.
1.a) Prouver $\alpha=-\theta-\tfrac{\pi}{2}\ [2\pi]$ et $\alpha=\theta-\beta+\pi\ [2\pi]$.
1.b) En déduire $\beta=2\theta-\tfrac{\pi}{2}\ [2\pi]$.
2.a) Démontrer $(\vec{O'B_1};\vec{O'A})=\beta\ [2\pi]$.
2.b) Pour quelles valeurs de $\beta$, l'octogone formé par les sommets des deux carrés est régulier ?
2.c) Valeurs correspondantes de $\theta$.
3. Calculer, dans la situation précédente, l'aire du carré EFGJ en fonction de $AB'=a$.""",

    # ═══════════════ 2001 SESSION NORMALE ═══════════════
    ("C", "math", 2001, "sn", 1): r"""Exercice 1
Le plan complexe est muni d'un repère orthonormé $(O;\vec{u},\vec{v})$. Pour tout réel $\theta\in]0;\tfrac{\pi}{2}[$ on définit l'application $f_\theta$ qui à tout point M d'affixe z associe $M'$ d'affixe $z'=(1-i\cos\theta)z-\cos\theta$.
1. Montrer que $f_\theta$ est une similitude directe dont on précisera le rapport en fonction de $\theta$ et le centre $\Omega$.
2. Soit $\Omega$ d'affixe i et $\alpha$ la mesure de l'angle de $f_\theta$, $-\pi<\alpha\le\pi$.
2.a) Démontrer que si M est distinct de $\Omega$, le triangle $\Omega MM'$ est rectangle et de sens indirect.
2.b) Prouver $\tfrac{\Omega M}{\Omega M'}>\tfrac{1}{\sqrt{2}}$ ; en déduire $-\tfrac{\pi}{4}<\alpha<0$.
3. Soit A un point du plan distinct de $\Omega$. Déterminer quand $\theta$ décrit $]0;\tfrac{\pi}{2}[$ :
3.a) $\Gamma_1=\{M : f_\theta(A)=M\}$.
3.b) $\Gamma_2=\{M : f_\theta(M)=A\}$.
4. Construire $\Gamma_1$ et $\Gamma_2$ pour $A(1;1)$.""",

    ("C", "math", 2001, "sn", 2): r"""Exercice 2
Dans le plan orienté, on considère un losange ABCD direct de centre O tel que $(\vec{AB};\vec{AD})=\tfrac{\pi}{3}\ [2\pi]$. Soient I, J, K, L les milieux respectifs de $[AB], [BC], [CD], [DA]$, et $P\in[OA]$ tel que le triangle PBD soit rectangle en P.
Transformations : $r_1$ rotation de centre D et d'angle $-\tfrac{\pi}{3}$ ; $r_2$ rotation de centre B et d'angle $\tfrac{2\pi}{3}$ ; $s_1$ réflexion d'axe (BD) ; $s_2$ réflexion d'axe (BC) ; $g=r_1\circ s_1$.
1.a) Figure ((AC) horizontale, $AB>5$ cm).
1.b) Déterminer les images de B et C par $r_1, r_2, s_1$.
2.a) Déterminer $g(B)$ et $g(C)$.
2.b) Nature de g et forme réduite.
3. Soit (E) l'ellipse de foyers B, C passant par O et $2a$ son grand axe.
3.a) Montrer $K\in(E)$ et $CP=2a$.
3.b) Construction des sommets de (E).
4. On pose $r_1(E)=E_1$, $r_2(E)=E_2$, $s_1(E)=E_3$, $g(E)=E_4$.
4.a) Déterminer $E_1, E_2, E_3, E_4$ ; remarque ?
4.b) Construire $E_1$ et les points $K_1, K_2, K_3, K_4$ images de K. Interprétation.""",

    ("C", "math", 2001, "sn", 3): r"""Problème
Partie A — Fonction auxiliaire. Soit $g_m$ le trinôme $g_m(x)=x^2+2x-2m$ ($m\in\mathbb{R}^*$).
1. Discuter suivant m le nombre de solutions de $g_m(x)=0$.
2. Si $g_m(x)=0$ a deux solutions $x'<x''$, montrer que si $m<0$ alors $-2<x'<x''<0$, et si $m>0$ alors $x'<-2<0<x''$.

Partie B — Famille de fonctions. On suppose $m>0$. Soit $f_m(x)=x+m\ln\left|\tfrac{x+2}{x}\right|$ et $(C_m)$ sa courbe.
1.a) Ensemble de définition et limites aux bornes.
1.b) Variations de $f_m$.
2.a) Toutes les courbes $(C_m)$ passent par un point fixe I (centre de symétrie).
2.b) Asymptotes et position relative par rapport à l'asymptote oblique $(\Delta)$.
2.c) Tracer $(C_1)$.

Partie C — Construction de $(C_m)$ à partir de $(C_1)$. Soit $\varphi_m : M(z)\to M'(z')$ avec $z'=\tfrac{1}{2}[(1+m)+(1-m)i]z+\tfrac{1}{2}[(1-m)+(1-m)i]\bar{z}$ ($m\ne 1$).
1.a) Écrire $x',y'$ en fonction de x, y et m.
1.b) Démontrer que l'ensemble des points invariants est la droite $(\Delta) : y=x$.
1.c) Si $M\notin(\Delta)$, $(MM')$ est parallèle à une droite fixe $(\Delta')$.
1.d) Soit $M_0$ le projeté de M sur $(\Delta)$ parallèlement à $(\Delta')$ ; exprimer $\vec{M_0M'}$ en fonction de $\vec{M_0M}$.
2.a) Démontrer $\varphi_m(C_1)=(C_m)$ ; en déduire une construction.
2.b) Construire $(C_m)$.

Partie D — Convergence d'une suite. Soit $0<\lambda<1$ et $A(\lambda)$ l'aire délimitée par $(C_m), (C_{m-1})$ et $x=\lambda, x=1$.
1. Calculer $A(\lambda)$ par intégration par parties, puis $\lim_{\lambda\to 0}A(\lambda)$.
2. Soit $h(x)=\ln(1+\tfrac{2}{x})$ et $S_n=\tfrac{1}{n}\sum_{p=1}^n h(\tfrac{p}{n})$.
2.a) Sens de variation de h sur $]0;1]$ et encadrement de l'intégrale.
2.b) En déduire l'encadrement de $A(\tfrac{1}{n})$.
2.c) Déduire $\lim_{n\to\infty}S_n=\ln(\tfrac{27}{4})$.""",

    # ═══════════════ 2002 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2002, "sc", 1): r"""Exercice 1
1. Résoudre dans $\mathbb{C}$ : $z^2-(8\cos\theta)z+16-7\sin^2\theta=0$ ($\theta\in[0,2\pi]$).
2. Soient $M_1(z_1)$ et $M_2(z_2)$. Soit $\Gamma$ l'ensemble des points $M_1, M_2$ quand $\theta$ décrit $[0,2\pi]$.
2.a) Équation cartésienne de $\Gamma$.
2.b) Nature et éléments caractéristiques de $\Gamma$, puis construction.
3. Soit $A(0;1)$ et G barycentre de $\{(A,-3),(M,1)\}$ avec $M\in\Gamma$.
3.a) Démontrer que G décrit une ellipse $\Gamma'$ (centre et sommets).
3.b) Équation cartésienne de $\Gamma'$ et construction.
3.c) Pour $\theta=\tfrac{\pi}{3}$, construire $M_1, M_2, G_1, G_2$.""",

    ("C", "math", 2002, "sc", 2): r"""Exercice 2
ABC est un triangle équilatéral direct. I milieu de [BC], O milieu de [AC], $B'$ symétrique de B par rapport à O.
1. Soit t la translation de vecteur $\vec{OB}$ et r la rotation de centre A et d'angle $\tfrac{\pi}{3}$. On pose $f=t\circ r$.
1.a) Figure et placer $A'=f(A)$ et $C'=f(B)$.
1.b) Nature du triangle ICO et préciser $f(C)$.
1.c) Caractériser f, en déduire la nature de $IAA'$.
2. Soit s la similitude directe telle que $s(O)=A$ et $s(C)=I$. Montrer $s(I)=A'$ puis déterminer angle et rapport de s.
3. Soit $\Omega$ le centre de s.
3.a) Démontrer que $\Omega, I, C, A$ sont cocycliques, ainsi que $\Omega, A, O, B'$.
3.b) Position de $\Omega$ et sa construction.
4.a) Montrer que $\Omega OIC$ est un losange.
4.b) Programme de construction des images de $\Omega OIC$ par $s^2$ et $s^3$ puis construire.
4.c) Particularité de $s^6$ ?""",

    ("C", "math", 2002, "sc", 3): r"""Problème
I — Étude d'une fonction auxiliaire. $f(x)=\dfrac{x}{1+x+x^2}$.
1. Tableau de variation de f et courbe C.
2. Discuter graphiquement suivant m le nombre et le signe des solutions de $mx^2+(m-1)x+m=0$.

II — Étude des tangentes à une courbe. $g(0)=0$ et $g(x)=(x+1)e^{-1/x}$ pour $x>0$.
1.a) Tangente pour $x>0$ et tangente à l'origine.
1.b) Tableau de variation de g.
2. Soit $T_a$ la tangente en a.
2.a) Démontrer que $T_a$ et $T_{1/a}$ ($a\ne 1$) coupent (Ox) au point d'abscisse $f(a)=\tfrac{a}{1+a+a^2}$.
2.b) Toutes les tangentes coupent $[OB]$ où $B(1/3;0)$.
2.c) De chaque point $A(m;0)$ de $[OB]\setminus\{O\}$ passent deux tangentes distinctes à $\Gamma$.
2.d) Point d'inflexion, équation de sa tangente T et intersection de T avec (Ox).
3. $h(t)=1-(1+t)e^{-t}$ pour $t\ge 0$.
3.a) Démontrer $0\le h'(t)\le t$ et $0\le h(t)\le\tfrac{t^2}{2}$.
3.b) Démontrer $0\le x-g(x)\le\tfrac{1}{2x}$ pour $x>0$ et interprétation graphique.
4. Construire tangentes et courbe $\Gamma$.

III — Étude d'une suite. $f_n(x)=\dfrac{x^n}{1+x+x^2}$ et $U_n=\int_0^1 f_n(x)\,dx$.
1. $(U_n)$ est décroissante et $0\le U_n\le\tfrac{1}{n+1}$.
2.a) Par intégration par parties : $U_n=\tfrac{1}{3(n+1)}+\tfrac{1}{n+1}\int_0^1 x^{n+1}\varphi(x)\,dx$ avec $\varphi(x)=\tfrac{1+2x}{(1+x+x^2)^2}$.
2.b) $\tfrac{1}{3}\le\varphi(x)\le 1$ sur [0,1].
3. Démontrer $\tfrac{n+3}{3(n+1)(n+2)}\le U_n\le\tfrac{n+5}{3(n+1)(n+2)}$. En déduire $\lim U_n$ et $\lim nU_n$.""",

    # ═══════════════ 2002 SESSION NORMALE ═══════════════
    ("C", "math", 2002, "sn", 1): r"""Exercice 1
ABCDEFGH est un cube de centre O et d'arête a.
1. Montrer que BED et CHF sont équilatéraux.
2. I et J centres de gravité respectifs de BED et CHF.
2.a) Prouver $\vec{AI}=\tfrac{1}{3}\vec{AG}$ et $\vec{GJ}=\tfrac{1}{3}\vec{GA}$.
2.b) En déduire $\vec{AI}=\vec{IJ}=\vec{JG}$ et O milieu de [IJ].
3. $s_1$ réflexion de plan (BAG), $s_2$ réflexion de plan (DAG), $f=s_1\circ s_2$.
3.a) f est une rotation, déterminer $f(G)$ et $f(A)$.
3.b) $(AG)\perp(BED)$ et $(AG)\perp(CHF)$.
3.c) f laisse globalement invariants BED et CHF.
3.d) Angle de f par rapport à un axe orienté.""",

    ("C", "math", 2002, "sn", 2): r"""Exercice 2
ABC triangle direct rectangle isocèle en A. $\mathcal{C}$ et $\Gamma$ cercles de centres respectifs B et C passant par A. G deuxième intersection de $\mathcal{C}$ et $\Gamma$. D point de $\mathcal{C}$ diamétralement opposé à A.
1.b) Existence et éléments de la rotation r : $A\to D$ et $C\to B$.
2. $M\in\Gamma\setminus\{G\}$, $r(M)=M'$. (GM) coupe $\mathcal{C}$ en $N'$ et $(GM')$ coupe $\mathcal{C}$ en N.
2.a) Construire R et S tels que $M'GMR$ et $N'GNS$ soient des carrés. Éléments de la similitude s : $M\to R$ et $N\to S$.
2.b) (RS) passe par un point fixe.
3. Similitude $s'$ : $D\to B$ et $B\to C$, centre I.
3.a) Angle et rapport de $s'$.
3.b) $(\vec{ID},\vec{IB})=(\vec{GD},\vec{GB})\ [\pi]$ et $(\vec{ID},\vec{IC})=(\vec{AD},\vec{AC})\ [\pi]$.
3.c) Position de I et nature de ACID.
4. $f=s\circ s'$ est une homothétie (rapport et centre).""",

    ("C", "math", 2002, "sn", 3): r"""Problème
Partie A — $f(0)=0$ et $f(x)=\dfrac{1}{\ln x}$ sur $]0,1[\cup]1,+\infty[$.
1. Continuité et dérivabilité en $x_0=0$.
2. Tableau de variation.
3. Point d'inflexion.
4. Construire $C_0$.

Partie B — $f_n(x)=\dfrac{e^n}{-n+\ln x}$ sur $\mathbb{R}\setminus\{e^n\}$.
1. $C_n$ est l'image de $C_0$ par une homothétie $h_n$ de centre O.
2. Tableau de variation de $f_n$.
3. $C_{n-1}$ image de $C_n$ par $h_1$.
4.a) $C_n$ et $C_{n+1}$ se coupent en $M_n$ d'abscisse $x_n=e^{n+1/2}$.
4.b) $M_n$ appartiennent à une droite fixe passant par O.
4.c) Allure de $C_n$ et $C_{n+1}$ et position relative.
5. Construction de $\Gamma$ représentative de $g(x)=\dfrac{e}{-1+\ln x}$.

Partie C — $F(1)=0$ et $F(x)=\int_x^{x^2+1} f(t)\,dt$ pour $x>1$.
1. Montrer $e^{x-1}\ge x$ pour $x>1$ et existence de $F(x)$.
2.a) $\dfrac{e^{x-1}-x}{x-1}\le F(x)\le\dfrac{e^{x-1}-x}{\ln x}$.
2.b) Continuité de F en $x_1=1$.
3. G restriction de F sur $[2,+\infty[$.
3.a) $G'(x)$ et $G''(x)$, montrer $G'(x)>0$ pour $x\ge 2$.
3.b) $\lim_{x\to+\infty}G(x)$ et $\lim_{x\to+\infty}\tfrac{G(x)}{x}$.
3.c) Tableau de variation de G et courbe.""",

    # ═══════════════ 2003 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2003, "sc", 1): r"""Exercice 1 (5 points)
Dans $\mathbb{C}$, on considère l'équation (E) : $z^2-(4\cos t)z+4+5\sin^2 t=0$ où $t\in[0;\pi]$.
1. Résoudre (E). On notera $z_1, z_2$ les solutions avec $\text{Im}(z_1)>0$.
2. Soient $M_1, M_2$ les points d'affixes $z_1, z_2$.
2.a) Démontrer que lorsque t décrit $[0;\pi]$, $M_1$ et $M_2$ décrivent une ellipse $\Gamma$ ; donner une équation cartésienne.
2.b) Éléments caractéristiques et construction.
2.c) Placer $M_1, M_2$ pour $t=\tfrac{\pi}{6}$.
3. Soit f : $M(z)\to M'(z')$ tel que $x'=\dfrac{5z+\bar{z}}{4}$.
3.a) Écrire $x', y'$ en fonction de x, y.
3.b) $f(\Gamma)=\Gamma'$ : équation cartésienne. $\Gamma'$ est un cercle (centre, rayon, construction).
3.c) Méthode géométrique pour construire l'ellipse à partir de $\Gamma'$.""",

    ("C", "math", 2003, "sc", 2): r"""Exercice 2 (5 points)
Dans le plan orienté, trois cercles $\Gamma_1, \Gamma_2, \Gamma_3$ de même rayon et de centres M, N, P, concourants en K et se coupant deux à deux en A, B, C.
1. Construction.
2. $r_1=s_{(KN)}\circ s_{(KA)}$, $r_2=s_{(KM)}\circ s_{(KC)}$, $f=s_{(KB)}\circ s_{(KA)}\circ s_{(KC)}$.
2.a) Nature de $r_1$ et $r_2$.
2.b) $r_1(M)$ et $r_2(P)$ ; conclusion ?
2.c) f est une réflexion ; axe.
3.a) $(\vec{KA},\vec{KB})=(\vec{KC},\vec{KP})\ [\pi]$ et deux relations semblables.
3.b) $(\vec{KA},\vec{BC})=\tfrac{\pi}{2}\ [\pi]$.
3.c) K est l'orthocentre du triangle ABC.
4. Cercles $\Gamma_4, \Gamma_5$ circonscrits à ABC et MNP. Montrer que les cinq cercles ont même rayon.""",

    ("C", "math", 2003, "sc", 3): r"""Problème (10 points)
$f_n(x)=(2+\sin(nx))e^{1-nx}$, $n\in\mathbb{N}^*$ ; courbe $(C_n)$.

Partie A — Étude de $f(x)=f_1(x)=(2+\sin x)e^{1-x}$.
1.a) Démontrer $\cos x+\sin x=\sqrt{2}\cos(x-\tfrac{\pi}{4})$.
1.b) En déduire $f'(x)$ et la stricte monotonie de f.
2.a) $e^{1-x}\le f(x)\le 3e^{1-x}$.
2.b) Limites en $\pm\infty$ et interprétation.
3. Tableau de variations et bijection.
4. $f''(x)=2(1+\cos x)e^{1-x}$.
5. Positions relatives avec $\Gamma_1$ et $\Gamma_2$ et points de contact.
6. Construction de $(C_1), \Gamma_1, \Gamma_2$ sur $[-\pi;\pi]$.
7. Aire entre $(C_1)$, (Ox) et $x=0, x=1$.

Partie B — $A_n=\int_0^1 f_n(x)\,dx$.
1. Démontrer la relation entre $A_n$ et $\int \sin(nx)e^{1-nx}\,dx$.
2. Calculer $I_n=\int_0^1 \sin(nx)e^{1-nx}\,dx$ et $J_n=\int_0^1 \cos(nx)e^{1-nx}\,dx$.
3. Expression de $A_n$ en fonction de n et comparaison.""",

    # ═══════════════ 2003 SESSION NORMALE ═══════════════
    ("C", "math", 2003, "sn", 1): r"""Exercice 1 (4 points)
$f(x)=\dfrac{1}{\ln x}$ sur $]1,+\infty[$ et $g_n(x)=\int_x^{x^n}f(t)\,dt$ pour $n\ge 2$.
1. Tableau de variations de f.
2.a) Démontrer $0<\ln t<t-1$ pour $t>1$ et en déduire $g_2(x)\ge\ln\tfrac{2x-1}{x-1}$.
2.b) Montrer $g_n(x)\ge g_2(x)$ et $\lim_{x\to 1^+} g_n(x)=+\infty$.
3.a) Montrer $\tfrac{(n-1)x}{\ln(nx)}\le g_n(x)\le\tfrac{(n-1)x}{\ln x}$.
3.b) $\lim_{x\to +\infty} g_n(x)$ et $\lim_{x\to +\infty}\tfrac{g_n(x)}{x}$.
4.a) Calculer $g_n'(x)$ et $g_n''(x)$.
4.b) Allure de $(C_2)$ et encadrement de l'ordonnée du point à tangente horizontale.""",

    ("C", "math", 2003, "sn", 2): r"""Exercice 2 (5 points)
$U_n=\int_0^1 \dfrac{e^{-nx}}{1+e^x}\,dx$ et $S_n=\sum_{p=1}^n U_p$.
1. $W_n=\sum_{p=1}^n \tfrac{1}{p}$. Montrer $\tfrac{1}{p+1}\le\ln(p+1)-\ln p\le\tfrac{1}{p}$ et encadrement/limite de $W_n$.
2. $V_n=\dfrac{1-e^{-n}}{n}$ et $T_n=\sum_{p=1}^n V_p$.
2.a) Montrer $\tfrac{e^{-x}}{2}\le\tfrac{1}{1+e^x}\le\tfrac{1}{2}$ sur [0,1].
2.b) $V_n=\int_0^1 e^{-nx}\,dx$ et $\tfrac{1}{2}V_{n+1}\le U_n\le\tfrac{1}{2}V_n$.
2.c) Déduire $\lim U_n$ et $\lim nU_n$.
3.a) $0\le\sum_{p=1}^n\tfrac{e^{-p}}{p}\le\tfrac{1}{e-1}$.
3.b) $\lim T_n=+\infty$ et $\lim\tfrac{T_n}{\ln n}$.
3.c) Déduire $\lim S_n$.""",

    ("C", "math", 2003, "sn", 3): r"""Problème (11 points)
Triangle ABC direct, on construit à l'extérieur ACQ, BAR et CBP rectangles isocèles en A, B, C. $P', Q', R'$ milieux de [BP], [CQ], [AR].

Partie A.
1. Construction.
2.a) Affixes $p', q', r'$ en fonction de a, b, c.
2.b) ABC et P'Q'R' ont le même centre de gravité G.
3. ABC et PQR ont aussi le même centre de gravité G.

Partie B.
1. Similitudes $s_1$ (centre C, $Q\to A$) et $s_2$ (centre A, $Q'\to Q$).
2. Nature de $\sigma=s_1\circ s_2$ et prouver $P'A=R'Q'$ et $(P'A)\perp(R'Q')$.
3. Construction du triangle ABC à partir de $P'Q'R'$.

Partie C : Cas équilatéral.
1. Construction.
2. PQR et $P'Q'R'$ équilatéraux via une rotation de centre G et d'angle $\tfrac{2\pi}{3}$.
3. Similitudes $\sigma_1, \sigma_2$ de centre G. Rapports et angles. Aires de PQR et $P'Q'R'$ en fonction de l'aire de ABC.""",

    # ═══════════════ 2004 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2004, "sc", 1): r"""Exercice 1 (4 points)
Espace muni d'un repère orthogonal $(O;\vec{i},\vec{j},\vec{k})$. Points $A(2;-3;1), B(3;-5;0), C(2;5;-4), D(3;2;3)$.
1.a) Coordonnées de $\vec{AD}, \vec{DB}, \vec{CD}$.
1.b) Montrer $(CD)\perp(ABD)$.
2. H projeté orthogonal de C sur (AB).
2.a) Montrer $(AB)\perp(CDH)$.
2.b) Équation de (CDH) et représentation de (AB).
2.c) Coordonnées de H.
3.a) Longueurs AB, CD, DH et volume du tétraèdre ABCD.
3.b) Distance de D au plan ABC.""",

    ("C", "math", 2004, "sc", 2): r"""Exercice 2 (5 points)
Triangle équilatéral ABC de côté a. D barycentre de $\{(A,-1);(B,-2);(C,2)\}$.
1.a) Construction.
1.b) $(BC)\parallel(AD)$.
1.c) ABD rectangle en B.
2. Ensemble (F) : $-MA^2-2MB^2+2MC^2=0$. Montrer $A\in(F)$, exprimer $f(M)$ selon MD et a, puis construire (F).
3. Ensemble (G) : $2\vec{MA}\cdot\vec{DB}+a^2=a^2$. Déterminer (G) et nature des triangles ADE et ACE (E intersection de F et G).
4. Similitude s : centre A, $B\to D$. Angle, rapport, image de ABC et images de (F) et (G) par $s^{-1}$.""",

    ("C", "math", 2004, "sc", 3): r"""Problème (11 points)
Partie I — $f(x)=x-e^{x-1}$.
1. Tableau de variations.
2. Asymptote $y=x$ et position relative.
3. Tracé.
4. Position relative avec $y=x-3$ et aire délimitée.

Partie II — Application s : $z'=-\tfrac{1}{2}(1+i)z+2$.
1. Nature et éléments de s.
2. $x, y$ en fonction de $x', y'$.
3. Transformées de $x=1$ et $y=x-3$.
4. Montrer que la courbe $(\Gamma)$ de $g(x)=1-x-\ln(4-2x)$ est l'image de (C) par s.

Partie III.
1. Variations de g.
2. Étude de $h(x)=f(x)-g(x)$. Variations de $h'$ et h, limites.
3. Montrer que $h(x)=0$ a deux solutions $\alpha, \beta$ et position relative de (C) et $(\Gamma)$.
4. Tracé de $(\Gamma)$.
5. Aire de la partie transformée $P'$.""",

    # ═══════════════ 2004 SESSION NORMALE ═══════════════
    ("C", "math", 2004, "sn", 1): r"""Exercice 1 (5 points)
Carré direct ABCD de centre O. I, J, K, L milieux des côtés. H intersection de (AJ) et (DI).
1. Étude de la rotation $r_1$ : $A\to I$ et $J\to D$.
1.a) Existence et unicité.
1.b) Angle de $r_1$ via le quart de tour vectoriel.
1.c) Centre $\Omega$ de $r_1$ par 3 méthodes (cocyclicité, $r_1\circ r_1(L)$, ou décomposition en réflexions/barycentre).
2. Images du rectangle ABJL par $r_1$, par un antidéplacement g ($K\to J$, C fixe) et par $r_2=s_{(IL)}\circ s_{(AC)}$.""",

    ("C", "math", 2004, "sn", 2): r"""Exercice 2 (5 points)
Triangle ABC rectangle en A avec $AB=2AC$. H milieu de [AB], E symétrique de H par A. J et K projetés de A et E sur (BC). I projeté de A sur (EK).
1. Figure.
2. Rotation r (centre A, angle $-\tfrac{\pi}{2}$). Déterminer $r(E), r(I), r(C)$ et $r(K)=L$. Montrer $\vec{BL}=\tfrac{1}{3}\vec{BK}$.
3. Homothétie h (centre B, $A\to E$). Rapport et montrer $h(J)=K$.
4. Similitude $s=h\circ r$. Rapport, angle et centre $\Omega$ (intersection de cercles).
5. Paraboles de directrice (BC) passant par A et I. Construction des foyers, axes et sommets. Image par s.""",

    ("C", "math", 2004, "sn", 3): r"""Problème (10 points)
Partie A — $f_n(x)=x^n(1+\ln x)$ pour $x>0$ et $f_n(0)=0$.
1. Continuité et dérivabilité en 0.
2. Variations et tableau.
3. Points communs à toutes les courbes $(C_n)$.
4. Position relative de $(C_n)$ et $(C_{n-1})$.
5. Identification des courbes $f_1, f_2, f_3$ sur graphique.

Partie B — $M_n(x_n, y_n)$ avec $x_n=e^{-(1+1/n)}$.
1. Montrer que $M_n$ appartient à une courbe fixe.
2. Suite $(x_n)$ croissante majorée.
3. Limite de $M_n$ quand $n\to+\infty$.
4. Aire $U_n$ entre $x=e^{-1}$ et $x=1$. Calcul et limite.

Partie C — Fonction g définie par $g(x)=(1+\ln x)e^{-(1+\ln x)/(1-\ln x)}$.
1. Continuité, dérivabilité et limites de g.
2. Variations de g et courbe $\Gamma$.
3. Intersections entre $\Gamma$ et $(C_n)$.""",

    # ═══════════════ 2005 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2005, "sc", 1): r"""Exercice 1 (4 points)
Dans $\mathbb{C}$, on considère (E) : $z^2-2z+1-e^{2i\theta}=0$ où $\theta\in[0,2\pi[$.
1.a) Résoudre (E) ; on note $z_1, z_2$ les solutions.
1.b) Discuter le module et un argument de $z_1, z_2$ suivant $\theta$.
2. $M_1, M_2$ d'affixes $z_1, z_2$.
2.a) Montrer que quand $\theta$ décrit $[0,2\pi[$, $M_1, M_2$ décrivent un cercle $\Gamma$ de centre $A(1,0)$ ; rayon ? La droite $(M_1M_2)$ passe par un point fixe.
2.b) Représenter pour $\theta=\tfrac{\pi}{3}$.
3. Pour $n\ge 2$, équation $(E_n)$ : $(z-1)^n-e^{2i\theta}=0$.
3.a) Solutions $(z_k)$.
3.b) Montrer $z_0+z_1+\cdots+z_{n-1}=n$.
3.c) Montrer que les points $M_k$ d'affixes $z_k$ appartiennent au cercle $\Gamma$.
3.d) $S_n=M_0M_1+M_1M_2+\cdots+M_{n-1}M_0$. Calculer $S_n$ en fonction de $\theta$ et n, puis $\lim_{n\to+\infty}S_n=2\pi$ ; interpréter.""",

    ("C", "math", 2005, "sc", 2): r"""Exercice 2 (5 points)
Triangle direct ABC rectangle isocèle en A. I, J, K milieux de [BC], [AC], [AB]. D image de K par la réflexion d'axe (AC).
1.a) Figure.
1.b) Rotation r de centre A et d'angle $\tfrac{\pi}{2}$, déterminer $r(B), r(J)$. (BJ) et (CD) perpendiculaires.
1.c) Similitude directe s de centre A, d'angle $\tfrac{\pi}{2}$ et rapport $\tfrac{1}{2}$ : $s(B), s(C)$. (BC) et (DJ) perpendiculaires.
1.d) J est l'orthocentre du triangle BCD.
2. F = (BJ) $\cap$ (CD). Montrer que A, D, F, J et A, B, C, F sont cocycliques.
3. $\Gamma_1$ cercle circonscrit à ABC. Lieu de $M'$ quand M décrit $\Gamma_1$ et $s(M)=M'$.
4. N milieu de $[MM']$ pour M distinct de A.
4.a) $\dfrac{AN}{AM}$.
4.b) $\cos\alpha=\tfrac{2\sqrt{5}}{5}$ et $(\vec{AM},\vec{AN})=\alpha$ constant.
4.c) N image de M par une similitude $\sigma$ ; caractériser.
4.d) Lieu géométrique $\Sigma$ de N quand M décrit $\Gamma_1$.""",

    ("C", "math", 2005, "sc", 3): r"""Problème (11 points)
Partie A — Pour $n\ge 1$ et $x\in\mathbb{R}$ : $S_n(x)=1-x+x^2+\cdots+(-1)^n x^n$.
1.a) Primitive de $S_n$ sur $\mathbb{R}$.
1.b) Démontrer que pour tout $x\ne -1$ et $n\ge 2$ : $S_{n-1}(x)=\tfrac{1}{1+x}-\tfrac{(-1)^n x^n}{1+x}$.
2.a) En déduire $\ln(1+x)=x-\tfrac{1}{2}x^2+\cdots+\tfrac{(-1)^{n-1}}{n}x^n+(-1)^n\int_0^x\tfrac{t^n}{1+t}\,dt$.
2.b) Encadrement de $\ln(1+x)$ par développements.
2.c) $\lim_{x\to 0}\tfrac{\ln(1+x)-x}{x^2}=-\tfrac{1}{2}$.

Partie B — $f(x)=\tfrac{\ln(1+x)}{x}$ pour $x\in]-1,0[\cup]0,+\infty[$ et $f(0)=1$.
1.a) Continuité en 0.
1.b) Dérivabilité en 0 et $f'(0)$.
2. $u(x)=x-(x+1)\ln(x+1)$.
2.a) Variations de u ; $u(x)\le 0$ pour $x>-1$.
2.b) $f'(x)=\tfrac{u(x)}{x^2(x+1)}$.
2.c) Tableau de variation de f.

Partie C — $g(x)=x\ln(\tfrac{1+x}{x})$ pour $x\ne 0$ et $g(0)=0$.
1.a) Définie sur $D=]-\infty,-1[\cup[0,+\infty[$.
1.b) Continuité et dérivabilité à droite en 0.
2.a) $g'(x)$ ; g croissante sur D.
2.b) Tableau de variation.
3. $h(x)=g(-x-1)$.
3.a) Expression de $h(x)$.
3.b) Variations.
3.c) Réflexion d'axe $x=-\tfrac{1}{2}$ transforme (C) en $(C')$.
4. Pour $n\ge 2$, $U_n=(1+\tfrac{1}{n})^n$ et $V_n=(1+\tfrac{1}{n})^{n+1}$.
4.a) $g(n)\le 1\le h(n)$ ; $U_n\le e\le V_n$.
4.b) $1\le\tfrac{e}{U_n}\le 1+\tfrac{1}{n}$ ; $\lim U_n=e$.
4.c) $(U_n)$ et $(V_n)$ adjacentes.""",

    # ═══════════════ 2005 SESSION NORMALE ═══════════════
    ("C", "math", 2005, "sn", 1): r"""Exercice 1 (4 points)
$P(z)=z^3-(5+7i)z^2+(-6+26i)z+24-24i$.
1.a) Montrer que $P(z)=0$ admet une solution imaginaire pure.
1.b) Résoudre $P(z)=0$.
2. A, B, C points images tels que $|z_A|<|z_B|<|z_C|$.
2.a) Montrer que O, A, B, C sont cocycliques.
2.b) Affixe de G barycentre de $\{(O;5),(A;-3),(C;4)\}$ et G milieu de [AB].
2.c) Ensemble $\Gamma$ des points M tels que $\tfrac{z-2}{z-4i}$ soit imaginaire pur.
3. $\varphi(M)=5MO^2-3MA^2+4MC^2$.
3.a) Discuter selon k la nature de $\Gamma_k=\{M:\varphi(M)=k\}$.
3.b) Construire $\Gamma_{60}$.
4. f : $M(z)\to M'(z')$ avec $z'=\tfrac{3z-\bar{z}}{4}$ et $\Gamma:(x-1)^2+(y-2)^2=5$.
4.a) $x', y'$ en fonction de x, y.
4.b) Équation de $\Gamma'=f(\Gamma)$.
4.c) $\Gamma'$ est une ellipse (centre, sommets, excentricité).""",

    ("C", "math", 2005, "sn", 2): r"""Exercice 2 (6 points)
$f_n(x)=\dfrac{\ln x}{x^n}$ sur $]0,+\infty[$.
1. Tableau de variation de $f_n$.
2.a) Les courbes $(C_n)$ passent par un point fixe A et ont la même tangente en A.
2.b) Position relative de $(C_n)$ et $(C_{n+1})$.
2.c) Lieu des points $M_n$ à tangente horizontale.
3. Tracer $(C_3)$.
4. $f=f_2$ et $S_n=\sum_{k=2}^n f(k)$.
4.a) $f(k+1)\le\int_k^{k+1}f(x)\,dx\le f(k)$.
4.b) $S_n-\tfrac{\ln 2}{8}\le\int_2^n f(x)\,dx\le S_n-\tfrac{\ln n}{n^2}$.
4.c) Encadrement de $S_n$.
4.d) Calcul d'intégrale et convergence de $(S_n)$.
4.e) $\tfrac{\ln(2\sqrt{e})}{8}<\lambda<\tfrac{\ln(4\sqrt{e})}{8}$ où $\lambda=\lim S_n$.""",

    ("C", "math", 2005, "sn", 3): r"""Problème (10 points)
Carré direct ABCD. M sur $[AC]$. E, F, G, H projetés de M sur les côtés.

Partie A : Concourance.
2. Homothéties $h_1, h_2$ de centre P (intersection de (AF) et (CE)). Montrer que (DM), (CE), (AF) sont concourantes.
3. Rotation vectorielle $\varphi$ d'angle $\tfrac{\pi}{2}$. Montrer $(DE)\perp(AF)$.
4. Déduire par réflexion la concourance de (BM), (CH), (AG).

Partie B : Cercles concourants.
1. Similitude s de centre $\Omega$ (intersection de (DM) et (EF)) telle que $s(M)=F$.
2. Image du carré AEMH par s.
3. Montrer que les cercles de diamètres [FM], [ME], [GA], [CH] sont concourants.

Partie C : Carrés.
1. $O_1, O_2, I, J$ milieux de [CM], [AM], [BM], [DM]. $O_1JO_2I$ est un carré d'aire constante.
2. Lieu de J.
3. Carré SGTH : S est fixe et déterminer le lieu de T.
4. Aire $f(x)$ entre $O_1JO_2I$ et SGTH avec $AE=x$.

Partie D : Coniques.
M au centre du carré. Parabole $\mathcal{P}$ (sommet H, directrice (CD)) et Ellipse $\mathcal{E}$ (foyers A, B, grand axe $a\sqrt{2}$).
1. Foyer de $\mathcal{P}$, montrer $B\in\mathcal{P}$. M est un sommet de $\mathcal{E}$.
2. (FH) est une tangente commune.
3. Tangentes à $\mathcal{P}$ et $\mathcal{E}$.""",

    # ═══════════════ 2006 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2006, "sc", 1): r"""Exercice 1 (5 points)
Application $s_t : z\to z_t=f(t)(\cos t+i\sin t)z$ avec $f(t)>0$.
1. Nature et éléments.
2. Cas $f(t)=\dfrac{1}{\cos t}$.
2.a) Montrer que $OMM_t$ est rectangle en M.
2.b) Lieu $\Gamma(M)$ décrit par $M_t$.
2.c) Image de la droite $x=a$.
3. Cas $f(t)=\cos t$. Montrer que $OMM_t$ est rectangle en $M_t$. Lieu $\Gamma'(M)$.
4. Mesure de $(\vec{AM},\vec{A_tM_t})$. Montrer que $O, H_t, A, A_t$ sont cocycliques ($H_t$ intersection des droites). Montrer que l'image de la droite $x=a$ passe par un point fixe.""",

    ("C", "math", 2006, "sc", 2): r"""Exercice 2 (4 points)
Équation $(iz)^n=(z+2i)^n$ ($n\ge 2$).
1.a) Solutions $z_1, z_2$ pour $n=2$.
1.b) $u=-\tfrac{\sqrt{2}}{2}z_1$, montrer $u^p+\bar{u}^p=2\cos(\tfrac{p\pi}{4})$.
1.c) Soit $f(x)=\sum_{p=0}^n C_n^p x^p \cos(\tfrac{p\pi}{4})$. Montrer $f(x)=\tfrac{1}{2}[(1+ux)^n+(1+\bar{u}x)^n]$.
1.d) Résoudre $f(z)=0$.
2.a) Montrer que si z est solution alors $OM=AM$ ($A(-2i)$).
2.b) En déduire $z=a-i$ ($a\in\mathbb{R}$).
3.a) Résoudre $(iz)^n=(z+2i)^n$.
3.b) $x_k=-i+\tan(\tfrac{\pi}{4}-\tfrac{k\pi}{n})$.""",

    ("C", "math", 2006, "sc", 3): r"""Problème (11 points)
Partie A — $f(x)=\tfrac{1}{2}\ln(\tfrac{1+x}{1-x})$. Ensemble de définition, parité, variations, tracé. Réciproque $g(x)=\tfrac{e^x-e^{-x}}{e^x+e^{-x}}$. Aire entre les deux courbes.

Partie B — $I_n(x)=\int_0^x [g(t)]^n\,dt$ ($x\ge 0$).
1. Calculer $I_0, I_1$. Montrer $0\le I_{2p}(x)\le x(g(x))^{2p}$ et limite.
2. Relation $I_{n+2}(x)=I_n(x)-\tfrac{1}{n+1}[g(x)]^{n+1}$. Calculer la limite d'une somme.

Partie C — $h(x)=\int_0^x\dfrac{t^2}{1-t^2}\,dt$ sur $]-1,1[$. Décomposition en éléments simples et relation $h(x)=-x+f(x)$. Étude de la suite $U_n=\ln(n!)-(n+\tfrac{1}{2})\ln(n)+n$. Montrer la convergence.""",

    # ═══════════════ 2006 SESSION NORMALE ═══════════════
    ("C", "math", 2006, "sn", 1): r"""Exercice 1 (4 points)
Parabole $\mathcal{P}$ (foyer $F(0,2)$, directrice $y=4$).
1.a) Pour $M\in\mathcal{P}$ ($y<2$), montrer $MF-MH=2$ (H sur $\Delta:y=2$).
1.b) Tangence de cercles.
2.a) Équation de $\mathcal{P}$ et tracé.
2.b) Lieu du milieu I de [ST] (S, T intersections avec $y=mx+2$).
3. Ellipse $\mathcal{E}$ ($e=\tfrac{1}{3}, F(0,2), y=4$).
3.a) Montrer que $\mathcal{P}$ et $\mathcal{E}$ sont disjointes.
3.b) Équation de $\mathcal{E}$, sommets, second foyer, seconde directrice, tracé.""",

    ("C", "math", 2006, "sn", 2): r"""Exercice 2 (5 points)
Carré direct ABCD. I, J, K milieux de [AB], [AD], [BC].
1. Antidéplacement f : $D\to A, J\to I$. Vérifier $f=S_{(DB)}\circ t_{\vec{JK}}$.
2. Caractériser f (décomposition ou écriture complexe).
3. $g=S_{(AI)}\circ f$. Caractériser le déplacement g.
4. Similitude directe S : $D\to O, C\to I$. Rapport, angle, $S(B), S(A)$.
5. $S\circ S$ : éléments et centre $\Omega$ barycentre de $\{(B,1);(J,4)\}$.
6. Caractériser $S\circ S'$ ($S'$ centre B, $C\to E$ avec $\vec{BE}=2\vec{BA}$).""",

    ("C", "math", 2006, "sn", 3): r"""Problème (11 points)
Partie A — $f(x)=\dfrac{e^x}{e^{2x}+1}$ ($x\ge 0$) et $f(x)=\dfrac{-\ln(1-x)}{2x}$ ($x<0$).
1. Continuité en 0.
2. Dérivabilité.
3. Limite de $\tfrac{\ln(1-h)+h}{h^2}$ et dérivabilité à gauche en 0.
4. Variations de f et de $v(x)=x+(1-x)\ln(1-x)$. Tableau de variation complet et tracé.

Partie B — $G(x)=\int_0^{\ln(\tan x)} f(t)\,dt$ sur $[\tfrac{\pi}{4},\tfrac{\pi}{2}[$.
1. Calculer $G(\tfrac{\pi}{4})$ et $G'(x)$.
2. Prouver $G(x)=x-\tfrac{\pi}{4}$.
3. Aire $A(\beta)$ entre courbe, (Ox), $x=0, x=\beta$. Calculer $\lim_{\beta\to+\infty}A(\beta)$.""",

    # ═══════════════ 2007 SESSION COMPLÉMENTAIRE ═══════════════
    ("C", "math", 2007, "sc", 1): r"""Exercice 1 (4 points)
Carré direct ABCD de centre O et de côté a. E symétrique de C par rapport à D.
1.a) Déterminer chacun des ensembles :
$\Gamma_1:\|\vec{MA}-\vec{MB}+\vec{MC}\|=a$
$\Gamma_2:MA^2-MB^2+MC^2=a^2$
$\Gamma_3:(\vec{MA}-\vec{MB}-\vec{MD})\cdot(2\vec{MA}-2\vec{MB}+\vec{MC})=0$
$\Gamma_4:\|\vec{MA}-\vec{MB}-\vec{ME}\|=\|\vec{MD}-\vec{MC}\|$
1.b) Constat sur les quatre ensembles.
2. Pour $k\in\mathbb{R}$, application f : $\vec{MM'}=\vec{MA}-\vec{MB}+(1-k)\vec{MC}$.
2.a) Pour quelles valeurs de k, f est une translation ? Vecteur.
2.c) Pour $k\in\mathbb{R}^*\setminus\{1\}$, f admet un unique point invariant $\Omega_k$. Lieu des $\Omega_k$.
2.d) Pour $k=\tfrac{1}{2}$, lieu du centre de gravité G du triangle DMM' quand M décrit le cercle I de diamètre [CE].""",

    ("C", "math", 2007, "sc", 2): r"""Exercice 2 (6 points)
Carré direct ABCD de centre O et de côté a. I, J, K, L milieux des côtés.
1.a) Figure ((AB) horizontale).
2.a) Vérifier $r=S_{(OJ)}\circ S_{(IJ)}=S_{(OI)}\circ S_{(LK)}$.
2.b) Rapport et angle de $s_1$.
2.c) Existence d'une unique rotation qui transforme A en O et B en K.
2.d) Angle et centre de cette rotation.
3.a) Unique similitude directe $s_1$ qui transforme O en L et C en B.
3.b) $s_1(A)=A$.
4. Similitude directe $S_2$ : $A\to O, B\to D$.
4.a) Rapport et angle de $S_2$.
4.b) Nature et éléments de $g=S_{(OI)}\circ S_{(LI)}\circ S_{(KJ)}$.
5.b) Le centre T de $s_1$ appartient au cercle $(C_1)$ de centre C et rayon CD, et au cercle $(C_2)$ de diamètre [AB].
5. $h=s_2\circ s_1^{-1}$ ; pour tout M : $s_1(M)=M'$ et $s_2(M)=M''$.
5.a) En utilisant h, montrer que le milieu F de $[M'M'']$ est un point fixe.
5.b) $s_1(O)=L$.
5.c) A, F, T, L cocycliques.
6.a) Position de $M'$ et $M''$ pour $M=A, F, T, L$.
6.b) Pour M distinct, $(\vec{MM'},\vec{MF})=-\tfrac{\pi}{4}+(\vec{MA},\vec{MF})\ [\pi]$.
6.c) Lieu $\Gamma$ des M tels que $M, M', M''$ sont alignés.""",

    ("C", "math", 2007, "sc", 3): r"""Problème (10 points)
$f_n(x)=x-n\ln x$ pour $x>0$, courbe $C_n$.

Partie A (5 points).
1. Cas $n=1$ : $f_1(x)=x-\ln x$.
1.a) $\lim_{x\to 0^+}f_1$ ; $\lim_{x\to+\infty}f_1$ ; $\lim_{x\to+\infty}\tfrac{f_1(x)}{x}$ ; $\lim_{x\to+\infty}(f_1(x)-x)$.
1.b) Tableau de variation.
1.c) Tracer $C_1$.
2. Cas $n\ge 1$.
2.a) Tableau de variation.
2.b) Points communs aux $C_n$ et positions relatives.
2.c) Tangentes aux $C_n$ aux points d'abscisses $x_n=n$ passent par un point commun.
3. $M_0, M_1, M_n$ de même abscisse x sur $C_0, C_1, C_n$.
3.a) $f_n(x)-f_0(x)=n(f_1(x)-f_0(x))$.
3.b) $\vec{M_nM_0}=n\vec{M_1M_0}$.
3.c) Construction de $C_n$ à partir de $C_1$ et $C_0$. Construire $C_2$.

Partie B (5 points). $g(x)=\dfrac{x}{x-\ln x}$ pour $x>0$.
1.a) Domaine de définition $D_g=[0,+\infty[$.
1.b) Continuité.
2.a) $\lim_{x\to+\infty}g(x)$.
2.b) $\lim_{x\to 0^+}\tfrac{g(x)}{x}$.
3.a) $g'(x)$.
3.b) Tableau de variation et courbe $\Gamma$.
4. $\forall x\in[1,e]: 0\le\tfrac{\ln x}{x}\le\tfrac{1}{e}$.
5. $U_n=\int_1^e(\tfrac{\ln x}{x})^n\,dx$, $U_0=e-1$.
5.a) Calculer $U_0, U_1$.
5.b) $(U_n)$ positive et décroissante.
5.c) $0\le U_n\le\tfrac{e-1}{e^n}$ ; $\lim U_n=0$.
6. $I=\int_1^e g(x)\,dx$ et $S_n=U_0+\cdots+U_n$.
6.a) $S_n=\int_1^e\tfrac{1-(\ln x/x)^{n+1}}{1-\ln x/x}\,dx$.
6.b) $1-S_n=\int_1^e\tfrac{x}{x-\ln x}(\tfrac{\ln x}{x})^{n+1}\,dx$.
6.c) $0\le 1-S_n\le\tfrac{I}{e^{n+1}}$ ; $\lim S_n=1$.
6.d) $S_n\le 1\le S_{n+1}$.
6.e) Pour quelles n, $S_n$ approche 1 à $e^{-(n+1)}$ près.""",

    # ═══════════════ 2007 SESSION NORMALE ═══════════════
    ("C", "math", 2007, "sn", 1): r"""Exercice 1 (4 points)
Triangle direct ABC d'angles aigus de centre de gravité G. On construit $[AA'], [BB'], [CC']$ tels que $AA'=BC$ et $(\vec{BC},\vec{AA'})=\tfrac{\pi}{2}\ [2\pi]$, et deux relations analogues. Rotation vectorielle $\varphi$ d'angle $-\tfrac{\pi}{2}$.

A) ABC et $A'B'C'$ ont même centre de gravité.
Méthode 1 (complexes).
a) $a'=a-ib+ic$.
b) Écrire $b', c'$.
c) Conclusion.
Méthode 2 (rotation vectorielle).
a) $\varphi(\vec{AA'}+\vec{BB'}+\vec{CC'})=\vec{0}$.
b) $\vec{GA'}+\vec{GB'}+\vec{GC'}=\vec{0}$.
c) Conclusion.

B) Construire ABC connaissant $A'B'C'$.
Méthode 1. $\tfrac{c-b'}{c-a'}=i$, nature de $A'B'C$. Résultats similaires.
Méthode 2. $\varphi(\vec{CB'})=\vec{CA'}$ ; nature. Résultats similaires.
Construire ABC à partir de $A'B'C'$.""",

    ("C", "math", 2007, "sn", 2): r"""Exercice 2 (5 points)
Losange direct ABCD de centre I tel que $IB=2IC=2a$. $\Gamma_1$ cercle de centre C rayon $CI=a$, $\Gamma_2$ centre B rayon $BI=2a$.
1.a) Figure ((BD) horizontale).
1.b) E, F tels que $\vec{EB}+2\vec{EC}=\vec{0}$ et $\vec{FB}-2\vec{FC}=\vec{0}$.
2. $\Gamma_3=\{M:\tfrac{MB}{MC}=2\}$.
2.a) I, E, F appartiennent à $\Gamma_3$.
2.b) Construction de $\Gamma_3$.
3. Unique rotation r : $C\to B, A\to I$. Angle et centre.
4.a) Unique similitude s : $C\to B, A\to D$.
4.b) $s(I)=I$.
4.c) Éléments.
4.d) $s(\Gamma_1)=\Gamma_2$.
5. $f=h\circ r$ avec h homothétie de centre B et rapport 2.
5.a) $f=s$.
5.b) Forme réduite de s.
6. $s'$ similitude qui transforme $\Gamma_1$ en $\Gamma_2$.
6.a) Rapport k' constant.
6.b) Lieu géométrique des centres.
6.c) Cas où $s'$ est une homothétie : centres et rapports possibles.""",

    ("C", "math", 2007, "sn", 3): r"""Problème (11 points)
Partie A — $f(x)=\ln\left|\dfrac{x}{x-1}\right|$ pour $x\in\mathbb{R}\setminus\{0;1\}$.
1.a) Limites en 0, $-\infty, +\infty, 1$ ; interprétation.
1.b) $f'(x)$.
1.c) Tableau de variation.
2.a) $f(x)+f(1-x)=0$.
2.b) Interpréter.
2.c) Tracer C.
3. Pour $k\in\mathbb{R}^*$, $f_k(x)=\ln\left|\dfrac{kx}{x-1}\right|$ ; $C_k$ sa courbe.
3.a) Le point $\Omega(\tfrac{1}{2};\ln|k|)$ est centre de symétrie de $C_k$.
3.b) $C_k$ image de C par une transformation simple.
3.c) Que dire des courbes $C_k$ et $C_{-k}$ ?""",

    # ═══════════════ 2008 SESSION COMPLÉMENTAIRE (5 exos) ═══════════════
    ("C", "math", 2008, "sc", 1): r"""Exercice 1 (4 points)
$P(z)=z^3-(4+8i)z^2+(-16+20i)z+24+8i$.
1.a) Calculer $P(2i)$.
1.b) $\alpha, \beta$ tels que $P(z)=(z-2i)(z^2+\alpha z+\beta)$ ; résoudre $P(z)=0$.
2. Repère $(O;\vec{u},\vec{v})$. A, B d'affixes $2+2i, 2i$. Cercle $\Gamma$ de diamètre [OA]. M variable sur $\Gamma\setminus\{O,A\}$. Triangles AEM et OMF directs, isocèles rectangles en A et O. G centre de gravité de OAM. e, f, g, m affixes.
a) Figure ; démontrer $|m-1-i|=\sqrt{2}$.
b) Écrire e, f, g en fonction de m.
c) Milieu H de [EF] indépendant de M sur $\Gamma$.
d) Lieux de E, F, G quand M décrit $\Gamma$.
e) Position de M pour (EF) tangente à $\Gamma$. Affixe de E.""",

    ("C", "math", 2008, "sc", 2): r"""Exercice 2 (4 points)
$U_0=\int_0^1\dfrac{1}{1+x^2}\,dx$ et $U_n=\int_0^1\dfrac{x^{2n}}{1+x^2}\,dx$.
a) En posant $x=\tan t$, $t\in[0;\tfrac{\pi}{2}[$, montrer $U_0=\tfrac{\pi}{4}$.
b) $(U_n)$ positive et décroissante ; convergente.
c) $U_{n+1}+U_n=\tfrac{1}{2n+1}$ ; déduire $U_1, U_2$.
d) Encadrement de $U_n$ permettant le calcul de la limite ; $\lim U_n$.
2. $V_0=\int_0^1\ln(1+x^2)\,dx$ et $V_n=\int_0^1(2n+1)x^{2n}\ln(1+x^2)\,dx$.
a) Par IPP, $V_n=\ln 2-2U_{n+1}$.
b) Valeur exacte de $\int_0^1\ln(x^2+1)\,dx$.
c) Variations de $(V_n)$ et $\lim V_n$.""",

    ("C", "math", 2008, "sc", 3): r"""Exercice 3 (4 points)
$f(x)=\dfrac{\ln x}{x^2}$ sur $\mathbb{R}_+^*$. Tableau de variation et courbe.
2. $f_k(x)=\dfrac{\ln x}{x^2}-kx$ pour $k\in[0;1]$, courbe $(C_k)$.
a) Limites en $+\infty$ et $0^+$ ; asymptotes.
b) $1-kx^3-2\ln x=0$ admet une unique solution $\alpha_k$ ; $1\le\alpha_k\le\sqrt{e}$.
c) $f_k'(x)$ et tableau de variation.
3.a) Position relative de $(C_k)$ et $(C_{k'})$ pour $0\le k<k'\le 1$.
3.b) Identifier $(C_0), (C_{0,2}), (C_{0,8})$ sur la figure.
4. $M_k$ point à tangente horizontale ; lieu $(\Gamma)$ (équation cartésienne).""",

    ("C", "math", 2008, "sc", 4): r"""Exercice 4 (4 points)
Carré direct ABCD de côté a. E, F, G, H définis par $\vec{AE}=\tfrac{1}{3}\vec{AB}$, $\vec{BF}=\tfrac{1}{3}\vec{BC}$, $\vec{CG}=\tfrac{1}{3}\vec{CD}$, $\vec{DH}=\tfrac{1}{3}\vec{DA}$.
1. Figure ((AB) horizontale).
2.a) Unique rotation r : $A\to B, E\to F$.
2.b) Angle et centre.
2.c) EFGH carré, aire en fonction de a.
3. Similitude directe s de centre O : $A\to E$.
3.a) $s(B)=F$ ; $s(C), s(D)$.
3.b) Rapport.
3.c) $\cos\alpha$.
4. I, J, K, L : I=[AG]$\cap$[BH], J=[BH]$\cap$[CE], K=[CE]$\cap$[DF], L=[DF]$\cap$[AG].
a) IJKL carré.
b) $K=\text{bar}\{(D,4);(F,9)\}=\text{bar}\{(C,7);(E,6)\}$.
c) Aire de IJKL en fonction de a.""",

    ("C", "math", 2008, "sc", 5): r"""Exercice 5 (4 points)
Triangle équilatéral ABC direct de côté a. D, E symétriques de A, B par C. I milieu de [BC].
1. Figure.
2.a) Unique similitude directe $s_1$ de centre B qui transforme D en A.
2.b) Angle et rapport.
2.c) M sur (DE) distinct de D, E. Lieu de $M'=s_1(M)$. Construire ; cocyclicité de $M', M, B, E$.
3. $S_2$ similitude qui transforme I en B et E en D.
a) Angle et rapport.
b) Centre.
4. $f=s_1\circ S_2$.
a) Similitude directe ; angle et rapport.
b) Centre = intersection du cercle de diamètre [BE] avec un autre cercle.""",

    # ═══════════════ 2008 SESSION NORMALE (5 exos) ═══════════════
    ("C", "math", 2008, "sn", 1): r"""Exercice 1 (3 points)
$f(x)=x+\dfrac{1}{e^x+1}$ sur $\mathbb{R}$. Courbe (C).
1.a) Tableau de variation.
1.b) Bijection de $\mathbb{R}$ sur un intervalle J.
2. Démontrer et interpréter :
a) $\lim_{x\to+\infty}(f(x)-(x+1))=0$.
b) $\lim_{x\to-\infty}(f(x)-x)=0$.
c) $x\le f(x)\le x+1$.
d) $f(-x)+f(x)=1$.
e) $f(-0,7)\times f(-0,6)<0$.
3. Construire (C).""",

    ("C", "math", 2008, "sn", 2): r"""Exercice 2 (3 points)
$U_n=\int_1^e x^3(\ln x)^n\,dx$ pour $n\in\mathbb{N}^*$.
1.a) Par IPP, $U_1=\dfrac{3e^4+1}{16}$.
1.b) $(U_n)$ décroissante et positive ; conclusion.
2.a) Par IPP, $4U_n+nU_{n-1}=e^4$ pour $n\ge 2$.
2.b) Calculer $U_2, U_3$.
3.a) $\dfrac{e^4}{n+5}\le U_n\le\dfrac{e^4}{n+4}$.
3.b) $\lim U_n$ et $\lim nU_n$.""",

    ("C", "math", 2008, "sn", 3): r"""Exercice 3 (4 points)
$P(z)=z^3-(5+6i)z^2+(-4+14i)z+8-8i$.
1.a) $P(1)$.
1.b) Résoudre $P(z)=0$.
2. Repère $(O;\vec{u},\vec{v})$ direct. A, B, C, G : $z_A=2i, z_B=1, G=\text{bar}\{(A,2),(B,-2),(C,-1)\}, z_G=6$.
a) $z_C$ ; ABC rectangle en A. Placer.
b) $\Gamma_1:2MA^2-2MB^2-MC^2=-10$ et $\Gamma_2:MA^2-MB^2=-5$.
c) Position relative de $\Gamma_1$ et $\Gamma_2$.""",

    ("C", "math", 2008, "sn", 4): r"""Exercice 4 (4 points)
$u(x)=\dfrac{1}{\ln x}$ sur $]1;+\infty[$. Tableau de variation.
2. $f(x)=e^{1/\ln x}$. Stricte décroissance et tableau.
3. $F_n(x)=\int_x^{x+n}f(t)\,dt=\int_x^{x+n}e^{1/\ln t}\,dt$ sur $]1;+\infty[$.
a) $nf(x+n)\le F_n(x)\le nf(x)$ ; $\lim_{x\to+\infty}F_n(x)$.
b) $e^x>1+x$ pour $x>0$ ; $0<\ln t<t-1$ pour $t>1$.
c) $F_n(x)-n>\ln(\tfrac{x+n-1}{x-1})$.
d) Tableau de variation de $F_n$ ; $\lim_{x\to 1^+}F_n(x)$.
e) Allure de $F_1$ (cas $n=1$).""",

    ("C", "math", 2008, "sn", 5): r"""Exercice 5 (6 points)
Triangle ABE direct rectangle isocèle en A. AEFG carré direct. I, O, C milieux de [AB], [BE], [EA]. J symétrique de I par O.
1.a) Figure ((AB) horizontale).
1.b) Unique rotation r : $A\to B, E\to A$.
1.c) Angle et centre.
1.d) $r(J)$.
2.a) Unique similitude directe s : $C\to A, A\to B$.
2.b) Angle et rapport.
2.c) $s(E)=G$ ; image du carré COJE par s.
3. $\Omega$ centre de s.
a) $\Omega$ sur les cercles de diamètres [JF], [EG], [CA], [AB].
b) Cercles de diamètres [JF] et [AB] tangents en $\Omega$.
4. $\Gamma, \Gamma'$ cercles passant par $\Omega$ de centres A, B. D autre intersection.
a) $s(\Gamma)=\Gamma'$ ; $\Omega, A, B, D$ cocycliques.
b) Pour $M\in\Gamma\setminus\{\Omega,D\}$, $M'=s(M)$ ; $M, M', D$ alignés.""",

    # ═══════════════ 2009 SESSION COMPLÉMENTAIRE (4 exos) ═══════════════
    ("C", "math", 2009, "sc", 1): r"""Exercice 1 (4 points)
$f_\omega : M(z)\to M'(z')$ avec $z'=(\tfrac{1}{2}+\omega i)z+1-2\omega i$, $\omega\in\mathbb{C}$.
1. Caractériser $f_\omega$ pour :
a) $\omega=\tfrac{\sqrt{3}}{2}$ ; b) $\omega=-\tfrac{1}{2}i$ ; c) $\omega=1+\tfrac{1}{2}i$ ; d) $\omega=2i$.
2. On suppose $\omega\in\mathbb{R}$ et $\theta=\arg(\tfrac{1}{2}+\omega i)$, $\theta\in]-\pi;\pi]$. $A(2;0), M_0(3;0)$. $M_{n+1}=f_\omega(M_n)$, $z_n$ affixe.
a) Vérifier $z_1=\tfrac{5}{2}+\omega i$ ; calculer $z_2$.
b) $z_n=2+(\tfrac{1}{2\cos\theta})^n e^{in\theta}$.
c) $V_n=|z_n-2|$ géométrique ; valeurs de $\omega$ pour $(V_n)$ convergente.
d) $d_n=\|M_nM_{n+1}\|=V_{n+1}$ ; $S_n=\sum_{k=0}^n d_k$ et interprétation.""",

    ("C", "math", 2009, "sc", 2): r"""Exercice 2 (5 points)
$f_n(x)=\dfrac{e^{(1-n)x}}{1+e^x}$, $n\in\mathbb{N}$, courbe $C_n$.
1.a) Tableau de variation de $f_0(x)=\dfrac{e^x}{1+e^x}$.
1.b) $C_0$ admet deux asymptotes horizontales.
1.c) $\Omega(0,\tfrac{1}{2})$ centre de symétrie ; construire $C_0$.
2.a) $f_1(x)=f_0(-x)$ ; transformation pour construire $C_1$.
2.b) $f_1(x)=1-f_0(x)$ ; autre transformation.
2.c) Construction de $C_1$.
3. $U_n=\int_0^1 f_n(x)\,dx$.
a) Calculer $U_0, U_1$.
b) $0<U_n<\tfrac{1}{n-1}$ pour $n>1$ ; $\lim U_n$.
4. $V_n=\dfrac{(-1)^n}{n}(1-\tfrac{1}{e^n})$ pour $n\ne 0$, $V_0=1$. $S_n=V_0+\cdots+V_n$.
a) $U_{n+1}+U_n=|V_n|$.
b) $|S_n-U_0|=|U_{n+1}|$ ; $\lim S_n$.""",

    ("C", "math", 2009, "sc", 3): r"""Exercice 3 (5 points)
Triangle équilatéral ABC direct de côté a. G centre de gravité. D symétrique de A par C.
1. Figure.
2.a) Unique rotation r : $A\to C, B\to D$.
2.b) Angle et centre E ; placer.
3. A, B, D, E cocycliques ; centre, rayon, cercle.
4. Similitude directe s de centre B : $D\to C$.
a) Angle et rapport.
b) Image du triangle BDE par $s\circ s$.
5. $f=r\circ s$ et $g=s\circ r$.
a) Construire $f(B), f(E), g(B), g(A)$.
b) Nature et éléments de f et g.
c) Cercles de diamètres [AG], [BC], [CE], [DB] ont un point commun.""",

    ("C", "math", 2009, "sc", 4): r"""Exercice 4 (6 points)
$f(x)=2x-3+\ln(\tfrac{x^2-2x+2}{x^2})$ sur $\mathbb{R}^+$, courbe (C).
1.a) Domaine et position de (C) et D.
2.a) $\lim_{x\to 0}f(x)$ ; interprétation.
2.b) $f'(x)=\tfrac{2(x-1)}{x}\phi(x)$ où $\phi>0$.
2.c) $\lim_{x\to+\infty}f(x)$ et $\lim_{x\to-\infty}f(x)$.
2.d) Asymptote oblique D.
2.b') Tableau de variation.
2.c') $f(x)=0$ a 3 solutions $\alpha, \beta, \gamma$ ; encadrement d'amplitude $5\times 10^{-1}$.
2.d') Construire (C).
3. Aire S délimitée par (C), $y=2x-3, x=2, x=1+\sqrt{3}$.
a) $\dfrac{2x-4}{x^2-2x+2}=\dfrac{2x-2}{x^2-2x+2}-\dfrac{2}{1+(x-1)^2}$.
b) $A=\int_2^{1+\sqrt{3}}\dfrac{2x-2}{x^2-2x+2}\,dx$.
c) En posant $x=1+\tan t$, calculer $B=\int_2^{1+\sqrt{3}}\dfrac{2}{1+(x-1)^2}\,dx$.
d) Aire S.""",

    # ═══════════════ 2009 SESSION NORMALE (4 exos) ═══════════════
    ("C", "math", 2009, "sn", 1): r"""Exercice 1 (4 points)
$E_\theta : z^2-2(1+i\sin\theta)z+2i\sin\theta=1$ avec $\theta\in[0;2\pi]$.
a) Résoudre $E_{\pi/2}$ et $E_0$.
b) Solutions $z', z''$ de $E_\theta$ avec $\text{Re}(z')\ge\text{Re}(z'')$ si $\cos\theta\ge 0$.
2. $M', M''$ d'affixes $z', z''$.
a) Quand $\theta$ décrit $[0;2\pi]$, lieu $\Gamma$ = cercle.
b) Si $M', M''$ distincts, direction fixe de $(M'M'')$.
c) Construire $\Gamma$ et placer $M', M''$ pour $\theta=\tfrac{\pi}{6}$.
3. $G=\text{bar}\{(M';3),(M'';2)\}$.
a) $z_G$ en fonction de $\theta$.
b) Lieu $\Gamma^*$ = ellipse, équation cartésienne.
c) Centre, sommets, excentricité, construction.""",

    ("C", "math", 2009, "sn", 2): r"""Exercice 2 (4 points)
$f(x)=x^2\ln(x+1)$ sur $]-1;+\infty[$, courbe (C).
1.a) $f'(x)$ ; f strictement croissante.
1.b) Tangente T en $x_0=0$ ; position relative.
1.c) Tableau de variation.
2.a) f bijective ; réciproque g, courbe $(C')$.
2.b) (C) et $(C')$ se coupent en 3 points dont un d'abscisse négative $\alpha$ : $-0,8<\alpha<-0,7$.
2.c) Construire (C) et $(C')$.
3.a) $a, b, c, d$ tels que $\dfrac{x^3}{x+1}=ax^2+bx+c+\dfrac{d}{x+1}$.
3.b) Par IPP, aire entre (C) et $(C')$ pour $\alpha\le x\le 0$.""",

    ("C", "math", 2009, "sn", 3): r"""Exercice 3 (5 points)
$f_n(x)=x^n e^{-x}$ sur $\mathbb{R}$, $n\in\mathbb{N}^*$, courbe $C_n$.
1.a) Variations de $f_1(x)=xe^{-x}$ ; courbe $C_1$.
1.b) Aire entre $C_1$, (Ox), $x=0, x=1$.
2.a) Les courbes $C_n$ passent par deux points fixes.
2.b) Position relative de $C_n$ et $C_{n-1}$ selon la parité.
3. $I_n=\int_0^1 f_n(x)\,dx$.
a) $I_1=1-2e^{-1}$.
b) $I_{n+1}=-e^{-1}+(n+1)I_n$.
c) $0\le I_n\le\tfrac{1}{n+1}$ ; $\lim I_n$.
4. $J_n=\tfrac{e}{n!}I_n$.
a) $J_{n+1}-J_n=\tfrac{-1}{(n+1)!}$.
b) $J_n=e-(\tfrac{1}{0!}+\tfrac{1}{1!}+\cdots+\tfrac{1}{n!})$.
c) $\lim J_n$ et $\lim\sum_{k=0}^n\tfrac{1}{k!}$.""",

    ("C", "math", 2009, "sn", 4): r"""Exercice 4 (7 points)
4 points A, B, C, D deux à deux distincts : $AC=BD, (\vec{AC};\vec{BD})=\tfrac{\pi}{2}\ [2\pi]$. M, N milieux de [AC], [BD]. H intersection. Cercles $\Gamma_1, \Gamma_2, \Gamma_3, \Gamma_4$ de diamètres [AB], [BC], [CD], [DA].
1.a) Unique rotation : $A\to B, C\to D$. Angle ; centre P sur $\Gamma_1, \Gamma_2$.
1.b) Unique rotation : $A\to D, C\to B$. Centre Q sur $\Gamma_2, \Gamma_4$.
1.c) PMQN carré.
2. $P_1, P_2$ diamétralement opposés à P sur $\Gamma_1, \Gamma_3$. $Q_1, Q_2$ diamétralement opposés à Q sur $\Gamma_1, \Gamma_4$.
a) Unique similitude $s_1$ : $A\to P_1, C\to P_2$ ; éléments.
b) $s_1(M)$ ; $P_1, P_2, Q, H$ alignés.
3. $s_2$ similitude directe de centre Q, rapport $\tfrac{1}{\sqrt{2}}$, angle $\tfrac{\pi}{4}$.
a) Images de $Q_1, Q_2, P$.
b) $Q_1, Q_2, P, H$ alignés.
4. $\sigma=s_1\circ s_2$.
a) Nature et éléments.
b) $P_1P_2=Q_1Q_2$ et $(\vec{P_1P_2},\vec{Q_1Q_2})=\tfrac{\pi}{2}\ [2\pi]$.
5. Rotation r : $P_1\to Q_2, Q_1\to P_2, P\to Q$.
a) Centre.
b) M, H, $P_2, Q_3$ cocycliques.
c) Cocyclicités similaires.
d) $P_2A^2+P_2C^2=Q_2A^2+Q_2C^2$.
e) Relations similaires.""",

    # ═══════════════ 2010 SESSION COMPLÉMENTAIRE (4 exos) ═══════════════
    ("C", "math", 2010, "sc", 1): r"""Exercice 1 (4 points)
$G_0(t)=\int_0^t e^x\,dx$ et $G_n(t)=\int_0^t x^n e^x\,dx$ pour $n\ge 1$.
1.a) Existence de $G_n(t)$ ; $G_0(t)$ et $G_1(t)$ en fonction de t.
1.b) Pour $t\ge 0$ : $\tfrac{1}{2}t^2\le G_1(t)\le\tfrac{1}{2}t^2 e^t$.
1.c) Pour $t\le 0$ : $\tfrac{1}{2}t^2 e^t\le G_1(t)\le\tfrac{1}{2}t^2$.
1.d) $\lim_{t\to 0}\dfrac{te^t-e^t+1}{t(e^t-1)}$.
2. $I_n=G_n(1)=\int_0^1 x^n e^x\,dx$.
a) Par IPP, $G_n(t)=t^n e^t-nG_{n-1}(t)$ ; $I_n$ en fonction de $I_{n-1}$.
b) $(I_n)$ décroissante et positive.
c) Encadrement et $\lim I_n$.""",

    ("C", "math", 2010, "sc", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(4+6i)z^2+(-6+16i)z+12-4i$.
1.a) $P(1+i)$.
1.b) $a, b$ tels que $P(z)=(z-1-i)(z^2+az+b)$.
1.c) Solutions de $P(z)=0$.
2.a) Points A, B, C avec $|z_A|\le|z_B|\le|z_C|$ ; nature de ABC.
2.b) Unique similitude directe s de centre A : $C\to B$.
2.c) Expression complexe ; rapport et angle.
3. f : $z'=\tfrac{1-i}{2}z+i$. $f^1=f, f^n=f\circ f^{n-1}$. $M_0=C, M_n=f^n(M_0)$.
a) Reconnaître f et éléments.
b) Nature du triangle $AM_nM_{n+1}$.
c) $S_n=M_0M_1+\cdots+M_nM_{n+1}$.
d) $\lim S_n$ et interprétation.""",

    ("C", "math", 2010, "sc", 3): r"""Exercice 3 (5 points)
Triangle équilatéral direct ABC de côté a. I, J, K milieux de [AB], [BC], [CA].
1. Figure.
2.a) Unique rotation $r_1$ : $I\to C, B\to J$.
2.b) Angle et centre.
3. t translation de vecteur $\vec{CK}$. $r_2=t\circ r_1$.
a) Nature de $r_2$ ; $r_2(I), r_2(B)$ ; caractériser.
b) Droite $\Delta$ telle que $s_\Delta=r_2$ ; autre décomposition.
4. Similitudes $s_1, s_2$ de centres A, C : $s_1(B)=K, s_2(K)=B$.
a) Angle et rapport de chacune.
b) $f=s_2\circ s_1$ ; nature et caractérisation.
5. M variable. $r_1(M)=M_1, r_2(M)=M_2$.
a) Si M distinct de J et $\Omega$ : $(\vec{M\Omega},\vec{MJ})=(\vec{MM_1},\vec{MM_2})\ [2\pi]$.
b) Lieu de M tels que $M, M_1, M_2$ alignés.
c) $M_1M_2$ constant et $(M_1M_2)$ direction fixe.""",

    ("C", "math", 2010, "sc", 4): r"""Exercice 4 (7 points)
I. $g(x)=\dfrac{2x^2+3x+2}{x+1}$.
1. $g(x)>0$ pour $x>-1$.
2. $a, b, c$ tels que $g(x)=ax+b+\dfrac{c}{x+1}$.
3. Primitive G sur $]-1,+\infty[$ avec $G(0)=1$.

II. $f(x)=x^2+x+1+\ln(x+1)$ sur $]-1,+\infty[$, courbe (C).
1.a) Limites en $-1^+$, $+\infty$, $\tfrac{f(x)}{x}$ en $+\infty$.
1.b) Tableau de variation.
1.c) Interprétation graphique.
2.a) Bijection sur J.
2.b) $f(x)=0$ a une unique solution $\alpha$ ; $-0,53<\alpha<-0,52$.
3.a) $f(x)\ge x+1$ pour $x>0$ ; interprétation.
3.b) (C) et $(C')$ se coupent en un unique point d'abscisse $\beta$ : $-0,81<\beta<-0,80$.
3.c) $(f^{-1})'(\beta)=\dfrac{\beta+1}{2\beta^2+3\beta+2}$.
4.a) Points de (C) avec tangentes parallèles à $y=2x$.
4.b) Discussion selon k de $x^2-x+1+\ln(x+1)=k$.
4.c) Construire (C) et $(C')$.
5. Aire A entre (C), $(C')$ et axes.
a) $A=\alpha^2+\int_0^\alpha(2x^2+2+2\ln(x+1))\,dx$.
b) Calculer A en fonction de $\alpha$ (IPP).""",

    # ═══════════════ 2010 SESSION NORMALE (4 exos) ═══════════════
    ("C", "math", 2010, "sn", 1): r"""Exercice 1 (3 points)
$f(x)=e^x-x-1$ sur $\mathbb{R}$.
1.a) Tableau de variation.
1.b) $e^x\ge x+1$.
2.a) $\ln(1+x)\le x$ pour $x>-1$.
2.b) $\ln(1-x)\le -x$ pour $x<1$.
3. $S_n=\sum_{k=1}^n\tfrac{1}{k}$.
a) $S_n\ge\ln(n+1)$.
b) $\lim S_n=+\infty$.
4. $U_n=S_n-\ln n$.
a) $U_n-U_{n-1}=\tfrac{1}{n}+\ln(1-\tfrac{1}{n})$ ; sens de variation.
b) $(U_n)$ converge vers $\gamma$ avec $0<\gamma<1$ (constante d'Euler).""",

    ("C", "math", 2010, "sn", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(6\cos\theta+i)z^2+(4+5\cos^2\theta+6i\cos\theta)z-(4+5\cos^2\theta)i$, $\theta\in[0;2\pi]$.
1.a) Vérifier $z_0=i$ solution ; $a, b$ tels que $P(z)=(z-i)(z^2+az+b)$.
1.b) Solutions $z_1, z_2$ avec $\text{Im}(z_1)\ge 0$ si $\sin\theta\ge 0$.
2. $M_0, M_1, M_2$ d'affixes $z_0, z_1, z_2$. G centre de gravité.
a) $z_G=2\cos\theta+\tfrac{1}{3}i$.
b) Lieu de G.
3.a) Lieu $\Gamma'$ des $M_1, M_2$ = ellipse, équation cartésienne.
3.b) Centre, sommets, excentricité, construction.""",

    ("C", "math", 2010, "sn", 3): r"""Exercice 3 (5 points)
$u(x)=x-2+\ln x$ sur $]0;+\infty[$.
1.a) Tableau de variation.
1.b) Bijection sur intervalle.
1.c) $u(x)=0$ admet une unique solution $\alpha$ ; $1\le\alpha\le 2$.
1.d) Signe de $u(x)$.
2. $f(x)=-\tfrac{3}{4}x^2+x-\tfrac{1}{2}x^2\ln x$ pour $x>0$ et $f(0)=0$. Courbe (C).
a) Continuité à droite en 0.
b) Dérivabilité à droite en 0 ; $f_d'(0)$.
c) $f'(x)=xu(\tfrac{1}{x})$ ; signe.
d) Tableau de variation ; $f(x)=0$ a une solution $\beta$ ; $1\le\beta\le 2$.
e) Tracer (C).
3. $I_n=\int_{1/n}^\beta f(x)\,dx$.
a) Par IPP, $I_n$ en fonction de $\beta$ et n.
b) $\lim I_n$ et interprétation.""",

    ("C", "math", 2010, "sn", 4): r"""Exercice 4 (8 points)
Carré direct ABCD de côté a. I, J, K, L milieux des côtés. E symétrique de C par D. F symétrique de B par A.
1. Figure.
2.a) Unique rotation r : $D\to F, C\to E$ ; angle et centre.
2.b) Droites $\Delta_1, \Delta_2$ tels que $r=s_{\Delta_1}\circ s_{(AC)}=s_{(AB)}\circ s_{\Delta_2}$.
2.c) Nature de $\sigma=s_{(AB)}\circ s_{(AD)}\circ s_{(AC)}$.
3.a) Unique similitude $s_1$ : $D\to L, C\to D$ ; angle et rapport.
3.b) Centre R sur cercles de diamètres [DL] et [CD] = intersection de (CL) et (DI).
3.c) Homothétie h de centre C rapport $\tfrac{1}{2}$. $f=h\circ r$ ; nature, $f(D), f(C)$.
3.d) Forme réduite de $s_1$.
4. Similitude directe $s_2$ : $F\to B, B\to C$.
a) Angle et rapport.
b) Centre Q = intersection de (CL) et (BK).
5. P = (AJ)$\cap$(BK), S = (AJ)$\cap$(DI).
a) $Q=\text{bar}\{(A,-1);(B,2);(C,1);(D,3)\}$.
b) Expressions similaires pour P, R, S.
c) PQRS carré ; aire en fonction de a.
6. $\Gamma$ similitudes directes de centre O transformant ABCD en PQRS.
a) Même rapport ; calculer.
b) Pour g d'angle $\theta\in]0,\tfrac{\pi}{2}[$, $\sin\theta, \cos\theta$ exacts.
c) Autres angles possibles.""",
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
        print("\nMises à jour (premiers 20) :")
        for label, eid, ol, nl in updated[:20]:
            print(f"  {label:25}  → {eid:45}  {ol} → {nl} chars")
        if len(updated) > 20:
            print(f"  ... + {len(updated)-20} autres")
    if skipped_missing:
        print("\nIntrouvables :")
        for label in skipped_missing:
            print(f"  {label}")
    if skipped_filled:
        print("\nDéjà remplis :")
        for label, eid, ln in skipped_filled[:10]:
            print(f"  {label:25}  → {eid:45}  ({ln} chars)")
        if len(skipped_filled) > 10:
            print(f"  ... + {len(skipped_filled)-10} autres")

    if args.dry_run:
        print("\n(--dry-run : aucune écriture)")
        return 0
    if not updated:
        print("\nRien à écrire.")
        return 0

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(p, BACKUP_DIR / f"json_bac-pre-fill-c-math-{stamp}.json")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"\n→ {p} mis à jour ({len(updated)} entrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
