import random
from threading import Thread, Semaphore
import time

class Parking(Thread):
    semaforo = Semaphore(5)
    def __init__(self, name):
        Thread.__init__(self, name = name)
    
    def run(self):
        coche = self.pintarCoche()
        color = self.pintar()
        Parking.semaforo.acquire()
        print(f"{coche}{color} Vehículo", self.name, "está entrando al estacionamiento. Espacios disponibles: " + str(Parking.semaforo._value) + self.pintarParking())
        time.sleep(random.randint(1, 10))
        Parking.semaforo.release()
        print(f"{coche}{color} Vehiculo", self.name, "salió del estacionamiento. Espacios disponibles: " + str(Parking.semaforo._value) + self.pintarParking())

    def pintarParking(self):
        espacios = Parking.semaforo._value
        parking = " ❌ "
        if espacios > 0:
            parking = ""
            for i in range(espacios):
                parking += " 🅿️ "
        return parking
    
    def pintarCoche(self):
        vehiculo = random.randint(1, 3)
        coche = ""
        if vehiculo == 1:
            coche = "🚗"
        elif vehiculo == 2:
            coche = "🚕"
        elif vehiculo == 3:
            coche = "🚙"
        return coche
    
    def pintar(self):
        color = ""
        num = random.randint(1, 5)
        if num == 1:
            color = "\033[92m"
        elif num == 2:
            color = "\033[93m"
        elif num == 3:
            color = "\033[91m"
        elif num == 4:
            color = "\033[0;34m"
        elif num == 5:
            color = "\033[1;32;40m"
        return color