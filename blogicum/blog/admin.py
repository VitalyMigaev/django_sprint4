from django.contrib import admin

from .models import Post, Comment, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'author',
        'pub_date',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'text',
        'category'
    )
    search_fields = ('title', 'text')
    list_filter = ('category', 'author')
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post',
        'text',
        'created_at',
        'is_published'
    )
    list_filter = ('author', 'post', 'is_published')
    search_fields = ('text',)
    list_editable = ('is_published',)
    empty_value_display = 'Не задано'


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.GET.get('action') == 'publish':
            return qs.filter(is_published=False)
        elif request.GET.get('action') == 'clean':
            return qs.filter(is_published=True)
        else:
            return qs.filter(is_published=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published',)
    empty_value_display = 'Не задано'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = 'Не задано'
