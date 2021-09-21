from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class LocationAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'phone', 'address', 'email', 'created')
    ordering = ('full_name',)
    search_fields = ('full_name', 'email', 'address',)
