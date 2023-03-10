
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from products.models import Plantin, Frutal, Arbol,Planta
from products.carrito import Carrito

from products.forms import *



def Listaproductos(request):

    return render(request=request,
                  template_name='products/lista-productos.html',

                  )


def busca_planta(request):
    if request.method == "POST":
        data = request.POST
        planta = Planta.objects.filter(
            Q(nombre__contains=data['nombre']) 
        )
        contexto = {
            'plantas': planta,
        }
        return render(
            request=request,
            template_name='products/listaPlantas.html',
            context=contexto,
        )


def busca_arboles(request):
    if request.method == "POST":
        data = request.POST
        arbol = Arbol.objects.filter(
            Q(nombre__contains=data['nombre']) 
        )
        contexto = {
            'object_list': arbol,
        }
        return render(
            request=request,
            template_name='products/listaArbol.html',
            context=contexto,
        )

def busca_frutales(request):
    if request.method == "POST":
        data = request.POST
        frutal = Frutal.objects.filter(
            Q(nombre__contains=data['nombre']) 
        )
        contexto = {
            'object_list': frutal
        }
        return render(
            request=request,
            template_name='products/listaFrutal.html',
            context=contexto,
        )
        
def busca_plantin(request):
    if request.method == "POST":
        data = request.POST
        plantin=Plantin.objects.filter(
            Q(nombre__contains=data['nombre']) 
        )
        contexto = {
            'object_list': plantin
        }
        return render(
            request=request,
            template_name='products/listaPlantin.html',
            context=contexto,
        )
        
        
##Form de Arboles



class ArbolListView(ListView):
    model = Arbol
    template_name = 'products/listaArbol.html'

class ArbolcreateView(LoginRequiredMixin,CreateView):
    model=Arbol
    fields = ['nombre', 'tipo', 'tama??o', 'stock','precio','imagen']
    success_url=reverse_lazy('listarbol')


class ArbolUpdateView(LoginRequiredMixin,UpdateView):
    model=Arbol
    fields = ['nombre', 'tipo', 'tama??o', 'stock','precio','imagen']
    success_url=reverse_lazy('listarbol')

class ArbolDetailView(DetailView):
    model=Arbol
    success_url=reverse_lazy('verarbol')
    
class ArbolDeleteView(LoginRequiredMixin,DeleteView):
    model=Arbol
    success_url=reverse_lazy('listarbol')
    


##Form Frutales
class FrutalListView(ListView):
    model = Frutal
    template_name = 'products/listaFrutal.html'

class FrutalcreateView(LoginRequiredMixin,CreateView):
    model=Frutal
    fields = ['nombre', 'tipo', 'tama??o', 'stock','precio','imagen']
    success_url=reverse_lazy('listfrutal')


class FrutalUpdateView(LoginRequiredMixin,UpdateView):
    model=Frutal
    fields = ['nombre', 'tipo', 'tama??o', 'stock','precio','imagen']
    success_url=reverse_lazy('listfrutal')

class FrutalDetailView(DetailView):
    model=Frutal
    success_url=reverse_lazy('verfrutal')
    
class FrutalDeleteView(DeleteView,LoginRequiredMixin):
    model=Frutal
    success_url=reverse_lazy('listfrutal')
    
    
    
## Forms Plantin

class PlantinListView(ListView):
    model = Plantin
    template_name = 'products/listaPlantin.html'

class PlantincreateView(LoginRequiredMixin,CreateView):
    model=Plantin
    fields = ['nombre', 'tipo', 'tama??o', 'stock','precio','imagen']
    success_url=reverse_lazy('listplantin')


class PlantinUpdateView(LoginRequiredMixin,UpdateView):
    model=Plantin
    fields = ['nombre', 'tipo', 'tama??o', 'stock','precio','imagen']
    success_url=reverse_lazy('listplantin')

class PlantinDetailView(DetailView):
    model=Plantin
    success_url=reverse_lazy('verplantin')
    
class PlantinDeleteView(LoginRequiredMixin,DeleteView):
    model=Plantin
    success_url=reverse_lazy('listplantin')
    
    
    
##PRUEBA DE CARRITO
########################################

def tienda(request):
   planta=Planta.objects.all()
   return render (request=request,
                  template_name="products/tienda.html",
                  context={'planta':planta},
                  )





def carro(request):
   return render (request=request, 
                   template_name="products/carrito.html",
                   
                   )


def agregar_carrito(request,planta_id):
    carrito = Carrito(request)
    planta=Planta.objects.get(id=planta_id)
    carrito.agregar(planta=planta)
    return redirect("tienda")



def eliminar_carrito(request,planta_id):
    carrito=Carrito(request)
    planta=Planta.objects.get(id=planta_id)
    carrito.eliminar(planta=planta)
    return redirect("tienda")
    
def restar_carrito(request,planta_id):
    carrito=Carrito(request)
    planta=Planta.objects.get(id=planta_id)
    carrito.restar(planta=planta)
    return redirect("tienda")


def limpiar_carrito(request):
    carrito=Carrito(request)
    carrito.limpiar()
    return redirect("tienda")
    








    
