#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos
#informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.


mayores = 0
menores = 0

for i in range(10):
    nota = int(input("Ingrese la nota: "))

    if nota >= 7:
        mayores = mayores + 1
    else:
        menores = menores + 1

print("Notas mayores o iguales a 7:", mayores)
print("Notas menores a 7:", menores)
