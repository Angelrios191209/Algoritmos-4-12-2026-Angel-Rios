""" 
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""
empleados=[]
faltas=[]

for x in range(3):

    nombre=input("Ingrese nombre del empleado: ")
    empleados.append(nombre)

    cantidad=int(input("¿Cuántos días faltó?: "))

    faltas.append([])

    for k in range(cantidad):
        dia=int(input("Ingrese el día de la falta: "))
        faltas[x].append(dia)

print("Listado de empleados y días que faltó")

for x in range(3):

    print("Empleado:",empleados[x])

    for k in range(len(faltas[x])):
        print(faltas[x][k])

print("Cantidad de inasistencias")

for x in range(3):
    print(empleados[x],len(faltas[x]))

menor=len(faltas[0])

for x in range(1,3):
    if len(faltas[x])<menor:
        menor=len(faltas[x])

print("Empleado/s con menos faltas")

for x in range(3):
    if len(faltas[x])==menor:
        print(empleados[x])




