from .. import get_option
from django import template
register = template.Library()


@register.simple_tag()
def option(name, default=None):
    return get_option(name, default)
