def mostrarMenu():
    print("\n0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    print("\nSeleccione una opción:")

def salir():
    print("\nHasta luego")

def sumar(num1, num2):
    suma = num1 + num2
    return suma

def restar(num1, num2):
    resta = num1 - num2
    return resta

def dividir(num1, num2):
    divi = num1 / num2
    return divi

def multiplicar(num1, num2):
    multi = num1 * num2
    return multi
    
def continuar():
    print("\n¿Desea probar con otros 2 números? (s/n)")

#MAIN
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
        mostrarMenu()
        opcion = int(input())
        if (opcion == 1):
        #Llamamos a sumar
            resultado = sumar(numero1, numero2)
            print("La suma es " + str(resultado))
        elif (opcion == 2):
            #Llamamos a restar
            resultado = restar(numero1, numero2)
            print("La resta es " + str(resultado))
        elif (opcion == 3):
            #Llamamos a dividir
            resultado = dividir(numero1, numero2)
            print("La división es " + str(resultado))
        elif (opcion == 4):
            resultado = multiplicar(numero1, numero2)
            print("La multiplicación es " + str(resultado))
        elif (opcion == 0):
            salir()
            mismosNumeros = False
        else:
            print("Opción incorrecta") 
        if opcion != 0:
            continuar()
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

    
