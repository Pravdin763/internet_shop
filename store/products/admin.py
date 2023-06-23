from django.contrib import admin

from .models import ProductCategory, Product

admin.site.register(ProductCategory)        # Почемуто надо каждый класс на отдельной строке!!
admin.site.register(Product)                 # Почемуто надо каждый класс на отдельной строке!!
