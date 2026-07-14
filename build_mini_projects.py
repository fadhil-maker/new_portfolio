"""
Mini-Project Static HTML Compiler
Merges Django templates into standalone HTML files for Next.js public directory.
Uses Tailwind V4 browser CDN and inlines all CSS variables for full dark mode support.
"""
import os
import re

projects_dir = r'backend/templates/core/mini_projects'
mini_base_path = r'backend/templates/core/mini_project_base.html'
output_dir = r'public/project'

with open(mini_base_path, 'r', encoding='utf-8') as f:
    mini_base = f.read()

# Extract blocks from mini_base
content_match = re.search(r'{%\s*block content\s*%}(.*?){%\s*endblock\s*%}', mini_base, re.DOTALL)
mini_content = content_match.group(1) if content_match else ''

scripts_match = re.search(r'{%\s*block extra_scripts\s*%}(.*?)\n{%\s*endblock\s*%}', mini_base, re.DOTALL)
mini_scripts = scripts_match.group(1) if scripts_match else ''

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
{content}
    </main>

    <footer class="py-8 text-center text-sm text-gray-500 dark:text-gray-400 border-t border-gray-200 dark:border-gray-800">
        <div class="mx-auto max-w-7xl px-6">
            <p>&copy; 2024 | Made with <i class="ph-fill ph-heart text-red-500 mx-1"></i> by Fadhil</p>
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
{scripts}
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

    # Merge content: inject canvas into the mini_base content block
    merged_content = mini_content.replace('{% block project_canvas %}{% endblock %}', proj_canvas_html)
    merged_content = merged_content.replace('{{ project.title }}', title)
    merged_content = merged_content.replace('{{ project.description }}', 'Interactive Physics Experiment')
    merged_content = merged_content.replace("{% url 'core:portfolio' %}", '/')
    # Remove Django tech loop
    merged_content = re.sub(r'{%\s*for tech in project\.technologies\s*%}.*?{%\s*endfor\s*%}', '', merged_content, flags=re.DOTALL)

    # Merge scripts: inject project scripts into the mini_base script block
    merged_scripts = mini_scripts.replace('{% block project_scripts %}{% endblock %}', proj_scripts_html)

    # Generate the final HTML
    final_html = TEMPLATE.format(
        title=title,
        css_variables=CSS_VARIABLES,
        content=merged_content,
        scripts=merged_scripts,
    )

    proj_out_dir = os.path.join(output_dir, slug)
    os.makedirs(proj_out_dir, exist_ok=True)
    with open(os.path.join(proj_out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"  [OK] Generated {slug}/index.html")

print("\n[DONE] All mini-projects compiled successfully.")
