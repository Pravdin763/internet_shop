from django.shortcuts import render
from .models import Product, ProductCategory

def index(request):
    context = {'title': 'Store', 'is_promotion': True}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'Store - Каталог товаров',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()}
    return render(request, 'products/products.html', context)