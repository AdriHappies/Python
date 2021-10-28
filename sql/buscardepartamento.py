import pyodbc

print("Buscador de departamentos")

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" +
servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

conexion = pyodbc.connect(cadenaconexion)

#vamos a pedir el numero de departamento
print("Departamento a buscar")
numero = input()

sql = "select dept_no, dnombre, loc from dept where dept_no =" + numero
cursor = conexion.execute(sql)
row = cursor.fetchone()
if row == None:
    print("No existe el departamento")
else:
    print(row.dnombre + ", " + row.loc)

cursor.close()
conexion.close()