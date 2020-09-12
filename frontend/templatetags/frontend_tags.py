from django import template

register = template.Library()

@register.inclusion_tag('ld-heuft-charts.html', takes_context=True)
def load_heuft_charts(context):
    return context
