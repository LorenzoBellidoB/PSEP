import random
from threading import Event, Thread
import time


class Empresa(Thread):

    TAQUILLA = Event()
    ENTRADA = Event()
    def __init__(self):
        Thread.__init__(self)
        
    
    def run(self):
        print(f"{self.pintarApertura()}Se abre la taquilla")
        self.TAQUILLA.set()
        self.ENTRADA.set()
        time.sleep(5)
        self.TAQUILLA.clear()
        self.ENTRADA.clear()
        print(f"{self.pintarApertura()}Se cierra la taquilla")
        
    def pintarApertura(self):
        aperturaOpc = random.randint(1,2)
        apertura = ""
        if aperturaOpc == 1:
            apertura = "🔓"
        else:
            apertura = "🔒"
        return apertura


class Comprador(Thread):
    def __init__(self, name):
        Thread.__init__(self, name = name)
    
    def run(self):
        compra = True
        while (not Empresa.ENTRADA.is_set() or not Empresa.TAQUILLA.is_set()) and compra:
            Empresa.ENTRADA.wait(timeout=3)
            print("Se va de la cola")
        if compra:
            print(f"{self.pintarApertura()}El comprador",self.name,"compra")
            time.sleep(1)
            print(f"{self.pintarApertura()}El comprador",self.name,"sale")
            if Empresa.TAQUILLA.is_set():
                Empresa.ENTRADA.set()
        else:
            print(f"{self.pintarApertura()}El comprador",self.name,"no ha comprado")

    def pintarApertura(self):
        aperturaOpc = random.randint(1,3)
        apertura = ""
        if aperturaOpc == 1:
            apertura = "🥸"
        elif aperturaOpc == 2:
            apertura = "🤑"
        elif aperturaOpc == 3:
            apertura = "🤩"
        return apertura

