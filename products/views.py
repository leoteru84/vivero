
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,DeleteView,UpdateView,CreateView

from products.models import Plantin, Frutal, Arbol
from products.forms import *



def cargaProductos(request):
    return render(request=request,
                  template_name='products/cargaproductos.html',
                  )


def Listaproductos(request):

    return render(request=request,
                  template_name='products/lista-productos.html',

                  )



def busca_arboles(request):
    if request.method == "POST":
        data = request.POST
        arbol = Arbol.objects.filter(
            Q(nombre__contains=data['nombre']) 
        )
        frutal = Frutal.objects.filter(
            Q(nombre__contains=data['nombre']) 
        )
        contexto = {
            'Arboles': arbol
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
            'Frutales': frutal
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
            'Plantines': plantin
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

class ArbolcreateView(CreateView):
    model=Arbol
    fields = ['nombre', 'tipo', 'tamaño', 'stock']
    success_url=reverse_lazy('listarbol')


class ArbolUpdateView(UpdateView):
    model=Arbol
    fields = ['nombre', 'tipo', 'tamaño', 'stock']
    success_url=reverse_lazy('listarbol')

class ArbolDetailView(DetailView):
    model=Arbol
    success_url=reverse_lazy('verarbol')
    
class ArbolDeleteView(DeleteView):
    model=Arbol
    success_url=reverse_lazy('listarbol')


##Form Frutales
class FrutalListView(ListView):
    model = Frutal
    template_name = 'products/listaFrutal.html'

class FrutalcreateView(CreateView):
    model=Frutal
    fields = ['nombre', 'tipo', 'tamaño', 'stock']
    success_url=reverse_lazy('listfrutal')


class FrutalUpdateView(UpdateView):
    model=Frutal
    fields = ['nombre', 'tipo', 'tamaño', 'stock']
    success_url=reverse_lazy('listfrutal')

class FrutalDetailView(DetailView):
    model=Frutal
    success_url=reverse_lazy('verfrutal')
    
class FrutalDeleteView(DeleteView):
    model=Frutal
    success_url=reverse_lazy('listfrutal')
    
    
    
## Forms Plantin

class PlantinListView(ListView):
    model = Plantin
    template_name = 'products/listaPlantin.html'

class PlantincreateView(CreateView):
    model=Plantin
    fields = ['nombre', 'tipo', 'tamaño', 'stock']
    success_url=reverse_lazy('listplantin')


class PlantinUpdateView(UpdateView):
    model=Plantin
    fields = ['nombre', 'tipo', 'tamaño', 'stock']
    success_url=reverse_lazy('listplantin')

class PlantinDetailView(DetailView):
    model=Plantin
    success_url=reverse_lazy('verplantin')
    
class PlantinDeleteView(DeleteView):
    model=Plantin
    success_url=reverse_lazy('listplantin')








    
