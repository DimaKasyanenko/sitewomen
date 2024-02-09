from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from women.models import Women, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавать статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

# cats_db = [
#     {'id': 1, 'name': 'Актрисы'},
#     {'id': 2, 'name': 'Певицы'},
#     {'id': 3, 'name': 'Спортсменки'},
# ]


def index(request):
    posts = Women.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'category_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'category_selected': 1,
    }
    return render(request, 'women/post.html', data)


def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Women.published.filter(category_id=category.pk)
    data = {
        'title': f'Рубрика: {category.title}',
        'menu': menu,
        'posts': posts,
        'category_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'women/about.html', context=data)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Страница авторизации")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")
