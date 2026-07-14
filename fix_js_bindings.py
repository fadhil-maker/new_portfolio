import os

def replace_in_file(filepath, replacements):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Gravity Golf
gg = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html'
replace_in_file(gg, [
    ("document.getElementById('gg-win-screen')", "document.getElementById('gg-overlay')"),
    ("document.getElementById('gg-score')", "document.getElementById('hud-attempts')"),
    ("document.getElementById('gg-lvl')", "document.getElementById('hud-level')"),
    ("document.getElementById('gg-probes')", "document.getElementById('hud-probes')"),
    ("document.getElementById('gg-end-title')", "document.getElementById('gg-screen-title')"),
    ("document.getElementById('gg-end-desc')", "document.getElementById('gg-screen-desc')"),
    ("const endIcon = document.getElementById('gg-end-icon');", ""),
    ("endIcon.className", "//"),
    ("const hudOverlay = document.getElementById('golf-hud-overlay');", "const hudOverlay = document.getElementById('gg-overlay');"), # fallback to overlay so style manipulation doesn't crash
])

# 2. Cyber Striker
cs = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\cyber-striker.html'
# Just wrap the first HUD div with id="cs-hud"
replace_in_file(cs, [
    ('<div class="absolute top-4 left-0 right-0 flex justify-center pointer-events-none z-10">',
     '<div id="cs-hud" class="absolute top-4 left-0 right-0 flex justify-center pointer-events-none z-10">')
])

# 3. Glyph Matrix
gm = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\glyph-matrix.html'
# Add missing hidden elements to prevent crash
gm_hidden = """<input type="file" id="matrix-image-upload" style="display:none;">
<div id="gm-upload-prompt" style="display:none;"></div>
{% endblock %}"""
replace_in_file(gm, [
    ("{% endblock %}", gm_hidden)
])

# 4. Typing Defender
td = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\typing-defender.html'
# Fix JS IDs and add hidden input
td_hidden = """<input type="text" id="arcade-type-input" style="opacity:0; position:absolute; top:0; left:0; z-index:-1;">
{% endblock %}"""
replace_in_file(td, [
    ("{% endblock %}", td_hidden),
    ("document.getElementById('typing-canvas')", "document.getElementById('defender-canvas')"),
    ("document.getElementById('td-score')", "document.getElementById('td-score-readout')"),
    ("document.getElementById('td-game-over-screen')", "document.getElementById('td-terminal-screen')"),
])

print("Fixed JS Bindings for all Mini Projects!")
