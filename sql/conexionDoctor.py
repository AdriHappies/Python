import pyodbc

from doctor import Doctor


servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "sa"
password = "azure"

class ConexionDoctor:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server}; SERVER=" + servidor
         + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
    
    # def insertarDoctor(self, hospcod, docnum, ape, espec, sal):
    #     cursor = self.conexion.cursor()
    #     sqlinsert = "insert into doctor values (?, ?, ?, ?, ?)"
    #     cursor.execute(sqlinsert, (hospcod, docnum, ape, espec, sal))
    #     cursor.commit()
    #     cursor.close()

    # def insertarDoctor(self, hospcod, ape, espec, sal):
    #     cursor = self.conexion.cursor()
    #     sqlinsert = ("insert into doctor values (?,"+ 
    #     "(select max(doctor_no)+1 from doctor), ?, ?, ?)")
    #     cursor.execute(sqlinsert, (hospcod, ape, espec, sal))
    #     cursor.commit()
    #     cursor.close()

    def insertarDoctor(self, ape, espec, sal):
        cursor = self.conexion.cursor()
        hospitales = self.mostrarHospital()
        print(hospitales)
        print("Elige un hospital")
        hos = input()
        hoscod = self.buscarCodigoHospital(hos)
        sqlinsert = ("insert into doctor values (?,"+ 
        "(select max(doctor_no)+1 from doctor), ?, ?, ?)")
        cursor.execute(sqlinsert, (hoscod, ape, espec, sal))
        cursor.commit()
        cursor.close()

    def eliminarDoctor(self, docnum):
        cursor = self.conexion.cursor()
        sqldelete = "delete from doctor where doctor_no = ?"
        cursor.execute(sqldelete, (docnum))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados

    def modificarSalarioDoctor(self, docnum, sal):
        cursor = self.conexion.cursor()
        sqlupdate = "update doctor set salario += ? where doctor_no = ?"
        cursor.execute(sqlupdate, (sal, docnum))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados

    def selectDoctor(self):
        cursor = self.conexion.cursor()
        sqlselect = "select hospital_cod, doctor_no, apellido, especialidad, salario from doctor"
        cursor.execute(sqlselect)
        doctores = []
        for row in cursor:
            doc = Doctor()
            doc.hoscod = row.hospital_cod
            doc.docnum = row.doctor_no
            doc.ape = row.apellido
            doc.espe = row.especialidad
            doc.sal = row.salario
            doctores.append(doc)
        cursor.close()
        return doctores

    def buscarDoctor(self, docnum):
        cursor = self.conexion.cursor()
        sqlselect = ("select hospital_cod, doctor_no, apellido, especialidad, salario from doctor where doctor_no = ?")
        cursor.execute(sqlselect, (docnum))
        row = cursor.fetchone()
        if not row:
            cursor.close()
            return None
        else:
            doc = Doctor()
            doc.hoscod = row.hospital_cod
            doc.docnum = row.doctor_no
            doc.ape = row.apellido
            doc.espe = row.especialidad
            doc.sal = row.salario
            cursor.close()
            return doc

    def mostrarHospital(self):
        cursor = self.conexion.cursor()
        sql = "select nombre from hospital"
        hospitales = []
        cursor.execute(sql)
        for row in cursor:
            hospitales.append(row)
        return hospitales

    def buscarCodigoHospital(self, hospital):
        cursor = self.conexion.cursor()
        sql = "select hospital_cod from hospital where nombre = ?"
        cursor.execute(sql, (hospital))
        row = cursor.fetchone()
        if not row:
            cursor.close()
            return None
        else:
            hoscod = row.hospital_cod
            cursor.close()
            return hoscod