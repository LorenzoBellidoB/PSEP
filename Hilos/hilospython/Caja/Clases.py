import random
from threading import Barrier, Thread
import time


class Caja(Thread):
    def __init__(self, name,barrera:Barrier):
        Thread.__init__(self, name = name)
        self.barrera = barrera

    def run(self):
        restantes = self.barrera.wait()
        print("Hilo", self.name, "entra en caja")
        time.sleep(random.randint(1, 3))
        print("Hilo", self.name, "sale de caja")