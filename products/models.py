from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='nombre')
    description = models.TextField(verbose_name='descrpción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='precio')
    available = models.BooleanField(default=True)
    product_image = models.ImageField(upload_to='products', null=True, blank=True, verbose_name='Imagen del producto')
    create_date = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
    update_date = models.DateField(auto_now=True, verbose_name='Fecha de actuaización')
    
    def __str__(self):
        return self.name
    

