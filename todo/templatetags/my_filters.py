from django import template

register = template.Library()
@register.filter
def in_category(qs, category):
    return qs.filter(category=category)