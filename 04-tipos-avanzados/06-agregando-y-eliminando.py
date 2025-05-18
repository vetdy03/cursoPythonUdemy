mascotas = ["migui",
            "negro", 
            "migui",
            "pato", 
            "migui",
            "olaf",
            "pelusa"
            
            ]
mascotas.insert(1, "Melvin")
mascotas.insert(-1, "zack") ##para agregar al penultimo de la lista
mascotas.append("cody") #agrega al ultimo esto
mascotas.remove("migui") #elimina el ultimo
mascotas.pop() #elimina el ultimo elemento sin preguntar
print(mascotas.pop(1))#elimina el elmento de la posicon que le damos y podemos capturar ese elemento
del mascotas[0]#elementos dentro de la lista pero no devuelve ningun valor no se puede guardar
mascotas.clear()
# mascotas.reverse()# voltea la lista
# mascotas.sort() ordena sin parametro en orden alfabetico

print()
print(mascotas)
