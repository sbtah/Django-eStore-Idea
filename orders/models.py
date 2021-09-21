from django.db import models
from django.urls import reverse
from customers.models import Customer
from products.models import Product


class Order(models.Model):

    STATUS = (
        ('PENDING', 'PENDING'),
        ('READY', 'READY'),
        ('DELIVERED', 'DELIVERED'),
    )

    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=120, choices=STATUS)

    def __str__(self):
        return f"Order: {self.pk}, {self.product.name} : {self.status}"

    def get_absolute_url(self):
        return reverse('orders:order-detail', kwargs={
            'pk': self.pk,
        })

    def date_created(self):
        return self.created.strftime('%Y-%m-%d')
