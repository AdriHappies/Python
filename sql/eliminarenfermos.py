import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" 
    + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)

sqlselect = "select apellido, inscripcion from enfermo"
cursor = conexion.cursor()
cursor.execute(sqlselect)
for apellido, inscripcion in cursor:
    print(apellido + ", " + str(inscripcion))
cursor.close()
print("Introduzca el numero de inscripción del enfermo que desea eliminar:")
ins = int(input())
sqldelete = "delete from enfermo where inscripcion = ?"
cursor = conexion.cursor()
cursor.execute(sqldelete, (ins))
print("filas afectadas: " + str(cursor.rowcount))
cursor.close()



conexion.close()