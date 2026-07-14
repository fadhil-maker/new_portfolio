import os
import re

def process_file(filepath, new_html):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract scripts
    script_match = re.search(r'{% block extra_scripts %}(.*?){% endblock %}', content, re.DOTALL)
    script_content = script_match.group(1).strip() if script_match else ""
    
    # In the scripts, change AudioMatrix if necessary, but it's shared now.
    
    final_content = f"""{{% extends "core/mini_project_base.html" %}}

{{% block project_canvas %}}
{new_html}
{{% endblock %}}

{{% block project_scripts %}}
{script_content}
{{% endblock %}}
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)


# 1. Chroma
chroma_html = """
<div class="absolute inset-0 z-0 bg-[#050505] flex flex-col items-center justify-center p-8">
    <div class="absolute top-6 left-8 z-10 pointer-events-none">
        <h2 class="text-3xl font-display font-bold text-white mb-1">Chroma</h2>
        <p class="text-sm text-gray-400 max-w-sm">Interactive Hardware Matrix. Tap keys to inject custom hex codes.</p>
    </div>
    
    <div class="w-full max-w-4xl mt-16 z-10">
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
            <div class="kbd-key flex-grow bg-gray-900 border border-white/10 rounded flex items-center justify-center text-sm font-medium cursor-pointer transition-all hover:bg-gray-800" data-key="\\">\\</div>
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
    
    <div class="studio-status mt-12 text-center text-[var(--color-accent)] font-mono text-sm tracking-widest uppercase opacity-80">
        MATRIX LOGIC STATE: HEX_NULL // CLICK CORE MODULES
    </div>
</div>
"""
process_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\chroma.html', chroma_html)

# 2. Cyber Striker
cyber_html = """
<canvas id="striker-canvas" class="absolute inset-0 w-full h-full z-0"></canvas>

<div id="cs-hud" class="absolute top-6 left-8 right-8 flex justify-between items-start z-10 pointer-events-none">
    <div>
        <h2 class="text-3xl font-display font-bold text-white mb-1 drop-shadow-lg">Cyber Striker</h2>
        <p class="text-sm text-gray-300 max-w-sm drop-shadow">Slide mouse to steer. Obliterate oncoming corrupted code cores. Gather gold nodes.</p>
    </div>
    <div class="bg-black/40 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-sm shadow-xl">
        <span id="cs-score-readout" class="text-[var(--color-accent)]">SYSTEM LOADED // MATRIX SHIELDS: 100%</span>
    </div>
</div>

<div id="cs-terminal-screen" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: none;">
    <h2 id="cs-screen-title" class="text-5xl font-display font-black text-red-500 mb-4 tracking-wider">CORE INTEGRITY COLLAPSE</h2>
    <p id="cs-screen-desc" class="text-gray-300 font-mono text-lg mb-8 max-w-md">Fighter chassis completely vaporized by incoming data thrash packets.</p>
    <button id="cs-restart-btn" class="px-8 py-3 bg-white text-black font-bold rounded-full hover:bg-gray-200 transition-colors">RE-MATERIALIZE SHIP</button>
</div>
"""
process_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\cyber-striker.html', cyber_html)

# 3. Glyph Matrix
glyph_html = """
<canvas id="glyph-canvas" class="absolute inset-0 w-full h-full z-0 cursor-none"></canvas>

<div id="glyph-hud" class="absolute top-6 left-8 right-8 flex justify-between items-start z-10 pointer-events-none">
    <div>
        <h2 class="text-3xl font-display font-bold text-white mb-1 drop-shadow-lg">Glyph Matrix</h2>
        <p class="text-sm text-gray-300 max-w-sm drop-shadow">Connect matching nodes. Avoid crossing streams.</p>
    </div>
    <div class="bg-black/40 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-sm shadow-xl">
        <span id="glyph-score-readout" class="text-[#00e5ff]">NODES: 0 / 4 // EFFICIENCY: 100%</span>
    </div>
</div>

<div id="glyph-overlay" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: none;">
    <h2 id="glyph-screen-title" class="text-5xl font-display font-black text-[#00e5ff] mb-4 tracking-wider">MATRIX SYNCHRONIZED</h2>
    <p id="glyph-screen-desc" class="text-gray-300 font-mono text-lg mb-8 max-w-md">All data streams successfully connected.</p>
    <button id="glyph-restart-btn" class="px-8 py-3 bg-[#00e5ff] text-black font-bold rounded-full hover:bg-[#00c2d6] transition-colors">NEXT SEQUENCE</button>
</div>
"""
process_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\glyph-matrix.html', glyph_html)


# 4. Typing Defender
typing_html = """
<canvas id="defender-canvas" class="absolute inset-0 w-full h-full z-0"></canvas>

<div id="td-hud" class="absolute top-6 left-8 right-8 flex flex-col md:flex-row justify-between items-start md:items-center z-10 pointer-events-none gap-4">
    <div>
        <h2 class="text-3xl font-display font-bold text-white mb-1 drop-shadow-lg">Typing Defender</h2>
        <p class="text-sm text-gray-300 max-w-md drop-shadow">Defend the core. Type the incoming words rapidly to vaporize them before they breach the firewall.</p>
    </div>
    <div class="flex flex-col items-end gap-2">
        <div class="bg-black/40 backdrop-blur-md border border-white/10 rounded-full px-6 py-2 text-white font-mono text-sm shadow-xl">
            <span id="td-score-readout" class="text-[var(--color-accent)]">SCORE: 0 // FIREWALL: 100%</span>
        </div>
        <div id="td-current-target" class="text-2xl font-mono font-bold tracking-[0.2em] text-[#ff007f] drop-shadow-md"></div>
    </div>
</div>

<div id="td-terminal-screen" class="absolute inset-0 z-50 bg-black/80 backdrop-blur-md flex flex-col items-center justify-center text-center p-6" style="display: flex;">
    <h2 id="td-screen-title" class="text-5xl font-display font-black text-white mb-4 tracking-wider">INITIATE DEFENSE</h2>
    <p id="td-screen-desc" class="text-gray-300 font-mono text-lg mb-8 max-w-md">The firewall is under heavy DDoS attack. Rely on manual override typing to intercept packets.</p>
    <button id="td-restart-btn" class="px-8 py-3 bg-white text-black font-bold rounded-full hover:bg-gray-200 transition-colors pointer-events-auto">ENGAGE</button>
</div>
"""
process_file(r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\typing-defender.html', typing_html)

print("Finished rewriting mini project HTML structures!")
