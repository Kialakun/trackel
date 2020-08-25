from django import template

register = template.Library()

@register.inclusion_tag('forms.html', takes_context=True)
def render_trackel_form(context):
    return context
