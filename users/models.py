from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=128)
    fechaNacimiento=models.DateField(null=True)
    edad=models.IntegerField()
    email=models.EmailField()

    
    
    def __str__(self):
        return f'{self.nombre},{self.apellido}'
   
  


class Avatar(models.Model):
    # Va a estar asociado con el User. Avatar es una tabla anexa de User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # upload_to es la subcarpeta dentro de la carpeta media
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Imagen de: {self.user}"
 