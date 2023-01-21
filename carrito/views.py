from django.shortcuts import render,redirect
from products.models import *
from carrito.carrito import Carrito


# Create your views here.

def tienda(request):
    plantas=Planta.objects.all()
    return render (request=request, 
                   template_name="carrito/carrito.html",
                   
                   )


def agregar_carrito(request,planta_id):
    carrito = Carrito(request)
    planta=Planta.objects.get(id=planta_id)
    carrito.agregar(planta)
    return redirect("Tienda")

def new_func(request):
    carrito=Carrito(request)
    return carrito

def eliminar_carrito(request,planta_id):
    carrito=Carrito(request)
    planta=Planta.objects.get(id=planta_id)
    carrito.eliminar(planta)
    return redirect("Tienda")
    
def restar_carrito(request,planta_id):
    carrito=Carrito(request)
    planta=Planta.objects.get(id=planta_id)
    carrito.restar(planta)
    return redirect("cTienda")


def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("carrito:Tienda")
    