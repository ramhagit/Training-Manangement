from django import template

register = template.Library()


@register.filter
def to_letter(value):
    d = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
    }
    return d[value]
