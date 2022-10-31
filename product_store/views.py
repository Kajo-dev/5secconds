
from django.shortcuts import render , get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from user_log_reg.models import Profile
from product_store.models import Order, OrderItem


def product_sell(request):
    products = Product.objects.all() 
    for_front = {'products':products}
    return render(request,'sellsite.html',for_front)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    for_front = {'product':product}
    return render(request, 'detail_product.html', for_front)
    
def my_orders(request):
    user_profile = Profile.objects.filter(user=request.user).first()
    orders = Order.objects.filter(owner=user_profile)
    for_front={
        'user_orders' : orders
    }
    return render(request,'my_orders.html', for_front)

def add_to_cart(request,**kwargs):
    user_profile = get_object_or_404(Profile,user=request.user)
    product = Product.objects.filter(id=kwargs.get('product_id', "")).first()

    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile)
    user_order.items.add(order_item)
    if status:
        user_order.save()

    return redirect('sellsite_page')


