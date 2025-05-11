saludo = 25

def saludar():
    global saludo
    saludo= "hola mundo"
    print(saludo)
def saludaChancito():
    saludo = "hola segudo saludador"
    print(saludo)
resul1 = saludo +3
print(resul1)
saludar()
resul2 = saludo + 3
print(resul2)

print(saludo)
saludaChancito()
