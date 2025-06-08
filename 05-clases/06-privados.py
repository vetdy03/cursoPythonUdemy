class Perro: #PascalCase or UpperCamelCase
    patas = 4
    
    def __init__(self, nombre, edad):
        self.name = nombre #PROPIEDAD.- var asociada a una clase
        self.age = edad
    
    @classmethod    
    def ladra(cls):#se refiere a la clase misma, un metodo de la clase misma                    #estas ya no son funciones SON METODOS
        print(f"dice; guauu") #Factory Method
    
    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 3)
    
Perro.ladra()
perro1 = Perro("ca", 2)
perro3 = Perro.factory()
print(perro3.name, "tienes {}".format(perro3.patas) )