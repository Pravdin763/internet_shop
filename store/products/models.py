from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products_images')
    price = models.DecimalField(decimal_places=2, max_digits=6)         # 1 сколько знаков ПОСЛЕ запятой, 2 сколько знаков ПЕРЕД запятой
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'