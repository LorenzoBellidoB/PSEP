from threading import Thread


class Vocales(Thread):
    fichero = "BoletinParte2/vocales.txt"
    def __init__(self, name):
        Thread.__init__(self, name = name)

    def contar_vocal(fichero, vocal):
        with open(fichero, 'r', encoding='utf-8') as f:
            texto = f.read().lower()
            return texto.count(vocal)

    def run(self):
        print(f"La vocal '{self.name}' aparece {self.contar_vocal(self.fichero, self.name)} veces.")