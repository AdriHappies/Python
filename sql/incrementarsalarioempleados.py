import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" 
    + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)

print("Introduce el incremento en el salario que deseas realizar:")
incremento = input()
print("Introduce el oficio al que deseas aplicarselo:")
oficio = input()
#update dept set loc='GRANADA' where DNOMBRE='PRODUCCION'
sql = ("update EMP set SALARIO += " + incremento + " where OFICIO = '" + oficio + "'")
#print(sql)
cursor = conexion.cursor()
cursor.execute(sql)
cursor.commit()
print(str(cursor.rowcount) + " empleados con incremento")
cursor.close()
cursor = conexion.cursor()
sqlselect = "select apellido, oficio, salario from emp where oficio = '" + oficio + "'"
cursor.execute(sqlselect)
for c in cursor:
    print(c)
cursor.close
conexion.close()