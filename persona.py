class Persona():
    nombre = ""
    apellido = ""
    fechaNacimiento = 0
    pais = ""

    #Constructor: se inician las variables o se le indican los elementos
    #cuando se construye un objeto
    def __init__(self):
        #Por ejemplo que cualquier persona sea de España al inicar
        self.pais = "Spain"

    def __str__(self):
        return (self.nombre + " " + self.apellido + " " + ", Pais: " 
            + self.pais + " " + ", Edad: " + str(self.getEdad()))  

    #Metodos
    #Mostrar nombre y apellidos
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellido

    def getEdad(self):
        return 2021 - self.fechaNacimiento

    def getDescripcion(self, midescripcion):
        return self.getNombreCompleto() + ", " + midescripcion