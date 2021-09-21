from django.shortcuts import render
from .models import Product


# All Products.
def product_list(request):

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)
