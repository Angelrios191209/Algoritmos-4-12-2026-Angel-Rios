#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.

cantidad=int(input("Ingrese cantidad de puntos: "))

cuad1=0
cuad2=0
cuad3=0
cuad4=0

for i in range(cantidad):
    x=int(input("Ingrese coordenada x: "))
    y=int(input("Ingrese coordenada y: "))

    if x>0 and y>0:
        cuad1=cuad1+1
    else:
        if x<0 and y>0:
            cuad2=cuad2+1
        else:
            if x<0 and y<0:
                cuad3=cuad3+1
            else:
                if x>0 and y<0:
                    cuad4=cuad4+1

print("Puntos en el primer cuadrante:", cuad1)
print("Puntos en el segundo cuadrante:", cuad2)
print("Puntos en el tercer cuadrante:", cuad3)
print("Puntos en el cuarto cuadrante:", cuad4)


