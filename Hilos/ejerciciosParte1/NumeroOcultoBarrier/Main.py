import random
from threading import Barrier
from Clases import NumeroOculto, Jugador

if __name__ == "__main__":
    
    numero = random.randint(1,10)
    barrera = Barrier(10)  # Ajustamos la barrera a 10 para coincidir con los jugadores

    hilos = []

    for i in range(10):
        print(f"Creando jugador {i+1} con número {numero}")  # Depuración
        hilo = Jugador(str(i+1), numero, barrera)
        hilo.start()
        hilos.append(hilo)

    for h in hilos:
        h.join()
