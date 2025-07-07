def div(n = 0):
    if n == 0:
        #raise se usa para lanzar una excepción
        raise ZeroDivisionError ("No se puede dividir por cero", f"n: {n}")
    return 10 / n #segun las mat basicas no se puede dividir por cero

try: 
    div()
except ZeroDivisionError as e:
    print(f"Error: {e}")