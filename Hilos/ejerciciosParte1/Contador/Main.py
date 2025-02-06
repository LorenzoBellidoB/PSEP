import threading
from Clases import Contador, incrementar_contador


if __name__ == "__main__":
   contador = Contador()  # Crear una instancia de la clase Contador
   hilos = []  # Lista para guardar los hilos
   N = 10  # Número de hilos
   TOTAL = 1000  # Total a alcanzar


   # Crear y arrancar los hilos
   for _ in range(N):
       hilo = threading.Thread(target=incrementar_contador, args=(contador, TOTAL))
       hilos.append(hilo)
       hilo.start()


   # Esperar a que todos los hilos terminen
   for hilo in hilos:
       hilo.join()


   # Mostrar el valor final del contador
   print(f"Valor final del contador: {contador.obtener_valor()}")