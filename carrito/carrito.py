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
            
            
            
            
def agregar(self,Arbol)    :
    id=str(Arbol.id)
    if id not in self.carrito.keys():
        self.carrito[id]={
            'id': Arbol.id,
            'nombre':Arbol.nombre,
            'acumulado':Arbol.precio,
            'cantidad':1,
        }