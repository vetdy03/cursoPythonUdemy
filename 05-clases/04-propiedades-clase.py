class Perro: #PascalCase or UpperCamelCase
    patas = 4
    def __init__(self, nombre, edad):
        self.name = nombre #PROPIEDAD.- var asociada a una clase
        self.age = edad
        
    def ladra(self): #estas ya no son funciones SON METODOS
        print(f"{self.name} dice; guauu")
Perro.patas = 3
    
mi_perro = Perro("migui", 1) #en otro lenguajes NEW
mi_perro2 = Perro("negro", 1) #en otro lenguajes NEW
mi_perro.patas = 7
print(Perro.patas)
print(mi_perro.patas)
