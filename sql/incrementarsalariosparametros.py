import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" 
    + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)

print("Introduce el incremento en el salario que deseas realizar:")
incremento = int(input())
print("Introduce el oficio al que deseas aplicarselo:")
oficio = input()

sqlupdate = "update emp set salario += ? where oficio = ?"
sqlselect = "select apellido, oficio, salario from emp where oficio = ?"

#print(sql)
cursor = conexion.cursor()
cursor.execute(sqlupdate, (incremento, oficio))
cursor.commit()
print(str(cursor.rowcount) + " empleados con incremento")
cursor.close()
cursor = conexion.cursor()

cursor.execute(sqlselect, (oficio))
for c in cursor:
    print(c)
cursor.close
conexion.close()