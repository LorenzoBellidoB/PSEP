from multiprocessing import Pipe, Process


def leerFichero(p):
    archivo = open("BoletinParte1/numeros07.txt", "r")
    lineas = archivo.readlines()
    for l in lineas:
        p.send(l)
    p.send(None)
    archivo.close()
    return lineas

def sumarIntervalo(p):
    while True:
        suma = 0
        numeros = p.recv()
        numeros = numeros.split(" ")
        num1 = int(numeros[0])
        num2 = int(numeros[1])
        if p.recv() is None:
            break
        else:
            if num1 >= num2:
                for i in range(num2, num1 + 1):
                    suma += i
            else:
                for i in range(num1, num2 + 1):
                    suma += i
            print(f"La suma total es: {suma}")
    return suma

if __name__ == '__main__':
    pipe1,pipe2 = Pipe()
    proceso1 = Process(target=leerFichero, args=(pipe1,))
    proceso2 = Process(target=sumarIntervalo, args=(pipe2,))

    proceso1.start()    
    proceso2.start()

    proceso1.join()    
    proceso2.join()
    print("Todos los procesos han acabado.")