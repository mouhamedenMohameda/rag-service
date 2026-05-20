"""Taxonomie figée des chapitres + notions clés du programme Sciences
Physiques Bac Mauritanien (séries C et D).

Cette liste est la **source de vérité** : tout exercice PC sera classifié
DANS un chapitre ci-dessous, avec **3 à 6 notions** sélectionnées parmi
celles du chapitre choisi. Aucun chapitre ou notion hors-liste n'est
autorisé. Cela garantit la cohérence d'année en année et permettra plus
tard de regrouper les exos par chapitre dans le RAG (Phase 3 — few-shot
prof IPN).

Pour ajouter un chapitre ou une notion : édite ce fichier et relance le
classifieur. Les anciennes classifications restent valides tant que le
chapitre/notion n'a pas été renommé.
"""
from __future__ import annotations

# ─── Chimie ──────────────────────────────────────────────────────────────────

CHIMIE: dict[str, list[str]] = {
    "Cinétique chimique": [
        "Vitesse instantanée de formation",
        "Vitesse instantanée de disparition",
        "Vitesse moyenne",
        "Facteurs cinétiques",
        "Trempe thermique",
        "Catalyseur",
        "Loi de vitesse",
        "Ordre de réaction",
        "Temps de demi-réaction",
        "Équation bilan",
        "Suivi par dosage",
        "Méthode de la trempe",
    ],
    "Acides et Bases": [
        "pH",
        "pKa",
        "Constante d'acidité Ka",
        "Acide fort",
        "Acide faible",
        "Base forte",
        "Base faible",
        "Monoacide",
        "Polyacide",
        "Dosage acide-base",
        "Équivalence",
        "Demi-équivalence",
        "Indicateur coloré",
        "Espèces majoritaires",
        "Diagramme de prédominance",
        "Couple acide/base",
    ],
    "Solutions tampons": [
        "Effet tampon",
        "Mélange équimolaire",
        "pH constant",
        "Capacité tampon",
        "Préparation d'une solution tampon",
        "pKa du couple",
    ],
    "Chimie Organique - Alcools et dérivés": [
        "Alcool primaire",
        "Alcool secondaire",
        "Alcool tertiaire",
        "Oxydation ménagée",
        "Aldéhyde",
        "Cétone",
        "Acide carboxylique",
        "Test à la DNPH",
        "Liqueur de Fehling",
        "Réactif de Tollens",
        "Tests caractéristiques",
        "Nomenclature",
        "Identification",
    ],
    "Chimie Organique - Esters": [
        "Acide carboxylique",
        "Alcool",
        "Réaction d'estérification",
        "Hydrolyse d'un ester",
        "Équilibre chimique",
        "Rendement",
        "Catalyseur acide",
        "Réaction limitée",
        "Anhydride d'acide",
        "Chlorure d'acyle",
        "Nomenclature des esters",
    ],
    "Chimie Organique - Amines et amides": [
        "Amine primaire",
        "Amine secondaire",
        "Amine tertiaire",
        "Amide",
        "Acylation",
        "Anhydride éthanoïque",
        "Nomenclature des amines",
        "Identification",
        "Basicité des amines",
    ],
    "Chimie Organique - Hydrocarbures": [
        "Alcanes",
        "Alcènes",
        "Alcynes",
        "Nomenclature",
        "Isomérie",
        "Combustion",
        "Halogénation",
        "Hydrogénation",
        "Polymérisation",
    ],
    "Oxydoréduction et piles": [
        "Couple oxydant/réducteur",
        "Demi-équation électronique",
        "Équation bilan",
        "Potentiel standard E°",
        "Pile électrochimique",
        "Pont salin",
        "Force électromotrice",
        "Loi de Nernst",
        "Électrolyse",
    ],
}

# ─── Physique ────────────────────────────────────────────────────────────────

PHYSIQUE: dict[str, list[str]] = {
    "Mécanique de Newton": [
        "Référentiel galiléen",
        "Première loi de Newton",
        "Deuxième loi de Newton (RFD)",
        "Troisième loi de Newton",
        "Mouvement rectiligne uniforme",
        "Mouvement rectiligne uniformément varié",
        "Mouvement circulaire uniforme",
        "Chute libre",
        "Frottements",
        "Plan incliné",
        "Théorème de l'énergie cinétique",
        "Travail d'une force",
        "Énergie potentielle",
        "Énergie mécanique",
    ],
    "Gravitation et Satellites": [
        "Loi de gravitation universelle",
        "Champ de gravitation",
        "Satellite géostationnaire",
        "Période orbitale",
        "Troisième loi de Kepler",
        "Vitesse orbitale",
        "Énergie d'un satellite",
        "Orbite circulaire",
        "Lune",
        "Masse de la Terre",
    ],
    "Oscillations mécaniques": [
        "Pendule simple",
        "Pendule pesant",
        "Ressort horizontal",
        "Ressort vertical",
        "Pulsation propre",
        "Période propre",
        "Équation différentielle du mouvement",
        "Amortissement",
        "Conservation de l'énergie mécanique",
        "Énergie potentielle élastique",
        "Énergie cinétique",
        "Oscillations forcées",
        "Résonance mécanique",
    ],
    "Oscillations électriques (RLC)": [
        "Circuit RLC série",
        "Pulsation propre",
        "Pulsation de résonance",
        "Impédance",
        "Déphasage",
        "Résonance d'intensité",
        "Surtension",
        "Bande passante",
        "Facteur de qualité",
        "Énergie dans une bobine",
        "Énergie dans un condensateur",
        "Construction de Fresnel",
    ],
    "Auto-induction": [
        "Bobine",
        "Inductance",
        "Tension d'auto-induction",
        "Loi de Lenz",
        "Circuit RL",
        "Constante de temps",
        "Établissement du courant",
        "Rupture du courant",
        "Énergie magnétique",
    ],
    "Champ magnétique": [
        "Force de Laplace",
        "Champ magnétique uniforme",
        "Particule chargée en mouvement",
        "Force de Lorentz",
        "Rails de Laplace",
        "Spectromètre de masse",
        "Cyclotron",
        "Sélecteur de vitesse",
        "Solénoïde",
        "Bobines de Helmholtz",
        "Règle de la main droite",
    ],
    "Champ électrique et Condensateurs": [
        "Condensateur plan",
        "Capacité",
        "Charge d'un condensateur",
        "Décharge d'un condensateur",
        "Tension aux bornes",
        "Énergie emmagasinée",
        "Circuit RC",
        "Constante de temps",
        "Champ électrique uniforme",
        "Mouvement d'une particule chargée",
    ],
    "Optique géométrique": [
        "Lentille convergente",
        "Lentille divergente",
        "Distance focale",
        "Vergence",
        "Image réelle",
        "Image virtuelle",
        "Grandissement",
        "Relation de conjugaison",
        "Construction géométrique",
    ],
    "Ondes et Lumière": [
        "Onde mécanique progressive",
        "Onde sinusoïdale",
        "Longueur d'onde",
        "Période",
        "Célérité",
        "Interférences lumineuses",
        "Fentes d'Young",
        "Diffraction",
        "Spectre",
        "Photon",
        "Effet photoélectrique",
        "Niveaux d'énergie",
    ],
    "Physique Nucléaire": [
        "Radioactivité alpha",
        "Radioactivité bêta moins",
        "Radioactivité bêta plus",
        "Radioactivité gamma",
        "Demi-vie",
        "Constante radioactive",
        "Activité radioactive",
        "Décroissance radioactive",
        "Énergie de liaison",
        "Défaut de masse",
        "Fusion nucléaire",
        "Fission nucléaire",
        "Réaction nucléaire",
        "Conservation du nombre de masse",
        "Conservation du nombre de charge",
        "Datation au carbone 14",
    ],
}

# Union complète pour le classifieur
ALL_PC: dict[str, list[str]] = {**CHIMIE, **PHYSIQUE}


def all_chapters() -> list[str]:
    return list(ALL_PC.keys())


def notions_for(chapter: str) -> list[str]:
    return ALL_PC.get(chapter, [])


def validate(chapter: str, notions: list[str]) -> tuple[bool, str]:
    """Vérifie que le chapitre existe et que toutes les notions sont
    autorisées pour ce chapitre. Retourne (ok, message_erreur)."""
    if chapter not in ALL_PC:
        return False, f"Chapitre '{chapter}' non dans la taxonomie"
    allowed = set(ALL_PC[chapter])
    bad = [n for n in notions if n not in allowed]
    if bad:
        return False, f"Notions non autorisées pour {chapter} : {bad}"
    if not 1 <= len(notions) <= 6:
        return False, f"{len(notions)} notions (attendu : 1 à 6)"
    return True, ""
