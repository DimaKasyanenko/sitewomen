from django.contrib import admin

from .models import Women, Category, TagPost, Husband


class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at', 'updated_at', 'slug')
    list_filter = ('is_published', 'created_at', 'tags')
    list_editable = ('category',)
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_display_links = ('title',)
    list_per_page = 10
    save_on_top = True
    actions_on_top = True

    def get_queryset(self, request):
        qs = Women.objects.all()
        return qs


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)


class TagPostAdmin(admin.ModelAdmin):
    list_display = ('tag', 'slug',)


class HusbandAdmin(admin.ModelAdmin):
    list_display = ('name', 'age',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TagPost, TagPostAdmin)
admin.site.register(Husband, HusbandAdmin)
