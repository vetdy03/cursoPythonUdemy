try:
    n1 = int(input("Introduce un primer número: "))
except ValueError as e:
    print("Ingrese un valor que corresponda.")
else:
    print("no hubo errores")
finally:
    print("Esto se ejecuta siempre, independientemente de si hubo una excepción o no.")
    print("Fin del programa.")