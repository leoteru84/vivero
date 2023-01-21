from django.db import models

# Create your models here.
class Carrito():
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carrito=self.session["carrito"]
        if not carrito:
            self.session["carrito"]={}
            self.carrito=self.session["carrito"]
        else:
            self.carrito = carrito
            
    
    def agregar(self,planta)    :
        id=str(planta.id)
        if id not in self.carrito.keys():
           self.carrito[id]={
            'planta_id': planta.id,
            'nombre':planta.nombre,
            'acumulado':planta.precio,
            'cantidad':1,
        }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += planta.precio
            self.guardar()
    
    def guardar(self):
        self.session["carrito"]= self.carrito
        self.session.modified = True
    

    def eliminar(self,planta):
        id=str(planta.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar()
        
    def restar(self,planta):
        id=str(planta.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= planta.precio
        if self.carrito[id]["cantidad"] <= 0:
           self.eliminar(planta)
        self.guardar()   
        
    
    
    def limpiar(self)           :
        self.session["carrito"] = {}
        self.session.modified = True