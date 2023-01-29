from django import forms
from blog.models import Entrada



class EntradaForm(forms.ModelForm):
      class Meta:
        model=Entrada
        fields= ['titulo','subtitulo','contenido','imagen','autor']
   