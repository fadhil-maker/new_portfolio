from django import template
from django.conf import settings

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
