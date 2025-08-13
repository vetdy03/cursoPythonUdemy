#import pathlib as Path
from pathlib import Path 
from zipfile import ZipFile

# with ZipFile("09-archivos/comprimidos.zip", "w") as zip: # Abre el archivo ZIP en modo escritura
#     #curso py
#     for path in Path().rglob("*.*"): # Recorre todos los archivos en el directorio actual y sus subdirectorios
#         print(path)  # Imprime la ruta del archivo
#         if str(path) != "09-archivos/comprimidos.zip":  # Si el archivo no es el ZIP que estamos creando
#             zip.write(path)

#leer zip
with ZipFile("09-archivos/comprimidos.zip") as zip:  # Abre el archivo ZIP en modo lectura 
    #print(zip.namelist())  # Imprime la lista de archivos en el ZIP
    info = zip.getinfo("09-archivos/06-comprimidos.py")  # Obtiene información sobre el archivo ZIP
    print(
        info.file_size, # Imprime el tamaño del archivo ZIP
        info.compress_size # Imprime el tamaño comprimido del archivo ZIP
        # info.is_dir(), # Imprime si el archivo es un directorio
        # info.filename, # Imprime el nombre del archivo
        # info.date_time, # Imprime la fecha y hora de modificación del archivo
    )

    zip.extractall("09-archivos/extract")  # Extrae todos los archivos del ZIP al directorio "extract"