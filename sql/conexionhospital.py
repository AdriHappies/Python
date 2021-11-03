import pyodbc

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

class ConexionHospital:
    #creamos la conexion para que sirva para cualquier metodo
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" 
    + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)

    #metodo para ver una tabla entera
    def selectTabla(self):
        cursor = self.conexion.cursor()
        sqlselect = "select * from enfermo"
        cursor.execute(sqlselect)
        for c in cursor:
            print(c)
        cursor.close()

    #Realizamos un método para eliminar un enfermo
    def eliminarEnfermo(self, inscripcion):
        #entrar y salir
        cursor = self.conexion.cursor()
        sqldelete = "delete from enfermo where inscripcion = ?"
        cursor.execute(sqldelete, (inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados

    def modificarEnfermo(self, apellido, inscripcion):
        cursor = self.conexion.cursor()
        sqlupdate = "update enfermo set apellido = ? where inscripcion = ?"
        cursor.execute(sqlupdate, (apellido, inscripcion))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados