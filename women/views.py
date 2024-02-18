from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from women.forms import AddPostForm, UploadFileForm
from women.models import Women, Category, TagPost, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]


# cats_db = [
#     {'id': 1, 'name': 'Актрисы'},
#     {'id': 2, 'name': 'Певицы'},
#     {'id': 3, 'name': 'Спортсменки'},
# ]


# def index(request):
#     posts = Women.published.all().select_related('category', )
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'posts': posts,
#         'category_selected': 0,
#     }
#     return render(request, 'women/index.html', context=data)


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'category_selected': 0,
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['menu'] = menu
    #     context['posts'] = Women.published.all().select_related('category', )
    #     context['category_selected'] = int(self.request.GET.get('category_selected', 0))
    #     return context


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
    posts = Women.published.filter(category_id=category.pk).select_related('category')
    data = {
        'title': f'Рубрика: {category.title}',
        'menu': menu,
        'posts': posts,
        'category_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


class WomenCategory(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['posts'][0].category
        context['title'] = 'Категория - ' + category.title
        context['menu'] = menu
        context['category_selected'] = category.pk
        return context


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('category')
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'category_selected': None,
    }
    return render(request, 'women/index.html', context=data)


class WomenTags(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = context['posts'][0].tags
        context['title'] = 'Тег - ' + tags.tag
        context['menu'] = menu
        return context


# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=request.FILES['file'])
            fp.save()
    else:
        form = UploadFileForm()
    data = {
        'title': 'О сайте',
        'menu': menu,
        'form': form,
    }
    return render(request, 'women/about.html', context=data)


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # # print(form.cleaned_data)
#             # try:
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     data = {
#         'menu': menu,
#         'title': 'Добавление статьи',
#         'form': form
#     }
#     return render(request, 'women/addpage.html', data)


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form
        }
        return render(request, 'women/addpage.html', data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'menu': menu,
            'title': 'Добавление статьи',
            'form': form
        }
        return render(request, 'women/addpage.html', data)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Страница авторизации")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")
