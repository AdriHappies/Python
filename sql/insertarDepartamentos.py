import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
         + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

conexion = pyodbc.connect(cadenaconexion)
#Ejemplo de insertar sin perdir datos
    # #creamos el cursor
    # cursor = conexion.cursor()
    # sql = "insert into dept values (66, 'PROGRAMACION', 'IBIZA')"
    # #ejecutamos la consulta
    # cursor.execute(sql)
    # #usamos rowcount para averiguar si hay contenido
    # print("Rowcount: " + str(cursor.rowcount))
    # #estas acciones son temporales, y no se realizan en la bbdd.
    # #debemos usar commit en cursor para que se llevan a cabo de forma permanente en la bbdd
    # cursor.commit()

#Codigo para pedir datos

print("Introduzca un número para el departamento")
numero = input()
print("Introduzaca el numbre del departamento")
nombre = input()
print("Introduzca la localidad")
loc = input()
sql = "insert into dept values (" + numero + ", '"+ nombre + "', '" + loc + "')"
cursor = conexion.cursor()
cursor.execute(sql)
cursor.commit()
#cerramos cursor 
cursor.close()
cursor = conexion.cursor()
sqlselect = "select dept_no, dnombre, loc from dept"
cursor.execute(sqlselect)
print("---------departamentos-------------")
for c in cursor:
    print(c.dnombre + ", " + c.loc)
cursor.close()

#cerramos conexion
conexion.close()