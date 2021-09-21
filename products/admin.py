from django.contrib import admin
from .models import Product


@admin.register(Product)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'category', 'created',)
    ordering = ('name',)
    list_filter = ('name', 'price', 'category', 'tag',)
    search_fields = ('name',)
