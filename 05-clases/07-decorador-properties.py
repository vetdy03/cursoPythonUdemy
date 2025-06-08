class Perro: 
    def __init__(self, nombre):
        self.name = nombre
    
    @property #solo se usa con funciones que devuelven GETTER
    def name(self): #ESTO YA ES UNA PROPIEDAD YA NO ES UN METODO
        return self.__nombre
    
    @name.setter#INDICAR CUAL ES EL METODO DE SETEAR EL VALOR  
    def name(self, name):
        print("pasndpo por el setter")
        if name.strip():
            self.__nombre = name
        
        
perro = Perro("choco")
print(perro.name)