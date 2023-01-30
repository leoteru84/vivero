
from django.shortcuts import render
from blog.models import Entrada
from django.views.generic import ListView, DetailView,DeleteView,UpdateView,CreateView
from blog.forms import EntradaForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def blog(request):
    blog=Entrada.objects.all()
    contexto={
            'entrada':blog,
            }
    
    return render(request=request,
                  template_name='blog/blog.html', 
                  context=contexto,
                  )  



class Entradalist(ListView):
    model=Entrada
    template_name="blog/blog.html"
    
    





class Entradacreate(LoginRequiredMixin,CreateView):
    model=Entrada
    template_name='blog/blog_form.html'
    fields=['titulo','subtitulo','contenido','imagen','autor']
    success_url=reverse_lazy('inicio')
    
    
    
class Entradaedit(LoginRequiredMixin,UpdateView):
    model=Entrada
    form=EntradaForm
    fields=['titulo','subtitulo','contenido','imagen']
    template_name='blog/blog_form.html'
    success_url=reverse_lazy('blog')
    
    


class Entradadelete(LoginRequiredMixin,DeleteView):
    model=Entrada
    success_url=reverse_lazy('blog')
    

    
    
    