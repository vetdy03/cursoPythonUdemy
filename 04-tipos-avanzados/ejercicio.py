#eliminar los espacios vacios de un strin y devolver una lista con los caracteres restantes
cadenita = input("Escribe tu cadenita: ")
nuevaCadena = ""
for charr in cadenita:
    if charr != " ":
        nuevaCadena += charr
        
print("Devolviendo la nueva {}".format(nuevaCadena))