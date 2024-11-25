from time import sleep

from multiprocessing import Pool

def suma(numero):
    print("Entrando: ", numero)
    suma = 0
    for i in range (1,numero+1):
        suma += i
        print("Sumando hasta el", numero,":", suma)
    sleep(2)
    return suma



if __name__ == "__main__":

    # Con pool indicamos que vamos a tener 3 procesos en paralelo
    with Pool(processes=3) as pool:
        numeros =[1,10,5]

        # Ejecutamos la función square y le pasamos la lista con los datos
        results = pool.map(suma,numeros)
    
    print("Resultados:",results)