import os

def rewrite_file(filepath, new_content):
    if not os.path.exists(filepath): return
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

# 1. Cyber Striker
cs_html = """{% extends "core/mini_project_base.html" %}

{% block project_canvas %}
<canvas id="striker-canvas" class="absolute inset-0 w-full h-full z-0"></canvas>

<div class="absolute top-4 left-0 right-0 flex justify-center pointer-events-none z-10">
    <div class="bg-black/60 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-xs md:text-sm shadow-xl">
        <span id="cs-score-readout" class="text-red-400">SYSTEM LOADED // SHIELDS: 100%</span>
    </div>
</div>

<div id="cs-terminal-screen" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: none;">
    <h2 id="cs-screen-title" class="text-3xl md:text-5xl font-display font-black text-red-500 mb-4 tracking-wider">CORE INTEGRITY COLLAPSE</h2>
    <p id="cs-screen-desc" class="text-gray-300 font-mono text-sm md:text-lg mb-8 max-w-md">Fighter chassis completely vaporized by incoming data thrash packets.</p>
    <button id="cs-restart-btn" class="px-6 py-3 bg-white text-black font-bold rounded-full hover:bg-gray-200 transition-colors text-sm">RE-MATERIALIZE SHIP</button>
</div>
{% endblock %}

{% block project_scripts %}
"""
# Append original scripts to CS
cs_path = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\cyber-striker.html'
with open(cs_path, 'r', encoding='utf-8') as f:
    cs_orig = f.read()
cs_scripts = cs_orig.split('{% block project_scripts %}')[1] if '{% block project_scripts %}' in cs_orig else ''
rewrite_file(cs_path, cs_html + cs_scripts)


# 2. Glyph Matrix
glyph_html = """{% extends "core/mini_project_base.html" %}

{% block project_canvas %}
<canvas id="glyph-canvas" class="absolute inset-0 w-full h-full z-0 cursor-none"></canvas>

<div class="absolute top-4 left-0 right-0 flex justify-center pointer-events-none z-10">
    <div class="bg-black/60 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-xs md:text-sm shadow-xl">
        <span id="glyph-score-readout" class="text-[#00e5ff]">NODES: 0 / 4 // EFFICIENCY: 100%</span>
    </div>
</div>

<div id="glyph-overlay" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: none;">
    <h2 id="glyph-screen-title" class="text-3xl md:text-5xl font-display font-black text-[#00e5ff] mb-4 tracking-wider">MATRIX SYNCHRONIZED</h2>
    <p id="glyph-screen-desc" class="text-gray-300 font-mono text-sm md:text-lg mb-8 max-w-md">All data streams successfully connected.</p>
    <button id="glyph-restart-btn" class="px-6 py-3 bg-[#00e5ff] text-black font-bold rounded-full hover:bg-[#00c2d6] transition-colors text-sm">NEXT SEQUENCE</button>
</div>
{% endblock %}

{% block project_scripts %}
"""
glyph_path = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\glyph-matrix.html'
with open(glyph_path, 'r', encoding='utf-8') as f: glyph_orig = f.read()
glyph_scripts = glyph_orig.split('{% block project_scripts %}')[1] if '{% block project_scripts %}' in glyph_orig else ''
rewrite_file(glyph_path, glyph_html + glyph_scripts)


# 3. Typing Defender
td_html = """{% extends "core/mini_project_base.html" %}

{% block project_canvas %}
<canvas id="defender-canvas" class="absolute inset-0 w-full h-full z-0"></canvas>

<div class="absolute top-4 left-0 right-0 flex flex-col items-center gap-2 pointer-events-none z-10">
    <div class="bg-black/60 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-xs md:text-sm shadow-xl">
        <span id="td-score-readout" class="text-[#ff007f]">SCORE: 0 // FIREWALL: 100%</span>
    </div>
    <div id="td-current-target" class="text-xl md:text-2xl font-mono font-bold tracking-[0.2em] text-[#ff007f] drop-shadow-md"></div>
</div>

<div id="td-terminal-screen" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: flex;">
    <h2 id="td-screen-title" class="text-3xl md:text-5xl font-display font-black text-white mb-4 tracking-wider">INITIATE DEFENSE</h2>
    <p id="td-screen-desc" class="text-gray-300 font-mono text-sm md:text-lg mb-8 max-w-md">The firewall is under heavy DDoS attack. Rely on manual override typing to intercept packets.</p>
    <button id="td-restart-btn" class="px-6 py-3 bg-white text-black font-bold rounded-full hover:bg-gray-200 transition-colors pointer-events-auto text-sm">ENGAGE</button>
</div>
{% endblock %}

{% block project_scripts %}
"""
td_path = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\typing-defender.html'
with open(td_path, 'r', encoding='utf-8') as f: td_orig = f.read()
td_scripts = td_orig.split('{% block project_scripts %}')[1] if '{% block project_scripts %}' in td_orig else ''
rewrite_file(td_path, td_html + td_scripts)


# 4. Gravity Golf
gg_html = """{% extends "core/mini_project_base.html" %}

{% block project_canvas %}
<canvas id="golf-canvas" class="absolute inset-0 w-full h-full z-0"></canvas>

<div class="absolute top-4 left-0 right-0 flex justify-center pointer-events-none z-10">
    <div class="bg-black/60 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-xs md:text-sm shadow-xl flex items-center gap-4">
        <span class="text-[#00ff66]">LVL <span id="hud-level">1</span></span>
        <span class="text-white/30">|</span>
        <span class="text-[#00ff66]">ATTEMPTS: <span id="hud-attempts">0</span></span>
        <span class="text-white/30">|</span>
        <span class="text-[#00ff66]">PROBES: <span id="hud-probes">5</span></span>
    </div>
</div>

<div id="gg-overlay" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: none;">
    <h2 id="gg-screen-title" class="text-3xl md:text-5xl font-display font-black text-[#00ff66] mb-4 tracking-wider">ORBIT ACHIEVED</h2>
    <p id="gg-screen-desc" class="text-gray-300 font-mono text-sm md:text-lg mb-8 max-w-md">Probe successfully delivered to target.</p>
    <button id="gg-restart-btn" class="px-6 py-3 bg-[#00ff66] text-black font-bold rounded-full hover:bg-[#00cc52] transition-colors text-sm">NEXT LEVEL</button>
</div>
{% endblock %}

{% block project_scripts %}
"""
gg_path = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html'
with open(gg_path, 'r', encoding='utf-8') as f: gg_orig = f.read()
gg_scripts = gg_orig.split('{% block project_scripts %}')[1] if '{% block project_scripts %}' in gg_orig else ''
rewrite_file(gg_path, gg_html + gg_scripts)


# 5. Chroma
chroma_html = """{% extends "core/mini_project_base.html" %}

{% block project_canvas %}
<div class="absolute inset-0 z-0 bg-[#050505] flex flex-col items-center justify-center p-4 md:p-8">
    <div class="w-full max-w-4xl z-10 overflow-x-auto pb-4 custom-scrollbar">
        <div class="min-w-[800px] px-2 flex flex-col">
            <div class="flex justify-between gap-1 mb-1">
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Esc">Esc</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="1">1</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="2">2</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="3">3</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="4">4</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="5">5</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="6">6</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="7">7</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="8">8</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="9">9</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="0">0</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="-">-</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="=">=</div>
                <div class="kbd-key flex-grow bg-gray-900 border border-white/10 rounded flex items-center justify-end pr-4 text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Backspace">Delete</div>
            </div>
            <div class="flex justify-between gap-1 mb-1">
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-start pl-4 text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Tab">Tab</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="Q">Q</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="W">W</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="E">E</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="R">R</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="T">T</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="Y">Y</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="U">U</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="I">I</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="O">O</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="P">P</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="[">[</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="]">]</div>
                <div class="kbd-key flex-grow bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="\\\\">\\\\</div>
            </div>
            <div class="flex justify-between gap-1 mb-1">
                <div class="kbd-key w-20 bg-gray-900 border border-white/10 rounded flex items-center justify-start pl-4 text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Caps">Caps</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="A">A</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="S">S</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="D">D</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="F">F</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="G">G</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="H">H</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="J">J</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="K">K</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="L">L</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key=";">;</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="'">'</div>
                <div class="kbd-key flex-grow bg-gray-900 border border-white/10 rounded flex items-center justify-end pr-4 text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Enter">Return</div>
            </div>
            <div class="flex justify-between gap-1 mb-1">
                <div class="kbd-key w-28 bg-gray-900 border border-white/10 rounded flex items-center justify-start pl-4 text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Shift">Shift</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="Z">Z</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="X">X</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="C">C</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="V">V</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="B">B</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="N">N</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="M">M</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key=",">,</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key=".">.</div>
                <div class="kbd-key h-12 w-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="/">/</div>
                <div class="kbd-key flex-grow bg-gray-900 border border-white/10 rounded flex items-center justify-end pr-4 text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Shift">Shift</div>
            </div>
            <div class="flex justify-between gap-1">
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Ctrl">Ctrl</div>
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Opt">Opt</div>
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Cmd">Cmd</div>
                <div class="kbd-key flex-grow h-12 bg-gray-900 border border-white/10 rounded flex items-center justify-center cursor-pointer transition-all hover:bg-gray-800" data-key="Space"></div>
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Cmd">Cmd</div>
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Opt">Opt</div>
                <div class="kbd-key w-16 bg-gray-900 border border-white/10 rounded flex items-center justify-center text-xs text-white/50 cursor-pointer transition-all hover:bg-gray-800" data-key="Ctrl">Ctrl</div>
            </div>
        </div>
    </div>
    
    <div class="studio-status mt-8 text-center text-[var(--color-accent)] font-mono text-xs md:text-sm tracking-widest uppercase opacity-80">
        MATRIX LOGIC STATE: HEX_NULL // CLICK CORE MODULES
    </div>
</div>
{% endblock %}

{% block project_scripts %}
"""
chroma_path = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\chroma.html'
with open(chroma_path, 'r', encoding='utf-8') as f: chroma_orig = f.read()
chroma_scripts = chroma_orig.split('{% block project_scripts %}')[1] if '{% block project_scripts %}' in chroma_orig else ''
rewrite_file(chroma_path, chroma_html + chroma_scripts)

print("HUDs perfectly cleaned up!")
