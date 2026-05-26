
#1. Definir una lista que almacene por asignación los nombres de 5 personas.
#Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.

# Lista por asignación
nombres=[]

for i in range(5):
    nombre=input("Ingrese un nombre: ")
    nombres.append(nombre)

contador=0

for nombre in nombres:
    if len(nombre)>=5:
        contador=contador+1

print("Cantidad de nombres con 5 o más caracteres:", contador)

