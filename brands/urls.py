from django.urls import path
from .views import brand_list

app_name = 'brands'

urlpatterns = [
    path('', brand_list, name='brand-list'),
]
