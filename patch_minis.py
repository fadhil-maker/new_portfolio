import os

def patch_file(filepath, replacements):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Cyber Striker
patch_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\cyber-striker.html', [
    ('class="absolute top-6 left-8 right-8 flex justify-between items-start z-10 pointer-events-none"',
     'class="absolute top-6 left-6 right-6 md:left-8 md:right-8 flex flex-col md:flex-row justify-between items-start z-10 pointer-events-none gap-4"'),
    ('max-w-sm drop-shadow', 'max-w-sm drop-shadow hidden md:block'),
])

# 2. Glyph Matrix
patch_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\glyph-matrix.html', [
    ('class="absolute top-6 left-8 right-8 flex justify-between items-start z-10 pointer-events-none"',
     'class="absolute top-6 left-6 right-6 md:left-8 md:right-8 flex flex-col md:flex-row justify-between items-start z-10 pointer-events-none gap-4"'),
    ('max-w-sm drop-shadow', 'max-w-sm drop-shadow hidden md:block'),
])

# 3. Typing Defender
patch_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\typing-defender.html', [
    ('class="absolute top-6 left-8 right-8 flex flex-col md:flex-row justify-between items-start md:items-center z-10 pointer-events-none gap-4"',
     'class="absolute top-6 left-6 right-6 md:left-8 md:right-8 flex flex-col md:flex-row justify-between items-start md:items-center z-10 pointer-events-none gap-4"'),
    ('max-w-md drop-shadow', 'max-w-md drop-shadow hidden md:block'),
    ('items-end', 'items-start md:items-end'),
])

# 4. Chroma
# Wrap the keyboard rows in a min-w container
chroma_path = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\chroma.html'
if os.path.exists(chroma_path):
    with open(chroma_path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<div class="w-full max-w-4xl mt-16 z-10">', '<div class="w-full max-w-4xl mt-24 md:mt-16 z-10 overflow-x-auto pb-4"><div class="min-w-[800px] px-4 flex flex-col">')
    c = c.replace('</div>\n    \n    <div class="studio-status', '</div></div>\n    \n    <div class="studio-status')
    c = c.replace('class="absolute top-6 left-8 z-10 pointer-events-none"', 'class="absolute top-6 left-6 md:left-8 z-10 pointer-events-none"')
    c = c.replace('class="text-sm text-gray-400 max-w-sm"', 'class="text-sm text-gray-400 max-w-sm hidden md:block"')
    with open(chroma_path, 'w', encoding='utf-8') as f:
        f.write(c)

# 5. Aether
patch_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\aether.html', [
    ('class="absolute top-6 left-8 right-8 flex justify-between items-start z-10 pointer-events-none"',
     'class="absolute top-6 left-6 right-6 md:left-8 md:right-8 flex flex-col md:flex-row justify-between items-start md:items-center z-10 pointer-events-none gap-4"'),
    ('text-sm text-gray-300 max-w-sm drop-shadow', 'text-sm text-gray-300 max-w-sm drop-shadow hidden md:block'),
])

# 6. Gravity Golf
patch_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html', [
    ('class="absolute top-6 left-8 right-8 flex justify-between items-start z-10 pointer-events-none"',
     'class="absolute top-6 left-6 right-6 md:left-8 md:right-8 flex flex-col md:flex-row justify-between items-start md:items-center z-10 pointer-events-none gap-4"'),
    ('text-sm text-gray-300 max-w-sm drop-shadow', 'text-sm text-gray-300 max-w-sm drop-shadow hidden md:block'),
])

print("Patched all mini project HUDs for mobile responsiveness!")
