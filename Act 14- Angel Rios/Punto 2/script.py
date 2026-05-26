#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
#empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa
#que permita almacenar los sueldos de los empleados agrupados en dos
#listas. Imprimir las dos listas de sueldos.


manana=[]
tarde=[]

print("Carga sueldos turno mañana")
for i in range(4):
    sueldo=int(input("Ingrese sueldo: "))
    manana.append(sueldo)

print("Carga sueldos turno tarde")

for i in range(4):
    sueldo=int(input("Ingrese sueldo: "))
    tarde.append(sueldo)

print("Sueldos turno mañana:", manana)
print("Sueldos turno tarde:", tarde)


