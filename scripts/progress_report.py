"""État d'avancement du contenu, par matière, série, chapitre et notion.

    python scripts/progress_report.py            # tableau complet
    python scripts/progress_report.py --short    # totaux seulement

Ne compte comme « SÛR » que ce qui a été vérifié et passe le contrôle
automatique (content_check.py) :
  - énoncé sûr     : énoncé présent dans un module de content/ (retranscrit et
                     vérifié sur le PDF officiel) ET identique à celui en base ;
  - correction sûre: correction présente dans un module de content/ ET
                     identique à celle en base ;
  - exercice SÛR   : énoncé sûr + correction sûre ;
  - cours sûr      : cours d'une notion écrit dans un module de content/ et
                     identique à celui en base.
« Validé admin » est affiché à part : c'est ta validation, pas une vérification
automatique (5 énoncés validés contenaient des erreurs).
"""
from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "content"))


def norm(s: str | None) -> str:
    return (s or "").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--short", action="store_true")
    args = ap.parse_args()

    json_path = Path(os.environ.get("RAG_JSON_BAC", ROOT / "json_bac.json")).resolve()
    data = json.load(open(json_path, encoding="utf-8"))
    data_dir = json_path.parent
    courses = json.load(open(data_dir / "cours.json", encoding="utf-8")) if (data_dir / "cours.json").exists() else {}
    registry = (json.load(open(data_dir / "notions_registry.json", encoding="utf-8"))
                if (data_dir / "notions_registry.json").exists() else {})

    # Contenu vérifié (modules de content/)
    v_enonce: dict[str, str] = {}
    v_corr: dict[str, str] = {}
    v_lesson: dict[str, str] = {}
    for p in sorted((ROOT / "content").glob("*.py")):
        if p.stem.startswith("_"):
            continue
        m = importlib.import_module(p.stem)
        for eid, it in getattr(m, "ENONCES", {}).items():
            v_enonce[eid] = norm(it["enonce"])
        for eid, it in getattr(m, "CORRECTIONS", {}).items():
            if it.get("enonce"):
                v_enonce[eid] = norm(it["enonce"])
            if it.get("correction"):
                v_corr[eid] = norm(it["correction"])
        for n in getattr(m, "NOTIONS", []):
            v_lesson[n["id"]] = norm(n.get("lesson"))

    # ── Exercices ──────────────────────────────────────────────────────────
    K = ("total", "vides", "enonce_sur", "corr_sur", "SUR", "valide_admin")
    by_chap: dict[tuple, dict] = defaultdict(lambda: dict.fromkeys(K, 0))
    by_mat: dict[str, dict] = defaultdict(lambda: dict.fromkeys(K, 0))
    tot = dict.fromkeys(K, 0)
    for e in data:
        mat = e.get("matiere_id") or "?"
        serie = (e.get("filiere") or "?").replace("Série ", "")
        chap = e.get("chapitre") or "(sans chapitre)"
        empty = e.get("is_skeleton") or len(norm(e.get("ennonce_complet"))) < 40
        en_ok = e["id"] in v_enonce and v_enonce[e["id"]] == norm(e.get("ennonce_complet"))
        co_ok = e["id"] in v_corr and v_corr[e["id"]] == norm(e.get("correction"))
        row = {"total": 1, "vides": int(bool(empty)), "enonce_sur": int(en_ok), "corr_sur": int(co_ok),
               "SUR": int(en_ok and co_ok), "valide_admin": int(bool(e.get("validated_by_admin")))}
        for bucket in (by_chap[(mat, serie, chap)], by_mat[mat], tot):
            for k, v in row.items():
                bucket[k] += v

    def pct(a: int, b: int) -> str:
        return f"{100 * a / b:5.1f}%" if b else "   — "

    print(f"Données : {json_path}\n")
    print("═══ EXERCICES ═══  (SÛR = énoncé vérifié + correction vérifiée)")
    print(f"{'':52} {'total':>6} {'vides':>6} {'énoncé✓':>8} {'corr.✓':>7} {'SÛR':>5} {'%SÛR':>7} {'validé':>7}")
    for mat in sorted(by_mat):
        b = by_mat[mat]
        print(f"{mat.upper():52} {b['total']:6} {b['vides']:6} {b['enonce_sur']:8} {b['corr_sur']:7} "
              f"{b['SUR']:5} {pct(b['SUR'], b['total']):>7} {b['valide_admin']:7}")
        if args.short:
            continue
        for (m, s, c), b in sorted(by_chap.items()):
            if m != mat:
                continue
            print(f"   {s:2} {c[:45]:46} {b['total']:6} {b['vides']:6} {b['enonce_sur']:8} {b['corr_sur']:7} "
                  f"{b['SUR']:5} {pct(b['SUR'], b['total']):>7} {b['valide_admin']:7}")
    print(f"{'TOTAL':52} {tot['total']:6} {tot['vides']:6} {tot['enonce_sur']:8} {tot['corr_sur']:7} "
          f"{tot['SUR']:5} {pct(tot['SUR'], tot['total']):>7} {tot['valide_admin']:7}")

    # ── Notions et cours ───────────────────────────────────────────────────
    print("\n═══ NOTIONS ET COURS ═══  (cours sûr = écrit et vérifié, identique en base)")
    nb: dict[str, dict] = defaultdict(lambda: {"notions": 0, "cours": 0, "cours_sur": 0, "cours_valide": 0})
    for nid, n in registry.items():
        mat = n.get("matiere_id") or "?"
        c = courses.get(nid) or {}
        nb[mat]["notions"] += 1
        nb[mat]["cours"] += int(bool(norm(c.get("content"))))
        nb[mat]["cours_sur"] += int(nid in v_lesson and v_lesson[nid] == norm(c.get("content")))
        nb[mat]["cours_valide"] += int(bool(c.get("validated_by_admin")))
    print(f"{'':10} {'notions':>8} {'avec cours':>11} {'cours sûrs':>11} {'%sûr':>7} {'validés':>8}")
    T = {"notions": 0, "cours": 0, "cours_sur": 0, "cours_valide": 0}
    for mat in sorted(nb):
        b = nb[mat]
        for k in T:
            T[k] += b[k]
        print(f"{mat.upper():10} {b['notions']:8} {b['cours']:11} {b['cours_sur']:11} "
              f"{pct(b['cours_sur'], b['notions']):>7} {b['cours_valide']:8}")
    print(f"{'TOTAL':10} {T['notions']:8} {T['cours']:11} {T['cours_sur']:11} "
          f"{pct(T['cours_sur'], T['notions']):>7} {T['cours_valide']:8}")

    # ── Objectif 20 % ──────────────────────────────────────────────────────
    goal = -(-tot["total"] * 20 // 100)
    print(f"\nObjectif 20 % : {goal} exercices SÛRS — actuellement {tot['SUR']} — il en manque {max(0, goal - tot['SUR'])}.")
    ready = tot["enonce_sur"] - tot["SUR"]
    print(f"Exercices dont l'énoncé est déjà sûr mais sans correction vérifiée : {ready}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
