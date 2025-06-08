class Perro: #PascalCase or UpperCamelCase    
    def __init__(self, nombre, edad):
        self.name = nombre #PROPIEDAD.- var asociada a una clase
        self.age = edad

    def __str__(self): #entregar info mas relevante
        return f"Clase Perro: {self.name}"
    
    def ladra(self):#se refiere a la clase misma, un metodo de la clase misma                    #estas ya no son funciones SON METODOS
        print(f"{self.name} dice; guauu") #Factory Method
    
perro = Perro("chanchito", 7)
texto = str(perro) 
print(perro)   
print(type(perro))   
print(type(texto))