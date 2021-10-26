import random

class Mes:
    nombre = ""
    tempMax = 0
    tempMin = 0
    tempMed = 0

    def getMedia(self):
        return (self.tempMax + self.tempMin) / 2

    def __str__(self):
        return (self.nombre + " | temperatura maxima: " + str(self.tempMax)
         + " | temperatura minima: " + str(self.tempMin) 
         + " | temperatura media: " + str(self.getMedia()))