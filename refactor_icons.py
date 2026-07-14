import os
import re

def kebab_to_pascal(name):
    # e.g., arrow-up-right -> ArrowUpRight
    return "".join(word.capitalize() for word in name.split('-'))

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all <i className="..."></i>
    pattern = r'<i\s+className="([^"]+)">\s*</i>'
    
    used_icons = set()
    
    def replacer(match):
        classes = match.group(1).split()
        
        weight = "regular"
        if "ph-fill" in classes:
            weight = "fill"
            classes.remove("ph-fill")
        if "ph-bold" in classes:
            weight = "bold"
            classes.remove("ph-bold")
            
        icon_name = None
        for c in classes[:]:
            if c.startswith("ph-") and c not in ["ph", "ph-fill", "ph-bold"]:
                icon_name = c[3:] # remove 'ph-'
                classes.remove(c)
                break
        
        if "ph" in classes:
            classes.remove("ph")
            
        if not icon_name:
            return match.group(0) # Not a phosphor icon
            
        pascal_name = kebab_to_pascal(icon_name)
        if pascal_name == "Image":
            pascal_name = "ImageIcon" # Alias it
            
        used_icons.add((pascal_name, icon_name))
        
        class_str = " ".join(classes)
        props = []
        if class_str:
            props.append(f'className="{class_str}"')
        if weight != "regular":
            props.append(f'weight="{weight}"')
            
        props_str = " ".join(props)
        if props_str:
            return f'<{pascal_name} {props_str} />'
        else:
            return f'<{pascal_name} />'

    new_content = re.sub(pattern, replacer, content)
    
    # Add imports
    if used_icons and new_content != content:
        import_statements = []
        for pascal, kebab in sorted(used_icons):
            if pascal == "ImageIcon":
                import_statements.append(f'import {{ Image as ImageIcon }} from "@phosphor-icons/react/dist/ssr/{pascal}";')
            else:
                import_statements.append(f'import {{ {pascal} }} from "@phosphor-icons/react/dist/ssr/{pascal}";')
        
        # Insert imports after 'import' block
        import_str = "\\n".join(import_statements)
        
        # Find last import
        import_matches = list(re.finditer(r'^import .*?;\\n', new_content, re.MULTILINE))
        if import_matches:
            last_import = import_matches[-1]
            insert_pos = last_import.end()
            new_content = new_content[:insert_pos] + import_str + "\\n" + new_content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Refactored {filepath} with {len(used_icons)} icons.")

process_file("c:\\\\Users\\\\vavac\\\\OneDrive\\\\Desktop\\\\port\\\\src\\\\app\\\\page.tsx")
process_file("c:\\\\Users\\\\vavac\\\\OneDrive\\\\Desktop\\\\port\\\\src\\\\app\\\\layout.tsx")
