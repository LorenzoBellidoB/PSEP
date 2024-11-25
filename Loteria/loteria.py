from multiprocessing import Process, Pipe
import random

def bombo(pipe):
    lista = []
    while True:
        if pipe.recv() == 0:
            numero = random.randint(1, 100)
            while numero in lista:
                numero = random.randint(1, 100)
            lista.append(numero)
            print("El", numero)
            pipe.send(numero)
        elif pipe.recv() == 1:
            pipe.close()
            break

def jugador(pipe):
    creditos = 10
    apuesta = random.randint(1, 100)
    print("Apuesta:", apuesta)
    while creditos > 0:
        pipe.send(0)
        mensaje = pipe.recv()
        if apuesta == mensaje:
            print("Ganaste")
            pipe.send(1)
            break
        else:
            print("Perdiste")
        creditos -= 1
    pipe.close()

if __name__ == '__main__':
    pipe1, pipe2 = Pipe()
    p1 = Process(target=bombo, args=(pipe1,))
    p2 = Process(target=jugador, args=(pipe2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
