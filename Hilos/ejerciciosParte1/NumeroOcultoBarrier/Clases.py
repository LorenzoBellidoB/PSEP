import random
from threading import Barrier, Thread

class NumeroOculto(Thread):

    numeroOculto = random.randint(1,10)
    def __init__(self):
        Thread.__init__(self)

class Jugador(Thread):

    def __init__(self, name,res, barrera:Barrier):
        
        Thread.__init__(self, name = name)
        self.res = res
        self.barrera = barrera

    def run(self):
        self.barrera.wait()
        while NumeroOculto.numeroOculto != self.res:
            print("El jugador", self.name, "no ha adivinado el número", self.res)
            self.res = random.randint(1,10)
        
        print("El jugador", self.name, "ha adivinado el número", self.res)
        self.barrera.abort()
            

