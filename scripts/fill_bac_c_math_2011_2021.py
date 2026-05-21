"""Remplit 87 énoncés Bac C · Math · 2011-2021 (Gemini, à valider).

Source : extraction Gemini synthétique, qualité ~60%. Pas de validated_by_admin.
Tous les slots `bac-c-YYYY-XX-math-exN` sont des squelettes vides.
"""
from __future__ import annotations

import argparse, json, shutil, sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "json_bac.json"
BACKUP_DIR = ROOT / "json_backups"


EXOS: dict[tuple[str, str, int, str, int], str] = {

    # ═══════════════ 2011 SC ═══════════════
    ("C", "math", 2011, "sc", 1): r"""Exercice 1 (4 points)
Dans $\mathbb{C}$ : $P(z)=z^3-(1-2i)z^2+(10-8i)z-4+8i$.
1.a) Calculer $P(2)$.
1.b) Résoudre $P(z)=0$.
2. Points A, B, C images des solutions avec $|z_A|<|z_B|<|z_C|$. Montrer que ABC est rectangle isocèle et que OACB est un parallélogramme.
3. Transformation s : $z'=\dfrac{1+i}{2}z-i$.
3.a) s est une similitude directe.
3.b) Éléments caractéristiques.
3.c) $s(C)=B$.""",
    ("C", "math", 2011, "sc", 2): r"""Exercice 2 (4 points)
$g(x)=-x^3-x^2-2x+2$ sur $\mathbb{R}$.
a) Tableau de variations de g.
b) g bijection de $\mathbb{R}$ sur $\mathbb{R}$.
c) $g(x)=0$ a une unique solution $\alpha$ avec $0{,}6\le\alpha\le 0{,}7$.
2. $f(x)=\dfrac{2xe^{-x}}{x^2+2}$. Calculer $f'(x)$ et vérifier $f'(x)=\dfrac{2g(x)e^{-x}}{(x^2+2)^2}$.
b) Tableau de variation de f et tracé.
3. $U_n=\int_n^{n+1}f(t)\,dt$.
a) $0\le U_n\le 1$ ; $\lim U_n$.
b) $n_0$ tel que $0\le U_n\le 10^{-3}$ pour $n\ge n_0$.""",
    ("C", "math", 2011, "sc", 3): r"""Exercice 3 (5,5 points)
Carré direct ABCD de centre O. E, F, G, H milieux de [AB], [BC], [CD], [DA].
1.a) Unique rotation r : $D\to H, H\to O$. Figure.
1.b) Centre I et angle.
1.c) $r(A)=F$ ; construire $B', C'$.
3. Homothétie h de centre D et rapport $\tfrac{1}{2}$. $s=r\circ h$.
3.a) s similitude directe ; rapport et angle.
3.b) Image du carré ABCD par s.
4. $\Omega$ centre de s.
4.a) $\Omega$ sur les cercles de diamètres [AC], [BG], [CD], [DH].
4.b) Cercles $\Gamma, \Gamma'$ passant par $\Omega$ de centres A, O. T autre intersection. $s(\Gamma)=\Gamma'$ ; $\Omega, A, O, T$ cocycliques.
4.c) Pour $M\in\Gamma\setminus\{\Omega,T\}$, $s(M)=M'$. M, M', T alignés.
4.d) $A', O'$ diamétralement opposés à $\Omega$. J, K milieux de [MM'], [OO']. Nature de $\Omega JK$ ; lieu de J.""",
    ("C", "math", 2011, "sc", 4): r"""Exercice 4 (6,5 points)
$f(x)=x\ln(x+1)$ sur $]-1;+\infty[$, courbe (C).
1.a) Limites en $-1^+, +\infty, \tfrac{f(x)}{x}$ en $+\infty$.
1.b) f décroissante sur $]-1,0]$ et croissante sur $[0;+\infty[$ ; tracé.
2.a) $a, b, c$ tels que $\dfrac{x^2}{x+1}=ax+b+\dfrac{c}{x+1}$.
2.b) Par IPP, aire A entre (C), (Ox), $x=0, x=1$.
3. $U_n=\int_0^1 x^n\ln(x+1)\,dx$.
a) Justifier l'existence.
b) $U_1$ et interprétation.
c) $(U_n)$ décroissante et convergente.
d) $0\le U_n\le\tfrac{\ln 2}{n+1}$ ; $\lim U_n$.
4. $V_n=\int_0^1\dfrac{x^{n+1}}{x+1}\,dx$.
a) $U_n=\tfrac{\ln 2}{n+1}-\tfrac{1}{n+1}V_n$.
b) Encadrement de $V_n$ ; $\lim V_n$.
c) $V_n=(-1)^n(1-\tfrac{1}{2}+\cdots+\tfrac{(-1)^n}{n+1}-\ln 2)$ ; $\lim\sum=\ln 2$.""",

    # ═══════════════ 2012 SN ═══════════════
    ("C", "math", 2012, "sn", 1): r"""Exercice 1 (3 points)
$f(x)=e^x\ln(e^x+1)$ sur $\mathbb{R}$, courbe (C).
1. Limites en $\pm\infty$, $\tfrac{f(x)}{x}$ ; interprétations.
2.a) Tableau de variation.
2.b) Bijection sur intervalle J.
2.c) Tracer (C).
3. $I=\int_0^1 f(x)\,dx$, deux méthodes.
Méthode a : $a, b, c$ tels que $f'(x)=f(x)+ae^x+b+\tfrac{ce^{-x}}{1+e^{-x}}$ ; calcul de I.
Méthode b : $t=e^x+1$, IPP.""",
    ("C", "math", 2012, "sn", 2): r"""Exercice 2 (3 points)
Espace $(O;\vec{i},\vec{j},\vec{k})$. $A(2;1;3), B(3;2;1), C(4;1;4), D(5;3;-2), E(6;-2;-4)$.
1.a) $\vec{AB}, \vec{AC}, \vec{DE}$ ; $\vec{DE}\perp$ plan (ABC).
1.b) Équation de (ABC).
1.c) Représentation paramétrique de (DE).
1.d) F projeté de D sur (ABC) ; $\vec{EF}=k\vec{DF}$.
2.a) Volume V du tétraèdre ABCD.
2.b) $\Gamma_1:11MD^2-ME^2=-30$ et $\Gamma_2:MD^2-ME^2=-36$.""",
    ("C", "math", 2012, "sn", 3): r"""Exercice 3 (4 points)
Dans $\mathbb{C}$ : $E_\theta:z^2-(6\cos\theta)z+4+5\cos^2\theta=0$, $\theta\in[0;2\pi[$.
1.a) Résoudre $E_\theta$ ; $z_1, z_2$ avec $\text{Im}(z_1)\ge 0$ si $\theta\in[0;\pi[$.
1.b) Cas solutions doubles ($A_1, A_2$ avec $\text{Re}(z_1)\ge 0$) ; cas imaginaires pures ($B_1, B_2$).
2.a) Lieu $\Gamma$ des $M_1, M_2$ quand $\theta$ décrit $[0;2\pi[$.
2.b) Nature et éléments ; construction.
3. f : M(z) → M'(z'), barycentre de $\{(A_1,-4);(B_1,2);(M,3)\}$.
3.a) Expression de $z'$ ; reconnaître f.
3.b) Équation de $\Gamma'=f(\Gamma)$ ; éléments.""",
    ("C", "math", 2012, "sn", 4): r"""Exercice 4 (4 points)
But : $\lim U_n$ où $U_n=\dfrac{\sqrt[n]{n!}}{n}$, $n\ge 2$. $f(x)=x-\ln x$ sur $]0;+\infty[$.
1. Tableau de variation de f.
2. $I(\lambda)=\int_\lambda^1 f(x)\,dx$, $\lambda\in\mathbb{R}^*$.
a) Par IPP, $\int_\lambda^1\ln x\,dx$.
b) En déduire $I(\lambda)$ et $\lim_{\lambda\to 0^+}I(\lambda)$.
3. $S_n=\tfrac{1}{n}\sum_{k=1}^n f(\tfrac{k}{n})$.
a) $\tfrac{1}{n}f(\tfrac{k+1}{n})\le\int_{k/n}^{(k+1)/n}f\le\tfrac{1}{n}f(\tfrac{k}{n})$.
b) $I(\tfrac{1}{n})\le S_n\le I(\tfrac{1}{n})+\tfrac{1}{n}f(\tfrac{1}{n})$ ; encadrement de $I(\tfrac{1}{n})$.
c) $\lim S_n=\tfrac{3}{2}$.
4.a) $\sum\ln(\tfrac{k}{n})=\ln(\tfrac{n!}{n^n})$ et $\sum k=\tfrac{n(n+1)}{2}$.
4.b) $S_n=\tfrac{n^2+n}{2n^2}-\ln U_n$.
4.c) $\lim U_n=\tfrac{1}{e}$.""",
    ("C", "math", 2012, "sn", 5): r"""Exercice 5 (6 points)
Triangle équilatéral direct ABC de côté a, centre G. I, J, K milieux de [BC], [CA], [AB]. E symétrique de K par I.
1. Figure.
2.a) Unique rotation $r_1$ : $B\to I, J\to A$.
2.b) Éléments caractéristiques.
3. $t$ translation de vecteur $\vec{AJ}$. $r_2=t\circ r_1$ et $f=s_{(JC)}\circ s_{(JE)}\circ s_{(KE)}$.
3.a) $r_2(J)$ et caractériser $r_2$.
3.b) $\Delta_1, \Delta_2$ tels que $r_1=s_{(KC)}\circ s_{\Delta_1}$ et $r_2=s_{(JC)}\circ s_{\Delta_2}$ ; $f=t_{\vec{AJ}}\circ s_{(KC)}$.
3.c) Image du triangle BIK par f ; symétrie glissante et forme réduite.
4.a) Unique similitude directe s : $E\to I, C\to G$.
4.b) Angle et rapport.
4.c) Centre sur cercles circonscrits aux triangles BCG et BEI.
5. M variable sur $\Gamma$ cercle de diamètre [BC]. $s(M)=M'$.
a) Lieu $\Gamma'$.
b) (MM') passe par K pour $M\ne B$.
c) Programme de construction et placer M, M'.
6. $M_n=s^n(E)$ avec $M_0=E, M_1=s(M_0)$.
a) Placer $B, M_0, M_1, M_2, M_3$.
b) $S_n=\sum M_kM_{k+1}$ en fonction de n et a.
c) $\lim S_n$ et interprétation.
d) $M_{1960}\in(BM_4)$ et $M_{2012}\in(BG)$.""",

    # ═══════════════ 2013 SC ═══════════════
    ("C", "math", 2013, "sc", 1): r"""Exercice 1 (3 points)
$f_n(x)=x^3+2(n+2)x+1$ sur $\mathbb{R}$, $n\in\mathbb{N}$, courbe $C_n$.
1.a) Tableau de variation de $f_0(x)=x^3+4x+1$.
1.b) $f_0(x)=0$ admet une unique solution $U_0\in]-1,0[$.
1.c) Tracer $C_0$.
2.a) Toutes les courbes $C_n$ passent par un point fixe A.
2.b) Positions relatives de $C_n$ et $C_{n+1}$.
3.a) $f_n(x)=0$ admet une unique solution $U_n\in]-1,0[$.
3.b) $(U_n)$ croissante donc convergente.""",
    ("C", "math", 2013, "sc", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(4+6i)z^2+(-5+18i)z+18-12i$.
1.a) Calculer $P(2), P(3i)$.
1.b) Solutions $Z_1, Z_2, Z_3$ avec $|z_1|\le|z_2|\le|z_3|$.
2. A, B, C d'affixes $Z_1, Z_2, Z_3$. G barycentre de $\{(A,1),(B,-3),(C,4)\}$. $\varphi_1(M)=MA^2-3MB^2+4MC^2$ et $\varphi_2(M)=4MA^2-2MB^2-2MC^2$.
2.a) $z_G=5+\tfrac{3}{2}i$.
2.b) Formes réduites de $\varphi_1, \varphi_2$.
2.c) $\Gamma_1:\varphi_1(M)=-3$ et $\Gamma_2:\varphi_2(M)=44$.""",
    ("C", "math", 2013, "sc", 3): r"""Exercice 3 (4 points)
$f(x)=\dfrac{2\ln x}{x^2-\ln x}$ pour $x>0$, $f(0)=-2$ sur $[0;+\infty[$.
1.a) Continuité en $0^+$.
1.b) Dérivabilité à droite en 0 ; interprétation.
1.c) $\lim_{x\to+\infty}f(x)=0$ ; interprétation.
2.a) Tableau de variation.
2.b) Tangente au point d'abscisse 1.
2.c) Tracer la courbe.
3. $g(t)=tf(t)$. Pour $x\ge 1$, $F(x)=\int_1^x g(t)\,dt$.
a) F dérivable, $F'(x)$ ; F croissante.
b) $g(t)\ge\tfrac{2\ln t}{t}$ ; $\lim F=+\infty$.
c) Tableau de variation de F.""",
    ("C", "math", 2013, "sc", 4): r"""Exercice 4 (5 points)
Losange direct ABCD de centre O et de côté a avec $(\vec{BC},\vec{BA})=\tfrac{\pi}{4}\ [2\pi]$. OEFD carré direct.
1. Figure ((AC) horizontale).
2.a) Unique rotation r : $A\to B, D\to A$.
2.b) Angle et centre.
3.a) Unique similitude directe s : $B\to D, D\to F$.
3.b) Rapport et angle.
3.c) H projeté orthogonal de D sur (BF) ; images de (BH) et (DH) par s ; H centre de s.
3.d) Images des sommets de OEFD par s.
4. Repère $(O;\vec{OE},\vec{OD})$.
a) Coordonnées de E, D, B, F.
b) Expression complexe de s.
c) Retrouver rapport, angle ; coordonnées de H.""",
    ("C", "math", 2013, "sc", 5): r"""Exercice 5 (4 points)
$f(x)=\dfrac{e^x-1}{e^x+1}$, courbe C.
1.a) $f(x)=-1+\tfrac{2e^x}{e^x+1}=1-\tfrac{2}{e^x+1}$.
1.b) Limites en $\pm\infty$.
2.a) Tableau de variation.
2.b) Tracer C.
2.c) Aire entre C, (Ox), (Oy), $x=\ln a$ ($a>1$).
3. $I_n=\int_0^{\ln a}(f(t))^n\,dt$.
a) $I_1=2\ln(\tfrac{a+1}{2\sqrt{a}})$ ; $\lim I_n$.
b) $f^2(x)=1-2f'(x)$ ; $I_2$.
c) $0\le I_n\le(\tfrac{a-1}{a+1})^n\ln a$.
d) $I_n-I_{n+2}=\tfrac{2}{n+1}(\tfrac{a-1}{a+1})^{n+1}$.
4. $S_n(a)=\sum_{k=1}^n\tfrac{1}{k}(\tfrac{a-1}{a+1})^k$.
a) $S_n(a)$ en fonction des $I_n$ ; $\lim S_n(a)$.
b) $T_n=\sum\tfrac{1}{k}(\tfrac{9}{11})^k$ ; $\lim T_n$.""",

    # ═══════════════ 2013 SN ═══════════════
    ("C", "math", 2013, "sn", 1): r"""Exercice 1 (3 points)
Équation (E) : $25x-9y=5$.
1.a) Algorithme d'Euclide pour u, v tels que $25u+9v=1$ ; solution particulière $(x_0, y_0)$ de (E).
1.b) Ensemble des solutions.
2. d = PGCD(x, y).
a) Valeurs possibles de d.
b) Solutions avec x et y premiers entre eux.
c) Peut-on trouver (x,y) tel que $(x^2, y^2)$ soit solution de (E) ?""",
    ("C", "math", 2013, "sn", 2): r"""Exercice 2 (3,5 points)
$P(z)=z^3-(9-i)z^2+(28-5i)z-32+4i$.
1.a) $P(4)$ ; $a, b$ tels que $P(z)=(z-4)(z^2+az+b)$.
1.b) Solutions.
2. A, B, C avec $z_A=4$, $\text{Im}(z_B)>0$, $\text{Im}(z_C)<0$.
a) Expression complexe de la similitude directe s de centre C : $A\to B$.
b) Rapport et angle.
3. $Q(z)=z^2-(5-i)z+8-i$ ; $\Gamma=\{M:Q(z)\text{ imaginaire pur}\}$.
a) Équation cartésienne ; hyperbole de centre $\Omega(\tfrac{5}{2},-\tfrac{1}{2})$.
b) Sommets, asymptotes, construction.""",
    ("C", "math", 2013, "sn", 3): r"""Exercice 3 (4 points)
$f(x)=(3-x)e^x$ sur $\mathbb{R}$, courbe (C).
a) Limites en $\pm\infty$ et $\tfrac{f(x)}{x}$.
b) Tableau de variation.
c) Tracer (C).
d) f solution de $y'-y=-e^x$ ; aire entre (C), (Ox), $x=0, x=3$.
2. $U_n=\dfrac{3^n}{n!}$.
a) $0\le\tfrac{U_{n+1}}{U_n}\le\tfrac{3}{4}$ pour $n\ge 3$ ; $U_n\le\tfrac{9}{2}(\tfrac{3}{4})^{n-3}$ ; $\lim U_n=0$.
3. $I_n=\tfrac{1}{n!}\int_0^3 (3-x)^n e^x\,dx$ et $S_n=\sum_{k=0}^n\tfrac{3^k}{k!}$.
a) $I_1=e^3-4$.
b) $\lim I_n=0$.
c) Par IPP, $I_{n+1}=I_n-U_{n+1}$.
d) Récurrence : $e^3=S_n+I_n$ ; $\lim S_n=e^3$.""",
    ("C", "math", 2013, "sn", 4): r"""Exercice 4 (4,5 points)
$g(x)=1+x^3-3x^3\ln x$ pour $x>0$, $g(0)=1$.
a) Continuité en $0^+$ ; $\lim_{x\to+\infty}g(x)=-\infty$.
b) Tableau de variation.
c) Unique solution $\alpha\in]1,2[$ ; signe de $g(x)$.
2. $f(x)=\dfrac{\ln x}{1+x^3}$ sur $]0;+\infty[$.
a) Limites en $0^+, +\infty$.
b) $f'(x)=\tfrac{g(x)}{x(1+x^3)^2}$ ; tableau de variation.
3. $F(x)=\int_1^x f(t)\,dt$ pour $x>1$.
a) F dérivable ; $F'(x)$ ; sens de variation.
b) $\dfrac{\ln t}{(1+t)^3}\le f(t)\le\dfrac{\ln t}{t^3}$.
c) Par IPP, $\int_1^x\tfrac{\ln t}{t^3}\,dt$.
d) $a, b, c$ tels que $\dfrac{1}{t(1+t)^2}=\tfrac{a}{t}+\tfrac{b}{1+t}+\tfrac{c}{(1+t)^2}$.
4.a) Encadrement de F(x).
4.b) $-\tfrac{1}{4}+\tfrac{1}{2}\ln 2\le l\le\tfrac{1}{4}$ où $l=\lim F$.
4.c) Tracer allure de F.""",
    ("C", "math", 2013, "sn", 5): r"""Exercice 5 (4 points)
Carré direct ABCD de centre O et de côté a. I, J, K, L milieux des côtés.
1.a) Figure.
1.b) Unique rotation r : $C\to O, K\to I$.
1.c) Angle et centre.
2. $f=S_{(IJ)}\circ S_{(JO)}\circ S_{(OK)}$.
a) $f=r\circ S_{(OK)}$ ; $f(D), f(K), f(O)$.
b) Nature et forme réduite.
3.a) Unique similitude directe $s_1$ : $B\to I, L\to A$ ; rapport $\lambda_1$.
3.b) Angle $\alpha$ avec $\cos\alpha=\tfrac{2\sqrt{5}}{5}$.
3.c) P centre de $s_1$. E symétrique de C par B. P sur cercles BEI et BAL ; préciser P.
3.d) $(\vec{PI},\vec{PA})=\tfrac{\pi}{2}\ [2\pi]$ ; A, P, E alignés.
4. $S_2$ similitude directe de centre B : $C\to L$ ; angle $\beta$. $g=S_1\circ S_2$.
a) g similitude directe ; $g(B), g(C)$.
b) $\alpha+\beta=\tfrac{\pi}{2}\ [2\pi]$ ; centre Q sur deux cercles.
c) $g(O)=P$ ; image du carré ABCD par g.""",

    # ═══════════════ 2014 SC ═══════════════
    ("C", "math", 2014, "sc", 1): r"""Exercice 1 (3 points)
(E) : $11x+9y=19$.
1.a) Vérifier que $(-4,7)$ est solution.
1.b) Ensemble des solutions.
2. (Série C) X variable aléatoire à 3 valeurs $-4, 7, 8$ avec $p_1=\tfrac{x-4}{9}, p_2=\tfrac{2x-y-8}{9}, p_3=\tfrac{8x+10y+2}{9}$.
a) Unique couple (x, y).
b) $E(X)=6$.
c) Variance.
2.bis (TMGM) Équation $(E'):(11-9i)z+(11+9i)\bar{z}=38$.
a) Infinité de solutions ; lieu A des $M(x,y)$.
b) Points de A à coordonnées entières.""",
    ("C", "math", 2014, "sc", 2): r"""Exercice 2 (4 points)
$P(z)=z^3+(2-2i)z^2+(-2-8i)z-8+4i$.
1.a) $P(2i)$.
1.b) Résoudre $P(z)=0$.
2. Transformation f : $z'=\tfrac{1}{3}iz+\tfrac{2}{3}+2i$.
a) Similitude directe ; centre A, rapport, angle.
b) $z_C=f(z_B)$ avec $B(-3,-1)$ ; ABC rectangle.
c) G barycentre de $\{(A,-4);(B,1);(C,6)\}$ ; ABCG cocycliques.
3. $\Gamma_1:-4MA^2+MB^2+6MC^2=30$ et $\Gamma_2:MB^2-MC^2=16$.""",
    ("C", "math", 2014, "sc", 3): r"""Exercice 3 (4 points)
$g(x)=-x^2-\ln x$ sur $]0;+\infty[$.
a) Tableau de variation.
b) Unique solution $\alpha$ ; $\tfrac{1}{e}<\alpha<1$ ; signe de g.
2. $f(x)=-x+1+\tfrac{1}{x}(1+\ln x)$.
a) $\lim_{0^+}f=-\infty$ ; interprétation.
b) $\lim(f(x)-(1-x))$ en $+\infty$.
c) $f'(x)=\tfrac{g(x)}{x^2}$ ; tableau de variation.
d) Construire la courbe.
3. $f_m(x)=-x+1+\tfrac{m^2}{x}(1+\ln x-\ln m)$, $m>0$.
a) Asymptotes communes ; point d'intersection G.
b) $(C_m)$ image de $(C_1)$ par homothétie de centre G ; rapport.
c) Tableau de variation de $f_m$.""",
    ("C", "math", 2014, "sc", 4): r"""Exercice 4 (5 points)
Triangle équilatéral direct ABC de centre O et de côté a. I, J, K milieux de [BC], [CA], [AB].
1.a) Figure.
1.b) Unique rotation $r_1$ : $A\to B, C\to A$.
1.c) Angle et centre.
1.d) Rotation $r_2$ de centre A et angle $\tfrac{\pi}{3}$ ; $r_1\circ r_2(B)$ ; caractériser $r_1\circ r_2$.
2. D, E symétriques de I, J par K.
a) Unique antidéplacement g : $A\to K, J\to E$.
b) g symétrie glissante ; $g(D)$ ; forme réduite.
4.a) Unique similitude directe $S_1$ : $B\to I, C\to J$.
4.b) Rapport et angle ; O centre.
5. $M\in[BC], N\in[CA], P\in[AB]$ avec $BM=CN=AP=x$.
a) MNP équilatéral de centre O.
b) H milieu de [MN] ; lieu de H.
c) Unique similitude directe $S_2$ : $(A,B,C)\to(P,M,N)$ ; centre.
d) Position de M minimisant $\tfrac{OM}{OB}$ ; aire minimale de MNP.""",
    ("C", "math", 2014, "sc", 5): r"""Exercice 5 (4 points)
$f(x)=\dfrac{e^x}{e^x-x}$ sur $\mathbb{R}$, courbe C.
1.a) $\lim_{+\infty}f=1$ ; interprétation.
1.b) $\lim_{-\infty}f$ ; interprétation.
1.c) Tableau de variation ; courbe.
2. A aire entre courbe, (Ox), $x=0, x=1$. $1\le A\le\tfrac{e}{e-1}$.
3. $I_n=\int_0^1 x^n e^{-nx}\,dx$, $I_0=1$.
a) $I_1=1-2e^{-1}$.
b) $0\le I_n\le\tfrac{1}{n+1}$ ; $\lim I_n=0$.
4. $S_n=I_0+\cdots+I_n$.
a) $S_n=\int_0^1\dfrac{1-(xe^{-x})^{n+1}}{1-xe^{-x}}\,dx$.
b) $A-S_n=\int_0^1\dfrac{(xe^{-x})^{n+1}}{1-xe^{-x}}\,dx$.
c) $0\le A-S_n\le\tfrac{2}{n+2}$ ; $\lim S_n=A$.
d) $n_0$ tel que A approche $S_n$ à $10^{-2}$ près.""",

    # ═══════════════ 2014 SN ═══════════════
    ("C", "math", 2014, "sn", 1): r"""Exercice 1 (4 points)
$P(z)=z^3+(1-2i)z^2+(1-2i)z-2i$.
1. $P(2i)$ et solutions $z_0, z_1, z_2$ avec $\text{Im}(z_0)\ge\text{Im}(z_1)\ge\text{Im}(z_2)$.
2. A, B, C d'affixes $z_0, z_1, z_2$. $z'=f(z)=\dfrac{1}{z^2+z+1}$.
a) Équation cartésienne de (BC) : $2x+1=0$.
b) Si M décrit (BC) privée de B, C, alors M' sur l'axe des abscisses.
3.a) Si $|z|=1$ alors $f(z)=\dfrac{\bar{z}}{1+z+\bar{z}}$.
3.b) Si $z=e^{i\theta}$ avec $\theta\in[-\pi;\pi]\setminus\{\pm\tfrac{2\pi}{3}\}$, $f(z)=\dfrac{\cos\theta-i\sin\theta}{1+2\cos\theta}$.
4.a) Si M décrit cercle unité privé de A, C, M' sur courbe $\Gamma:x^2+y^2=(2x-1)^2$.
4.b) $\Gamma$ hyperbole ; centre, sommets, excentricité, construction.""",
    ("C", "math", 2014, "sn", 2): r"""Exercice 2 (5 points)
$f(x)=xe^x$ sur $\mathbb{R}$, courbe (C).
1.a) Tableau de variation.
1.b) Tracer (C).
1.c) f solution de $y''-2y'+y=0$.
1.d) Aire entre (C), (Ox), $x=0, x=1$.
2. $I_n=(-1)^n\int_0^1 x^n e^x\,dx$.
a) $I_1=-1$.
b) $\tfrac{1}{n+1}\le|I_n|\le\tfrac{e}{n+1}$ ; $\lim I_n=0$.
c) Par IPP, $I_{n+1}=(-1)^{n+1}e+(n+1)I_n$.
d) $J=\int_0^1\dfrac{(x^3+4x^2-3x-6)e^x}{x+1}\,dx$ sous la forme $ae+b$.""",
    ("C", "math", 2014, "sn", 3): r"""Exercice 3 (5 points)
$f(x)=x\ln(1+\tfrac{1}{x})$ pour $x>0$, $f(0)=0$.
a) Continuité à droite en 0 ($f(x)=x\ln(x+1)-x\ln x$).
b) Dérivabilité à droite en 0 ; interprétation.
c) $\lim_{+\infty}f=1$ (poser $t=\tfrac{1}{x}$) ; interprétation.
2.a) $f''(x)=\dfrac{-1}{x(x+1)^2}$ ; signe de $f'$.
2.b) Tableau de variation.
2.c) Tracer la courbe.
3. $f_n(x)=x^n\ln(1+\tfrac{1}{x})$ pour $x>0$, $f_n(0)=0$ ; $A_n=\int_0^1 f_n(x)\,dx$.
a) Existence de $(A_n)$.
b) $0\le x^{n-1}f(x)\le x^{n-1}$.
c) $0\le A_n\le\tfrac{1}{n}$ ; $\lim A_n=0$.
4. $I_n(\alpha)=\int_\alpha^1 x^n\ln x\,dx$, $I_n=\lim_{\alpha\to 0^+}I_n(\alpha)$, $J_n=\int_0^1 x^n\ln(x+1)\,dx$.
a) Par IPP, $I_n(\alpha)$ en fonction de $\alpha, n$.
b) $\lim I_n(\alpha)=\dfrac{-1}{(n+1)^2}$.
c) Par IPP, $J_{n+1}=\dfrac{2\ln 2}{n+2}-\dfrac{1}{(n+2)^2}-\dfrac{n+1}{n+2}J_n$.""",
    ("C", "math", 2014, "sn", 4): r"""Exercice 4 (6 points)
Partie A — Carré direct ABCD de centre O et de côté a. K, L milieux de [CD], [DA].
1. Figure.
2. Unique rotation r : $A\to B, K\to L$ ; centre et angle.
3.a) Unique similitude directe $f_1$ : $D\to L, B\to O$ ; rapport et angle.
3.b) P centre de $f_1$ ; sur cercles [AB] et [OD] ; P = (BL)∩(AK).
4.a) $f_2$ : $B\to D, O\to L$ ; angle et rapport.
4.b) Centre de $f_2$ = P.
5.a) $h=f_1\circ f_2$ homothétie ; centre et rapport. $P=\text{bar}\{(B,\beta);(L,\gamma)\}$.
5.b) $P=\text{bar}\{(A,\alpha);(K,\lambda)\}$.
Partie B — Cube ABCDEFGH ; réflexions $s_1, s_2, s_3, s_4$ de plans (ABCD), (AEHD), (ABFE), (DCGH). $f=s_1\circ s_2\circ s_3\circ s_4$, $r=s_1\circ s_2$, $t=s_3\circ s_4$.
1. r demi-tour ; axe.
2. t translation ; vecteur.
3. Caractériser f.""",

    # ═══════════════ 2015 SC ═══════════════
    ("C", "math", 2015, "sc", 1): r"""Exercice 1 (3 points)
$f(x,y)=2x-3y$ pour x, y entiers.
1.a) Calculer $f(5,3)$.
1.b) Solutions dans $\mathbb{Z}^2$ de $2x+3y=1$.
2. $X_n=f(5^n, 3^n)$.
a) Reste de $X_n$ par 7 selon n.
b) $X_{2015}-5$ divisible par 7.""",
    ("C", "math", 2015, "sc", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(6+5i)z^2+(1+20i)z+14-5i$.
1.a) $P(i)$ ; $a, b$ tels que $P(z)=(z-i)(z^2+az+b)$.
1.b) Solutions.
2. A, B, C d'affixes $i, 4+i, 2+3i$. Similitude directe s de centre A : $B\to C$.
a) Expression complexe de s.
b) Rapport et angle.
3.a) $\Gamma_1:\dfrac{z-i}{z-4-i}$ imaginaire pur ; $\Gamma_2:\dfrac{z-i}{z-2-3i}$ imaginaire pur.
3.b) $s(\Gamma_1)=\Gamma_2$.""",
    ("C", "math", 2015, "sc", 3): r"""Exercice 3 (4 points)
Triangle équilatéral direct ABC de centre O et de côté a. I, J, K milieux.
1.a) Figure.
1.b) Unique rotation $r_1$ : $B\to C, J\to K$ ; centre et angle.
1.c) $r_2$ : $B\to C, K\to J$ ; centre et angle.
2.a) $f=r_1\circ r_2$ et $g=r_2\circ r_1$ ; caractériser.
2.b) $g\circ f=t_{\vec{BC}}$.
3.a) Unique similitude directe s : $B\to I, C\to J$ ; angle et rapport.
3.b) $s(A), s(O)$.
3.c) $h=r\circ s$.
4. $\Gamma$ ellipse de foyers I, J passant par C.
a) $K\in\Gamma$.
b) Construire les sommets.""",
    ("C", "math", 2015, "sc", 4): r"""Exercice 4 (4 points)
$f(x)=\dfrac{x+1}{e^x}$ sur $\mathbb{R}$, courbe C.
a) Tableau de variation.
b) Tracer C.
2. $f_n(x)=\dfrac{(1+x)^n}{e^x}$ ; $F_n(x)=\int_{-1}^x f_n(t)\,dt$. Par IPP, $F_{n+1}(x)=(n+1)F_n(x)-f_{n+1}(x)$.
3. $I_n=F_n(0)$.
a) $I_{n+1}=(n+1)I_n-1$.
b) Suite décroissante et positive.
c) $\tfrac{1}{n+1}\le I_n\le\tfrac{1}{n}$ ; $\lim I_n=0$.
4. $U_n=\tfrac{I_n}{n!}$.
a) $U_{n+1}=U_n-\tfrac{1}{(n+1)!}$ ; $U_n=e-\sum_{k=0}^n\tfrac{1}{k!}$.
b) $\lim\sum\tfrac{1}{k!}=e$.""",
    ("C", "math", 2015, "sc", 5): r"""Exercice 5 (5 points)
$f(x)=x\ln(x+1)$.
1.a) Limites en $-1$ et $+\infty$.
1.b) $f'(x)$ et signe.
1.c) Tableau de variation.
2.a) Tracer (C).
2.b) $\int_0^1\tfrac{x^2}{1+x}\,dx$.
2.c) Aire A du domaine.
3. $U_n=\int_0^1 x^n\ln(1+x)\,dx$.
a) $U_1=\tfrac{1}{4}$.
b) $0\le U_n\le\tfrac{\ln 2}{n+1}$ ; $\lim U_n=0$.
4. $S_n(x)=1-x+\cdots+(-x)^n$.
a) Expression de $S_n(x)$.
b) Somme $\sum\tfrac{(-1)^k}{k+1}$.
c) IPP.
5. $V_n=1-\tfrac{1}{2}+\tfrac{1}{3}-\cdots+\tfrac{(-1)^n}{n+1}$.
a) Encadrement.
b) $\lim V_n=\ln 2$.
c) $\lim(n+1)U_n$.""",

    # ═══════════════ 2015 SN ═══════════════
    ("C", "math", 2015, "sn", 1): r"""Exercice 1 (5 points)
1. $P(z)=z^3-(11+6i)z^2+(28+38i)z-12-60i$.
a) $P(3)=0$ et factorisation.
b) Résoudre $P(z)=0$.
c) Barycentre G.
2. $f_k(M)=M'\Leftrightarrow\vec{MM'}=2\vec{MA}-2\vec{MB}+(3-k)\vec{MC}$.
a) Translation.
b) Point invariant $\Omega_k$.
c) Lieu de $\Omega_k$.
d) Lieu de R.
3. $\varphi(M)=2MA^2-2MB^2+2MC^2$ et $\Gamma_m$.
a) Nature de $\Gamma_m$.
b) Construction pour $m=10$.""",
    ("C", "math", 2015, "sn", 2): r"""Exercice 2 (5 points)
Rectangle direct ABCD, $AB=a, AD=2a$.
1. Figure.
1.b) Rotation r.
2.a) Antidéplacement g.
2.b) Symétrie glissante.
2.c) Forme réduite.
3. Similitude s : angle, rapport, $s(J)=B$.
4. P centre de s.
a) P sur $\Gamma_1, \Gamma_2$.
b) Symétrie.
c) P sur (BE).
5. R symétrique de L.
a) $s(L)=R$.
b) Droite fixe et triangle rectangle isocèle.
6. Parabole $\Gamma$.
a) Passage par A, O, D.
b) Tangente.
c) Foyer et directrice de $\Gamma'$.""",
    ("C", "math", 2015, "sn", 3): r"""Exercice 3 (5 points)
$f(x)=\dfrac{1}{1+e^x}$.
1.a) Limites.
1.b) Tableau de variation.
1.c) Bijection et $f^{-1}(x)$.
2.a) $\Omega(0,\tfrac{1}{2})$ centre de symétrie.
2.b) Intersection C et C'.
2.c) Tracer C, C'.
2.d) Aire A.
3. $I_n=\int_0^\alpha f^n(t)\,dt$.
a) $I_1$.
b) $f'(x)=f^2(x)-f(x)$.
c) $I_{n+1}-I_n$.
d) Suite décroissante.
4. Encadrement de $I_n$ et limites.""",
    ("C", "math", 2015, "sn", 4): r"""Exercice 4 (5 points)
$g(x)=\dfrac{3x^3-12x^2+19x-10}{x^3-4x^2+5x}$.
1.a) Déterminer a, b, c.
1.b) Signe de g(x).
2. $f(x)=3x-3+\ln(\tfrac{x^2-4x+5}{x^2})$.
a) Limite en 0.
b) Limites en $\pm\infty$.
c) Asymptotes et position relative.
3.a) $f'(x)=g(x)$.
3.b) $f(x)=0$ unique solution.
3.c) Construire (C).
4. Aire S.
a) Vérification.
b) Calcul de A.
c) Calcul de B par changement de variable.
d) IPP pour J et K.""",

    # ═══════════════ 2016 SC ═══════════════
    ("C", "math", 2016, "sc", 1): r"""Exercice 1 (5 points)
$P(z)=z^3-(1+3i)z^2+2iz+6-2i$.
1.a) $P(1-i)$.
1.b) $a, b$ tels que $P(z)=(z-1+i)(z^2+az+b)$.
1.c) Solutions.
2. A, B, C d'affixes $-1+i, 1-i, 1+3i$.
a) Placer ; nature de ABC.
b) G barycentre de $\{(A,2);(B,1);(C,1)\}$.
c) $I:2MA^2+MB^2+MC^2=16$.
d) $A:-2MA^2+MB^2+MC^2=16$.
3. s similitude directe de centre C : $A\to B$.
a) Expression complexe.
b) Rapport et angle.
4. Parabole P de foyer A et directrice (BC).
a) Axe focal et sommet.
b) Tracer P et $P'=s(P)$.
c) Équations cartésiennes de P et $P'$.""",
    ("C", "math", 2016, "sc", 2): r"""Exercice 2 (5 points)
$f(x)=(1+x)e^{-x}$ sur $\mathbb{R}$, courbe (C).
1.a) Limites en $\pm\infty$ et $\tfrac{f(x)}{x}$.
1.b) Interprétation.
2.a) Tableau de variation et tracé.
2.b) Aire A entre (C), (Ox), $x=-1, x=0$.
3. $f_n(x)=\dfrac{(1+x)^n e^{-x}}{n!}$. $0\le f_n(x)\le\dfrac{e}{n!}$ sur $[-1;0]$.
4. $I_n=\int_{-1}^0 f_n(x)\,dx$.
a) $I_1=$ A.
b) Par IPP, $I_{n+1}=I_n-\dfrac{1}{(n+1)!}$.
5. $U_n=\sum_{k=0}^n\dfrac{1}{k!}$.
a) $I_n=e-U_n$.
b) $0\le I_n\le\dfrac{e}{n!}$ ; $\lim I_n=0$.
c) $\lim U_n=e$.""",
    ("C", "math", 2016, "sc", 3): r"""Exercice 3 (5 points)
$f(x)=\dfrac{e^{2x}-1}{6e^x}$ sur $\mathbb{R}$, courbe (C).
1.a) f impaire ; $\lim_{-\infty}f=-\infty$ ; $\lim_{+\infty}f=+\infty$.
1.b) $\lim\tfrac{f(x)}{x}$ en $+\infty$ ; interprétation.
1.c) Tableau de variation.
1.d) $f(x)=x$ admet 3 solutions dont $\alpha\in]2{,}8; 2{,}9[$.
2.a) Bijection.
2.b) $(f(x))^2-(f'(x))^2=-\tfrac{1}{9}$ ; expression de $(f^{-1})'(x)$.
2.c) $I(x)=\int_0^x\dfrac{3}{\sqrt{9t^2+1}}\,dt$ en fonction de $f^{-1}(x)$.
3. r rotation de centre O et angle $\tfrac{\pi}{2}$. $r(M)=M'$ ; $r(C)=C_1$.
a) Expression complexe ; $x', y'$.
b) $(C_1)$ est la courbe de $h(x)=\ln(-3x+\sqrt{9x^2+1})$.
c) $h(-x)=f^{-1}(x)$ ; $(C')$ courbe de $f^{-1}$.
4.a) (C) et $(C')$ se coupent en 2 points autres que O.
4.b) Construire ; aire entre (C) et $(C')$ en fonction de $\alpha$.""",
    ("C", "math", 2016, "sc", 4): r"""Exercice 4 (5 points)
Triangle équilatéral direct ABC de centre G et côté a. I, J, K, L milieux de [BC], [AC], [AB], [AI]. D symétrique de I par J.
1. Figure.
2.a) Unique rotation $r_1$ : $B\to C, I\to J$.
2.b) $r_1(K)$ ; centre et angle.
3. $r_2$ rotation de centre K et angle $\tfrac{\pi}{3}$.
a) $r_2(B), r_2(I)$.
b) $r_2(C)$.
4.a) Unique antidéplacement f : $B\to C, I\to J$.
4.b) f symétrie glissante ; forme réduite.
4.c) $g=f\circ r_1^{-1}$.
5. $\sigma=r_2\circ r_1$ ; $\sigma(M)=M'$.
a) Caractériser $\sigma$.
b) Si $M\ne M'$, (MM') passe par un point fixe.
c) AMIM' parallélogramme.
6. M tels que M, $M_1, M_2$ alignés.""",

    # ═══════════════ 2016 SN ═══════════════
    ("C", "math", 2016, "sn", 1): r"""Exercice 1 (3 points)
(E) : $5x-3y=17$.
1.a) Existence ; (4,1) solution particulière.
1.b) Solutions.
2. (x,y) solution de (E).
a) Si x divise y alors x divise 17.
b) m tels que $\dfrac{1+5m}{4+3m}\in\mathbb{Z}$.""",
    ("C", "math", 2016, "sn", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(4+8i)z^2+(-14+24i)z+32+4i$.
1.a) $P(2i)$ ; $a, b$ tels que $P(z)=(z-2i)(z^2+az+b)$.
1.b) Solutions $z_1, z_2, z_3$ avec $|z_1|<|z_2|<|z_3|$.
1.c) G barycentre de $\{(O,5);(A,-7);(C,4)\}$.
2. $Q(z)=z^2-(4+6i)z-2+16i$ ; $\Gamma=\{M:Q(z)\text{ imaginaire pur}\}$.
a) Équation cartésienne ; conique de centre G.
b) Sommets, excentricité, construction.""",
    ("C", "math", 2016, "sn", 3): r"""Exercice 3 (4 points)
$f(x)=xe^{1/x}$ pour $x\ne 0$, $f(0)=0$, courbe (C).
a) Limites en $0^-$ et $0^+$.
b) $\lim\tfrac{f}{x}$ en $0^+$ ; $\lim(f-(x+1))$ en $\pm\infty$.
c) Tableau de variation.
d) Construire (C).
2. $f_n(x)=xe^{n/x}$ pour $x\ne 0$, $f_n(0)=0$ ; courbe $(C_n)$.
a) $(C_n)$ image de (C) par homothétie $h_n$ de centre O ; rapport.
b) Lieu $\Delta$ des points à tangente horizontale.
c) Tableau de variation de $f_2$ et $(C_2)$.""",
    ("C", "math", 2016, "sn", 4): r"""Exercice 4 (4 points)
$f(x)=\ln(x+1)-\tfrac{x}{x+1}$ sur $]-1,+\infty[$, courbe (C).
1.a) Limites en $-1^+, +\infty$ et $\tfrac{f}{x}$.
1.b) Tableau de variation.
1.c) Point d'inflexion.
1.d) Tracer (C).
2.a) $\int_0^x\ln(1+t)\,dt$ et primitive F qui s'annule en 0.
2.b) Aire $A_n$ entre (C), (Ox), $x=0, x=\tfrac{1}{n}$.
3. $x\in]0;1[$, $n\ge 1$.
a) $\dfrac{1}{1+x}=\sum_{k=1}^{n+1}(-1)^{k-1}x^{k-1}+\dfrac{(-1)^{n+1}x^{n+1}}{1+x}$.
b) Développement de $\ln(1+x)$.
c) Développement de $f(x)$.
d) $0\le\int_0^x\dfrac{t^{n+1}}{1+t}\,dt\le\dfrac{x^{n+2}}{n+2}$.
e) $f(x)=\lim_{n\to\infty}\sum(-1)^{k-1}\dfrac{1-k}{k}x^k$.""",
    ("C", "math", 2016, "sn", 5): r"""Exercice 5 (5 points)
Carré direct ABCD de centre O et côté a. I, J, K, L milieux des côtés. LDEF carré direct.
1.a) Figure.
1.b) Unique rotation r : $A\to D, L\to E$.
1.c) Angle et centre.
2.a) Unique similitude directe $s_1$ : $J\to O, C\to D$.
2.b) Angle et rapport.
2.c) $s_1(B)$ ; centre de $s_1$.
2.d) $s_1(O)$ ; image du carré ABCD.
3. $s_2$ similitude directe de centre A, rapport $\tfrac{1}{\sqrt{2}}$, angle $\tfrac{\pi}{4}$. $s_2(O), s_2(C)$.
4. $f=s_2\circ s_1^{-1}$ ; $M_1=s_1(M), M_2=s_2(M)$.
a) $f(D)$ et caractériser f.
b) $(M_1M_2)$ passe par un point fixe.
c) $\Gamma_1$ : M, $M_1, M_2$ alignés.
5.a) $O=\text{bar}\{(A,1);(D,3);(E,-2)\}$.
5.b) $\Gamma_2:2MA^2+6MD^2-4ME^2=a^2$ ; $\Gamma_3:(\vec{MA}+\vec{MK}-\vec{ME})\cdot(2\vec{ML}+2\vec{MK}-\vec{MB})=0$.""",

    # ═══════════════ 2017 SC ═══════════════
    ("C", "math", 2017, "sc", 1): r"""Exercice 1 (3 points)
(E) : $2017x+41y=1$.
1.a) 2017 premier ; (E) admet des solutions entières.
1.b) (-5;246) solution particulière ; résoudre (E).
1.c) Unique entier $y\le 2016$ tel que $41y\equiv 1\ [2017]$.
2. a, b entiers ; ab inverse modulo 2017.
a) $ab\equiv 0\ [2017]$ implique $a\equiv 0$ ou $b\equiv 0$.
b) $a^2\equiv 1\ [2017]$ implique $a\equiv\pm 1$.
c) Entiers de [1;4033] égaux à leurs inverses modulo 2017.""",
    ("C", "math", 2017, "sc", 2): r"""Exercice 2 (4 points)
(E) : $iz^3-(1+i)z^2-(2+2i)z+8i=0$.
a) Solution réelle.
b) Autres solutions.
c) A, B, C d'affixes $-2, 2-2i, 1+i$ ; nature de ABC.
2. s : $x'=x+y, y'=-x+y-2$.
a) Expression complexe.
b) Nature et éléments ; $s(C)$.
3. $z_G$ et $f(z)=|z+2|^2+|z-2+2i|^2+|z-1-i|^2$.
a) $z_G=\tfrac{1}{3}-\tfrac{1}{3}i$ ; $f(z)=3|z-z_G|^2+\tfrac{40}{3}$.
b) Ensemble $\Gamma_k:f(z)=k$.""",
    ("C", "math", 2017, "sc", 3): r"""Exercice 3 (5 points)
Rectangle direct ABCD avec $CB=2CD$. E, F, O milieux de [CB], [AD], [AE]. $I=S_B(A)$.
1.a) Figure.
1.b) Unique rotation r : $A\to E, E\to D$ ; centre et angle.
1.c) $f=S_D\circ S_B\circ S_A\circ S_F$ ; $f(A), f(B)$ ; f symétrie glissante.
2.a) Unique similitude directe s : $O\to E, E\to B$ ; rapport et angle.
2.b) $\Omega$ centre sur $\Gamma_1, \Gamma_2$ (diamètres [EF], [EI]).
3. M sur $\Gamma_1$ et $M'=s(M)$.
a) J, K milieux de [EF], [EI] ; $s(J)=K$ ; $s(\Gamma_1)=\Gamma_2$.
b) (MM') passe par un point fixe.
c) Construction de $M'$.
4. P parabole de directrice (AD) et foyer E.
a) Sommet.
b) P passe par B, C.
c) Tangentes en B, C.
d) Unicité.""",
    ("C", "math", 2017, "sc", 4): r"""Exercice 4 (4 points)
$f_n(x)=(\ln x)^n$ sur $]0;+\infty[$, $n>1$ ; courbe $(C_n)$.
1.a) Limites en $+\infty$ et $0^+$ selon parité.
1.b) $f_n'(x)$ ; tableau de variation.
2.a) Positions relatives de $(C_2)$ et $(C_3)$.
2.b) Construire.
3. $I_n=\dfrac{(-1)^n}{n!}\int_1^e f_n(x)\,dx$ et $u_n=\sum_{k=0}^n\dfrac{(-1)^k}{k!}$.
a) Par IPP, $I_2=\dfrac{e-2}{2}$.
b) $I_{n+1}=\dfrac{(-1)^{n+1}}{(n+1)!}e+I_n$.
c) $I_2=-1+e\cdot u_2$.
c') $I_n=-1+e\cdot u_n$.
4.a) $0\le f_n(x)\le 1$ sur $[1;e]$ ; $|I_n|\le\dfrac{e-1}{n!}$.
4.b) $\lim I_n=0$ ; $\lim u_n=e^{-1}$.""",
    ("C", "math", 2017, "sc", 5): r"""Exercice 5 (4 points)
$f(x)=\int_x^{3x}\dfrac{e^{-t^2}}{t}\,dt$ et $f(0)=\ln 3$.
1.a) $e^x\ge x+1$.
1.b) $1-t\le e^{-t}\le 1$ pour $t>0$.
1.c) $\ln 3-4x^2\le f(x)\le\ln 3$ pour $x>0$.
1.d) f continue et dérivable en $0^+$ ; $f_d'(0)=0$.
2. $g(x)=\int_1^x\dfrac{e^{-t^2}}{t}\,dt$.
a) g dérivable ; $g'(x)$.
b) $f(x)=-g(x)+g(3x)$.
c) $f'(x)=\dfrac{e^{-x^2}}{x}(e^{-8x^2}-1)$.
3.a) Pour $t\in[x;3x]$ avec $x>1$, $e^{-9x^2}\le e^{-t^2}\le e^{-x^2}$.
3.b) Encadrement de f(x).
3.c) $\lim_{+\infty}f$.
3.d) Tableau de variation.""",

    # ═══════════════ 2017 SN ═══════════════
    ("C", "math", 2017, "sn", 1): r"""Exercice 1 (4 points)
1.a) a réel ; résoudre dans $\mathbb{C}$ : $(1+i)z^2-2(a+1)z-(-1+i)(a^2+1)=0$.
1.b) $f:z\to z'=1-iz$ et $g:z\to z''=z-i$ ; nature et éléments.
2. I, $M_1, M_2$ d'affixes $1-i, 1-ia, a-i$ où $a=e^{i\alpha}$, $\alpha\in]0,2\pi[$.
a) Triangle $IM_1M_2$ rectangle isocèle direct.
b) Lieux des $M_1, M_2$ pour $\alpha\in]0,\pi[$.
c) Formes exponentielles.
3. $M_3$ d'affixe $i\sin\alpha+ia$ ; G isobarycentre des $M_i$.
a) $z_G=\tfrac{1+\cos\alpha}{3}+i\tfrac{-1+2\sin\alpha}{3}$ ; G sur ellipse $\mathcal{E}$.
b) Sommets, excentricité, construction.""",
    ("C", "math", 2017, "sn", 2): r"""Exercice 2 (6 points)
Triangle équilatéral direct ABC de côté 4 cm, cercle circonscrit $\mathcal{C}$. I, J, K milieux. $A'=s_B(A)$.
1.a) Figure.
1.b) Antidéplacement g : $B\to A, A'\to B$ ; symétrie glissante.
1.c) Rotation r : $C\to B, J\to K$ ; angle et centre.
2. Similitude directe s : $A\to B, C\to I$ ; $h=s\circ r$.
a) Rapport et angle de s.
b) $\Omega$ centre de s ; $\Omega\in\mathcal{C}$ ; $\Omega, A, I$ alignés.
c) Nature et éléments de h.
3. M sur $\mathcal{C}\setminus\{\Omega\}$ ; $M'=s(M)$, $M_1=r(M)$.
a) $\Omega MM'$ rectangle.
b) $(MM')$ passe par un point fixe.
c) $M_1, M, M'$ alignés.
4. $M_0=A, M_{n+1}=s(M_n)$.
a) $M_1, M_2$.
b) $M_{2017}\in(\Omega B)$.
c) $L_n=M_nM_{n+1}$, $S_n=\sum L_k$ ; $\lim S_n$.""",
    ("C", "math", 2017, "sn", 3): r"""Exercice 3 (5 points)
$f_n(x)=\dfrac{e^{-nx}}{1+e^{-x}}$ sur $\mathbb{R}$ ; courbe $(C_n)$.
1. Toutes les courbes passent par un point fixe.
2.a) Tableau de variation de $f_0$.
2.b) M, N de $(C_0)$ d'abscisses $x, -x$ ; milieu A.
3.a) $(C_0), (C_1)$ symétriques par rapport à (Oy).
3.b) Tableau de variation de $f_1$.
3.c) Construire.
4. $n>1$.
a) Limites ; interprétation.
b) $f_n'$ ; tableau de variation.
5. $u_n=\int_0^1 f_n(x)\,dx$.
a) $u_0=\ln(\tfrac{1+e}{2})$.
b) $u_0+u_1=1$ ; $u_{n+1}+u_n=\tfrac{1-e^{-n}}{n}$ ; $u_1, u_2$.
c) Convergence et limite.""",
    ("C", "math", 2017, "sn", 4): r"""Exercice 4 (5 points)
$f(x)=\dfrac{\ln x}{x^2}$ sur $]0;+\infty[$.
a) Tableau de variation.
b) Pour $n\ge 6$, $f(x)=\tfrac{1}{n}$ admet une seule solution $a_n\in[1,\sqrt{e}]$.
c) $(a_n)$ décroissante et convergente.
2.a) $\dfrac{\ln(k+1)}{(k+1)^2}\le\int_k^{k+1}f\le\dfrac{\ln k}{k^2}$.
2.b) Par IPP, $\int_2^n\dfrac{\ln x}{x^2}\,dx$.
3. $S_n=\sum_{k=2}^n\dfrac{\ln k}{k^2}$.
a) Encadrement.
b) Encadrement explicite.
4. $u_n=\sum_{k=1}^n\dfrac{(\ln 2)^{k-1}}{k!}$ et $I_n=\tfrac{1}{n!}\int_1^2\dfrac{(\ln x)^n}{x^2}\,dx$.
a) $0\le I_n\le\dfrac{(\ln 2)^n}{n!}$ ; $\lim I_n$.
b) $I_{n+1}=I_n-\tfrac{1}{2}\dfrac{(\ln 2)^{n+1}}{(n+1)!}$.
c) $I_n=\tfrac{1}{2}-\tfrac{1}{2}\sum_{k=1}^n\dfrac{(\ln 2)^k}{k!}$.
d) $(u_n)$ et limite.""",

    # ═══════════════ 2018 SC ═══════════════
    ("C", "math", 2018, "sc", 1): r"""Exercice 1 (5 points)
$P(z)=z^3-(7+3i)z^2+(12+15i)z-4-18i$.
1.a) $P(2)$ ; $a, b$ tels que $P(z)=(z-2)(z^2+az+b)$.
1.b) Solutions.
1.c) A, B, D images avec $\text{Im}(z_A)\le\text{Im}(z_B)\le\text{Im}(z_D)$ ; nature de ABD.
2.a) Barycentre de $\{(A;9),(B;-6),(C;2)\}$, C symétrique de A par (BD).
2.b) $\Gamma_1:9MA^2-6MB^2+2MC^2=-10$.
2.c) $\Gamma_2:4MA^2-6MB^2+2MC^2=-10$.
2.d) $\Gamma_3:(9\vec{MA}-6\vec{MB}+2\vec{MC})\cdot(\vec{MA}-\vec{MB}+\vec{MC})=10$.
3. $S^0=\text{id}, S^{n+1}=S\circ S^n$ ; S similitude directe $A\to B, B\to D$.
a) $S^{2018}$ ; nature et éléments.
b) $S^{2020^{2020}}$ homothétie de rapport positif.""",
    ("C", "math", 2018, "sc", 2): r"""Exercice 2 (5 points)
I. $f(x)=(x+1)e^{-1/x}$ pour $x>0$, $f(0)=0$.
1.a) Continuité et dérivabilité à droite en 0.
1.b) Tableau de variation.
2.a) $0\le e^{-t}+t-1\le\dfrac{t^2}{2}$.
2.b) $f(x)-x\le\dfrac{1}{2x^2}-\dfrac{1}{2x}$.
2.c) Asymptote oblique A.
3. Construire (C) et A.
4.a) Bijection sur J.
4.b) Construire $(C')$ de $f^{-1}$.
II. $f_n(x)=(x+\tfrac{1}{n})e^{-1/x}$ pour $x>0$, $f_n(0)=0$.
1.a) Continuité, dérivabilité en 0.
1.b) Variations ; $f_n(x)=\tfrac{1}{n}$ admet une unique solution $\alpha_n$.
2.a) $g_n(x)=f_n(x)-\tfrac{1}{n}$ ; signe de $g_{n+1}-g_n$ ; $(\alpha_n)$ décroissante convergente.
2.b) $\alpha_n=\tfrac{1}{n}(e^{1/\alpha_n}-1)$ ; $\lim\alpha_n$.""",
    ("C", "math", 2018, "sc", 3): r"""Exercice 3 (5 points)
Carré direct ABCD de centre O et côté a. G milieu de [AB]. AEFG carré direct.
1.a) Figure.
1.b) Unique rotation r : $O\to A, B\to O$.
1.c) Éléments.
1.d) g antidéplacement : $B\to E, O\to G$ ; symétrie glissante ; forme réduite.
2.a) Unique similitude directe s : $C\to F, B\to E$.
2.b) Image du carré ABCD par s ; centre de s.
3. $h=s\circ r^{-1}$.
a) h homothétie ; rapport.
b) I centre de h ; $I=\text{bar}\{(O,1);(E,2)\}$.
c) $M'=r(M), M''=s(M)$ ; (M'M'') passe par un point fixe.
4. $\Gamma$ hyperbole de foyers O, F passant par J projeté orthogonal de I sur (OF).
a) Coordonnées dans $(G,\vec{GB},\vec{GO})$.
b) Équation.
c) Sommets, asymptotes, excentricité.
d) Construire.""",
    ("C", "math", 2018, "sc", 4): r"""Exercice 4 (5 points)
$f(x)=-x+2\ln(1+e^x)$ sur $\mathbb{R}$, courbe (C).
Partie A.
1.a) Tableau de variation.
1.b) Asymptotes D, D' ; positions relatives.
1.c) Construire (C) et asymptotes.
2. g restriction sur $I=[0,+\infty[$.
a) Bijection sur J.
b) Construire $(C')$ de $g^{-1}$.
Partie B. $u_n=\int_0^{\ln 5}(f'(t))^n\,dt$, $u_0=\ln 5$.
1. Calculer $u_1$.
2.a) $0\le f'(x)\le\tfrac{2}{3}$ sur $[0,\ln 5]$.
2.b) $0\le u_n\le(\tfrac{2}{3})^n\ln 5$.
2.c) $\lim u_n$.
3.a) $(f'(x))^2-1=-2f''(x)$.
3.b) $u_{n+2}-u_n=\dfrac{-2}{n+1}(\tfrac{2}{3})^{n+1}$.
3.c) Expressions de $u_{2n}, u_{2n+1}$.
4. $v_n=\sum_{p=1}^{2n}\dfrac{1}{p}(\tfrac{2}{3})^p$ ; $v_n=\ln 3-\tfrac{u_{2n}+u_{2n+1}}{2}$ ; $\lim v_n$.""",

    # ═══════════════ 2018 SN ═══════════════
    ("C", "math", 2018, "sn", 1): r"""Exercice 1 (3 points)
1.a) (E) : $25x-49y=5$ ; PGCD ; solutions entières.
1.b) (10;5) solution particulière ; résoudre (E).
1.c) Unique entier $p\in[1960;2018]$ tel que $25p\equiv 5\ [49]$.
2.a) Si (x,y) solution alors $5x\equiv 1\ [7]$ et $y\equiv 0\ [5]$.
2.b) $5x\equiv 1\ [7]\Leftrightarrow x\equiv 3\ [7]$.
3.a) Restes de $x^2$ par 7.
3.b) Existence de $(x^2, y^2)$ solution de (E).""",
    ("C", "math", 2018, "sn", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(1+4i)z^2-(9-i)z-6+18i$.
1.a) $P(3i)$ ; factorisation.
1.b) Solutions.
1.c) A, B, C avec $|z_C|\le|z_B|\le|z_A|$ ; nature de ABC.
1.d) $A'=\text{bar}\{(A;-5),(B;6),(C;12)\}$ ; $z_{A'}=-3+i$.
2. Ellipse $\Gamma$ de sommets A, $A'$, B.
a) Centre I et excentricité.
b) Équation cartésienne.
c) Intersections avec (Ox).
d) Foyers et directrices ; construction.""",
    ("C", "math", 2018, "sn", 3): r"""Exercice 3 (4 points)
Parallélogramme ABCD avec $(\vec{AB},\vec{AD})=\tfrac{\pi}{4}$ et $AB=2AD$. E, F, G, H tels que AFEB et ADGH carrés directs. I, J, K milieux de [EC], [CG], [GA].
1. Figure.
2. $R_A$ rotation centre A angle $\tfrac{\pi}{2}$, T translation $\vec{BC}$, $f=T\circ R_A$.
a) Nature de f.
b) $f(D)$ ; caractériser f ; image de F.
c) [DF] et [CG] perpendiculaires et de même longueur.
3.a) $\vec{DF}, \vec{CE}$ ; ECG rectangle isocèle direct en C.
3.b) Unique antidéplacement g : $E\to C, C\to G$.
3.c) g symétrie glissante ; forme réduite.
4. S similitude directe : $B\to A, A\to D$.
a) Rapport et angle.
b) $\Omega$ centre sur $\Gamma_1, \Gamma_2$ (cercles AFEB et ADGH).
c) $S(F)=G$ ; $S(\Gamma_1)=\Gamma_2$.
d) $M\in\Gamma_1, M'=S(M)$ ; A, M, $M'$ alignés.""",
    ("C", "math", 2018, "sn", 4): r"""Exercice 4 (4 points)
1.a) (E) : $y''-6y'+8y=0$.
1.b) Solution $y_0$ passant par $(0,-1)$ avec tangente horizontale.
2. $f(x)=e^{4x}-2e^{2x}$ sur $\mathbb{R}$, courbe (C).
a) Limites.
b) Tableau de variation.
3. g restriction sur $I=]-\infty,0]$.
a) Bijection sur J.
b) $\lim\dfrac{g^{-1}(x)}{x+1}$ en $-1$.
c) (C) et (C') se coupent en B d'abscisse $\alpha\in]-0,6;-0,5[$.
d) Tracer (C) et (C').
e) Expression de $g^{-1}(x)$.
4. Aire S.
a) $S=2\int_\alpha^0(x-f(x))\,dx$.
b) Valeur de S en fonction de $\alpha$.""",
    ("C", "math", 2018, "sn", 5): r"""Exercice 5 (5 points)
Partie A. $f(x)=\dfrac{x}{x+1}-(x+1)\ln(x+1)$ sur $]-1,+\infty[$, courbe (C).
1. Limites en $-1^+, +\infty$.
2.a) $f'(x), f''(x)$ ; variations de $f'$.
2.b) $f'(0)$ ; signe de $f'(x)$.
3.a) Tableau de variation.
3.b) Tracer (C).
4.a) $\int_0^x\dfrac{t}{t+1}\,dt$ et par IPP $\int_0^x(t+1)\ln(1+t)\,dt$.
4.b) Primitive F qui s'annule en 0.
4.c) Aire $A_n$ entre (C), (Ox), $x=0, x=n$.
Partie B. $U_n=\sum_{k=1}^{n-1}\tfrac{1}{k+1}f(k)$.
1. $V_n=\tfrac{1}{n+1}f(n)$.
a) $V_n=\dfrac{1}{n+1}-\dfrac{1}{(n+1)^2}-\ln(n+1)$.
b) $U_n=S_n-S_n'-\ln(n!)$.
2. $S_n=\sum\tfrac{1}{k}$, $S_n'=\sum\tfrac{1}{k^2}$.
a) $\tfrac{1}{n}+\ln n\le S_n\le 1+\ln n$.
b) $1-\tfrac{1}{n}+\tfrac{1}{n^2}\le S_n'\le 2-\tfrac{1}{n}$.
c) Encadrement de $U_n+\ln((n-1)!)$.""",

    # ═══════════════ 2019 SC ═══════════════
    ("C", "math", 2019, "sc", 1): r"""Exercice 1 (5 points)
$P(z)=z^3-(12+5i)z^2+(45+42i)z-(54+97i)$.
a) m, p tels que $P(z)=(z-3-4i)(z^2+mz+p)$ ; résoudre $P(z)=0$.
b) A, B, C avec $\text{Re}(z_A)\ge\text{Re}(z_B)\ge\text{Re}(z_C)$.
a') I barycentre de $\{(A;-3);(B;2);(C;3)\}$.
b') S similitude directe de centre I, rapport $\tfrac{1}{\sqrt{2}}$, angle $\tfrac{\pi}{4}$.
c') $S(C)=D$ d'affixe $1+4i$.
2. Ellipse $\Gamma$ de centre I avec D, A sommets.
a) Équation réduite dans $(O,\vec{i},\vec{j})$.
b) Excentricité, foyers, autres sommets ; construire.
3. $(M_n)$ : $M_0=C, M_{n+1}=S(M_n)$.
a) Affixes $z_1, z_2, z_3$.
b) Tous $M_n$ sur l'une des droites (IA), (IB), (IC), (ID) ; laquelle pour $M_{2019}$.""",
    ("C", "math", 2019, "sc", 2): r"""Exercice 2 (5 points)
$I_n=\int_2^4\dfrac{(x-2)^n e^{2-x}}{n!}\,dx$.
1.a) Par IPP, $I_1$.
1.b) $0\le I_n\le\dfrac{2^n}{n!}(1-e^{-2})$.
2.a) Par IPP, $I_{n+1}=I_n-\dfrac{2^{n+1}}{(n+1)!}e^{-2}$.
2.b) $(I_n)$ décroissante donc convergente.
3. $u_n=\dfrac{2^n}{n!}e^{-2}$.
a) $u_{n+1}\le\tfrac{1}{3}u_n$ pour $n\ge 5$.
b) $0\le u_n\le\tfrac{4}{15}(\tfrac{1}{3})^{n-5}$ ; $\lim u_n=0$.
c) $0\le I_n\le(e^2-1)u_n$ ; $\lim I_n=0$.
4.a) $I_n=1-e^{-2}\sum_{k=0}^n\dfrac{2^k}{k!}$.
4.b) $\lim\sum=e^2$.""",
    ("C", "math", 2019, "sc", 3): r"""Exercice 3 (4 points)
Triangle ABC rectangle isocèle direct en A. I, J, K, O milieux de [AB], [BC], [CA], [AJ]. D symétrique de A par J.
1. Figure.
2. Antidéplacement f : $K\to J, I\to D$ ; symétrie glissante ; forme réduite.
3.a) Unique similitude directe S : $A\to I, B\to J$.
3.b) Rapport et angle.
3.c) Centre $\Omega$ sur cercles AOI et BIJ.
3.d) $S(C)$ ; $\Omega, C, I$ alignés.
3.e) $\Omega=\text{bar}\{(C,a);(I,b)\}$.
4. h homothétie de centre $\Omega$ : $O\to B$. $g=h\circ S$.
a) $h(I)=C$ ; rapport.
b) Nature et éléments de g ; $g(I)$.
c) Image de AIJK par g ; ($\Omega D$) passe par L milieu de [AI].""",
    ("C", "math", 2019, "sc", 4): r"""Exercice 4 (5 points)
$f(x)=\dfrac{3\ln x}{1+x^3}$ sur $]0;+\infty[$, courbe (C).
1. $u(x)=1+x^3(1-3\ln x)$.
a) Limites en $0^+, +\infty$.
b) Tableau de variation.
c) Solution unique $\alpha$ avec $1{,}5\le\alpha\le 1{,}6$ ; signe.
2.a) Limites de f ; interprétations.
2.b) $f'(x)=\dfrac{3u(x)}{x(1+x^3)^2}$ ; tableau de variation.
2.c) $f(\alpha)=\dfrac{1}{\alpha^3}$ ; tracer (C).
3. $v_n=\int_1^e\dfrac{(\ln t)^n}{1+t^3}\,dt$.
a) Décroissante et minorée ; convergente.
b) $\dfrac{1}{1+e^3}\int_1^e(\ln t)^n\,dt\le v_n\le\int_1^e(\ln t)^n\,dt$.
4. $w_n=\int_1^e(\ln t)^n\,dt$.
a) Décroissante.
b) Par IPP, $w_{n+1}=e-(n+1)w_n$.
c) $\dfrac{e}{n+2}\le w_n\le\dfrac{e}{n+1}$ ; $\lim w_n=0$.
d) $\lim v_n=0$.""",

    # ═══════════════ 2019 SN ═══════════════
    ("C", "math", 2019, "sn", 1): r"""Exercice 1 (3 points)
1. (E) : $7x-5y=1$.
a) (3;4) solution ; résoudre.
b) Si (x,y) solution, $x\equiv 3\ [5]$ et $y\equiv 4\ [7]$.
2. S = $\{A : A\equiv 4\ [5], A\equiv 3\ [7]\}$.
a) (x,y) tel que $A=7x+3=5y+4$.
b) $A\in S\Leftrightarrow A\equiv 24\ [35]$.
c) B en base n s'écrit 374a ; déterminer n et écriture décimale.""",
    ("C", "math", 2019, "sn", 2): r"""Exercice 2 (4 points)
$P(z)=z^3-(5+4i)z^2+(7+10i)z+5-10i$.
1. $P(i)$ et solutions $z_0, z_1, z_2$ avec $\text{Re}(z_0)<\text{Re}(z_1)<\text{Re}(z_2)$.
2. A, B, C d'affixes $z_0, z_1, z_2$.
a) Nature de ABC.
b) G barycentre de $\{(A,13);(B,-3);(C,2)\}$.
c) $\Gamma:13MA^2-3MB^2+2MC^2=12$.
3. Hyperbole H de centre G passant par C avec A sommet.
a) 2e sommet.
b) Équation $x^2-3(y-2)^2=-3$.
c) Équation réduite, foyers, asymptotes, excentricité.""",
    ("C", "math", 2019, "sn", 3): r"""Exercice 3 (5 points)
$f(x)=x^3-x\ln x$ pour $x>0$, $f(0)=0$ ; courbe (C).
1.a) Continuité et dérivabilité à droite en 0.
1.b) Limites en $+\infty$.
2.a) $f'(x), f''(x)$ ; point d'inflexion A.
2.b) Variations de $f'$ ; signe.
2.c) Tableau de variation.
3.a) Bijection sur J.
3.b) Positions relatives entre (C) et $(C')$ ; 3 points dont $\alpha\in[0,45;0,46]$.
4. Tracer (C) et $(C')$.
5.a) Par IPP, primitive F qui s'annule en 1.
5.b) $K=\int_\alpha^1 f(t)\,dt$ et $I(n)=\int_{1/n}^\alpha f(t)\,dt$ ; $\lim I(n)$.
5.c) Aire S entre (C) et $(C')$.""",
    ("C", "math", 2019, "sn", 4): r"""Exercice 4 (4 points)
Triangle équilatéral direct ABC de côté a. D, E, F milieux de [BC], [CA], [AB]. Carré direct AGHD de centre O. I, J, K milieux de [EC], [GH], [AD].
1. Figure.
2.a) Unique antidéplacement f : $A\to C, E\to D$.
2.b) f symétrie glissante ; forme réduite.
3.a) Unique rotation r : $H\to B, D\to E$ ; angle. Centre $\Omega$.
3.b) $\Omega\in(CF)$ et sur cercle de diamètre [AB].
3.c) $\Omega\in(DG)$.
4.a) Unique similitude directe S : $B\to D, D\to I$.
4.b) S' similitude directe de centre A, rapport $\tfrac{\sqrt{3}}{2}$, angle $\tfrac{\pi}{6}$.
5. $(M_n)$ : $M_0=B, M_{n+1}=S(M_n)$.
a) $AM_nM_{n+1}$ rectangle.
b) Nature de $ABM_{2019}$ et aire.""",
    ("C", "math", 2019, "sn", 5): r"""Exercice 5 (4 points)
$f(x)=\dfrac{1}{\sqrt{1+e^x}}$.
1. Variations et tracer la courbe.
2. $f(x)=x$ admet une unique solution $\alpha\in]0,7;0,8[$.
3. Aire A entre courbe, (Ox), $x=\alpha, x=\ln 3$.
a) $A=\int_\alpha^{\ln 3}\dfrac{dx}{\sqrt{1+e^x}}$.
b) $t=\dfrac{1}{\sqrt{1+e^x}}$ ; $A=\int_\alpha^{1/2}\dfrac{2dt}{t^2-1}$.
c) Décomposition en éléments simples ; valeur de A.
4. $I_n=\int_\alpha^{\ln 3}(f(t))^{2n}\,dt$, $S_n=\sum I_k$.
a) Encadrement de $I_n$ ; $\lim I_n=0$.
b) $2f'(x)=(f(x))^3-f(x)$.
c) $(f(x))^2=1+2(\tfrac{f'(x)}{f(x)})$ ; $I_1$.
5.a) $I_{n+1}-I_n=\dfrac{1}{n}(\tfrac{1}{2^{2n}}-\alpha^{2n})$.
5.b) Récurrence sur $I_{n+1}$.
5.c) $\lim\sum\tfrac{1}{k}(\alpha^{2k}-\tfrac{1}{2^{2k}})=\ln(\tfrac{3}{4(1-\alpha^2)})$.""",

    # ═══════════════ 2020 SN ═══════════════
    ("C", "math", 2020, "sn", 1): r"""Exercice 1 (3 points)
1. (E) : $13x-15y=5$.
a) Entier p tel que $(p+1;p)$ solution.
b) Résoudre (E).
2. S = $\{N:N\equiv 5\ [13], N\equiv 10\ [15]\}$.
a) (x,y) tel que $N=13x+5=15y+10$.
b) $N\in S\Leftrightarrow N\equiv 70\ [195]$.
c) Plus petit A de S avec $A\ge 2000$.
d) A s'écrit COVID en base n ; déterminer n.""",
    ("C", "math", 2020, "sn", 2): r"""Exercice 2 (4 points)
$P(z)=z^3+(1-2i)z^2-(5+3i)z+4-8i$.
1. $P(-i)$ et solutions.
2. A, B, C images avec $|z_B|<|z_A|<|z_C|$.
a) Placer ; nature de ABC.
b) G barycentre de $\{(A;9),(B;-2),(C;6)\}$ ; $z_G=2i$.
c) $E:9MA^2-2MB^2+6MC^2=195$.
d) $F:3MA^2-5MB^2+2MC^2=65$.
e) Position relative entre E et F.
3. f : $z'=mz+(2-2m)i$, $m\in\mathbb{C}$.
a) Résoudre $z'=z$.
b) m tel que $f(B)=A$ ; caractériser.""",
    ("C", "math", 2020, "sn", 3): r"""Exercice 3 (4 points)
Triangle isocèle direct ABC avec $BC=2a, AB=AC=3a$, $(\vec{AB},\vec{AC})=\theta\ [2\pi]$. $A'$ milieu de [BC], H orthocentre, $B'$ projeté de B sur (AC).
1. Figure.
2.a) $\vec{CA}\cdot\vec{CB}=CA\cdot CB'=CB\cdot CA'$.
2.b) Distance B'C et B'A.
2.c) $\dfrac{\overline{B'A}}{\overline{B'C}}=-\tfrac{7}{2}$ ; $B'=\text{bar}\{(A,2);(C,7)\}$.
2.d) $G=\text{bar}\{(A,1);(B,1);(C,1)\}$ sur hauteurs.
3.a) A, B, $A', B'$ cocycliques ; H, C, $A', B'$ cocycliques.
3.b) Relations d'angles.""",
    ("C", "math", 2020, "sn", 4): r"""Exercice 4 (4 points)
I. $f(x)=x\ln(\tfrac{x+1}{x})$ pour $x>0$, $f(0)=0$, courbe (C).
1.a) Continuité et dérivabilité à droite en 0.
1.b) $f''(x)=\dfrac{-1}{x(x+1)^2}$.
1.c) Variations de $f'$ ; $f'(x)>0$.
2.a) $\lim_{+\infty}f=1$ ; interprétation.
2.b) Tableau de variation ; tracer (C).
II. $g(x)=\dfrac{1}{x}-\ln(\tfrac{x+1}{x})$ sur $]0;+\infty[$.
1.a) $g(n)=\tfrac{1}{n}-\int_n^{n+1}\tfrac{1}{x}\,dx$.
1.b) Encadrement de g(n).
2. $U_n=\sum_{k=n}^{2n}\tfrac{1}{k(k+1)}$.
a) $\sum g(k)\le U_n$.
b) $U_n=\dfrac{n+1}{n(2n+1)}$.
c) $\lim U_n=\tfrac{1}{2}$ ; $\lim\sum g(k)$.""",
    ("C", "math", 2020, "sn", 5): r"""Exercice 5 (5 points)
1. $f(x)=(x+2)e^{-x}$ sur $\mathbb{R}$, courbe (C).
a) Limites et $\tfrac{f}{x}$.
b) Tableau de variation ; tracer (C).
2. g restriction sur $I=[-1;+\infty[$.
a) Bijection sur J.
b) Tracer $(C')$ de $g^{-1}$.
3. $I_n=\int_{-2}^0\dfrac{(x+2)^n e^{-x}}{n!}\,dx$.
a) $0\le\tfrac{(x+2)^n}{n!}e^{-x}\le\tfrac{2^n}{n!}e^2$.
b) Par IPP, $I_1=e^2-3$.
c) $I_{n+1}=I_n-\dfrac{2^{n+1}}{(n+1)!}$ ; $I_n=e^2-U_n$ ; $\lim I_n=0$, $\lim U_n=e^2$.
4. $v_n=\dfrac{2^n}{n!}$ ; $v_{n+1}\le\tfrac{2}{3}v_n$ pour $n\ge 2$ ; $v_n\le 2\cdot(\tfrac{2}{3})^{n-2}e$ ; $\lim v_n=0$.
5. $0\le I_n\le 2e^2 v_n$.""",

    # ═══════════════ 2021 SN ═══════════════
    ("C", "math", 2021, "sn", 1): r"""Exercice 1 (3 points)
A. 1. Reste de 2021 par 11.
2. Reste de $2021^n$ par 11.
3. $2021^{2020}-2021^{1960}$ divisible par 11.
B. N s'écrit xyxy en décimal.
1. N multiple de 101.
2. y pour N multiple de 5.
3. x, y pour N multiple de 20.
C. $M=\begin{pmatrix}x&y\\5&11\end{pmatrix}$, $0<x,y<10$.
1. M inversible ; $M^{-1}$.
2. Valeurs de x, y telles que $\det M=1$.""",
    ("C", "math", 2021, "sn", 2): r"""Exercice 2 (4 points)
Rectangle ABCD de centre O avec $(\vec{AB},\vec{AC})=\tfrac{\pi}{3}\ [2\pi]$. E symétrique de B par (AC), F celui de O par A, I milieu de [OA], J milieu de [OD].
1. Figure soignée.
2. BEF équilatéral direct.
3. O, E, F, B cocycliques ; centre.
4.a) Unique antidéplacement f : $F\to O, A\to D$.
4.b) f symétrie glissante ; forme réduite.
5.a) Unique similitude directe S : $E\to O, B\to C$.
5.b) Rapport et angle.
5.c) Centre sur cercles [OE] et [BC].
5.d) Image de C ; construire K=S(D).
5.e) $(M_n)$ : $M_0=B, M_{n+1}=S(M_n)$ ; $M_{2021}\in[JC]$.""",
    ("C", "math", 2021, "sn", 3): r"""Exercice 3 (5 points)
Plan complexe, A, B d'affixes $-2-i, -1-3i$.
1.a) $-4z^2-(12+16i)z+7-24i=(2iz-4+3i)^2$.
1.b) Solutions de (E) : $z^2-(2m+2+i)z+2m^2+(5+5i)m-1+7i=0$.
2. $S_1:z_1=(1+i)m-1+2i$ et $S_2:z_2=(1-i)m+3-i$.
a) Éléments de $S_1, S_2$.
b) $S_1\circ S_2$ homothétie ; rapport et centre C.
c) R rotation $M_1\to M_2$ ; angle et centre D.
d) Placer A, B, C, D ; nature de ABD.
3. E ellipse de foyers A, B, sommet D.
a) Centre I ; grand axe $\sqrt{10}$.
b) Équation.
c) Construire après sommets.""",
    ("C", "math", 2021, "sn", 4): r"""Exercice 4 (4 points)
$f(x)=1+(x+1)\ln(x+1)-(\ln(x+1))^2$ sur $I=]-1;+\infty[$, courbe (C).
1. Limites.
2. $u(x)=x+1-\ln(x+1)$, $v(x)=x\ln(x+1)$.
a) v positive sur $]-1,0[$ et $]0,+\infty[$.
b) Variations de u ; positive.
c) $f'(x)=\dfrac{u(x)+v(x)}{x+1}$.
d) Tableau de variation.
3. f bijection sur J.
4. $g(x)=f(x)-x$.
a) Variations de g ; $g(x)=0$ admet une unique solution $\alpha$.
b) $-0,7<\alpha<-0,6$ ; position de (C) et $y=x$.
5. Construire $\Delta$, (C), $(C')$.""",
    ("C", "math", 2021, "sn", 5): r"""Exercice 5 (4 points)
$f(0)=0$, $f(x)=\dfrac{e^{1-1/x}}{x^2}$ pour $x>0$, courbe $\Gamma$.
1.a) $\dfrac{e^{1-1/x}}{x^n}=e^{1-1/x+n\ln(1/x)}$ ; $\lim_{0^+}\tfrac{e^{1-1/x}}{x^n}=0$.
1.b) Continuité et dérivabilité à droite en 0.
2.a) $f'(x)=\dfrac{(1-2x)e^{1-1/x}}{x^4}$ ; signe.
2.b) Tableau de variation ; tracer $\Gamma$.
3. Aire A entre $\Gamma$, (Ox), $x=1, x=2$.
4. $I_n=\int_1^2\dfrac{f(x)}{x^n}\,dx$.
a) $I_0=A$.
b) $(I_n)$ décroissante et positive ; convergente.
c) Par IPP, $I_{n+1}-(n+1)I_n=\dfrac{\sqrt{e}}{2^{n+1}}-1$.
d) $0\le I_n\le\dfrac{1}{n}(1-\dfrac{\sqrt{e}}{2^{n+1}})$ ; $\lim I_n=0$.""",
}


_SESSION_MATCH = {"sn": "normal", "sc": "compl"}


def find_entry(data, filiere, matiere, annee, sess_code, ex_num):
    sess_substr = _SESSION_MATCH[sess_code]
    mat_accept = {"pc", "physique", "chimie"} if matiere == "pc" else {matiere}
    candidates = []
    for e in data:
        if e.get("filiere_id") != filiere: continue
        if e.get("matiere_id") not in mat_accept: continue
        if e.get("annee") != annee: continue
        if sess_substr not in str(e.get("session", "")).lower(): continue
        try: num = int(e.get("exercice_numero"))
        except: continue
        if num != ex_num: continue
        candidates.append(e)
    if not candidates: return None
    if len(candidates) == 1: return candidates[0]
    for c in candidates:
        if not c.get("is_skeleton") and (c.get("ennonce_complet") or "").strip(): return c
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
            skipped_missing.append(label); continue
        eid = e.get("id", "?")
        old = (e.get("ennonce_complet") or "").strip()
        if old and len(old) > 100 and not args.force:
            skipped_filled.append((label, eid, len(old))); continue
        e["ennonce_complet"] = ennonce.strip()
        e["is_skeleton"] = False
        e["updated_at"] = now
        updated.append((label, eid, len(old), len(ennonce.strip())))
    print(f"Cible : {len(EXOS)} énoncés.")
    print(f"  → mis à jour    : {len(updated)}")
    print(f"  → introuvables  : {len(skipped_missing)}")
    print(f"  → déjà remplis  : {len(skipped_filled)}")
    if skipped_missing:
        print("\nIntrouvables :")
        for label in skipped_missing: print(f"  {label}")
    if args.dry_run:
        print("\n(--dry-run : aucune écriture)"); return 0
    if not updated:
        print("\nRien à écrire."); return 0
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    shutil.copy2(p, BACKUP_DIR / f"json_bac-pre-fill-c-math-2011-2021-{stamp}.json")
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(p)
    print(f"\n→ {p} mis à jour ({len(updated)} entrées).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
