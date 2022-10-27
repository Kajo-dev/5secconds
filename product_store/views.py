
from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from user_log_reg.models import Profile
from product_store.models import Order, OrderItem


def product_sell(request):
    products = Product.objects.all() 
    for_front = {'products':products}
    return render(request,'sellsite.html',for_front )

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    for_front = {'product':product}
    return render(request, 'detail_product.html', for_front)
    

def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile,user=request.user)
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()


    order_item = OrderItem.objects.get_or_create(product=product)
    user_order = Order.objects.get_or_create(owner=user_profile, is_ordered=False)

    return redirect('sellsite_page')


