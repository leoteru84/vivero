from django.urls import path
from products.views import *





urlpatterns = [
     path('', views.inicio, name='inicio'),
     
     path('products/', Listaproductos, name='Productos'),
     path('Carga/', cargaPlantin, name='Carga'),
     
    
]
