
class Usuario():
    def guardar(self):
        print("Guardando en BBDD")
        
class Sesion(): #identica al user que se esta conectando y --- 
    def guardar(self):
        print("Guardando en acrchivo")
        
def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()
    
guardar([Usuario(), Sesion()])

#Si camina como pato y suena como pato, entonces es un pato.