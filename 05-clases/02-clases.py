class MiPerro: #PascalCase or UpperCamelCase
    def ladra(self): #estas ya no son funciones SON METODOS
        print("Guauu")
    
mi_perro = MiPerro() #en otro lenguajes NEW
print(type(mi_perro))
mi_perro.ladra()
print(isinstance(mi_perro, MiPerro))