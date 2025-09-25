import requests

# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout= 10) #get, post, put/path, delete
# print(
#     r.status_code,
#     r.text
# )
# r= r.json() #esto se llama casting o parseo o conversion o 
# for user in r:
#     print(user["name"],"-", user["email"])
# 
url = "https://jsonplaceholder.typicode.com/users/1"
user = {
    "id": 11,
    "name": "chanchito feliz"
}
r = requests.post(url, timeout=10, data=user)


# API = APLICATIONS PROGRAMING INTERFACE
# rest = REPRESENTATIONAL STATE TRANSFER