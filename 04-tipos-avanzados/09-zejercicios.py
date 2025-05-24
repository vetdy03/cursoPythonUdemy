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
#FILTRAR PRODUCTOS ECONOMICOS
proEconomicos = []
def productosEconomicos(listaDeComprass):
    for producto in listaDeComprass:
        if producto[1] < 50:
            proEconomicos.append(producto)
    return proEconomicos
print("\nfiltra productos economicos")
print(productosEconomicos(listaDeCompras))

#DESCUENTO DEL 50 A PRODUCTOS QUE VALEN MAS DE 50
#MEJORANDO ESTO Si un producto cuesta más de 100, aplicarle 30%. Si cuesta entre 50 y 100, 15%. Si cuesta menos de 50, no tiene descuento.
def aplicarDescuentoMenos50(listaDeComprass):
    for producto in listaDeComprass: # 
        if producto[1] > 100:
            producto[1] = producto[1] - int(producto[1]*0.3)
        if 100 > producto[1] >= 50:
            producto[1] = producto[1] - int(producto[1]*0.15)
            
    return listaDeComprass
print("\naplicar descuentos de 100 30%......")
print(aplicarDescuentoMenos50(listaDeCompras))

#ELIMINAR PRODUCTOS QUE VALEN MENOS DE 25
# def eliminarMenosDe10(listaDeComprass):
#     for i in range(len(listaDeComprass)-1, -1, -1):
#         if listaDeComprass[i][1] < 25:
#             del(listaDeComprass[i])
#     return listaDeComprass
# print(eliminarMenosDe10(listaDeCompras))


    

#lumnos con baja nota de 51#


#listaDeCompras = list(map(lambda listaNueva: listaNueva[0]  ))

#NO SE PUEDE ->listaDeCompras2 = list(filter(lambda listadecomp: ((listadecomp[1] > 50)//2), listaDeCompras ))
