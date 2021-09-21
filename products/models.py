from django.db import models
from django.urls import reverse
from brands.models import Brand
from tags.models import Tag


class Product(models.Model):

    CATEGORY = (
        ('Karate', 'Karate'),
        ('Judo', 'Judo'),
        ('Aikido', 'Aikido'),
        ('Boxing', 'Boxing'),
        ('Muai Tai', 'Muai Tai'),
        ('Training', 'Training'),
        ('Outdoor', 'Outdoor'),
        ('Shoes', 'Shoes'),
    )

    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    brand = models.ForeignKey(
        Brand, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=120, choices=CATEGORY)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.id}: {self.name} - {self.price}"

    def get_absolute_url(self):

        return reverse('products:product-detail', kwargs={
            'pk': self.pk,
        })
