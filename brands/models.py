from django.db import models
from django.urls import reverse


class Brand(models.Model):

    name = models.CharField(max_length=120)
    address = models.TextField()
    phone = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brands:brand-detail', kwargs={
            'pk': self.pk,
        })
