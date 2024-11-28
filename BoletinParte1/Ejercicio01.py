from time import sleep

from multiprocessing import 

def suma(numero):
    print("Entrando: ", numero)
    suma = 0
    for i in range (1,numero+1):
        suma += i
        print("Sumando hasta el", numero,":", suma)
    sleep(2)
    return suma



if __name__ == "__main__":

    