import pyodbc
print("Primera consulta SQL Server")
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"
cadenaconexion = ("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" +
servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

try:
    print("Intentando conectar")
    conexion = pyodbc.connect(cadenaconexion)
    print("Conectado")
except:
    print("Buff, esto no va bien")
finally:
    conexion.close()