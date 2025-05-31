#eliminar los espacios vacios de un strin y devolver una lista con los caracteres restantes
cadenita = input("Escribe tu cadenita: ")#lagunala
# nuevaCadena = ""
# for charr in cadenita:
#     if charr != " ":
#         nuevaCadena += charr
        
# print("Devolviendo la nueva {}".format(nuevaCadena))

#Contar en un diccionario cuantos se repiten 
cadenita2 = list(cadenita.lower())#lagunala
dic = {}
for charr in cadenita2:
    if charr not in dic:
        dic[charr] = 1
    elif charr in dic:
        dic[charr] += 1

sumaDeCaracteres = sum(dic.values())
print("Suma de caracteres:", sumaDeCaracteres)
print(dic)