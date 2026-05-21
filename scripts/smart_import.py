import os
import re
import json
import shutil
import argparse
from datetime import datetime

def clean_text(text):
    if not text:
        return ""
    text = text.strip()
    # Normalize multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def parse_backup_file(path, default_subject, default_filiere):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    headers = []
    
    # Pattern 1: Triple equals header (e.g. === Sciences Physiques - Série C 2002 - Session Normale - Exercice 1 ===)
    re_eq = re.compile(r'^===\s*(.*?)\s*===+$')
    
    # Pattern 2: Session header prefix matcher
    re_header_prefix = re.compile(
        r'^('
        r'(?:baccalauréat|baccalaureate|bacc|bac|session|normale|normal|complémentaire|compl|série|serie|sciences|naturelles|physiques|mathématiques|math|pc|svt|epreuve|épreuve|document|additionnel|snb\+?|sn|sc|pdf|de|la|et|20\d{2}|\b[cdm]\b|[\s\-:,.\(\)]+)'
        r'+'
        r')',
        re.IGNORECASE
    )

    for idx, line in enumerate(lines):
        line_s = line.strip()
        if not line_s:
            continue
            
        m_eq = re_eq.match(line_s)
        if m_eq:
            headers.append((idx, 'eq', m_eq.group(1), line_s))
            continue
            
        if line_s.lower().startswith('bac') or line_s.lower().startswith('document'):
            m_pref = re_header_prefix.match(line_s)
            if m_pref:
                prefix = m_pref.group(1).strip()
                remainder = line_s[len(prefix):].strip()
                # Ensure the matched prefix contains a year
                if re.search(r'\b(20\d{2}|19\d{2})\b', prefix):
                    headers.append((idx, 'session', (prefix, remainder), line_s))
                    continue

    blocks = []
    for i, (idx, htype, hval, full_line) in enumerate(headers):
        start_line = idx
        end_line = headers[i+1][0] if i+1 < len(headers) else len(lines)
        
        remainder = ""
        if htype == 'session':
            prefix, remainder = hval
        
        block_lines = []
        if remainder:
            block_lines.append(remainder)
        block_lines.extend(lines[start_line+1 : end_line])
        block_text = '\n'.join(block_lines)
        
        blocks.append({
            'type': htype,
            'header_val': hval,
            'full_line': full_line,
            'block_text': block_text
        })

    parsed_exercises = []
    for b in blocks:
        if b['type'] == 'eq':
            header_str = b['header_val']
            
            # Subject
            subject = default_subject
            if 'phys' in header_str.lower() or 'chim' in header_str.lower() or ' pc ' in header_str.lower():
                subject = 'pc'
            elif 'math' in header_str.lower():
                subject = 'math'
            elif 'nat' in header_str.lower() or 'svt' in header_str.lower():
                subject = 'svt'
                
            # Filiere (Series)
            filiere = default_filiere
            if any(x in header_str.lower() for x in ['série c', 'serie c', 'série m', 'serie m']):
                filiere = 'C'
            elif any(x in header_str.lower() for x in ['série d', 'serie d', 'snb']):
                filiere = 'D'
                
            # Year
            year_m = re.search(r'\b(20\d{2}|19\d{2})\b', header_str)
            year = int(year_m.group(1)) if year_m else None
            
            # Session
            session_lower = header_str.lower()
            if 'compl' in session_lower:
                session = 'compl'
            elif re.search(r'\bsc\b', session_lower):
                session = 'compl'
            else:
                session = 'normal'
            
            # Exercise number
            ex_num = None
            ex_m = re.search(r'(?:Exercice|EXO|EXO-)\s*(\d+)', header_str, re.IGNORECASE)
            if ex_m:
                ex_num = int(ex_m.group(1))
            elif 'qcm' in header_str.lower():
                ex_num = 1
                
            parsed_exercises.append({
                'subject': subject,
                'filiere': filiere,
                'annee': year,
                'session': session,
                'ex_num': ex_num,
                'header': header_str,
                'content': clean_text(b['block_text'])
            })
        else:
            prefix, remainder = b['header_val']
            header_str = prefix
            
            # Year
            year_m = re.search(r'\b(20\d{2}|19\d{2})\b', header_str)
            year = int(year_m.group(1)) if year_m else None
            
            # Session
            session_lower = header_str.lower()
            if 'compl' in session_lower:
                session = 'compl'
            elif re.search(r'\bsc\b', session_lower):
                session = 'compl'
            else:
                session = 'normal'
            
            # Filiere
            filiere = default_filiere
            if any(x in header_str.upper() for x in [' C ', ' SÉRIE C ', ' SERIE C ', ' SÉRIE M ', ' SERIE M ']) or header_str.upper().endswith(' C'):
                filiere = 'C'
            elif any(x in header_str.upper() for x in [' D ', ' SÉRIE D ', ' SERIE D ', ' SN ', ' SNB ']) or header_str.upper().endswith(' D'):
                filiere = 'D'
                
            # Subject
            subject = default_subject
            if 'phys' in header_str.lower() or 'chim' in header_str.lower():
                subject = 'pc'
            elif 'math' in header_str.lower():
                subject = 'math'
            elif 'nat' in header_str.lower() or 'svt' in header_str.lower():
                subject = 'svt'
                
            # Split block_text by sub-exercise headers
            sub_lines = b['block_text'].split('\n')
            re_sub = re.compile(
                r'^(?:Exercice|EXERCICE)\s*N?[°ºo]?\s*(\d+)'
                r'|^(?:Q\.?\s*C\.?\s*M\.?)(?:\s*\([^)]*\))?'
                r'|^(?:Premier|Deuxième|Troisième|1er|2ème|3ème|1ère|2nd)\s+sujet'
                r'|^[I|II|III|IV|V]+\.\s+\w+'
                r'|^(?:Partie|PARTIE)\s+(\d+|[A-Z])'
                r'|^[A-Z]-\s+Le\s+document',
                re.IGNORECASE
            )
            
            sub_sections = []
            curr_header = ""
            curr_lines = []
            
            for line in sub_lines:
                line_s = line.strip()
                m_sub = re_sub.match(line_s)
                if m_sub:
                    if curr_lines or curr_header:
                        sub_sections.append((curr_header, curr_lines))
                    curr_header = m_sub.group(0).strip()
                    curr_lines = []
                    rem = line_s[m_sub.end():].strip()
                    if rem:
                        curr_lines.append(rem)
                else:
                    curr_lines.append(line)
            if curr_lines or curr_header:
                sub_sections.append((curr_header, curr_lines))
                
            # Check if session starts with a QCM
            has_qcm = False
            if sub_sections:
                first_hdr = sub_sections[0][0].lower()
                if 'qcm' in first_hdr:
                    has_qcm = True
                    
            for idx, (sub_hdr, s_lines) in enumerate(sub_sections):
                s_content = clean_text('\n'.join(s_lines))
                if not s_content.strip() and not sub_hdr.strip():
                    continue
                    
                sub_ex_num = None
                if sub_hdr:
                    if 'qcm' in sub_hdr.lower():
                        sub_ex_num = 1
                    else:
                        ex_m = re.search(r'(?:Exercice|EXO|EXO-)\s*(\d+)', sub_hdr, re.IGNORECASE)
                        if ex_m:
                            num = int(ex_m.group(1))
                            sub_ex_num = num + 1 if (has_qcm and num > 0) else num
                
                # fallback to index + 1
                if sub_ex_num is None or sub_ex_num == 0:
                    sub_ex_num = idx + 1
                    
                parsed_exercises.append({
                    'subject': subject,
                    'filiere': filiere,
                    'annee': year,
                    'session': session,
                    'ex_num': sub_ex_num,
                    'header': f"{header_str} -> {sub_hdr}",
                    'content': s_content
                })
                
    return parsed_exercises

def is_corrupted(e):
    val = e.get('ennonce_complet') or ''
    if '===' in val:
        return True
    if len(val) > 15000:
        return True
    return False

def is_empty(e):
    val = (e.get('ennonce_complet') or '').strip()
    if not val:
        return True
    if len(val) < 100:
        return True
    if e.get('is_skeleton'):
        return True
    if is_corrupted(e):
        return True
    return False

def find_entry(data, subject, filiere, annee, session, ex_num):
    sess_substr = 'normal' if session == 'normal' else 'compl'
    
    if subject == 'pc':
        mat_accept = {'pc', 'physique', 'chimie', 'Sciences Physiques'}
    elif subject == 'svt':
        mat_accept = {'svt', 'Sciences Naturelles', 'Sciences Naturelles (SVT)'}
    else:
        mat_accept = {subject}
        
    candidates = []
    for e in data:
        if e.get('filiere_id') != filiere:
            continue
            
        e_mat = e.get('matiere_id') or e.get('matiere') or ''
        if not any(x.lower() in e_mat.lower() for x in mat_accept):
            continue
            
        if e.get('annee') != annee:
            continue
            
        e_sess = e.get('session') or ''
        if sess_substr not in str(e_sess).lower():
            continue
            
        try:
            num = int(e.get('exercice_numero'))
        except (TypeError, ValueError):
            continue
            
        if num != ex_num:
            continue
            
        candidates.append(e)
        
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]
        
    # Prefer empty or skeleton candidates
    for c in candidates:
        if c.get('is_skeleton') or is_empty(c):
            return c
    return candidates[0]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', default='/Users/mohameda/Documents/Bac/rag-service/json_bac.json')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--force', action='store_true', help='Overwrite even if not empty or corrupted')
    args = parser.parse_args()

    # Load JSON data
    with open(args.json) as f:
        data = json.load(f)

    # Backup JSON before modifying
    if not args.dry_run:
        backup_dir = '/Users/mohameda/Documents/Bac/rag-service/json_backups'
        os.makedirs(backup_dir, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = os.path.join(backup_dir, f"json_bac-pre-smart-import-{stamp}.json")
        shutil.copy2(args.json, backup_path)
        print(f"Created backup at {backup_path}")

    # Files to process: (directory, filename, default_subject, default_filiere)
    files_to_process = [
        ('exo_extracted', 'science-bacc.txt', 'svt', 'C'),
        ('exo_extracted', 'science-bacD.txt', 'svt', 'D'),
        ('exo_extracted', 'math-bacC.txt', 'math', 'C'),
        ('exo_extracted', 'math-bacD.txt', 'math', 'D'),
        ('exo_extracted_backup', 'science-bacc.txt', 'pc', 'C'),
        ('exo_extracted_backup', 'science-bacD.txt', 'pc', 'D'),
    ]

    all_exercises = []
    for dir_name, fname, default_subj, default_fil in files_to_process:
        fpath = os.path.join('/Users/mohameda/Documents/Bac/rag-service', dir_name, fname)
        if os.path.exists(fpath):
            exos = parse_backup_file(fpath, default_subj, default_fil)
            if dir_name == 'exo_extracted_backup':
                exos = [e for e in exos if e['subject'] == 'pc']
            elif dir_name == 'exo_extracted' and fname.startswith('science'):
                exos = [e for e in exos if e['subject'] == 'svt']
            all_exercises.extend(exos)

    # Shift 0-indexed exercises to 1-indexed to match database
    groups_with_zero = set()
    for exo in all_exercises:
        if exo['ex_num'] == 0:
            groups_with_zero.add((exo['subject'], exo['filiere'], exo['annee'], exo['session']))
            
    for exo in all_exercises:
        group_key = (exo['subject'], exo['filiere'], exo['annee'], exo['session'])
        if group_key in groups_with_zero and isinstance(exo['ex_num'], int):
            exo['ex_num'] += 1

    print(f"Total exercises parsed: {len(all_exercises)}")

    updated_count = 0
    skipped_filled = 0
    skipped_missing = 0
    overwritten_corrupted = 0

    now = datetime.now().isoformat(timespec="seconds")

    for exo in all_exercises:
        subject = exo['subject']
        filiere = exo['filiere']
        annee = exo['annee']
        session = exo['session']
        ex_num = exo['ex_num']
        content = exo['content']

        if not content.strip() or len(content.strip()) < 50:
            continue

        entry = find_entry(data, subject, filiere, annee, session, ex_num)
        
        label = f"{filiere}/{subject}/{annee}/{session}/ex{ex_num}"

        if not entry:
            skipped_missing += 1
            # print(f"  Missing slot: {label}")
            continue

        empty = is_empty(entry)
        corrupt = is_corrupted(entry)

        if not empty and not args.force:
            skipped_filled += 1
            continue

        # Update entry
        entry['ennonce_complet'] = content
        entry['is_skeleton'] = False
        entry['updated_at'] = now
        updated_count += 1
        if corrupt:
            overwritten_corrupted += 1
            print(f"  Overwriting corrupted slot: {label} (id: {entry.get('id')})")
        else:
            print(f"  Filling slot: {label} (id: {entry.get('id')})")

    print("\n--- RESULTS ---")
    print(f"Updated/Filled : {updated_count} slots (including {overwritten_corrupted} corrupted ones)")
    print(f"Skipped filled : {skipped_filled} slots")
    print(f"Skipped missing: {skipped_missing} slots")

    if args.dry_run:
        print("\n[DRY RUN] No changes written to file.")
    else:
        # Write back to JSON
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\nSaved changes to {args.json}.")

if __name__ == '__main__':
    main()
