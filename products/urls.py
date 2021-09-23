from django.urls import path
from .views import product_list, product_detail, product_create, product_update, product_delete


app_name = 'products'

urlpatterns = [
    path('', product_list, name='product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('create/', product_create, name='product-create'),
    path('update/<int:pk>/', product_update, name='product-update'),
    path('delete/<int:pk>/', product_delete, name='product-delete'),
]
