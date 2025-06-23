class Vehiculo:
    def moverse(self):
        return "El vehículo se mueve."

class Coche(Vehiculo):
    def moverse(self):
        return "El coche está conduciendo."

class Barco(Vehiculo):
    def moverse(self):
        return "El barco está navegando."

vehiculos = [Coche(), Barco()]

for vehiculo in vehiculos:
    print(vehiculo.moverse())
    
