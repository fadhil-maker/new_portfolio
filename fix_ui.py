import os
import re

def fix_ui_issues():
    # Fix base.html (Mobile Nav & Padding)
    base_html = r"c:\Users\vavac\OneDrive\Desktop\port\templates\base.html"
    with open(base_html, 'r', encoding='utf-8') as f:
        content = f.read()

    # Increase padding to prevent overlap
    content = content.replace(
        '<body class="relative flex min-h-screen flex-col overflow-x-hidden selection:bg-[var(--color-accent)] selection:text-black">',
        '<body class="relative flex min-h-screen flex-col overflow-x-hidden pt-24 selection:bg-[var(--color-accent)] selection:text-black">'
    )

    # Add mobile hamburger menu
    old_nav = """                <div class="flex items-center gap-6">
                    <div class="hidden md:flex items-center gap-6 text-sm font-medium">
                        <a href="#about" class="hover:text-[var(--color-accent)] transition-colors">About</a>
                        <a href="#experience" class="hover:text-[var(--color-accent)] transition-colors">Experience</a>
                        <a href="#works" class="hover:text-[var(--color-accent)] transition-colors">Works</a>
                    </div>
                    
                    <button id="theme-toggle" class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors" aria-label="Toggle Dark Mode">
                        <i class="ph ph-sun text-xl hidden dark:block"></i>
                        <i class="ph ph-moon text-xl block dark:hidden"></i>
                    </button>
                </div>"""

    new_nav = """                <div class="flex items-center gap-4">
                    <div class="hidden md:flex items-center gap-6 text-sm font-medium">
                        <a href="#about" class="hover:text-[var(--color-accent)] transition-colors">About</a>
                        <a href="#experience" class="hover:text-[var(--color-accent)] transition-colors">Experience</a>
                        <a href="#works" class="hover:text-[var(--color-accent)] transition-colors">Works</a>
                    </div>
                    
                    <button id="theme-toggle" class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors" aria-label="Toggle Dark Mode">
                        <i class="ph ph-sun text-xl hidden dark:block"></i>
                        <i class="ph ph-moon text-xl block dark:hidden"></i>
                    </button>

                    <!-- Mobile Menu Button -->
                    <button id="mobile-menu-btn" class="md:hidden p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-800 transition-colors">
                        <i class="ph ph-list text-xl"></i>
                    </button>
                </div>
            </div>
            
            <!-- Mobile Menu Dropdown -->
            <div id="mobile-menu" class="hidden md:hidden glass dark:glass mt-2 p-4 rounded-2xl flex flex-col gap-4 text-sm font-medium">
                <a href="#about" class="hover:text-[var(--color-accent)] transition-colors mobile-link">About</a>
                <a href="#experience" class="hover:text-[var(--color-accent)] transition-colors mobile-link">Experience</a>
                <a href="#works" class="hover:text-[var(--color-accent)] transition-colors mobile-link">Works</a>
                <a href="#mini-projects" class="hover:text-[var(--color-accent)] transition-colors mobile-link">Mini Projects</a>
            </div>"""

    content = content.replace(old_nav, new_nav)

    # Add script for mobile menu
    if "mobile-menu-btn" in content and "document.getElementById('mobile-menu-btn')" not in content:
        script = """    <!-- Main JS -->
    <script>
        const menuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        if(menuBtn && mobileMenu) {
            menuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
            });
            document.querySelectorAll('.mobile-link').forEach(link => {
                link.addEventListener('click', () => {
                    mobileMenu.classList.add('hidden');
                });
            });
        }
    </script>
    <script src="{% static 'js/main.js' %}"></script>"""
        content = content.replace("""    <!-- Main JS -->
    <script src="{% static 'js/main.js' %}"></script>""", script)

    with open(base_html, 'w', encoding='utf-8') as f:
        f.write(content)

    # Fix index.html (Timeline dot & Image Placeholder)
    index_html = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\index.html"
    with open(index_html, 'r', encoding='utf-8') as f:
        content_idx = f.read()

    # Timeline dot fix: Ensure text doesn't overlap by adding more padding
    content_idx = content_idx.replace(
        '<div class="relative pl-8 md:pl-12 mb-16">',
        '<div class="relative pl-10 md:pl-12 mb-16">'
    )
    content_idx = content_idx.replace(
        '<div class="relative pl-8 md:pl-12">',
        '<div class="relative pl-10 md:pl-12">'
    )
    
    # Image Placeholder fix: Change ph-image to a styled fallback or nothing
    img_fallback = """                    <div class="rounded-3xl overflow-hidden aspect-video bg-black/10 border border-white/10 flex items-center justify-center">
                        {% if project.image %}
                            <img src="{{ project.image.url }}" alt="{{ project.title }}" class="w-full h-full object-cover">
                        {% else %}
                            <div class="flex flex-col items-center opacity-40">
                                <span class="font-display font-bold text-2xl tracking-widest uppercase">{{ project.title }}</span>
                            </div>
                        {% endif %}
                    </div>"""
    
    # regex replace because of exact indentation mismatches
    content_idx = re.sub(
        r'<div class="rounded-3xl overflow-hidden aspect-video[^>]*>.*?</div>',
        img_fallback,
        content_idx,
        flags=re.DOTALL
    )

    with open(index_html, 'w', encoding='utf-8') as f:
        f.write(content_idx)

if __name__ == "__main__":
    fix_ui_issues()
