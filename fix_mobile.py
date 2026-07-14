import os
import re

def fix_css():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\static\css\arcade.css"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the block was removed
    if "@keyframes kineticRotationHint" in content:
        # We need to restore it properly
        replacement = """
        @keyframes kineticRotationHint {
            0% { transform: rotate(0deg); }
            40% { transform: rotate(-90deg); }
            70% { transform: rotate(-90deg); }
            100% { transform: rotate(0deg); }
        }

        @media (max-width: 768px) and (orientation: portrait) {
            body.landscape-lock-active .orientation-guard {
                display: none !important; /* disabled for mobile */
            }
        }

        /* ==================================================== */
        /* 10. MOBILE LANDSCAPE SCREEN REAL-ESTATE OPTIMIZATION */
        /* ==================================================== */
        @media (max-width: 932px) and (orientation: landscape) {"""
        
        # Regex to replace the butchered section
        content = re.sub(r'@keyframes kineticRotationHint\s*\{\s*0% \{ transform: rotate\(0deg\);\s*\}\s*\.golf-hud-overlay p', replacement + "\n            .golf-hud-overlay p", content)
        
        # Also ensure we didn't miss it if the replace_file_content failed completely
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

def fix_aether():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\aether.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add buttons to HTML
    if "override-btn-group" not in content:
        btn_html = """
                <div class="override-btn-group" style="display: flex; gap: 1rem; margin-top: 1rem;">
                    <button id="override-snow" style="background: transparent; border: 1px solid var(--accent); color: var(--accent); padding: 0.5rem 1rem; font-family: monospace; font-size: 0.75rem; cursor: pointer; text-transform: uppercase;">[ Override: Snow ]</button>
                    <button id="override-thunder" style="background: transparent; border: 1px solid var(--neon-cyan); color: var(--neon-cyan); padding: 0.5rem 1rem; font-family: monospace; font-size: 0.75rem; cursor: pointer; text-transform: uppercase;">[ Override: Thunder ]</button>
                </div>
        """
        content = content.replace('<h2>Aether</h2>', '<h2>Aether</h2>' + btn_html)

    # Add logic to JS
    if "override-snow" in content and "document.getElementById('override-snow')" not in content:
        js_logic = """
            const overrideSnow = document.getElementById('override-snow');
            const overrideThunder = document.getElementById('override-thunder');

            overrideSnow.addEventListener('click', (e) => {
                e.stopPropagation();
                targetCondition = 'snow';
                targetParticleCount = 200;
                isDay = 1; windSpeed = 8;
                stats.innerText = `MANUAL OVERRIDE // MATRIX: DAY_CRYOSPHERIC_SNOWFALL`;
            });

            overrideThunder.addEventListener('click', (e) => {
                e.stopPropagation();
                targetCondition = 'thunder';
                targetParticleCount = 180;
                isDay = 0; windSpeed = 25;
                stats.innerText = `MANUAL OVERRIDE // MATRIX: NIGHT_ELECTROMAGNETIC_THUNDERSTORM // GALE_FORCE: 25KM/H`;
            });
"""
        # Insert before run() call at the bottom
        content = content.replace("fetchMetrics(10.52, 76.21, \"Thrissur\");\n            run();", js_logic + "\n            fetchMetrics(10.52, 76.21, \"Thrissur\");\n            run();")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_golf():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change target node X to use percentage
    content = content.replace(
        "let targetNode = { x: canvas.width - 180, y: canvas.height / 2, r: 24 };",
        "let targetNode = { x: canvas.width > 600 ? canvas.width - 180 : canvas.width * 0.8, y: canvas.height / 2, r: 24 };"
    )

    # Add global activeMouseX / activeMouseY fallback for touch
    touch_logic = """
            let _mouseX = 0; let _mouseY = 0;
            window.addEventListener('mousemove', e => { _mouseX = e.clientX; _mouseY = e.clientY; });
            window.addEventListener('touchmove', e => { if(e.touches.length > 0) { _mouseX = e.touches[0].clientX; _mouseY = e.touches[0].clientY; } }, { passive: true });
"""
    if "let _mouseX = 0;" not in content:
        content = content.replace("let currentLevel = 1;", touch_logic + "\n            let currentLevel = 1;")
    
    # Replace activeMouseX and activeMouseY with _mouseX and _mouseY in drag simulation
    content = content.replace("dragControl.startX - activeMouseX", "dragControl.startX - _mouseX")
    content = content.replace("dragControl.startY - activeMouseY", "dragControl.startY - _mouseY")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_striker():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\cyber-striker.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add fallback for touch trackFighterPosition
    if "e.touches.length > 0" in content:
        # Wait, striker already has touchmove tracking. Let's make it smoother.
        content = content.replace(
            "window.addEventListener('touchmove', (e) => {\n                if (isSessionActive && e.touches.length > 0) trackFighterPosition(e.touches[0].clientX);\n            }, { passive: true });",
            "window.addEventListener('touchmove', (e) => {\n                if (isSessionActive && e.touches.length > 0) {\n                    const rect = canvas.getBoundingClientRect();\n                    let touchRelativeX = e.touches[0].clientX - rect.left;\n                    player.x = Math.max(20, Math.min(canvas.width - 20, touchRelativeX));\n                }\n            }, { passive: true });"
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_css()
    fix_aether()
    fix_golf()
    fix_striker()
