from django.contrib import admin, messages

from .models import Women, Category, TagPost, Husband


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at', 'updated_at', 'slug', 'brief_info')
    list_filter = ('is_published', 'created_at', 'tags')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_per_page = 10
    save_on_top = True
    actions_on_top = True
    actions = ['set_published', 'set_draft']

    @admin.display(description='Краткое описание', ordering='description')
    def brief_info(self, women: Women):
        return f"Описание {len(women.description)} символов."

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
