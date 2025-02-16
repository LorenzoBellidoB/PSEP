from threading import Barrier
from Clases import Repartidor

# Ejecutar el programa
if __name__ == "__main__":
    NUM_REPARTIDORES = 5
    barrera = Barrier(NUM_REPARTIDORES)
    hilos = [Repartidor(i, barrera) for i in range(NUM_REPARTIDORES)]

        # Iniciar todos los hilos
    for hilo in hilos:
        hilo.start()

        # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("✅ Todos los repartidores han salido a entregar paquetes.")