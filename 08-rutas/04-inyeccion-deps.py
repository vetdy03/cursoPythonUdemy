from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]  # esto es asignacion de lista por comprension

def load(p):
    
    paquete = __import__(print(str(p).replace()))

list(map(load, paths))  # esto es asignacion de lista por comprension