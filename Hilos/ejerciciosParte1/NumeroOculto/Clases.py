import random
from threading import Thread

class NumeroOculto(Thread):

    numeroOculto = random.randint(1,10)
    def __init__(self):
        Thread.__init__(self)

class Jugador(Thread):

    def __init__(self, name,res):
        
        Thread.__init__(self)
        self.name = name
        self.res = res

    def run(self):
        while NumeroOculto.numeroOculto != self.res:
            print("El jugador", self.name, "no ha adivinado el número", self.res)
            self.res = random.randint(1,10)
        
        print("El jugador", self.name, "ha adivinado el número", self.res)
        
            

