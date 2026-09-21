#Ingresar dos números por input, transformarlos a entero (int).
#Luego seleccionar la opción:
#Sumar
#Restar
#Multiplicar
#Dividir (numero_uno / numero_dos)
#Mostar el resulto por consola.
#Ejemplo: "la suma es 750"

numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))

print("Seleccione una opción:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Ingrese una opción: "))

match opcion:
    case 1:
        resultado = numero_uno + numero_dos
        print(f"La suma es {resultado}")

    case 2:
        resultado = numero_uno - numero_dos
        print(f"La resta es {resultado}")

    case 3:
        resultado = numero_uno * numero_dos
        print(f"La multiplicación es {resultado}")

    case 4:
        resultado = numero_uno / numero_dos
        print(f"La división es {resultado}")

    case _:
        print("Opción inválida")