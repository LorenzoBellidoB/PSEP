import threading


class Contador:
   def __init__(self):
       self.valor = 0  # Contador inicializado en 0
       self.lock = threading.Lock()  # Lock para asegurar acceso atómico al contador


   # Método para incrementar el contador de forma segura
   def incrementar(self, total):
       with self.lock:  # Asegura que solo un hilo pueda modificar el contador a la vez
           if self.obtener_valor() >= total:   # Si el contador ya alcanza el total
               return  # Sale del método 
           self.valor += 1  # Incrementar el valor del contador


   # Método para obtener el valor actual del contador
   def obtener_valor(self):
       return self.valor




# Función que simula la operación de incrementar el contador desde múltiples hilos
def incrementar_contador(contador, total):
   while contador.obtener_valor() < total:
       contador.incrementar(total)  # Cada hilo incrementará el contador N veces
