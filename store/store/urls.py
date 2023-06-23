"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import index, products
from django.conf.urls.static import static          # для картинок
from django.conf import settings                    # для картинок

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    #path('products', products, name='products')
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#if settings.DEBUG:              # если debug в значении Tquit()rue, то идем дальше
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
