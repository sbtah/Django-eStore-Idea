from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('customers/', include('customers.urls', namespace='customers')),
    path('brands/', include('brands.urls', namespace='brands')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('authentication/', include('accounts.urls', namespace='accounts')),
]


# Adding STATIC and MEDIA
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)


admin.site.site_header = "shisaStore"
