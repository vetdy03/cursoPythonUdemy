users = [["chanchito", 8],
         ["zelipe", 7],
         ["pulga", 4]
         ]

# nombres = []
# for usuario in users:
#     nombres.append(usuario[0])
#     #MAP
# nombres = [usuario[0] for usuario in users]    #usuario[0] accedemos al primer elemento
#     #filtrar FILTER
# nombres= [usuario[0] for usuario in users if usuario[1] > 5]#nombres= [expresion forn item in items]

# nombres = list(map(lambda usuario: usuario[0], users))
menosUsers = list(filter(lambda usuario: usuario[1] > 2, users))# f(x) anonima filter recibe funcion lambda
        #ARRIBA 
print(menosUsers)







#aplicar descuento y mostrar los que valen menos de 50 bs 