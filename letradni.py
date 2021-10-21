from math import trunc
print("ejemplo calculo de letra de dni")
print("Introduce tu numero de DNI")
#comprobamos si es un número
aux = input()
if (aux.isdigit() == False):
    print("Solo debe escribir los numeros sin letra")
    print(len(aux))
else:
    if (len(aux) != 8):
        print("Debe contener 8 numeros")
    else:
        numDNI = int(aux)
    resultado = numDNI - (trunc(numDNI / 23) * 23)
    #print(resultado)
    tabladni = "TRWAGMYFPDXBNJZSQVHLCKET"
    letra = tabladni[resultado]
    print("\nLa letra de su dni es: " + letra)


print("\nFin de programa")
    