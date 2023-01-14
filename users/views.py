from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from users.models import Cliente
from users.forms import RegistroUsuario
from django.urls import reverse, reverse_lazy


# Create your views here.


def inicio(request):
    return render(
        request=request,
        template_name='users/home.html',
    )


def login(request):
    return render(
        request=request,
        template_name='users/login.html',
    )


def registro(request):
    if request.method == 'POST':
        formulario = RegistroUsuario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Cliente(nombre=data['nombre'],
                              apellido=data['apellido'],
                              fechaNacimiento=data['fechaNacimiento'],
                              edad=data['edad'],
                              email=data['email'],


                              )
            cliente.save()
            url_exitosa = reverse('Productos')
            return redirect(url_exitosa)

    else:  # GET
        formulario = RegistroUsuario()
    return render(
        request=request,
        template_name='users/registro.html',
        context={'formulario': formulario},
    )

