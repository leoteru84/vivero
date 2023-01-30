from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView
from users.models import Cliente, Avatar

    
    
class RegistroForm(UserCreationForm):
    password1= forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']
        
        
class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields= ['last_name', 'first_name', 'username', 'email']
        


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']        
        
        
        
class ContactoForm(forms.Form):
    nombre=forms.CharField(label='Nombre',required=True)
    email=forms.CharField(label='E-mail',required=True)
    contenido=forms.CharField(widget=forms.Textarea)

   
   
    

    
    

