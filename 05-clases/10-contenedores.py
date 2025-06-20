
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    #metodo magico que devuelve el nombr y precio como STRING    
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"
class Categoria:
    #atributo que se encarga de contener los productos que querramos
    productos = []
    
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos