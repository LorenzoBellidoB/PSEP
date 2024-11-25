from multiprocessing import Process,Queue
import random
from time import sleep

def producer(q,id):
    for i in range(10):
        if q.full():
            print(f'p:{id} Cola llena')
            
        q.put(i)
        print(f'p:{id} He puesto',i)
        sleep(random.randint(1,5))
    q.put(None)
    print(f'p:{id} He terminado')

def consumer(q, id):
    while True:
        if q.empty():
            print(f'c:{id} Cola vacia')
        item = q.get()
        if item is None:
            break
                
        print(f'c:{id} He cogido',item)
        sleep(random.randint(1,5))
    print(f'c:{id} He terminado')
    

if __name__ == '__main__':

    productores = []
    consumidores = []

    queue = Queue(maxsize=3)
    for i in range(3):
        productores.append(Process(target=producer, args=(queue,i,)))
    for i in range(2):
        consumidores.append(Process(target=consumer, args=(queue,i,)))

    for p in productores:
        p.start()
    for c in consumidores:
        c.start()

    for p in productores:
        p.join()
        #print('Proceso 1 terminado')

    for c in consumidores:
        c.join()
        #print('Proceso 2 terminado')
    print('Todas las tareas han acabado')