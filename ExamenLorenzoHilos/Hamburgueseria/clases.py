import random
from threading import Thread, Semaphore
import time

# Clase Maquina la cual contine un semaforo que se encargara de decir la cantidad de maquinas que tiene la hamburgueseria
class Maquina(Thread):
    maquina = Semaphore(2)

# Clase Dependiente la cual contine un semaforo que se encargara de decir la cantidad de dependientes que tiene la hamburgueseria
class Dependiente(Thread):
    dependiente = Semaphore(5)

# Clase Hamburgueseria que se encarga de adjudicar las maquinas y los clientes a cada hilo y luego liberarlos para el siguiente hilo
class Hamburgueseria(Thread):
    def __init__(self, name):
        Thread.__init__(self,name=name)
    
    # Método que dibuja por consola el paso de cada cliente por los distintos semáforos de cada clase
    def run(self):
        print(self.pintarCliente(),"El cliente", self.name, "está buscando una maquina libre", self.pintarMaquina())
        if(Maquina.maquina._value == 0):
            print(self.pintarCliente(),"El cliente", self.name, "está esperando en las maquinas")
        # Asigno el hilo al semáforo (semáforo(i-1)) para que se sepa que se esta usando esa maquina de tickets
        Maquina.maquina.acquire()
        print(self.pintarCliente(),"El cliente", self.name, "llega a la maquina de tickets", self.pintarMaquina())
        time.sleep(random.randint(1,4))
        print("📋","El ticket del cliente",self.name, "ha sido impreso")
        print(self.pintarCliente(),"El cliente", self.name," libera la maquina")
        # Luego de realizar el ticket libero el semáforo(i+1) para que pueda pasar el hilo que este esperando
        Maquina.maquina.release()

        print(self.pintarCliente(),"El cliente", self.name, "se dirige a un dependiente libre", self.pintarDependiente())
        if(Dependiente.dependiente._value == 0):
            print(self.pintarCliente(),"El cliente", self.name, "está esperando en las cajas")
        # Asigno el hilo al semáforo (semáforo(i-1)) para que se sepa que se esta usando ese dependiente
        Dependiente.dependiente.acquire()
        print(self.pintarCliente(),"El cliente", self.name, "le da el ticket al dependiente", self.pintarDependiente())
        time.sleep(random.randint(3,7))
        print(self.pintarCliente(),"El cliente", self.name, "ya tiene su comida")
        print(self.pintarCliente(),"El cliente", self.name, "paga y deja libre al dependiente")
        # Luego de realizar el pedido libero el semáforo(i+1) para que pueda pasar el hilo que este esperando
        Dependiente.dependiente.release()

# Función que dibuja las maquinas libres
    def pintarMaquina(self):
        espacios = Maquina.maquina._value
        maquina = " ❌ "
        if espacios > 0:
            maquina = ""
            for i in range(espacios):
                maquina += " 📋 "
        return maquina
    
# Función que dibuja los dependientes libres
    def pintarDependiente(self):
        espacios = Dependiente.dependiente._value
        maquina = " ❌ "
        if espacios > 0:
            maquina = ""
            for i in range(espacios):
                maquina += " 🍔 "
        return maquina
    
# Función que dibuja los clientes
    def pintarCliente(self):
        vehiculo = random.randint(1, 3)
        cliente = ""
        if vehiculo == 1:
            cliente = "🦸"
        elif vehiculo == 2:
            cliente = "🧙"
        elif vehiculo == 3:
            cliente = "🦹"
        return cliente

