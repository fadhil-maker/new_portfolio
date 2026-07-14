import os
import re

files = ['aether.html', 'gravity-golf.html', 'chroma.html', 'cyber-striker.html', 'glyph-matrix.html', 'typing-defender.html']
base_dir = r'C:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects'

for f in files:
    path = os.path.join(base_dir, f)
    if not os.path.exists(path): continue
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    print(f'\n--- {f} ---')
    ids = re.findall(r'getElementById\([\'\"](.*?)[\'\"]\)', content)
    for i in ids:
        if f'id="{i}"' not in content and f"id='{i}'" not in content:
            print(f'MISSING ID: {i}')
    
    qs = re.findall(r'querySelector\([\'\"](.*?)[\'\"]\)', content)
    for q in qs:
        if q.startswith('.'):
            class_name = q[1:]
            if class_name not in content:
                 print(f'POSSIBLE MISSING CLASS: {q}')
