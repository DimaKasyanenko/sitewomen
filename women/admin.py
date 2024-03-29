from django.contrib import admin, messages
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.utils.safestring import mark_safe

from .models import Women, Category, TagPost, Husband


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'slug', 'photo', 'post_photo', 'category', 'husband', 'tags', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('post_photo', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('title', 'post_photo', 'category', 'is_published', 'created_at', 'updated_at', 'slug')
    list_filter = (MarriedFilter, 'category', 'is_published', 'created_at', 'tags')
    list_editable = ('is_published',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_per_page = 10
    save_on_top = True
    actions_on_top = True
    actions = ('set_published', 'set_draft')

    @admin.display(description='Изображение')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)

    def get_queryset(self, request):
        qs = Women.objects.all()
        return qs


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ('tag', 'slug',)


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)
