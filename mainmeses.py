from mes import Mes
import random
meses = []
nombremeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
for i in range(12):
    month = Mes()
    # month.nombre = nombremeses[i]
    month.nombre = "Mes " + str(i + 1)
    month.tempMax = random.randint(10, 40)
    month.tempMin = random.randint(-5, 9)
    # meses[i].nombre = "Mes " + str(i + 1)
    # if i == 0:
    #     month.nombre = "Enero"
    # elif i == 1:
    #     month.nombre = "Febrero"
    # elif i == 2:
    #     month.nombre = "Marzo"
    # elif i == 3:
    #     month.nombre = "Abril"
    # elif i == 4:
    #     month.nombre = "Mayo"
    # elif i == 5:
    #     month.nombre = "Junio"
    # elif i == 6:
    #     month.nombre = "Julio"
    # elif i == 7:
    #     month.nombre = "Agosto"
    # elif i == 8:
    #     month.nombre = "Septiembre"
    # elif i == 9:
    #     month.nombre = "Octubre"
    # elif i == 10:
    #     month.nombre = "Noviembre"
    # elif i == 11:
    #     month.nombre = "Diciembre"
    meses.append(month)

for mes in meses:
    print(mes)
    
