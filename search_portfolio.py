import re
with open('C:/Users/vavac/portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
    emails = re.findall(r'mailto:([^"\']+)', content)
    photos = re.findall(r'<img.*?src=["\']([^"\']+)["\']', content)
    print("Emails:", emails)
    print("Photos:", photos)
