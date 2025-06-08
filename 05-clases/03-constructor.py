class MiPerro: #PascalCase or UpperCamelCase
    def __init__(self, nombre, edad):
        self.name = nombre #PROPIEDAD.- var asociada a una clase
        self.age = edad
    def ladra(self): #estas ya no son funciones SON METODOS
        print(f"{self.name} dice; guauu")
    
mi_perro = MiPerro("migui", 1) #en otro lenguajes NEW
print(mi_perro.ladra())

#mi_perro2 = MiPerro()