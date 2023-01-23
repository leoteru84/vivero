from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from users.models import Cliente
from users.forms import  RegistroForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView, LoginView


# Create your views here.


def inicio(request):
    return render(
        request=request,
        template_name='users/home.html',
    )

def registro(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('login')
            return redirect(url_exitosa)

    else:  # GET
        formulario = RegistroForm()
    return render(
        request=request,
        template_name='users/registro.html',
        context={'formulario': formulario},
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                url_exitosa = reverse('bienvenida')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='users/login.html',
        context={'form': form},
    )
    
    
class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('login')
    
    
    
class CustomLoginView(LoginView):
    template_name = 'users/bienvenido.html'
    next_page =reverse_lazy('products/tienda.html')
   