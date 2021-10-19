import math
print("A continuación escribe tu fecha de nacimiento")

print("Escribe el día que naciste")
dia = int(input())
print("Escribe el mes que naciste")
mes = int(input())
print("Escribe el año que naciste")
year = int(input())

if mes == 1 or mes == 2:
    mes += 12
    year -= 1

op1 = math.trunc(((mes + 1) * 3) / 5)
op2 = math.trunc(year / 4)
op3 = math.trunc(year / 100)
op4 = math.trunc(year / 400)
op5 = math.trunc(dia + (mes * 2) + year + op1 + op2 - op3 + op4 + 2)
op6 = math.trunc(op5 / 7)
resultado = op5 - (op6 * 7)

if resultado == 0:
    print("Naciste un sábado")
elif resultado == 1:
    print("Naciste un domingo")
elif resultado == 2:
    print("Naciste un lunes")
elif resultado == 3:
    print("Naciste un martes")
elif resultado == 4:
    print("Naciste un miércoles")
elif resultado == 5:
    print("Naciste un jueves")
elif resultado == 6:
    print("Naciste un viernes")
else:
    print("Error de computación")
    