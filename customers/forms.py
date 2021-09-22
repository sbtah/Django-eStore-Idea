from django import forms
from django.forms import fields
from .models import Customer


class CustomerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control', })
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', })

    class Meta:

        model = Customer
        fields = '__all__'
