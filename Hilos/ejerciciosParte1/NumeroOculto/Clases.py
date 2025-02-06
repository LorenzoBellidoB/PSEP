import random
from threading import Thread,Condition


class NumeroOculto(Thread):

    numero = random.randint(0, 100)
    cond = Condition()
    def __init__(self, name, res):
        Thread.__init__(self, name = name, res = res)

    def run(self):
        NumeroOculto.cond.acquire()

        while numero != self.res:
            print("El hilo", self.name, "no a adivinado el numero")
            NumeroOculto.cond.wait()
