""" 
2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado.
"""

def cargardatos():
    nombres = []
    precios = []

    for x in range(5):
        nombre = input("Ingrese el nombre del articulo: ")
        precio = float(input("Ingrese el precio: "))

        nombres.append(nombre)
        precios.append(precio)

    return nombres, precios


def imprimirdatos(nombres, precios):
    print("\nLista de articulos:")
    for x in range(len(nombres)):
        print(nombres[x], "-", precios[x])


def articulomayorprecio(nombres, precios):
    posmayor = 0

    for x in range(1, len(precios)):
        if precios[x] > precios[posmayor]:
            posmayor = x

    print("\nArticulo mas caro:")
    print(nombres[posmayor], "-", precios[posmayor])


def menoresimporte(nombres, precios):
    importe = float(input("\nIngrese un importe: "))

    print("Articulos con precio menor o igual al importe ingresado:")
    for x in range(len(precios)):
        if precios[x] <= importe:
            print(nombres[x], "-", precios[x])

nombres, precios = cargardatos()

imprimirdatos(nombres, precios)

articulomayorprecio(nombres, precios)

menoresimporte(nombres, precios)


