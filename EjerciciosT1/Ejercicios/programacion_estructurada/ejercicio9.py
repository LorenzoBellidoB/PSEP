#coding: latin1

def rango(num1, num2):
    for numero in range(num1 + 1, num2):
        print(numero, end=", ")

def main():
    num1 = int(input("Escriba el primer número"))
    num2 = int(input("Escriba el segundo número"))
    if num1 < num2:
        numeros = rango(num1,num2)
        print = str(numeros)
    else:
        print("El primer número en mayor")

if __name__ == "__main__":
    main()