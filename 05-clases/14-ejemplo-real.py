#crud.- leer crear actualizar eliminar
#user atributes: nombre
#                apellido
#                nImpuesto

class Model(): 
    tabla = False
    def __init__(self):
        print("Error, tienes que definir una tabla")
        
    def guardar(self):
        print(f"Guardando {self.tabla} en la BBDD")
    @classmethod    
    def buscar_por_id(self, _id):
        print("Bsucando por id: {}".format(_id))
        
class User(Model):
    tabla = "Usuario"
    
user = User()
user.guardar()
User.buscar_por_id(123)