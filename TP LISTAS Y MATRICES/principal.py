import biblioteca as bi

# FUNCIONES DEL MENÚ

def mostrar_menu()-> None:
    """
    Imprime las opciones del menú

        Parámetros:
        Ninguno
 
    Retorna:
        None: no devuelve nada, solo imprime por pantalla

    """
    print()
    print()
    print("GESTIÓN DE ESTUDIANTES FG")
    print("1. Cargar datos")
    print("2. Mostrar todos los estudiantes")
    print("3. Calcular promedios")
    print("4. Estudiantes ordenados por promedio (DESCENDIENTE)")
    print("5. Estudiante con mayor promedio")
    print("6. Buscar estudiante por legajo")
    print("7. Salir")


def opciones() -> int:
    """
    Pide una opción del menú y verifica que sea un entero entre 1 y 7

        Parámetros:
        Ninguno
 
    Retorna:
        int: opción válida elegida, entre 1 y 7

    """
    while True:
        texto = input("Elija una opción: ")

        if bi.es_entero(texto) and 1 <= int(texto) <= 7:
            return int(texto)

        print("Error: Ingrese un número entre 1 y 7")





# ITEMS DEL MENÚ

def op1_cargar_datos(legajos:list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list)-> bool:
    """
    Carga los datos de forma manual o con datos de prueba. Resetea los promedios x las dudas

        Parámetros:
        legajos (list): lista de legajos (se modifica)
        nombres (list): lista de apellidos y nombres (se modifica)
        generos (list): lista de géneros (se modifica)
        parcial1 (list): lista de notas del primer parcial (se modifica)
        parcial2 (list): lista de notas del segundo parcial (se modifica)
        promedios (list): lista de promedios (se reinicia en 0.0)
 
    Retorna:
        bool: True, indicando que los datos quedaron cargados.

    """
    op = ""

    while op != "M" and op != "T":
        op = bi.convertir_a_mayus(input("Carga manual (M) o datos de testeo (T): "))

        if op != "M" and op != "T":
            print("Error: ingrese M o T")

    match op:
        case "M":
            bi.cargar_estudiantes(legajos, nombres, generos, parcial1, parcial2)
        case "T":
            bi.cargar_datos_prueba(legajos, nombres, generos, parcial1, parcial2)

    for i in range(bi.CANTIDAD):
        promedios[i] = 0.0

    print("Datos cargados correctamente")
    return True


def op2_mostrar_todos(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, cargados: bool, promedios_calculados: bool)-> None:
    """
    Muestra todos los datos ingresados de los estudiantes en forma de informe
 
    Parámetros:
        legajos (list): lista de legajos
        nombres (list): lista de apellidos y nombres
        generos (list): lista de géneros
        parcial1 (list): lista de notas del primer parcial
        parcial2 (list): lista de notas del segundo parcial
        promedios (list): lista de promedios
        cargados (bool): indica si los datos ya fueron cargados
        promedios_calculados (bool): indica si los promedios ya fueron calculados (decide si se muestra la columna)
 
    Retorna:
        None: no devuelve nada, solo imprime por pantalla.
    
    """
    if not cargados:
        print("Debe cargar los datos antes!")
    else:
        bi.recorrer_estudiantes(legajos, nombres, generos, parcial1, parcial2, promedios, mostrar_promedio=promedios_calculados)


def op3_calcular_promedios(parcial1: list, parcial2: list, promedios: list, cargados: bool, promedios_calculados: bool)-> bool:
    """
    Calcula y guarda los promedios en su lista
 
    Parámetros:
        parcial1 (list): lista de notas del primer parcial.
        parcial2 (list): lista de notas del segundo parcial.
        promedios (list): lista donde se guardan los promedios (se modifica).
        cargados (bool): indica si los datos ya fueron cargados.
        promedios_calculados (bool): estado actual de los promedios (calculados o no).
 
    Retorna:
        bool: True si los promedios fueron calculados. Si no había datos cargados, devuelve el estado que recibió.

    """
    if not cargados:
        print("Debe cargar los datos antes!")
    else:
        bi.calcular_promedio(parcial1, parcial2, promedios)
        promedios_calculados = True
        print("Promedios calculados correctamente")

    return promedios_calculados


def op4_ordenados_por_promedio(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, cargados: bool, promedios_calculados: bool)-> None:
    """
    Muestra a los estudiantes ordenados por promedio (descendiente, orden alterable desde acá)

    Parámetros:
        legajos (list): lista de legajos (no se modifica, se ordena una copia).
        nombres (list): lista de apellidos y nombres (no se modifica).
        generos (list): lista de géneros (no se modifica).
        parcial1 (list): lista de notas del primer parcial (no se modifica).
        parcial2 (list): lista de notas del segundo parcial (no se modifica).
        promedios (list): lista de promedios (no se modifica).
        cargados (bool): indica si los datos ya fueron cargados.
        promedios_calculados (bool): indica si los promedios ya fueron calculados.
 
    Retorna:
        None: no devuelve nada, solo imprime por pantalla.

    """
    if not cargados:
        print("Debe cargar los datos antes!")
    elif not promedios_calculados:
        print("Debe calcular los promedios antes!")
    else:
        # Se ordena una copia para no alterar el orden de carga de las listas originales (orden de muestra en op2)
        legajos_ord = bi.copiar_lista(legajos, bi.CANTIDAD)
        nombres_ord = bi.copiar_lista(nombres, bi.CANTIDAD)
        generos_ord = bi.copiar_lista(generos, bi.CANTIDAD)
        par1_ord = bi.copiar_lista(parcial1, bi.CANTIDAD)
        par2_ord = bi.copiar_lista(parcial2, bi.CANTIDAD)
        prom_ord = bi.copiar_lista(promedios, bi.CANTIDAD)

        bi.ordenar_estudiantes(legajos_ord, nombres_ord, generos_ord, par1_ord, par2_ord, prom_ord, "DESC")

        bi.recorrer_estudiantes(legajos_ord, nombres_ord, generos_ord, par1_ord, par2_ord, prom_ord)


def op5_mayor_promedio(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, cargados: bool, promedios_calculados: bool)-> None:
    """
    Muestra el estudiante de mayor promedio
    Le paso el max calculado en buscar_maximo y se lo asigno a promedio_busqueda para que filtre en recorrer_estudiantes

    Parámetros:
        legajos (list): lista de legajos.
        nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        parcial1 (list): lista de notas del primer parcial.
        parcial2 (list): lista de notas del segundo parcial.
        promedios (list): lista de promedios.
        cargados (bool): indica si los datos ya fueron cargados.
        promedios_calculados (bool): indica si los promedios ya fueron calculados.
 
    Retorna:
        None: no devuelve nada, solo imprime por pantalla.
    
    """
    if not cargados:
        print("Debe cargar los datos antes!")
    elif not promedios_calculados:
        print("Debe calcular los promedios antes!")
    else:
        maximo = bi.buscar_maximo(promedios)
        bi.recorrer_estudiantes(legajos, nombres, generos, parcial1, parcial2, promedios, promedio_busqueda=maximo)


def op6_buscar_por_legajo(legajos: list, nombres: list, generos: list, parcial1: list, parcial2: list, promedios: list, cargados: bool, promedios_calculados: bool)-> None:
    """
    Muestra un estudiante por legajo.
    Le paso el imput de texto y se lo asigno a legajo_busqueda para que filtre en recorrer_estudiantes

    Parámetros:
        legajos (list): lista de legajos.
        nombres (list): lista de apellidos y nombres.
        generos (list): lista de géneros.
        parcial1 (list): lista de notas del primer parcial.
        parcial2 (list): lista de notas del segundo parcial.
        promedios (list): lista de promedios.
        cargados (bool): indica si los datos ya fueron cargados.
        promedios_calculados (bool): indica si los promedios ya fueron calculados (decide si se muestra la columna)
 
    Retorna:
        None: no devuelve nada, solo imprime por pantalla.
    
    """
    if not cargados:
        print("Debe cargar los datos antes!")
    else:
        texto = input("Legajo a buscar: ")

        while not bi.validar_legajo(texto):
            print("Error: el legajo debe ser un numero entero mayor a 0")
            texto = input("Legajo a buscar: ")

        encontrado = bi.recorrer_estudiantes(legajos, nombres, generos, parcial1, parcial2, promedios, legajo_busqueda=int(texto), mostrar_promedio=promedios_calculados)

        if encontrado == 0:
            print("No existe un estudiante con ese legajo")


# PROGRAMA PRINCIPAL

def programa_principal():
    """
    Crea las listas y variables de estado, y ejecuta el menú principal hasta que se elige la opción 7 (Salir)
 
    Parámetros:
        Ninguno.
 
    Retorna:
        None: no devuelve nada.
    """
    
    legajos = [0] * bi.CANTIDAD
    nombres = [""] * bi.CANTIDAD
    generos = [""] * bi.CANTIDAD
    parcial1 = [0] * bi.CANTIDAD
    parcial2 = [0] * bi.CANTIDAD
    promedios = [0.0] * bi.CANTIDAD

    cargados = False
    promedios_calculados = False

    opcion = 0

    while opcion != 7:
        mostrar_menu()
        opcion = opciones()

        match opcion:
            case 1:
                cargados = op1_cargar_datos(legajos, nombres, generos, parcial1, parcial2, promedios)
                promedios_calculados = False  # Necesario para que al recargar datos, la lista de promedios no se muestre antes de calcularlos
            case 2:
                op2_mostrar_todos(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados)
            case 3:
                promedios_calculados = op3_calcular_promedios(parcial1, parcial2, promedios, cargados, promedios_calculados)
            case 4:
                op4_ordenados_por_promedio(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados)
            case 5:
                op5_mayor_promedio(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados)
            case 6:
                op6_buscar_por_legajo(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados)
            case 7:
                print("Fin del programa. Adiós!")
