import random
from Clases import NumeroOculto,Jugador

if __name__ == "__main__":
    
    nombres = ["Marco","Raul","Hector","Pablo","Edu"]
    numero = random.randint(1,10)
    for n in nombres:
        Jugador(n,numero).start()