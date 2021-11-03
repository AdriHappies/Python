import pyodbc
from departamento import Departamento

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

class ConexionDepartamentos:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
         + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

    def insertarDept(self, num, nom, loc):
        cursor = self.conexion.cursor()
        sqlinsert = "insert into dept values (?, ?, ?)"
        cursor.execute(sqlinsert, (num, nom, loc))
        cursor.commit()
        cursor.close()

    def eliminarDept(self, num):
        cursor = self.conexion.cursor()
        sqlinsert = "delete from dept where dept_no = ?"
        cursor.execute(sqlinsert, (num))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados

    def modificarDept(self, num, nom, loc):
        cursor = self.conexion.cursor()
        sqlupdate = "update dept set dnombre = ?, loc = ? where dept_no = ?"
        cursor.execute(sqlupdate, (nom, loc, num))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados

    def selectDept(self):
        cursor = self.conexion.cursor()
        sqlselect = "select dept_no, dnombre, loc from dept"
        cursor.execute(sqlselect)
        departamentos = []
        for row in cursor:
            dept = Departamento()
            dept.numero = row.dept_no
            dept.nombre = row.dnombre
            dept.localidad = row.loc
            departamentos.append(dept)
        cursor.close()
        return departamentos

    def buscarDepartamento(self, num):
        cursor = self.conexion.cursor()
        sqlselect = "select dept_no, dnombre, loc from dept where dept_no = ?"
        cursor.execute(sqlselect, (num))
        row = cursor.fetchone()
        if not row:
            cursor.close()
            return None
        else:
            departamento = Departamento()
            departamento.numero = row.dept_no
            departamento.nombre = row.dnombre
            departamento.localidad = row.loc
            cursor.close()
            return departamento