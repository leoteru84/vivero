from django.db import models

# Create your models here.


class Plantin(models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField()
    precio=models.FloatField(null=True)
    
   
    
    def __str__(self):
        return f'{self.nombre}'
    



class Arbol(models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField()
    precio=models.FloatField(null=True)
    

   
    def __str__(self):
        return f'{self.nombre}'

class Frutal(models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField()
    precio=models.FloatField(null=True)
    

  
    def __str__(self):
        return f'{self.nombre}'