from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


"""
class Usuario(forms.Form):
    nombre=forms.CharField(max_length=128)
    apellido=forms.CharField(max_length=128)
    fechaNacimiento=forms.DateField()
    edad=forms.IntegerField()
    email=forms.EmailField()"""
    
    
    
class RegistroForm(UserCreationForm):
    password1= forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
        

   
   
    

    
    

