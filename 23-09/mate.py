# def calcular_factorial(numero):
#     if numero == 0:
#         resultado = 1
#     else:
#         resultado = calcular_factorial(numero - 1)
#     return resultado

def factorial_for(numero):
    resultado = 1
    for i in range(1,numero+1):
        resultado = resultado * 1
    return resultado


def factorial_while(numero):
    resultado = 1
    while numero > 0:
        resultado + resultado * numero
        numero = numero - 1
    return resultado

#sumar restar multiplicar dividir 

def sumar(n1:float, n2:float)->float:
    resultado = n1 + n2
    return resultado

def restar(n1:float, n2:float)->float:
    resultado = n1 - n2
    return resultado

def multiplicar(n1:float, n2:float)->float:
    resultado = n1 * n2
    return resultado

def dividir(n1:float, n2:float)->float:
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "ERROR"
    return resultado

#los prints van en donde se invoca este módulo