import math

n1 = int(input("Ingresa primer numero: "))
n2 = int(input("Ingresa segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2 

mesage = f"""
para {n1} y {n2}
la suma es {suma}
la resta es {resta}
la multi es {multi}
la div es {div}
"""
print(mesage)