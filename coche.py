class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    arrancado = False

    def __init__(self):
        self.velocidad = 0
        self.arrancado = False

    def getCoche(self):
        if self.arrancado:
            print("\n" + self.marca + " " + self.modelo + ", velocidad: " + 
            str(self.velocidad) + "kmh, estado: " + "arrancado")
        else:
            print("\n" + self.marca + " " + self.modelo + ", velocidad: " + 
            str(self.velocidad) + "kmh, estado: " + "detenido")
    def arrancar(self):
        self.arrancado = True
        print("\nSe ha arrancado el coche")

    def acelerar(self):
        if self.arrancado:
            self.velocidad += 20
            print("\nVelocidad aumenta a " + str(self.velocidad) + "kmh")
        else:
            print("\nNo puedes acelerar el coche si no está arrancado")
    def frenar(self):
        if self.velocidad == 0:
            print("\nEl coche no puede ir más lento")
        else:
            self.velocidad -= 20
            print("\nVelocidad disminuye a " + str(self.velocidad) + "kmh")
    
    def detener(self):
        self.velocidad = 0
        self.arrancado = False
        print("\nEl coche se ha detenido")
