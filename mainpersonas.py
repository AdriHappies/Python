from persona import Persona

person = Persona()

person.nombre = "Alumno"
person.apellido = "Azure"
person.fechaNacimiento = 1984
midescripcion = "Excelente estudiante"
#print(person.getNombreCompleto())
#print("Edad " + str(person.getEdad()))
#print("Pais " + person.pais)
print(person)
print(person.getDescripcion(midescripcion))
