#coding: latin1

def rango(num1, num2):
    for numero in range(num1 + 1, num2):
        print(numero, end=", ")

def main():
    num1 = int(input("Escriba el primer n�mero"))
    num2 = int(input("Escriba el segundo n�mero"))
    if num1 < num2:
        numeros = rango(num1,num2)
        print = str(numeros)
    else:
        print("El primer n�mero en mayor")

if __name__ == "__main__":
    main()