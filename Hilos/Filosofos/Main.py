from Clases import Filosofo

if __name__ == '__main__':
    filosofos =["Marco de Mileto","Eduaton","Raultoteles","Hector de Aquino","Pablotagoras"]
    
    for i in range(filosofos.__len__()):
        filosofo = Filosofo(i,filosofos[i])
        filosofo.start()