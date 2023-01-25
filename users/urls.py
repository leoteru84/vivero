from django.urls import path
from .views import *

urlpatterns = [
    path('Registro/', registro, name='registro'),
    path('Login/', bienvenida, name='bienvenida'),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('inicio/', CustomLoginView.as_view() , name="login"),
    path('Edit/', PerfilupdateView.as_view() , name="editdatos"),
    
               
]
