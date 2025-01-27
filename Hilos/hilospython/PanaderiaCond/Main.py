from Clases import Panaderia, Comprador, Reponedor

if __name__ == '__main__':
    NUM_COMP = 15
    p=Panaderia()
    lista=[]
    for i in range(NUM_COMP):
        lista.append(Comprador(i,p, ))
    lista.append(Reponedor(p, )) # Contrato a un reponedor

    for c in lista:
        c.start()

    for c in lista:
        c.join()