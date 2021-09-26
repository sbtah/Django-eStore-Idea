import django_filters
from django_filters import DateFilter
from .models import Order


class OrderFilter(django_filters.FilterSet):

    start_date = DateFilter(field_name='created', lookup_expr='gte')

    end_date = DateFilter(field_name='created', lookup_expr='lte')

    class Meta:

        model = Order
        fields = '__all__'


class OrderFilter1(django_filters.FilterSet):

    start_date = DateFilter(field_name='created', lookup_expr='gte')

    end_date = DateFilter(field_name='created', lookup_expr='lte')

    class Meta:

        model = Order
        fields = '__all__'
        exclude = ['customer', 'created']


class OrderFilter2(django_filters.FilterSet):

    start_date = DateFilter(field_name='created', lookup_expr='gte')

    end_date = DateFilter(field_name='created', lookup_expr='lte')

    class Meta:

        model = Order
        fields = '__all__'
        exclude = ['product', 'created']
