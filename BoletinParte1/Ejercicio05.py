from multiprocessing import Process


def sumarIntervalo(num1, num2):
    suma = 0
    if num1 >= num2:
        for i in range(num2,num1 + 1):
            suma += i
    else:
        for i in range(num1,num2 + 1):
            suma += i
    print(f"La suma total es: {suma}")
    return suma

if __name__ == '__main__':
    proceso1 = Process(target=sumarIntervalo, args=(1,4))
    proceso2 = Process(target=sumarIntervalo,args=(3,1))
    proceso3 = Process(target=sumarIntervalo, args=(4,9))

    proceso1.start()
    proceso2.start()
    proceso3.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()
    print("Todos los procesos han acabado.")
