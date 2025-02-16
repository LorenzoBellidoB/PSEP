import threading
import time
import random

class Repartidor(threading.Thread):
    def __init__(self, id, barrier):
        super().__init__()
        self.id = id
        self.barrier = barrier

    def run(self):
        print(f"Repartidor {self.id} está preparándose...")  
        tiempo_preparacion = random.randint(2, 6)  # Simula el tiempo de preparación
        time.sleep(tiempo_preparacion)  
        print(f"Repartidor {self.id} está listo después de {tiempo_preparacion} segundos.")

        # Esperar a que todos los repartidores estén listos
        self.barrier.wait()  
        print(f"🚀 Repartidor {self.id} ha salido a hacer entregas.")
