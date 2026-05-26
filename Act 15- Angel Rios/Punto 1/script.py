#1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
#deben procesar de acuerdo a lo siguiente:
#a. Ingresar nombre y nota de cada alumno (almacenar los datos en
#dos listas paralelas)
#b. Realizar un listado que muestre los nombres, notas y condición del
#alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o
#igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot;
#si la nota es inferior a 4.
#c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”.

nombres=[]
notas=[]

for x in range(4):
    nom=input("Ingrese nombre del alumno: ")
    nombres.append(nom)
    nota=int(input("Ingrese nota del alumno: "))
    notas.append(nota)

muybuenos=0

for x in range(4):
    if notas[x]>=8:
        condicion="Muy Bueno"
        muybuenos=muybuenos+1
    else:
        if notas[x]>=4:
            condicion="Bueno"
        else:
            condicion="Insuficiente"

    print(nombres[x], notas[x], condicion)

print("Cantidad de alumnos Muy Bueno:", muybuenos)

