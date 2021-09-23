from django.urls import path
from .views import customer_detail, customer_list, customer_create, customer_update, customer_delete


app_name = 'customers'

urlpatterns = [
    path('', customer_list, name='customer-list'),
    path('<int:pk>/', customer_detail, name='customer-detail'),
    path('create/', customer_create, name='customer-create'),
    path('update/<int:pk>', customer_update, name='customer-update'),
    path('delete/<int:pk>', customer_delete, name='customer-delete'),
]
