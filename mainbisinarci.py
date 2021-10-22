import metodosbisinarci
from datetime import date

opcion = -1


while opcion != 0:
    metodosbisinarci.menu()
    print("Selecciona una opción:")
    aux = input()
    if aux.isdigit() == True:
        opcion=int(aux)
        
    if opcion == 1:
        print("Escribe un año:")
        numero = input()
        if numero.isdigit():
            esbisiesto = metodosbisinarci.bisiesto(numero)
            if esbisiesto:
                print("\nEl año es bisiesto")
            else:
                print("\nEl año no es bisiesto")
        else:
            print("Valor incorrecto")
    elif opcion == 2:
        print("Escribe un número:")
        numero = input()
        if numero.isdigit():
            esnarcisista = metodosbisinarci.narcisista(numero)
            if esnarcisista:
                print("\nEl número es narcisista")
            else:
                print("\nEl número no es narcisista")
        else:
            print("Valor incorrecto")
    elif opcion == 3:
        today = date.today()
        year = today.year
        print("Introduce el año de tu nacimiento:")
        nacimiento = input()
        if nacimiento.isdigit():
            nacimiento = int(nacimiento)
            print("\nLista de años bisiestos:")
            metodosbisinarci.listaBisiestos(year, nacimiento)
    elif opcion == 0:
        print("\nHasta luego")
    else:
        print("Opción incorrecta")