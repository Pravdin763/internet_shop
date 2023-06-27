from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
@login_required
def index(request):
    context = {'title': 'Store', 'is_promotion': True}
    return render(request, 'products/index.html', context)

@login_required
def products(request, category_id=None, page_number=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, per_page=9)         # для страниц
    products_paginator = paginator.page(page_number)           # для страниц
    context = {'title': 'Store - Каталог товаров',
            # 'products': Product.objects.all(),
            'products': products_paginator,
            'categories': ProductCategory.objects.all()}
    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity +=1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])       # возвращает на туже страницу!

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
