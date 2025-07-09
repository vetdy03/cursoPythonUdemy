#from usuarios.acciones import guardar # * #Nunca importar todo con *
import usuarios.acciones # no es incorrecto pero es muy tedioso
from usuarios.acciones import guardar #RECOMENDADO
from usuarios import acciones # RECOMENDADO

acciones.guardar()









# # guardar()
# def guardar():
    # print("soy app.py y estoy guardando datos...")
