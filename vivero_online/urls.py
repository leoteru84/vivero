"""vivero_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users.views import  inicio
from django.conf.urls.static import static
from django.conf import settings
from products.views import tienda
from django.conf import settings
from django.conf.urls.static import static
from users.views import *





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='inicio'),
    path('Usuario/',include('users.urls')),
    path('Productos/',include('products.urls')),
    path('Blog/',include('blog.urls')),
    path('Contacto/',contacto, name="contacto"),
    path('Acerca_de_nosotr@s/',acerca, name="acerca"),
    
    
    
    
] 

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
