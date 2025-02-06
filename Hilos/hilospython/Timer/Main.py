from threading import Timer
import time

def saludo():
    print("Hola")

if __name__ == "__main__":
    temporizador = Timer(5, saludo)
    temporizador.start()
    print("Esperando a que se ejecute la función.")