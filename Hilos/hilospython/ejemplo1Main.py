from ejemplo1 import MiThreading


if __name__ == "__main__":
    print("Soy el principal")

    for i in range(10):
        hilo = MiThreading(i)
        hilo.start()