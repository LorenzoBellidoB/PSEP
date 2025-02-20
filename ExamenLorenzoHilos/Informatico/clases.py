import random
from threading import Thread,Condition
import time

# Clase Recaudacion que se encarga de manejar la condicion por la que pasa cada hilo y el saldo total de la cuenta
class Recaudacion:
    cond = Condition()
    saldo = 0

    def __init__(self):
        pass

# Clase Voluntario que se encarga de añadir el dinero recaudado a la cuenta mientras que la condicion lo permita
class Voluntario(Thread):
    
    def __init__(self, name):
        Thread.__init__(self,name=name)
        self.recaudado = 0
    
    # Llama a la función para recaudar dinero, comprueba que se pueda añadir dicho dinero y lo añade
    def run(self):
        while True:
            
            self.voluntariado()
            while (Recaudacion.saldo + self.recaudado) > 2000:
                print("EL voluntario",self.name, "no puede añadir más dinero. Saldo total: ", Recaudacion.saldo, "€. Recaudado: ", self.recaudado, "€")
                Recaudacion.cond.wait()

            Recaudacion.saldo += self.recaudado
            Recaudacion.cond.release()

            print("Cuenta: ", Recaudacion.saldo, "€")
            
            
    
    def voluntariado(self):
        print("El voluntario", self.name, "sale a recaudar")
        time.sleep(random.randint(1,3))
        Recaudacion.cond.acquire()        
        self.recaudado = random.randint(4,25)
        print("El voluntario", self.name, "ha recaudado", self.recaudado, "€")

# Clase Gestor que se encarga de retirar el dinero recaudado de la cuenta mientras que la condicion lo permita
class Gestor(Thread):
    def __init__(self, name):
        Thread.__init__(self,name=name)
        self.retirado = 0

 # Llama a la función para retira dinero, comprueba que se pueda retirar dicho dinero y lo retira
    def run(self):
        while True:
            
            self.gestion()
            while (Recaudacion.saldo - self.retirado) < 0:
                print("El gestor", self.name, "no puede retirar más dinero. Saldo total: ", Recaudacion.saldo, "€. El gestor pide: ", self.retirado, "€")
                Recaudacion.cond.wait()

            Recaudacion.saldo -= self.retirado
            Recaudacion.cond.release()

            print("Cuenta: ", Recaudacion.saldo, "€")


    def gestion(self):
        print("El gestor ", self.name, "toma el dinero")
        time.sleep(random.randint(2,5))
        Recaudacion.cond.acquire()
        self.retirado = random.randint(4,25)
        print("El gestor", self.name, "intenta tomar", self.retirado,"€")