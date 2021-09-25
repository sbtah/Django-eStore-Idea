from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})

    class Meta:

        model = User
        fields = ('username', 'email', 'password1', 'password2',)
