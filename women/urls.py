from django.urls import path, register_converter
from .views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', WomenTags.as_view(), name='tag'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', login, name='login'),
]
