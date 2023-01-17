from django import forms 

class RegistroUsuario(forms.Form):
    nombre=forms.CharField(max_length=128)
    apellido=forms.CharField(max_length=128)
    fechaNacimiento=forms.DateField()
    edad=forms.IntegerField()
    email=forms.EmailField()
    
    
    
class LoginUsuario(forms.Form):

    pass
   
    

    
    

