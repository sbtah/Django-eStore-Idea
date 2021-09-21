from customers.models import Customer
from django.shortcuts import render


def customer_list(request):

    customers = Customer.objects.all()

    return render(request, 'customers/customer_list.html', {
        'customers': customers,
    })


def customer_detail(request, pk):

    customer = Customer.objects.get(pk=pk)
    related_orders = customer.order_set.all()
    total_orders = related_orders.count()

    return render(request, 'customers/customer_detail.html', {
        'customer': customer,
        'related_orders': related_orders,
        'total_orders': total_orders,
    })
