from django.urls import path, register_converter
from .views import *
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:category_slug>/', WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', TagPostList.as_view(), name='tag'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('edit/<slug:slug>/', UpdatePage.as_view(), name='edit_page'),
    path('delete/<slug:slug>/', DeletePage.as_view(), name='edit_page'),
    path('login/', login, name='login'),
]
