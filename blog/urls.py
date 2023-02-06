
from django.urls import path
from blog.views import *





urlpatterns = [
    path("Blog/", Entradalist.as_view(), name="blog"),
    path("Crear-Blog/", Entradacreate.as_view() , name="crearpost"),
    path("Editar-Blog<int:pk>/", Entradaedit.as_view() , name="editpost"),
    path("Eliminar-Blog<int:pk>/", Entradadelete.as_view() , name="deletepost"),


]