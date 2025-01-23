from Clases import Cajero


if __name__ == '__main__':
    for i in range(1,11):
        hilo = Cajero(i)
        hilo.start()