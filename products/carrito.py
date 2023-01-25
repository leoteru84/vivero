class Carrito:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carrito=self.session.get("carrito")
        if not carrito:
           carrito=self.session["carrito"]={}
            
        #else:
        self.carrito=carrito
            
    
    def agregar(self,planta):
        id=str(planta.id)
        if id not in self.carrito.keys():
           self.carrito[id]={
            'planta_id': planta.id,
            'nombre':planta.nombre,
            'precio': str(planta.precio),
            'stock':planta.stock,
            'cantidad':1,
                }
        else:
           for key, value in self.carrito.items():
                if key == id:
                    value["cantidad"]+= 1
                    value["precio"]=float(value["precio"])+planta.precio
                    
                               
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
        for key, value in self.carrito.items():
                if key == id:
                   value["cantidad"]=value["cantidad"] - 1
                   value["precio"]=float(value["precio"])-planta.precio
                   if value["cantidad"] < 1:
                       self.eliminar(planta)
                   self.guardar() 
                   break  
        
    
    
    def limpiar(self):
        self.session["carrito"]= {}
        self.session.modified = True
            
            
            
