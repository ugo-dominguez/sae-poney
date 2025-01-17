from django import template


register = template.Library()


@register.filter
def hour(date, duree=0):
    return date.hour + duree

@register.filter
def contains(liste_cours, cours):
    return cours in liste_cours