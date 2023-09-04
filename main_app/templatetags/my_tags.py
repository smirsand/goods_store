from django import template

register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.simple_tag
def mediapath(image):
    if image:
        return f'/media/{image}'
    return '#'
