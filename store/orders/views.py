from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from customers.models import Orders, Shippers, Suppliers 


class IndexView(generic.ListView):
        template_name = 'orders/orders-list.html'
        context_object_name = 'orders'

        def get_queryset(self):
            return Orders.objects.order_by('-orderid')
# Create your views here.