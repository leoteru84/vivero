from django.shortcuts import render
from products.models import Arbol, Plantin, Frutal
from carrito.carrito import Carrito


# Create your views here.

def add_to_cart(request, Arbol_id, quantity): 
    arbol = Arbol.objects.get(id=Arbol_id) 
    cart = carrito(request) 
    carrito.add(Arbol, Arbol.precio, quantity)

def remove_from_carrito(request, Arbol_id): 
    arbol = Arbol.objects.get(id=Arbol_id) 
    cart = carrito(request) carrito.remove(Arbol)

def get_carrito(request): 
    return render_to_response('carrito.html', dict(carrito=carrito(request)))
