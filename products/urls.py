from django.urls import path
from products.views import  *





urlpatterns = [
     path('Lista-Plantas/', Listaproductos, name='Productos'),
     path('Carga-Arbol/', cargarArbol, name='arbol'),
     path('Carga-Frutal/', cargarFrutal, name='frutal'),
     path('Carga-Plantin/', cargarPlantin, name='plantin'),
     path('lista-Plantin/', listarPlantin, name='listaplantin'),
     path('lista-Arbol/', listarArbol, name='listaarbol'),
     path('lista-Frutal/', listarFrutal, name='listafrutal'),
     path('Buscar-Arbol/',busca_arboles, name= 'buscaarbol'),# type: ignore  
     path('Buscar-Frutal/',busca_frutales, name= 'buscafrutal'),# type: ignore  
     path('Buscar-Plantin/',busca_plantin, name= 'buscaplantin'),# type: ignore  
]
