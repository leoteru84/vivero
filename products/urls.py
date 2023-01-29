from django.urls import path
from products.views import  *
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
     
     ## Url listado
     path('Lista-Plantas/', Listaproductos, name='Productos'),
     #Url frutal
     path('Carga-Frutal/', FrutalcreateView.as_view(), name='createfrutal'),
     path('lista-Frutal/', FrutalListView.as_view(), name='listfrutal'),
     path('Ver-frutal/<int:pk>/', FrutalDetailView.as_view(), name='verfrutal'),
     path('Edita-frutal/<int:pk>/', FrutalUpdateView.as_view(), name='editfrutal'),
     path('Elimina-frutal/<int:pk>/', FrutalDeleteView.as_view(), name='eliminafrutal'),
     #Url Plantin
     path('Carga-Plantin/', PlantincreateView.as_view(), name='createplantin'),
     path('lista-Plantin/', PlantinListView.as_view(), name='listplantin'),
     path('Ver-Plantin/<int:pk>/', PlantinDetailView.as_view(), name='verplantin'),
     path('Edita-Plantin/<int:pk>/', PlantinUpdateView.as_view(), name='editplantin'),
     path('Elimina-Plantin/<int:pk>/', PlantinDeleteView.as_view(), name='eliminaplantin'),
     
     #Url busqueda
     path('Buscar-Arbol/',busca_arboles, name= 'buscaarbol'),# type: ignore
     path('Buscar-Frutal/',busca_frutales, name= 'buscafrutal'),# type: ignore
     path('Buscar-Plantin/',busca_plantin, name= 'buscaplantin'),# type: ignore
     path('Buscar-Plantas/',busca_planta, name= 'buscaplanta'),# type: ignore
     #Url Arbol
     path('Carga-Arbol/', ArbolcreateView.as_view(), name='createarbol'),
     path('Ver-arbol/<int:pk>/', ArbolDetailView.as_view(), name='verarbol'),
     path('Eliminar-arbol/<int:pk>/', ArbolDeleteView.as_view(), name='eliminaarbol'),
     path('Edita-arbol/<int:pk>/', ArbolUpdateView.as_view(), name='editarbol'),
     path('Listar-arbol/', ArbolListView.as_view(), name='listarbol'),
     
     ##PRUEBA CARRITO
     path('Tienda/', tienda, name='tienda'),
     path('Carrito/', carro, name='carro'),
     path('Carrito-agrega/<int:planta_id>/', agregar_carrito, name='addcarrito'),
     path('Carrito-elimina/<int:planta_id>/', eliminar_carrito, name='eliminacarrito'),
     path('Carrito-resta/<int:planta_id>/', restar_carrito, name='restacarrito'),
     path('Carrito-limpia/', limpiar_carrito, name='limpiacarrito'),
  
    
     
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
