import random
from threading import Barrier
import time

from Clases import Caja


if __name__ == "__main__":
    barrera = Barrier(5)

    hilos = []

    for i in range(10):
        hilo = Caja(str(i), barrera)
        time.sleep(random.randint(1, 3))
        hilo.start()
        hilos.append(hilo)

    for h in hilos:
        h.join()