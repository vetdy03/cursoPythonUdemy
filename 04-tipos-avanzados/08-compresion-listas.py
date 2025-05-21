users = [["chanchito", 8],
         ["zelipe", 7],
         ["pulga", 4]
         ]

# nombres = []
# for usuario in users:
#     nombres.append(usuario[0])
#     #MAP sin map
#nombres = [usuario[0] for usuario in users]    #usuario[0] accedemos al primer elemento
#     #filtrar sin FILTER
nombresSinFilter= [usuario[0] for usuario in users if usuario[1] > 5]#nombres= [expresion forn item in items]
print(nombresSinFilter)
        #mapear con map
nombres = list(map(lambda usuario: usuario[0], users))#mapear con maps
    #filter con filter
menosUsers = list(filter(lambda usuario: usuario[1] > 2, users))# f(x) anonima filter recibe funcion lambda
         
print(menosUsers)



# filter → filtra una lista según una condición.

# lambda → es una función rápida sin nombre.

# # list → convierte el resultado en una lista normal.



# #aplicar descuento y mostrar los que valen menos de 50 bs 