import os
import re

def fix_imports(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all <Icon /> tags by looking for capital letters at start of tag
    # e.g. <ArrowUpRight ... />
    used = set()
    matches = re.finditer(r'<([A-Z][a-zA-Z]+)(?:\s|>)', content)
    for match in matches:
        tag = match.group(1)
        if tag not in ["Image", "Script"]: # Ignore Next.js standard components
            used.add(tag)
            
    if not used:
        return

    # Check if already imported
    if "@phosphor-icons/react" in content:
        return

    import_statements = []
    for icon in sorted(used):
        if icon == "ImageIcon":
            import_statements.append(f'import {{ Image as ImageIcon }} from "@phosphor-icons/react/dist/ssr/{icon}";')
        else:
            import_statements.append(f'import {{ {icon} }} from "@phosphor-icons/react/dist/ssr/{icon}";')
            
    import_str = "\\n".join(import_statements) + "\\n"
    
    # Insert right after the last import statement
    import_matches = list(re.finditer(r'^import .*?;(?:\\r?\\n)?', content, re.MULTILINE))
    if import_matches:
        last_import = import_matches[-1]
        insert_pos = last_import.end()
        new_content = content[:insert_pos] + import_str + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added {len(used)} imports to {filepath}")

fix_imports("c:\\\\Users\\\\vavac\\\\OneDrive\\\\Desktop\\\\port\\\\src\\\\app\\\\page.tsx")
fix_imports("c:\\\\Users\\\\vavac\\\\OneDrive\\\\Desktop\\\\port\\\\src\\\\app\\\\layout.tsx")
