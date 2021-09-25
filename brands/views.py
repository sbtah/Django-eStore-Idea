from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Brand
from .forms import BrandForm
from .filters import BrandFilter


def brand_list(request):

    brands = Brand.objects.all()
    my_filter = BrandFilter(request.GET, queryset=brands)
    brands = my_filter.qs

    return render(request, 'brands/brand_list.html', {

        'my_filter': my_filter,
        'brands': brands,

    })


def brand_detail(request, pk):

    brand = Brand.objects.get(pk=pk)
    related_products = brand.product_set.all()
    total_orders = related_products.count()

    return render(request, 'brands/brand_detail.html', {

        'brand': brand,
        'total_orders': total_orders,
        'related_products': related_products,

    })


def brand_create(request):

    form = BrandForm()

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Brand added.'))
            return redirect('brands:brand-list')

    return render(request, 'brands/brand_create.html', {

        'form': form,

    })


def brand_update(request, pk):

    product = Brand.objects.get(pk=pk)
    form = BrandForm(instance=product)

    if request.method == 'POST':
        form = BrandForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, ('Brand updated.'))
            return HttpResponseRedirect(reverse('brands:brand-detail', args=[product.pk]))

    return render(request, 'brands/brand_create.html', {

        'form': form,

    })


def brand_delete(request, pk):

    brand = Brand.objects.get(pk=pk)

    if request.method == 'POST':
        brand.delete()
        messages.success(request, ('Brand deleted.'))
        return redirect('brands:brand-list')

    return render(request, 'brands/brand_delete.html', {

        'brand': brand,

    })
