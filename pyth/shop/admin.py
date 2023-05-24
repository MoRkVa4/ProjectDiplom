from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug")
    list_display_links = ("pk", "title")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "category")
    list_display_links = ("pk", "title")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("title",)}
