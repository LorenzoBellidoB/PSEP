import random
from threading import Thread, Semaphore
import time

from colorama import Fore

class Puente(Thread):
    semaforoNorte = Semaphore(1)
    semaforoSur = Semaphore(1)
    def __init__(self, name,direccion):
        Thread.__init__(self, name = name)
        self.direccion = direccion

    def run(self):
        coche = self.pintarCoche()
        if self.direccion == 0:
            Puente.semaforoNorte.acquire()
            Puente.semaforoSur.acquire()
            print(Fore.LIGHTRED_EX + coche, self.name, "esta cruzando el puente direccion Norte")
            time.sleep(random.randint(1, 3))
            print(Fore.GREEN + coche, self.name, "ha cruzado el puente direccion Norte")
            Puente.semaforoNorte.release()
            Puente.semaforoSur.release()
        
        else:
            Puente.semaforoSur.acquire()
            Puente.semaforoNorte.acquire()
            print(Fore.LIGHTRED_EX + coche, self.name, "esta cruzando el puente direccion Sur")
            time.sleep(random.randint(1, 3))
            print(Fore.GREEN + coche, self.name, "ha cruzado el puente direccion Norte")
            Puente.semaforoSur.release()
            Puente.semaforoNorte.release()

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