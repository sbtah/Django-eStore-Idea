from django.contrib import admin
from .models import Brand


@admin.register(Brand)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    ordering = ('name',)
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('name',)
