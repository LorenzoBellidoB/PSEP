from Hilos.hilospython.Lock.ejemplo2 import BloqueaLista

if __name__ == '__main__':
    for i in range(1,6):
        hilo = BloqueaLista(i)
        hilo.start()