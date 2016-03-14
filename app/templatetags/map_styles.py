from django import template

register = template.Library()


@register.filter
def generate_style(id):
    return "#map-canvas-" + id + " {\
            width: 100% !important;\
            height: 400px !important;\
        		}"
