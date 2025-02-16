# Importamos las librerías necesarias
import threading  # Para manejar hilos (jugadores y croupier)
import queue      # Para crear una cola de jugadores esperando
import random     # Para generar números aleatorios (ruleta y apuestas)
import time       # Para pausas y simular el tiempo

# Clase que representa la Ruleta
class Ruleta:
    def __init__(self):
        self.cola_jugadores = queue.Queue()  # Cola donde los jugadores esperan
        self.resultado = None                # Aquí se guarda el resultado de la ruleta
        self.evento = threading.Event()     # Evento para sincronizar jugadores y croupier

    # Método para girar la ruleta
    def girar(self):
        print("🎰 Croupier: Girando la ruleta...")
        self.resultado = random.randint(0, 36)  # Genera un número aleatorio entre 0 y 36
        print(f"🎰 Croupier: ¡El resultado es {self.resultado}!")  # Muestra el resultado
        self.evento.set()  # Notifica a los jugadores que el resultado está listo

    # Método para que los jugadores obtengan el resultado
    def obtener_resultado(self):
        self.evento.wait()   # Los jugadores esperan aquí hasta que la ruleta termine
        self.evento.clear()  # Reinicia el evento para la siguiente ronda
        return self.resultado  # Devuelve el número que salió en la ruleta

# Clase que representa a un Jugador
class Jugador(threading.Thread):
    def __init__(self, nombre, ruleta):
        super().__init__()  # Inicializa el hilo
        self.nombre = nombre  # Nombre del jugador
        self.ruleta = ruleta  # Referencia a la ruleta
        self.dinero = 100     # Dinero inicial del jugador
        self.jugando = True   # Estado del jugador (si sigue jugando o no)

    # Método que se ejecuta cuando el hilo del jugador comienza
    def run(self):
        while self.jugando:  # Mientras el jugador siga jugando
            print(f"🎲 {self.nombre}: Esperando para apostar...")
            self.ruleta.cola_jugadores.put(self)  # El jugador se une a la cola de espera
            self.ruleta.evento.wait()  # Espera a que la ruleta gire

            if not self.jugando:  # Si el jugador decidió retirarse, sale del bucle
                break

            print(f"🎲 {self.nombre}: ¡Haciendo apuesta!")
            apuesta = random.randint(1, 10)  # Apuesta un monto aleatorio entre 1 y 10
            numero = random.randint(0, 36)   # Elige un número aleatorio entre 0 y 36
            print(f"🎲 {self.nombre}: Apuesto {apuesta}💰 al número {numero}")

            resultado = self.ruleta.obtener_resultado()  # Obtiene el resultado de la ruleta
            if resultado == numero:  # Si acertó el número
                self.dinero += apuesta * 36  # Gana 36 veces su apuesta
                print(f"🎲 {self.nombre}: ¡Gané! 💸 Ahora tengo {self.dinero}💰")
            else:  # Si no acertó
                self.dinero -= apuesta  # Pierde lo que apostó
                print(f"🎲 {self.nombre}: Perdí. 😢 Ahora tengo {self.dinero}💰")

            if self.dinero <= 0:  # Si se queda sin dinero
                print(f"🎲 {self.nombre}: Me quedé sin dinero. 🏃‍♂️ Me retiro.")
                self.jugando = False  # Deja de jugar
            elif random.random() < 0.2:  # 20% de probabilidad de retirarse
                print(f"🎲 {self.nombre}: ¡Me aburro! 🏃‍♂️ Me retiro.")
                self.jugando = False  # Deja de jugar

# Clase que representa al Croupier
class Croupier(threading.Thread):
    def __init__(self, ruleta):
        super().__init__()  # Inicializa el hilo
        self.ruleta = ruleta  # Referencia a la ruleta

    # Método que se ejecuta cuando el hilo del croupier comienza
    def run(self):
        while True:  # El croupier siempre está activo
            jugadores = []
            while len(jugadores) < 3:  # Espera a que haya al menos 3 jugadores
                jugador = self.ruleta.cola_jugadores.get()  # Obtiene un jugador de la cola
                jugadores.append(jugador)  # Agrega al jugador a la lista
                print(f"🎰 Croupier: {jugador.nombre} está listo para apostar.")

            print("🎰 Croupier: ¡3 jugadores listos! Girando la ruleta...")
            self.ruleta.girar()  # Gira la ruleta

            for jugador in jugadores:
                self.ruleta.cola_jugadores.task_done()  # Marca al jugador como atendido

            time.sleep(1)  # Pequeña pausa entre rondas

# Función principal del programa
def main():
    ruleta = Ruleta()  # Crea una ruleta
    croupier = Croupier(ruleta)  # Crea un croupier
    croupier.start()  # Inicia el hilo del croupier

    # Crea 6 jugadores
    jugadores = [Jugador(f"Jugador {i}", ruleta) for i in range(6)]
    for jugador in jugadores:
        jugador.start()  # Inicia el hilo de cada jugador

    for jugador in jugadores:
        jugador.join()  # Espera a que todos los jugadores terminen

    croupier.join()  # Espera a que el croupier termine (en este caso, nunca termina)

# Punto de entrada del programa
if __name__ == "__main__":
    main()