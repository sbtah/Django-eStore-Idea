from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


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


def product_create(request):

    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('products:product-list')

    return render(request, 'products/product_create.html', {

        'form': form,

    })
