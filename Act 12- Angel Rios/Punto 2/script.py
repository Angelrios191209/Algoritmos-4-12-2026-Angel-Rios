#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.

cant = int(input("Ingrese la cantidad de personas: "))
suma = 0
for i in range(cant):
    altura = float(input("Ingrese la altura de la persona: "))
    suma += altura

promedio = suma / cant
print("La altura promedio es:", promedio)
