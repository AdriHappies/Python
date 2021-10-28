nombres = []

def rellenarNombres():
    name = ""
    nombres.clear()
    print("\nEscribe un nombre")
    name = input()
    while name != "ok":        
        if name != "ok":
            nombres.append(name)
        mostrarNombres()
        print("Escriba otro nombre, o introduzca ok para terminar")
        name = input()
        
def mostrarNombres():
    for i in range(len(nombres)):
        name = nombres[i]
        print(str(i) + ".- " + name)       

def mostrarMenu():
    print("\n-----Menú-----")
    print("\n0.- Salir")
    print("1.- Nuevo nombre")
    print("2.- Eliminar nombre (posición)")
    print("3.- Comenzar de nuevo")
    print("Elija una opción:")

def nuevoNombre():
    mostrarNombres()
    print("\nEscriba el nombre que quiere añadir")
    name = input()
    nombres.append(name)

def borrarNombre():
    mostrarNombres()
    print("Escriba la posición en la que se encuentra el nombre que desea borrar")
    pos = int(input())
    nombres.pop(pos)

#main
print("A continuación se le pedirá que escriba una lista de nombres")
rellenarNombres()
opcion = -1
while opcion != 0:
    mostrarMenu()        
    opcion = int(input())
    if opcion == 1:
        nuevoNombre()
        mostrarNombres()
    elif opcion == 2:
        borrarNombre()
        mostrarNombres()
    elif opcion == 3:
        rellenarNombres()
    elif opcion == 0:
        print("\nHasta la próxima")
