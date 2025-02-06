import random
from threading import Thread
import time


class Trabajador(Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        while True:
            print("Soy el trabajador", self.nombre, "y estoy trabajando")
            time.sleep(random.randint(1, 10))
            print("Soy ", self.nombre, "y he terminado de trabajar")