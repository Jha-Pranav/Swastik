from django import template

register = template.Library()

@register.simple_tag
def underscoreTag(obj, attribute):
    obj = dict(obj)
    return obj.get(attribute)

@register.filter
def get_field_value(obj, field_name):
    return getattr(obj, field_name)