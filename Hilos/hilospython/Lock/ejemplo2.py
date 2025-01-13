import random
from threading import Lock, Thread


class BloqueaLista(Thread):
    lista = [False,False,False,False,False]
    bloqueo = Lock()

    def __init__(self,nombre):
        Thread.__init__(self, name = nombre)
    
    def run(self):
        print("Hilo", self.name, "ejecutandose")
        
        pos = random.randint(0,4)

        print('Hilo ', self.name, ' quiere tomar la posicion ', pos)

        BloqueaLista.bloqueo.acquire()
        if not BloqueaLista.lista[pos]:
            print('Hilo ', self.name, ' toma a la posicion ', pos)
            BloqueaLista.lista[pos] = True
        BloqueaLista.bloqueo.release()