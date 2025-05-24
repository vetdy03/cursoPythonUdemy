#significa grupo o conjunto..
#no se repite y es ordenado si o si 
letras = {"c", 'b', 'b', 'a'}
print(letras)
primer = {1, 1, 2, 4}
primer.remove(1)#eliminar elementos
primer.add(7) #aniadir elemento
#primer.remove(8) # error al no encontra elemento para elminar
print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)
#print(primer | segundo) #union
print(primer & segundo)# intersecion
print(primer - segundo) # diferencia.- elimina lo que si hay en "primer 1 2" de "segundo 2 3"--> 2 
print(primer ^ segundo)# diferencia simetrica.- elimina lo que se enceuntra duplicado entre el primer y segundo 

if 5 in segundo:
    print("si hay xd")