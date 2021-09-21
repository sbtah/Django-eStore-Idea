from django.db import models
from django.urls import reverse


class Customer(models.Model):

    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    address = models.TextField()
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} : {self.email}"

    def get_absolute_url(self):

        return reverse('customers:customer-detail', kwargs={
            'pk': self.pk,
        })
