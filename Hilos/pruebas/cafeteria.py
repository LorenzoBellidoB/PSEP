import threading
import time


def cafe():
    for i in range(3): 
        print(f"Sirviendo café {i + 1}")
        time.sleep(1)  
    print("Terminó los cafés")

def tostadas():
    for i in range(3):  
        print(f"Poniendo tostada {i + 1}")
        time.sleep(1.5) 
    print("Terminó las tostadas")

def tortilla():
    for i in range(3):  
        print(f"Haciendo tortilla {i + 1}")
        time.sleep(2)  
    print("Terminó las tortillas")

if __name__ == "__main__":
    hilo_cafe = threading.Thread(target=cafe)
    hilo_tostadas = threading.Thread(target=tostadas)
    hilo_tortilla = threading.Thread(target=tortilla)

    hilo_cafe.start()
    hilo_tostadas.start()
    hilo_tortilla.start()

    hilo_cafe.join()
    hilo_tostadas.join()
    hilo_tortilla.join()