import csv
import os
#escribir
# with open("09-archivos/archivo.csv", "w") as archivo: # Abre el archivo en modo escritura
#     writer = csv.writer(archivo)  # Crea un objeto writer para escribir en el archivo CSV
#     writer.writerow(["twit_id", "user_id", "text"]) # Escribe la cabecera del CSV
#     writer.writerow([100, 1, "pablo"]) # Escribe una fila de datos en el CSV])
#     writer.writerow([101, 2, "maria"]) # Escribe otra fila de datos en el CSV
#     writer.writerow([102, 3, "pedro"]) # Escribe otra fila de datos en el CSV

#leer
# with open("09-archivos/archivo.csv", "r") as archivo:  # Abre el archivo en modo lectura
#     reader = csv.reader(archivo)
#     print(list(reader))  # Imprime el objeto reader
#     archivo.seek(0)  # Mueve el cursor al inicio del archivo
#     for line in reader:  # Itera sobre cada línea del archivo CSV
#         print(line)

# LEER Y MODIFICAR actualizar
with open("09-archivos/archivo.csv") as r, open("09-archivos/archivo_temp.csv", "w") as w:  # Abre el archivo en modo lectura y escritura
    reader = csv.reader(r)
    writer = csv.writer(w)
    for line in reader :  # Itera sobre cada línea del archivo CSV
        if line[0] == "100":  # Si el primer elemento de la línea es "101"
            writer.writerow([100, 1, "pablo actualizado"])  # Escribe la línea modificada en el archivo temporal
        else:
            writer.writerow(line)  
    os.remove("09-archivos/archivo.csv")  # Elimina el archivo original
    os.rename("09-archivos/archivo_temp.csv", "09-archivos/archivo.csv")  # Renombra el archivo temporal al nombre original