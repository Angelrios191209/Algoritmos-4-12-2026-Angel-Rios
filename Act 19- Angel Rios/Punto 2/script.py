""" 
2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""

def cargarsueldos():
    sueldos = []
    for x in range(10):
        sueldo = float(input("Ingrese el sueldo: "))
        sueldos.append(sueldo)
    return sueldos


def imprimirsueldos(lista):
    print("Lista de sueldos:")
    for x in range(len(lista)):
        print(lista[x])


def superiores4000(lista):
    contador = 0
    for x in range(len(lista)):
        if lista[x] > 4000:
            contador += 1
    print("Cantidad de sueldos mayores a $4000:", contador)


def promediosueldos(lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x]

    promedio = suma / len(lista)
    return promedio


def debajopromedio(lista, promedio):
    print("Sueldos debajo del promedio:")
    for x in range(len(lista)):
        if lista[x] < promedio:
            print(lista[x])


sueldos = cargarsueldos()

imprimirsueldos(sueldos)

superiores4000(sueldos)

promedio = promediosueldos(sueldos)
print("Promedio de sueldos:", promedio)

debajopromedio(sueldos, promedio)


