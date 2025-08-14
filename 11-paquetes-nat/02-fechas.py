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

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")  # Convierte una cadena a un objeto datetime
#print(fechaStr)  # Imprime la fecha convertida desde la cadena

print(fecha.strftime("%Y.%m.%d"))

print(fecha > fecha2)  # Compara las dos fechas

print(
    fecha.year, # Imprime el año de la fecha
    fecha.month, # Imprime el mes de la fecha
    fecha.day, # Imprime el día de la fecha
    fecha.weekday(), # Imprime el día de la semana (0=Monday, 6=Sunday)
    fecha.isoweekday(), # Imprime el día de la semana (1=Monday, 7=Sunday)
)