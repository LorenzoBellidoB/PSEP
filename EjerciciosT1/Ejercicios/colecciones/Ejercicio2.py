#coding: latin1

lista = []

while len(lista) < 10:
    num = int(input("Introduzca un n�mero:"))
    lista.append(num)

max = max(lista)
min = min(lista)

print("El n�mero m�ximo es: " + str(max))
print("El n�meron m�nimo es: " + str(min))