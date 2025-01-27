import random
from threading import Condition, Thread
import time


class Lista(Thread):
    lista=[False,False,False,False,False]
    cond=Condition()

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        # Se genera una posicion aleatoria
        num = random.randint(0,4)

        # Mientras el hilo este siendo usado por otro hilo no lo puede usar el actual
        Lista.cond.acquire()
        while Lista.lista[num]:
            print("El hilo", self.name, "esta esperando a que se libere la posición", num)
            Lista.cond.wait()

        # Una vez que veo que esta libre lo reservo para mi
        Lista.lista[num] = True
        # Aqui podemos liberar el bloque porque ya he modificado la lista
        Lista.cond.release()

        print("El hilo", self.name, "esta usando el objeto", num)
        time.sleep(random.randint(1, 5))
        print("El hilo", self.name, "libera el objeto", num)

        # Antes de modificar la lista volvemos a bloquear
        Lista.cond.acquire()
        Lista.lista[num] = False
        Lista.cond.notifyAll()

        # Una vez hemos notificado liberamos el bloqueo
        Lista.cond.release()