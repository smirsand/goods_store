from django.contrib import admin

from main_app.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)
