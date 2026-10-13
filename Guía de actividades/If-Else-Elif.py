# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar
# la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

Altura = int(input("Ingrese la altura del jugador en centímetros: "))
if Altura < 160:
    print("La posición del jugador es: Base")
