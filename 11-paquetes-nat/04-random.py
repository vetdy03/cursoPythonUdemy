import random
import string

lists = [1, 2, 3, 4, 5, 6, 7, 8]
lists2 = [1, 2, 3, 4, 5, 6, 7, 8]

random.shuffle(lists)  # Mezcla aleatoriamente los elementos de la lista

print(
    random.random(),
    random.randint(1, 10),  # Genera un número entero aleatorio entre 1 y 10
    lists,
    random.choice(lists2),
    random.choices(lists2, k=7),
    "".join(random.choices("abcde", k = 3)),

)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k = 16)  # Genera una cadena aleatoria de 16 caracteres (letras y dígitos)
print(seleccion) 

contrasena = "".join(seleccion)
print(contrasena)  # Imprime la contraseña generada aleatoriamente