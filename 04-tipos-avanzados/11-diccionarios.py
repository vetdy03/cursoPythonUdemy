punto = {"x": 25, "y": 50, "z": 75} # string si o si despues lo que sea y numero en ese orden
print(punto)
print(punto["x"]) #no se puede acceder por posicion sino por el string asociado
punto["w"] = 45
#print(punto)
#print(punto, punto["w"])
if "lala" in punto:
    print("encontre", punto["lala"])

print(punto.get("lala", 97))
del punto["x"] #eliminar alguna de estas llaves incluyendo su valor
print(punto)
del (punto["y"])
print(punto)

for valor in punto:
    print(valor, punto[valor])
    
for valor in punto.items(): #devuelve tuplas que raro
    print(valor)
    
for llave, valor in punto.items():
    print(llave, valor)
    
 #min  2 
 
usuarios = [
     {"id":1, "nombre": "chanchito"},
     {"id":2, "nombre": "Feliz"},
     {"id":3, "nombre": "Nico"},
     {"id":4, "nombre": "felipe"},
     {"id":5, "nombre": "vetdy"},
     {"id":6, "nombre": "clexo"}

 ]
for usuario in usuarios:
     print(usuario["nombre"])
