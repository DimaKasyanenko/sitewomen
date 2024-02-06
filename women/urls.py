from django.urls import path, register_converter
from .views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('category/<int:category_id>', category_by_id, name='category_id'),
    path('category/<slug:category_slug>', category_by_slug, name='category_slug'),
    path('archive/<year4:year>/', archive, name='archive'),
]
