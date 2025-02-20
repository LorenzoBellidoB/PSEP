#Clase operario
import random
from threading import Condition, Thread
import time


class Operario(Thread):
    condicion = Condition()

    trabajando=False

    atomo=0

    moleculasCreadas=0

    def __init__(self, nombre):
        self.atomosH=0
        self.atomosO=0
        self.nombre=nombre
        Thread.__init__(self)
    
    #metodo run
    def run(self):
        
        Operario.atomo = random.randint(1,2)
        while True:
            with Operario.condicion:  

                while Operario.atomo==1 and self.atomosH>=2 or Operario.trabajando or Operario.atomo == 2 and self.atomosO>=1:
                    Operario.condicion.wait(timeout=7) 

                Operario.trabajando=True

    
            if(Operario.atomo==1 and self.atomosH<2):
                self.atomosH+=1
                print("El operario ",self.nombre," tiene ", self.atomosH," atomos de H")    
                
            if(Operario.atomo==2 and self.atomosO<1):
                self.atomosO+=1
                print("El operario ",self.nombre," tiene ", self.atomosO," atomos de O")   

            if(self.atomosH==2 and self.atomosO==1):
                print("El operario ",self.nombre," está creando la molecula")
                self.atomosO=0
                self.atomosH=0
                time.sleep(2)
                Operario.moleculasCreadas+=1

                print("Hay ",Operario.moleculasCreadas, "moleculas creadas")
                

            print("La fabrica está produciendo otro atomo")
            Operario.atomo=random.randint(1,2)            
            print("Se ha creado el atomo ",Operario.atomo)
            time.sleep(2)

            with Operario.condicion:
                Operario.trabajando=False
                Operario.condicion.notifyAll()