"""
Mini-Project Static HTML Compiler
Merges Django templates into standalone HTML files for Next.js public directory.
Uses Tailwind V4 browser CDN and inlines all CSS variables for full dark mode support.
"""
import os
import re

projects_dir = r'backend/templates/core/mini_projects'
output_dir = r'public/project'

# CSS variables that match globals.css exactly
CSS_VARIABLES = """
:root {
    --color-accent: #6c63ff;
    --color-surface: #ffffff;
    --color-surface-elevated: #f8f9fa;
    --color-text-primary: #111111;
    --color-text-secondary: #555555;
    --font-inter: 'Inter', sans-serif;
    --font-outfit: 'Outfit', sans-serif;
}
.dark {
    --color-accent: #6c63ff;
    --color-surface: #0a0a0a;
    --color-surface-elevated: #141414;
    --color-text-primary: #f1f1f1;
    --color-text-secondary: #a0a0a0;
}
html { font-family: var(--font-inter); color: var(--color-text-primary); background: var(--color-surface); }
.dark { color-scheme: dark; }
body { background: var(--color-surface); color: var(--color-text-primary); }
.font-display, .font-outfit { font-family: var(--font-outfit); }
.glass {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
}
.dark .glass {
    background: rgba(255,255,255,0.04);
}
.reveal-up { opacity: 1; transform: none; }
"""

# Shared Audio Engine injected into all mini projects
SHARED_AUDIO_ENGINE = """
<script>
    // Shared Audio Engine
    const AudioMatrix = {
        ctx: null,
        init() {
            if (!this.ctx) this.ctx = new (window.AudioContext || window.webkitAudioContext)();
            if (this.ctx.state === 'suspended') this.ctx.resume();
        },
        playTick() {
            this.init();
            const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
            osc.type = 'triangle'; osc.frequency.setValueAtTime(750, this.ctx.currentTime);
            gain.gain.setValueAtTime(0.02, this.ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.015);
            osc.connect(gain); gain.connect(this.ctx.destination);
            osc.start(); osc.stop(this.ctx.currentTime + 0.015);
        },
        playDynamicKey(char) {
            this.init();
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const filter = this.ctx.createBiquadFilter();
            osc.type = 'square';
            osc.frequency.setValueAtTime(150, this.ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(40, this.ctx.currentTime + 0.05);
            filter.type = 'lowpass';
            filter.frequency.setValueAtTime(800, this.ctx.currentTime);
            filter.frequency.exponentialRampToValueAtTime(100, this.ctx.currentTime + 0.05);
            gain.gain.setValueAtTime(0, this.ctx.currentTime);
            gain.gain.linearRampToValueAtTime(0.15, this.ctx.currentTime + 0.01);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.05);
            osc.connect(filter); filter.connect(gain); gain.connect(this.ctx.destination);
            osc.start(); osc.stop(this.ctx.currentTime + 0.06);
        },
        playExplosion() {
            this.init();
            const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
            osc.type = 'sawtooth'; osc.frequency.setValueAtTime(400, this.ctx.currentTime);
            osc.frequency.linearRampToValueAtTime(60, this.ctx.currentTime + 0.14);
            gain.gain.setValueAtTime(0.05, this.ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.14);
            osc.connect(gain); gain.connect(this.ctx.destination);
            osc.start(); osc.stop(this.ctx.currentTime + 0.14);
        },
        playError() {
            this.init();
            const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
            osc.type = 'sawtooth'; osc.frequency.setValueAtTime(120, this.ctx.currentTime);
            gain.gain.setValueAtTime(0.09, this.ctx.currentTime);
            gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + 0.15);
            osc.connect(gain); gain.connect(this.ctx.destination);
            osc.start(); osc.stop(this.ctx.currentTime + 0.15);
        },
        playGameOver() {
            this.init(); const now = this.ctx.currentTime;
            [160, 130, 95].forEach((freq, i) => {
                const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
                osc.type = 'sawtooth'; osc.frequency.setValueAtTime(freq, now + i * 0.1);
                gain.gain.setValueAtTime(0.08, now + i * 0.1);
                gain.gain.linearRampToValueAtTime(0.001, now + i * 0.1 + 0.35);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now + i * 0.1); osc.stop(now + i * 0.1 + 0.35);
            });
        },
        playWin() {
            this.init(); const now = this.ctx.currentTime;
            [261.63, 329.63, 392.00, 523.25].forEach((freq, i) => {
                const osc = this.ctx.createOscillator(); const gain = this.ctx.createGain();
                osc.type = 'sine'; osc.frequency.setValueAtTime(freq, now + i * 0.06);
                gain.gain.setValueAtTime(0.04, now + i * 0.06);
                gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.06 + 0.22);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now + i * 0.06); osc.stop(now + i * 0.06 + 0.22);
            });
        }
    };
    let activeMouseX = 0, activeMouseY = 0;
    window.addEventListener('mousemove', (e) => { activeMouseX = e.clientX; activeMouseY = e.clientY; });
    window.addEventListener('touchmove', (e) => { if (e.touches && e.touches.length > 0) { activeMouseX = e.touches[0].clientX; activeMouseY = e.touches[0].clientY; } }, { passive: true });
</script>
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Muhammed Fadhil EH</title>
    <meta name="description" content="{title} - Interactive experiment by Muhammed Fadhil EH">
    <link rel="icon" type="image/png" href="/favicon.ico">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@500;700;900&display=swap">
    <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
    <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">
    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
    <style type="text/tailwindcss">
{css_variables}
    </style>
    <script>
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
            document.documentElement.classList.add('dark');
        }} else {{
            document.documentElement.classList.remove('dark');
        }}
    </script>
</head>
<body class="relative flex min-h-screen flex-col overflow-x-hidden pt-24 selection:bg-[var(--color-accent)] selection:text-black">
    <!-- Floating Navbar -->
    <nav class="fixed top-6 left-1/2 -translate-x-1/2 w-[90%] max-w-2xl z-50 transition-all duration-300" id="navbar">
        <div class="px-6 py-4 rounded-full flex items-center justify-between shadow-[0_8px_32px_rgba(0,0,0,0.1)] dark:shadow-[0_8px_32px_rgba(0,0,0,0.3)] border border-white/30 dark:border-white/10 bg-white/20 dark:bg-black/20 backdrop-blur-lg backdrop-saturate-200">
            <a href="/" class="flex items-center gap-2 group">
                <span class="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-gray-900 to-gray-600 dark:from-white dark:to-gray-400 font-outfit tracking-tight">Fadhil.</span>
            </a>
            <div class="flex items-center gap-4">
                <a href="/" class="text-sm font-semibold hover:text-[var(--color-accent)] transition-colors">← Back to Portfolio</a>
                <button id="theme-toggle" class="p-2 rounded-full border-2 border-transparent hover:border-black dark:hover:border-white bg-gray-100 dark:bg-gray-800 transition-all" aria-label="Toggle Dark Mode">
                    <i class="ph-fill ph-sun text-lg hidden dark:block"></i>
                    <i class="ph-fill ph-moon text-lg block dark:hidden"></i>
                </button>
            </div>
        </div>
    </nav>

    <main class="flex-grow">
        <div class="pt-32 max-w-7xl mx-auto px-6 mb-32 min-h-[80vh] flex flex-col">
            <!-- Header -->
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-8 reveal-up">
                <div>
                    <div class="flex items-center gap-4 mb-2">
                        <a href="/" class="inline-flex items-center justify-center w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-500 hover:text-[var(--color-accent)] transition-colors">
                            <i class="ph ph-arrow-left text-xl"></i>
                        </a>
                        <h1 class="text-4xl md:text-5xl font-display font-bold">{title}</h1>
                    </div>
                    <p class="text-[var(--color-text-secondary)] text-lg ml-14 max-w-2xl">Interactive Physics Experiment</p>
                </div>
            </div>

            <!-- Game Container -->
            <div class="relative w-full flex-grow min-h-[60vh] rounded-3xl overflow-hidden bg-black border border-gray-200 dark:border-gray-800 shadow-2xl reveal-up" style="transition-delay: 0.2s;">
{project_canvas}
            </div>
        </div>
    </main>

    <footer class="py-8 text-center text-sm text-gray-500 dark:text-gray-400 border-t border-gray-200 dark:border-gray-800">
        <div class="mx-auto max-w-7xl px-6">
            <p>&copy; 2026 | Made with <i class="ph-fill ph-heart text-red-500 mx-1"></i> by Fadhil</p>
        </div>
    </footer>

    <script>
        const themeToggleBtn = document.getElementById('theme-toggle');
        if (themeToggleBtn) {{
            themeToggleBtn.addEventListener('click', () => {{
                if (document.documentElement.classList.contains('dark')) {{
                    document.documentElement.classList.remove('dark');
                    localStorage.theme = 'light';
                }} else {{
                    document.documentElement.classList.add('dark');
                    localStorage.theme = 'dark';
                }}
            }});
        }}
    </script>
{shared_audio}
{project_scripts}
</body>
</html>"""

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(projects_dir):
    if not filename.endswith('.html'):
        continue
    slug = filename.replace('.html', '')
    title = slug.replace('-', ' ').title()

    with open(os.path.join(projects_dir, filename), 'r', encoding='utf-8') as f:
        proj_html = f.read()

    # Extract blocks from individual project
    proj_canvas = re.search(r'{%\s*block project_canvas\s*%}(.*?){%\s*endblock\s*%}', proj_html, re.DOTALL)
    proj_canvas_html = proj_canvas.group(1).strip() if proj_canvas else ''

    proj_scripts = re.search(r'{%\s*block project_scripts\s*%}(.*?){%\s*endblock\s*%}', proj_html, re.DOTALL)
    proj_scripts_html = proj_scripts.group(1).strip() if proj_scripts else ''

    # Generate the final HTML
    final_html = TEMPLATE.format(
        title=title,
        css_variables=CSS_VARIABLES,
        project_canvas=proj_canvas_html,
        shared_audio=SHARED_AUDIO_ENGINE,
        project_scripts=proj_scripts_html,
    )

    proj_out_dir = os.path.join(output_dir, slug)
    os.makedirs(proj_out_dir, exist_ok=True)
    with open(os.path.join(proj_out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"  [OK] Generated {slug}/index.html")

print("\n[DONE] All mini-projects compiled successfully.")
