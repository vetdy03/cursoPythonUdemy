class Ave: ##CLASE PADRE O SUPER CLASE
    def __init__(self):
        self.volador = True
    
    def vuela(self):
        print("vuela ave")
      
class Pato(Ave): # SUBCLASE O CLASE HIJA 
    def __init__(self):
        super().__init__()
        self.nada = False
    
    def vuela(self):
        super().vuela()
        print("Vuelava pato")
    
pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)#esto da ERROR.- se debe llamar al constructor de la clase padre en la subclase