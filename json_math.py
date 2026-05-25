"""Construit /Users/mohameda/Documents/Bac/rag-service/json_math.json
en fusionnant les énoncés extraits 2007-2014 avec les corrections refaites
par Claude. Format compatible avec json_bac.json.

Strategie:
- Source des énoncés: math_c_2007sc_2012sc.json + math_c_2014.json
- Corrections: ce module enregistre des entrées CORRECTIONS[id] = correction_str
- Sortie: json_math.json (liste d'objets aux clés compatibles json_bac.json)
"""
import json, datetime, pathlib

ROOT = pathlib.Path(__file__).parent
SRC1 = ROOT / "exo_extracted" / "math_c_2007sc_2012sc.json"
SRC2 = ROOT / "exo_extracted" / "math_c_2014.json"
OUT  = ROOT / "json_math.json"

# Importe les corrections refaites depuis le module corrections_math.py
import sys
sys.path.insert(0, str(ROOT))
from corrections_math import CORRECTIONS

src = json.loads(SRC1.read_text()) + json.loads(SRC2.read_text())

now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

out = []
for ex in src:
    eid = ex["id"]
    if eid not in CORRECTIONS:
        continue  # pas encore refait
    entry = {
        "id": eid,
        "matiere_id": "math",
        "matiere": "Mathématiques",
        "filiere_id": ex.get("filiere_id", "C"),
        "filiere": ex.get("filiere", "Série C"),
        "annee": ex["annee"],
        "session": ex["session"],
        "fichier": ex.get("fichier", ""),
        "exercice_numero": ex["exercice_numero"],
        "ennonce_complet": ex["ennonce_complet"],
        "correction": CORRECTIONS[eid],
        "correction_source": "claude-opus-4-7 rewrite",
        "correction_quality": "claude_rewritten_v1",
        "_corrected_at": now,
        "_source_pages_enonce": ex.get("_source_pages_enonce", []),
        "_source_pages_corrige": ex.get("_source_pages_corrige", []),
        "chapitres": [],
        "notions_traitees": [],
        "donnees_fournies": {},
        "updated_at": now,
    }
    out.append(entry)

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(f"Wrote {OUT}")
print(f"  {len(out)} exercices avec correction Claude")
print(f"  {len(src) - len(out)} exercices restants à refaire")
print()
print("Détail par épreuve :")
from collections import defaultdict
done = defaultdict(int)
pending = defaultdict(int)
for ex in src:
    key = f"{ex['annee']} {ex['session']}"
    if ex['id'] in CORRECTIONS:
        done[key] += 1
    else:
        pending[key] += 1
for key in sorted(set(done) | set(pending)):
    d = done.get(key, 0)
    p = pending.get(key, 0)
    print(f"  {key:<25} {d}/{d+p}")
