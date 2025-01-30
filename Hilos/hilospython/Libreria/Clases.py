import random
from threading import Condition, Thread
import time

from colorama import Fore


class Libreria(Thread):
    libros=[False,False,False,False,False,False,False,False,False]
    cond=Condition()

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        # Se genera una posicion aleatoria
        libro1 = random.randint(0,8)
        libro2 = random.randint(0,8)

        librop1 = self.pintarLibro()
        librop2 = self.pintarLibro()

        estudiante = self.pintarEstudiante()

        while libro1 == libro2:
            libro2 = random.randint(0,8)

        # Mientras el hilo este siendo usado por otro hilo no lo puede usar el actual
        Libreria.cond.acquire()
        while Libreria.libros[libro1] or Libreria.libros[libro2]:
            print(Fore.LIGHTRED_EX,estudiante, "El estudiante", self.name, "esta esperando a que se libere el libro", libro1, librop1)
            print(Fore.LIGHTRED_EX,estudiante, "El estudiante", self.name, "esta esperando a que se libere el libro", libro2, librop2)
            Libreria.cond.wait()

        # Una vez que veo que esta libre lo reservo para mi
        Libreria.libros[libro1] = True
        Libreria.libros[libro2] = True
        # Aqui podemos liberar el bloque porque ya he modificado la lista
        Libreria.cond.release()
        print(Fore.BLUE,estudiante, "Estudiante", self.name, "esta usando el libro", libro1, librop1)
        print(Fore.BLUE,estudiante, "Estudiante", self.name, "esta usando el libro", libro2, librop2)
        time.sleep(random.randint(1, 10))
        print(Fore.GREEN,estudiante, "Estudiante", self.name, "libera el libro", libro1, librop1)
        print(Fore.GREEN,estudiante, "Estudiante", self.name, "libera el libro", libro2, librop2)

        # Antes de modificar la lista volvemos a bloquear
        Libreria.cond.acquire()
        Libreria.libros[libro1] = False
        Libreria.libros[libro2] = False
        Libreria.cond.notifyAll()

        # Una vez hemos notificado liberamos el bloqueo
        Libreria.cond.release()
    
    def pintarLibro(self):
        libro = random.randint(1, 4)
        libroT = ""
        if libro == 1:
            libroT = "📕"
        elif libro == 2:
            libroT = "📗"
        elif libro == 3:
            libroT = "📘"
        elif libro == 4:
            libroT ="📙"
        return libroT
    
    def pintarEstudiante(self):
        estudiante = random.randint(1, 3)
        estudianteT = ""
        if estudiante == 1:
            estudianteT = "🤩"
        elif estudiante == 2:
            estudianteT = "🤑"
        elif estudiante == 3:
            estudianteT = "🥸"
        return estudianteT