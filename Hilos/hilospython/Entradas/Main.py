from threading import Event
from Clases import Empresa,Comprador

if __name__ == '__main__':
    NUM_COMP = 50
    lista=[]
    e = Empresa()
    for i in range(NUM_COMP):
        lista.append(Comprador(i+1))

    e.start()
    for c in lista:
        c.start()

    for c in lista:
        c.join()