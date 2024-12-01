from multiprocessing import Pool


def sumarIntervalo(num1, num2):
    suma = 0
    if num1 >= num2:
        for i in range (num2, num1 + 1):
            suma += i
    else:
        for i in range (num1,num2 + 1):
            suma += i
    print(f"La suma total es: {suma}")
    return suma

if __name__ == '__main__':
    with Pool(processes=2) as pool:
        numeros = [[1,4],[3,1],[4,9]]
        res = pool.starmap(sumarIntervalo,numeros)

    print(res)