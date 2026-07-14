import os
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def media_url(value):
    """
    Returns the URL for a FileField or ImageField.
    If it's a Cloudinary image URL, injects f_auto,q_auto for optimization.
    """
    if not value:
        return ''
    
    url = ''
    str_val = str(value)
    
    if str_val.startswith('http') or str_val.startswith('/static/'):
        url = str_val
    elif hasattr(value, 'url'):
        try:
            url = value.url
        except Exception:
            url = str_val
    else:
        url = f"{settings.MEDIA_URL}{str_val}"
        
    # Auto-optimize Cloudinary images
    if 'res.cloudinary.com' in url and '/upload/' in url:
        is_pdf_dir = '/resume/' in url.lower() or '/certificates/' in url.lower()
        
        # Force PDF extension if missing to prevent Cloudinary from serving it as an image
        if is_pdf_dir and not url.lower().endswith('.pdf'):
            url += '.pdf'
            
        if not 'f_auto' in url and not url.lower().endswith('.pdf') and not is_pdf_dir:
            url = url.replace('/upload/', '/upload/c_limit,w_1000,f_auto,q_auto/')
            
    return url

@register.filter
def media_url_size(value, size):
    """Returns the Cloudinary URL aggressively resized for a specific width"""
    url = media_url(value)
    if 'c_limit,w_1000' in url:
        return url.replace('c_limit,w_1000', f'c_fill,w_{size}')
    elif '/upload/' in url and not url.lower().endswith('.pdf'):
        return url.replace('/upload/', f'/upload/c_fill,w_{size},f_auto,q_auto/')
    return url

@register.simple_tag
def inline_css(path):
    """Reads a CSS file and injects it directly into the HTML to eliminate render-blocking network requests"""
    full_path = os.path.join(settings.BASE_DIR, 'static', path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return mark_safe(f"<style>{f.read()}</style>")
    except Exception:
        # Fallback to standard link if file reading fails
        static_url = f"{settings.STATIC_URL}{path}"
        return mark_safe(f'<link rel="stylesheet" href="{static_url}">')
