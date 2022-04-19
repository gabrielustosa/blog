from django.contrib import admin

from blog.apps.posts.models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
