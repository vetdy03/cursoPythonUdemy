import math

def formulagral():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    c = int(input("Ingrese c: "))
    
    formPos = (-b + math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    formNeg = (-b - math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
    print("El resultado del valor positivo es: {} \nEl resultado del valor positivo es: {}".format(formPos, formNeg))
if __name__ == "__main__":
    formulagral()