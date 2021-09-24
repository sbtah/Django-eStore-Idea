import django_filters
from django import forms
from .models import Product


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = Product
        fields = ['name', 'brand', 'category', 'price']
