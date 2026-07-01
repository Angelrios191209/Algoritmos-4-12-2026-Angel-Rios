""" 
2-
Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea
el número de documento del alumno. Como valor almacenar una lista con
componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las
materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

def cargar():
    alumnos={}

    for x in range(3):
        dni=int(input("Ingrese el DNI del alumno: "))
        materias=[]

        for y in range(3):
            nombre=input("Ingrese el nombre de la materia: ")
            nota=int(input("Ingrese la nota: "))
            materias.append((nombre,nota))

        alumnos[dni]=materias

    return alumnos

def imprimir(alumnos):
    print("Listado de alumnos")

    for dni in alumnos:
        print("DNI:", dni)

        for materia,nota in alumnos[dni]:
            print(materia, nota)

def consultar(alumnos):
    dni=int(input("Ingrese el DNI a consultar: "))

    if dni in alumnos:
        print("Materias del alumno")

        for materia,nota in alumnos[dni]:
            print(materia, nota)
    else:
        print("El alumno no existe")


alumnos=cargar()
imprimir(alumnos)
consultar(alumnos)


