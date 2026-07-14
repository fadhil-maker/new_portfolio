import re

gg = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html'
with open(gg, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r"getElementById\(['\"]golf-hud-overlay['\"]\)", "getElementById('gg-overlay')", content)
content = re.sub(r"getElementById\(['\"]gg-end-icon['\"]\)", "getElementById('gg-screen-title')", content) # fallback to a valid element to avoid null crash

with open(gg, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Gravity Golf JS!")
