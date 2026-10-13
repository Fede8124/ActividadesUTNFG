# determinar si un digito/caracter que ingreso es un caracter numerico entre 0 a 9 (48 a 57 en ascii)
# que devuelva true si es numero que devuelva false si no es
def es_numero(caracter:str)->bool:
    retorno = False
    if ord(caracter) >= 48 and ord(caracter) <= 57:
        retorno = True
    
    return retorno


#hacer una funcion que determine si un str es un numero (5G3 seria falso, 123 seria verdadero)
def es_numerico(cadena:str)->bool:
    retorno = True
    for caracter in cadena:
        valor = es_numero(caracter)
        if(valor == False):
            retorno = False
            break
        
    return retorno

#Una funcion de determine si un caracter es alfabetico

def es_alfabeto(caracter:str)->bool:
    retorno = False
    if (ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
        retorno = True 

    return retorno

#Una funcion de determine si una cadena es alfabetico

def es_alfabetico(cadena:str)->bool:
    retorno = True
    for caracter in cadena:
            valor = es_alfabeto(caracter)
            if(valor == False):
                retorno = False
                break

    return retorno

#Una funcion de determine si una cadena es un numero entero

def es_entero(cadena:str)->bool:
    retorno = True
    primer_caracter = cadena[0]
    if ord(primer_caracter) != 45 and not es_numero(caracter):
        retorno = False
    elif ord(primer_caracter) == 45 and es_numero(caracter):
        # for caracter in cadena:
        #         valor = es_numero(caracter)
        #         if(valor == False):
        #             retorno = False
        #             break

    


#Una funcion de determine si una cadena es un numero real (un solo numero, un punto y parte decimal)