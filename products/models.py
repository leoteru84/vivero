from django.db import models

# Create your models here.


class Plantin(models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}'
    



class Arbol(models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField()
    
    

class Frutal(models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}'