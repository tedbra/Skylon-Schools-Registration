from django import template

register = template.Library()

@register.filter

def last_three_lines(value):
    lines = value.split('\n')
    return '\n'.join(lines[-3:])
