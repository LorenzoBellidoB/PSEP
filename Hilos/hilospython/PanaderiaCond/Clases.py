
import random
from threading import Condition, Thread
import time


class Panaderia(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.cesta = 7
        self.cond = Condition()

# Solo si ahy pan se compr
class Comprador(Thread):

    def __init__(self, num, panaderia):
        Thread.__init__(self)
        self.p = panaderia
        self.num = num

    def run(self):
        with(self.p.cond):
            while self.p.cesta == 0:
                self.p.cond.wait()
            print("Comprador", self.num, "esta comprando pan")
            time.sleep(random.uniform(0.1,0.5))
            self.p.cesta -= 1
            self.p.cond.notify_all()

# Solo si no hay pan reponen
class Reponedor(Thread):
    def __init__(self,Panaderia):
        Thread.__init__(self)
        self.p = Panaderia

    def run(self):
        with(self.p.cond):
            while self.p.cesta <= 0:
                print("Reponedor esta reponiendo pan")
                time.sleep(random.uniform(0.1,0.5))
                self.p.cesta = 7
                self.p.cond.notify_all()
    
