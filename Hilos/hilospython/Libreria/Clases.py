import random
from threading import Condition, Thread
import time


class Libreria(Thread):
    libros=[False,False,False,False,False,False,False,False,False]
    cond=Condition()

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        # Se genera una posicion aleatoria
        libro1 = random.randint(0,8)
        libro2 = random.randint(0,8).

        # Mientras el hilo este siendo usado por otro hilo no lo puede usar el actual
        Libreria.cond.acquire()
        while Libreria.libros[libro1] & Libreria.libros[libro2]:
            print("El estudiante", self.name, "esta esperando a que se libere el libro", libro1)
            print("El estudiante", self.name, "esta esperando a que se libere el libro", libro2)
            Libreria.cond.wait()

        # Una vez que veo que esta libre lo reservo para mi
        Libreria.libros[libro1] = True
        Libreria.libros[libro2] = True
        # Aqui podemos liberar el bloque porque ya he modificado la lista
        Libreria.cond.release()

        print("Estudiante", self.name, "esta usando el libro", libro1)
        print("Estudiante", self.name, "esta usando el libro", libro2)
        time.sleep(random.randint(1, 5))
        print("Estudiante", self.name, "libera el libro", libro1)
        print("Estudiante", self.name, "libera el libro", libro2)

        # Antes de modificar la lista volvemos a bloquear
        Libreria.cond.acquire()
        Libreria.libros[libro1] = False
        Libreria.libros[libro2] = False
        Libreria.cond.notifyAll()

        # Una vez hemos notificado liberamos el bloqueo
        Libreria.cond.release()