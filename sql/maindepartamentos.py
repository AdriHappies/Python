from conexiondepartamentos import ConexionDepartamentos

conection = ConexionDepartamentos()

opcion = 0

while opcion != 4:
    print("\n-----Menu-----")
    print("\n1.- Insertar departamento")
    print("2.- Eliminar departamento")
    print("3.- Modificar departamento")
    print("4.- Salir")
    print("\nElija una opción")
    opcion = int(input())
    print("\n")
    conection.selectDept()

    if opcion == 1:
        print("\nEscriba el número de departamento")
        num = int(input())
        print("Escriba el nombre del departamento")
        nom = input()
        print("Escriba la localidad del departamento")
        loc = input()
        conection.insertarDept(num, nom, loc)
    if opcion == 2:
        print("\nEscriba el número de departamento")
        num = int(input())
        conection.eliminarDept(num)
    if opcion == 3:
        print("\nEscriba el número de departamento")
        num = int(input())
        print("Escriba el nuevo nombre del departamento")
        nom = input()
        print("Escriba la nueva localidad del departamento")
        loc = input()
        conection.insertarDept( nom, loc, num)
    if opcion == 4:
        conection.conexion.close()
        print("\nHasta pronto")



