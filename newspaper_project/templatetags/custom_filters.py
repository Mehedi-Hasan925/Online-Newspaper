from django import template

register = template.Library()


def range_filter(value):
    return value[0:150]+"......"

def model_name(value):
    return value.__class__.__name__
register.filter('range_filter',range_filter)
register.filter('model_name',model_name)