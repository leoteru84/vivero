from django.urls import path
from . import views






urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('registro/', views.registro, name='Registrese'),
     path('products/', views.Listaproductos, name='Productos'),
    
]
