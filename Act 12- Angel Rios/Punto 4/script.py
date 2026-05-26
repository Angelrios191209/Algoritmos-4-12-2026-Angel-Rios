#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos15 = 0
sumapares = 0

for i in range(10):
    num = int(input("Ingrese un número: "))

    if num < 0:
        negativos = negativos + 1
    else:
        if num > 0:
            positivos = positivos + 1

    if num % 15 == 0:
        multiplos15 = multiplos15 + 1

    if num % 2 == 0:
        sumapares = sumapares + num

print("Cantidad de negativos:", negativos)
print("Cantidad de positivos:", positivos)
print("Cantidad de múltiplos de 15:", multiplos15)
print("Suma de números pares:", sumapares)


