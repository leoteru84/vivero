from django.urls import path
from carrito.carrito import Carrito
from carrito.views import *

urlpatterns = [
    path('Carrito/', tienda, name='Tienda'),
    
    path('Carrito-agrega/<int:planta_id>', agregar_carrito, name='addcarrito'),
    path('Carrito-elimina/<int:planta_id>/', eliminar_carrito, name='eliminacarrito'),
    path('Carrito-resta/<int:planta_id>/', restar_carrito, name='restacarrito'),
    path('Carrito-limpia/', limpiar_carrito, name='limpiacarrito'),
    
    
               
]




