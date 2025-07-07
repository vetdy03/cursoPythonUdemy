class MiError(Exception): #hereda de Exception
    "Clase personalizada para representar un error específico"
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo
    def __str__(self):
        return f"{self.mensaje} - código: {self.codigo}"

def div(n = 0):
    if n == 0:
        #raise se usa para lanzar una excepción
        raise MiError ("No se puede dividir por cero", 404)
    return 10 / n #segun las mat basicas no se puede dividir por cero

try: 
    div()
except MiError as e:
    print(e)
