from django.urls import path
from .views import brand_list, brand_create, brand_detail

app_name = 'brands'

urlpatterns = [
    path('', brand_list, name='brand-list'),
    path('<int:pk>/', brand_detail, name='brand-detail'),
    path('create/', brand_create, name='brand-create'),
]
