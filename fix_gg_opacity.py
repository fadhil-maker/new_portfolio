import os

filepath = r'c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\gravity-golf.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "document.getElementById('gg-overlay').style.opacity" in line:
        continue
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Gravity Golf opacity bug fixed!")
