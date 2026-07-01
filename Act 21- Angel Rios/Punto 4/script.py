""" 
4-
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""

def cargar():
    candidatos = []

    for x in range(3):
        nombre = input("Nombre del candidato: ")

        provincias = []

        cantidad = int(input("Cuantas provincias desea cargar: "))

        for i in range(cantidad):
            provincia = input("Nombre de la provincia: ")
            votos = int(input("Cantidad de votos: "))

            provincias.append((provincia, votos))

        candidatos.append([nombre, provincias])

    return candidatos


def totalvotos(candidatos):
    for candidato in candidatos:
        suma = 0

        for provincia in candidato[1]:
            suma += provincia[1]

        print(candidato[0], "obtuvo", suma, "votos")


candidatos = cargar()

totalvotos(candidatos)


