from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass
        #print("Guardando ")
        
class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")
        
class Sesion(Model): #identica al user que se esta conectando y --- 
    def guardar(self):
        print("Guardando en acrchivo")
        
def guardar(entidad):
    entidad.guardar()
    
usuario = Usuario()
guardar(usuario)