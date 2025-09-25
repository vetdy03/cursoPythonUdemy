import requests

#url = "https://jsonplaceholder.typicode.com/users"

##METODO GET
#r = requests.get(url, timeout= 10)# esto es una peticion http donde url es el recurso y #get, post, put/path, delete
# print(
#     r.status_code,
#     r.text
# )
# r= r.json() #esto se llama casting o parseo o conversion o 
# for user in r:
#     print(user["name"],"-", user["email"])


##METODO GET PARA LISTAR SOLO UN USER
# url = "https://jsonplaceholder.typicode.com/users/1"
# r = requests.get(url, timeout=10)
# print(r.json())

##METODO POST PARA CREAR UN USER
# url = "https://jsonplaceholder.typicode.com/users/"
# user = {
#     "id": 11,
#     "name": "chanchito feliz"
# }
# r = requests.post(url, timeout=10, data=user) #que hace esta linea de odigo? #hace una peticion post a la url con el user como data que mandamos 
# print(r.json())
# print(r.status_code)

##METODO PUT/PATCH PARA ACTUALIZAR UN USER
# url = "https://jsonplaceholder.typicode.com/users/2"
# user = {
#     "name": "chanchito triste"
# }
# r = requests.put(url, timeout=10, data=user) 
# print(r.json())
# print(r.status_code)
# 
# 
#METODO DELETE PARA ACTUALIZAR UN USER
# url = "https://jsonplaceholder.typicode.com/users/2"
# r = requests.put(url, timeout=10) 
# print(r.json())
# print(r.status_code)

##METODO DELETE PARA ACTUALIZAR UN USER
url = "https://jsonplaceholder.typicode.com/users/2"
apikeyOfVetdy03 = "1234567890"
headers = {
    "Authorization": f"Bearer {apikeyOfVetdy03}"
}
r = requests.put(url, timeout=10, headers=headers) 
# print(r.json())
print(r.status_code)




# API = APLICATIONS PROGRAMING INTERFACE= es como tu interactuas con un software 
# rest = REPRESENTATIONAL STATE TRANSFER = se usa para representar recursos
