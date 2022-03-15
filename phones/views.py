from django.shortcuts import render, redirect
from phones import models


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort', '')
    if sorting == 'name':
        phones = list(models.Phone.objects.all().order_by('name'))
    elif sorting == 'min_price':
        phones = list(models.Phone.objects.all().order_by('price'))
    elif sorting == 'max_price':
        phones = reversed(list(models.Phone.objects.all().order_by('price')))
    else:
        phones = list(models.Phone.objects.all())
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = list(models.Phone.objects.filter(slug=slug))[0]
    context = {'phone': phone}
    return render(request, template, context)
