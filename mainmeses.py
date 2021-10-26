from mes import Mes
import random
meses = []

for i in range(12):
    month = Mes()
    month.nombre = "Mes " + str(i + 1)
    month.tempMax = random.randint(10, 40)
    month.tempMin = random.randint(-5, 9)
    meses.append(month)
    # meses.append(Mes())
    # meses[i].nombre = "Mes " + str(i + 1)
    # if i == 0:
    #     meses[i].nombre = "Enero"
    # elif i == 1:
    #     meses[i].nombre = "Febrero"
    # elif i == 2:
    #     meses[i].nombre = "Marzo"
    # elif i == 3:
    #     meses[i].nombre = "Abril"
    # elif i == 4:
    #     meses[i].nombre = "Mayo"
    # elif i == 5:
    #     meses[i].nombre = "Junio"
    # elif i == 6:
    #     meses[i].nombre = "Julio"
    # elif i == 7:
    #     meses[i].nombre = "Agosto"
    # elif i == 8:
    #     meses[i].nombre = "Septiembre"
    # elif i == 9:
    #     meses[i].nombre = "Octubre"
    # elif i == 10:
    #     meses[i].nombre = "Noviembre"
    # elif i == 11:
    #     meses[i].nombre = "Diciembre"

for j in range(len(meses)):
    print(meses[j])
    
