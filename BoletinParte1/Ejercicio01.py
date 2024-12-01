from time import sleep

from multiprocessing import Process

def suma(numero):
    print("Entrando: ", numero)
    suma = 0
    for i in range (1,numero+1):
        suma += i
        print("Sumando hasta el", numero,":", suma)
        sleep(1)
    return suma



if __name__ == "__main__":

    proceso1 = Process(target=suma, args=(5,))
    proceso2 = Process(target=suma, args=(3,))
    proceso3 = Process(target=suma, args=(10,))
    proceso1.start()
    proceso2.start()
    proceso3.start()
    proceso1.join()
    proceso2.join()
    proceso3.join()