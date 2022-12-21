
from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.conf import settings

from user_log_reg.models import Profile


class Category(models.Model):
    name = models.CharField(
        unique = True,
        max_length = 100,
    )
    slug = models.SlugField(
        verbose_name = ("safe URL"),
        max_length = 255,
    )
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = 'product',
        on_delete = models.CASCADE
        )
    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    image = models.ImageField(
        upload_to = 'product/',
        default = 'front/img/default_img.png',
        )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)  
    date_created = models.DateTimeField(auto_now_add=True)
    on_sale = models.BooleanField(default=False)
    before_sale = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal(0.00))
    slug = models.SlugField(
        verbose_name = ("safe URL"),
        max_length = 255,
        default = 'URL_' 
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', args=[self.slug])

class Sizes(models.Model):
    id_product = models.ForeignKey(
        Product,
        related_name='rozmiar',
        on_delete=models.CASCADE
    )

    name_size = models.CharField(max_length=3)

    quantity_size = models.IntegerField(default=0)
    
    def __str__(self):
        return self.id_product.title +" "+ self.name_size


#jeden element zamówienia
class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

#całe zamowienie
class Cart(models.Model):
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)


    def get_sum_cart(self):
        return sum(item.product.price for item in self.items.all())

    def get_cart_items(self):
        return self.items.all()

    def __str__(self):
        return '{0}'.format(self.owner)

