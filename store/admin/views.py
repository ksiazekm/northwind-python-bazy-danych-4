from django.shortcuts import render
from django.http.response import HttpResponse
from customers.models import Products
from .forms import SubmitSearchForm

def index(request):
    all_products = Products.objects.all()


    context = {
        'products': all_products
    }

    return render(request, 'dashboard.html', context)


def products(request):

    form = SubmitSearchForm(request.GET)

    data = None
    if form.is_valid():
        data = form.cleaned_data

    if data is not None:
        print(data)
        products = Products.objects.filter(productname__contains=data['name'])
    else:
        products = Products.objects.all()

    context = {
        'form': form,
        'products': products
    }

    return render(request, 'products.html', context)