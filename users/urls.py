from django.urls import path
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Registro/', registro, name='registro'),
    path('Bienvenid@/', bienvenida, name='bienvenida'),
    path('Logout/', CustomLogoutView.as_view(), name="logout"),
    path('Login/', CustomLoginView.as_view() , name="login"),
    path('Edit/', PerfilupdateView.as_view() , name="editdatos"),
    path('Agregar-avatar/',agregar_avatar, name="avatar"),
   
    
               
]

