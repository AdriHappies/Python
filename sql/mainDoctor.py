from conexionDoctor import ConexionDoctor

conection = ConexionDoctor()

opcion = 0

while opcion != 6:
    print("\n-----Menu-----")
    print("\n1.- Insertar doctor")
    print("2.- Modificar salario de doctor")
    print("3.- Eliminar doctor")
    print("4.- Buscar un doctor")
    print("5.- Mostrar doctores")
    print("6.- Salir")
    print("\nElija una opción")
    opcion = int(input())
    print("\n")


    if opcion == 1:
        # print("\nEscriba el código de hospital")
        # hoscod = int(input())
        # print("\nEscriba el número del doctor")
        # docnum = int(input())
        print("Escriba el apellido del doctor")
        ape = input()
        print("Escriba la especialidad del doctor")
        esp = input()
        print("\nEscriba el salario del doctor")
        sal = int(input())
        # conection.insertarDoctor(hoscod, docnum, ape, esp, sal)
        # conection.insertarDoctor(hoscod, ape, esp, sal)
        conection.insertarDoctor(ape, esp, sal)
    if opcion == 2:
        print("\nEscriba el número del doctor")
        docnum = int(input())
        print("Escriba el incemento de salario")
        sal = input()
        respuesta = conection.modificarSalarioDoctor(docnum, sal)
        print("\nRegistros modificados: " + str(respuesta))
    if opcion == 3:
        print("\nEscriba el número de doctor")
        docnum = int(input())
        respuesta = conection.eliminarDoctor(docnum)
        print("\nRegistros eliminados: " + str(respuesta))
    if opcion == 4:
        print("\nEscriba el número del doctor")
        docnum = int(input())
        doctor = conection.buscarDoctor(docnum)
        if doctor == None:
            print("\nNo existe el departamento")
        else:
            print(doctor)
    if opcion == 5:
        doctores = conection.selectDoctor()
        print("\n")
        for doc in doctores:
            print(doc)
    if opcion == 6:
        #conection.conexion.close()
        print("\nHasta pronto")