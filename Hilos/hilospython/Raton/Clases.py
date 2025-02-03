import random
from threading import Event, Thread
import time


class Raton(Thread):
    def __init__(self, name, event:Event):
        Thread.__init__(self, name = name)
        self.event = event

    def run(self):
        # El ratón espera a que el plato esté listo
        while not self.event.is_set():
            self.event.wait()
        
        self.event.clear()
        print("El ratón", self.name, "toma el control del plato")
        time.sleep(random.randint(1, 3))
        print("El ratón", self.name, "termina de comer")
        self.event.set()