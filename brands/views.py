from django.shortcuts import render


def brand_list(request):

    return render(request, 'brands/brand_list.html', {})
