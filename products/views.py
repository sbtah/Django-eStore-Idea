from django.shortcuts import render
from .models import Product


# All Products.
def product_list(request):

    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):

    product = Product.objects.get(pk=pk)

    related_orders = product.order_set.all()

    total_orders = related_orders.count()

    return render(request, 'products/product_detail.html', {

        'product': product,
        'related_orders': related_orders,
        'total_orders': total_orders,

    })
