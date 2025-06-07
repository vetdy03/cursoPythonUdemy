#eliminar los espacios vacios de un strin y devolver una lista con los caracteres restantes
cadenita = input("Escribe tu cadenita: ")#lagunala
nuevaCadena = ""
for charr in cadenita:
    if charr != " ":
        nuevaCadena += charr
        
print("Devolviendo la nueva {}".format(nuevaCadena))

#Contar en un diccionario cuantos se repiten 
cadenita2 = list(nuevaCadena.lower())#lagunala
#cadenita2 = list(cadenita.lower())#lagunala
dic = {}
for charr in cadenita2:
    if charr not in dic:
        dic[charr] = 1
    elif charr in dic:
        dic[charr] += 1

sumaDeCaracteres = sum(dic.values())
print("Suma de caracteres:", sumaDeCaracteres)
print(dic)
## SALIDA: {'d': 3, 'i': 8, 'c': 6, 'o': 7, 'n': 6, 'a': 10, 'r': 5, 'e': 3, 'u': 3, 'q': 1, 'm': 2, 'b': 1, 's': 1, 'p': 2, 'l': 1}


#verificar cuáles valores son mayores a 4
#letra toma el valor de la clave (en tu caso, cada carácter de la cadena).
#cantidad toma el valor asociado a esa clave (cuántas veces aparece ese carácter).
for letra, cantidad in dic.items():#devuelve una lista de tuplas, donde cada tupla es (clave, valor) del diccionario.
    if cantidad > 4:
        print(f"La letra '{letra}' se repite {cantidad} veces.")

for llave, cant in dic.items():
    if cant >= 4:
        print("La letra {} se repite {}".format(llave, cant))
