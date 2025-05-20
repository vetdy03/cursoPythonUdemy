listaDeCompras = [["cebolla",10],
                  ["carne",104],
                  ["queso",12],
                  ["pollo",90],
                  ["papa",200],
                  ["arroz",480],
                  ["azucar",350],
                  ["aceite",22],
                  ["naranja", 22]
                  ]
#DESCUENTO DEL 50 A PRODUCTOS QUE VALEN MAS DE 50
for producto in listaDeCompras:
    if producto[1] > 50:
        
        listaDeCompras[producto[1]//2]
        print(producto[1])
        
#listaDeCompras = list(map(lambda listaNueva: listaNueva[0]  ))
#print(listaDeCompras)

#NO SE PUEDE ->listaDeCompras2 = list(filter(lambda listadecomp: ((listadecomp[1] > 50)//2), listaDeCompras ))
