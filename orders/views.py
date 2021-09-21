from django.shortcuts import render
from .models import Order


def order_list(request):

    orders = Order.objects.all()

    return render(request, 'orders/order_list.html', {

        'orders': orders,
    })


def order_detail(request, pk):

    order = Order.objects.get(pk=pk)
    orders = Order.objects.all()
    total_orders = orders.count()

    return render(request, 'orders/order_detail.html', {

        'order': order,
        'total_orders': total_orders,

    })
