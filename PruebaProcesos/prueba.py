from time import sleep
from multiprocessing import Pool

def square(number):
    print("Entrando:",number)
    sleep(2)
    cuadrado = number*number
    print(number,"x",number,"=",cuadrado)
    sleep(2)
    return cuadrado

if __name__ == "__main__":
    # Con pool indicamos que vamos a tener 3 procesos en paralelo
    with Pool(processes=3) as pool:
        numbers=[1,2,3,4,5]

        # Ejecutamos la función square y le pasamos la lista con los datos
        results = pool.map(square,numbers)
    
    print("Resultados:",results)