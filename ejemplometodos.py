def saludo(nombre):
    print("\nBienvenido, " + nombre)

def despedida(nombre, dia):
    print("\nHa sido un placer hoy " + dia + ", " + nombre)

print("\n¿Cuál es tu nombre?")
name = input()
saludo(name)
print("\n¿Qué día de la semana es hoy?")
day = input()
despedida(name, day)