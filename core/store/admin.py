from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated', 'category', 'subcategory']
    list_filter = ['in_stock', 'is_active', 'category', 'subcategory']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug':('title',)}