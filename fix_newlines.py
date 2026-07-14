import os

def fix_newlines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('\\n', '\n')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed literal \\n in {filepath}")

fix_newlines("c:\\\\Users\\\\vavac\\\\OneDrive\\\\Desktop\\\\port\\\\src\\\\app\\\\page.tsx")
fix_newlines("c:\\\\Users\\\\vavac\\\\OneDrive\\\\Desktop\\\\port\\\\src\\\\app\\\\layout.tsx")
