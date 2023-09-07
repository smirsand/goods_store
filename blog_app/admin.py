from django.contrib import admin

from blog_app.models import Blog


@admin.register(Blog)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('header', 'content',)
