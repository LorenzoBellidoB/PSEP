import random
from threading import Thread, Condition
import time

class Peaton(Thread):
    semaforo_verde = False  # Variable compartida
    pasar_semaforo = Condition()  # Condición para esperar el semáforo

    def __init__(self, name):
        super().__init__(name=name)  # Iniciar hilo con nombre

    def run(self):
        while True:
            with Peaton.pasar_semaforo:
                while not Peaton.semaforo_verde:
                    print(f"🚶 Peatón {self.name} esperando en la acera...")
                    Peaton.pasar_semaforo.wait()  # Espera hasta que el semáforo esté en verde

                print(f"✅ Peatón {self.name} cruzando la calle...")
            
            time.sleep(random.uniform(1, 3))  # Simula el tiempo de cruce
            print(f"🏁 Peatón {self.name} ha cruzado.")

class Semaforo(Thread):
    def run(self):
        while True:
            with Peaton.pasar_semaforo:
                Peaton.semaforo_verde = False
                print("\n🚦 Semáforo en ROJO. Los peatones deben esperar...")

            time.sleep(5)

            with Peaton.pasar_semaforo:
                Peaton.semaforo_verde = True
                print("\n🚦 Semáforo en VERDE. ¡Pueden cruzar!")
                Peaton.pasar_semaforo.notify_all()  # Despierta a todos los peatones

            time.sleep(5)