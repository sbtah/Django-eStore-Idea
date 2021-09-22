from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['brand'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['tag'].widget.attrs.update(
            {'class': 'form-control'})

    price = forms.DecimalField(
        required=False, max_digits=6, decimal_places=2, min_value=0)

    class Meta:

        model = Product
        fields = '__all__'

        widgets = {
            'price': forms.NumberInput(attrs={}),
        }
