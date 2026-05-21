import json
import os
import sys

def is_empty(e):
    val = (e.get('ennonce_complet') or '').strip()
    if not val:
        return True
    if len(val) < 100:
        return True
    if e.get('is_skeleton'):
        return True
    return False

def main():
    json_path = '/Users/mohameda/Documents/Bac/rag-service/json_bac.json'
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found")
        sys.exit(1)

    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)

    stats = {}
    for e in data:
        # Standardize subject
        subj = e.get('matiere_id')
        if not subj:
            m = str(e.get('matiere', '')).lower()
            if 'math' in m:
                subj = 'math'
            elif 'phys' in m or 'chim' in m or 'pc' in m:
                subj = 'pc'
            elif 'nat' in m or 'svt' in m:
                subj = 'svt'
            else:
                subj = 'other'

        # Standardize filiere
        fil = e.get('filiere_id')
        if not fil:
            filiere = str(e.get('filiere', '')).upper()
            if 'D' in filiere:
                fil = 'D'
            else:
                fil = 'C'

        key = (subj, fil)
        if key not in stats:
            stats[key] = {'total': 0, 'filled': 0, 'empty': 0}

        stats[key]['total'] += 1
        if is_empty(e):
            stats[key]['empty'] += 1
        else:
            stats[key]['filled'] += 1

    print("\n=================== DATABASE COVERAGE ===================")
    print(f"{'Subject':<10} | {'Série':<5} | {'Filled':<8} / {'Total':<8} | {'Coverage %':<10}")
    print("-" * 55)
    
    total_all = 0
    filled_all = 0

    for (subj, fil), counts in sorted(stats.items(), key=lambda x: (x[0][0], x[0][1])):
        if subj == 'other':
            continue
        total = counts['total']
        filled = counts['filled']
        total_all += total
        filled_all += filled
        pct = (filled / total * 100) if total > 0 else 0
        print(f"{subj:<10} | {fil:<5} | {filled:<8} / {total:<8} | {pct:.1f}%")

    print("-" * 55)
    total_pct = (filled_all / total_all * 100) if total_all > 0 else 0
    print(f"{'TOTAL':<10} | {'ALL':<5} | {filled_all:<8} / {total_all:<8} | {total_pct:.1f}%")
    print("=========================================================\n")

if __name__ == '__main__':
    main()
