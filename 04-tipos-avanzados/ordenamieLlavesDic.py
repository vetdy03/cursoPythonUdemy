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

#ord#ordenar llaves de un diccionario y mostrar llave y valor en una TUPLA
ordenado = sorted(dic.items())#
print(ordenado)#imprime ordenado por llaves con ss valores mas EN UNA NUEVA TUPLA

#ORDENA LLAVES DE UN DIC PERO SOLO DEVUELVE LAS LLAVES EN UNA LISTA
ordenado2 = sorted(dic.keys())
#print(type(ordenado2))
print(ordenado2)

#creando u nnuevo DICCIONARIO ORDEN DE INSERCCION
mi_dic_new = OrderedDict(sorted(dic.items()))
print(type(mi_dic_new))
print(mi_dic_new)