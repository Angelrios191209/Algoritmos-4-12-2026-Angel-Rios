#3. Realizar un programa que solicite la carga por teclado de dos 
#números, si el primero es mayor al segundo informar su suma y 
#diferencia, en caso contrario informar el producto y la división 
#del primero respecto al segundo.

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    suma = num1 + num2
    diferencia = num1 - num2
    print("La suma es:", suma)
    print("La diferencia es:", diferencia)
else:
    producto = num1 * num2
    division = num1 / num2
    print("El producto es:", producto)
    print("La división es:", division)