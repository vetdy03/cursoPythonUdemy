listaDeCompras = [["cebolla",10], #1#
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
def aplicarDescuentoMenos50(listaDeComprass):
    for producto in listaDeCompras:
        if producto[1] > 50:
            producto[1] = int(producto[1]*0.5)
    
    return listaDeComprass
print(aplicarDescuentoMenos50(listaDeCompras))

#ELIMINAR PRODUCTOS QUE VALEN MENOS DE 25
def eliminarMenosDe10(listaDeComprass):
    for i in range(len(listaDeComprass)-1, -1, -1):
        if listaDeComprass[i][1] < 25:
            del(listaDeComprass[i])
    return listaDeComprass

print(eliminarMenosDe10(listaDeCompras))




#listaDeCompras = list(map(lambda listaNueva: listaNueva[0]  ))

#NO SE PUEDE ->listaDeCompras2 = list(filter(lambda listadecomp: ((listadecomp[1] > 50)//2), listaDeCompras ))
