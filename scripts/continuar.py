
con = True
num = 0
opcion = " "

while con == True:
    print("\nIntroduce un número (positivo, negativo o 0):")
    num = int(input())
    if num < 0:
        print("\nEl número " + str(num) + "es negativo")
    elif num > 0:
        print("\nEl número " + str(num) + "es positivo")
    else:
        print("\nEl número " + str(num) + "es cero")
    print("\n¿Desea continuar? (s/n)")
    opcion = input()
    if opcion == "s":
        con = True
    elif opcion == "n":
        con = False
    else:
        print("\nError 404, letra not found")
        break