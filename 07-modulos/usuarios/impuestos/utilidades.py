if __name__ != "__main__":
    from usuarios.gestion.crud import guardar_crud 
    from ..gestion.crud import guardar_crud 

    print(__name__)

    def pagar_impuestos():
        print("Pagando impuestos desde utilidades.py...")
        guardar_crud()

if __name__ == "__main__":
    print("tarea de mantenimiento")
