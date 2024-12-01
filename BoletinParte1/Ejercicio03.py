
from multiprocessing import Process, Queue
from time import sleep


def leerFichero(q):
    archivo = open("BoletinParte1/numeros.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    for l in lineas:
        q.put(int(l))
    q.put(None)
    return lineas

def suma(q):
    while True:
        suma = 0
        num = q.get()
        if num is None:
            break
        else:
            for i in range (1,num+1):
                suma += i
                print("Sumando hasta el", num,":", suma)
                sleep(1)
    return suma

if __name__ == "__main__":

    queue = Queue()

    proceso1 = Process(target=leerFichero, args=(queue,))

    prcoeso2 = Process(target=suma, args=(queue,))

    proceso1.start()
    prcoeso2.start()

    proceso1.join()
    prcoeso2.join()


