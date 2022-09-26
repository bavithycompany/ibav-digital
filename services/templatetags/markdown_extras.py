import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def markdown_filter(value):
    return markdown.markdown(value)
