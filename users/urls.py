from django.urls import path
from . import views

urlpatterns = [
    path('Registro/', views.registro, name='registro'),
    path('Login/', views.login_view, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
               
]
