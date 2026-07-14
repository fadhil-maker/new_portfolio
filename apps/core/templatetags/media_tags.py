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
        if not 'f_auto' in url and not url.lower().endswith('.pdf'):
            url = url.replace('/upload/', '/upload/f_auto,q_auto/')
            
    return url
