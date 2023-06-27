from django.contrib import admin

from .models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)        # Почемуто надо каждый класс на отдельной строке!!
#admin.site.register(Product)                 # Почемуто надо каждый класс на отдельной строке!!

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')    # что будет отображаться в меню
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')    # отображение внутри заполнения. кортеж внутри - отображение на одной строке
    readonly_fields = ('description',)      # только для чтения
    search_fields = ('name', )              # поиск по полю
    ordering = ('-price',)                  # сортировка

class BasketAdmin(admin.TabularInline):         # TabularInline будет частью другой! админки (группы) в данном случае users
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')     # обязательно readonly_fields! иначе ошибка
    readonly_fields = ('created_timestamp', )               # обязательно! не будет возможно для редактирования!
    extra = 0  # не выводит дополнительные поля корзины пользователя по умолчанию 3