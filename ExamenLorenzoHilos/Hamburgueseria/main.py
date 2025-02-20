from clases import Hamburgueseria

if __name__ == "__main__":
# Bucle que crea hilos, le asigna el valor i como nombre y los inicia
    for i in range(1,11):
        hilo = Hamburgueseria(i)
        hilo.start()
