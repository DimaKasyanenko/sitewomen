from django.urls import path, register_converter
from .views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', addpage, name='add_page'),
    path('login/', login, name='login'),
]
