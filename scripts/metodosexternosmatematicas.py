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