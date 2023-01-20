from products.models import Arbol, Plantin, Frutal





class Carrito:
    def __init__(self,request) -> None:
        self.request=request
        self.session=request.session
        carrito=self.session["Carrito"]
        if not carrito:
            self.session["Carrito"]={}
            self.carrito=self.session["Carrito"]
        else:
            self.carrito=carrito
            
    
    def agregararbol(self,Arbol)    :
        id=str(Arbol.id)
        if id not in self.carrito.keys():
           self.carrito[id]={
            'id': Arbol.id,
            'nombre':Arbol.nombre,
            'acumulado':Arbol.precio,
            'cantidad':1,
        }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += Arbol.precio
            self.guardarcarrito()
    
    def guardarcarrito(self):
        self.session["carrito"]= self.carrito
        self.session.modified = True
    

    def eliminar(self,Arbol):
        id=str(Arbol.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardarcarrito()
        
    def restar(self,Arbol):
        id=str(Arbol.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= Arbol.precio
        if self.carrito[id]["cantidad"] <= 0:
           self.eliminar(Arbol)
        self.guardarcarrito()   
        
    
    
    def limpiar(self)           :
        self.session["carrito"] = {}
        self.session.modified = True
            
            
            
