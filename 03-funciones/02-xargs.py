def suma(*numeros):
    #print(a + b +c)
    resltado = 0
    for num in numeros:
        resltado += num
    print(resltado)

    
suma(2, 5, 7)
suma(2, 5)
suma(2, 5, 7, 8)