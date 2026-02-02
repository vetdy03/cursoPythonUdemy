# Primero instala selenium ejecutando en la terminal:
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

# esto sirve para que no se cierre el navegador automáticamente
# options = webdriver.ChromeOptions() # Configuramos opciones para el navegador
# options.add_experimental_option("detach", True) # Evita que el navegador se cierre automáticamente

browser = webdriver.Chrome()#options=options) 
browser.implicitly_wait(10)
browser.get("https://github.com")

link = browser.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
link.click() # Simula el click en el enlace


user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")
user_input.send_keys(os.environ.get("GITHUB_USER")) # Simula escribir el usuario
pass_input.send_keys(os.environ.get("GITHUB_PASS"))

# wait = WebDriverWait(browser, 10)

pass_input.send_keys(Keys.RETURN) # Simula presionar la tecla Enter

profile = browser.find_element(
    By.CLASS_NAME,
    "AppHeader-context-item-label"
)
label = profile.get_attribute("innerHTML") # Extrae el texto del elemento
assert "Dashboard" in label # Verifica que el texto contenga "Dashboard"
print("Login exitoso")

browser.quit()# close the browser)
##no funciona
# linkk = browser.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
# waitt = WebDriverWait(browser, 10)
# linkk.click() # Simula el click en el enlace