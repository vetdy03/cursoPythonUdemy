import requests #para hacer consultas a https
from bs4 import BeautifulSoup #sirve para parsear html y xml 

url = "https://stackoverflow.com/questions"
resp = requests.get(url) #esto sirve para poder hacer peticiones get a la ulr 
texto = resp.text
soup = BeautifulSoup(texto, "html.parser") #esto sirve para parsear el html
preguntas = soup.select(".s-post-summary") or soup.select("js-post-summary")
print(preguntas[0]["data-post-id"])
for pregunta in preguntas:
    titulo = pregunta.select_one("s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print(f"{usuario.strip()} - Titulo:\{titulo.strip()}")