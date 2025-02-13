import random
from threading import Condition, Thread
import time


class Filosofo(Thread):
    tenedores = [False, False, False, False, False]
    cond = Condition()
    
    def __init__(self,id, name):
        Thread.__init__(self, name = name)
        self.id = id

    def run(self):
        print("El filósofo", self.id,self.name, "esta filosofando 🧠")
        time.sleep(random.randint(1, 5))

        Filosofo.cond.acquire()
        while Filosofo.tenedores[self.id]:
            print("El Filosofo", self.name, "está esperando a que se libere un tenedor", self.id,"❌")
            Filosofo.cond.wait()

        while Filosofo.tenedores[(self.id + 1)%5]:
            print("El Filosofo", self.name, "está esperando a que se libere un tenedor", (self.id + 1)%5,"❌")
            Filosofo.cond.wait()
        
        Filosofo.tenedores[self.id] = True
        Filosofo.tenedores[(self.id + 1)%5] = True

        Filosofo.cond.release()

        print("El Filosofo", self.name, "está usando el tenedor", self.id, "🍴")
        print("El Filosofo", self.name, "está usando el tenedor", (self.id + 1)%5,"🍴")
        time.sleep(random.randint(1,5))
        print("El Filosofo", self.name, "deja el tenedor", self.id,"🍴")
        print("El Filosofo", self.name, "deja el tenedor", (self.id + 1)%5,"🍴")

        Filosofo.cond.acquire()
        Filosofo.tenedores[self.id] = False
        Filosofo.tenedores[(self.id + 1)%5] = False
        Filosofo.cond.notify_all()
        print("El filosofo", self.name, "vuelve a pensar 🧠")

        Filosofo.cond.release()