from django.shortcuts import render

def index(request):
    context = {'title': 'Store', 'is_promotion': True}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'Store - Каталог товаров', 'products': [
        {'image': "static/vendor/img/products/Adidas-hoodie.png",
         'name': 'Худи черного цвета с монограммами adidas Originals',
         'price': 6090,
         'descriptions': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни'},
        {'image': "static/vendor/img/products/Blue-jacket-The-North-Face.png",
         'name': 'Синяя куртка The North Face',
         'price':23725,
         'descriptions': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
        {'image': "static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
         'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
         'price': 3390,
         'descriptions': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
        {'image': "static/vendor/img/products/Black-Nike-Heritage-backpack.png",
         'name': 'Черный рюкзак Nike Heritage',
         'price': 2340,
         'descriptions': 'Плотная ткань. Легкий материал'},
    ]}
    return render(request, 'products/products.html', context)