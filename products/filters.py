import django_filters
from django_filters import DateFilter
from .models import Product


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:

        model = Product
        fields = ['name', 'brand', 'category', 'price']


class OrderFilterForProduct(django_filters.FilterSet):

    start_date = DateFilter(field_name='created', lookup_expr='gte')

    end_date = DateFilter(field_name='created', lookup_expr='lte')

    class Meta:

        model = Product
        fields = '__all__'
