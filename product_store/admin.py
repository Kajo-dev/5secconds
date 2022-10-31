from django.contrib import admin
from product_store.models import Category,Product,Sizes,Order,OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sizes)
admin.site.register(Order)
admin.site.register(OrderItem)