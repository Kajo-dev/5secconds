from django.contrib import admin
from django.urls import path

from user_log_reg import views as user_log_reg_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',user_log_reg_views.register_page,name='register_page'),
    path('login/',user_log_reg_views.login_page,name='login_page'),
    path('logout/',user_log_reg_views.logout_page,name='logout_page'),

    path('home/',home_views.home_page,name='home_page'),
]
