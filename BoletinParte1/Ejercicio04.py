
from multiprocessing import Pipe, Process
from time import sleep


def leerFichero(p):
    archivo = open("BoletinParte1/numeros.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    
    for l in lineas:
        l = l.replace("\n","")
        p.send(l)
    p.send(None)
    return lineas

def sumar(p):
    while True:
        suma = 0
        num = p.recv()
        if num is None:
            break
        for i in range (1,int(num)+1):

            suma += i
            print("Sumando hasta el", num,":", suma)
            sleep(1)

if __name__ == '__main__':
    pipe1, pipe2 = Pipe()

    proceso1 = Process(target=leerFichero, args=(pipe1,))
    proceso2 = Process(target=sumar, args=(pipe2,))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()