from django.urls import path
from . import views

urlpatterns = [
    path('Registro/', views.registro, name='registro'),
    path('Login/', views.login, name='login'),
               
]
