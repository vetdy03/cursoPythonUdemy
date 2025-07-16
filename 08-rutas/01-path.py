from pathlib import Path

#Path(r"C:\Users\vetdy03\Documents\cursos\cursoPythonUdemy\08-rutas\01-path.py")
path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,  # Nombre del archivo
    path.stem,  # Nombre del archivo sin extensión
    path.suffix,  # Extensión del archivo
    path.parent,  # Carpeta padre
    path.absolute(),  # Ruta absoluta
    # path.resolve(),  # Ruta absoluta resuelta
)

p = path.with_name("chanchito.py")  # Cambia el nombre del archivo
print(p)    
print(path.with_suffix(".txt"))  # Cambia la extensión del archivo
