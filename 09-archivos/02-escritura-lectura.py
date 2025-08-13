from pathlib import Path

archivo = Path("09-archivos/archivo-prueba.txt")  # Crea un objeto Path para el archivo
text = archivo.read_text("utf-8").split("\n")  # Lee el contenido del archivo como texto y lo divide en líneas con la codificación UTF-8
print(text)  # Imprime el contenido del archivo
print(type(text))  # Imprime el tipo de la variable text
text.insert(0, "hola mundo")  # Inserta "hola mundo" al inicio de la lista text
archivo.write_text("\n".join(text))