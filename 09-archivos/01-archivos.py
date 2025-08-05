from pathlib import Path
#import os
a = 1
# for a in range(1, 10):
#     archivo = Path(F"09-archivos/archivo-prueba{a}.txt")
#     archivo.write_text("Hola, este es un archivo de prueba by: Vetdy03.")  # Crea o escribe en el archivo

archivo = Path("09-archivos/archivo-prueba10.txt") # Crea un objeto Path para el archivo
#archivo.write_text("Hola, este es un archivo de prueba by: Vetdy03.")  # Crea o escribe en el archivo

#archivo.stats() # Imprime información del archivo
#contenido = archivo.read_text()  # Lee el contenido del archivo
#print(contenido)  # Imprime el contenido del archivodirectorio
print(archivo.exists())  # Verifica si el archivo existe
# print(archivo.is_file())  # Verifica si es un archivo
# print(archivo.stat())  # Obtiene información del archivo
#archivo.rename("nuevo_archivo1002.txt")  # Renombra el archivo cambiando la ruta
#archivo.with_suffix(".md")  # Cambia la extensión del archivo
archivo.rename(archivo.with_suffix(".md"))
#archivo.with_name("nuevo_archivo101.txt")  # Cambia el nombre del archivo manteniendo la ruta
#print(nuevo_nombre)
# archivo.unlink()  # Elimina el archivo
# print(archivo.parent)  # Imprime el directorio padre del archivo
# print(archivo.name)  # Imprime el nombre del archivo
# print(archivo.suffix)  # Imprime la extensión del archivo
#print(archivo.stem)  # Imprime el nombre del archivo sin la extensión
# directorio
# print(archivo.resolve())  # Imprime la ruta absoluta del archivo
# print(archivo.is_absolute())  # Verifica si la ruta es absoluta
# print(archivo.relative_to(Path.cwd()))  # Imprime la ruta relativa al directorio actual