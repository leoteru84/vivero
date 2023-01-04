from django.shortcuts import render
from django.http import HttpResponse




def inicio(request):
    return render(request=request, 
                  template_name='/home/lean/Proyectos_Coder/django1/vivero_online/vivero_online/templates/vivero_online/base.html',
                  )

def Listaproductos(request):
    contexto={
        'plantas':['Plantines','Frutales','Arboles']
           }
    
    return render(request=request, 
                  template_name='products/lista-productos.html',
                  context=contexto,
                  )
   


