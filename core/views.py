from django.shortcuts import render
from orders.models import Order
from customers.models import Customer


def home_page(request):

    return render(request, 'core/home_page.html', {})


def dashboard(request):

    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='DELIVERED').count()
    pending = orders.filter(status='PENDING').count()

    return render(request, 'core/dashboard.html', {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,

    })
