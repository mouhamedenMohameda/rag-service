"""Validateur + sanitizer KaTeX/Markdown pour les cours générés.

Détecte les erreurs de rendu courantes AVANT de servir un cours à l'élève.
Stratégie : pas de parsing complet — uniquement des heuristiques regex
robustes qui couvrent 95% des erreurs réelles.

Inclut aussi ``sanitize()`` qui corrige automatiquement les erreurs
mécaniques avant validation finale.

Catégories d'erreurs détectées :
  - Délimiteurs ``$`` non appariés (compte les ``$`` libres, hors ``$$``)
  - ``$$`` non appariés
  - ``\\begin{X}`` sans ``\\end{X}`` correspondant
  - Commandes LaTeX interdites par KaTeX (``\\(...``, ``\\[...``, ``\\mathds``)
  - Ensembles raccourcis non rendus (``\\N``, ``\\Z``, ``\\R``)
  - Sections manquantes (vérifie les 12 sections obligatoires)
  - Blocs de code accidentels autour du markdown (``` au début/fin)
  - Restes de ``<think>`` non strippés (DeepSeek)
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# Sections obligatoires (recherche par titre, insensible à la casse de l'emoji)
REQUIRED_SECTIONS = [
    r"##\s*1\.\s*🎯",
    r"##\s*2\.\s*🤔",
    r"##\s*3\.\s*🧠",
    r"##\s*4\.\s*📐",
    r"##\s*5\.\s*🔑",
    r"##\s*6\.\s*💡",
    r"##\s*7\.\s*⚠️",
    r"##\s*8\.\s*🛠️",
    r"##\s*9\.\s*📚",
    r"##\s*10\.\s*✏️",
    r"##\s*11\.\s*🎯",
    r"##\s*12\.\s*📝",
]

# Commandes interdites par KaTeX (qui font planter le rendu)
FORBIDDEN_PATTERNS = [
    (r"\\mathds\b",       "Commande \\mathds non supportée par KaTeX → utilise \\mathbb"),
    (r"\\mathbbm\b",      "Commande \\mathbbm non supportée → utilise \\mathbb"),
    (r"\\textcolor\b",    "Commande \\textcolor non supportée"),
    (r"\\color\b",        "Commande \\color non supportée"),
    (r"\\begin\{equation\}", "Utilise $$...$$ au lieu de \\begin{equation}"),
    (r"\\begin\{align\}\b",  "Utilise \\begin{aligned}...\\end{aligned} DANS $$...$$"),
    (r"\\\(",             "Délimiteur \\( interdit → utilise $...$"),
    (r"\\\[",             "Délimiteur \\[ interdit → utilise $$...$$"),
]

# Raccourcis d'ensembles non valides
SET_SHORTCUT_PATTERNS = [
    (r"(?<!\\mathbb\{)\\N(?![a-zA-Z])",  "\\N → utilise \\mathbb{N}"),
    (r"(?<!\\mathbb\{)\\Z(?![a-zA-Z])",  "\\Z → utilise \\mathbb{Z}"),
    (r"(?<!\\mathbb\{)\\R(?![a-zA-Z])",  "\\R → utilise \\mathbb{R}"),
    (r"(?<!\\mathbb\{)\\Q(?![a-zA-Z])",  "\\Q → utilise \\mathbb{Q}"),
    (r"(?<!\\mathbb\{)\\C(?![a-zA-Z])",  "\\C → utilise \\mathbb{C}"),
]


@dataclass
class ValidationReport:
    ok: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def fail(self, msg: str) -> None:
        self.ok = False
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def summary(self) -> str:
        if self.ok and not self.warnings:
            return "✅ OK"
        parts = []
        if self.errors:
            parts.append(f"❌ {len(self.errors)} erreur(s) :")
            parts.extend(f"   - {e}" for e in self.errors)
        if self.warnings:
            parts.append(f"⚠️  {len(self.warnings)} avertissement(s) :")
            parts.extend(f"   - {w}" for w in self.warnings)
        return "\n".join(parts)


def _strip_inline_code(text: str) -> str:
    """Retire les blocs de code (```...```) et inline code (`...`) du texte,
    car les ``$`` à l'intérieur ne sont pas des délimiteurs maths."""
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def _count_unescaped(text: str, char: str) -> int:
    """Compte les occurrences de ``char`` non précédées de ``\\``."""
    count = 0
    i = 0
    while i < len(text):
        if text[i] == char and (i == 0 or text[i - 1] != "\\"):
            count += 1
        i += 1
    return count


def sanitize(content: str) -> str:
    """Corrige automatiquement les erreurs mécaniques courantes.

    Conversions effectuées :
      - ``\\[...\\]`` (bloc MathJax) → ``$$...$$``  (bloc KaTeX)
      - ``\\(...\\)`` (inline MathJax) → ``$...$``  (inline KaTeX)
      - Strip d'éventuel ``` ``` autour du markdown
      - Strip de balises ``<think>...</think>`` résiduelles
      - Strip de phrases conversationnelles en préambule

    Ne touche PAS au contenu mathématique lui-même, uniquement aux
    délimiteurs et au boilerplate.
    """
    if not content:
        return content

    # 1. Strip <think>...</think> (DeepSeek/raisonnement)
    if "<think>" in content:
        m = re.search(r"</think>\s*(.*)", content, re.DOTALL)
        content = m.group(1).strip() if m else re.sub(r"<think>.*", "", content, flags=re.DOTALL).strip()

    # 2. Strip ``` enveloppant
    stripped = content.strip()
    if stripped.startswith("```"):
        first_nl = stripped.find("\n")
        if first_nl > 0:
            stripped = stripped[first_nl + 1:]
        if stripped.rstrip().endswith("```"):
            stripped = stripped.rstrip()[:-3].rstrip()
        content = stripped

    # 3. Convertir \[...\] → $$...$$ et \(...\) → $...$
    # Note : on cible spécifiquement \[ et \( en tant que paires.
    content = re.sub(r"\\\[", "$$", content)
    content = re.sub(r"\\\]", "$$", content)
    content = re.sub(r"\\\(", "$", content)
    content = re.sub(r"\\\)", "$", content)

    # 4. Strip préambules conversationnels
    bad_starts = (
        "Voici le cours",
        "Voici un cours",
        "Bien sûr",
        "D'accord",
        "Parfait",
        "Je vais",
    )
    lines = content.lstrip().split("\n")
    while lines and any(lines[0].startswith(p) for p in bad_starts):
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
    content = "\n".join(lines)

    return content.strip()


def validate(content: str) -> ValidationReport:
    """Valide un cours markdown généré. Renvoie un ``ValidationReport``."""
    report = ValidationReport()

    if not content or not content.strip():
        report.fail("Contenu vide")
        return report

    # 1. Restes de <think> non strippés
    if "<think>" in content or "</think>" in content:
        report.fail("Balise <think> non strippée (sortie DeepSeek mal nettoyée)")

    # 2. Bloc ``` autour du markdown
    stripped = content.strip()
    if stripped.startswith("```"):
        report.fail("Cours entouré de ``` au début (à nettoyer)")
    if stripped.endswith("```") and not stripped.startswith("```"):
        report.fail("Cours terminé par ``` (à nettoyer)")

    # 3. Apparenge des $$
    code_free = _strip_inline_code(content)
    double_dollars = code_free.count("$$")
    if double_dollars % 2 != 0:
        report.fail(f"$$ non appariés ({double_dollars} occurrences impaires)")

    # 4. Apparenge des $ (après avoir retiré $$)
    no_double = code_free.replace("$$", "")
    single_dollars = _count_unescaped(no_double, "$")
    if single_dollars % 2 != 0:
        report.fail(f"$ non appariés ({single_dollars} occurrences impaires)")

    # 5. \begin / \end appariés
    begins = re.findall(r"\\begin\{([a-zA-Z*]+)\}", content)
    ends = re.findall(r"\\end\{([a-zA-Z*]+)\}", content)
    from collections import Counter
    b_count, e_count = Counter(begins), Counter(ends)
    for env in set(begins) | set(ends):
        if b_count[env] != e_count[env]:
            report.fail(
                f"Environnement '{env}' non équilibré : "
                f"{b_count[env]} \\begin / {e_count[env]} \\end"
            )

    # 6. Commandes interdites
    for pattern, msg in FORBIDDEN_PATTERNS:
        if re.search(pattern, content):
            report.fail(msg)

    # 7. Raccourcis d'ensembles
    for pattern, msg in SET_SHORTCUT_PATTERNS:
        if re.search(pattern, content):
            report.warn(msg)

    # 8. Sections obligatoires
    missing = []
    for i, pat in enumerate(REQUIRED_SECTIONS, 1):
        if not re.search(pat, content):
            missing.append(f"Section {i}")
    if missing:
        report.fail(f"Sections manquantes : {', '.join(missing)}")

    # 9. Préambules indésirables
    first_line = content.strip().split("\n", 1)[0]
    bad_starts = ("Voici", "Bien sûr", "D'accord", "Parfait", "Je vais")
    if any(first_line.startswith(p) for p in bad_starts):
        report.fail(f"Préambule conversationnel détecté : '{first_line[:50]}…'")

    # 10. Accolades évidemment non équilibrées (heuristique simple — mode math)
    # On compte hors-code uniquement.
    open_b = code_free.count("{")
    close_b = code_free.count("}")
    if abs(open_b - close_b) > 2:  # tolère léger bruit (texte avec accolades)
        report.warn(
            f"Accolades possiblement déséquilibrées : "
            f"{open_b} '{{' vs {close_b} '}}'"
        )

    return report


# ─── CLI utilitaire ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python katex_validator.py <fichier.md>")
        sys.exit(1)
    text = open(sys.argv[1], encoding="utf-8").read()
    rep = validate(text)
    print(rep.summary())
    sys.exit(0 if rep.ok else 1)
