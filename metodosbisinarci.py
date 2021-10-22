def menu():
    print("\n-----Menu-----")
    print("\n0.- Salir")
    print("1.- Calcular año Bisiesto")
    print("2.- Calcular número Narcisista")
    print("3.- Lista de años bisiestos desde tu nacimiento hasta hoy")

def bisiesto(numero):
    esBisiesto = False
    num = int(numero)
    if num % 4 == 0:
        if (num % 100 != 0) and (num % 400 != 0):
            esBisiesto = True
        elif (num % 100 == 0) and (num % 400 == 0):
            esBisiesto = True
    return esBisiesto

def listaBisiestos(year, nacimiento):
    for i in range(nacimiento, year + 1):
        esbisiesto = bisiesto(i)
        if esbisiesto:
            print(i)

def narcisista(num):
    esNarcisista = False
    suma = 0
    for i in range(len(num)):
        numero = int(num[i])
        suma = suma + elevar(numero, len(num))
    if suma == int(num):
        esNarcisista = True
    return esNarcisista



def elevar(num, i):
    numero = 1
    for j in range(i):
        numero *= num
    return numero
    
