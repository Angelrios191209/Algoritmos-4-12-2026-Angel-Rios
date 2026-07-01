""" 
3-

Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [[&quot;juan&quot;,(2000,3000,4233)] , [&quot;ana&quot;,(3444,1000,5333)] , etc. ]
"""
def cargar():
    empleados = []

    for x in range(5):
        nombre = input("Nombre del empleado: ")

        sueldo1 = float(input("Primer sueldo: "))
        sueldo2 = float(input("Segundo sueldo: "))
        sueldo3 = float(input("Tercer sueldo: "))

        empleados.append([nombre, (sueldo1, sueldo2, sueldo3)])

    return empleados


def imprimirtotales(empleados):
    print("Total cobrado por cada empleado")

    for empleado in empleados:
        total = empleado[1][0] + empleado[1][1] + empleado[1][2]
        print(empleado[0], "cobro", total)


def mayores10000(empleados):
    print("Empleados con ingresos mayores a 10000")

    for empleado in empleados:
        total = empleado[1][0] + empleado[1][1] + empleado[1][2]

        if total > 10000:
            print(empleado[0])


empleados = cargar()

imprimirtotales(empleados)

mayores10000(empleados)




