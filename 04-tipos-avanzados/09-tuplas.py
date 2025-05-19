#no se puede modificar ni elimnar

numeros = (2,3,4,5,6)+(44,45, 17, 60, 80)#
print(numeros)
punto1 = tuple([1, 2])
print(punto1)
menosNUm= numeros[:3]
print(menosNUm)
prim, segu, *otros, ulti = numeros
print(prim, segu, otros, ulti)

for n in numeros:
   print(n)

listanew = list(numeros)
print("tupla cnvertida en lista:\n{}".format(listanew))
# punto = tuple("cadena")
# print(punto)