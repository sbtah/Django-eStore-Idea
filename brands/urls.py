from django.urls import path
from .views import brand_list, brand_create, brand_detail, brand_update, brand_delete

app_name = 'brands'

urlpatterns = [
    path('', brand_list, name='brand-list'),
    path('<int:pk>/', brand_detail, name='brand-detail'),
    path('create/', brand_create, name='brand-create'),
    path('update/<int:pk>/', brand_update, name='brand-update'),
    path('delete/<int:pk>/', brand_delete, name='brand-delete'),
]
