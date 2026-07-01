""" 
4. Crear dos listas paralelas. En la primera ingresar los nombres de 
empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad 
de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 
(tanto el sueldo como su nombre)

"""
def contar_a(cadena):
    cantidad=0

    for x in range(len(cadena)):
        if cadena[x]=="a" or cadena[x]=="A":
            cantidad=cantidad+1

    return cantidad


texto=input("Ingrese una palabra o frase: ")

cant=contar_a(texto)

print("La cantidad de letras a o A es:",cant)










