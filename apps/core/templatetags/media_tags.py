from django import template

register = template.Library()


@register.filter
def media_url(field):
    """Return the correct URL for a file field, whether it's a Cloudinary URL or local."""
    if not field:
        return ''
    field_name = str(field)
    if field_name.startswith('http'):
        return field_name
    try:
        return field.url
    except Exception:
        return field_name
