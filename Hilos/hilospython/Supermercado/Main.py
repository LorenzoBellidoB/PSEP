

from Supermecado import Supermercado


if __name__ == '__main__':
    for i in range(1,11):
        hilo = Supermercado(i)
        hilo.start()