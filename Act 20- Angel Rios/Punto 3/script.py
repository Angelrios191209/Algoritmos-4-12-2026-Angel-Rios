""" 
3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""
def cargarlista():
    lista = []

    for x in range(10):
        valor = int(input("Ingrese un numero: "))
        lista.append(valor)

    return lista


def separarlistas(lista):
    positivos = []
    negativos = []

    for x in range(len(lista)):
        if lista[x] >= 0:
            positivos.append(lista[x])
        else:
            negativos.append(lista[x])

    return positivos, negativos


def imprimirlista(lista, titulo):
    print(titulo)

    for x in range(len(lista)):
        print(lista[x], end=" ")

    print()


lista = cargarlista()

positivos, negativos = separarlistas(lista)

imprimirlista(positivos, "Lista de positivos:")
imprimirlista(negativos, "Lista de negativos:")




