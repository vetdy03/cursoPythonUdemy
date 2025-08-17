import os
from pathlib import Path
import sys
#print(sys.argv)  # Imprime los argumentos de la línea de comandos

def cli(args):
#     pass
    if len(args) == 1:
        print("No se han proporcionado argumentos.")
        return
    if len(args) != 3:
        print("Se necesitan 2 argumentos.")
        return
    
    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe.")
        return #retorna none y termina la función, porque? porque no tiene sentido seguir

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino no puedo existir.")
        return #retorna none y termina la función, porque? porque no tiene sentido seguir
    
    os.rename(o, d) #renombra el archivo origen al destino
    # os.rename(str(origen), str(destino)) #otra forma de renombrar
    print("Archivo movido exitosamente.")
    
cli (sys.argv)
