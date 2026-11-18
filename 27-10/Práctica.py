#1. Crear una función que reciba la nota de estudiantes y su nombre y lo muestre en pantalla. La función solo puede recibir un parámetro.

def mostrar_estudiante(estudiante: dict):
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Nota: {estudiante['nota']}")


alumno = {"nombre": "Juan", "nota": 8}

mostrar_estudiante(alumno)

#2. Crear una función que almacene las coordenadas de una función lineal y = mx + b. Mostrar la tabla de coordenadas 'x' e 'y'.
#Pista: En matemáticas, las coordenadas son tuplas.(3,8)

#3. Diseñar una función que determine si una lista de números contiene al menos un elemento repetido, Pista: Aprovechar que los sets o conjuntos descartan duplicados automáticamente. set(lista)