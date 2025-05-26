lista = [1, 2, 3, 4]
# print()
# print(*lista) # cualquier iterable si le pones asterisco lo hace automatico

lista2 = [4, 6, 7, 8]

combinada = ["hola", *lista, *lista2] #agregando digo uniendo listas iterables
print(combinada)

punto1 = {"x": 19, "y":"hola"}
punto2 = {"y": 15}

combinadaConDicicionarios  = {**punto1, "lala": "vetdy03", **punto2, "zz":"fuck xd"} #combinando diccionarios
print(combinadaConDicicionarios)