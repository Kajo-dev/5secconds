from django.db import models
from django.urls import reverse

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
        upload_to='product/',
        default='front/img/default_img.png',
        )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)  
    date_created = models.DateTimeField(auto_now_add=True)
    on_sale = models.BooleanField(default=False)
    before_sale = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    slug = models.SlugField(
        verbose_name = ("safe URL"),
        max_length = 255,
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
    S=models.IntegerField()
    M=models.IntegerField()
    L=models.IntegerField()
    XL=models.IntegerField()