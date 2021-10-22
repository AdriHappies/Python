import metodosexternosmatematicas

seguir = True
cont = " "
mismosNumeros = True
while seguir:
    print("Introduzca número 1: ")
    numero1 = int(input())
    print("Introduzca número 2")
    numero2 = int(input())
    mismosNumeros = True
    while mismosNumeros:
        metodosexternosmatematicas.mostrarMenu()
        opcion = int(input())
        if (opcion == 1):
        #Llamamos a sumar
            resultado = metodosexternosmatematicas.sumar(numero1, numero2)
            print("La suma es " + str(resultado))
        elif (opcion == 2):
            #Llamamos a restar
            resultado = metodosexternosmatematicas.restar(numero1, numero2)
            print("La resta es " + str(resultado))
        elif (opcion == 3):
            #Llamamos a dividir
            resultado = metodosexternosmatematicas.dividir(numero1, numero2)
            print("La división es " + str(resultado))
        elif (opcion == 4):
            resultado = metodosexternosmatematicas.multiplicar(numero1, numero2)
            print("La multiplicación es " + str(resultado))
        elif (opcion == 0):
            metodosexternosmatematicas.salir()
            mismosNumeros = False
        else:
            print("Opción incorrecta") 
        if opcion != 0:
            metodosexternosmatematicas.continuar()
            cont = input()
            if cont == "s":
                print("\nReanudamos\n")
                mismosNumeros = False
            elif cont == "n":
                print("\nVuelve a elegir opción")
            else:
                print("Lo interpreto como 'n'")
                print("\nVuelve a elegir opción")
    if opcion == 0:
        seguir = False