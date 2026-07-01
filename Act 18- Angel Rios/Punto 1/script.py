""" 
1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)
"""
def menor():
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))
    valor3=int(input("Ingrese el tercer valor: "))

    if valor1<valor2 and valor1<valor3:
        print("El menor es:",valor1)
    else:
        if valor2<valor3:
            print("El menor es:",valor2)
        else:
            print("El menor es:",valor3)



menor()
print("****************")
menor()
