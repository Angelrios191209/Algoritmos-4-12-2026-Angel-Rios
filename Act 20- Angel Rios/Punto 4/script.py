""" 
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""
def mayoresedad(*edades):
    contador = 0

    for x in range(len(edades)):
        if edades[x] >= 18:
            contador += 1

    return contador


cantidad = mayoresedad(15, 20, 18, 25, 12, 30, 17)

print("Cantidad de mayores de edad:", cantidad)



