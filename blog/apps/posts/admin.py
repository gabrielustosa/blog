from django.contrib import admin

from blog.apps.posts.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Category)
