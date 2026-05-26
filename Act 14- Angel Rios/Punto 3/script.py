#3. Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje
#si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o
#más posiciones en la lista)


numeros=[]

for i in range(5):
    valor=int(input("Ingrese un número entero: "))
    numeros.append(valor)

mayor=numeros[0]

for num in numeros:
    if num>mayor:
        mayor=num

contador=0
for num in numeros:
    if num==mayor:
        contador=contador+1

print("El mayor valor es:", mayor)

if contador>=2:
    print("El mayor se repite en la lista")



