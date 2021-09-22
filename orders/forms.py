from django.forms import ModelForm
from django import forms
from .models import Order


class OrderForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].widget.attrs.update(
            {'class': 'form-control', })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].widget.attrs.update(
            {'class': 'form-control', })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update(
            {'class': 'form-control', })

    class Meta:

        model = Order

        fields = '__all__'

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Customer'}),
            'product': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Product'}),
        }
