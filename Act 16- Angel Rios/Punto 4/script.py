""" 
4. Se realiza una evaluación a 6 docentes por parte de sus alumnos. Se registran
sus nombres y puntajes promedio obtenidos (de 1 a 10).
Cargar sus datos en vectores paralelos, mostrar docente con calificación más
alta y más baja, ordenar los vectores de mayor a menor de acuerdo con la
calificación y mostrar en pantalla la cantidad de docentes que aprobaron y
desaprobaron (tomando como base que se aprueba con una nota mayor o
igual a 6)

"""

docentes=[]
puntajes=[]

for x in range(6):
    nom=input("Ingrese nombre del docente: ")
    docentes.append(nom)

    nota=int(input("Ingrese puntaje: "))
    puntajes.append(nota)

mayor=puntajes[0]
menor=puntajes[0]

for x in range(6):
    if puntajes[x]>mayor:
        mayor=puntajes[x]

    if puntajes[x]<menor:
        menor=puntajes[x]

print("Docente con mejor calificación:")
for x in range(6):
    if puntajes[x]==mayor:
        print(docentes[x], mayor)

print("Docente con menor calificación:")
for x in range(6):
    if puntajes[x]==menor:
        print(docentes[x], menor)

for k in range(5):
    for x in range(5-k):

        if puntajes[x]<puntajes[x+1]:

            aux1=puntajes[x]
            puntajes[x]=puntajes[x+1]
            puntajes[x+1]=aux1

            aux2=docentes[x]
            docentes[x]=docentes[x+1]
            docentes[x+1]=aux2

print("Docentes ordenados de mayor a menor:")

for x in range(6):
    print(docentes[x], puntajes[x])

aprobaron=0
desaprobaron=0

for x in range(6):

    if puntajes[x]>=6:
        aprobaron=aprobaron+1
    else:
        desaprobaron=desaprobaron+1

print("Cantidad que aprobaron:", aprobaron)
print("Cantidad que desaprobaron:", desaprobaron)



