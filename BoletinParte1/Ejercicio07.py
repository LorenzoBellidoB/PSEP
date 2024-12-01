from multiprocessing import Process, Queue


def leerFichero(q):
    archivo = open("BoletinParte1/numeros07.txt", "r")
    lineas = archivo.readlines()
    for l in lineas:
        q.put(l)
    q.put(None)
    archivo.close()
    return lineas

def sumarIntervalo(q):
    while True:
        numeros = q.get()
        if numeros is None:
            break
        else:
            numeros = numeros.split(" ")
            num1 = int(numeros[0])
            num2 = int(numeros[1])
            suma = 0
            if num1 >= num2:
                for i in range(num2, num1 + 1):
                    suma += i
            else:
                for i in range(num1, num2 + 1):
                    suma += i
        print(f"La suma total es: {suma}")
    return suma


if __name__ == "__main__":
    q = Queue()
    proceso1 = Process(target=leerFichero, args=(q,))
    proceso2 = Process(target=sumarIntervalo, args=(q,))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()