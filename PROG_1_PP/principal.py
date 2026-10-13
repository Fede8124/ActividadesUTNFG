import biblioteca as bi

# FUNCIONES DEL MENÚ

def mostrar_menu():
    """
    Imprime las opciones del menú
    """
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
    """
    while True:
        texto = input("Elija una opción: ")

        if bi.es_entero(texto) and 1 <= int(texto) <= 7:
            return int(texto)

        print("Error: Ingrese un número entre 1 y 7")


def datos_cargados(cargados):
    """
    Verifica que los datos hayan sido cargados
    """
    if not cargados:
        print("Debe cargar los datos antes!")

    return cargados


def verificar_promedios(promedios_calculados):
    """
    Verifica que los promedios hayan sido calculados
    """
    if not promedios_calculados:
        print("Debe calcular los promedios antes!")

    return promedios_calculados


# ITEMS DEL MENÚ

def op1_cargar_datos(legajos, nombres, generos, parcial1, parcial2, promedios):
    """
    Carga los datos de forma manual o con datos de prueba. Resetea los promedios x las dudas

    """
    op = ""

    while op != "M" and op != "T":
        op = bi.convertir_a_mayus(input("Carga manual (M) o datos de testeo (T): "))

        if op != "M" and op != "T":
            print("Error: ingrese M o T")

    match op:
        case "M":
            bi.cargar_legajos(legajos)
            bi.cargar_nombres(nombres)
            bi.cargar_generos(generos)
            bi.cargar_notas(parcial1, "primer parcial")
            bi.cargar_notas(parcial2, "segundo parcial")
        case "T":
            bi.cargar_datos_prueba(legajos, nombres, generos, parcial1, parcial2)

    for i in range(bi.CANTIDAD):
        promedios[i] = 0.0

    print("Datos cargados correctamente")
    return True


def op2_mostrar_todos(legajos, nombres, generos, parcial1, parcial2, promedios, cargados):
    """
    Muestra todos los datos ingresados de los estudiantes en forma de informe
    
    """
    if datos_cargados(cargados):
        bi.recorrer_estudiantes(legajos, nombres, generos, parcial1, parcial2, promedios)


def op3_calcular_promedios(parcial1, parcial2, promedios, cargados, promedios_calculados):
    """
    Calcula y guarda los promedios en su lista

    """
    if datos_cargados(cargados):
        bi.calcular_promedio(parcial1, parcial2, promedios)
        promedios_calculados = True
        print("Promedios calculados correctamente")

    return promedios_calculados


def op4_ordenados_por_promedio(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados):
    """
    Muestra a los estudiantes ordenados por promedio (descendiente, orden alterable desde acá)

    """
    if datos_cargados(cargados) and verificar_promedios(promedios_calculados):

        legajos_ord = bi.copiar_lista(legajos, bi.CANTIDAD)
        nombres_ord = bi.copiar_lista(nombres, bi.CANTIDAD)
        generos_ord = bi.copiar_lista(generos, bi.CANTIDAD)
        par1_ord = bi.copiar_lista(parcial1, bi.CANTIDAD)
        par2_ord = bi.copiar_lista(parcial2, bi.CANTIDAD)
        prom_ord = bi.copiar_lista(promedios, bi.CANTIDAD)

        bi.ordenar_estudiantes(legajos_ord, nombres_ord, generos_ord, par1_ord, par2_ord, prom_ord, "DESC")

        bi.recorrer_estudiantes(legajos_ord, nombres_ord, generos_ord, par1_ord, par2_ord, prom_ord)


def op5_mayor_promedio(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados):
    """
    Muestra el estudiante de mayor promedio
    Le paso el max calculado en buscar_maximo y se lo asigno a promedio_busqueda para que filtre en recorrer_estudiantes
    
    """
    if datos_cargados(cargados) and verificar_promedios(promedios_calculados):

        maximo = bi.buscar_maximo(promedios)

        bi.recorrer_estudiantes(legajos, nombres, generos, parcial1, parcial2, promedios, promedio_busqueda=maximo)


def op6_buscar_por_legajo(legajos, nombres, generos, parcial1, parcial2, promedios, cargados):
    """
    Muestra un estudiante por legajo.
    Le paso el imput de texto y se lo asigno a legajo_busqueda para que filtre en recorrer_estudiantes
    
    """
    if datos_cargados(cargados):

        texto = input("Legajo a buscar: ")

        while not bi.validar_legajo(texto):
            print("Error: el legajo debe ser un numero entero mayor a 0")
            texto = input("Legajo a buscar: ")

        encontrado = bi.recorrer_estudiantes(legajos, nombres, generos, parcial1, parcial2, promedios, legajo_busqueda=int(texto))

        if encontrado == 0:
            print("No existe un estudiante con ese legajo")


# PROGRAMA PRINCIPAL

# Creo e inicializo las listas y variables de estado

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
        case 2:
            op2_mostrar_todos(legajos, nombres, generos, parcial1, parcial2, promedios, cargados)
        case 3:
            promedios_calculados = op3_calcular_promedios(parcial1, parcial2, promedios, cargados, promedios_calculados)
        case 4:
            op4_ordenados_por_promedio(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados)
        case 5:
            op5_mayor_promedio(legajos, nombres, generos, parcial1, parcial2, promedios, cargados, promedios_calculados)
        case 6:
            op6_buscar_por_legajo(legajos, nombres, generos, parcial1, parcial2, promedios, cargados)
        case 7:
            print("Fin del programa. Adiós!")
