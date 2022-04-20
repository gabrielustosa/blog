from django.contrib import admin

from blog.apps.authors.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']