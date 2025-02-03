from threading import Event
from Clases import Raton

if __name__ == '__main__':
    plato = Event()
    plato.set()

    ratones = [Raton(f"Ratón {i}", plato) for i in range(1, 7)]

    for r in ratones:
        r.start()
    
    for r in ratones:
        r.join()
    