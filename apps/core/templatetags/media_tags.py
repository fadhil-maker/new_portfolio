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
    if hasattr(value, 'url'):
        url = value.url
    elif isinstance(value, str) and value.startswith('http'):
        url = value
    else:
        url = f"{settings.MEDIA_URL}{value}"
        
    # Auto-optimize Cloudinary images
    if 'res.cloudinary.com' in url and '/upload/' in url:
        if not 'f_auto' in url and not url.lower().endswith('.pdf'):
            url = url.replace('/upload/', '/upload/f_auto,q_auto/')
            
    return url
