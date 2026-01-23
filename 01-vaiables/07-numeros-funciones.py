import math

print(round(8.33))
negativo = -4
if negativo < 0:
    postivo = negativo * (-1)
    print(postivo)
print(abs(-3)) # lo vuelve postivo el numero


print(math.ceil(-10)) ##lleva al num entero mas cercano
print(math.floor(2.99)) #al numero entero hacia abajo
print(math.isnan(8)) # esto es para saber si es un numero o no
print(math.factorial(5)) # saca el factorial de un numero
print(int(math.pow(10,2))) #Eleva a la potencia
print(math.sqrt(9)) #eleva al cuadrado
print(math.fma(3,3,5)) 
print(math.modf(16))
print(math.trunc(15.17))
