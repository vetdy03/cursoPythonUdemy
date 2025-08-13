from io import open
#ESCRITURA Y LECTURA DE ARCHIVOS
# texto = "hola mjundo mundial donde andas chicocos?"

# archivo = open("09-archivos/hola-mundo.txt", "w") # Abre el archivo en modo escritura
# archivo.write(texto) # Escribe el texto en el archivo
# archivo.close() # Cierra el archivo después de escribir

# #LECTURA DE ARCHIVO
# archivo = open("09-archivos/hola-mundo.txt", "r")
# texto = archivo.read() # Lee todo el contenido del archivo
# archivo.close() # Cierra el archivo después de leer
# print(texto)

# #LECTURA COM LISTA
# archivo = open("09-archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()  # Lee el contenido del archivo como una lista de líneas
# archivo.close() # Cierra el archivo después de leer y evitar errores
# print(texto)

# with open("09-archivos/hola-mundo.txt", "r") as archivo:  # Abre el archivo en modo lectura
#     print(archivo.readlines())  # Lee el contenido del archivo como una lista de líneas
#     archivo.seek(0)  # Mueve el cursor al inicio del archivo
#     for linea in archivo:  # Itera sobre cada línea del archivo    
#         print(linea)


# #AGREGAR TEXTO A UN ARCHIVO
# archivo = open("09-archivos/hola-mundo.txt", "a+") # Abre el archivo en modo append (añadir)
# archivo.write(" chao mundo")  # Escribe "chao mundo" al final del archivo
# archivo.close() # Cierra el archivo después de escribir 
# 

# LECTURA Y ESCRITURA
with open("09-archivos/hola-mundo.txt", "r+") as archivo:  # Abre el archivo en modo lectura y escritura
    texto = archivo.readlines()
    archivo.seek(0) # Mueve el cursor al inicio del archivo
    texto[0] = "rebeca i love"  # Modifica la primera línea de la lista texto
    archivo.writelines(texto) # Escribe la lista texto de nuevo en el archivo

# Abre el archivo en modo append (añadir)