from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=128)
    apellido=models.CharField(max_length=128)
    fechaNacimiento=models.DateField(null=True)
    edad=models.IntegerField()
    email=models.EmailField()
    
    
    def __str__(self):
        return f'{self.nombre},{self.apellido}'
   
    