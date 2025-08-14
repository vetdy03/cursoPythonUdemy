from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)  # Crea una fecha con un día añadido
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1  # Calcula la diferencia entre las dos fechas
print(delta)  # Imprime la diferencia como un objeto timedelta
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds", delta.total_seconds())  # Imprime el total de segundos de la diferencia