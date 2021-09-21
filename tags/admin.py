from django.contrib import admin
from .models import Tag


@admin.register(Tag)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
