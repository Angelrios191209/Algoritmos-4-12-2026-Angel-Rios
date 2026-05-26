#3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
#y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
#lista de sueldos ordenamos de menor a mayor.

n=int(input("Cantidad de empleados: "))
sueldos=[]

for x in range(n):
    sueldo=int(input("Ingrese sueldo: "))
    sueldos.append(sueldo)

for k in range(n-1):
    for x in range(n-1-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Sueldos ordenados:", sueldos)



