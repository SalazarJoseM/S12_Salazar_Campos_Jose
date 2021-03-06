"""
Date:       2021-11-26
Authors:    Jose Magdaleno Salazar Campos
File:       T3E3_arithmetic.py
Brief:      Se tienen funciones que suman, restan, multiplican y dividen dos numeros de punto flotante.
Score:      80 (55)
Version:    0.1.1
Fixes:      - [25] PEP8 recomienda no rebasar los 99 carácteres en una
                línea de código, yo establecí en los requerimientos
                máximo 72 carácteres (aplica para comentarios también)}

            - [20] PEP8 recomienda añadir un espacio en blanco después del
                carácter de coma ','

            * La variable resultado te la puedes ahorrar en las funciones
                simplmente poniendo la operación en el return
"""


def suma(num_1, num_2):
    resultado = num_1 + num_2
    return resultado


def resta(num_1, num_2):
    resultado = num_1 - num_2
    return resultado


def multiplicacion(num_1, num_2):
    resultado = num_1 * num_2
    return resultado


def division(num_1, num_2):
    resultado = num_1 / num_2
    return resultado


if __name__ == '__main__':
    numero_1 = float(input("Ingresa un numero 1 flotante: "))
    numero_2 = float(input("Ingresa un numero 2 flotante: "))
    print("\nLa suma de los dos numeros es: " + str(round(suma(numero_1, numero_2),2)))
    print("La resta de los dos numeros es: " + str(round(resta(numero_1, numero_2),2)))
    print("La multiplicacion de los dos numeros es: " + str(round(multiplicacion(numero_1, numero_2),2)))
    print("La division de los dos numeros es: " + str(round(division(numero_1, numero_2),2)))
