from django.db import models
from users.models import User   # для basket(корзины)

class ProductCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:                     #  отображение в меню админки
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products_images')
    price = models.DecimalField(decimal_places=2, max_digits=8)         # 1 сколько знаков ПОСЛЕ запятой, 2 сколько знаков ПЕРЕД запятой
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    class Meta:                     #  отображение в меню админки
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.price} {self.category.name}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.name} Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity