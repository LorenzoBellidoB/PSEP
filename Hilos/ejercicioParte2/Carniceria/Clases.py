import random
from threading import Thread, Semaphore
import time

class Carniceria(Thread):
    semaforo = Semaphore(4)
    def __init__(self, name):
        Thread.__init__(self, name = name)
    
    def run(self):
        cliente = self.pintarCliente()
        color = self.pintar()
        Carniceria.semaforo.acquire()
        print(f"{cliente}{color} Cliente", self.name, "está siendo atendido. Carnicerias disponibles: " + str(Carniceria.semaforo._value) + self.pintarCarniceria())
        time.sleep(random.randint(1, 5))
        Carniceria.semaforo.release()
        print(f"{cliente}{color} Cliente", self.name, "ha terminado en la carnicería. Carnicerias disponibles: " + str(Carniceria.semaforo._value) + self.pintarCarniceria())

    def pintarCarniceria(self):
        espacios = self.semaforo._value
        Carniceria = " ❌ "
        if espacios > 0:
            Carniceria = ""
            for i in range(espacios):
                Carniceria += " 🛒 "
        return Carniceria
    
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