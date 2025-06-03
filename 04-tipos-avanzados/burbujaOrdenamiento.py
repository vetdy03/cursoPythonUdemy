from collections import OrderedDict

cadenita = input("Escribe tu cadenita: ")
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

#ordenar llaves de un diccionario y mostrar llave y valor en una TUPLA
ordenado = sorted(dic.items())#
print(type(ordenado))
print(ordenado)#imprime ordenado por llaves con ss valores mas EN UNA NUEVA TUPLA
