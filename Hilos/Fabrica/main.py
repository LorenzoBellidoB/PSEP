from clases import Operario
if __name__ == "__main__":
    for i in range(10):
        operario = Operario(f"Operario {i+1}")
        operario.start()