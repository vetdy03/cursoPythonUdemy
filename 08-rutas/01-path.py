from pathlib import Path

#Path(r"C:\Users\vetdy03\Documents\cursos\cursoPythonUdemy\08-rutas\01-path.py")
#Path(r"\home\vetdy03\Documents\cursos\cursoPythonUdemy\08-rutas\del.py")
path = Path("/home/vetdy03/Documents/cursos/cursoPythonUdemy/08-rutas/one/")
patito = Path("del.py")
path.is_file()
print(patito.is_file())

print(patito.is_dir())
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
