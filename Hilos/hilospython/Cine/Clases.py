import random
from threading import Thread, Semaphore
import time

from colorama import Fore

class Cine(Thread):
    semaforo = Semaphore(10)

    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        cara = self.pintarEspectador()
        Cine.semaforo.acquire()
        print(f"{Fore.GREEN}{cara} Espectador", self.name, "entrando al cine", str(Cine.semaforo._value) + " espacios disponibles", self.pintarAsiento())
        time.sleep(5)
        Cine.semaforo.release()
        print(f"{Fore.RED}{cara} Espectador", self.name, "saliendo del cine", str(Cine.semaforo._value) + " espacios disponibles", self.pintarAsiento())

    def pintarEspectador(self):
        persona = random.randint(1, 3)
        cara = ""
        if persona == 1:
            cara = "🦹"
        elif persona == 2:
            cara = "🧙"
        elif persona == 3:
            cara = "🦸"
        return cara
    
    def pintarAsiento(self):
        espacios = Cine.semaforo._value
        parking = " ❌ "
        if espacios > 0:
            parking = ""
            for i in range(espacios):
                parking += " 💺 "
        return parking