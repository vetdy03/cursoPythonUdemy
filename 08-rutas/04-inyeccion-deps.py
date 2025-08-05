from pathlib import Path
path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]  # esto es asignacion de lista por comprension

depden = {
    "db": "db",
    "api": "es la api",
    "graql": "es la graql"
}

def load(p):
    
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**depden)
    except:
        print("El paquete no tiene funcion init()")

list(map(load, paths))  # esto es asignacion de lista por comprension