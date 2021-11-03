import pyodbc

from conexionhospital import ConexionHospital

# servidor = "LOCALHOST\SQLEXPRESS"
# bbdd = "HOSPITAL"
# usuario = "sa"
# password = "azure"

# conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" 
#     + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)

# sqlselect = "select apellido, inscripcion from enfermo"
# cursor = conexion.cursor()
# cursor.execute(sqlselect)
# for apellido, inscripcion in cursor:
#     print(apellido + ", " + str(inscripcion))
# cursor.close()
# print("Introduzca el numero de inscripción del enfermo que desea eliminar:")
# ins = int(input())
# sqldelete = "delete from enfermo where inscripcion = ?"
# cursor = conexion.cursor()
# cursor.execute(sqldelete, (ins))
# print("filas afectadas: " + str(cursor.rowcount))
#cursor.commit()
#cursor.close()

#aqui eliminamos con la clase conexion
connection = ConexionHospital()

connection.selectTabla()
print("Introduzca el numero de inscripción del enfermo que desea eliminar:")
ins = int(input())
respuesta = connection.eliminarEnfermo(ins)
print("Registros eliminados " + str(respuesta))

#cambiamos el apellido de un enfermo por su inscripción
#pedimos apellido e inscripción
print("Escriba el numero de inscripción del enfermo a modificar")
ins = int(input())
print("Escriba el nuevo apellido del enfermo")
ape = input()

respuesta = connection.modificarEnfermo(ape, ins)
print("Registros modificados: " + str(respuesta))

connection.conexion.close()