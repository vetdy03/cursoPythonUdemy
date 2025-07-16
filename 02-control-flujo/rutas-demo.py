from pathlib import Path

path = Path("02-control-flujo")
# path.exists()  # Verifica si el directorio existe
# path.is_dir()  # Verifica si es un directorio
# path.mkdir(exist_ok=True)  # Crea el directorio si no existe
# path.rmdir()  # Elimina el directorio condicion (debe estar vacío)
# path.rename("chanchito_feliz")  # Renombra el directorio

for p in path.iterdir():
    print(path.iterdir())  # Itera sobre los elementos del 
