from django import forms 

class CargaPlantin(forms.Form):
    nombre=forms.CharField(max_length=200)
    tipo=forms.CharField(max_length=128)
    tamaño=forms.CharField(max_length=200)
    stock=forms.IntegerField(required=True)
    precio=forms.FloatField(required=True)
    imagen = forms.ImageField()
   
    
class CargaFrutal(forms.Form):
    nombre=forms.CharField(max_length=200)
    tipo=forms.CharField(max_length=128)
    tamaño=forms.CharField(max_length=200)
    stock=forms.IntegerField(required=True)
    precio=forms.FloatField(required=True)
    imagen = forms.ImageField()

class CargaArbol(forms.Form):
    nombre=forms.CharField(max_length=200)
    tipo=forms.CharField(max_length=128)
    tamaño=forms.CharField(max_length=200)
    stock=forms.IntegerField(required=True)
    precio=forms.FloatField(required=True)   
    imagen = forms.ImageField()