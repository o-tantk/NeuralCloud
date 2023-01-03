from django import template

register = template.Library()

@register.simple_tag
def join_by_attr(list, attr_name, separator):
    return separator.join(getattr(i, attr_name) for i in list)