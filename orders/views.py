from django.forms.widgets import Select
from django.shortcuts import HttpResponseRedirect, render, redirect
from django.forms import inlineformset_factory
from django.contrib import messages
from django.urls import reverse
from .models import Order
from .forms import OrderForm
from customers.models import Customer
from .filters import OrderFilter


def order_list(request):

    orders = Order.objects.all().order_by('-created')
    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    return render(request, 'orders/order_list.html', {

        'my_filter': my_filter,
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


def order_create_customer(request, pk):

    OrderFormSet = inlineformset_factory(
        Customer,
        Order,
        fields=('product', 'status'),
        widgets={
            'product': Select(attrs={'class': 'form-control'}),
            'status': Select(attrs={'class': 'form-control'}),
        },
    )
    customer = Customer.objects.get(pk=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})

    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            messages.success(request, ('Order created.'))
            return redirect('core:dashboard')

    return render(request, 'orders/order_formset.html', {

        'formset': formset,

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


def order_delete(request, pk):

    order = Order.objects.get(pk=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('orders:order-list')

    return render(request, 'orders/order_delete.html', {

        'order': order,

    })
