from functools import reduce

listaDeCompras = [["cebolla",10], #1#
                  ["carne",104],
                  ["queso",12],
                  ["pollo",90],
                  ["papa",200],
                  ["arroz",480],
                  ["azucar",350],
                  ["aceite",22],
                  ["naranja",22] #9
                  ]
#Sumar los precios de todos los productos (con o sin descuentos). CON REDUCE
def sumaConReduce(listaDeComprass):
    total = reduce(lambda acum, producto: acum + producto[1], listaDeComprass, 1)#lambda ...= suma el precio del producto en ACUM
                            #listaDeComprass la lista iterable -------- 0= valor inicial de acum
    return total
print(f"Total de la compra con REDUCE ES: {sumaConReduce(listaDeCompras):.2f} Bs")

def sumaConSuma(lisaDeComprass):
    total = sum(producto[1] for producto in lisaDeComprass)
    return total
print(f"Sumando con SUM es: {sumaConSuma(listaDeCompras):.2f} Bs")

def sumaConFor(listaDeCompras):
    total = 0
    for producto in listaDeCompras:
        total += producto[1]
    return total
print("El total con FOR es: {}".format(sumaConFor(listaDeCompras)))

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
    contadorDescuento= 0
    for producto in listaDeComprass: # 
        if producto[1] > 100:
            producto[1] = producto[1] - int(producto[1]*0.3)
            contadorDescuento +=1
        elif 100 > producto[1] >= 50:
            producto[1] = producto[1] - int(producto[1]*0.15)
            contadorDescuento += 1
    return listaDeComprass, contadorDescuento
listaDeDescuentos, contadorDescuentoUltimo = aplicarDescuentoMenos50(listaDeCompras)
print("\nDescuento para precios mayores a 100->30%, 100-50->15%, total de = {} productos \n{}\n".format(contadorDescuentoUltimo, listaDeDescuentos))
##print(aplicarDescuentoMenos50(listaDeCompras))

#CREAR TICKET DE COMPRA 
def ticketDeCompra(listaDeComprass):
    for producto in listaDeComprass:
        print("______________****_____________")        
        valor= "|Nombre del producto: " + str(producto[0]).upper() +"\nPrecio Original:  "+ str(producto[1])
        #print(valor)
        if producto[1] > 100:
            valor = valor +"\nPrecio con descuento: {} Bs".format(producto[1] - producto[1]*0.30)
        elif 100> producto[1] >= 50:
            valor = valor +"\nPrecio con descuento: {} Bs".format(producto[1] - producto[1]*0.15)
        else:
            valor = valor +"\nNo aplica descuento"      
        print("\n"+valor+"\n|_____________________________|")
print(ticketDeCompra(listaDeCompras))

#ELIMINAR PRODUCTOS QUE VALEN MENOS DE 25
def eliminarMenosDe10(listaDeComprass):
    for i in range(len(listaDeComprass)-1, -1, -1):
        if listaDeComprass[i][1] < 25:
            del(listaDeComprass[i])
    return listaDeComprass
print(f"\nProductos que valen menos de 50 eliminados\n{eliminarMenosDe10(listaDeCompras)}")


    

#lumnos con baja nota de 51#


#listaDeCompras = list(map(lambda listaNueva: listaNueva[0]  ))

#NO SE PUEDE ->listaDeCompras2 = list(filter(lambda listadecomp: ((listadecomp[1] > 50)//2), listaDeCompras ))
