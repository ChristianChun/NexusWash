from django import template

register = template.Library()


@register.filter
def split(value, delimiter=','):
    """Splits the string by the given delimiter, handling None values."""
    if value is None:
        return []
    return value.split(delimiter)
