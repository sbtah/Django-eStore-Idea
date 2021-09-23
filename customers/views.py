from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Customer
from .forms import CustomerForm


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
