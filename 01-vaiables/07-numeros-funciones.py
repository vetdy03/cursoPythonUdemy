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
print(math.fma(3,3,5)) # multiplica y suma
print(math.copysign(-5,8)) #copia el signo del segundo numero
print(math.trunc(math.copysign(5,-3))) #copia el signo del segundo numero
print(math.exp(3)) #eleva e a la potencia del numero
print(math.isfinite(8)) #si es finito
print(math.isinf(math.inf)) #si es infinito
print(math.log2(8)) #logaritmo en base 2
print(math.log10(100)) #logaritmo en base 10
print(math.radians(90)) #convierte a radianes
print(math.degrees(math.pi/2)) #convierte a grados
print(math.modf(0.33)) #parte decimal y entera
print(math.trunc(44.017)) #parte entera
