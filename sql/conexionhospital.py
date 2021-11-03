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
    def selectTabla(self, tabla):
        cursor = self.conexion.cursor()
        sqlselect = "select * from ?"
        cursor.execute(sqlselect, (tabla))
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