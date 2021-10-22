import metodosbisinarci

opcion = -1


while opcion != 0:
    metodosbisinarci.menu()
    print("Selecciona una opción:")
    opcion = int(input())
    if opcion == 1:
        print("Escribe un año:")
        numero = input()
        esbisiesto = metodosbisinarci.bisiesto(numero)
        if esbisiesto:
            print("\nEl año es bisiesto")
        else:
            print("\nEl año no es bisiesto")
    if opcion == 2:
        print("Escribe un número:")
        numero = input()
        esnarcisista = metodosbisinarci.narcisista(numero)
        if esnarcisista:
            print("\nEl número es narcisista")
        else:
            print("\nEl número no es narcisista")
    if opcion == 3:
        print("\nEscribe el año en el que nos encontramos:")
        year = int(input())
        print("\nLista de años bisiestos:")
        for i in range(1, year + 1):
            esbisiesto = metodosbisinarci.bisiesto(i)
            if esbisiesto:
                print(i)
    if opcion == 0:
        print("\nHasta luego")