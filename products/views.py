from django.shortcuts import render
from django.http import HttpResponse
from products.models import Plantin, Frutal,Arbol



def inicio(request):
   
    
    
    return render(request=request, 
                  template_name='products/home.html',
                  
                  )

def Listaproductos(request):
    contexto={
        'plantin': Plantin.objects.all(),
        'Frutal': Frutal.objects.all(),
        'Arboles': Arbol.objects.all(),
        
           }
    
    return render(request=request, 
                  template_name='products/lista-productos.html',
                  context=contexto,
                  )

