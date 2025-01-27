import random
from Clases import Puente


if __name__ == '__main__':
    for i in range(1,11):
        hilo = Puente(i,random.randint(0,2))
        hilo.start()