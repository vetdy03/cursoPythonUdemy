import json
from pathlib import Path

#escribir

# productos = [ 
#     {"id": 1, "name": "surf"},
#     {"id": 2, "name": "skate"},
#     {"id": 3, "name": "bici"}
# ]

# data = json.dumps(productos)
# # print(data)  # Imprime el JSON como una cadena
# Path("09-archivos/productos.json").write_text(data) 

#LEER JSON
data = Path("09-archivos/productos.json").read_text(encoding="utf-8")  # Lee el contenido del archivo JSON 
productos = json.loads(data) # Convierte el JSON a un objeto de Python
print(productos)  # Imprime la lista de productos

#MODIFICAR JSON
productos[0]["name"] = "feliz"
Path("09-archivos/productos.json").write_text(json.dumps(productos))  # Escribe la lista de productos modificada de nuevo en el archivo JSON