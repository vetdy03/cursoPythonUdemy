def es_palindromo():
    palabra = input("Ingrese palabra:")
    palabra = no_space(palabra)
    print(palabra)
    palabraNueva = palabraAlReves(palabra)
    
    print(palabra) 

    if palabra == palabraNueva:#(palabra[::-1]):
        print("Es palindromo")
    else:
        print("No es palidromo")

#def texto_al_rebves():
def palabraAlReves(palReves):
    nueva_palarbra =""
    for char in palReves:
        nueva_palarbra = char + nueva_palarbra
    return nueva_palarbra
             
def no_space(palabra):
    nuevo_text = ""
    for chars in palabra:
        if chars != " ":
            nuevo_text += chars
    
    return nuevo_text.lower()
            
    
if __name__ == "__main__":
    es_palindromo()
#pistas eliminar espacios y volvtear palabra
