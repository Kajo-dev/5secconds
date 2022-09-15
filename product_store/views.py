from django.shortcuts import render

# Create your views here.

def product_sell(request):
    return render(request,'sellsite.html',{})