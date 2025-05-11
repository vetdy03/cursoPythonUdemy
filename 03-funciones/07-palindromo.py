def es_palindromo():
    palabra = input("Ingrese palabra:")
    palabra = no_space(palabra)
    print(palabra)
    if palabra == (palabra[::-1]):
        print("Es palindromo")
    else:
        print("No es palidromo")
        
def no_space(pala):
    nuevo_text = ""
    for char in pala:
        if char != " ":
            nuevo_text += char
    
    return nuevo_text
            
    
if __name__ == "__main__":
    es_palindromo()
#pistas eliminar espacios y volvtear palabra
