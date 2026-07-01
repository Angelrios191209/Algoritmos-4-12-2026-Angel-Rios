""" 
3. Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los
números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltan menos
días.
"""
def retornarsuperficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie


def cargarrectangulo():
    lado1=int(input("Ingrese el primer lado: "))
    lado2=int(input("Ingrese el segundo lado: "))
    superficie=retornarsuperficie(lado1,lado2)
    return superficie



superficie1=cargarrectangulo()
superficie2=cargarrectangulo()

if superficie1>superficie2:
    print("El rectángulo 1 tiene mayor superficie")
elif superficie2>superficie1:
    print("El rectángulo 2 tiene mayor superficie")
else:
    print("Los dos rectángulos tienen la misma superficie")



