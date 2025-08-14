# import time

# print(time.time())  # Imprime el tiempo actual en segundos desde la época (epoch)


#import datetime
from datetime import datetime

fecha = datetime(2025, 1, 1)
fecha2  = datetime(2025, 2, 1)
print(fecha)  # Imprime la fecha y hora especificadas
print(fecha2)  # Imprime la segunda fecha y hora especificadas

ahora = datetime.now()  # Obtiene la fecha y hora actuales
print(ahora)  # Imprime la fecha y hora actuales

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%A")  # Convierte una cadena a un objeto datetime
print(fechaStr)  # Imprime la fecha convertida desde la cadena