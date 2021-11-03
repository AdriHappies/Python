from conexiondepartamentos import ConexionDepartamentos

conection = ConexionDepartamentos()

opcion = 0

while opcion != 6:
    print("\n-----Menu-----")
    print("\n1.- Insertar departamento")
    print("2.- Eliminar departamento")
    print("3.- Modificar departamento")
    print("4.- Buscar un departamento")
    print("5.- Mostrar departamentos")
    print("6.- Salir")
    print("\nElija una opción")
    opcion = int(input())
    print("\n")


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
        respuesta = conection.eliminarDept(num)
        print("\nRegistros eliminados: " + str(respuesta))
    if opcion == 3:
        print("\nEscriba el número de departamento")
        num = int(input())
        print("Escriba el nuevo nombre del departamento")
        nom = input()
        print("Escriba la nueva localidad del departamento")
        loc = input()
        respuesta = conection.modificarDept(num, nom, loc)
        print("\nRegistros modificados: " + str(respuesta))
    if opcion == 4:
        print("\nEscriba el número del departamento")
        num = int(input())
        departamento = conection.buscarDepartamento(num)
        if departamento == None:
            print("\nNo existe el departamento")
        else:
            print("\n"+departamento)
    if opcion == 5:
        departamentos = conection.selectDept()
        print("\n")
        for dept in departamentos:
            print(dept)
    if opcion == 6:
        #conection.conexion.close()
        print("\nHasta pronto")



