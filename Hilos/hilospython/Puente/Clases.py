import random
from threading import Thread, Semaphore
import time

class Puente(Thread):
    semaforoNorte = Semaphore(1)
    semaforoSur = Semaphore(1)
    def __init__(self, name):
        Thread.__init__(self, name = name)

    def run(self):
        