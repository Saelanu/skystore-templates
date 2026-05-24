from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='mediapath')
def mediapath_filter(image_path):
    if not image_path:
        return ''
    return f'{settings.MEDIA_URL}{image_path}'

@register.simple_tag(name='mediapath')
def mediapath_tag(image_path):
    if not image_path:
        return ''
    return f'{settings.MEDIA_URL}{image_path}'