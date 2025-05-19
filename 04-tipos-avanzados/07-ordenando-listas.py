numeros = [1, 4, 77, 33, 66, 23, 44]

numeros2 = sorted(numeros, reverse=True)#ordena y copia a u nuevo arreglo xd
numeros.sort()#orden ascendente y se chingo
numeros.sort(reverse=True)#de atras adela

print(numeros2)
print(numeros)

# users = [[4, "chanchito"],
#          [1, "felipe"],
#          [5, "pulga"]
#          ]
users = [["chanchito", 8],
         ["zelipe", 7],
         ["pulga", 4]
         ]

def ordena(ele):
    return ele[1]
olaf = ordena(users)
print(olaf)

users.sort(key=ordena)#orden segun el ordena
print(users)
users.sort(key=ordena, reverse= True) 
print(users)

