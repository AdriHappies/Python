def saludo(nombre):
    print("\nBienvenido, " + nombre)

def diasemana(nombre, dia):
    print("\nAsí que hoy es " + dia + ", gracias!")
    despedida(nombre)

def despedida(nombre):
    print("\nHasta luego " + nombre)

#main
print("\n¿Cuál es tu nombre?")
name = input()
saludo(name)
print("\n¿Qué día de la semana es hoy?")
day = input()
diasemana(name, day)