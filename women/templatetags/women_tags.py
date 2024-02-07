from django import template

import women.views as views

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories(category_selected=0):
    categories = views.cats_db
    return {'categories': categories, 'category_selected': category_selected}
