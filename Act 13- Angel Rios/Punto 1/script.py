
#1. En una empresa trabajan n empleados cuyos 
#sueldos oscilan entre $100 y $500, realizar 
#un programa que lea los sueldos que cobra 
#cada empleado e informe cuántos empleados 
#cobran entre $100 y $300 y cuántos cobran 
#más de $300. Además el programa deberá 
#informar el importe que gasta la empresaen sueldos al personal.

n=int(input("Ingrese la cantidad de empleados:"))

entre100y300=0
mayor300=0
gastototal=0

for i in range(n):
    sueldo=int(input("Ingrese sueldo del empleado: "))
    gastototal=gastototal+sueldo

    if sueldo>=100 and sueldo<=300:
        entre100y300=entre100y300+1
    else:
        if sueldo>300:
            mayory300=mayory300+1

print("Empleados que cobran entre 100 y 300:", entre100y300)
print("Empleados que cobran más de 300:", mayory300)
print("Gasto total en sueldos:", gastototal)

