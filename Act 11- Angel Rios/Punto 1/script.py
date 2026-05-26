#1. Realizar un programa que lea cuatro valores numéricos e 
#informar su suma y promedio


num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
num4 = int(input("Ingrese el cuarto valor: "))

suma = num1 + num2 + num3 + num4
promedio = suma / 4

print("La suma es:", suma)
print("El promedio es:", promedio)