
#CLASE ABSTRACTA.- una clase que no se puede instancias de ahi
         
from abc import ABC, abstractmethod 
#abc abstract class  ABC
class Model(ABC): 
    
    # def __init__(self):
    #     print("Error, tienes que definir una tabla")
    
    @property
    @abstractmethod #una vez que ponemos aqui esto no deberias poder instanciar la clase Model
    def tabla(self):
        pass   
    
    @abstractmethod     
    def guardar(self):
        pass
        # print(f"Guardando {self.tabla} en la BBDD")
        
    @classmethod    
    def buscar_por_id(self, _id):
        print("Bsucando por id: {} en la tabla de user {}".format(_id, self.tabla))
        
class User(Model):
    tabla = "Usuario"
    #como es un metodo abstracto el metodo GUARDAR  de MODELO no se puede instanciasr y debenemos definir otro aqui
    
    def guardar(self):
        print("guardando usuario: ")

user = User()
user.guardar()
User.buscar_por_id(123)

