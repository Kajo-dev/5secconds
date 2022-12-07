from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from user_log_reg import views as user_log_reg_views
from home import views as home_views
from product_store import views as product_store_views

urlpatterns = [
    path('admin', admin.site.urls),
    
    path('register',user_log_reg_views.register_page, name='register_page'),
    path('login',user_log_reg_views.login_page, name='login_page'),
    path('logout',user_log_reg_views.logout_page, name='logout_page'),
    path('activate/<uidb64>/<token>', user_log_reg_views.activate, name='activate'),

    path('',home_views.home_page, name='home_page'),

    path('cart',product_store_views.my_cart, name='cart_page'),
    path('orders',product_store_views.my_orders, name='orders_page'),
    path('sellsite',product_store_views.product_sell, name='sellsite_page'),
    path('<slug:slug>', product_store_views.product_detail, name='detail_page'),
    path('add_to_cart/<int:product_id>/', product_store_views.add_to_cart, name='add_to_cart'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
