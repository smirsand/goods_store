from django.contrib import admin

from main_app.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category', 'active_version')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)

    def active_version(self, obj):
        active = Version.objects.get(product=obj, version_flag=True)

        return active.version_flag

    active_version.short_description = 'Признак версии'


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'version_name', 'version_flag')
    list_filter = ('version_flag',)
