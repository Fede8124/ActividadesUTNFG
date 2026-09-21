#Al ingresar una edad por input, solo se debe informar si la persona NO es adolescente.

edad = int(input("Ingrese su edad: "))
if edad < 13 or edad > 17:
    print("La persona NO es adolescente.")
    