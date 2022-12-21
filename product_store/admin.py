from django.contrib import admin
from product_store.models import Category,Product,Sizes,Cart,CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sizes)
admin.site.register(Cart)
admin.site.register(CartItem)