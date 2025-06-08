class Perro: #PascalCase or UpperCamelCase
    patas = 4
    
    def __init__(self, nombre, edad):#constyructor
        self.__name = nombre #PRIVATE.- __name--> loponeen privado, 
        self.age = edad

    def get_name(self):#No podemos acceder ni modificar pero si podemos retornar
        return self.__name
    
    def __set_name(self, newName):
        self.__name = newName
        
    def ladra(self):#se refiere a la clase misma, un metodo de la clase misma                    #estas ya no son funciones SON METODOS
        print(f"{self.__name} dice; guauu") #Factory Method
        
    @classmethod  
    def factory(cls):
        return cls("Chanchito feliz", 3)

perro1 = Perro.factory()
perro1.ladra()
#print(perro1.__dict__) #NO se deberia de hacer esto
print(perro1._Perro__name)