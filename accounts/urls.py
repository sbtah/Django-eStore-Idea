from django.urls import path
from .views import register_user, login_user


app_name = 'accounts'


urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
]
