from threading import Thread
from time import sleep
import time


def download_file(n:str,t:int):
    print(f"Inicio descarga de {n}")
    sleep(t)
    print(f"Descarga de {n} finalizada")


if __name__ == "__main__":
    tiempo = time.time()
    hilos = [
        Thread(target=download_file, args=("Archivo1",2)),
        Thread(target=download_file, args=("Archivo2",5)),
        Thread(target=download_file, args=("Archivo3",2)),
    ]

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    tiempo = time.time()-tiempo
    print(f"Finalizado en {tiempo}")