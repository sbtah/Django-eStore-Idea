from django.contrib import admin
from .models import Order


@admin.register(Order)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'created', 'status')
    ordering = ('status', 'customer')
    list_filter = ('created', 'customer', 'status',)
    search_fields = ('status',)
