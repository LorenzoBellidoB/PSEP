from time import sleep

from multiprocessing import Process

def suma(numeros):
    suma = 0
    for i in range (len(numeros)):
        suma += i
        print("Sumando hasta el", numeros[i],":", suma)
    sleep(2)
    return suma



if __name__ == "__main__":

    numeros = [1,10,5]
    p=Process(target=suma, args=(numeros,))
    p.start()
    p.join()
    print("Resultados:",p)