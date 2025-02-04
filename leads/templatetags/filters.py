from django.utils.translation import gettext
from django import template

register = template.Library()
@register.filter(name='template_trans')
def template_trans(text):
    try:
        return gettext(text)
    except Exception:
        return text