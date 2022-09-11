from django.db import models

# Create your models here.

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
        upload_to='front/img/',
        default='front/img/default_tshirt.png'
        )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)  
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

