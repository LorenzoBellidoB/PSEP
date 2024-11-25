from multiprocessing import Lock, Value, Process

def incrementar(numero,valor,lock):
    for i in range(10):
        with lock:
            print(f"Proceso {numero} incrementa el valor {valor.value}")
            valor.value += 1

if __name__ == '__main__':
    contador = Value('i', 0)
    procesos = []
    lock = Lock()
    for i in range(4):
        procesos.append(Process(target=incrementar, args=(i,contador,lock,)))

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

    print("El valor final es:", contador.value)