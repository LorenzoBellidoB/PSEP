import queue
from random import randint
import threading
import time

def clientes(cola, clientes):
    for c in clientes:
        print(f"El cliente {c} ha entrado a la cola")
        cola.put(c)

def cajas(cola, caja):
    while True:
        cliente = cola.get(timeout=5)
        time.sleep(randint(1, 5))
        print(f"La caja {caja} ha atendido al cliente {cliente}")

if __name__ == "__main__":
    tiempo = time.time()
    lista_clientes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cola = queue.Queue()
    
    t1 = threading.Thread(target=clientes, args=(cola, lista_clientes))
    t1.start()
    
    cajas_threads = []
    for i in range(5):
        t = threading.Thread(target=cajas, args=(cola, i))
        cajas_threads.append(t)
        t.start()
    
    t1.join()
    cola.join()  # Esperar a que todos los clientes sean atendidos
    
    for t in cajas_threads:
        cola.put(None)  # Señal para terminar los hilos de las cajas
    
    for t in cajas_threads:
        t.join()
    
    tiempo = time.time() - tiempo
    print("Todos los clientes han sido atendidos")
    print(f"Finalizado en {tiempo:.2f} segundos")
