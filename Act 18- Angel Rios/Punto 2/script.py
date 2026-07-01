""" 
2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida.
"""
def ordenar(v1,v2,v3):
    if v1>v2:
        aux=v1
        v1=v2
        v2=aux

    if v1>v3:
        aux=v1
        v1=v3
        v3=aux

    if v2>v3:
        aux=v2
        v2=v3
        v3=aux

    print("Valores ordenados:")
    print(v1)
    print(v2)
    print(v3)


def cargar():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    valor3=int(input("Ingrese el tercer valor: "))

    ordenar(valor1,valor2,valor3)



cargar()



