class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"
class Categoria:
    Producto = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.Producto