nums = [1, 2, 3]#, 4, 5, 6]

#feyo
primero = nums[0]
segundo = nums[1]
tercero = nums[2]

#primero, segundo, tercero = nums # el tam debe ser igual a num de variables declaras
#primero, = nums #no se puede acceder a un solo elemeto de la lista
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
primero, segundo, *others, penu, ultimo = nums #ese * lo hace iterable es como : primero=[1] y *otros = [2, 3]
print(primero, segundo,  others, penu, ultimo) #imprimimos pero no da error si no llamo a todos
