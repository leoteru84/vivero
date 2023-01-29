from django.urls import path
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Registro/', registro, name='registro'),
    path('Login/', bienvenida, name='bienvenida'),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('inicio/', CustomLoginView.as_view() , name="login"),
    path('Edit/', PerfilupdateView.as_view() , name="editdatos"),
    path('Agregar-avatar/',agregar_avatar, name="avatar"),
    
               
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
