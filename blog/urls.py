
from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path("Blog/", Entradalist.as_view(), name="blog"),
    path("Crear-Blog/", Entradacreate.as_view() , name="crearpost"),
    path("Editar-Blog<int:pk>/", Entradaedit.as_view() , name="editpost"),
]
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
