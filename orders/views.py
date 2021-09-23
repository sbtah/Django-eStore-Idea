from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Order
from .forms import OrderForm


def order_list(request):

    orders = Order.objects.all()

    return render(request, 'orders/order_list.html', {

        'orders': orders,
    })


def order_detail(request, pk):

    order = Order.objects.get(pk=pk)
    # related_products = order.product_set.all()
    orders = Order.objects.all()
    total_orders = orders.count()

    return render(request, 'orders/order_detail.html', {

        'order': order,
        'total_orders': total_orders,
        # 'related_products': related_products,

    })


def order_create(request):

    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Order created.'))
            return redirect('core:dashboard')

    return render(request, 'orders/order_create.html', {

        'form': form,

    })


def order_update(request, pk):

    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            messages.success(request, ('Order updated.'))
            return HttpResponseRedirect(reverse('orders:order-detail', args=[order.pk]))

    return render(request, 'orders/order_create.html', {

        'form': form,

    })
