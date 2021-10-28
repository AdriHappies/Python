from coche import Coche

class Deportivo(Coche):
    def turbo(self):
        self.velocidad += 80
        print("Activando turbo!!!")
    def acelerar(self):
        if self.arrancado:
            self.velocidad += 30
            print("\nVelocidad aumenta a " + str(self.velocidad) + "kmh")
            self.turbo()
        else:
            print("\nNo puedes acelerar el deportivo si no está arrancado")