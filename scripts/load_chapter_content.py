"""Charge le contenu d'un chapitre (notions canoniques + cours) dans les données.

Par défaut : SIMULATION (rien n'est écrit), avec un rapport complet.
Ajouter --apply pour écrire. Chaque fichier modifié est sauvegardé avant
écriture dans json_backups/ (mêmes stores que l'API admin).

Ce que fait --apply :
  1. notions_registry.json : crée les notions canoniques absentes.
  2. cours.json : insère chaque cours en BROUILLON (validated_by_admin=False).
     Un cours déjà validé n'est JAMAIS touché ; un cours existant non validé
     n'est remplacé qu'avec --force-lessons.
  3. publications.json : fixe la liste de notions du chapitre pour chaque
     série (C, D…) si elle n'a pas encore été enregistrée (--force-lists pour
     remplacer). Le statut (brouillon / publié) n'est pas modifié.
  4. --tag : pose les notions canoniques sur les exercices du chapitre.
     Exercices listés dans EXERCISE_TAGS (vérifiés à la main) : les notions
     canoniques sont REMPLACÉES par la liste vérifiée. Autres exercices :
     ajout par mots-clés. --clean-old retire en plus les anciennes notions
     (non canoniques) de ces exercices.

Usage (depuis rag-service/) :
  python scripts/load_chapter_content.py nombres_complexes            # simulation
  python scripts/load_chapter_content.py nombres_complexes --tag      # simulation + tags
  python scripts/load_chapter_content.py nombres_complexes --tag --apply
  python scripts/load_chapter_content.py nombres_complexes --tag --clean-old --apply
"""
from __future__ import annotations

import argparse
import importlib
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from admin_api import AdminStore  # noqa: E402
from admin_chapters import (  # noqa: E402
    PublicationsStore,
    RegistryStore,
    _canon_matiere,
    _in_chapter,
    chapter_key,
)
from admin_courses import CoursesStore  # noqa: E402

try:
    from katex_validator import validate as katex_validate  # noqa: E402
except Exception:  # pragma: no cover
    katex_validate = None


def load_content(name: str):
    sys.path.insert(0, str(ROOT / "content"))
    return importlib.import_module(name)


def detect(text: str, notions: list[dict]) -> list[str]:
    t = text.lower()
    return [n["id"] for n in notions if any(k.lower() in t for k in n.get("keywords", []))]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("content", help="module dans content/, ex. nombres_complexes")
    ap.add_argument("--apply", action="store_true", help="écrire (sinon simulation)")
    ap.add_argument("--tag", action="store_true", help="taguer les exercices du chapitre")
    ap.add_argument("--force-lessons", action="store_true", help="remplacer les cours NON validés existants")
    ap.add_argument("--force-lists", action="store_true", help="remplacer les listes de notions déjà enregistrées")
    ap.add_argument("--corrections", metavar="MODULE",
                    help="module de content/ avec CORRECTIONS = {exercice_id: {enonce, correction, note}}")
    ap.add_argument("--force-corrections", action="store_true",
                    help="avec --corrections : remplacer une correction déjà présente (exercice non validé)")
    ap.add_argument("--clean-old", action="store_true",
                    help="avec --tag : retirer des exercices du chapitre les anciennes notions non canoniques")
    args = ap.parse_args()

    c = load_content(args.content)
    matiere = _canon_matiere(c.MATIERE)
    chapitre = c.CHAPITRE
    notions = c.NOTIONS
    ids = [n["id"] for n in notions]
    assert len(ids) == len(set(ids)), "ids de notions en double"

    json_path = Path(os.environ.get("RAG_JSON_BAC", ROOT / "json_bac.json")).resolve()
    data_dir = json_path.parent
    backups = data_dir / "json_backups"
    bac_store = AdminStore(json_path=json_path, backup_dir=backups)
    courses_store = CoursesStore(path=data_dir / "cours.json", backup_dir=backups)
    reg_store = RegistryStore(data_dir / "notions_registry.json", backups)
    pub_store = PublicationsStore(data_dir / "publications.json", backups)

    mode = "ÉCRITURE" if args.apply else "SIMULATION (ajoute --apply pour écrire)"
    print(f"== {chapitre} ({matiere}) — {len(notions)} notions — {mode}\n")

    # ── 0. Validation KaTeX + couverture du programme ──────────────────────
    codes = [p for n in notions for p in n.get("programme", [])]
    dup = [p for p, k in Counter(codes).items() if k > 1]
    print(f"Programme : {len(codes)} items couverts" + (f" — DOUBLONS {dup}" if dup else ""))
    bad_katex = 0
    for n in notions:
        if not n.get("lesson", "").strip():
            print(f"  ✗ cours vide : {n['id']}")
            bad_katex += 1
            continue
        if katex_validate:
            rep = katex_validate(n["lesson"])
            # Le validateur vérifie aussi l'ancien format 12 sections : on ne
            # garde que les erreurs LaTeX/KaTeX (format court = 6 sections).
            errs = [e for e in rep.errors if not e.startswith("Sections manquantes")]
            if errs:
                bad_katex += 1
                print(f"  ✗ KaTeX {n['id']} : {errs[:3]}")
            for w in rep.warnings[:2]:
                print(f"  ⚠ {n['id']} : {w}")
    print(f"Cours : {len(notions) - bad_katex}/{len(notions)} valides\n")
    if bad_katex and args.apply:
        print("Arrêt : corrige les cours invalides avant --apply.")
        return 1

    # ── 1. Registry ────────────────────────────────────────────────────────
    registry = reg_store.load()
    new_reg = [n for n in notions if n["id"] not in registry]
    kw_updates = 0
    for n in notions:
        if n["id"] in registry and registry[n["id"]].get("keywords") != n.get("keywords", []):
            registry[n["id"]]["keywords"] = n.get("keywords", [])
            kw_updates += 1
    print(f"1. Registry : {len(new_reg)} notion(s) à créer, {len(notions) - len(new_reg)} déjà présente(s)"
          + (f", mots-clés mis à jour pour {kw_updates}" if kw_updates else ""))
    for n in new_reg:
        registry[n["id"]] = {
            "label": n["label"],
            "matiere_id": matiere,
            "aliases": [],
            "chapitre": chapitre,
            "programme": n.get("programme", []),
            "keywords": n.get("keywords", []),
        }

    # ── 2. Cours ───────────────────────────────────────────────────────────
    courses = courses_store.load()
    now = datetime.now(timezone.utc).replace(tzinfo=None).isoformat(timespec="seconds")
    ins = rep = skip_valid = skip_exist = 0
    for n in notions:
        cur = courses.get(n["id"])
        if cur and cur.get("validated_by_admin"):
            skip_valid += 1
            continue
        if cur and not args.force_lessons:
            skip_exist += 1
            continue
        if cur:
            rep += 1
        else:
            ins += 1
        courses[n["id"]] = {
            "content": n["lesson"].strip() + "\n",
            "model": "claude-ipn",
            "generated_at": now,
            "edited_at": None,
            "validated_by_admin": False,
            "notion_label": n["label"],
            "context_exo_ids": [],
            "source": getattr(c, "SOURCE", ""),
        }
    print(f"2. Cours : {ins} inséré(s), {rep} remplacé(s), {skip_exist} existant(s) gardé(s), "
          f"{skip_valid} déjà validé(s) jamais touché(s)")

    # ── 3. Listes de notions par série ─────────────────────────────────────
    series = sorted({s for n in notions for s in n["series"]})
    pubs = pub_store.load()
    list_updates = {}
    for s in series:
        wanted = [n["id"] for n in notions if s in n["series"]]
        cur = pubs.get(chapter_key(s, matiere, chapitre)) or {}
        curated = cur.get("notion_ids") is not None
        status = cur.get("status", "draft")
        if curated and not args.force_lists:
            print(f"3. Série {s} : liste déjà enregistrée ({len(cur['notion_ids'])} notions, {status}) — gardée")
            continue
        list_updates[s] = wanted
        print(f"3. Série {s} : liste → {len(wanted)} notions (statut {status} inchangé)")

    # ── 4. Tags exercices ──────────────────────────────────────────────────
    # Tags vérifiés (EXERCISE_TAGS) : ils REMPLACENT les notions canoniques de
    # l'exercice. Exercice absent de la liste : détection par mots-clés (ajout).
    # --clean-old : retire aussi les anciennes notions (hors notions canoniques
    # du chapitre) des exercices du chapitre.
    verified = getattr(c, "EXERCISE_TAGS", {})
    data = bac_store.load()
    tagged_changes = 0
    coverage: dict[str, Counter] = {s: Counter() for s in series}
    untagged: list[str] = []
    for e in data:
        for s in series:
            if not _in_chapter(e, s, matiere, chapitre):
                continue
            allowed = [n for n in notions if s in n["series"]]
            existing = list(e.get("notion_ids") or [])
            others = [i for i in existing if i not in ids]
            if e.get("id") in verified:
                canon, how = list(verified[e["id"]]), "vérifié"
            else:
                found = detect(f"{e.get('ennonce_complet') or ''}\n{e.get('correction') or ''}", allowed)
                canon = [i for i in existing if i in ids] + [i for i in found if i not in existing]
                how = "mots-clés"
            kept = [] if args.clean_old else others
            target = kept + [i for i in canon if i not in kept]
            changed = target != existing
            if args.tag and changed:
                e["notion_ids"] = target
                tagged_changes += 1
            final = canon if args.tag else [i for i in existing if i in ids]
            for i in final:
                coverage[s][i] += 1
            if not final:
                untagged.append(f"{e.get('id')} ({s})")
            if args.tag:
                removed_old = len(others) if args.clean_old else 0
                print(f"   {e.get('id'):30} {how:9} {len(canon)} notions"
                      + (f", {removed_old} ancienne(s) retirée(s)" if removed_old else ""))
    if args.tag:
        print(f"4. Tags : {tagged_changes} exercice(s) modifié(s)")
    else:
        print("4. Tags : non demandés (--tag)")

    # ── 5. Énoncés vérifiés + corrections ──────────────────────────────────
    corr_changes = 0
    if args.corrections:
        cm = load_content(args.corrections)
        by_id = {e.get("id"): e for e in data}
        now_s = datetime.now().isoformat(timespec="seconds")
        print(f"5. Corrections ({args.corrections}) : {len(cm.CORRECTIONS)} exercice(s)")
        for eid, item in cm.CORRECTIONS.items():
            e = by_id.get(eid)
            if e is None:
                print(f"   ✗ {eid} : introuvable")
                continue
            if katex_validate:
                errs = [x for k in ("enonce", "correction") if item.get(k)
                        for x in katex_validate(item[k]).errors if not x.startswith("Sections manquantes")]
                if errs:
                    print(f"   ✗ {eid} : KaTeX {errs[:2]}")
                    continue
            if e.get("validated_by_admin"):
                print(f"   = {eid} : déjà validé par l'admin — pas touché")
                continue
            what = []
            new_enonce = (item.get("enonce") or "").strip()
            if new_enonce and new_enonce != (e.get("ennonce_complet") or "").strip():
                if not e.get("ennonce_ocr"):
                    e["ennonce_ocr"] = e.get("ennonce_complet") or ""
                e["ennonce_complet"] = new_enonce + "\n"
                what.append("énoncé")
            new_corr = (item.get("correction") or "").strip()
            has_corr = bool((e.get("correction") or "").strip())
            if new_corr and (not has_corr or args.force_corrections):
                e["correction"] = new_corr + "\n"
                what.append("correction")
            elif new_corr and has_corr:
                what.append("correction existante gardée")
            if item.get("note"):
                e["note_admin"] = item["note"]
            if any(w in ("énoncé", "correction") for w in what):
                e["is_skeleton"] = False
                e["updated_at"] = now_s
                corr_changes += 1
            print(f"   {'+' if what else '='} {eid} : {', '.join(what) or 'rien à changer'}"
                  + (" ⚠ note" if item.get("note") else ""))

    print("\nCouverture (exercices par notion) :")
    for s in series:
        print(f"  Série {s} :")
        for n in notions:
            if s in n["series"]:
                print(f"    {coverage[s][n['id']]:3}  {n['label']}")
    if untagged:
        print(f"\n  ⚠ {len(untagged)} exercice(s) sans aucune notion canonique : {untagged[:10]}")

    # ── Écriture ───────────────────────────────────────────────────────────
    if not args.apply:
        print("\nSimulation terminée : rien n'a été écrit.")
        return 0
    if new_reg or kw_updates:
        reg_store.save(registry)
    if ins or rep:
        courses_store.save(courses)
    for s, wanted in list_updates.items():
        pub_store.upsert(s, matiere, chapitre, notion_ids=wanted)
    if (args.tag and tagged_changes) or corr_changes:
        bac_store.save(data)
    print("\nÉcrit. Sauvegardes dans json_backups/. Relis et valide les cours dans /admin/chapitres.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
