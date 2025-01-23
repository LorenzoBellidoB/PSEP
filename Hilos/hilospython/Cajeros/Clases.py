import random
from threading import Thread, Semaphore
import time

class Cajero(Thread):
    semaforo = Semaphore(3)
    def __init__(self, name):
        Thread.__init__(self, name = name)
    
    def run(self):
        cliente = self.pintarCliente()
        color = self.pintar()
        Cajero.semaforo.acquire()
        print(f"{cliente}{color} Cliente", self.name, "está entrando al super. Cajeros disponibles: " + str(Cajero.semaforo._value) + self.pintarCajero())
        time.sleep(random.randint(1, 5))
        Cajero.semaforo.release()
        print(f"{cliente}{color} Cliente", self.name, "salió del super. Cajeros disponibles: " + str(Cajero.semaforo._value) + self.pintarCajero())

    def pintarCajero(self):
        espacios = self.semaforo._value
        Cajero = " ❌ "
        if espacios > 0:
            Cajero = ""
            for i in range(espacios):
                Cajero += " 🛒 "
        return Cajero
    
    def pintarCliente(self):
        vehiculo = random.randint(1, 3)
        cliente = ""
        if vehiculo == 1:
            cliente = "🦸"
        elif vehiculo == 2:
            cliente = "🧙"
        elif vehiculo == 3:
            cliente = "🦹"
        return cliente
    
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