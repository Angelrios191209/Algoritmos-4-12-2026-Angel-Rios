#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas
#(valores float)
#Obtener el promedio de las mismas. Contar cuántas personas son más
#altas que el promedio y cuántas más bajas.

alturas=[]

for i in range(5):
    altura=float(input("Ingrese altura: "))
    alturas.append(altura)

suma=0
for altura in alturas:
    suma=suma+altura

promedio=suma/5

masaltos=0
masbajos=0

for altura in alturas:
    if altura>promedio:
        masaltos=masaltos+1
    else:
        masbajos=masbajos+1

print("Promedio de alturas:", promedio)
print("Personas más altas que el promedio:", masaltos)
print("Personas más bajas que el promedio:", masbajos)
