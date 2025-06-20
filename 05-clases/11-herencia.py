class Animal:
    def comer(self):
        print("Comiendo")
        
class Perro(Animal):
    def pasear(self):
        print("paseando")

perro = Perro()
perro.comer()

class Chanchito(Perro): #herencia multi-nivel no es recomendable mas de 2
    def programar (self):
        print("Programando")
        
chanchi = Chanchito()
chanchi.comer()
chanchi.pasear()

#si tendria un metodo en comun tendria qe modficiar en cada clase por eso existe l herencia