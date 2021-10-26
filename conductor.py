#main para la clase coche
def mostrarMenu():
    print("\n----Menu----")
    print("\n0.- Salir")
    print("1.- Arrancar")
    print("2.- Acelerar")
    print("3.- Frenar")
    print("4.- Detner")
    print("Elige una opción")


from coche import Coche

car = Coche()

car.marca = "Renault"
car.modelo = "Captur"

opcion = -1
print("\nBienvenido al coche")
car.getCoche()

while opcion != 0:
    mostrarMenu()
    opcion = int(input())
    if opcion == 1:
        car.arrancar()
        car.getCoche()
    elif opcion == 2:
        car.acelerar()
        car.getCoche()
    elif opcion == 3:
        car.frenar()
        car.getCoche()
    elif opcion == 4:
        car.detener()
        car.getCoche()
    elif opcion == 0:
        print("\nSaliendo del coche")
    