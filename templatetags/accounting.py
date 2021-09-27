from django import template

from accounting import display

register = template.Library()

@register.filter
def currency(amount):
    return display.currency(amount)