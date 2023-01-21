from django.db import models

# Create your models here.


class Planta (models.Model):
    nombre=models.CharField(max_length=200)
    tipo=models.CharField(max_length=128)
    tamaño=models.CharField(max_length=200)
    stock=models.IntegerField(null=False)
    precio=models.FloatField(null=True)
   
    
    def __str__(self):
        return f'{self.nombre}'
    

class Plantin(Planta):
    pass
   
    



class Arbol(Planta):
    pass
  



class Frutal(Planta):
    pass



