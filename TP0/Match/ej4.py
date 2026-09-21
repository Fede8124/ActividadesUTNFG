#Ingresar un mes por input e informar:
#Si tiene 28 días.
#Si tiene 30 días.
#Si tiene 31 días.
#30 dias: abril, junio, septiembre, noviembre
#31 dias: enero, marzo, mayo, julio, agosto, octubre, diciembre
#28 dias: febrero

mes = input("Ingrese un mes: ")

match mes:
    case "Febrero":
        print("Tiene 28 días.")

    case "Abril" | "Junio" | "Septiembre" | "Noviembre":
        print("Tiene 30 días.")

    case "Enero" | "Marzo" | "Mayo" | "Julio" | "Agosto" | "Octubre" | "Diciembre":
        print("Tiene 31 días.")

#como contemplo todos los meses posibles, no hace falta un case _
