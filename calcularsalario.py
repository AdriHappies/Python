print("Intruduzca número de horas trabajadas")
numHoras = int(input())
print("Introduzca el precio por hora")
precioHora = int(input())
print("introduzca el número de kilómetros")
km = int(input())
print("\n")

horasExtra = 0
salarioBase = 0
salarioExtra = 0
salarioTotal = 0
dieta = " "
retencion = " "

if numHoras > 36:
    horasExtra = numHoras - 36
    salarioBase = precioHora * 36
    salarioExtra = horasExtra * (precioHora + 2)
else:
    salarioBase = precioHora * numHoras

if km <= 100:
    dieta = "Dieta Local"
elif km > 100 and km <= 500:
    dieta = "Dieta Nacional"
else:
    dieta = "Dieta Internacional"

salarioTotal = salarioBase + salarioExtra

if salarioTotal <=250 :
    retencion = "No tiene retención"
elif salarioTotal > 250 and salarioTotal <= 800 :
    retencion = "Retención del 20%"
else:
    retencion = "Retención del 40%"

print("Numero de horas: " + str(numHoras))
print("Precio Hora: " + str(precioHora))
print("Kilómetros: " + str(km))
print("Horas Extra: " + str(horasExtra))
print("Salario Base: " + str(salarioBase))
print("Salario Extra: " + str(salarioExtra))
print("Salario Total: " + str(salarioTotal))
print(dieta)
print(retencion)
print("\n")
print("Fin de programa")