import os

def fix_aether():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\aether.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove buttons from HTML
    btn_html = """                <div class="override-btn-group" style="display: flex; gap: 1rem; margin-top: 1rem;">
                    <button id="override-snow" style="background: transparent; border: 1px solid var(--accent); color: var(--accent); padding: 0.5rem 1rem; font-family: monospace; font-size: 0.75rem; cursor: pointer; text-transform: uppercase;">[ Override: Snow ]</button>
                    <button id="override-thunder" style="background: transparent; border: 1px solid var(--neon-cyan); color: var(--neon-cyan); padding: 0.5rem 1rem; font-family: monospace; font-size: 0.75rem; cursor: pointer; text-transform: uppercase;">[ Override: Thunder ]</button>
                </div>"""
    content = content.replace(btn_html, "")

    # Remove logic from JS
    js_logic = """            const overrideSnow = document.getElementById('override-snow');
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
            });"""
    content = content.replace(js_logic, "")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_golf():
    filepath = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the issue where game stops working after one shot.
    # The issue is `ghostTrail = [...fullPathHistory]; probesLeft--; if (probesLeft <= 0) triggerTerminalOverlay(false); else generateLevelLayout();`
    # generateLevelLayout() sets ballNode.launching = false, resets everything.
    # BUT wait... if generateLevelLayout() resets the state, why doesn't it work?
    # Because `calculateActive` is still true, but wait, `generateLevelLayout()` doesn't clear `dragControl.active`.
    # Let's explicitly reset dragControl.active = false inside generateLevelLayout.
    if "dragControl.active = false;" not in content.split("function generateLevelLayout() {")[1]:
        content = content.replace(
            "ballNode.launching = false;",
            "ballNode.launching = false;\n                dragControl.active = false;"
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_aether()
    fix_golf()
