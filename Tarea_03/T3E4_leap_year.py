"""
Date: 2021-11-26
Authors: Jose Magdaleno Salazar Campos

File: T3E4_leap_year.py
Brief: Se tiene una funcion que valide si una fecha es valida.
Score:
Version: A.B.1
Fixes:
"""


def fecha(dia, mes, anio):
    # Enero
    if mes == 1 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    # Febrero
    elif mes == 2 and 1 <= anio <= 2021:
        # Verificacion de año bisiesto
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            if 1 <= dia <= 29:
                return True
            else:
                return False
        else:
            if 1 <= dia <= 28:
                return True
            else:
                return False
    # Marzo
    elif mes == 3 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    # Abril
    elif mes == 4 and 1 <= dia <= 30 and 1 <= anio <= 2021:
        return True
    # Mayo
    elif mes == 5 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    # Junio
    elif mes == 6 and 1 <= dia <= 30 and 1 <= anio <= 2021:
        return True
    # Julio
    elif mes == 7 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    # Agosto
    elif mes == 8 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    # Septiembre
    elif mes == 9 and 1 <= dia <= 30 and 1 <= anio <= 2021:
        return True
    # Octubre
    elif mes == 10 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    # Noviembre
    elif mes == 11 and 1 <= dia <= 30 and 1 <= anio <= 2021:
        return True
    # Diciembre
    elif mes == 12 and 1 <= dia <= 31 and 1 <= anio <= 2021:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(5):
        print("Intento " + str(i + 1))
        dia = int(input("Ingresa un numero de dia: (de 1 a 31) "))
        mes = int(input("Ingresa un numero de mes: (de 1 a 12) "))
        anio = int(input("Ingresa un numero de año: (de 1 a 2021) "))
        print(fecha(dia, mes, anio))
        print("\n")
