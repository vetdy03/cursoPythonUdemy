from pathlib import Path

path = Path("08-rutas")
# path.exists()  # Verifica si el directorio existe
# path.is_dir()  # Verifica si es un directorio
# path.mkdir(exist_ok=True)  # Crea el directorio si no existe
# path.rmdir()  # Elimina el directorio condicion (debe estar vacío)
# path.rename("chanchito_feliz")  # Renombra el directorio

# for p in path.iterdir():
#     print(path.iterdir())  # Itera sobre los elementos del 

archi = [p for p in path.iterdir() if not p.is_dir()]
archi = [p for p in path.glob("01*.py") ] # Lista los archivos en el directorio
archi = [p for p in path.glob("**/*.py") ] # lista todo de adelante y s hubiese subdirectorios
archi = [p for p in path.rglob("*.py") ] # lista recursivamente todo de adelante y s hubiese subdirectorios


print(archi)  # Lista los archivos en el directorio