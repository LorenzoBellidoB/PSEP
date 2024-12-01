from multiprocessing import Process, Queue

def leerFichero(ruta_fichero, año, queue):
    with open(ruta_fichero, 'r') as file:
        for linea in file:
            nombre, año_estreno = linea.strip().split(';')
            if int(año_estreno) == año:
                queue.put((nombre, año_estreno))
    queue.put(None)  # Señal de finalización

### Proceso 2: Guardar películas en un fichero
'''
Este proceso recibe las películas del primer proceso y las almacena en un fichero.
'''
def escribirFichero(año, queue):
    with open(f'BoletinParte2/peliculas{año}.txt', 'w') as file:
        while True:
            pelicula = queue.get()
            if pelicula is None:
                break
            nombre, año_estreno = pelicula
            file.write(f'{nombre};{año_estreno}\n')

### Main: Solicitar datos al usuario y lanzar los procesos
'''
El 'Main' solicita al usuario que introduzca un año y la ruta del fichero, y luego lanza los dos procesos.
'''
   

if __name__ == '__main__':
    año = int(input("Introduce un año (debe ser menor al actual): "))
    ruta_fichero = "BoletinParte2/peliculas.txt"

    queue = Queue()

    p1 = Process(target=leerFichero, args=(ruta_fichero, año, queue))
    p2 = Process(target=escribirFichero, args=(año, queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
