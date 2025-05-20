listaDeCompras = [["cebolla",10],
                  ["carne",104],
                  ["queso",12],
                  ["pollo",90],
                  ["papa",200],
                  ["arroz",480],
                  ["azucar",350],
                  ["aceite",22],
                  ["naranja",22]
                  ]
#DESCUENTO DEL 50 A PRODUCTOS QUE VALEN MAS DE 50
for producto in listaDeCompras:
    if producto[1] < 25:
        listaDeCompras.remove(producto)
        #print(producto[1])
    elif producto[1] > 50:
        producto[1] = int(producto[1]*0.5)

print(listaDeCompras)


#ELIMINAR PRODUCTOS QUE VALEN MENOS DE 25

#listaDeCompras = list(map(lambda listaNueva: listaNueva[0]  ))

#NO SE PUEDE ->listaDeCompras2 = list(filter(lambda listadecomp: ((listadecomp[1] > 50)//2), listaDeCompras ))
