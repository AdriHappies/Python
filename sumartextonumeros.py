print("Escribe una cadena de numeros seguidos")
aux = input()
suma = 0
if aux.isdigit() == False:
    print("solo numeros porfavor")
else:
    for i in range(len(aux)):
        suma += int(aux[i])
        #print(suma)
    print("El resultado de la suma de todos los caracteres es: " + str(suma))
