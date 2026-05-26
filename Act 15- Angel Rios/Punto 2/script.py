#2. Realizar un programa que pida la carga de dos listas numéricas enteras
#de 4 elementos cada una. Generar una tercera lista que surja de la suma
#de los elementos de la misma posición de cada lista. Mostrar esta tercera
#lista.


lista1=[]
lista2=[]
lista3=[]

for x in range(4):
    n1=int(input("Ingrese valor lista 1: "))
    lista1.append(n1)

for x in range(4):
    n2=int(input("Ingrese valor lista 2: "))
    lista2.append(n2)

for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)

print("Lista 3 resultante:", lista3)


