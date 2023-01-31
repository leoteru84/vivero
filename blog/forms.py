from django import forms
from blog.models import Entrada
from django.forms import ModelForm, Textarea, TextInput



class EntradaForm(forms.ModelForm):
    
    class Meta:
        model=Entrada
        fields= ['titulo','subtitulo','contenido','imagen','autor']
        widgets = { 
                   'contenido': Textarea(attrs={'size':20}), 
                   
                   }
    