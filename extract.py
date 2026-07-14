import os
import re

def extract_project(slug, view_id, func_name, source_path, dest_dir):
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract HTML
    # We want everything between <div id="view_id" class="app-view"> and the next <div id="something-view" or <script>
    pattern_html = re.compile(rf'<div id="{view_id}" class="app-view">(.*?)</div>\s*<div id="[a-z]+-view"', re.DOTALL)
    match_html = pattern_html.search(content)
    
    if not match_html:
        # Try finding until script tag if it's the last one
        pattern_html = re.compile(rf'<div id="{view_id}" class="app-view">(.*?)</div>\s*<script>', re.DOTALL)
        match_html = pattern_html.search(content)

    html_content = match_html.group(1) if match_html else ""
    # Remove the project-header because it's already in base template
    html_content = re.sub(r'<div class="project-header">.*?</div>', '', html_content, flags=re.DOTALL)

    # Extract JS function
    # Match function func_name() { ... }
    # We will just find 'function func_name() {' and grab everything until the next 'function start' or 'const dot = '
    pattern_js = re.compile(rf'function {func_name}\(\) {{(.*?)\n        function start[A-Z]', re.DOTALL)
    match_js = pattern_js.search(content)
    if not match_js:
        pattern_js = re.compile(rf'function {func_name}\(\) {{(.*?)\n        const dot = ', re.DOTALL)
        match_js = pattern_js.search(content)

    js_content = match_js.group(1) if match_js else ""

    template = f"""{{% extends "core/mini_project_base.html" %}}
{{% block content %}}
<div class="app-view active" id="{view_id}">
    {{{{ html_content }}}}
</div>
{{% endblock %}}

{{% block extra_scripts %}}
<script>
    (function() {{
        {js_content}
    }})();
</script>
{{% endblock %}}
"""
    # Replace {{ html_content }} safely to avoid python format errors
    template = template.replace('{{ html_content }}', html_content)
    
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(dest_dir, f"{slug}.html"), 'w', encoding='utf-8') as out:
        out.write(template)

def run():
    source = r"C:\Users\vavac\portfolio\index.html"
    dest = r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects"
    
    projects = [
        ("aether", "aether-view", "startAetherEngine"),
        ("chroma", "chroma-view", "startChromaStudio"),
        ("typing-defender", "typing-view", "startTypingDefender"),
        ("gravity-golf", "golf-view", "startGravityGolfPhysics"),
        ("cyber-striker", "striker-view", "startCyberStriker"),
        ("glyph-matrix", "glyph-view", "startGlyphMatrixLab")
    ]
    
    for slug, vid, fname in projects:
        try:
            extract_project(slug, vid, fname, source, dest)
            print(f"Extracted {slug}")
        except Exception as e:
            print(f"Error extracting {slug}: {e}")

if __name__ == "__main__":
    run()
