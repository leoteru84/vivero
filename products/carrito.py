class Carrito:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
            self.session["carrito"]={}
            self.carrito=self.session["carrito"]
        else:
            self.carrito=carrito
            
    
    def agregar(self,planta):
        id=str(planta.id)
        if id not in self.carrito.keys():
           self.carrito[planta.id]={
            'planta_id': planta.id,
            'nombre':planta.nombre,
            'precio':str(planta.precio),
            'cantidad':1,
                }
        else:
            #self.carrito[id]["cantidad"] += 1
            #self.carrito[id]["acumulado"] += planta.precio
            #self.guardar()
            for key, value in self.carrito.items():
                if key == id:
                    value["cantidad"]+= 1
                    self.guardar()
                    break
    
    
    
    
    
    
    
    
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
        for key, value in self.carrito.items():
                if key == id:
                   value["cantidad"]=value["cantidad"] - 1
                   if value["cantidad"] < 1:
                       self.eliminar(planta)
                   self.guardar() 
                   break  
        
    
    
    def limpiar(self):
        self.session["carrito"]= {}
        self.session.modified = True
            
            
            
