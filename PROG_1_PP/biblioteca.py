#CONSTANTES

CANTIDAD = 2
DIGITOS = "0123456789"
LETRAS = ("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ")
GENEROS = ("F", "M", "X")
NOTA_MINIMA = 1
NOTA_MAXIMA = 10



#FUNCIONES NECESARIAS

def es_entero(texto:str)->bool:
    """
    Verifica que el texto ingresado contenga números enteros positivos.

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
    Crea una copia independiente de una lista. Usarlo en main para ordenar por promedio !!
 
    """
    copia = [None] * cantidad
    for i in range(cantidad):
        copia[i] = lista[i]
    return copia


def intercambiar(lista:list, i:int, j:int)-> None: 
    """
    Intercambia los elementos de las posiciones i y j. (lo uso para ordenar por promedio)
 
    """
    auxiliar = lista[i]
    lista[i] = lista[j]
    lista[j] = auxiliar


def legajo_repetido(legajos:list, hasta:int, valor:int)-> bool:
    """
    Busca un legajo repetido entre las posiciones cargadas de la lista.
 
    """
    for i in range(hasta):
        if legajos[i] == valor:
            return True
    return False



#VALIDACIONES

def validar_legajo(texto:str)-> bool:
    """
    Valida que el legajo sea un número entero y mayor que cero.
 
    """
    valido = False
    if es_entero(texto):
        valor = int(texto)
        valido = valor > 0
    return valido


def validar_nombre(texto:str)-> bool:
    """
    Valida que el nombre y apellido sean alfabeticos (incluyendo ñ, tildes y espacios solo entre medio).
 
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
 
    """
    valido = False
    texto = convertir_a_mayus(texto)
    if texto in GENEROS:
        valido = True
    return valido


def validar_nota(texto:str)-> bool:
    """
    Valida que la nota sea un entero entre 1 y 10.
 
    """
    valido = False
    if es_entero(texto):
        valor = int(texto)
        if NOTA_MINIMA <= valor <= NOTA_MAXIMA:
            valido = True
    return valido



#CARGA DE DATOS

def cargar_legajos(legajos:list):
    """
    Carga por teclado la lista de legajos, validando que sean correctos.
 
    """
    for i in range(len(legajos)):
        valido = False
        while not valido:
            texto = input(f"Legajo del estudiante {i + 1}: ")
            if not validar_legajo(texto):
                print("Error: número de legajo inválido.")
            elif legajo_repetido(legajos, i, int(texto)):
                print("Error: ese legajo ya fue cargado.")
            else:
                legajos[i] = int(texto)
                valido = True


def cargar_nombres(nombres:list):
    """
    Carga por teclado la lista de nombres y apellidos, validando que sean alfabéticos.
 
    """
    for i in range(len(nombres)):
        valido = False
        while not valido:
            texto = input(f"Apellido y nombre del estudiante {i + 1}: ")
            if validar_nombre(texto):
                nombres[i] = texto
                valido = True
            else:
                print("Error: solo se admiten letras y espacios.")


def cargar_generos(generos:list):
    """
    Carga por teclado la lista de géneros, validando F, M o X.
 
    """
    for i in range(len(generos)):
        valido = False
        while not valido:
            texto = input(f"Género del estudiante {i + 1} (F/M/X): ")
            if validar_genero(texto):
                generos[i] = convertir_a_mayus(texto)
                valido = True
            else:
                print("Error: el género debe ser F, M o X.")


def cargar_notas(notas:list, nombre_parcial:str):
    """
    Carga por teclado un listado de notas, validando que lo ingresado sean números enteros entre 1 y 10.
    Sirve para ambos parciales
 
    """
    for i in range(len(notas)):
        valido = False
        while not valido:
            texto = input(f"Nota de {nombre_parcial} del estudiante {i + 1} (1-10): ")
            if validar_nota(texto):
                notas[i] = int(texto)
                valido = True
            else:
                print("Error: la nota debe ser un número entero entre 1 y 10.")


def cargar_datos_prueba(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list):
    """
    Carga 30 estudiantes hardcodeados y amigables en los listados.
 
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

    """
    for i in range(len(parcial1)):
        promedios[i] = (parcial1[i] + parcial2[i]) / 2


def buscar_maximo(lista: list) -> float:
    """
    Busca el mayor valor de una lista de numeros.
 
    """
    maximo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo



# ORDENAR

def ordenar_estudiantes(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, orden: str)-> bool:
    """
    Ordena todas las listas por promedio (con bubble sort).
    
    """
    if orden != "ASC" and orden != "DESC":
        return False
    cantidad = len(promedios)
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if orden == "ASC" and promedios[j] > promedios[j + 1]:
                intercambiar(legajos, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(generos, j, j + 1)
                intercambiar(parcial1, j, j + 1)
                intercambiar(parcial2, j, j + 1)
                intercambiar(promedios, j, j + 1)
            elif orden == "DESC" and promedios[j] < promedios[j + 1]:
                intercambiar(legajos, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(generos, j, j + 1)
                intercambiar(parcial1, j, j + 1)
                intercambiar(parcial2, j, j + 1)
                intercambiar(promedios, j, j + 1)
    return True



# MOSTRAR Y RECORRER

def mostrar_estudiante(legajo: int, nombre: str, genero: str, nota1: int, nota2: int, promedio: float)-> None:
    """
    Muestra en una línea los datos de un estudiante.
 
    """
    print(f"{legajo}  {nombre}  {genero}  {nota1}  {nota2}  {promedio:.2f}") #.2f para que imprima dos decimales exactos
 
 
def recorrer_estudiantes(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, promedio_busqueda=None, legajo_busqueda=None):
    """
    Recorre las listas e imprime un informe. Además busca un estudiante a partir de su legajo/promedio 

    """
    print()
    print(f"ESTUDIANTES")
    print()
    print(f"LEGAJO  APELLIDO Y NOMBRE  GÉNERO  1ER PARCIAL  2DO PARCIAL  PROMEDIO")
    print()
    mostrados = 0
    for i in range(len(legajos)):
        cumple = True
        if promedio_busqueda is not None:
            if promedios[i] != promedio_busqueda:
                cumple = False
        if legajo_busqueda is not None:
            if legajos[i] != legajo_busqueda:
                cumple = False
        if cumple:
            mostrar_estudiante(legajos[i], nombres[i], generos[i], parcial1[i], parcial2[i], promedios[i])
            mostrados = mostrados + 1
    print()
    return mostrados