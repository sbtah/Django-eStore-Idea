from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib import messages
from django.urls import reverse
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

    total_orders = related_orders.count() / 100

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
            messages.success(request, ('Product created.'))
            return redirect('products:product-list')

    return render(request, 'products/product_create.html', {

        'form': form,

    })


def product_update(request, pk):

    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, ('Product updated.'))
            return HttpResponseRedirect(reverse('products:product-detail', args=[product.pk]))

    return render(request, 'products/product_create.html', {

        'form': form,

    })
