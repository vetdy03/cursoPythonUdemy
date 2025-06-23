def sumar(a, b):
    return a + b

#usart la fx con dif tipos de datos
print(sumar(2, 4))
print(sumar(2.5, 2.6))
print(sumar("hola ", "mundo"))

#Explicación:

#La función sumar() es polimórfica porque acepta diferentes tipos de datos: enteros, flotantes y cadenas. Python decide el comportamiento de la función en tiempo de ejecución, dependiendo del tipo de los argumentos.