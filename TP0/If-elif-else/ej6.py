#Al ingresar una edad por input, se debe informar si la persona es mayor de edad (mayor a 17 años)
#o adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("Ingrese su edad: "))
if edad > 17:
    print("La persona es mayor de edad.")
elif edad >= 13 and edad <= 17:
    print("La persona es adolescente.")
else:
    print("La persona es un niño.")