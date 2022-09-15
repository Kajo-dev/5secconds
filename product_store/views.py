from itertools import product
from django.shortcuts import render
from .models import *

def product_sell(request):
    products = Product.objects.all() 
    for_front = {'products':products}
    return render(request,'sellsite.html',for_front )