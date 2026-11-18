#CONSTANTES

CANTIDAD = 30
DIGITOS = "0123456789"
LETRAS = ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ")
NOTA_MINIMA = 1
NOTA_MAXIMA = 10



#FUNCIONES NECESARIAS

def es_entero(texto:str)->bool:
    """
    Verifica que el texto ingresado contenga números enteros positivos.

    Parámetros:
        texto (str): texto a verificar
 
    Retorno:
        bool: True si el texto no está vacío y todos sus caracteres son dígitos
              False en caso contrario.

    """
    if texto == "":
        return False
    for caracter in texto:
        if caracter not in DIGITOS:
            return False
    return True


def convertir_a_mayus(texto:str)->str:
    """
    Convierte letras minus a mayus.

     Parámetros:
        texto (str): texto a convertir
 
    Retorno:
        str: el mismo texto con las letras minúsculas pasadas a mayúsculas
 
    """
    resultado = ""
    for caracter in texto:
        codigo = ord(caracter)
        if 97 <= codigo <= 122:
            caracter = chr(codigo - 32)
        resultado = resultado + caracter
    return resultado


def copiar_lista(lista:list, cantidad:int)->list:
    """
    Crea una copia independiente de una lista. (lo uso en principal para ordenar por promedio)

    Parámetros:
        lista (list): lista original a copiar
        cantidad (int): cantidad de elementos a copiar
 
    Retorno:
        list: nueva lista con los mismos elementos que la original.
 
    """
    copia = [None] * cantidad
    for i in range(cantidad):
        copia[i] = lista[i]
    return copia



#VALIDACIONES

def validar_legajo(texto:str)-> bool:
    """
    Valida que el legajo sea un número entero y mayor que cero

    Parámetros:
        texto (str): legajo ingresado
 
    Retorno:
        bool: True si es un entero mayor que cero
                False en caso contrario
 
    """
    valido = False
    if es_entero(texto):
        valor = int(texto)
        valido = valor > 0
    return valido


def validar_nombre(texto:str)-> bool:
    """
    Valida que el nombre y apellido sean alfabeticos (incluyendo ñ, tildes y espacios solo entre medio).

    Parámetros:
        texto (str): apellido y nombre ingresados
 
    Retorno:
        bool: True si contiene solo letras y espacios intermedios (con al menos una letra)
              False en caso contrario.

    """
    if texto == "":
        return False
    if texto[0] == " " or texto[-1] == " ":
        return False
    es_alfabeto = False
    for caracter in texto:
        if caracter in LETRAS:
            es_alfabeto = True
        elif caracter != " ":
            return False
    return es_alfabeto


def validar_genero(texto:str)-> bool:
    """
    Valida que el género sea 'F', 'M' o 'X' (en minus o mayus).

    Parámetros:
        texto (str): género ingresado
 
    Retorno:
        bool: True si es F, M o X (sin importar mayúsculas)
                False en caso contrario
 
    """
    valido = False
    texto = convertir_a_mayus(texto)
    if texto == "F" or texto == "M" or texto == "X":
        valido = True
    return valido


def validar_nota(texto:str)-> bool:
    """
    Valida que la nota sea un entero entre 1 y 10.

    Parámetros:
        texto (str): nota ingresada
 
    Retorno:
        bool: True si es un entero entre NOTA_MINIMA y NOTA_MAXIMA
                False en caso contrario
 
    """
    valido = False
    if es_entero(texto):
        valor = int(texto)
        if NOTA_MINIMA <= valor <= NOTA_MAXIMA:
            valido = True
    return valido



#INGRESO DE DATOS

def pedir_legajo(legajos:list, posicion:int)->int:
    """
    Pide el legajo de un estudiante hasta que sea válido y no esté repetido.
    Devuelve el legajo como entero.

    Parámetros:
        legajos (list): lista de legajos (se usa para chequear repetidos)
        posicion (int): posición del estudiante que se está cargando

    Retorno:
        int: legajo válido y no repetido.

    """
    valido = False
    while not valido:
        texto = input(f"Legajo del estudiante {posicion + 1}: ")
        if not validar_legajo(texto):
            print("Error: número de legajo inválido.")
        else:
            repetido = False
            for i in range(posicion): #se compara con los ya cargados (de 0 a -1)
                if legajos[i] == int(texto):
                    repetido = True
            if repetido:
                print("Error: ese legajo ya fue cargado.")
            else:
                valido = True
    return int(texto)


def pedir_nombre(posicion:int)->str:
    """
    Pide el apellido y nombre de un estudiante hasta que sea válido.

    Parámetros:
        posicion (int): posición del estudiante que se está cargando
 
    Retorno:
        str: apellido y nombre válidos

    """
    valido = False
    while not valido:
        texto = input(f"Apellido y nombre del estudiante {posicion + 1}: ")
        if validar_nombre(texto):
            valido = True
        else:
            print("Error: solo se admiten letras y espacios.")
    return texto


def pedir_genero(posicion:int)->str:
    """
    Pide el género de un estudiante (F/M/X) y lo devuelve en mayúscula.

    Parámetros:
        posicion (int): posición del estudiante que se está cargando
 
    Retorno:
        str: género válido en mayúscula ("F", "M" o "X").

    """
    valido = False
    while not valido:
        texto = input(f"Género del estudiante {posicion + 1} (F/M/X): ")
        if validar_genero(texto):
            valido = True
        else:
            print("Error: el género debe ser F, M o X.")
    return convertir_a_mayus(texto)


def pedir_nota(posicion:int, nombre_parcial:str)->int:
    """
    Pide la nota de un parcial hasta que sea un entero entre 1 y 10.

    Parámetros:
        posicion (int): posición del estudiante que se está cargando
        nombre_parcial (str): nombre del parcial que se muestra en el mensaje
 
    Retorno:
        int: nota válida entre 1 y 10.

    """
    valido = False
    while not valido:
        texto = input(f"Nota de {nombre_parcial} del estudiante {posicion + 1} (1-10): ")
        if validar_nota(texto):
            valido = True
        else:
            print("Error: la nota debe ser un número entero entre 1 y 10.")
    return int(texto)


def cargar_estudiantes(legajos:list, nombres:list, generos:list, parcial1:list, parcial2:list)-> None:
    """
    Carga por teclado los datos completos de un estudiante a la vez (legajo, nombre, género y las dos notas) y luego pasa al siguiente.

    Parámetros:
        legajos (list): lista de legajos (se modifica)
        nombres (list): lista de apellidos y nombres (se modifica)
        generos (list): lista de géneros (se modifica)
        parcial1 (list): lista de notas del primer parcial (se modifica)
        parcial2 (list): lista de notas del segundo parcial (se modifica)
 
    Retorno:
        None: no devuelve nada, modifica las listas recibidas.

    """
    for i in range(len(legajos)):
        print()
        print(f"Estudiante {i + 1}")
        legajos[i] = pedir_legajo(legajos, i)
        nombres[i] = pedir_nombre(i)
        generos[i] = pedir_genero(i)
        parcial1[i] = pedir_nota(i, "primer parcial")
        parcial2[i] = pedir_nota(i, "segundo parcial")


def cargar_datos_prueba(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list):
    """
    Carga 30 estudiantes hardcodeados y amigables en los listados.

    Parámetros:
        legajos (list): lista de legajos (se modifica)
        nombres (list): lista de apellidos y nombres (se modifica)
        generos (list): lista de géneros (se modifica)
        parcial1 (list): lista de notas del primer parcial (se modifica)
        parcial2 (list): lista de notas del segundo parcial (se modifica)
 
    Retorno:
        None: no devuelve nada, modifica las listas recibidas.
 
    """
    l = [10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10010,
         10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019, 10020,
         10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029, 10030]
    n = ["Roth Yago", "Casal Azul", "Grande Ana", "Caserotto Martín", "Tursi Ivana",
         "Vernengo Julián", "Boson Marisa", "Adamec Joaquín", "Arias Sofia", "Scheffer Agustín",
         "Rivara Paola", "Corbo Mauricio", "Cáceres Cecilia", "Bataller Santiago", "Juarez Brenda",
         "Giaccone Maximiliano", "Miño Martina", "Fiestas Tomás", "Calduch Analía", "Folino Carlos",
         "Ramiro Malena", "Salcedo Arturo", "Conde Celeste", "Sosa Lucas", "Gimenez Camila",
         "Morales Matías", "Larocca Renata", "Manna Matías", "Argento Ian", "Cesare Martina"]
    g = ["M", "F", "F", "M", "F", "M", "F", "M", "F", "M",
         "F", "M", "F", "M", "F", "M", "F", "M", "F", "M",
         "F", "M", "F", "M", "F", "M", "F", "M", "X", "M"]
    p1 = [8, 10, 6, 7, 9, 5, 10, 4, 8, 7, 9, 6, 10, 3, 7, 8, 5, 9, 6, 7, 10, 4, 8, 6, 9, 7, 5, 8, 10, 2]
    p2 = [7, 10, 8, 9, 9, 6, 10, 5, 7, 8, 10, 7, 9, 4, 6, 8, 7, 10, 5, 6, 9, 3, 9, 7, 8, 7, 4, 9, 10, 1]
    for i in range(len(legajos)):
        legajos[i] = l[i]
        nombres[i] = n[i]
        generos[i] = g[i]
        parcial1[i] = p1[i]
        parcial2[i] = p2[i]



#CÁLCULOS IMPORTANTES

def calcular_promedio(parcial1: list, parcial2: list, promedios: list)-> None:
    """
    Calcula el promedio de cada estudiante y lo guarda en una nueva lista "promedios".

    Parámetros:
        parcial1 (list): lista de notas del primer parcial
        parcial2 (list): lista de notas del segundo parcial
        promedios (list): lista donde se guardan los promedios (se modifica)
 
    Retorno:
        None: no devuelve nada, modifica la lista promedios

    """
    for i in range(len(parcial1)):
        promedios[i] = (parcial1[i] + parcial2[i]) / 2


def buscar_maximo(lista: list) -> float:
    """
    Busca el mayor valor de una lista de numeros

    Parámetros:
        lista (list): lista de números
 
    Retorno:
        float: el mayor valor de la lista
 
    """
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo



# ORDENAR

def ordenar_estudiantes(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, orden: str) -> bool:
    """
    Ordena todas las listas por promedio (con bubble sort)

    Parámetros:
        legajos (list): lista de legajos (se modifica)
        nombres (list): lista de apellidos y nombres (se modifica)
        generos (list): lista de géneros (se modifica)
        parcial1 (list): lista de notas del primer parcial (se modifica)
        parcial2 (list): lista de notas del segundo parcial (se modifica)
        promedios (list): lista de promedios, a partir de la cual se ordena (se modifica)
        orden (str): "ASC" para ascendente o "DESC" para descendente
 
    Retorno:
        bool: True si se ordenó correctamente, False si el parámetro orden es inválido

    """

    if orden != "ASC" and orden != "DESC":
        return False

    cantidad = len(promedios)

    for i in range(cantidad - 1): #pasadas
        for j in range(cantidad - 1 - i): #comparaciones

            debe_intercambiar = False

            if orden == "ASC" and promedios[j] > promedios[j + 1]:
                debe_intercambiar = True
            elif orden == "DESC" and promedios[j] < promedios[j + 1]:
                debe_intercambiar = True

            if debe_intercambiar:
                legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                generos[j], generos[j + 1] = generos[j + 1], generos[j]
                parcial1[j], parcial1[j + 1] = parcial1[j + 1], parcial1[j]
                parcial2[j], parcial2[j + 1] = parcial2[j + 1], parcial2[j]
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]

    return True



# MOSTRAR Y RECORRER

def mostrar_estudiante(legajo: int, nombre: str, genero: str, nota1: int, nota2: int, promedio: float, mostrar_promedio: bool)-> None:
    """
    Muestra en una línea los datos de un estudiante.

    Parámetros:
        legajo (int): legajo del estudiante
        nombre (str): apellido y nombre del estudiante
        genero (str): género del estudiante ("F", "M" o "X")
        nota1 (int): nota del primer parcial
        nota2 (int): nota del segundo parcial
        promedio (float): promedio de las dos notas
        mostrar_promedio (bool): su valor determina si el promedio ya fue calculado y se debe mostrar

 
    Retorno:
        None: no devuelve nada, solo imprime por pantalla
 
    """
    if mostrar_promedio:
        print(f"{legajo:<10}{nombre:<25}{genero:<8}{nota1:<14}{nota2:<14}{promedio:.2f}") #.2f para que imprima dos decimales exactos
    else:
        print(f"{legajo:<10}{nombre:<25}{genero:<8}{nota1:<14}{nota2:<14}")
 
 
def recorrer_estudiantes(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, promedio_busqueda=None, legajo_busqueda=None, mostrar_promedio=True)-> int:
    """
    Recorre las listas e imprime un informe. Además busca un estudiante a partir de su legajo/promedio 

    Parámetros:
        legajos (list): lista de legajos
        nombres (list): lista de apellidos y nombres
        generos (list): lista de géneros
        parcial1 (list): lista de notas del primer parcial
        parcial2 (list): lista de notas del segundo parcial
        promedios (list): lista de promedios
        promedio_busqueda (float/None): si se indica, solo muestra los estudiantes con ese promedio (op5)
                                          Por defecto es None (no filtra)
        legajo_busqueda (int/None): si se indica, solo muestra el estudiante con ese legajo (op6)
                                      Por defecto es None (no filtra)
        mostrar_promedio (bool): su valor determina si los promedios ya fueron calculados y se deben mostrar

        Retorno:
        int: cantidad de estudiantes mostrados (necesario para op6)

    """
    print()
    print()
    print(f"ESTUDIANTES")
    print()
    if mostrar_promedio:
        print(f"{'LEGAJO':<10}{'APELLIDO Y NOMBRE':<25}{'GÉNERO':<8}{'1ER PARCIAL':<14}{'2DO PARCIAL':<14}PROMEDIO")
    else:
        print(f"{'LEGAJO':<10}{'APELLIDO Y NOMBRE':<25}{'GÉNERO':<8}{'1ER PARCIAL':<14}{'2DO PARCIAL':<14}")
    print()
    mostrados = 0
    for i in range(len(legajos)):
        cumple = True
        if promedio_busqueda is not None: #solo se entra si promedio_busqueda tiene valor asignado (como sucede en op5). En op2 al llamar a recorrer_estudiantes sin pasarle ningún filtro, estos dos toman su valor por defento (none), son ignorados y se salta directo al if cumple. Por eso imprime todos los estudiantes.
            if promedios[i] != promedio_busqueda:
                cumple = False
        if legajo_busqueda is not None: #solo se entra si legajo_busqueda tiene valor asignado (como sucede en op6)
            if legajos[i] != legajo_busqueda:
                cumple = False
        if cumple:
            mostrar_estudiante(legajos[i], nombres[i], generos[i], parcial1[i], parcial2[i], promedios[i], mostrar_promedio)
            mostrados = mostrados + 1

    return mostrados