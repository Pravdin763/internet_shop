from django.contrib import admin
from .models import User
from products.admin import BasketAdmin

#admin.site.register(User)

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', )
    inlines = (BasketAdmin, )             # отображение корзины из другой админки! другого приложения!
