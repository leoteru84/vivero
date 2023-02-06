from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from users.models import Cliente, Avatar
from users.forms import  RegistroForm, AvatarFormulario, ContactoForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import ListView, DetailView,DeleteView,UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import PerfilUpdateForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

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

"""
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
    )"""
    
    
class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('login')
    
    
    
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    sucess_url='bienvenida'
    next_page =reverse_lazy('bienvenida')
    
   
def bienvenida(request):
    request=request
    return render(request,template_name='users/bienvenido.html')
   
class PerfilupdateView(LoginRequiredMixin,UpdateView):
    model=User
    form_class= PerfilUpdateForm  # type: ignore
    template_name='users/perfil.html'
    success_url=reverse_lazy('tienda')
    
    def get_object(self, queryset=None):
        return self.request.user
    


def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html
         
        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user= request.user
            try:
              avatar.save()
            except IntegrityError:
                 pass
            url_exitosa = reverse('blog')
            return redirect(url_exitosa)
    else:  # GET
            formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='users/formulario_avatar.html',
        context={'form': formulario},
    )


    
    
    










def contacto (request):
    form=ContactoForm()
    if request == 'POST':
        form=ContactoForm(data=request.POST)
        if form.is_valid:
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            
            
            email=EmailMessage(
                "Mensaje de vivero online",
                "El usuario{}, Email: {}, le ha enviado un mensaje:\n {}".format(nombre,email,contenido),
                               )
            try:
                email.send()
                return redirect('/Contacto/?ok')
            except:
                return redirect('/Contacto/?nok')

    
    return render(request, "users/contacto.html",{'form':form})
    
    


def acerca (request):
    return render(request, 'users/acerca.html')