print("Introduce un numero de ISBN")
#comprobamos si es un número
numisbn = input()
suma = 0
if (numisbn.isdigit() == False):
    print("Solo debe escribir numeros")
elif (len(numisbn) != 10):
    print("Debe contener 10 numeros")
else:
    for i in range(len(numisbn)):
        aux = int(numisbn[i])
        aux = aux * (i + 1)
        suma += aux
    if (suma % 11) == 0:
        print("\nISBN correcto :)")
    else:
        print("\nISBN incorrecto")

print("\nFin de programa")