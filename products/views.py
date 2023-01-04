from django.shortcuts import render
from django.http import HttpResponse




def inicio(request):
    
    
    return render(request=request, 
                  template_name='products/home.html',
                  )

def Listaproductos(request):
    contexto={
        'plantas':['Plantines','Frutales','Arboles']
           }
    
    return render(request=request, 
                  template_name='products/lista-productos.html',
                  context=contexto,
                  )
   
def registro(request):
    return render(request=request, 
                  template_name='products/registro.html',
                  
                  )

