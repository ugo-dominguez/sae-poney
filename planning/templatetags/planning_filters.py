from django import template


register = template.Library()


@register.filter
def hour(date, duree=0):
    return date.hour + duree