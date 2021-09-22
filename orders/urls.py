from django.urls import path
from .views import order_create, order_detail, order_list

app_name = 'orders'

urlpatterns = [
    path('', order_list, name='order-list'),
    path('<int:pk>/', order_detail, name='order-detail'),
    path('create/', order_create, name='order-create'),
]
