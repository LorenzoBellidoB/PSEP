from Clases import Peaton,Semaforo


if __name__ == '__main__':
    peatones = [Peaton(f"Peatón-{i}") for i in range(5)]
    semaforo = Semaforo()

    semaforo.start()
    for p in peatones:
        p.start()

    # Mantener el programa en ejecución
    semaforo.join()
    for p in peatones:
        p.join()