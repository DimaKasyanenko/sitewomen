from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

menu = ['О сайте', 'Добавать статью', 'Обратная связь', 'Войти']


def index(request):
    data = {
        'title': 'Главная',
        'menu': menu
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=data)


def category_by_id(request, category_id):
    return HttpResponse(f"Posts from category, {category_id}")


def category_by_slug(request, category_slug):
    return HttpResponse(f"Posts from category, {category_slug}")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"Archive post, {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")
