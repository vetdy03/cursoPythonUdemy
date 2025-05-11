def calcu():
    print("Los operadores disponibles son: *, +, /, - \n para salir \"salir\"")
    resultado = ""   # resultado es falso
    while True:
        if not resultado: # is es verdadero
            resultado = input("Ingrese numero: ")
            if resultado.lower() == "salir":
                break
            resultado = int(resultado)
        operador = input("Ingrese operación: ")
        if operador.lower() == "salir":
            break
        n2 = input("Ingrese siguiente numero: ")
        if n2.lower() == "salir" :
            break
        n2 = int(n2)
        if operador.lower() == "suma":
            resultado += n2
        elif operador.lower() == "multi":
            resultado *= n2
        elif operador.lower() == "resta":
            resultado -= n2
        elif operador.lower() == "div":
            resultado /= n2
        else:
            print("Operación no valida")  
    
        print("El resultado es: {}".format(resultado))
        
        
        

if __name__ == "__main__":
    calcu()