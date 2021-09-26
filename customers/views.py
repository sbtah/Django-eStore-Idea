from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm
from .filters import CustomerFilter
from accounts.decorators import allowed_users
from orders.filters import OrderFilter1, OrderFilter2


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer_list(request):

    customers = Customer.objects.all()
    my_filter = CustomerFilter(request.GET, queryset=customers)
    customers = my_filter.qs

    return render(request, 'customers/customer_list.html', {

        'my_filter': my_filter,
        'customers': customers,
    })


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer_detail(request, pk):

    customer = Customer.objects.get(pk=pk)
    related_orders = customer.order_set.all()
    total_orders = related_orders.count()

    my_filter = OrderFilter1(request.GET, queryset=related_orders)
    related_orders = my_filter.qs

    return render(request, 'customers/customer_detail.html', {
        'customer': customer,
        'related_orders': related_orders,
        'total_orders': total_orders,
        'my_filter': my_filter,
    })


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer_create(request):

    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:dashboard')

    return render(request, 'customers/customer_create.html', {

        'form': form,

    })


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer_update(request, pk):

    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
            messages.success(request, ('Customer updated.'))
            return HttpResponseRedirect(reverse('customers:customer-detail', args=[customer.pk]))

    return render(request, 'customers/customer_create.html', {

        'form': form,

    })


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['admin'])
def customer_delete(request, pk):

    customer = Customer.objects.get(pk=pk)

    if request.method == 'POST':
        customer.delete()
        messages.success(request, ('Customer deleted.'))
        return redirect('customers:customer-list')

    return render(request, 'customers/customer_delete.html', {

        'customer': customer,

    })
