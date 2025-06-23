# ¿Qué es el Polimorfismo?
# El término polimorfismo proviene del griego y significa «muchas formas». En programación, el polimorfismo permite que un mismo método o función funcione de diferentes maneras dependiendo del tipo de objeto con el que esté trabajando.

# En Python, el polimorfismo se puede implementar de varias maneras, incluidas:

# Polimorfismo con herencia: Clases hijas que sobrescriben métodos de la clase padre.
# Polimorfismo en funciones: Funciones que aceptan diferentes tipos de objetos y ejecutan operaciones específicas basadas en esos tipos.


#Ejemplo de Polimorfismo con Herencia
class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "Guauuuu"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miauuuuuuu!"
    
def reproducir_sonido(animal):
    print(animal.hacer_sonido())

perro = Perro()
gato = Gato()

reproducir_sonido(perro)
reproducir_sonido(gato)