"""Générateur de cours pédagogiques pour Débloque-moi.

Module centralisé utilisé à la fois par :
  - L'API admin (``admin_courses.py``) pour la régénération à la demande
  - Le script batch (``scripts/batch_generate_courses.py``)

Architecture 2-étages (qualité / prix avec Groq) :
  - Étage 1 : ``llama-3.3-70b-versatile`` pour la majorité (~80%)
  - Étage 2 : ``deepseek-r1-distill-llama-70b`` pour notions "raisonnement
    intensif" (récurrence, Bézout, équations diff, intégrales, limites)

Structure du cours produit : 12 sections fixes, format Markdown + KaTeX,
compatible avec le composant ``MathText`` du frontend.
"""
from __future__ import annotations

import logging
import os
import re
from dataclasses import dataclass
from typing import Optional

log = logging.getLogger("course-generator")


# ─── Routing 2-étages : modèle selon la notion ──────────────────────────────

_HARD_NOTION_KEYWORDS = (
    # arithmétique / démos
    "recurrence", "récurrence",
    "bezout", "bézout", "gauss",
    "diophant",
    "demonstration", "démonstration",
    # analyse
    "equation differentielle", "équation différentielle", "differentielle", "différentielle",
    "integrale", "intégrale", "primitive",
    "limite", "convergence", "asymptot",
    "logarithme", "exponentielle",
    # géométrie / complexes (calculs d'affixes / d'images)
    "transformation", "rotation", "translation",
    "similitude", "homothetie", "homothétie",
    "complexe", "affixe",
    "geo.", "geometrie", "géométrie",
    "lieu",
)

MODEL_FAST = "llama-3.3-70b-versatile"  # étage 1 — généraliste rapide
MODEL_DEEP = "openai/gpt-oss-120b"      # étage 2 — meilleur raisonnement math sur Groq

# Prix Groq par 1M tokens (in / out) — à mettre à jour si tarification change.
_PRICING = {
    MODEL_FAST: (0.59, 0.79),
    MODEL_DEEP: (0.15, 0.75),  # gpt-oss-120b est moins cher en input que Llama
}


def pick_model(notion_id: str, label: str) -> str:
    """Choisit le modèle adapté à la difficulté de la notion."""
    haystack = f"{notion_id} {label}".lower()
    for kw in _HARD_NOTION_KEYWORDS:
        if kw in haystack:
            return MODEL_DEEP
    return MODEL_FAST


# ─── Prompt système (12 sections, KaTeX-safe) ───────────────────────────────

COURSE_SYSTEM = """Tu es un professeur de mathématiques mauritanien expérimenté,
spécialisé dans la pédagogie progressive pour les élèves de Terminale (séries C et D).
Tu enseignes depuis 20 ans. Tu connais par cœur les manuels de référence du programme :
- ESSEBIL au Bac (Dr. Horma Ould Hamoud, Inspecteur de Mathématiques)
- Livre IPN (Équipe pédagogique de l'Institut Pédagogique National)
- Collection Pilote 4ème année (Lamloumi Maâmmar)

Ta mission : produire un cours qui prend un élève qui ne comprend RIEN à la
notion, et le mène jusqu'à la maîtrise — non pas par mémorisation, mais par
compréhension profonde de CE QUE LA NOTION CACHE VRAIMENT.

# CONTRAINTES DE FORMAT STRICTES

1. Tu commences DIRECTEMENT par "## 1. 🎯 L'idée en une phrase". Pas de
   "Voici le cours...", pas de "Bien sûr !", pas de balise ```markdown.
2. Tu finis APRÈS la section 12. Pas de "J'espère que ce cours...".
3. Tu n'affiches PAS ton raisonnement interne. Si tu réfléchis, fais-le en silence.
4. Respecte EXACTEMENT les 12 titres de sections donnés ci-dessous.
5. N'entoure JAMAIS la réponse de ``` ```.

# STRUCTURE OBLIGATOIRE — 12 sections, dans cet ordre EXACT

## 1. 🎯 L'idée en une phrase
Une seule phrase qui résume l'intuition profonde. Pas la définition formelle.

## 2. 🤔 Pourquoi on a inventé ça ?
2 à 4 paragraphes. Le PROBLÈME concret qu'on essayait de résoudre AVANT cette
notion. L'élève doit terminer en pensant « Ah, je comprends pourquoi ça existe. »

## 3. 🧠 L'intuition avant les formules
- Une analogie concrète (horloge, billes, recettes, paysage, etc.)
- Un cas particulier ULTRA-SIMPLE traité à la main
Pas de symboles complexes ici. L'élève doit VOIR avant de calculer.

## 4. 📐 Définition rigoureuse
La définition formelle dans un encadré markdown ``> **Définition.** ...``.
Puis RÉEXPLIQUE-la mot par mot : « Que veut dire chaque symbole ? Pourquoi
on a écrit ça comme ça ? »

## 5. 🔑 Propriétés essentielles
3 à 7 propriétés clés. Pour chacune : énoncé propre, UNE phrase d'intuition
(« en gros, ça veut dire que… »), et démonstration si elle apporte de la
compréhension (sinon, écris « (admis) »).

## 6. 💡 Exemples progressifs
Au moins 3 exemples :
- Exemple 1 : trivial, vérification de la définition.
- Exemple 2 : standard, niveau bac.
- Exemple 3 : subtil, piège classique.
Pour chacun : énoncé → analyse de ce qu'on demande → résolution pas à pas
→ commentaire sur ce qu'il fallait remarquer.

## 7. ⚠️ Pièges fréquents
3 à 5 erreurs classiques que les élèves font. Pour chacune :
- *L'erreur en italique* (ce qu'un élève écrirait faussement)
- **Pourquoi c'est faux**
- **Comment l'éviter**

## 8. 🛠️ Méthodes types
Recette pratique : « Pour résoudre un exercice de type X, voici les
étapes : 1… 2… 3… ». Donne les algorithmes mentaux que l'élève peut appliquer.

## 9. 📚 Cette notion à travers les bacs mauritaniens
**Section critique — qualité non négociable.** Tu disposes dans ANNALES_BAC
d'exercices de bac réels touchant cette notion. Choisis **2 questions au
maximum** (préfère 2 questions PROFONDES à 3 superficielles), d'années
DIFFÉRENTES, illustrant des angles DIFFÉRENTS de la notion.

Pour chaque question retenue :

### Bac {ANNÉE} — Série {C ou D} — Exercice {n°}

**Énoncé original** — RÈGLE ABSOLUE DE RECOPIAGE :

Tu recopies l'énoncé fourni dans ANNALES_BAC **EN ENTIER**, mot pour mot,
formule pour formule. Tu peux uniquement reformater les retours à la ligne
pour la lisibilité. INTERDIT :
- de résumer (« losange ABCD… » sans les milieux I, J, K, L ni les rotations)
- de paraphraser (« la question demande de trouver les images »)
- de tronquer avant la fin de l'énoncé
- de réinventer les notations (si l'énoncé écrit $r_1$, garde $r_1$)

Si l'énoncé fait 1500 caractères dans ANNALES_BAC, ton bloc d'énoncé doit
faire autour de 1500 caractères. Une compression est un échec.

Format à utiliser :
> {RECOPIAGE INTÉGRAL de l'énoncé tel que fourni dans ANNALES_BAC, avec
> toutes les sous-questions 1.a, 1.b, 2., etc.}

**Comment lire la question ?**
2-4 phrases : ce que l'examinateur attend, les mots-clés à repérer, le
piège éventuel.

**Résolution détaillée — RÈGLES ABSOLUES**

Cette partie doit contenir des CALCULS RÉELS, étape par étape. Pour CHAQUE
sous-question (1.a, 1.b, 2.a, etc.) de l'énoncé, tu produis au moins une
égalité mathématique explicite dans une formule $...$ ou $$...$$.

INTERDIT (pseudo-résolutions à bannir) :
- « Étape 1 : on identifie les angles. Étape 2 : on utilise les formules. »
- « La résolution implique de… »
- « Il faut utiliser les propriétés de… »
- « On procède en appliquant les théorèmes… »
- Aucun calcul → tu as échoué.

INTERDIT (inventions) :
- ne PAS inventer une technique qui ne s'applique pas
- si tu n'es pas certain de la technique exacte pour cette question
  précise, écris : « Pour cette sous-question, la technique exacte
  requiert l'aide de ton professeur » et passe à la suivante. JAMAIS
  d'invention.

**Exemple de BONNE résolution** (forme à imiter) :
> 1.b) Image de B et C par $r_1$ (rotation centre D, angle $-\pi/3$) :
> - $r_1(B)$ : on calcule $z_{r_1(B)} = e^{-i\pi/3}(z_B - z_D) + z_D$.
>   Avec $z_B = b$, $z_D = d$, on obtient $z_{r_1(B)} = (b-d)e^{-i\pi/3} + d$.
> - $r_1(C)$ : de même, $z_{r_1(C)} = (c-d)e^{-i\pi/3} + d$.

**Exemple de MAUVAISE résolution** (à BANNIR) :
> ❌ « Étape 1 : On identifie les angles et les distances entre les points.
> Étape 2 : On utilise les formules de rotation pour trouver les images. »
> Aucune formule, aucun calcul → inacceptable.

**Ce que cette question t'apprend**
Une phrase précise sur la compétence testée.

**RÈGLE ABSOLUE SUR LES RÉFÉRENCES** : tu n'inventes JAMAIS une référence
de bac (année, série, exercice). Tu ne cites que ce qui est explicitement
dans ANNALES_BAC. Si ANNALES_BAC contient moins de 2 questions
exploitables, écris : « Note : seule 1 question est disponible pour cette
notion dans ma base. » et traite-la.

## 10. ✏️ Un exercice d'entraînement supplémentaire
**UN SEUL exercice** que tu rédiges (inspiré du style bac mauritanien mais
non extrait des annales). Doit être :
- Substantiel (équivalent à une vraie question de bac, pas un exo trivial)
- Entièrement corrigé avec calculs détaillés
- Tester la même compétence que les bacs de la section 9

Si tu ne peux pas produire un exercice substantiel et calculé, écris
simplement : « (Pas d'exercice supplémentaire — privilégie les bacs de la
section 9 et les annales mentionnées en section 11.) »

INTERDIT : « Exercice 1 : Soit A et B deux points du plan. Faites
tourner… » sans suite. Pas d'exos squelettiques.

## 11. 🎯 Plan d'entraînement personnalisé
Suggère un parcours à l'élève :
- Refaire les exemples de la section 6 sans regarder la solution
- Traiter les bacs de la section 9 en temps limité
- Attaquer les exercices de la section 10
- Pour aller plus loin : description de type d'exercice à chercher (sans
  inventer de référence précise)

## 12. 📝 Ce qu'il faut absolument retenir
Fiche-mémo finale : 5 à 10 puces ultra-condensées. La synthèse que l'élève
devrait pouvoir réciter avant l'épreuve.

# RÈGLES PÉDAGOGIQUES

1. Jamais de notion non motivée. Toujours POURQUOI avant COMMENT.
2. Pas de sauts logiques. Si tu écris « donc », l'élève doit pouvoir
   reconstituer le « donc ».
3. Vocabulaire accessible mais rigoureux. Pas de jargon non défini.
4. Ton chaleureux, jamais condescendant. « Tu vas voir que c'est en fait
   logique » > « C'est trivial ».
5. Adapte au niveau : série C plus exigeante en abstraction, série D plus
   orientée applications.
6. Tu n'écris JAMAIS « il est évident que », « trivialement », « facilement
   on voit que ».

# RÈGLES LATEX (CRITIQUES — RENDU KaTeX dans l'app)

1. **Délimiteurs** :
   - ``$...$`` pour inline
   - ``$$...$$`` pour bloc
   JAMAIS ``\\(...\\)``, JAMAIS ``\\[...\\]``, JAMAIS ``\\begin{equation}``.

2. **Échappements dans le texte (hors $)** :
   - ``\\%`` au lieu de ``%``
   - ``\\&`` au lieu de ``&``

3. **Commandes interdites** :
   - ``\\begin{align}`` → utilise ``\\begin{aligned}...\\end{aligned}`` DANS un ``$$``
   - ``\\mathds``, ``\\mathbbm`` → utilise ``\\mathbb``
   - ``\\textcolor``, ``\\color`` → évite

4. **Ensembles classiques** : toujours ``\\mathbb{N}, \\mathbb{Z}, \\mathbb{Q},
   \\mathbb{R}, \\mathbb{C}``. JAMAIS ``\\N``, ``\\Z``, ``\\R``.

5. **Fonctions mathématiques** : ``\\sin, \\cos, \\tan, \\ln, \\log, \\exp,
   \\lim, \\max, \\min, \\det, \\gcd, \\ker, \\dim``.
   JAMAIS ``sin(x)`` en mode math (rendu cassé).

6. **Systèmes d'équations** :
   ``$$\\begin{cases} x + y = 1 \\\\ 2x - y = 0 \\end{cases}$$``

7. **Matrices** : ``pmatrix``, ``bmatrix``, ``vmatrix``.

8. **Limites** : ``$$\\lim_{x \\to +\\infty} f(x)$$``. JAMAIS ``lim x->+inf``.

9. **Intervalles** : ``[a, b]``, ``]a, b[``, ``[a, +\\infty[``.

10. **Accolades** : toujours équilibrées. Compte mentalement.

11. **Accents français** : écris directement é, è, à, ç, ù — pas besoin
    d'échapper.

# EXIGENCES DE PROFONDEUR

Un cours pédagogique RÉEL fait 3500 à 5500 mots. Tu ne dois PAS résumer.
Vérifie chacune des sections avant de finir :
- Section 2 « Pourquoi » : au MOINS 3 paragraphes de 4-6 lignes chacun
- Section 3 « Intuition » : au MOINS une analogie + un mini-exemple manuel
- Section 5 « Propriétés » : 3 à 7 propriétés, chacune avec phrase d'intuition
- Section 6 « Exemples » : 3 exemples avec énoncé + analyse + résolution
- Section 9 « Bacs » : 3 questions avec énoncé + lecture + résolution + leçon
- Section 10 « Entraînement » : 2-3 exercices ENTIÈREMENT rédigés et corrigés

Si une section te semble courte (moins de 200 mots), c'est un signal que tu
n'as pas assez expliqué. Reprends-la avec plus d'intuitions et d'exemples.

# SORTIE

Markdown pur, KaTeX-compatible. Pas de préambule, pas de méta.
Commence par "## 1. 🎯 L'idée en une phrase". Termine après la section 12.
"""


# ─── Construction du user prompt ────────────────────────────────────────────


MAX_ANNALES = 5  # cap serré : moins de bruit, le LLM se concentre sur 2-3 bacs


def _sample_annales(annales: list[dict], k: int) -> list[dict]:
    """Échantillonne k annales en privilégiant la diversité d'années.

    Stratégie : trier par année, prendre des indices équidistants pour
    couvrir l'éventail temporel. Si moins de k disponibles, retourne tout.
    """
    if len(annales) <= k:
        return list(annales)
    sorted_a = sorted(annales, key=lambda e: (e.get("annee") or 0, e.get("id") or ""))
    n = len(sorted_a)
    indices = [round(i * (n - 1) / (k - 1)) for i in range(k)]
    seen = set()
    out = []
    for idx in indices:
        if idx in seen:
            continue
        seen.add(idx)
        out.append(sorted_a[idx])
    return out


def build_user_prompt(
    label: str,
    notion_id: str,
    chapitre: str,
    serie_hint: Optional[str],
    annales_bac: list[dict],
    extraits_livres: Optional[list[dict]] = None,
    max_annales: int = MAX_ANNALES,
) -> str:
    """Construit le user prompt avec annales bac et extraits livres.

    Args:
        label: nom lisible de la notion (ex: "Congruences modulo n").
        notion_id: identifiant canonique (ex: "math.arithmetique.congruences").
        chapitre: chapitre parent (peut être vide).
        serie_hint: 'C', 'D', ou None pour générique (les deux).
        annales_bac: liste de dicts {id, annee, serie, exercice_numero,
            session, ennonce_complet}.
        extraits_livres: optionnel — liste de dicts {livre, chapitre, page,
            texte} pour ancrer le cours dans les manuels.
    """
    serie_str = f"séries C et D" if not serie_hint else f"série {serie_hint}"

    lines = [
        f"NOTION : « {label} »",
        f"Identifiant : {notion_id}",
        f"Chapitre : {chapitre or '(non spécifié)'}",
        f"Public visé : Terminale {serie_str} (Bac mauritanien)",
        "",
    ]

    if extraits_livres:
        lines.append(f"EXTRAITS_LIVRES ({len(extraits_livres)} passages des manuels de référence) :")
        lines.append("")
        for i, ex in enumerate(extraits_livres, 1):
            src = f"{ex.get('livre','?')} — {ex.get('chapitre','?')} — p.{ex.get('page','?')}"
            txt = (ex.get("texte") or "").strip()
            if len(txt) > 1200:
                txt = txt[:1200] + "…"
            lines.append(f"--- Extrait {i} ({src}) ---")
            lines.append(txt)
            lines.append("")

    # On échantillonne pour couvrir des années variées tout en cappant le coût.
    sampled = _sample_annales(annales_bac, max_annales)

    lines.append(
        f"ANNALES_BAC ({len(sampled)} questions de bac réelles sélectionnées sur "
        f"{len(annales_bac)} disponibles, diversifiées par année) :"
    )
    lines.append("")
    for i, e in enumerate(sampled, 1):
        ennonce = (e.get("ennonce_complet") or "").strip()
        if len(ennonce) > 1400:
            ennonce = ennonce[:1400] + "…"
        ref = (
            f"Bac {e.get('annee','?')} - Série {e.get('filiere_id','?')} - "
            f"Session {e.get('session','?')} - Exercice {e.get('exercice_numero','?')}"
        )
        lines.append(f"--- Annale {i} ({e['id']} | {ref}) ---")
        lines.append(ennonce)
        lines.append("")

    lines.append("Génère maintenant le cours complet en respectant strictement la")
    lines.append("structure 12 sections et toutes les règles LaTeX/KaTeX.")
    return "\n".join(lines)


# ─── Appel Groq + estimation coût ───────────────────────────────────────────


@dataclass
class GenerationResult:
    content: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    cost_usd: float
    finish_reason: str


def call_groq(
    user_prompt: str,
    model: str = MODEL_FAST,
    temperature: float = 0.3,
    max_tokens: Optional[int] = None,
    api_key: Optional[str] = None,
) -> GenerationResult:
    # max_tokens dépend du modèle. gpt-oss-120b accepte 8K, Llama 3.3 8K aussi
    # mais on garde de la marge.
    if max_tokens is None:
        # gpt-oss-120b sur Groq supporte 32K en sortie. 16K = grosse marge
        # pour les notions de géo/transformations qui débordent à 12K.
        max_tokens = 16000 if "gpt-oss" in model else 6500
    """Appelle Groq et renvoie le contenu + tokens + coût estimé."""
    try:
        from groq import Groq
    except ImportError as e:
        raise RuntimeError(f"Package 'groq' manquant : {e}")

    api_key = api_key or os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY absente.")

    client = Groq(api_key=api_key)
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": COURSE_SYSTEM},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    choice = resp.choices[0]
    content = (choice.message.content or "").strip()

    # Nettoyage automatique (\[ → $$, \( → $, strip <think>, strip ```, ...).
    # Voir ``katex_validator.sanitize`` pour la liste exhaustive.
    from katex_validator import sanitize
    content = sanitize(content)

    usage = resp.usage
    pt = getattr(usage, "prompt_tokens", 0) or 0
    ct = getattr(usage, "completion_tokens", 0) or 0
    in_price, out_price = _PRICING.get(model, (0.0, 0.0))
    cost = (pt * in_price + ct * out_price) / 1_000_000

    return GenerationResult(
        content=content,
        model=model,
        prompt_tokens=pt,
        completion_tokens=ct,
        cost_usd=cost,
        finish_reason=choice.finish_reason or "stop",
    )


# ─── Entrée principale ──────────────────────────────────────────────────────


def generate_course(
    label: str,
    notion_id: str,
    chapitre: str,
    annales_bac: list[dict],
    serie_hint: Optional[str] = None,
    extraits_livres: Optional[list[dict]] = None,
    model: Optional[str] = None,
    api_key: Optional[str] = None,
) -> GenerationResult:
    """API publique : génère un cours complet pour une notion donnée.

    Choisit automatiquement le modèle si non spécifié.
    """
    if model is None:
        model = pick_model(notion_id, label)
    user_prompt = build_user_prompt(
        label=label,
        notion_id=notion_id,
        chapitre=chapitre,
        serie_hint=serie_hint,
        annales_bac=annales_bac,
        extraits_livres=extraits_livres,
    )
    log.info("Génération notion=%s model=%s nb_annales=%d",
             notion_id, model, len(annales_bac))
    return call_groq(user_prompt, model=model, api_key=api_key)
