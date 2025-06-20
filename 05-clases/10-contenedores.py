
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
        
    def agregar(self, producto):
        self.productos.append(producto)
        
    def imprimir(self):
        for producto in self.productos:
            print(producto)
kayak = Producto("kayak", 1000)
bicicleta = Producto("bici", 5600)
laptop = Producto("laptop", 500)

deportes = Categoria("deporte", [kayak, bicicleta])

deportes.agregar(laptop)
deportes.imprimir()