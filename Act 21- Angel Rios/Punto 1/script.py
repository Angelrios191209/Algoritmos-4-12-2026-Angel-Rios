"""
1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

"""

def cargarlista():
    lista = []

    for x in range(5):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)

    return lista


def mayormenor(lista):
    mayor = lista[0]
    menor = lista[0]

    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
        elif elemento < menor:
            menor = elemento

    return (mayor, menor)


lista = cargarlista()

mayor, menor = mayormenor(lista)

print("Mayor:", mayor)
print("Menor:", menor)



