from multiprocessing import Queue, Process
from time import sleep
import random

'''
Método que recibe una cola y coge del fichero "propietarios.txt" los datos de los conductores que han pasado por un radar
y los envia mediante la cola a otro proceso.
'''
def leerFichero(cola1):
    i = 0
    archivo = open("ExamenLorenzo/propietarios.txt", "r")
    lineas = archivo.readlines()
    while i < 20:
        num = random.randint(0,len(lineas)-1)
        conductor = lineas[num]
        conductor = conductor.replace("\n","")
        cola1.put(conductor)
        i = i + 1
        sleep(0.5)
'''
Método que recibe una cola y se encarga de asignar una velocidad aleatoria al vehiculo recibido por la cola y comprueba
si dicha velocidad es superior a la limite para enviar el conductor mediante la cola a otro proceso
'''
def asignarVelocidad(cola1,cola2, velMax):
    for i in range (0,20):
        velocidad = random.randint(0,velMax + 50)
        conductor = cola1.get()
        if velocidad > velMax:
            conductor = f"{conductor}:{velocidad}"
            cola2.put(conductor)
    cola2.put(None)

'''
Método que recibe una cola y se encarga de escribir una multa en el fichero "multas.txt" con la matricula y la velocidad asignada
'''
def escribirMulta(cola2):
    archivo = open("ExamenLorenzo/multas.txt", "w")
    conductor = ""
    datos = ""
    conductor = cola2.get()
    while conductor != None:
        datos = conductor.split(":")
        archivo.write(f"Multa para {datos[1]} ({datos[0]}): {datos[2]} km/h\n")
        conductor = cola2.get()
    archivo.close()

    


if __name__ == '__main__':
    cola1 = Queue()
    cola2 = Queue()
    velocidadMaxima = int(input("Inserta una velocidad máxima: "))
    proceso1 = Process(target=leerFichero, args=(cola1,))
    proceso2 = Process(target=asignarVelocidad, args=(cola1, cola2, velocidadMaxima))
    proceso3 = Process(target=escribirMulta,args=(cola2,))

    proceso1.start()
    proceso2.start()
    proceso3.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()

    print("Todos los procesos han acabado")