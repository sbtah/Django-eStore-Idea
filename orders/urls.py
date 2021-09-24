from django.urls import path
from .views import order_create, order_create_customer, order_detail, order_list, order_update, order_delete, order_create_customer

app_name = 'orders'

urlpatterns = [
    path('', order_list, name='order-list'),
    path('<int:pk>/', order_detail, name='order-detail'),

    path('create/', order_create, name='order-create'),
    path('create/<int:pk>', order_create_customer, name='order-create-customer'),
    path('update/<int:pk>', order_update, name='order-update'),
    path('delete/<int:pk>', order_delete, name='order-delete'),

]
