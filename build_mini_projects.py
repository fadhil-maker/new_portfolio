import os
import re

base_path = r'backend/templates/base.html'
mini_base_path = r'backend/templates/core/mini_project_base.html'
projects_dir = r'backend/templates/core/mini_projects'
output_dir = r'public/project'

with open(base_path, 'r', encoding='utf-8') as f:
    base_html = f.read()

with open(mini_base_path, 'r', encoding='utf-8') as f:
    mini_base = f.read()

base_html = base_html.replace('{% load static %}', '')
base_html = base_html.replace('{% load media_tags %}', '')
base_html = base_html.replace('{% static ''img/logo.png'' %}', '/img/logo.png')
base_html = base_html.replace('{% url ''core:portfolio'' %}', '/')
base_html = re.sub(r'{% include "core/inline_styles.html" %}', '', base_html)
base_html = re.sub(r'{%.*?%}', '', base_html)

content_match = re.search(r'{%\s*block content\s*%}(.*?){%\s*endblock\s*%}', mini_base, re.DOTALL)
mini_content = content_match.group(1) if content_match else ''
scripts_match = re.search(r'{%\s*block extra_scripts\s*%}(.*?){%\s*endblock\s*%}', mini_base, re.DOTALL)
mini_scripts = scripts_match.group(1) if scripts_match else ''

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(projects_dir):
    if not filename.endswith('.html'): continue
    slug = filename.replace('.html', '')
    
    with open(os.path.join(projects_dir, filename), 'r', encoding='utf-8') as f:
        proj_html = f.read()
    
    proj_canvas = re.search(r'{%\s*block project_canvas\s*%}(.*?){%\s*endblock\s*%}', proj_html, re.DOTALL)
    proj_canvas_html = proj_canvas.group(1) if proj_canvas else ''
    
    proj_scripts = re.search(r'{%\s*block project_scripts\s*%}(.*?){%\s*endblock\s*%}', proj_html, re.DOTALL)
    proj_scripts_html = proj_scripts.group(1) if proj_scripts else ''
    
    merged_content = mini_content.replace('{% block project_canvas %}{% endblock %}', proj_canvas_html)
    merged_content = merged_content.replace('{{ project.title }}', slug.replace('-', ' ').title())
    merged_content = merged_content.replace('{{ project.description }}', 'Interactive Physics Experiment')
    merged_content = re.sub(r'{%\s*for tech in project.technologies\s*%}.*?{%\s*endfor\s*%}', '', merged_content, flags=re.DOTALL)
    
    merged_scripts = mini_scripts.replace('{% block project_scripts %}{% endblock %}', proj_scripts_html)
    
    final_html = base_html.replace('<body>', '<body class="relative flex min-h-screen flex-col overflow-x-hidden pt-24 selection:bg-[var(--color-accent)] selection:text-black">')
    final_html = final_html.replace('<main class="flex-grow">', f'<main class="flex-grow">{merged_content}')
    final_html = final_html.replace('</body>', f'{merged_scripts}</body>')
    final_html = final_html.replace('</head>', '<script src="https://cdn.tailwindcss.com"></script><link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@500;700;900&display=swap" rel="stylesheet"></head>')
    
    proj_out_dir = os.path.join(output_dir, slug)
    os.makedirs(proj_out_dir, exist_ok=True)
    with open(os.path.join(proj_out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Generated {slug}/index.html")

print("Success")
