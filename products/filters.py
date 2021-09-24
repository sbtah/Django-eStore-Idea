import django_filters
from django import forms
from .models import Product


class ProductFilter(django_filters.FilterSet):

    class Meta:

        model = Product
        fields = ['name', 'brand', 'category', 'price']
