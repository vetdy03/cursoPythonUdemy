#PILAS-- > MONEDAS UNA ECNIMA OTRA ENCIMA, si quisieramos quitar deberiams quitar la de encima
#ejemplos de la vida real--> historia de navegacion
#LIFO last in first out
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ulti = pila.pop()
print(ulti)
print(pila)
print(pila[-1])
pila.pop()
pila.pop()
if not pila: #si pila es vacia mostramos de que si lo sea..
    print("Vacia")
