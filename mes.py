import random

class Mes:
    nombre = ""
    tempMax = 0
    tempMin = 0
    tempMed = 0

    def __init__(self):
        self.tempMax = random.randint(10, 40)
        self.tempMin = random.randint(-5, 9)
        self.tempMed = (self.tempMax + self.tempMin) / 2

    def mostrarMes(self):
        print(self.nombre + " | temperatura maxima: " + str(self.tempMax)
         + " | temperatura minima: " + str(self.tempMin) 
         + " | temperatura media: " + str(self.tempMed))