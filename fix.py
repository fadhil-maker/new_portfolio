import os
import glob

def fix():
    files = glob.glob(r"c:\Users\vavac\OneDrive\Desktop\port\templates\core\mini_projects\*.html")
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace '}\n\n    })();' with '\n    })();'
        # Or more robustly, find the last '}' before '})();'
        # Let's just find `        }\n\n    })();`
        
        # Actually, let's just find the last '}' inside the IIFE and remove it.
        if "        }\n\n    })();" in content:
            content = content.replace("        }\n\n    })();", "\n    })();")
        elif "        }\n    })();" in content:
             content = content.replace("        }\n    })();", "\n    })();")
             
        # Just to be sure, let's regex it
        import re
        content = re.sub(r'\}\s*\)\(\);\s*</script>', '\n    })();\n</script>', content)

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed {os.path.basename(f)}")

if __name__ == "__main__":
    fix()
