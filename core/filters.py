import django_filters
from orders.models import Order


class OrderFilter(django_filters.FilterSet):

    # def __ini__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['customer'].widget.attrs.update(
    #         {'class': 'form-control', })

    class Meta:

        model = Order
        fields = '__all__'
