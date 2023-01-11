from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from users.models import Cliente

# Create your views here.


def login(request):
    return render(request=request, 
                  template_name='users/login.html',
                  
                  
                  )



class Registro(forms.ModelForm):
    class Meta:
        model=Cliente
        fields='__all__'
        widgets= {'fechaNacimiento': forms.DateInput(attrs={'type':'date'})}

   

