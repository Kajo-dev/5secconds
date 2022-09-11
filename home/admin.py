from django.contrib import admin
from user_log_reg.models import User
from product_store.models import Category,Product

admin.site.register(User)
admin.site.register(Category,Product)
