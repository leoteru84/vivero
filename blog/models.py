from django.db import models
from django.contrib.auth.models import User



class Entrada(models.Model):
    titulo=models.TextField(max_length=100)
    subtitulo=models.TextField(max_length=100)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='entradas/',null=True, blank=True)
    autor=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    creado=models.DateTimeField(auto_now_add=True,null=True)
    actualizado=models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        verbose_name='entrada'
        verbose_name_plural='entradas'
        
    def __str__(self):
      return self.titulo


    

