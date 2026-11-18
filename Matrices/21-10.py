#El objetivo aquí es entender cómo indexar una matriz con bucles anidados (for i para filas, for j para columnas).

#Ejercicio 1: El Tablero de Ceros
#Escribir una función llamada crear_tablero(filas, columnas) que reciba dos números enteros y devuelva una matriz llena de ceros (0).

def crear_tablero(filas, columnas):
    tablero = [None] * filas
    for i in range(filas):
        tablero[i] = [None] * columnas
        for j in range(columnas):
            tablero[i][j] = 0
    return tablero

#Probarla generando una matriz de 3x4 e imprimir fila por fila para que se vea cuadrada en la consola.

m = crear_tablero(3, 4)
for fila in m:
    print(fila)


#Dada una matriz de números enteros de 3 x 3 (se pueden inventar los números):
#   1. Calcular y mostrar la suma de todos los elementos de la matriz.
#   2. Calcular y mostrar la suma de cada fila por separado.

matriz = [
    [4, 7, 2],
    [9, 1, 6],
    [3, 8, 5]
]

suma_total = 0

for i in range(3):
    suma_fila = 0
    for j in range(3):
        suma_fila = suma_fila + matriz[i][j]
    print("Suma de la fila", i, ":", suma_fila)
    suma_total = suma_total + suma_fila

print("Suma de todos los elementos:", suma_total)


#Ejercicio 3: Buscando al Intruso (Mayor y Menor)
#Crear un programa que recorra una matriz de números enteros de 4 x 3. El programa debe encontrar:
#   • El número más grande y su posición (fila y columna).
#   • El número más chico y su posición (fila y columna).

#ejercicio 4: Una matriz de 5 x 4 donde cada fila es un alumno y cada columna es la nota de un examen parcial.
#•	Escribir un programa que reemplace todas las notas menores a 4 (desaprobado) por un 0, simulando que el alumno debe recuperar esa instancia.
#•	Imprimir la matriz original y la matriz modificada.

#Ejercicio 5: El Espejo (Matriz Transpuesta)
#La transpuesta de una matriz se obtiene cambiando sus filas por columnas.
#•	Crear una matriz de 2 x 3 (2 filas por 3 columnas).
#•	Diseñar un algoritmo que construya una nueva matriz que sea la transpuesta quedando la misma de 3 x 2 (3 filas por 2 columnas).
#•	Ejemplo: Si la entrada es [[1, 2, 3], [4, 5, 6]], la salida debe ser [[1, 4], [2, 5], [3, 6]].

#conveniente crear una biblioteca para funciones de matrices asi vamos reutilizando entre ejercicios

#Ejercicio 6: Diagonales (Solo para Matrices Cuadradas)
#Dada una matriz cuadrada de 4 x 4:
#1.	Mostrar en pantalla únicamente los elementos que forman la diagonal principal (donde la fila es igual a la columna: i == j).
#•	Definición: Elementos aij tales que i = j
#•	Posiciones en 4 x 4: (1,1), (2,2), (3,3), (4,4)
#•	Trayectoria: Desde la esquina superior izquierda hasta la esquina inferior derecha.

#2.	Mostrar los elementos de la diagonal secundaria.
#•	Definición: Elementos aij tales que i + j = n + 1 (donde n = 4, por lo que i + j = 5).
#•	Posiciones en 4 x 4: (1,4), (2,3), (3,2), (4,1)
#Trayectoria: Desde la esquina superior derecha hasta la esquina inferior izquierda.

#ej7 en el campus