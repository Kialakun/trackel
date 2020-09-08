from django import template

register = template.Library()

@register.inclusion_tag('ld-heuft-charts.html')
def load_heuft_charts():
    return 
