import os
import re
from smart_import import parse_backup_file

def inspect(dir_name, fname, default_subject, default_filiere):
    fpath = os.path.join('/Users/mohameda/Documents/Bac/rag-service', dir_name, fname)
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return
    print(f"\n=== Inspecting {dir_name}/{fname} (default: {default_subject}, {default_filiere}) ===")
    exos = parse_backup_file(fpath, default_subject, default_filiere)
    subject_counts = {}
    for e in exos:
        subj = e['subject']
        subject_counts[subj] = subject_counts.get(subj, 0) + 1
    print(f"Total parsed: {len(exos)}")
    for subj, count in subject_counts.items():
        print(f"  Subject '{subj}': {count}")
    
    # Print the first few of each subject
    for subj in sorted(subject_counts.keys()):
        print(f"  Examples for '{subj}':")
        printed = 0
        for e in exos:
            if e['subject'] == subj:
                print(f"    - [{e['filiere']}] Year: {e['annee']}, Sess: {e['session']}, Ex: {e['ex_num']}, Header: {e['header']}")
                printed += 1
                if printed >= 5:
                    break

inspect('exo_extracted', 'science-bacc.txt', 'svt', 'C')
inspect('exo_extracted', 'science-bacD.txt', 'svt', 'D')
inspect('exo_extracted_backup', 'science-bacc.txt', 'pc', 'C')
inspect('exo_extracted_backup', 'science-bacD.txt', 'pc', 'D')
