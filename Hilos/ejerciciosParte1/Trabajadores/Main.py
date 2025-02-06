from Clases import Trabajador


if __name__ == "__main__":
    
    nombres = ["Marco","Raul","Hector","Pablo","Edu"]

    for n in nombres:
        Trabajador(n).start()