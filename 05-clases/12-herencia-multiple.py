class Caminador:
    def caminar(self):
        print("caminando")
    
class Volador:
    def volar(self):
       print("volando ando") 

class Nadador:
    def nadar(self):
        print("nadando ando xd")
        
class Perro():
    def pasear(self):
        print("paseando al perro")

#heredando de multples, las clases de donde se quiere heredar deben de ser lo mas pequeñas posibles.
class pato(Volador, Caminador, Nadador): # aplica la herencia de DER - IZQ
    def programar (self):
        print("Programando")
#regla.- 


