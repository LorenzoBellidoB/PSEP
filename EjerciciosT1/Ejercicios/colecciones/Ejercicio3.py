#coding: latin1

lista = []

while len(lista) < 8:
    num = int(input("Introduzca un número: "))
    lista.append(num)

for numero in lista:
    var = "El numero" + str(numero) +  " es par" if (numero % 2 == 0) else "El numero" + str(numero) +  " es impar"
    print(var)
