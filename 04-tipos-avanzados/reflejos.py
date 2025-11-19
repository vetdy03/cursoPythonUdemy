def reflejos():
    reflejos = [1,1,1,1,1,1]#2,5,2,3,5,6,8,6,3,2,4,8,7,8,9,0] #
    reflejos_2 = [2,3,2,5,4,5,3,5]
    contador = 0
    i = reflejos[1]
    j = reflejos_2[1]
    tam = len(reflejos)-2
    print("Reflejos: {} y tam es:{}".format(j, tam))
    for i in range(len(reflejos)-2):
        if reflejos[i-1] == reflejos[i+1] :# si el valor anterior es igual al siguiente
            contador += 1
            #print("Valor repetido: {}".format(reflejos[i]))
    print("Cantidad de reflejos repetidos: {}".format(contador))
    print(len(reflejos))

if __name__ == "__main__":
    reflejos()