import re
import os
import json
from collections import defaultdict

def clean_text(text):
    if not text:
        return ""
    text = text.strip()
    # Replace 3 or more newlines with 2 newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def parse_file(path):
    print(f"Parsing {os.path.basename(path)}...")
    with open(path, encoding='utf-8') as f:
        content = f.read()

    # Split the file into lines
    lines = content.split('\n')
    
    # We will identify headers. Each header marks the start of a new section.
    # We want to be very precise.
    # Let's define the two patterns:
    # 1. Triple-equals header
    re_eq = re.compile(r'^===\s*(.*?)\s*===+$')
    
    # 2. Session header (Bac or Baccalauréat followed by year and session)
    re_session = re.compile(
        r'^(?:Document\s*:\s*)?'
        r'Bac(?:c?al(?:\.|[éae]?aur[ée]?at)?)?\.?\s*'
        r'(?:([CD])\s+)?'
        r'(?:(SN|SC)\s+)?'
        r'(\d{4})\b',
        re.IGNORECASE
    )
    
    sections = []
    
    for idx, line in enumerate(lines):
        line_s = line.strip()
        if not line_s:
            continue
            
        m_eq = re_eq.match(line_s)
        if m_eq:
            sections.append({
                'line_idx': idx,
                'type': 'eq',
                'header_text': m_eq.group(1),
                'full_line': line_s
            })
            continue
            
        m_sess = re_session.match(line_s)
        if m_sess:
            sections.append({
                'line_idx': idx,
                'type': 'session',
                'header_text': line_s,
                'full_line': line_s,
                'groups': m_sess.groups()
            })
            continue

    # Extract text blocks between section headers
    parsed_exercises = []
    for i, sec in enumerate(sections):
        start_line = sec['line_idx']
        end_line = sections[i+1]['line_idx'] if i+1 < len(sections) else len(lines)
        
        block_lines = lines[start_line+1 : end_line]
        block_text = '\n'.join(block_lines)
        
        # If type is 'eq', it's a single exercise block
        if sec['type'] == 'eq':
            parsed_exercises.append({
                'source_file': os.path.basename(path),
                'header_type': 'eq',
                'header_text': sec['header_text'],
                'full_header': sec['full_line'],
                'content': clean_text(block_text)
            })
        else:
            # It's a session block, which may contain multiple internal exercises (Exercice 1, Exercice 2, QCM, etc.)
            # We split the block_text by 'Exercice N' or 'QCM' or 'Premier sujet'
            # Let's find exercise markers inside the session block
            sub_lines = block_text.split('\n')
            sub_sections = []
            
            re_sub_ex = re.compile(
                r'^(?:Exercice|EXERCICE)\s*N?[°ºo]?\s*(\d+)'
                r'|^(?:Q\.?\s*C\.?\s*M\.?)'
                r'|^(?:Premier|Deuxième|Troisième|1er|2ème|3ème|1ère|2nd)\s+sujet'
                r'|^[I|II|III|IV|V]+\.\s+\w+'
                r'|^(?:Partie|PARTIE)\s+(\d+|[A-Z])'
                r'|^[A-Z]-\s+Le\s+document',
                re.IGNORECASE
            )
            
            # Add the start of the session block as the first sub-section if it has text
            current_sub_header = sec['header_text']
            current_sub_lines = []
            
            for sub_idx, sub_l in enumerate(sub_lines):
                sub_l_s = sub_l.strip()
                if re_sub_ex.match(sub_l_s):
                    # Save previous sub-section
                    if current_sub_lines or current_sub_header:
                        sub_sections.append({
                            'sub_header': current_sub_header,
                            'lines': current_sub_lines
                        })
                    current_sub_header = sub_l_s
                    current_sub_lines = []
                else:
                    current_sub_lines.append(sub_l)
            
            # Save the last sub-section
            if current_sub_lines or current_sub_header:
                sub_sections.append({
                    'sub_header': current_sub_header,
                    'lines': current_sub_lines
                })
                
            for s_sec in sub_sections:
                content = clean_text('\n'.join(s_sec['lines']))
                parsed_exercises.append({
                    'source_file': os.path.basename(path),
                    'header_type': 'session_sub',
                    'session_header': sec['header_text'],
                    'header_text': s_sec['sub_header'],
                    'full_header': f"{sec['header_text']} -> {s_sec['sub_header']}",
                    'content': content
                })
                
    return parsed_exercises

if __name__ == '__main__':
    for f in ['science-bacc.txt', 'science-bacD.txt', 'math-bacD.txt']:
        p = os.path.join('/Users/mohameda/Documents/Bac/rag-service/exo_extracted_backup', f)
        exos = parse_file(p)
        print(f"Total exercises extracted: {len(exos)}")
        print("First 5 exercises:")
        for idx, exo in enumerate(exos[:5]):
            print(f"  {idx+1}. Header: {exo['full_header'][:100]}")
            print(f"     Content length: {len(exo['content'])}")
        print("-" * 50)
