
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

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


def listarArbol(request):
    contexto = {
        'Arboles': Arbol.objects.all(),
    }
    return render(request=request,
                  template_name='products/listaArbol.html',
                  context=contexto,

                  )


def listarPlantin(request):
    contexto = {
        'Plantines': Plantin.objects.all(),
    }
    return render(request=request,
                  template_name='products/listaPlantin.html',
                  context=contexto,

                  )


def listarFrutal(request):
    contexto = {
        'Frutales': Frutal.objects.all(),
    }
    return render(request=request,
                  template_name='products/listaFrutal.html',
                  context=contexto,

                  )


def cargarPlantin(request):
    if request.method == 'POST':
        formulario = CargaPlantin(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            plantin = Plantin(nombre=data['nombre'],
                              tipo=data['tipo'],
                              tamaño=data['tamaño'],
                              stock=data['stock'],



                              )
            plantin.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = CargaPlantin()
    return render(
        request=request,
        template_name='products/cargaPlantin.html',
        context={'formulario': formulario},
    )


def cargarFrutal(request):
    if request.method == 'POST':
        formulario = CargaFrutal(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            frutal = Frutal(nombre=data['nombre'],
                            tipo=data['tipo'],
                            tamaño=data['tamaño'],
                            stock=data['stock'],



                            )
            frutal.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = CargaFrutal()
    return render(
        request=request,
        template_name='products/cargaFrutal.html',
        context={'formulario': formulario},
    )


def cargarArbol(request):
    if request.method == 'POST':
        formulario = CargaArbol(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            arbol = Arbol(nombre=data['nombre'],
                          tipo=data['tipo'],
                          tamaño=data['tamaño'],
                          stock=data['stock'],



                          )
            arbol.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = CargaArbol()
    return render(
        request=request,
        template_name='products/cargaArbol.html',
        context={'formulario': formulario},
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
    
