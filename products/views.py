from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Product
from .forms import ProductForm
from .filters import ProductFilter
from orders.filters import OrderFilter1, OrderFilter2


# All Products.
def product_list(request):

    products = Product.objects.all()
    my_filter = ProductFilter(request.GET, queryset=products)
    products = my_filter.qs

    context = {
        'my_filter': my_filter,
        'products': products,
    }

    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):

    product = Product.objects.get(pk=pk)
    related_orders = product.order_set.all()
    total_orders = related_orders.count() / 100

    my_filter = OrderFilter2(request.GET, queryset=related_orders)
    related_orders = my_filter.qs

    return render(request, 'products/product_detail.html', {

        'product': product,
        'related_orders': related_orders,
        'total_orders': total_orders,
        'my_filter': my_filter,

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


def product_delete(request, pk):

    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        product.delete()
        messages.success(request, ('Product deleted.'))
        return redirect('products:product-list')

    return render(request, 'products/product_delete.html', {

        'product': product,

    })
