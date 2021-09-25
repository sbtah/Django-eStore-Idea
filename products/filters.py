import django_filters
from django_filters import DateFilter
from .models import Product


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = Product
        fields = ['name', 'brand', 'category', 'price']


class ProductFilterForModel(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = Product
        fields = ['name', 'brand', 'category', 'price']
        exclude = ['brand']
