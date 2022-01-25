"""
Date:       2021-11-21
Authors:    Jose Magdaleno Salazar Campos
File:       T3E1_return_test.py
Brief:      La funcion pide un numero y regresa un string con el numero introducido.
Score:      95
Version:    1.1.1
Fixes:      - [5] PEP8 recomienda no rebasar los 99 carácteres en una
                línea de código, yo establecí en los requerimientos
                máximo 72 carácteres (aplica para comentarios también)
"""


def imprimir_numero():
    numero = float(input("Ingresa un numero: "))
    numero_intro = "El numero introducido fue " + str(numero)
    return numero_intro


if __name__ == '__main__':
    print(imprimir_numero())
