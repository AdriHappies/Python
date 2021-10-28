import pyodbc
print("Primera consulta SQL Server")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" +
servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)


print("Intentando conectar")
conexion = pyodbc.connect(cadenaconexion)
print("Conectado")

#Cursor se crea con una coneion abierta
cursor = conexion.cursor()
#necesitamos una consulta, el cursor maneja consultas select o de accion
#creamos una consulta select
sql = "select * from dept"
#el cursor ejecuta la consulta
cursor.execute(sql)
#podemos recuperar una fila
#row = cursor.fetchone()
#dibujamos la fila
#print(row)
#repetimos fetchone
#row = cursor.fetchone()
#print(row)
#cada vez que se ejecuta el metodo fetch el cursor se mueve una fila
#no podemos volver a la fila anterior, a no ser que hagamos el execute otra vez
for row in cursor:
    #print(row[0])
    print(row.LOC)



cursor.close()    
conexion.close()
print("----------------\nfin de programa\n-----------------")