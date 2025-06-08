#eliminar los espacios vacios de un strin y devolver una lista con los caracteres restantes
cadenita = input("Escribe tu cadenita: ")#lagunala
nuevaCadena = ""
for charr in cadenita:
    if charr != " ":
        nuevaCadena += charr
        
print("Devolviendo la nueva {}".format(nuevaCadena))

#Contar en un diccionario cuantos se repiten 
cadenita2 = list(nuevaCadena.lower())#lagunala #["l", "a", "g", "u", "n", "a", "l", "a",]
#cadenita2 = list(cadenita.lower())#lagunala
dic = {}
for charr in cadenita2:
    if charr not in dic:
        dic[charr] = 1
    elif charr in dic:
        dic[charr] += 1

#EXTRA SUMA DE CARACTERES
sumaDeCaracteres = sum(dic.values())
print("Suma de caracteres: {}".format(sumaDeCaracteres))
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


#{ de la linea 40 a la son los mismos sol oque uno es de forma simple y la tradicional}
#-----*OTRA FORMA DE SACAR EL MAYOR EN LISTA DE TUPLAS*------#
newTuple = list(dic.items())#convertir el diccionario en una lista de tuplas
mayor_val = None
masRepetidas = []
for tuplee in newTuple:
    if mayor_val is None or tuplee[1] > mayor_val:
        mayor_val= tuplee[1]
        
for tuplee in newTuple:
    if tuplee[1] == mayor_val:
        masRepetidas.append(tuplee)
print("la mas repetida es:{}".format(masRepetidas))
#DE UN LISTADO DE TUPLAS, DEVOLVER LAS TUPLAS QUE TENGAN EL MAYOR VALOR. Obtener el valor máximo de repeticiones

maxRepeticiones = max(dic.values())
maximosDecimoPrimero = [(letra, cantidad) for letra, cantidad in dic.items() if cantidad == maxRepeticiones]
print("las letras que mas se repiten son: ")
for letra, cantidad in maximosDecimoPrimero:
    print("{} se repite {}".format(letra, cantidad))