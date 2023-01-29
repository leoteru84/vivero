from django import forms 
from products.models import Planta

class CargaPlantin(forms.ModelForm):
    class Meta:
        model=Planta
        fields = ['nombre', 'tipo', 'tamaño', 'stock','precio','imagen']
    
   
    
class CargaFrutal(forms.Form):
   class Meta:
        model=Planta
        fields = ['nombre', 'tipo', 'tamaño', 'stock','precio','imagen']

class CargaArbol(forms.Form):
   class Meta:
        model=Planta
        fields = ['nombre', 'tipo', 'tamaño', 'stock','precio','imagen']
    