#coding: latin1

lista = []

while len(lista) < 10:
    num = int(input("Introduzca un número:"))
    lista.append(num)

max = max(lista)
min = min(lista)

print("El número máximo es: " + str(max))
print("El númeron mínimo es: " + str(min))