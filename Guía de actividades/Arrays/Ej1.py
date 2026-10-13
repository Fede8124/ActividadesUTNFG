# Desarrollar una función que permita crear un array de números con la cantidad de elementos
# que establezca el parámetro recibido.

# Escribir una función que permita ingresar la cantidad de números que reciba como parámetro. 
# Crear el array con la función del punto 1.


# Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números


def crear_array(cantidad: int) -> list:
    

# 1 y 2 segun el profe

# def crear_lista(elementos : int)->list:
#     lista = [0] * elementos
    
#     return lista
    
# def poblar_lista(numero:int):
#     lista = crear_lista(5)
#     for i in range(len(lista)):
#         lista[i] = (i+1)
        
#     return lista
        
# mi_lista = poblar_lista(5)

# for elemento in mi_lista:
#     print(elemento)


#el 3 segun otro compa
# '''
# Escribir una función parecida a la anterior, pero la misma deberá calcular
# y devolver el promedio de los números positivos
# '''

# array = [1, -2, -3, 4, 5]

# def calcular_promedio(lista):
#     """Esta función recibe una lista de enteros y calcula el promedio de todos los números.
    
#     argumentos:
    
#         lista(list): lista de enteros
    
#     retorno:
    
#         float: promedio de todos los números en la lista
    
#     """

#     suma = 0
#     contador_positivos = 0
#     for numero in lista:
#         if numero > 0:    
#             suma += numero
#             contador_positivos += 1

#     if contador_positivos == 0:
#         return 0

#     promedio = suma / contador_positivos
#     return promedio

# promedio = calcular_promedio(array)
# if promedio == 0:
#     print("No hay números positivos en la lista.")
# else:
#     print(f"El promedio de los números en la lista es: {round(promedio, 2)}")



# punto 4 segun el profe

# '''
# Escribir una función parecida a la anterior, pero la misma deberá calcular
# y devolver el promedio de los números positivos
# '''

# array = [1, -2, -3, 4, 5]

# def calcular_promedio(lista):
#     """Esta función recibe una lista de enteros y calcula el promedio de todos los números.
    
#     argumentos:
    
#         lista(list): lista de enteros
    
#     retorno:
    
#         float: promedio de todos los números en la lista
    
#     """

#     suma = 0
#     contador_positivos = 0
#     for numero in lista:
#         if numero > 0:    
#             suma += numero
#             contador_positivos += 1

#     if contador_positivos == 0:
#         return 0

#     promedio = suma / contador_positivos
#     return promedio

# promedio = calcular_promedio(array)
# if promedio == 0:
#     print("No hay números positivos en la lista.")
# else:
#     print(f"El promedio de los números en la lista es: {round(promedio, 2)}")




# ej 5 segun el profe


# def crear_lista(elementos : int)->list:
#     lista = [0] * elementos
    
#     return lista
    
# def poblar_lista(numero:int):
#     lista = crear_lista(3)
#     for i in range(len(lista)):
#         lista[i] = (i+1)
        
#     return lista
        
# def multiplicar_elementos(lista:list)->list:
#     multiplicacion = 1
#     for elemento in lista:
#         multiplicacion *= elemento
    
#     return multiplicacion
    
# def obtener_maximo(lista:list)->int:
#     for i in range(len(lista)):
#         if i == 0:
#             indice_maximo = i
#             maximo = lista[i]
#         if lista[i] > maximo:
#             indice_maximo = i
#             maximo = lista[i]
        
#     return indice_maximo

# mi_lista = poblar_lista(3)

# for elemento in mi_lista:
#     print(elemento)

# resultado = multiplicar_elementos(mi_lista)
# print(f"La multiplicacion es: {resultado}")

# print(obtener_maximo([3,5,7,4]))

